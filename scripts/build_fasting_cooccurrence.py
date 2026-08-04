#!/usr/bin/env python3
"""Co-occurrence + divergence pre-cut for the fasting investigation.

Two questions this answers deterministically, so no agent has to guess:
  1. What company does Swm (صوم) keep? Which roots share an ayah with it, and
     which roots share the SURAH-passage neighbourhood (2:183-187 etc.)?
  2. Where do the four translators disagree most across the fasting verse set?
     Divergence marks the places where the Arabic resists English.

Outputs data/structural/fasting-cooccurrence.json
"""
import json, sys, itertools
from collections import defaultdict, Counter
from pathlib import Path

# Buckwalter, case-sensitive. Swm = صوم (fast); NOT swm = سوم.
FASTING_ROOTS = [
    'Swm',   # fast
    'wqy',   # taqwa - the stated purpose (2:183)
    'Sbr',   # patience/endurance - the adjacent discipline
    '$hr',   # month
    'Edd',   # numbered days
    'ysr',   # ease (2:185)
    'Esr',   # hardship (2:185)
    'TEm',   # feeding (the alternative to fasting)
    'fdy',   # ransom/redemption
    'rqb',   # neck = freeing a slave (expiation ladder)
    'kfr',   # kaffara = expiation (and disbelief - polysemous, watch it)
    'Ekf',   # i'tikaf - retreat in the mosque
    'rfv',   # rafath - sexual approach (2:187, 2:197)
    'xyT',   # thread (the white/black thread of dawn)
    'qdr',   # laylat al-qadr
    'hll',   # new moons / what is consecrated
    'mrD',   # illness (the exemption)
    'sfr',   # travel (the exemption)
    'Akl',   # eating
    'lyl',   # night
    'fjr',   # dawn
    'Slw',   # prayer
    'zkw',   # purification/zakat
    'dEw',   # supplication (2:186 sits INSIDE the fasting passage)
    'qrb',   # nearness
    'Hmd', 'skn', 'Efw', 'gfr',
]

# The verse set the investigation actually cares about.
FASTING_VERSES = [
    (2,183),(2,184),(2,185),(2,186),(2,187),(2,196),(2,197),
    (4,92),(5,89),(5,95),(58,3),(58,4),
    (19,26),(33,35),(97,1),(97,2),(97,3),(97,4),(97,5),(2,177),(2,189),
]
TRANSLATIONS = ['saheeh','khattab','arberry','pickthall']


def tokens(s):
    return {w.strip('.,;:!?"\'()[]').lower() for w in s.split() if len(w) > 3}


def main():
    root = Path(__file__).resolve().parent.parent
    ayah_roots = defaultdict(set)
    root_totals = Counter()
    with open(root / 'data/morphology/words.jsonl') as f:
        for line in f:
            w = json.loads(line)
            r = w.get('root')
            if not r:
                continue
            loc = tuple(w['location'])[:2]
            ayah_roots[loc].add(r)
            if r in FASTING_ROOTS:
                root_totals[r] += 1

    # ---- 1. Ayah-level co-occurrence within the fasting vocabulary ----
    pair = Counter()
    for loc, roots in ayah_roots.items():
        present = sorted(roots & set(FASTING_ROOTS))
        for a, b in itertools.combinations(present, 2):
            pair[(a, b)] += 1

    # ---- 2. Everything that shares an ayah with Swm ----
    swm_ayahs = [loc for loc, rs in ayah_roots.items() if 'Swm' in rs]
    swm_neighbours = Counter()
    for loc in swm_ayahs:
        for r in ayah_roots[loc]:
            if r != 'Swm':
                swm_neighbours[r] += 1

    # ---- 3. The 2:183-187 passage as a closed neighbourhood ----
    passage = [(2, a) for a in range(183, 188)]
    passage_roots = Counter()
    for loc in passage:
        for r in ayah_roots.get(loc, ()):
            passage_roots[r] += 1

    # ---- 4. Translation divergence over the fasting verse set ----
    tr = {}
    for t in TRANSLATIONS:
        tr[t] = json.load(open(root / f'data/translations/{t}.json'))['ayahs']
    divergence = []
    for (su, ay) in FASTING_VERSES:
        key = f'{su}:{ay}'
        texts = [tr[t].get(key, '') for t in TRANSLATIONS]
        if not all(texts):
            continue
        sets = [tokens(x) for x in texts]
        sims = []
        for a, b in itertools.combinations(sets, 2):
            union = a | b
            sims.append(len(a & b) / len(union) if union else 1.0)
        divergence.append({
            'ref': key,
            'mean_jaccard': round(sum(sims) / len(sims), 4),
            'divergence': round(1 - sum(sims) / len(sims), 4),
            'lengths': {t: len(x.split()) for t, x in zip(TRANSLATIONS, texts)},
        })
    divergence.sort(key=lambda d: -d['divergence'])

    out = {
        'note': 'Deterministic pre-cut for the fasting investigation. '
                'Swm = صوم (case-sensitive; swm = سوم is a different root).',
        'root_totals': dict(root_totals.most_common()),
        'swm_ayahs': [f'{s}:{a}' for s, a in sorted(swm_ayahs)],
        'roots_sharing_an_ayah_with_Swm': swm_neighbours.most_common(40),
        'roots_in_passage_2_183_187': passage_roots.most_common(60),
        'fasting_vocabulary_pairs': [
            {'pair': f'{a}+{b}', 'ayahs_together': n}
            for (a, b), n in pair.most_common(40)
        ],
        'translation_divergence': divergence,
    }
    dest = root / 'data/structural/fasting-cooccurrence.json'
    json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
    print(f'wrote {dest}')
    print(f'  Swm ayahs: {len(swm_ayahs)}')
    print(f'  highest-divergence fasting verses: '
          f'{[d["ref"] for d in divergence[:6]]}')


if __name__ == '__main__':
    main()
