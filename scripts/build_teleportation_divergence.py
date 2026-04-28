#!/usr/bin/env python3
"""
Build teleportation-divergence analysis for the 16 teleportation/instant-transit
roots plus a curated set of explicit narrative passages.

Mirrors scripts/build_time_divergence.py:
  1. Scan morphology/words.jsonl for the teleportation roots.
  2. Tag each ayah with the roots it contains.
  3. Manually fold in the named narrative passages (the divergence may be high
     even when no listed root surfaces).
  4. Join with data/structural/translation-divergence.json for divergence scores.
  5. Aggregate by root, translator, surah, and "miracle vs ritual" axis.
  6. Emit:
       data/structural/teleportation-divergence.json
       notes/teleportation/0-structural/teleportation-divergence.md
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

# 16 teleportation / instant-transit roots (Buckwalter, case-sensitive)
TELEPORT_ROOTS = {
    "sry",  # to journey by night (al-Isrā')
    "rfE",  # to raise up
    "Erj",  # to ascend (mi'rāj)
    "Trf",  # blink, glance (qabla an yartadda ilayka tarfuk)
    "lmH",  # glance, glimpse
    "nb*",  # to throw, cast (sometimes used for hurling jinn from heavens)
    "Awy",  # to take refuge / withdraw (Maryam withdrew)
    "HDr",  # to bring/be present (the throne brought-present)
    "Hml",  # to carry (carriers of the Throne, etc.)
    "gyb",  # the unseen (ghayb)
    "Zhr",  # to appear (Zahir)
    "lbv",  # to tarry, abide for a duration
    "bEv",  # to send forth, raise from the dead
    "n$r",  # to spread, raise up, resurrect
    "wfy",  # to take in full / take a soul (tawaffā)
    "sxr",  # to subjugate, make subservient (winds, jinn)
}

# Curated narrative passages — must always be tabulated, even if no listed
# root appears. Each entry expands to one or more citations.
NARRATIVE_PASSAGES = [
    # citation_range, label, category
    ("17:1",                "Night Journey (al-Isra')",                  "miracle"),
    ("27:38-40",            "Solomon's throne — before your gaze returns","miracle"),
    ("27:42",               "Throne brought-present (muhdar)",           "miracle"),
    ("27:20-28",            "Hoopoe (hudhud) intelligence-mission",      "miracle"),
    ("19:16-26",            "Maryam's withdrawal, palm tree, dates",     "miracle"),
    ("19:57",               "Idris raised to a lofty place",             "miracle"),
    ("3:55",                "Jesus's tawaffa / raising",                 "miracle"),
    ("4:158",               "Jesus raised — bal rafa'ahu llahu",         "miracle"),
    ("18:9-26",             "Cave Sleepers (full passage)",              "miracle"),
    ("2:259",               "The man revived after 100 years",           "miracle"),
    ("2:260",               "Abraham's four birds",                      "miracle"),
    ("34:12-13",            "Solomon's wind (month-in-a-morning)",       "miracle"),
    ("32:5",                "Angels ascending — 1000-year day",          "eschatological"),
    ("70:3-4",              "Angels — 50000-year day",                   "eschatological"),
    ("16:77",               "Hour as blink-of-eye",                      "eschatological"),
    ("54:50",               "Divine command as blink-of-eye",            "eschatological"),
    ("11:69-83",            "Angels visiting Lot",                       "miracle"),
    ("19:17",               "Angel coming to Maryam",                    "miracle"),
    ("51:24-37",            "Angels visiting Abraham",                   "miracle"),
    ("72:8-9",              "Jinn flight through the heavens",           "miracle"),
    ("37:8-10",             "Jinn eavesdropping, stoned by stars",       "miracle"),
    ("67:5",                "Lamps as missiles for devils",              "miracle"),
    ("15:18",               "Eavesdropper followed by clear flame",      "miracle"),
    ("32:11",               "Angel of death taking souls",               "eschatological"),
    ("39:42",               "God taking souls in death and sleep",       "eschatological"),
    ("21:91",               "Maryam — We breathed into her",             "miracle"),
    ("66:12",               "Maryam — guarded chastity",                 "miracle"),
    ("3:37",                "Provisions appearing in Maryam's mihrab",   "miracle"),
]

# Surah-level priors used for "ritual / legal" baseline contrast
LEGAL_SURAHS = {2, 3, 4, 5, 8, 9, 24, 33, 58, 59, 60, 62, 65}


def expand_range(spec: str):
    """Expand '27:38-40' -> ['27:38','27:39','27:40']. '17:1' -> ['17:1']."""
    if "-" in spec:
        head, tail = spec.split("-")
        surah, start = head.split(":")
        end = int(tail)
        start = int(start)
        return [f"{surah}:{a}" for a in range(start, end + 1)]
    return [spec]


def load_translations():
    trans = {}
    for translator in ("saheeh", "pickthall", "khattab", "arberry"):
        with open(f"/Users/fuyofulo/research/quran/data/translations/{translator}.json") as f:
            trans[translator] = json.load(f)["ayahs"]
    return trans


def load_divergence_data():
    with open("/Users/fuyofulo/research/quran/data/structural/translation-divergence.json") as f:
        return json.load(f)


def load_arabic_by_citation():
    """Build {citation: arabic_text} from the by-surah quran.json."""
    with open("/Users/fuyofulo/research/quran/data/arabic/quran.json") as f:
        data = json.load(f)
    out = {}
    for surah in data["surahs"]:
        s_num = surah["number"]
        for ayah in surah["ayahs"]:
            out[f"{s_num}:{ayah['ayah']}"] = ayah["text"]
    return out


def scan_words_for_teleport_roots():
    """Return {citation: {'roots': sorted-list, 'words': [...]}}."""
    bearing = defaultdict(lambda: {"roots": set(), "words": []})
    print("Scanning words.jsonl for teleportation roots...", file=sys.stderr)
    with open("/Users/fuyofulo/research/quran/data/morphology/words.jsonl") as f:
        for line_num, line in enumerate(f, 1):
            if line_num % 100000 == 0:
                print(f"  {line_num} lines", file=sys.stderr)
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            root = obj.get("root", "")
            if root in TELEPORT_ROOTS:
                surah = obj.get("surah")
                ayah = obj.get("ayah")
                if surah and ayah:
                    citation = f"{surah}:{ayah}"
                    bearing[citation]["roots"].add(root)
                    bearing[citation]["words"].append({
                        "word": obj.get("word"),
                        "form": obj.get("form_buckwalter"),
                        "root": root,
                    })
    for c in bearing:
        bearing[c]["roots"] = sorted(bearing[c]["roots"])
    print(f"Found {len(bearing)} root-bearing ayahs", file=sys.stderr)
    return bearing


def classify_passage(citation, narrative_lookup):
    """miracle | eschatological | legal | other."""
    if citation in narrative_lookup:
        return narrative_lookup[citation]["category"]
    surah = int(citation.split(":")[0])
    if surah in LEGAL_SURAHS:
        return "legal"
    return "other"


def main():
    print("Loading data...", file=sys.stderr)
    bearing = scan_words_for_teleport_roots()
    divergence = load_divergence_data()
    translations = load_translations()
    arabic = load_arabic_by_citation()

    # Build narrative-passage lookup
    narrative_lookup = {}
    for spec, label, category in NARRATIVE_PASSAGES:
        for citation in expand_range(spec):
            narrative_lookup[citation] = {
                "label": label,
                "spec": spec,
                "category": category,
            }
    # Manually injected citations (so they appear even with no root)
    narrative_citations = list(narrative_lookup.keys())
    print(f"Narrative-passage citations: {len(narrative_citations)}", file=sys.stderr)

    # Union: root-bearing ∪ narrative
    universe = set(bearing.keys()) | set(narrative_citations)

    # Enrich
    enriched = []
    missing_div = 0
    for citation in universe:
        if citation not in divergence:
            missing_div += 1
            continue
        div = divergence[citation]
        surah, ayah = map(int, citation.split(":"))
        roots = bearing.get(citation, {}).get("roots", [])
        narrative_meta = narrative_lookup.get(citation)
        category = classify_passage(citation, narrative_lookup)
        enriched.append({
            "citation": citation,
            "surah": surah,
            "ayah": ayah,
            "teleport_roots": roots,
            "narrative_passage": narrative_meta["label"] if narrative_meta else None,
            "narrative_spec": narrative_meta["spec"] if narrative_meta else None,
            "category": category,
            "is_root_bearing": bool(roots),
            "is_narrative": narrative_meta is not None,
            "divergence_score": div["scores"]["combined"],
            "outlier_translator": div["outlier"],
            "regime": div.get("regime", "unknown"),
            "length_variance": div["scores"]["length_variance"],
            "jaccard": div["scores"]["jaccard"],
            "lexical_disagreement": div["scores"]["lexical_disagreement"],
        })
    print(f"Enriched {len(enriched)} ayahs (missed {missing_div})", file=sys.stderr)

    enriched.sort(key=lambda x: x["divergence_score"], reverse=True)

    # ---- Top 50 (overall, root-bearing OR narrative) ----
    top_50 = enriched[:50]

    # ---- Per-root divergence average ----
    root_scores = defaultdict(list)
    for item in enriched:
        for r in item["teleport_roots"]:
            root_scores[r].append(item["divergence_score"])
    per_root_avg = {
        r: sum(s) / len(s) for r, s in root_scores.items()
    }
    per_root_sorted = sorted(per_root_avg.items(), key=lambda x: x[1], reverse=True)
    per_root_counts = {r: len(s) for r, s in root_scores.items()}

    # ---- Per-translator outlier rate ----
    outlier_counts = defaultdict(int)
    total = len(enriched)
    for item in enriched:
        if item["outlier_translator"]:
            outlier_counts[item["outlier_translator"]] += 1
    per_translator_rate = {
        t: count / total for t, count in outlier_counts.items()
    }

    # ---- Surah concentration ----
    surah_counts = defaultdict(lambda: {"count": 0, "sum_div": 0.0})
    for item in enriched:
        s = item["surah"]
        surah_counts[s]["count"] += 1
        surah_counts[s]["sum_div"] += item["divergence_score"]
    for s in surah_counts:
        c = surah_counts[s]["count"]
        surah_counts[s]["avg_divergence"] = surah_counts[s]["sum_div"] / c
    top_surahs = sorted(
        surah_counts.items(),
        key=lambda x: (x[1]["avg_divergence"], x[1]["count"]),
        reverse=True,
    )[:25]
    surah_concentration = {
        str(s): {
            "count": d["count"],
            "avg_divergence": round(d["avg_divergence"], 4),
        } for s, d in top_surahs
    }

    # ---- Narrative panel ----
    narrative_panel = []
    seen_specs = set()
    # group by spec, average within spec
    spec_to_items = defaultdict(list)
    for item in enriched:
        if item["narrative_spec"]:
            spec_to_items[item["narrative_spec"]].append(item)
    spec_summary = []
    for spec, items in spec_to_items.items():
        avg = sum(i["divergence_score"] for i in items) / len(items)
        max_item = max(items, key=lambda i: i["divergence_score"])
        spec_summary.append({
            "spec": spec,
            "label": items[0]["narrative_passage"],
            "category": items[0]["category"],
            "ayah_count": len(items),
            "avg_divergence": round(avg, 4),
            "max_divergence_citation": max_item["citation"],
            "max_divergence_score": round(max_item["divergence_score"], 4),
            "max_outlier": max_item["outlier_translator"],
        })
    spec_summary.sort(key=lambda x: x["avg_divergence"], reverse=True)

    # ---- Miracle vs Legal/Ritual divergence ----
    miracle_divs = [i["divergence_score"] for i in enriched if i["category"] == "miracle"]
    esch_divs = [i["divergence_score"] for i in enriched if i["category"] == "eschatological"]
    legal_divs = [i["divergence_score"] for i in enriched if i["category"] == "legal"]
    other_divs = [i["divergence_score"] for i in enriched if i["category"] == "other"]
    def _avg(xs):
        return round(sum(xs) / len(xs), 4) if xs else None
    miracle_vs_ritual = {
        "miracle_avg": _avg(miracle_divs),
        "miracle_count": len(miracle_divs),
        "eschatological_avg": _avg(esch_divs),
        "eschatological_count": len(esch_divs),
        "legal_avg": _avg(legal_divs),
        "legal_count": len(legal_divs),
        "other_avg": _avg(other_divs),
        "other_count": len(other_divs),
    }

    # ---- Build output JSON ----
    output = {
        "metadata": {
            "teleport_roots": sorted(TELEPORT_ROOTS),
            "teleport_roots_total": len(TELEPORT_ROOTS),
            "narrative_passage_specs": [s for s, _, _ in NARRATIVE_PASSAGES],
            "ayahs_total": len(enriched),
            "root_bearing_total": sum(1 for i in enriched if i["is_root_bearing"]),
            "narrative_only_total": sum(1 for i in enriched if not i["is_root_bearing"] and i["is_narrative"]),
            "divergence_metric": "combined (length_variance + jaccard + lexical_disagreement)",
        },
        "top_50_high_divergence": [
            {
                "citation": i["citation"],
                "roots": i["teleport_roots"],
                "narrative_passage": i["narrative_passage"],
                "category": i["category"],
                "divergence_score": round(i["divergence_score"], 4),
                "outlier_translator": i["outlier_translator"],
                "regime": i["regime"],
            } for i in top_50
        ],
        "per_root_divergence_avg": {
            r: {"avg_divergence": round(s, 4), "ayah_count": per_root_counts[r]}
            for r, s in per_root_sorted
        },
        "per_translator_outlier_rate_on_teleportation": {
            t: round(rate, 4) for t, rate in sorted(per_translator_rate.items(), key=lambda x: x[1], reverse=True)
        },
        "narrative_passage_divergence": spec_summary,
        "surah_concentration": surah_concentration,
        "miracle_vs_ritual": miracle_vs_ritual,
    }

    out_path = Path("/Users/fuyofulo/research/quran/data/structural/teleportation-divergence.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Saved {out_path}", file=sys.stderr)

    # ---- Stash side-by-side details for the markdown writer ----
    side_by_side_path = Path("/tmp/teleportation_top20_panel.json")
    panel = []
    for item in top_50[:20]:
        c = item["citation"]
        panel.append({
            "citation": c,
            "roots": item["teleport_roots"],
            "narrative_passage": item["narrative_passage"],
            "category": item["category"],
            "divergence_score": round(item["divergence_score"], 4),
            "outlier": item["outlier_translator"],
            "regime": item["regime"],
            "arabic": arabic.get(c, ""),
            "saheeh": translations["saheeh"].get(c, ""),
            "pickthall": translations["pickthall"].get(c, ""),
            "khattab": translations["khattab"].get(c, ""),
            "arberry": translations["arberry"].get(c, ""),
        })
    # Also stash narrative panel (top 20) with translations for the markdown
    narrative_top20 = []
    for s in spec_summary[:20]:
        max_c = s["max_divergence_citation"]
        narrative_top20.append({
            **s,
            "arabic": arabic.get(max_c, ""),
            "saheeh": translations["saheeh"].get(max_c, ""),
            "pickthall": translations["pickthall"].get(max_c, ""),
            "khattab": translations["khattab"].get(max_c, ""),
            "arberry": translations["arberry"].get(max_c, ""),
        })
    with open(side_by_side_path, "w") as f:
        json.dump({
            "top20": panel,
            "narrative_top20": narrative_top20,
            "miracle_vs_ritual": miracle_vs_ritual,
            "per_root": per_root_sorted,
            "per_translator": per_translator_rate,
            "surah_concentration": surah_concentration,
            "totals": {
                "ayahs_total": len(enriched),
                "root_bearing": sum(1 for i in enriched if i["is_root_bearing"]),
                "narrative_only": sum(1 for i in enriched if not i["is_root_bearing"] and i["is_narrative"]),
            },
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved {side_by_side_path}", file=sys.stderr)
    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
