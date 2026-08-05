#!/usr/bin/env python3
"""Structural pre-cut for the tahajjud / night-worship investigation.

Answers deterministically, so no agent guesses:
  1. What does `lyl` (night) actually keep company with across its 92 occurrences?
     Which roots are night-attached and which never touch it?
  2. Which worship-verbs are commanded AT night vs anywhere?
  3. Where do the four translators diverge across the night-worship verse set?
  4. The hapax census — how much of this vocabulary occurs exactly once?

Outputs data/structural/tahajjud-cooccurrence.json
"""
import json, itertools
from collections import defaultdict, Counter
from pathlib import Path

NIGHT_ROOTS = [
    'hjd',   # tahajjud - ONE occurrence, 17:79
    'lyl',   # night
    'sbH',   # glorify (NOT SbH = morning)
    '*kr',   # remember
    'dEw',   # call / supplicate
    'sjd',   # prostrate
    'qwm',   # stand
    'Slw',   # prayer
    'qnt',   # devoutly obedient
    'tlw',   # recite
    'rtl',   # measured recitation
    'gfr',   # forgiveness / istighfar
    'hjE',   # sleep lightly - ONE occurrence, 51:17
    'nwm',   # sleep
    'DjE',   # beds
    'rqd',   # sleep
    'n$A',   # nashi'at al-layl
    'wTA',   # ashaddu wat'an
    'Any',   # ana' al-layl
    'zlf',   # zulafan mina al-layl
    'sHr',   # ashar (pre-dawn) - POLYSEMOUS with sihr (magic); disambiguate by lemma
    'fjr',   # dawn
    'njm',   # stars
    'dlk',   # duluk (sun's decline) - ONE occurrence
    'Hmd',   # maqam mahmud
    'nfl',   # nafila
    'xwf', 'TmE',   # fear and hope (32:16)
    'jnb',   # sides
    'qll',   # little
    'ASl', 'bkr',   # evening and morning
    'Swm',   # fasting - for the comparison
    'wqy',   # taqwa - for the comparison
]

# The verse set the investigation cares about, for divergence scoring.
NIGHT_VERSES = [
    (17,78),(17,79),(73,1),(73,2),(73,3),(73,4),(73,5),(73,6),(73,7),(73,8),(73,20),
    (51,15),(51,16),(51,17),(51,18),(32,15),(32,16),(32,17),(39,9),(3,113),(3,17),
    (25,64),(76,25),(76,26),(50,39),(50,40),(52,48),(52,49),(11,114),(20,130),(40,55),
    (26,218),(26,219),(96,19),(13,28),(2,186),(30,23),(39,42),(89,4),(93,2),(97,1),
]
TRANSLATIONS = ['saheeh','khattab','arberry','pickthall']


def tokens(s):
    return {w.strip('.,;:!?"\'()[]').lower() for w in s.split() if len(w) > 3}


def main():
    root = Path(__file__).resolve().parent.parent
    ayah_roots = defaultdict(set)
    ayah_lemmas = defaultdict(set)
    root_totals = Counter()
    lemma_locs = defaultdict(list)

    with open(root / 'data/morphology/words.jsonl') as f:
        for line in f:
            w = json.loads(line)
            r = w.get('root')
            if not r:
                continue
            loc = tuple(w['location'])[:2]
            ayah_roots[loc].add(r)
            ayah_lemmas[loc].add(w.get('lemma'))
            if r in NIGHT_ROOTS:
                root_totals[r] += 1
                lemma_locs[(r, w.get('lemma'))].append(f'{loc[0]}:{loc[1]}')

    # ---- 1. Everything sharing an ayah with lyl (night) ----
    lyl_ayahs = sorted(loc for loc, rs in ayah_roots.items() if 'lyl' in rs)
    lyl_neighbours = Counter()
    for loc in lyl_ayahs:
        for r in ayah_roots[loc]:
            if r != 'lyl':
                lyl_neighbours[r] += 1

    # ---- 2. Which worship roots co-occur with night, and how often ----
    WORSHIP = ['Slw','sbH','*kr','sjd','qwm','dEw','tlw','qnt','gfr','Swm','rtl','nfl']
    worship_vs_night = {}
    for w in WORSHIP:
        w_ayahs = {loc for loc, rs in ayah_roots.items() if w in rs}
        together = len(w_ayahs & set(lyl_ayahs))
        worship_vs_night[w] = {
            'total_ayahs': len(w_ayahs),
            'ayahs_with_night': together,
            'share_of_root_with_night': round(together / len(w_ayahs), 4) if w_ayahs else 0.0,
            'refs_with_night': sorted(f'{a}:{b}' for a, b in (w_ayahs & set(lyl_ayahs))),
        }

    # ---- 3. Hapax census across the night vocabulary ----
    hapaxes = {f'{r}/{lem}': locs[0] for (r, lem), locs in lemma_locs.items() if len(locs) == 1}

    # ---- 4. Pairwise co-occurrence inside the night vocabulary ----
    pair = Counter()
    for loc, roots in ayah_roots.items():
        present = sorted(roots & set(NIGHT_ROOTS))
        for a, b in itertools.combinations(present, 2):
            pair[(a, b)] += 1

    # ---- 5. Translator divergence ----
    tr = {t: json.load(open(root / f'data/translations/{t}.json'))['ayahs'] for t in TRANSLATIONS}
    divergence = []
    for (su, ay) in NIGHT_VERSES:
        key = f'{su}:{ay}'
        texts = [tr[t].get(key, '') for t in TRANSLATIONS]
        if not all(texts):
            continue
        sets = [tokens(x) for x in texts]
        sims = []
        for a, b in itertools.combinations(sets, 2):
            u = a | b
            sims.append(len(a & b) / len(u) if u else 1.0)
        divergence.append({'ref': key,
                           'divergence': round(1 - sum(sims) / len(sims), 4),
                           'lengths': {t: len(x.split()) for t, x in zip(TRANSLATIONS, texts)}})
    divergence.sort(key=lambda d: -d['divergence'])

    out = {
        'note': 'Deterministic pre-cut for the tahajjud investigation. sbH=سبح (glorify) is a '
                'DIFFERENT root from SbH=صبح (morning); sHr=سحر carries BOTH sihr (magic) and '
                'sahar (pre-dawn) — disambiguate by lemma, never by root alone.',
        'root_totals': dict(root_totals.most_common()),
        'lyl_ayah_count': len(lyl_ayahs),
        'roots_sharing_an_ayah_with_lyl': lyl_neighbours.most_common(50),
        'worship_roots_vs_night': worship_vs_night,
        'hapaxes_in_night_vocabulary': hapaxes,
        'night_vocabulary_pairs': [{'pair': f'{a}+{b}', 'ayahs_together': n}
                                   for (a, b), n in pair.most_common(45)],
        'translation_divergence': divergence,
    }
    dest = root / 'data/structural/tahajjud-cooccurrence.json'
    json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
    print(f'wrote {dest}')
    print(f"  lyl ayahs: {len(lyl_ayahs)}")
    print(f"  hapaxes in night vocabulary: {len(hapaxes)}")
    print("  worship-root share occurring WITH night:")
    for w, d in sorted(worship_vs_night.items(), key=lambda kv: -kv[1]['share_of_root_with_night']):
        print(f"    {w:5s} {d['ayahs_with_night']:3d}/{d['total_ayahs']:3d} = {d['share_of_root_with_night']:.1%}")
    print(f"  highest-divergence: {[d['ref'] for d in divergence[:6]]}")


if __name__ == '__main__':
    main()
