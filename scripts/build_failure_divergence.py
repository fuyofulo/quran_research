#!/usr/bin/env python3
"""
Build translation-divergence catalog for 32 failure-vocabulary roots.

Outputs to: data/structural/failure-divergence.json
"""

import json
import sys
from collections import defaultdict

FAILURE_ROOTS = ['xsr', 'xyb', 'hlk', 'bwr', 'DyE', 'bTl', 'Dll', 'ErD', 'gfl', 'nks', 'jhl', 'kfr', 'nfq', '$rk', 'jHd', 'kbr', 'Tgy', 'bgy', 'srf', 'fjr', 'qsw', 'xtm', 'qfl', 'mrD', 'glf', 'knn', '*nb', 'Avm', 'Zlm', 'swA', 'fsq', 'fsd']

def build_divergence_catalog():
    """
    Load words.jsonl to identify all ayahs containing failure roots.
    Load translation-divergence.json to fetch divergence scores.
    Build per-root and per-ayah divergence profiles.
    """

    print("[1/4] Loading words.jsonl...", file=sys.stderr)

    # Map (surah, ayah) -> set of roots that appear in it
    ayah_roots = defaultdict(set)
    root_ayahs = defaultdict(list)

    with open('data/morphology/words.jsonl', 'r') as f:
        for line in f:
            word = json.loads(line)
            root = word.get('root')
            if root in FAILURE_ROOTS:
                location = tuple(word['location'])[:2]  # (surah, ayah)
                ayah_roots[location].add(root)
                if location not in root_ayahs[root]:
                    root_ayahs[root].append(location)

    print(f"   Found {len(ayah_roots)} ayahs with failure roots", file=sys.stderr)

    # Load translation-divergence data
    print("[2/4] Loading translation-divergence.json...", file=sys.stderr)

    with open('data/structural/translation-divergence.json', 'r') as f:
        divergence_data = json.load(f)

    # Collect all failure-ayahs with their divergence scores
    print("[3/4] Computing divergence profiles...", file=sys.stderr)

    ayah_divergence_list = []
    for (surah, ayah), roots in ayah_roots.items():
        key = f"{surah}:{ayah}"
        if key in divergence_data:
            div_entry = divergence_data[key]
            ayah_divergence_list.append({
                'reference': key,
                'surah': surah,
                'ayah': ayah,
                'roots': sorted(list(roots)),
                'divergence_combined': round(div_entry['scores']['combined'], 4),
                'divergence_jaccard': round(div_entry['scores']['jaccard'], 4),
                'outlier': div_entry.get('outlier'),
                'regime': div_entry.get('regime', 'unknown')
            })

    # Sort by divergence score (descending)
    ayah_divergence_list.sort(key=lambda x: -x['divergence_combined'])

    # Top 30 high-divergence failure-bearing ayahs
    top_30_high_divergence = ayah_divergence_list[:30]

    # Per-root divergence average
    per_root_divergence_avg = {}
    for root in FAILURE_ROOTS:
        scores = []
        for (surah, ayah), roots_in_ayah in ayah_roots.items():
            if root in roots_in_ayah:
                key = f"{surah}:{ayah}"
                if key in divergence_data:
                    scores.append(divergence_data[key]['scores']['combined'])

        avg = sum(scores) / len(scores) if scores else 0.0
        per_root_divergence_avg[root] = round(avg, 4)

    # Surah concentration: identify top 10 surahs by failure-root density with high divergence
    surah_failure_divergence = defaultdict(lambda: {'count': 0, 'total_divergence': 0.0, 'ayahs': []})

    for (surah, ayah), roots in ayah_roots.items():
        key = f"{surah}:{ayah}"
        if key in divergence_data:
            div_score = divergence_data[key]['scores']['combined']
            surah_failure_divergence[surah]['count'] += 1
            surah_failure_divergence[surah]['total_divergence'] += div_score
            surah_failure_divergence[surah]['ayahs'].append({
                'ayah': ayah,
                'roots': sorted(list(roots)),
                'divergence': round(div_score, 4)
            })

    surah_concentration = []
    for surah in sorted(surah_failure_divergence.keys()):
        entry = surah_failure_divergence[surah]
        avg_div = entry['total_divergence'] / entry['count'] if entry['count'] > 0 else 0.0
        surah_concentration.append({
            'surah': surah,
            'failure_ayah_count': entry['count'],
            'avg_divergence': round(avg_div, 4),
            'total_divergence': round(entry['total_divergence'], 4)
        })

    surah_concentration.sort(key=lambda x: -x['total_divergence'])
    surah_concentration = surah_concentration[:10]

    # Per-translator outlier rate on failure vocabulary
    print("[4/4] Computing per-translator outlier rates...", file=sys.stderr)

    translator_outlier_count = defaultdict(int)
    translator_ayah_count = defaultdict(int)

    for (surah, ayah), roots in ayah_roots.items():
        key = f"{surah}:{ayah}"
        if key in divergence_data:
            outlier = divergence_data[key].get('outlier')
            translators = ['saheeh', 'pickthall', 'khattab', 'arberry']
            for trans in translators:
                translator_ayah_count[trans] += 1
                if outlier == trans:
                    translator_outlier_count[trans] += 1

    per_translator_outlier_rate = {}
    for trans in ['saheeh', 'pickthall', 'khattab', 'arberry']:
        count = translator_ayah_count.get(trans, 0)
        outlier_rate = translator_outlier_count.get(trans, 0) / count if count > 0 else 0.0
        per_translator_outlier_rate[trans] = round(outlier_rate, 3)

    output = {
        'top_30_high_divergence': top_30_high_divergence,
        'per_root_divergence_avg': per_root_divergence_avg,
        'surah_concentration': surah_concentration,
        'per_translator_outlier_rate': per_translator_outlier_rate,
        'total_failure_ayahs': len(ayah_divergence_list)
    }

    output_path = 'data/structural/failure-divergence.json'
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"✓ Written to {output_path}", file=sys.stderr)

if __name__ == '__main__':
    build_divergence_catalog()
