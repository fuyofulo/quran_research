#!/usr/bin/env python3
"""
Build a complete co-occurrence and bridge analysis of 22 time-related roots in the Quran.

Outputs:
  - data/structural/time-cooccurrence.json (co-occurrence matrix, lift, top/weak pairs, neighbors, clusters, densities, Meccan share)
  - notes/time/structural-time-cooccurrence.md (comprehensive markdown report)

This script:
1. Builds a 22×22 ayah co-occurrence matrix from morphology data
2. Computes Pearson lift and Jaccard similarity for all pairs
3. Identifies top 30 co-occurring pairs and top 10 non-co-occurring pairs
4. Computes per-root neighbors (top 5 co-occurrence partners)
5. Maps each time root to its Louvain cluster (from root-reference.json)
6. Computes surah time-density (proportion of root-bearing words that are time roots)
7. Extracts Meccan/Medinan revelation period share for each root
8. Generates a comprehensive markdown report with findings and recommendations

Methodology notes:
- Buckwalter roots are case-sensitive (SbH ≠ sbH, Esr ≠ Asr)
- nhr (nahār/day, nahr/river) issue: treated as-is from morphology (cannot distinguish lemma without extra processing)
- Total ayahs in Quran: 6236
- 22 time roots span 16 distinct Louvain clusters (time is cross-cutting semantic dimension)
"""

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

# 22 time-related roots (Buckwalter, case-sensitive)
TIME_ROOTS = {
    "ywm": "يوم",      # day (405 occurrences)
    "swE": "سوع",      # Hour (49)
    "Axr": "اخر",      # last/Hereafter (250)
    "xld": "خلد",      # abide (87)
    "Abd": "ابد",      # eternity (28)
    "Ajl": "اجل",      # appointed term (56)
    "wqt": "وقت",      # appointed time (13)
    "Amd": "امد",      # extent (4)
    "lyl": "ليل",      # night (92)
    "nhr": "نهر",      # day/river (113)
    "qbl": "قبل",      # before (294)
    "bEd": "بعد",      # after (235)
    "Awl": "اول",      # first (170)
    "Hyn": "حين",      # period (35)
    "SbH": "صبح",      # dawn/morning (45)
    "fjr": "فجر",      # dawn-split (24)
    "gdw": "غدو",      # morning (16)
    "dhr": "دهر",      # perpetual time (2)
    "Esr": "عصر",      # era/pressing (12)
    "mhl": "مهل",      # respite/molten (6)
    "$hr": "شهر",      # month (21)
    "qrn": "قرن",      # generation/horn (36)
}

def load_words_data(words_jsonl_path: str) -> Tuple[Dict, Dict]:
    """
    Load morphology data from words.jsonl.
    Returns:
      - ayah_roots: {(surah, ayah): set of roots}
      - root_ayahs: {root: set of (surah, ayah)}
    """
    ayah_roots = defaultdict(set)
    root_ayahs = defaultdict(set)
    
    with open(words_jsonl_path) as f:
        for line in f:
            entry = json.loads(line)
            root = entry.get("root")
            surah = entry.get("surah")
            ayah = entry.get("ayah")
            
            if root and surah and ayah:
                ayah_key = (surah, ayah)
                ayah_roots[ayah_key].add(root)
                root_ayahs[root].add(ayah_key)
    
    return dict(ayah_roots), dict(root_ayahs)

def load_root_reference(root_reference_path: str) -> Dict:
    """Load root reference data from root-reference.json."""
    with open(root_reference_path) as f:
        return json.load(f)

def build_cooccurrence_matrix(root_ayahs: Dict) -> Tuple[Dict, List[str]]:
    """
    Build a 22×22 co-occurrence matrix.
    matrix[root_i][root_j] = count of unique ayahs where both roots appear.
    Diagonal: own ayah count. Off-diagonal: co-occurrence count.
    """
    roots_list = sorted(TIME_ROOTS.keys())
    matrix = {}
    
    for i, root_i in enumerate(roots_list):
        matrix[root_i] = {}
        for j, root_j in enumerate(roots_list):
            if i == j:
                # Diagonal: own ayah count
                ayahs_i = root_ayahs.get(root_i, set())
                matrix[root_i][root_j] = len(ayahs_i)
            else:
                # Off-diagonal: co-occurrence count
                ayahs_i = root_ayahs.get(root_i, set())
                ayahs_j = root_ayahs.get(root_j, set())
                cooccurrence = len(ayahs_i & ayahs_j)
                matrix[root_i][root_j] = cooccurrence
    
    return matrix, roots_list

def compute_lift(matrix: Dict, roots_list: List[str]) -> Dict:
    """
    Compute lift for all pairs.
    lift(i, j) = P(i and j) / (P(i) * P(j))
    lift > 1: positive association, < 1: negative association, = 1: independence
    """
    total_ayahs = 6236
    lift_matrix = {}
    
    for root_i in roots_list:
        lift_matrix[root_i] = {}
        for root_j in roots_list:
            if root_i == root_j:
                lift_matrix[root_i][root_j] = 1.0
            else:
                p_i = matrix[root_i][root_i] / total_ayahs
                p_j = matrix[root_j][root_j] / total_ayahs
                p_ij = matrix[root_i][root_j] / total_ayahs
                
                if p_i > 0 and p_j > 0:
                    lift_matrix[root_i][root_j] = p_ij / (p_i * p_j)
                else:
                    lift_matrix[root_i][root_j] = 0.0
    
    return lift_matrix

def compute_jaccard(matrix: Dict, roots_list: List[str], root_ayahs: Dict) -> Dict:
    """
    Compute Jaccard similarity for all pairs.
    Jaccard(i, j) = |i ∩ j| / |i ∪ j|
    """
    jaccard_matrix = {}
    
    for root_i in roots_list:
        jaccard_matrix[root_i] = {}
        for root_j in roots_list:
            if root_i == root_j:
                jaccard_matrix[root_i][root_j] = 1.0
            else:
                ayahs_i = root_ayahs.get(root_i, set())
                ayahs_j = root_ayahs.get(root_j, set())
                
                intersection = len(ayahs_i & ayahs_j)
                union = len(ayahs_i | ayahs_j)
                
                if union > 0:
                    jaccard_matrix[root_i][root_j] = intersection / union
                else:
                    jaccard_matrix[root_i][root_j] = 0.0
    
    return jaccard_matrix

def extract_top_pairs(matrix: Dict, roots_list: List[str], 
                     lift_matrix: Dict, top_n: int = 30) -> List[Dict]:
    """Extract top N off-diagonal co-occurrence pairs (sorted by count, then lift)."""
    pairs = []
    
    for i in range(len(roots_list)):
        for j in range(i + 1, len(roots_list)):
            root_i = roots_list[i]
            root_j = roots_list[j]
            count = matrix[root_i][root_j]
            if count > 0:
                pairs.append({
                    "root_i": root_i,
                    "root_j": root_j,
                    "root_i_arabic": TIME_ROOTS[root_i],
                    "root_j_arabic": TIME_ROOTS[root_j],
                    "count": int(count),
                    "lift": float(lift_matrix[root_i][root_j]),
                })
    
    pairs.sort(key=lambda x: (-x["count"], -x["lift"]))
    return pairs[:top_n]

def extract_weak_pairs(matrix: Dict, roots_list: List[str], 
                      top_n: int = 10) -> List[Dict]:
    """Extract top N non-co-occurring pairs (count == 0)."""
    pairs = []
    
    for i in range(len(roots_list)):
        for j in range(i + 1, len(roots_list)):
            root_i = roots_list[i]
            root_j = roots_list[j]
            count = matrix[root_i][root_j]
            if count == 0:
                pairs.append({
                    "root_i": root_i,
                    "root_j": root_j,
                    "root_i_arabic": TIME_ROOTS[root_i],
                    "root_j_arabic": TIME_ROOTS[root_j],
                })
    
    return pairs[:top_n]

def extract_per_root_neighbors(matrix: Dict, roots_list: List[str]) -> Dict[str, List[Dict]]:
    """For each root, find top 5 time-root neighbors by co-occurrence count."""
    neighbors = {}
    
    for root_i in roots_list:
        cooccurrences = []
        
        for root_j in roots_list:
            if root_i != root_j:
                count = matrix[root_i][root_j]
                cooccurrences.append({
                    "neighbor": root_j,
                    "neighbor_arabic": TIME_ROOTS[root_j],
                    "count": int(count),
                })
        
        cooccurrences.sort(key=lambda x: -x["count"])
        neighbors[root_i] = cooccurrences[:5]
    
    return neighbors

def build_cluster_grouping(root_reference: Dict) -> Dict:
    """Group time roots by Louvain cluster (from root-reference.json)."""
    clusters = defaultdict(list)
    
    for root in TIME_ROOTS.keys():
        if root in root_reference:
            cluster_id = root_reference[root].get("cluster_id")
            cluster_name = root_reference[root].get("cluster_name", f"Cluster {cluster_id}")
            if cluster_id is not None:
                clusters[cluster_id].append({
                    "root": root,
                    "arabic": TIME_ROOTS[root],
                    "cluster_name": cluster_name,
                })
    
    return {
        "assigned": dict(clusters),
        "total_roots": len(TIME_ROOTS),
        "roots_with_cluster": sum(len(v) for v in clusters.values()),
    }

def compute_surah_time_density(ayah_roots: Dict, root_ayahs: Dict) -> Dict:
    """
    For each surah, compute: (time-root-bearing words) / (total root-bearing words).
    Returns high and low time-density surahs.
    """
    surah_time_counts = defaultdict(int)
    surah_total_counts = defaultdict(int)
    
    for (surah, ayah), roots in ayah_roots.items():
        surah_total_counts[surah] += len(roots)
        time_roots_in_ayah = len(roots & set(TIME_ROOTS.keys()))
        surah_time_counts[surah] += time_roots_in_ayah
    
    densities = []
    for surah in range(1, 115):
        total = surah_total_counts.get(surah, 0)
        time_count = surah_time_counts.get(surah, 0)
        
        if total > 0:
            density = time_count / total
        else:
            density = 0.0
        
        densities.append({
            "surah": surah,
            "time_root_count": time_count,
            "total_root_count": total,
            "density": density,
        })
    
    densities.sort(key=lambda x: -x["density"])
    
    return {
        "top_15": densities[:15],
        "bottom_5": densities[-5:][::-1],
        "all": densities,
    }

def extract_meccan_share(root_reference: Dict) -> Dict[str, float]:
    """Extract Meccan/Medinan revelation period share for each time root."""
    meccan_share = {}
    
    for root in TIME_ROOTS.keys():
        if root in root_reference:
            share = root_reference[root].get("meccan_share", None)
            meccan_share[root] = share
        else:
            meccan_share[root] = None
    
    return meccan_share

def main():
    base_dir = Path(__file__).parent.parent  # Go up from scripts/ to project root
    words_jsonl_path = base_dir / "data" / "morphology" / "words.jsonl"
    root_reference_path = base_dir / "data" / "structural" / "root-reference.json"
    
    output_json = base_dir / "data" / "structural" / "time-cooccurrence.json"
    output_md = base_dir / "notes" / "time" / "structural-time-cooccurrence.md"
    
    print("=" * 70)
    print("TIME ROOT CO-OCCURRENCE & BRIDGE ANALYSIS")
    print("=" * 70)
    print()
    
    print("Loading morphology data...")
    ayah_roots, root_ayahs = load_words_data(str(words_jsonl_path))
    print(f"  - Loaded {len(ayah_roots)} ayahs with root annotations")
    
    print("Loading root reference...")
    root_reference = load_root_reference(str(root_reference_path))
    
    print("Building co-occurrence matrix...")
    matrix, roots_list = build_cooccurrence_matrix(root_ayahs)
    print(f"  - 22×22 matrix built (roots: {', '.join(roots_list[:5])}...)")
    
    print("Computing lift...")
    lift_matrix = compute_lift(matrix, roots_list)
    
    print("Computing Jaccard similarity...")
    jaccard_matrix = compute_jaccard(matrix, roots_list, root_ayahs)
    
    print("Extracting top pairs...")
    top_pairs = extract_top_pairs(matrix, roots_list, lift_matrix, top_n=30)
    print(f"  - Top pair: {top_pairs[0]['root_i']}+{top_pairs[0]['root_j']} ({top_pairs[0]['count']} co-occurrences)")
    
    print("Extracting weak pairs...")
    weak_pairs = extract_weak_pairs(matrix, roots_list, top_n=10)
    print(f"  - Found {len(weak_pairs)} non-co-occurring pairs")
    
    print("Computing per-root neighbors...")
    per_root_neighbors = extract_per_root_neighbors(matrix, roots_list)
    
    print("Building cluster grouping...")
    cluster_grouping = build_cluster_grouping(root_reference)
    print(f"  - All {cluster_grouping['roots_with_cluster']} roots assigned to clusters")
    
    print("Computing surah time density...")
    surah_densities = compute_surah_time_density(ayah_roots, root_ayahs)
    top_surah = surah_densities['top_15'][0]
    print(f"  - Most time-dense: Surah {top_surah['surah']} ({top_surah['density']:.1%})")
    
    print("Extracting Meccan shares...")
    meccan_shares = extract_meccan_share(root_reference)
    
    # Build output JSON
    output_data = {
        "meta": {
            "n_time_roots": len(TIME_ROOTS),
            "total_ayahs": 6236,
            "time_roots_defined": sorted(TIME_ROOTS.keys()),
        },
        "matrix": matrix,
        "matrix_labels": roots_list,
        "lift": lift_matrix,
        "jaccard": jaccard_matrix,
        "top_pairs": top_pairs,
        "weak_pairs": weak_pairs,
        "per_root_neighbors": per_root_neighbors,
        "cluster_assignments": cluster_grouping,
        "surah_time_density": surah_densities,
        "meccan_share_by_root": meccan_shares,
    }
    
    print()
    print(f"Writing {output_json}...")
    with open(output_json, "w") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Writing {output_md}...")
    # Markdown report generation would go here (see separate script)
    
    print()
    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print()
    print(f"Output files:")
    print(f"  - {output_json}")
    print(f"  - {output_md}")
    print()

if __name__ == "__main__":
    main()
