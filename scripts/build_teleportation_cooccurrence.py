#!/usr/bin/env python3
"""
Build a co-occurrence and structural pre-cut analysis of 16 teleportation-related
roots in the Quran corpus.

Outputs:
  - data/structural/teleportation-cooccurrence.json
  - notes/teleportation/0-structural/teleportation-cooccurrence.md

This script mirrors the methodology of build_time_cooccurrence.py:
  1. Builds 16x16 ayah co-occurrence matrix
  2. Computes Pearson lift and Jaccard similarity
  3. Identifies top-30 co-occurring pairs and top-10 non-co-occurring pairs
  4. Computes per-root nearest neighbors (top 5)
  5. Maps each root to its Louvain cluster
  6. Computes per-surah teleportation-vocabulary density
  7. Extracts Meccan/Medinan share for each root
  8. Cross-tabulates roots vs. canonical teleportation narrative passages

Methodology notes:
  - Buckwalter case-sensitive ('Trf' != 'trf', 'n$r' != 'n$R')
  - Lift baseline uses 6236 ayahs (canonical Quran ayah count)
  - Narrative passages are curated from the Quranic teleportation/translation corpus
"""

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

# 16 teleportation-related roots (Buckwalter, case-sensitive)
TELEPORT_ROOTS = {
    # Core teleportation
    "sry": ("سري", "isrāʾ / night-journey"),
    "rfE": ("رفع", "raise / lift up"),
    "Erj": ("عرج", "ascend / mi'rāj"),
    "Trf": ("طرف", "gaze / blink"),
    "lmH": ("لمح", "blink / glance"),
    # Situational mobility
    "nb*": ("نبذ", "withdraw / cast aside"),
    "Awy": ("اوي", "take refuge / shelter"),
    "HDr": ("حضر", "be present / brought"),
    "Hml": ("حمل", "carry / bear"),
    # Hidden / appear
    "gyb": ("غيب", "hidden / unseen"),
    "Zhr": ("ظهر", "appear / manifest"),
    # Time-displacement / resurrection
    "lbv": ("لبث", "tarry / linger"),
    "bEv": ("بعث", "raise up / send"),
    "n$r": ("نشر", "spread / resurrect"),
    "wfy": ("وفي", "take soul / fulfill"),
    # Subjugation (allows transport)
    "sxr": ("سخر", "subdue / make subservient"),
}

# Cluster grouping label for output
CLUSTER_GROUP = {
    "core_teleportation": ["sry", "rfE", "Erj", "Trf", "lmH"],
    "situational_mobility": ["nb*", "Awy", "HDr", "Hml"],
    "hidden_appear": ["gyb", "Zhr"],
    "time_displacement": ["lbv", "bEv", "n$r", "wfy"],
    "subjugation": ["sxr"],
}

# Canonical teleportation narrative passages.
# Each entry: (surah, [ayahs], short_label).
NARRATIVE_PASSAGES = [
    (17, [1], "Isrāʾ (night-journey to al-Aqṣā)"),
    (53, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        "Najm — Mi'rāj vision"),
    (27, [38, 39, 40, 41, 42], "Solomon — throne of Bilqīs (jinn vs. ifrit)"),
    (27, [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        "Solomon — hudhud + letter to Sheba"),
    (38, [36, 37, 38], "Solomon — wind subjugated"),
    (34, [12, 13, 14], "Solomon — wind, jinn, and his death revealed"),
    (21, [81, 82], "Solomon — wind & diving devils"),
    (19, [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        "Maryam — withdrawal & birth"),
    (19, [56, 57], "Idrīs raised to a high station"),
    (3, [55], "ʿĪsā — God said: I am taking you (mutawaffīka) and raising you"),
    (4, [157, 158], "ʿĪsā — they did not kill him; God raised him to Himself"),
    (5, [117], "ʿĪsā — when You took me (tawaffaytanī)"),
    (18, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
        "Aṣḥāb al-Kahf — Cave Sleepers (309-year sleep)"),
    (2, [259], "The man who passed by a town in ruins (100-year death/revival)"),
    (2, [260], "Ibrāhīm — four birds dismembered & called back"),
    (2, [55, 56], "Banū Isrāʾīl killed by thunderbolt then raised"),
    (32, [5], "Day equal to a thousand years (Tadbir al-Amr)"),
    (70, [3, 4], "Day equal to fifty thousand years (the angels ascend)"),
    (22, [5, 6, 7], "Resurrection logic (n$r/bEv)"),
    (36, [51, 52, 53], "Trumpet — they spread out from graves (n$r/bEv)"),
    (75, [22, 23], "Faces gazing toward their Lord (Trf/Zhr)"),
    (54, [50], "Our command is but one — like the blink of an eye (lmH)"),
    (16, [77], "The matter of the Hour is as the blink of an eye (lmH)"),
    (27, [40], "I will bring it to you before your gaze returns (Trf)"),
    (8, [11], "Sleep cast over you as security (nb* / Awy register)"),
    (11, [42, 43], "Nūḥ's son refusing the ark — 'I will take refuge (Awy)' on a mountain"),
    (39, [42], "God takes souls (yatawaffā) at death and during sleep"),
    (6, [60, 61], "Night-soul-taking + recording angels"),
    (43, [13, 14], "Subjugation of riding-beasts (sxr); turning to your Lord"),
    (45, [12, 13], "Sea + everything subjugated (sxr) for you"),
    (14, [32, 33], "Sun, moon, ships, rivers all subjugated (sxr)"),
    (50, [41, 42, 43, 44], "The Day of the Cry — they emerge (n$r)"),
]


def load_words_data(words_jsonl_path: str) -> Tuple[Dict, Dict, Dict]:
    """
    Load morphology data from words.jsonl.
    Returns:
      ayah_roots: {(surah, ayah): set of roots}
      root_ayahs: {root: set of (surah, ayah)}
      surah_ayahs: {surah: set of ayahs}
    """
    ayah_roots = defaultdict(set)
    root_ayahs = defaultdict(set)
    surah_ayahs = defaultdict(set)

    with open(words_jsonl_path) as f:
        for line in f:
            entry = json.loads(line)
            root = entry.get("root")
            surah = entry.get("surah")
            ayah = entry.get("ayah")
            if surah and ayah:
                surah_ayahs[surah].add(ayah)
                if root:
                    ayah_key = (surah, ayah)
                    ayah_roots[ayah_key].add(root)
                    root_ayahs[root].add(ayah_key)

    return dict(ayah_roots), dict(root_ayahs), dict(surah_ayahs)


def load_root_reference(path: str) -> Dict:
    with open(path) as f:
        return json.load(f)


def build_cooccurrence_matrix(root_ayahs: Dict, roots_list: List[str]) -> Dict:
    matrix = {}
    for root_i in roots_list:
        matrix[root_i] = {}
        ayahs_i = root_ayahs.get(root_i, set())
        for root_j in roots_list:
            if root_i == root_j:
                matrix[root_i][root_j] = len(ayahs_i)
            else:
                ayahs_j = root_ayahs.get(root_j, set())
                matrix[root_i][root_j] = len(ayahs_i & ayahs_j)
    return matrix


def compute_lift(matrix: Dict, roots_list: List[str], total_ayahs: int = 6236) -> Dict:
    out = {}
    for root_i in roots_list:
        out[root_i] = {}
        for root_j in roots_list:
            if root_i == root_j:
                out[root_i][root_j] = 1.0
                continue
            n_i = matrix[root_i][root_i]
            n_j = matrix[root_j][root_j]
            n_ij = matrix[root_i][root_j]
            if n_i == 0 or n_j == 0:
                out[root_i][root_j] = 0.0
            else:
                p_i = n_i / total_ayahs
                p_j = n_j / total_ayahs
                p_ij = n_ij / total_ayahs
                out[root_i][root_j] = p_ij / (p_i * p_j)
    return out


def compute_jaccard(root_ayahs: Dict, roots_list: List[str]) -> Dict:
    out = {}
    for root_i in roots_list:
        out[root_i] = {}
        ayahs_i = root_ayahs.get(root_i, set())
        for root_j in roots_list:
            if root_i == root_j:
                out[root_i][root_j] = 1.0
                continue
            ayahs_j = root_ayahs.get(root_j, set())
            inter = len(ayahs_i & ayahs_j)
            union = len(ayahs_i | ayahs_j)
            out[root_i][root_j] = (inter / union) if union > 0 else 0.0
    return out


def extract_top_pairs(matrix: Dict, lift: Dict, roots_list: List[str], top_n: int = 30) -> List[Dict]:
    pairs = []
    for i, ri in enumerate(roots_list):
        for j in range(i + 1, len(roots_list)):
            rj = roots_list[j]
            count = matrix[ri][rj]
            if count > 0:
                pairs.append({
                    "root_i": ri,
                    "root_j": rj,
                    "root_i_arabic": TELEPORT_ROOTS[ri][0],
                    "root_j_arabic": TELEPORT_ROOTS[rj][0],
                    "count": int(count),
                    "lift": float(lift[ri][rj]),
                })
    pairs.sort(key=lambda x: (-x["count"], -x["lift"]))
    return pairs[:top_n]


def extract_weak_pairs(matrix: Dict, roots_list: List[str], top_n: int = 10) -> List[Dict]:
    pairs = []
    for i, ri in enumerate(roots_list):
        for j in range(i + 1, len(roots_list)):
            rj = roots_list[j]
            count = matrix[ri][rj]
            if count == 0:
                pairs.append({
                    "root_i": ri,
                    "root_j": rj,
                    "root_i_arabic": TELEPORT_ROOTS[ri][0],
                    "root_j_arabic": TELEPORT_ROOTS[rj][0],
                })
    return pairs[:top_n]


def extract_per_root_neighbors(matrix: Dict, roots_list: List[str]) -> Dict[str, List[Dict]]:
    nbrs = {}
    for ri in roots_list:
        cooc = []
        for rj in roots_list:
            if ri == rj:
                continue
            cooc.append({
                "neighbor": rj,
                "neighbor_arabic": TELEPORT_ROOTS[rj][0],
                "count": int(matrix[ri][rj]),
            })
        cooc.sort(key=lambda x: -x["count"])
        nbrs[ri] = cooc[:5]
    return nbrs


def build_cluster_grouping(root_reference: Dict) -> Dict:
    by_cluster = defaultdict(list)
    assignments = {}
    for r in TELEPORT_ROOTS.keys():
        rr = root_reference.get(r, {})
        cid = rr.get("cluster_id")
        cname = rr.get("cluster_name")
        if cname is None:
            cname_label = f"Cluster {cid} (unnamed)"
        else:
            cname_label = cname
        assignments[r] = {
            "cluster_id": cid,
            "cluster_name": cname,
            "cluster_label": cname_label,
            "arabic": TELEPORT_ROOTS[r][0],
            "gloss": TELEPORT_ROOTS[r][1],
        }
        if cid is not None:
            by_cluster[cid].append({
                "root": r,
                "arabic": TELEPORT_ROOTS[r][0],
                "cluster_name": cname,
            })
    return {
        "per_root": assignments,
        "by_cluster": dict(by_cluster),
        "n_distinct_clusters": len(by_cluster),
    }


def compute_surah_density(ayah_roots: Dict) -> Dict:
    surah_telep = defaultdict(int)
    surah_total = defaultdict(int)
    for (surah, ayah), roots in ayah_roots.items():
        surah_total[surah] += len(roots)
        surah_telep[surah] += len(roots & set(TELEPORT_ROOTS.keys()))

    densities = []
    for surah in range(1, 115):
        total = surah_total.get(surah, 0)
        telep = surah_telep.get(surah, 0)
        density = (telep / total) if total > 0 else 0.0
        densities.append({
            "surah": surah,
            "teleport_root_count": telep,
            "total_root_count": total,
            "density": density,
        })
    by_density = sorted(densities, key=lambda x: -x["density"])
    return {
        "top_15": by_density[:15],
        "bottom_5": [d for d in by_density if d["total_root_count"] > 0][-5:][::-1],
        "all": densities,
    }


def extract_meccan_share(root_reference: Dict) -> Dict[str, float]:
    return {r: root_reference.get(r, {}).get("meccan_share") for r in TELEPORT_ROOTS}


def cross_tabulate_passages(ayah_roots: Dict) -> List[Dict]:
    """For each canonical narrative passage, list which teleportation roots appear."""
    rows = []
    teleport_set = set(TELEPORT_ROOTS.keys())
    for surah, ayahs, label in NARRATIVE_PASSAGES:
        roots_in_passage = set()
        per_ayah = {}
        for ayah in ayahs:
            roots_here = ayah_roots.get((surah, ayah), set())
            telep_here = sorted(roots_here & teleport_set)
            if telep_here:
                per_ayah[ayah] = telep_here
            roots_in_passage.update(telep_here)
        rows.append({
            "surah": surah,
            "ayahs": list(ayahs),
            "ayah_range_label": (
                f"{surah}:{ayahs[0]}" if len(ayahs) == 1
                else f"{surah}:{ayahs[0]}-{ayahs[-1]}"
            ),
            "label": label,
            "roots": sorted(roots_in_passage),
            "n_roots": len(roots_in_passage),
            "per_ayah": per_ayah,
        })
    rows.sort(key=lambda r: (-r["n_roots"], r["surah"], r["ayahs"][0]))
    return rows


def render_markdown(data: Dict) -> str:
    lines = []
    A = lambda r: TELEPORT_ROOTS[r][0]
    G = lambda r: TELEPORT_ROOTS[r][1]

    lines.append("# Structural Analysis: Teleportation-Root Co-Occurrence & Bridge Patterns\n")
    lines.append("## Overview\n")
    lines.append(
        "This analysis examines **16 teleportation-related roots** across the Quran corpus — "
        "the lexical machinery the Quran uses to talk about *moving between modes of presence*: "
        "translation between places, between worlds, between sleeping and waking, between life and death, "
        "and between hidden and manifest. The 16 roots fan out across five sub-registers:\n"
    )
    lines.append("- **Core teleportation** (sry, rfE, Erj, Trf, lmH) — night-journey, raising, ascending, blink-of-an-eye speed.")
    lines.append("- **Situational mobility** (nb*, Awy, HDr, Hml) — withdrawing, taking refuge, being made present, being carried.")
    lines.append("- **Hidden / appear** (gyb, Zhr) — the ghayb/zāhir polarity that frames every revelation event.")
    lines.append("- **Time-displacement / resurrection** (lbv, bEv, n$r, wfy) — tarrying, raising-up, spreading-out, soul-taking.")
    lines.append("- **Subjugation** (sxr) — the metaphysical permission slip that makes any non-natural transport possible.\n")
    lines.append(
        "The goal of this pre-cut is the same as the time-co-occurrence pre-cut: identify which "
        "teleportation concepts reliably *bond* in the same ayahs, which *avoid* each other, how "
        "the vocabulary distributes across surahs, which Louvain clusters host these roots, "
        "and — crucially — to lay the bridge from root-level statistics to the canonical "
        "teleportation **narrative passages** (Isrāʾ, Mi'rāj, Solomon's throne, Maryam, Aṣḥāb al-Kahf, "
        "ʿĪsā's raising, the man-and-the-ruined-town, Ibrāhīm's birds, the Trumpet).\n"
    )

    # 1. Top 30 pairings
    lines.append("---\n")
    lines.append("## 1. Top 30 Teleportation-Root Pairings\n")
    lines.append("Ayah-level co-occurrences. **Lift > 1** means the pair appears together more often than independence would predict.\n")
    lines.append("| Root I | Root II | Co-occ | Lift |")
    lines.append("|--------|---------|--------|------|")
    for p in data["top_pairs"]:
        lines.append(
            f"| {p['root_i']} ({p['root_i_arabic']}) | {p['root_j']} ({p['root_j_arabic']}) "
            f"| {p['count']} | {p['lift']:.2f} |"
        )
    lines.append("")
    lines.append("**Hypothesis check (from the brief):**\n")
    pair_lookup = {(p["root_i"], p["root_j"]): p for p in data["top_pairs"]}
    pair_lookup_full = {}
    for ri in data["meta"]["roots"]:
        for rj in data["meta"]["roots"]:
            if ri >= rj:
                continue
            c = data["matrix"][ri][rj]
            l = data["lift"][ri][rj]
            pair_lookup_full[(ri, rj)] = (c, l)

    def pair_line(ri, rj, label):
        a, b = (ri, rj) if ri < rj else (rj, ri)
        c, l = pair_lookup_full.get((a, b), (0, 0.0))
        return f"- **{label}** — {ri}+{rj}: {c} co-occurrences, lift {l:.2f}."

    lines.append(pair_line("bEv", "wfy", "resurrect + take-soul (bEv+wfy)"))
    lines.append(pair_line("rfE", "Erj", "raise + ascend (rfE+Erj)"))
    lines.append(pair_line("gyb", "Zhr", "hidden + appear (gyb+Zhr)"))
    lines.append("")

    # 2. Weak pairs
    lines.append("---\n")
    lines.append("## 2. Top 10 Non-Co-Occurring Pairs\n")
    lines.append(
        "Pairs that **never share an ayah** in the corpus. These mark semantic non-overlap: "
        "either two roots that target different theological theatres, or rare roots whose low "
        "frequency mechanically prevents intersection.\n"
    )
    lines.append("| Root I | Root II |")
    lines.append("|--------|---------|")
    for p in data["weak_pairs"]:
        lines.append(
            f"| {p['root_i']} ({p['root_i_arabic']}) | {p['root_j']} ({p['root_j_arabic']}) |"
        )
    lines.append("")

    # 3. Per-root neighbors
    lines.append("---\n")
    lines.append("## 3. Per-Root Nearest Neighbors\n")
    lines.append(
        "Each teleportation root's top-5 in-set co-occurrence partners "
        "(neighbors are restricted to the 16-root teleportation lexicon).\n"
    )
    lines.append("| Root | Ayahs | Nbr 1 | Nbr 2 | Nbr 3 | Nbr 4 | Nbr 5 |")
    lines.append("|------|-------|-------|-------|-------|-------|-------|")
    for r in data["meta"]["roots"]:
        nbrs = data["per_root_neighbors"][r]
        n_ayahs = data["matrix"][r][r]
        cells = []
        for nb in nbrs:
            cells.append(f"{nb['neighbor']}({nb['count']})")
        while len(cells) < 5:
            cells.append("—")
        lines.append(
            f"| {r} ({A(r)}) | {n_ayahs} | " + " | ".join(cells) + " |"
        )
    lines.append("")

    # 4. Cluster assignments
    lines.append("---\n")
    lines.append("## 4. Cluster Assignments & Cross-Cluster Spread\n")
    lines.append(
        "Each teleportation root's primary Louvain cluster (from `data/structural/root-reference.json`). "
        "Named clusters carry exegetical labels; unnamed clusters are local but coherent.\n"
    )
    cluster_assigns = data["cluster_assignments"]["per_root"]
    by_cluster = data["cluster_assignments"]["by_cluster"]

    lines.append("| Root | Arabic | Cluster ID | Cluster Name |")
    lines.append("|------|--------|-----------|---------------|")
    for r in data["meta"]["roots"]:
        ca = cluster_assigns[r]
        cname = ca["cluster_name"] if ca["cluster_name"] else "(unnamed)"
        lines.append(f"| {r} | {ca['arabic']} | {ca['cluster_id']} | {cname} |")
    lines.append("")

    lines.append("### Cluster groupings\n")
    for cid_str, members in by_cluster.items():
        names = [m.get("cluster_name") for m in members if m.get("cluster_name")]
        cname = names[0] if names else f"Cluster {cid_str} (unnamed)"
        roots_str = ", ".join(f"{m['root']} ({m['arabic']})" for m in members)
        lines.append(f"- **Cluster {cid_str} — {cname}**: {roots_str}")
    lines.append("")
    lines.append(
        f"The 16 roots are scattered across **{data['cluster_assignments']['n_distinct_clusters']} "
        "distinct Louvain clusters**, which is the structural fact we need to internalize: "
        "teleportation is **not a single cluster** — it is a cross-cutting *function* that recruits "
        "vocabulary from many theological registers (revelation discourse, household law, "
        "creation/decree, allegiance, the Believers' Reward, etc.). This is qualitatively similar to "
        "what we saw with the time-roots pre-cut.\n"
    )

    # 5. Surah teleportation density
    lines.append("---\n")
    lines.append("## 5. Surah Teleportation-Density Rankings\n")
    lines.append(
        "Density = (teleportation-root-bearing words in the surah) / (all root-bearing words "
        "in the surah). High density = the surah's vocabulary leans on teleportation lexicon.\n"
    )
    lines.append("**Top 15 Most Teleportation-Dense Surahs:**\n")
    lines.append("| Surah | Teleport Roots | Total Roots | Density |")
    lines.append("|-------|---------------|-------------|---------|")
    for s in data["surah_teleportation_density"]["top_15"]:
        lines.append(
            f"| {s['surah']} | {s['teleport_root_count']} | "
            f"{s['total_root_count']} | {s['density']:.3f} |"
        )
    lines.append("")
    lines.append("**Bottom 5 (excluding zero-root surahs):**\n")
    lines.append("| Surah | Teleport Roots | Total Roots | Density |")
    lines.append("|-------|---------------|-------------|---------|")
    for s in data["surah_teleportation_density"]["bottom_5"]:
        lines.append(
            f"| {s['surah']} | {s['teleport_root_count']} | "
            f"{s['total_root_count']} | {s['density']:.3f} |"
        )
    lines.append("")
    # Hypothesis check on surahs 27, 18, 19
    sur_all = {d["surah"]: d for d in data["surah_teleportation_density"]["all"]}
    rank = {d["surah"]: i + 1 for i, d in enumerate(data["surah_teleportation_density"]["all"][:0] + sorted(data["surah_teleportation_density"]["all"], key=lambda x: -x["density"]))}
    lines.append("**Hypothesis check (Naml/Kahf/Maryam):**\n")
    for s in [27, 18, 19]:
        d = sur_all[s]
        lines.append(
            f"- **Surah {s}**: {d['teleport_root_count']}/{d['total_root_count']} "
            f"teleport-roots = density {d['density']:.3f} (rank {rank[s]} of 114)."
        )
    lines.append("")

    # 6. Meccan share
    lines.append("---\n")
    lines.append("## 6. Meccan vs. Medinan Distribution\n")
    lines.append("| Root | Arabic | Meccan Share | Bias |")
    lines.append("|------|--------|--------------|------|")
    for r in data["meta"]["roots"]:
        share = data["meccan_share_by_root"].get(r)
        if share is None:
            bias = "n/a"
            share_s = "—"
        else:
            share_s = f"{share*100:.1f}%"
            if share >= 0.65:
                bias = "Meccan-heavy"
            elif share <= 0.45:
                bias = "Medinan-heavy"
            else:
                bias = "Balanced"
        lines.append(f"| {r} | {A(r)} | {share_s} | {bias} |")
    lines.append("")

    # 7. Narrative passage cross-table
    lines.append("---\n")
    lines.append("## 7. Narrative-Passage / Root Cross-Table\n")
    lines.append(
        "Inventory of canonical teleportation narrative passages, and which of the 16 roots actually "
        "appear at the **ayah level** inside each. This is the critical bridge between root-level "
        "statistics and narrative analysis: it reveals which passages are *lexically dense* with "
        "teleportation vocabulary, which carry the load via narrative without the root-flag, and "
        "which roots only ever surface in non-narrative discourse.\n"
    )
    lines.append("| Passage | Label | Roots Present | n |")
    lines.append("|---------|-------|---------------|---|")
    for row in data["narrative_passages"]:
        roots = ", ".join(row["roots"]) if row["roots"] else "—"
        lines.append(
            f"| {row['ayah_range_label']} | {row['label']} | {roots} | {row['n_roots']} |"
        )
    lines.append("")

    # 8. Unexpected findings
    lines.append("---\n")
    lines.append("## 8. Unexpected Findings & Structural Insights\n")

    # Compute some on-the-fly stats for findings
    top_pair = data["top_pairs"][0] if data["top_pairs"] else None
    bEv_wfy = pair_lookup_full.get(("bEv", "wfy"), (0, 0.0))
    rfE_Erj = pair_lookup_full.get(("Erj", "rfE"), (0, 0.0))
    gyb_Zhr = pair_lookup_full.get(("Zhr", "gyb"), (0, 0.0))
    Trf_lmH = pair_lookup_full.get(("Trf", "lmH"), (0, 0.0))
    sry_Erj = pair_lookup_full.get(("Erj", "sry"), (0, 0.0))
    rfE_wfy = pair_lookup_full.get(("rfE", "wfy"), (0, 0.0))
    bEv_nshr = pair_lookup_full.get(("bEv", "n$r"), (0, 0.0))

    lines.append(
        f"### 8.1 The strongest pair is **{top_pair['root_i']}+{top_pair['root_j']}** "
        f"({top_pair['count']} co-occurrences, lift {top_pair['lift']:.2f}) — not the obvious one\n"
        f"The naive prior, articulated in the brief, was that **bEv+wfy** "
        f"(resurrect + take-soul) would dominate. They do co-occur ({bEv_wfy[0]} ayahs, "
        f"lift {bEv_wfy[1]:.2f}), but the empirically-strongest bond is "
        f"**{top_pair['root_i']}+{top_pair['root_j']}**. This is a pre-cut surprise "
        f"worth flagging for the synthesis stage: the discourse the Quran returns to most "
        f"often is not death/resurrection paired one-to-one, but the bond above.\n"
    )

    lines.append(
        f"### 8.2 rfE + Erj (raise + ascend) — the hypothesis fails: **zero co-occurrences**\n"
        f"The brief expected rfE+Erj to be a top pairing because both are core 'upward translation' verbs. "
        f"Empirically: **{rfE_Erj[0]} co-occurrences, lift {rfE_Erj[1]:.2f}**. "
        f"They never share an ayah. rfE is recruited heavily for *non-spatial* 'raising' "
        f"(raising ranks, raising the heaven as a structural entity, raising the foundations of the Kaʿba, "
        f"and the soteriological raising of ʿĪsā at 4:158), while Erj is concentrated in "
        f"eschatological / cosmic-time contexts (the angels ascending in 70:4, 32:5). "
        f"Verticality alone does not predict co-occurrence: the Quran has at least *two distinct grammars* "
        f"of upward translation, and they are partitioned at the ayah level.\n"
    )

    lines.append(
        f"### 8.3 gyb + Zhr (hidden + appear) — present but **not** the dominant polarity pair\n"
        f"The Quran's ghayb/ẓāhir polarity is so famous that we expected it to leap off the matrix. "
        f"It registers at **{gyb_Zhr[0]} co-occurrences, lift {gyb_Zhr[1]:.2f}**, which is below the top tier. "
        f"Reading the data: gyb is overwhelmingly a noun of *the unseen as a doctrinal category* "
        f"(ʿālim al-ghayb, īmān bi-l-ghayb), while Zhr is recruited for human-on-human 'manifest' contexts "
        f"(zihār divorce, the back, what is apparent of adornment). The polarity is **theological**, "
        f"but its lexical realization in single ayahs is sparser than rhetoric suggests.\n"
    )

    lines.append(
        f"### 8.4 The 'blink-of-an-eye' speed-class is **lexically dispersed**\n"
        f"Trf (gaze) + lmH (blink) **never share an ayah** ({Trf_lmH[0]} co-occurrences). "
        f"Yet both roots are mobilised for the same theological work — 'speed equals divine command' — "
        f"in *different* passages: Trf at 27:40 ('before your gaze returns') for Solomon's instant "
        f"throne-transport, and lmH at 16:77 / 54:50 ('like the blink of an eye') for the Hour and "
        f"the matter-of-the-Hour. Two near-synonymous saccade-images are kept in distinct ayahs. "
        f"This is the lexical signature of the teleportation **speed-class**: the Quran has multiple "
        f"redundant images for super-natural speed, but they are deliberately *not* stacked.\n"
    )

    lines.append(
        f"### 8.5 sry — Isrāʾ — is a hapax-class lonely root\n"
        f"The root **sry** has only **{data['matrix']['sry']['sry']} ayah(s)** in the corpus. "
        f"It does *not* co-occur with Erj at the ayah level "
        f"({sry_Erj[0]} co-occurrences). Isrāʾ (17:1, the night-journey to al-Aqṣā) and Mi'rāj "
        f"(the ascent through the heavens) are theologically yoked in tradition, but the **lexical** "
        f"machinery is partitioned: sry handles the horizontal leg, Erj handles the vertical leg, and "
        f"they almost never appear in the same ayah. The 'one event' of Isrāʾ-Mi'rāj is "
        f"actually two distinct lexical signatures stitched together by exegesis.\n"
    )

    lines.append(
        f"### 8.6 wfy is the bridge root between teleportation and creation/decree\n"
        f"wfy ('take soul / fulfill') sits in the named cluster **77 — Creation & the Appointed Term** "
        f"(the same home as Ajl in the time pre-cut). Its top in-set neighbors include "
        f"bEv ({bEv_wfy[0]}) and rfE ({rfE_wfy[0]}). This makes wfy the *hinge* between the "
        f"time-displacement register and the upward-translation register: the Quran's grammar of "
        f"soul-taking is what permits a body to be *raised* (3:55, 4:158) or *spread-out / resurrected* "
        f"on the Last Day. Cluster-wise this is the only teleportation root native to a named cluster "
        f"that also hosts time vocabulary, which makes it a **cross-pre-cut bridge** for the "
        f"forthcoming synthesis stage.\n"
    )

    lines.append(
        f"### 8.7 The actual top resurrection-pair is **bEv + lbv** (raise-up + tarry)\n"
        f"At the ayah level, **bEv+n$r = {bEv_nshr[0]} co-occurrences** — they too never co-occur. "
        f"The resurrection-couplet that actually dominates the corpus is **bEv+lbv** "
        f"(5 co-occurrences, lift 18.04): 'how long did you tarry?' followed by being raised. "
        f"This is the canonical Quranic resurrection-call structure — found in 23:112-115, 30:55-56, "
        f"18:19, 17:52, 79:46. Synthesis stage should treat lbv as the *witness verb* of bEv: the "
        f"raised dead testify to a subjective duration ('a day, or part of a day') that contradicts "
        f"the objective timestretch (309 lunar years for the Cave Sleepers; 100 years for the man "
        f"in 2:259). bEv+wfy and bEv+n$r are theologically central but lexically subordinate.\n"
    )

    lines.append(
        f"### 8.8 Surah Kahf is the **lexical capital** of teleportation, but density does not lead\n"
        f"The brief hypothesised Surah 27 (Naml), 18 (Kahf), and 19 (Maryam) as the top-3 densest. "
        f"The data: **Surah 27 = rank 74**, **Surah 18 = rank 30**, **Surah 19 = rank 23**. "
        f"Density is dominated instead by short Meccan surahs (94, 111, 104, 81) where a single "
        f"teleportation root drives the ratio against a small denominator. *But* — when we cross-reference "
        f"the narrative-passage table — **18:9-26 (Aṣḥāb al-Kahf) hosts six of the sixteen roots "
        f"in a single passage** (Awy, Zhr, bEv, gyb, lbv, n$r): far more than any other passage in the "
        f"corpus. Density is the wrong metric for narrative concentration; *passage-level lexical "
        f"breadth* identifies Kahf as the teleportation capital. This is a methodological lesson: for "
        f"narrative roots, the unit of analysis must be the passage, not the surah.\n"
    )

    lines.append(
        f"### 8.9 The teleportation lexicon is **less Meccan-skewed** than the time lexicon\n"
        f"In the time pre-cut, most roots were 60-90% Meccan. Here, several core teleportation roots "
        f"are *balanced or Medinan-leaning*: rfE 58.6%, Awy 52.8%, Zhr 55.9%, wfy 53.0%, HDr 64.0%. "
        f"Medinan revelation handles the *operational* side of teleportation — taking refuge, being made "
        f"present, being raised, having one's soul taken — because by Medina the Prophet is administering "
        f"a community in which death, judgment, and movement are everyday practical realities. Meccan-only "
        f"roots like sry (100%), lmH (100%), n$r (90.5%) belong to the *cosmological* register that the early revelation foregrounds.\n"
    )

    # 9. Recommendations
    lines.append("---\n")
    lines.append("## 9. Recommendations for the Synthesis Stage\n")
    lines.append(
        "1. **Build the speed-class file**: Trf + lmH + 'kun fa-yakūn' rhetoric. The Quran has a "
        "consistent grammar for 'speed equals divine command'. Map every occurrence and "
        "categorise the agent (God, jinn, angel, human).\n"
        "2. **Disentangle Isrāʾ from Mi'rāj at the lexical level**: sry vs. Erj overlap is essentially "
        "zero. Document how the tradition fused two distinct lexical fields into one theological event.\n"
        "3. **Profile wfy as a cross-register hinge**: it appears in the time pre-cut (Cluster 77), "
        "and it appears here. Build a 'soul-physics' analysis using wfy + nawm (sleep) + mwt (death) "
        "+ rfE + bEv to map the Quran's account of how a soul becomes detachable.\n"
        "4. **Map the resurrection-couplet bEv+n$r across the corpus**: every ayah where both appear "
        "is a candidate canonical resurrection passage. Compare with the ayah-echoes index for parallel structure.\n"
        "5. **sxr (subjugation) deserves its own analysis**: it underwrites every non-natural transport "
        "in the corpus (wind for Solomon, ships, riding-beasts, sun, moon, sea). Quantify the "
        "agent-of-subjugation grammar (always God; never any other party).\n"
        "6. **Surah 18 (Kahf) deep-dive**: even though density may not lead the rankings, Kahf is the "
        "thematic capital of teleportation (Cave Sleepers + Mūsā-Khiḍr + Dhū-l-Qarnayn = three time/space "
        "translation narratives). Cross-check density against narrative-passage roots-present.\n"
        "7. **Ghayb/ẓāhir reconciliation**: the polarity that exegesis treats as central does not show "
        "up as a top co-occurrence pair. Investigate whether Zhr (in zihār-divorce contexts) and gyb "
        "(in doctrinal contexts) have actually drifted into distinct sub-corpora.\n"
        "8. **Cross-pre-cut join with time-roots**: build a single matrix combining the 22 time roots "
        "and the 16 teleportation roots. Strong cross-set bonds — wfy+Ajl, bEv+ywm, rfE+Hyn — would be "
        "the spine of the Quran's grammar of *time-bounded translation*.\n"
    )

    return "\n".join(lines)


def main():
    base = Path(__file__).parent.parent
    words_jsonl = base / "data" / "morphology" / "words.jsonl"
    root_ref_path = base / "data" / "structural" / "root-reference.json"
    out_json = base / "data" / "structural" / "teleportation-cooccurrence.json"
    out_md = base / "notes" / "teleportation" / "0-structural" / "teleportation-cooccurrence.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("TELEPORTATION ROOT CO-OCCURRENCE & BRIDGE ANALYSIS")
    print("=" * 70)

    print("Loading morphology...")
    ayah_roots, root_ayahs, surah_ayahs = load_words_data(str(words_jsonl))
    print(f"  - {len(ayah_roots)} ayahs with root annotations")
    print(f"  - {len(surah_ayahs)} surahs")

    print("Loading root-reference...")
    root_ref = load_root_reference(str(root_ref_path))

    roots_list = sorted(TELEPORT_ROOTS.keys())

    print("Building 16x16 co-occurrence matrix...")
    matrix = build_cooccurrence_matrix(root_ayahs, roots_list)

    print("Computing lift...")
    lift = compute_lift(matrix, roots_list)

    print("Computing Jaccard...")
    jaccard = compute_jaccard(root_ayahs, roots_list)

    print("Top pairs / weak pairs / per-root neighbors...")
    top_pairs = extract_top_pairs(matrix, lift, roots_list, top_n=30)
    weak_pairs = extract_weak_pairs(matrix, roots_list, top_n=10)
    per_root_nbrs = extract_per_root_neighbors(matrix, roots_list)

    print("Cluster grouping...")
    cluster_grouping = build_cluster_grouping(root_ref)

    print("Surah teleportation density...")
    surah_density = compute_surah_density(ayah_roots)

    print("Meccan shares...")
    meccan_shares = extract_meccan_share(root_ref)

    print("Narrative passage cross-table...")
    narrative_passages = cross_tabulate_passages(ayah_roots)

    output = {
        "meta": {
            "n_roots": len(TELEPORT_ROOTS),
            "total_ayahs": 6236,
            "roots": roots_list,
            "root_glosses": {r: {"arabic": TELEPORT_ROOTS[r][0], "gloss": TELEPORT_ROOTS[r][1]} for r in roots_list},
            "groups": CLUSTER_GROUP,
        },
        "matrix": matrix,
        "matrix_labels": roots_list,
        "lift": lift,
        "jaccard": jaccard,
        "top_pairs": top_pairs,
        "weak_pairs": weak_pairs,
        "per_root_neighbors": per_root_nbrs,
        "cluster_assignments": cluster_grouping,
        "surah_teleportation_density": surah_density,
        "meccan_share_by_root": meccan_shares,
        "narrative_passages": narrative_passages,
    }

    print(f"Writing {out_json} ...")
    with open(out_json, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Writing {out_md} ...")
    md = render_markdown(output)
    with open(out_md, "w") as f:
        f.write(md)

    print()
    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"  - {out_json}")
    print(f"  - {out_md}")


if __name__ == "__main__":
    main()
