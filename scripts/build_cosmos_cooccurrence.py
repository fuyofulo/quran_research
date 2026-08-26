#!/usr/bin/env python3
"""Structural pre-cut for the cosmos / extraterrestrial-life investigation.

Deterministic answers to four questions, so no agent guesses:
  1. THE PRONOUN AUDIT. The Quran has parallel "He scattered creatures" verses.
     Some use a singular pronoun (the earth), one uses the DUAL (heavens and earth).
     Which is which, verified from the morphology segments.
  2. THE HUMAN-LOCATION AUDIT. Every occurrence of the human-words (`Ans`/insan+ins,
     `b$r`/bashar, `nws`/nas) — is any of them ever located anywhere but the earth?
  3. WHAT CO-OCCURS WITH `samAwAt` (the plural heavens) — is it ever paired with
     human-words, or only with angels, jinn, dabba and cosmic furniture?
  4. Translator divergence over the verse set.

Outputs data/structural/cosmos-cooccurrence.json
"""
import json, itertools
from collections import defaultdict, Counter
from pathlib import Path

DISPERSAL = [(42,29),(31,10),(2,164),(45,4)]
HUMAN_ROOTS = ['Ans','b$r','nws']
LIFE_ROOTS  = ['dbb','Hyy','xlq','rwH','nfs']
COSMOS_ROOTS= ['smw','ArD','njm','kwkb','qmr','$ms','brj','flk','sbE','Erj','sxr']
BEING_ROOTS = ['jnn','mlk','Ans','b$r','nws','dbb']
VERSES = [(42,29),(31,10),(2,164),(45,4),(65,12),(2,29),(67,3),(41,12),(17,44),(6,38),
          (55,33),(51,47),(21,30),(13,15),(22,18),(16,49),(19,93),(27,82),(24,45),(72,1)]
TRANSLATIONS = ['saheeh','khattab','arberry','pickthall']


def tokens(s):
    return {w.strip('.,;:!?"\'()[]').lower() for w in s.split() if len(w) > 3}


def main():
    root = Path(__file__).resolve().parent.parent
    words = []
    with open(root / 'data/morphology/words.jsonl') as f:
        for line in f:
            words.append(json.loads(line))

    ayah_roots = defaultdict(set)
    for w in words:
        r = w.get('root')
        if r:
            ayah_roots[tuple(w['location'][:2])].add(r)

    # ---- 1. The pronoun audit on the dispersal verses ----
    pronoun_audit = {}
    for (su, ay) in DISPERSAL:
        rec = []
        for w in words:
            if tuple(w['location'][:2]) != (su, ay):
                continue
            for sg in w.get('segments', []):
                p = sg.get('features', {}).get('PRON')
                if p:
                    rec.append({'form': w['form_arabic'], 'pron': p})
        has_dabba = 'dbb' in ayah_roots[(su, ay)]
        pronoun_audit[f'{su}:{ay}'] = {
            'contains_dabba': has_dabba,
            'pronouns_in_verse': rec,
            'dual_present': any(x['pron'] == '3D' for x in rec),
        }

    # ---- 2. Human-location audit: which ayahs contain a human-word AND a heaven-word ----
    human_ayahs = {loc for loc, rs in ayah_roots.items() if rs & set(HUMAN_ROOTS)}
    heaven_ayahs = {loc for loc, rs in ayah_roots.items() if 'smw' in rs}
    both = sorted(human_ayahs & heaven_ayahs)
    print(f'  human-word ayahs: {len(human_ayahs)}; heaven-word ayahs: {len(heaven_ayahs)}; '
          f'both: {len(both)}')

    # ---- 3. What shares an ayah with samAwAt, ranked ----
    smw_neighbours = Counter()
    for loc in heaven_ayahs:
        for r in ayah_roots[loc]:
            if r != 'smw':
                smw_neighbours[r] += 1

    # Which BEING-roots co-occur with the plural heavens, and how often
    beings_with_heavens = {}
    for b in BEING_ROOTS:
        b_ayahs = {loc for loc, rs in ayah_roots.items() if b in rs}
        tog = b_ayahs & heaven_ayahs
        beings_with_heavens[b] = {
            'total_ayahs': len(b_ayahs),
            'with_heavens': len(tog),
            'share': round(len(tog) / len(b_ayahs), 4) if b_ayahs else 0.0,
            'refs': sorted(f'{a}:{b_}' for a, b_ in tog)[:60],
        }

    # ---- 4. Divergence ----
    tr = {t: json.load(open(root / f'data/translations/{t}.json'))['ayahs'] for t in TRANSLATIONS}
    divergence = []
    for (su, ay) in VERSES:
        key = f'{su}:{ay}'
        texts = [tr[t].get(key, '') for t in TRANSLATIONS]
        if not all(texts):
            continue
        sets = [tokens(x) for x in texts]
        sims = [len(a & b) / len(a | b) if (a | b) else 1.0 for a, b in itertools.combinations(sets, 2)]
        divergence.append({'ref': key, 'divergence': round(1 - sum(sims) / len(sims), 4)})
    divergence.sort(key=lambda d: -d['divergence'])

    out = {
        'note': 'Deterministic pre-cut for the cosmos investigation. The pronoun audit is the '
                'load-bearing item: 42:29 uses the DUAL fihima (heavens AND earth) where the '
                'parallel verses 2:164 and 31:10 use the singular fiha (the earth alone).',
        'pronoun_audit_on_dispersal_verses': pronoun_audit,
        'human_and_heaven_shared_ayahs': [f'{a}:{b}' for a, b in both],
        'being_roots_vs_plural_heavens': beings_with_heavens,
        'roots_sharing_an_ayah_with_samawat_top40': smw_neighbours.most_common(40),
        'translation_divergence': divergence,
    }
    dest = root / 'data/structural/cosmos-cooccurrence.json'
    json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
    print(f'wrote {dest}')
    print('  DISPERSAL PRONOUNS:')
    for k, v in pronoun_audit.items():
        print(f"    {k:8s} dabba={v['contains_dabba']}  DUAL={v['dual_present']}")
    print('  BEINGS vs PLURAL HEAVENS:')
    for b, d in sorted(beings_with_heavens.items(), key=lambda kv: -kv[1]['share']):
        print(f"    {b:5s} {d['with_heavens']:3d}/{d['total_ayahs']:3d} = {d['share']:.1%}")
    print(f"  top divergence: {[d['ref'] for d in divergence[:6]]}")


if __name__ == '__main__':
    main()
