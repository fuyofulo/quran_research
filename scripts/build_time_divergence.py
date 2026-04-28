#!/usr/bin/env python3
"""
Build time-divergence analysis for time-bearing ayahs.
Identifies ayahs with time roots, joins with translation-divergence data,
and performs multi-level analysis.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

# Time roots (Buckwalter, case-sensitive)
TIME_ROOTS = {
    "ywm", "swE", "Axr", "xld", "Abd", "Ajl", "wqt", "Amd",
    "lyl", "nhr", "qbl", "bEd", "Awl", "Hyn", "SbH", "fjr",
    "gdw", "dhr", "Esr", "mhl", "$hr", "qrn"
}

# Meccan oath surahs (known eschatological)
MECCAN_OATH_SURAHS = {51, 77, 79, 81, 82, 84, 86, 88, 89, 92, 93, 100, 101, 103}

# Medinan legal surahs
LEGAL_SURAHS = {2, 3, 4, 5, 8, 9, 24, 33, 58, 59, 60, 62, 65}

# Surah classification
def classify_surah(surah_num):
    """Classify a surah as legal, eschatological, or other."""
    if surah_num in LEGAL_SURAHS:
        return "legal"
    if surah_num in MECCAN_OATH_SURAHS:
        return "eschatological"
    return "other"

def load_translations():
    """Load all translation files."""
    trans = {}
    for translator in ['saheeh', 'pickthall', 'khattab', 'arberry']:
        with open(f'/Users/fuyofulo/research/quran/data/translations/{translator}.json') as f:
            data = json.load(f)
            trans[translator] = data['ayahs']
    return trans

def load_divergence_data():
    """Load pre-computed divergence scores."""
    with open('/Users/fuyofulo/research/quran/data/structural/translation-divergence.json') as f:
        return json.load(f)

def load_arabic_text():
    """Load Arabic text."""
    with open('/Users/fuyofulo/research/quran/data/arabic/quran.json') as f:
        return json.load(f)

def scan_words_for_time_roots():
    """Scan words.jsonl to find all ayahs with time roots."""
    time_bearing_ayahs = defaultdict(lambda: {'roots': set(), 'words': []})
    
    print("Scanning words.jsonl for time roots...", file=sys.stderr)
    
    with open('/Users/fuyofulo/research/quran/data/morphology/words.jsonl') as f:
        for line_num, line in enumerate(f, 1):
            if line_num % 100000 == 0:
                print(f"  Processed {line_num} lines...", file=sys.stderr)
            
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            
            root = obj.get('root', '')
            if root in TIME_ROOTS:
                surah = obj.get('surah')
                ayah = obj.get('ayah')
                if surah and ayah:
                    citation = f"{surah}:{ayah}"
                    time_bearing_ayahs[citation]['roots'].add(root)
                    time_bearing_ayahs[citation]['words'].append({
                        'word': obj.get('word'),
                        'form': obj.get('form_buckwalter'),
                        'root': root
                    })
    
    # Convert sets to sorted lists for JSON serialization
    for citation in time_bearing_ayahs:
        time_bearing_ayahs[citation]['roots'] = sorted(list(time_bearing_ayahs[citation]['roots']))
    
    print(f"Found {len(time_bearing_ayahs)} time-bearing ayahs", file=sys.stderr)
    return time_bearing_ayahs

def main():
    # Load data
    print("Loading data...", file=sys.stderr)
    time_bearing = scan_words_for_time_roots()
    divergence_data = load_divergence_data()
    translations = load_translations()
    arabic_text = load_arabic_text()
    
    # Enrich time-bearing ayahs with divergence scores
    enriched = []
    for citation, time_info in time_bearing.items():
        if citation not in divergence_data:
            continue
        
        div_data = divergence_data[citation]
        surah, ayah = map(int, citation.split(':'))
        
        enriched.append({
            'citation': citation,
            'surah': surah,
            'ayah': ayah,
            'time_roots': time_info['roots'],
            'divergence_score': div_data['scores']['combined'],
            'outlier_translator': div_data['outlier'],
            'regime': div_data.get('regime', 'unknown'),
            'length_variance': div_data['scores']['length_variance'],
            'jaccard': div_data['scores']['jaccard'],
            'lexical_disagreement': div_data['scores']['lexical_disagreement'],
        })
    
    print(f"Enriched {len(enriched)} time-bearing ayahs with divergence scores", file=sys.stderr)
    
    # Sort by divergence score (descending)
    enriched.sort(key=lambda x: x['divergence_score'], reverse=True)
    
    # Top 50
    top_50 = enriched[:50]
    
    # Per-root divergence average
    root_scores = defaultdict(list)
    for item in enriched:
        for root in item['time_roots']:
            root_scores[root].append(item['divergence_score'])
    
    per_root_avg = {
        root: sum(scores) / len(scores)
        for root, scores in root_scores.items()
    }
    
    per_root_avg_sorted = sorted(per_root_avg.items(), key=lambda x: x[1], reverse=True)
    
    # Per-translator outlier rate on time verses
    outlier_counts = defaultdict(int)
    total_time_ayahs = len(enriched)
    for item in enriched:
        if item['outlier_translator']:
            outlier_counts[item['outlier_translator']] += 1
    
    per_translator_outlier_rate = {
        trans: count / total_time_ayahs
        for trans, count in outlier_counts.items()
    }
    
    # Surah concentration
    surah_counts = defaultdict(lambda: {'count': 0, 'avg_divergence': 0})
    for item in enriched:
        surah = item['surah']
        surah_counts[surah]['count'] += 1
        surah_counts[surah]['avg_divergence'] += item['divergence_score']
    
    for surah in surah_counts:
        if surah_counts[surah]['count'] > 0:
            surah_counts[surah]['avg_divergence'] /= surah_counts[surah]['count']
    
    top_surahs = sorted(
        [(s, data) for s, data in surah_counts.items()],
        key=lambda x: x[1]['avg_divergence'],
        reverse=True
    )[:20]
    
    surah_concentration = {
        f"{surah}": {
            'count': data['count'],
            'avg_divergence': round(data['avg_divergence'], 4)
        }
        for surah, data in top_surahs
    }
    
    # Legal vs Eschatological divergence
    legal_divs = []
    esc_divs = []
    for item in enriched:
        classification = classify_surah(item['surah'])
        if classification == 'legal':
            legal_divs.append(item['divergence_score'])
        elif classification == 'eschatological':
            esc_divs.append(item['divergence_score'])
    
    legal_vs_esc = {
        'legal_avg': round(sum(legal_divs) / len(legal_divs), 4) if legal_divs else None,
        'legal_count': len(legal_divs),
        'eschatological_avg': round(sum(esc_divs) / len(esc_divs), 4) if esc_divs else None,
        'eschatological_count': len(esc_divs),
    }
    
    # Build output JSON
    output = {
        'metadata': {
            'time_roots_total': len(TIME_ROOTS),
            'time_bearing_ayahs_total': len(enriched),
            'divergence_metric': 'combined (length_variance + jaccard + lexical_disagreement)',
        },
        'top_50_high_divergence': [
            {
                'citation': item['citation'],
                'time_roots': item['time_roots'],
                'divergence_score': round(item['divergence_score'], 4),
                'outlier_translator': item['outlier_translator'],
                'regime': item['regime'],
            }
            for item in top_50
        ],
        'per_root_divergence_avg': {
            root: round(score, 4)
            for root, score in per_root_avg_sorted
        },
        'per_translator_outlier_rate_on_time': {
            trans: round(rate, 4)
            for trans, rate in sorted(per_translator_outlier_rate.items(), key=lambda x: x[1], reverse=True)
        },
        'surah_concentration': surah_concentration,
        'legal_vs_eschatological_divergence': legal_vs_esc,
    }
    
    # Save
    output_path = Path('/Users/fuyofulo/research/quran/data/structural/time-divergence.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Saved time-divergence.json", file=sys.stderr)
    
    # Now build the detailed side-by-side markdown report
    print("Building side-by-side reading panel...", file=sys.stderr)
    
    md_lines = [
        "# Time-Bearing Ayah Divergence Analysis",
        "",
        "## Summary Statistics",
        "",
        f"- **Total time-bearing ayahs**: {len(enriched)}",
        f"- **Legal-classification ayahs**: {legal_vs_esc['legal_count']}",
        f"- **Eschatological-classification ayahs**: {legal_vs_esc['eschatological_count']}",
        f"- **Legal vs Eschatological divergence**: {legal_vs_esc['legal_avg']} vs {legal_vs_esc['eschatological_avg']}",
        "",
        "## Per-Root Divergence Rankings",
        "",
        "Average translation divergence for each time root (higher = more contested):",
        "",
    ]
    
    for root, score in per_root_avg_sorted:
        md_lines.append(f"- **{root}**: {score:.4f}")
    
    md_lines.extend([
        "",
        "## Translator Outlier Rates on Time Verses",
        "",
        "Frequency with which each translator produces the outlier reading:",
        "",
    ])
    
    for trans, rate in sorted(per_translator_outlier_rate.items(), key=lambda x: x[1], reverse=True):
        md_lines.append(f"- **{trans}**: {rate*100:.1f}%")
    
    md_lines.extend([
        "",
        "## Top 20 High-Divergence Time-Bearing Ayahs",
        "",
    ])
    
    # Build detailed panels for top 20
    for idx, item in enumerate(top_50[:20], 1):
        citation = item['citation']
        surah, ayah = map(int, citation.split(':'))
        
        # Get translations
        saheeh = translations['saheeh'].get(citation, "")
        pickthall = translations['pickthall'].get(citation, "")
        khattab = translations['khattab'].get(citation, "")
        arberry = translations['arberry'].get(citation, "")
        arabic = arabic_text.get(citation, "")
        
        md_lines.extend([
            f"### {idx}. [{citation}]",
            "",
            f"**Time roots**: {', '.join(item['time_roots'])}",
            f"**Divergence score**: {item['divergence_score']:.4f} ({item['regime']})",
            f"**Outlier translator**: {item['outlier_translator'] or 'None'}",
            "",
            f"**Arabic**: {arabic}",
            "",
            "**Translations**:",
            "",
            f"- **Saheeh International**: {saheeh}",
            f"- **Pickthall**: {pickthall}",
            f"- **Khattab**: {khattab}",
            f"- **Arberry**: {arberry}",
            "",
            f"**Divergence Analysis**: [Will be filled with manual analysis]",
            "",
        ])
    
    # Write markdown
    md_path = Path('/Users/fuyofulo/research/quran/notes/time/structural-time-divergence.md')
    md_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(md_path, 'w') as f:
        f.write('\n'.join(md_lines))
    
    print(f"Saved structural-time-divergence.md", file=sys.stderr)
    print("Done.", file=sys.stderr)

if __name__ == '__main__':
    main()
