#!/usr/bin/env python3
"""
Build co-occurrence matrix + translation-divergence catalog for 49 afterlife-vocabulary roots.
Mirrors methodology of failure-cooccurrence.py and success-cooccurrence.py.

Outputs to: data/structural/afterlife-cooccurrence.json

Afterlife roots (Buckwalter, case-sensitive):
  mwt, wfy, qbr, mlk, qwm, HSr, jmE, bEv, n$r, $qq, rkm, Hsb, jzy, Hkm, qDy, gfr, fSl, ktb, wzn, $fE, ErD, jnn, nEm, rDw, wEd, nwr, E*b, jHm, sEr, lZy, hwy, HTm, Hmm, gsq, zqm, zbn, glq, sjr, $ml, $hd, ymn, sbq, qrb, Hwr, wld, Hrr, Tyb, jry, zlf
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

AFTERLIFE_ROOTS = ['mwt', 'wfy', 'qbr', 'mlk', 'qwm', 'HSr', 'jmE', 'bEv', 'n$r', '$qq', 'rkm', 'Hsb', 'jzy', 'Hkm', 'qDy', 'gfr', 'fSl', 'ktb', 'wzn', '$fE', 'ErD', 'jnn', 'nEm', 'rDw', 'wEd', 'nwr', 'E*b', 'jHm', 'sEr', 'lZy', 'hwy', 'HTm', 'Hmm', 'gsq', 'zqm', 'zbn', 'glq', 'sjr', '$ml', '$hd', 'ymn', 'sbq', 'qrb', 'Hwr', 'wld', 'Hrr', 'Tyb', 'jry', 'zlf']

def build_cooccurrence_matrix():
    """
    Load words.jsonl, group by (surah, ayah), identify which afterlife roots appear in each ayah.
    Build NxN co-occurrence matrix.
    """

    print("[1/5] Loading words.jsonl...", file=sys.stderr)

    # Map (surah, ayah) -> set of roots that appear in it
    ayah_roots = defaultdict(set)
    root_totals = defaultdict(int)
    root_meccan = defaultdict(int)

    with open('data/morphology/words.jsonl', 'r') as f:
        for line in f:
            word = json.loads(line)
            root = word.get('root')
            if root in AFTERLIFE_ROOTS:
                location = tuple(word['location'])[:2]  # (surah, ayah)
                ayah_roots[location].add(root)
                root_totals[root] += 1

                # Track Meccan vs Medinan
                if word.get('flags') and 'M' in word['flags']:
                    root_meccan[root] += 1

    print(f"   Found {len(ayah_roots)} ayahs containing afterlife roots", file=sys.stderr)

    # Initialize NxN matrix
    root_list = sorted(AFTERLIFE_ROOTS)
    n = len(root_list)
    cooccurrence = [[0] * n for _ in range(n)]

    # Fill matrix
    print("[2/5] Building co-occurrence matrix...", file=sys.stderr)
    for ayah, roots in ayah_roots.items():
        roots_list = [r for r in roots if r in AFTERLIFE_ROOTS]
        for i, r1 in enumerate(roots_list):
            for j, r2 in enumerate(roots_list):
                if i <= j:
                    idx1 = root_list.index(r1)
                    idx2 = root_list.index(r2)
                    cooccurrence[idx1][idx2] += 1
                    if i != j:  # symmetric
                        cooccurrence[idx2][idx1] += 1

    # Build lift matrix (association strength)
    print("[3/5] Computing lift scores...", file=sys.stderr)
    lift = [[0.0] * n for _ in range(n)]

    total_ayahs = len(ayah_roots)
    for i in range(n):
        for j in range(n):
            co = cooccurrence[i][j]
            if co == 0:
                lift[i][j] = 0.0
            else:
                # Lift = P(A and B) / (P(A) * P(B))
                # Using ayah frequencies: P(root_i) = root_totals[root_list[i]] / total_ayahs
                p_a = root_totals[root_list[i]] / total_ayahs
                p_b = root_totals[root_list[j]] / total_ayahs
                p_ab = co / total_ayahs

                if p_a > 0 and p_b > 0:
                    lift[i][j] = p_ab / (p_a * p_b)
                else:
                    lift[i][j] = 0.0

    # Top 25 pairs by co-occurrence count
    print("[4/5] Extracting top pairings...", file=sys.stderr)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if cooccurrence[i][j] > 0:
                pairs.append({
                    'root_1': root_list[i],
                    'root_2': root_list[j],
                    'cooccurrence': cooccurrence[i][j],
                    'lift': round(lift[i][j], 2)
                })

    pairs.sort(key=lambda x: (-x['cooccurrence'], -x['lift']))
    top_pairs = pairs[:25]

    # Weak/zero pairs (top 10 zero co-occurrences sorted by what would be expected)
    weak_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if cooccurrence[i][j] == 0:
                p_a = root_totals[root_list[i]] / total_ayahs
                p_b = root_totals[root_list[j]] / total_ayahs
                expected = p_a * p_b * total_ayahs
                weak_pairs.append({
                    'root_1': root_list[i],
                    'root_2': root_list[j],
                    'cooccurrence': 0,
                    'expected': round(expected, 2)
                })

    weak_pairs.sort(key=lambda x: -x['expected'])
    weak_pairs = weak_pairs[:10]

    # Per-root neighbors (top 3 by count)
    per_root_neighbors = {}
    for i, root in enumerate(root_list):
        neighbors = []
        for j, other_root in enumerate(root_list):
            if i != j and cooccurrence[i][j] > 0:
                neighbors.append({
                    'root': other_root,
                    'cooccurrence': cooccurrence[i][j]
                })
        neighbors.sort(key=lambda x: -x['cooccurrence'])
        per_root_neighbors[root] = neighbors[:3]

    # Surah density: (afterlife-vocabulary ayahs in surah) / (all root-bearing words)
    print("[4/5] Computing surah density...", file=sys.stderr)

    surah_all_roots = defaultdict(int)
    surah_afterlife_roots = defaultdict(int)

    with open('data/morphology/words.jsonl', 'r') as f:
        for line in f:
            word = json.loads(line)
            root = word.get('root')
            if root:
                surah = word['surah']
                surah_all_roots[surah] += 1
                if root in AFTERLIFE_ROOTS:
                    surah_afterlife_roots[surah] += 1

    surah_density = {}
    for surah_num in range(1, 115):
        total = surah_all_roots.get(surah_num, 0)
        afterlife = surah_afterlife_roots.get(surah_num, 0)
        density = (afterlife / total * 100) if total > 0 else 0.0
        surah_density[str(surah_num)] = round(density, 1)

    # Meccan share per root
    meccan_share = {}
    for root in root_list:
        total = root_totals[root]
        meccan = root_meccan[root]
        share = (meccan / total) if total > 0 else 0.0
        meccan_share[root] = round(share, 3)

    print("[5/5] Writing output...", file=sys.stderr)

    output = {
        'roots': root_list,
        'matrix': cooccurrence,
        'lift': lift,
        'top_pairs': top_pairs,
        'weak_pairs': weak_pairs,
        'per_root_neighbors': per_root_neighbors,
        'surah_density': surah_density,
        'meccan_share': meccan_share,
        'root_totals': {root: root_totals[root] for root in root_list},
        'root_meccan': {root: root_meccan[root] for root in root_list}
    }

    output_path = Path('data/structural/afterlife-cooccurrence.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"✓ Written to {output_path}", file=sys.stderr)

    # Summary
    print(f"\nSummary:", file=sys.stderr)
    for root in root_list:
        print(f"  {root}: {root_totals[root]} occurrences ({root_meccan[root]} Meccan)", file=sys.stderr)

if __name__ == '__main__':
    build_cooccurrence_matrix()
