"""Build a concept profile for a single Arabic root.

A "concept" is anchored on a root (e.g. rHm = ر-ح-م = mercy/womb). The profile
captures everything we know about how that root behaves in the Quran:

  - All lemmas derived from it, with counts and POS
  - Every occurrence with its ayah text and surah context
  - Co-occurrence with other roots inside the same ayah (the semantic field)
  - Distribution across surahs and Meccan vs Medinan revelation

Output: data/concepts/<root>.json

Schema (the same shape applies to every root, so this scales to all 1,642):

  {
    root, root_arabic,
    stats: { occurrences, lemmas, ayahs, surahs, pos_distribution },
    lemmas: [ {lemma, lemma_arabic, count, pos_distribution, occurrences[]} ],
    co_occurring_roots: [ {root, root_arabic, ayahs_together, share} ],
    distribution: {
      by_surah:        [ {surah, name, revelation, occurrences} ],
      by_revelation:   {Meccan, Medinan},
    },
    all_occurrences: [ {location, form_arabic, lemma, pos, ayah_id, ayah_arabic, surah_revelation} ],
  }

Usage:  python3 scripts/build_concept.py rHm
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MORPH = ROOT_DIR / "data" / "morphology"
ARABIC = ROOT_DIR / "data" / "arabic"
TRANS = ROOT_DIR / "data" / "translations"
OUT_DIR = ROOT_DIR / "data" / "concepts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Translations are display-only annotations on the Arabic. They are NEVER
# used as input to analysis (clusters, co-occurrence, distribution all derive
# from morphology + canonical text). They appear at occurrence level only,
# and always plural — disagreement between translators is preserved as signal.
SENTENCE_TRANSLATIONS = ["saheeh", "pickthall", "khattab", "arberry"]


def load_words():
    """Return list of all words (each with surah/ayah/word/root/lemma/pos)."""
    out = []
    with (MORPH / "words.jsonl").open() as f:
        for line in f:
            out.append(json.loads(line))
    return out


def load_quran():
    """Return: ayah_text[(surah, ayah)] = arabic_text; surah_meta[surah] = {...}."""
    with (ARABIC / "quran.json").open() as f:
        q = json.load(f)
    ayah_text = {}
    surah_meta = {}
    for s in q["surahs"]:
        surah_meta[s["number"]] = {
            "name_english": s["name_english"],
            "name_arabic": s["name_arabic"],
            "name_translation": s["name_translation"],
            "revelation": s["revelation"],
            "ayah_count": s["ayah_count"],
        }
        for a in s["ayahs"]:
            ayah_text[(s["number"], a["ayah"])] = a["text"]
    return ayah_text, surah_meta


def load_translations():
    """Return: sentences[source][ayah_id] = text; words[loc] = literal_gloss.

    Returns empty dicts if files don't exist (translations are optional)."""
    sentences = {}
    for sid in SENTENCE_TRANSLATIONS:
        path = TRANS / f"{sid}.json"
        if not path.exists():
            continue
        with path.open() as f:
            sentences[sid] = json.load(f)["ayahs"]
    wbw = {}
    wbw_path = TRANS / "word-by-word.json"
    if wbw_path.exists():
        with wbw_path.open() as f:
            wbw = json.load(f)["words"]
    return sentences, wbw


def build_concept(target_root, words, ayah_text, surah_meta, sentences=None, wbw=None):
    """Build the concept profile.

    Translations (sentences, wbw) are attached as display annotations only.
    They are NOT used in any of the analytical computations below — clusters,
    co-occurrence, lemma groupings, distributions all derive from Arabic
    morphology and canonical text. This is the methodological discipline:
    Arabic is primary, English is annotation."""
    sentences = sentences or {}
    wbw = wbw or {}

    # All occurrences of the target root, in order.
    target_occs = [w for w in words if w["root"] == target_root]
    if not target_occs:
        raise SystemExit(f"root {target_root!r} not found")

    root_arabic = target_occs[0]["root_arabic"]

    # All ayahs containing the target root.
    target_ayahs = {(w["surah"], w["ayah"]) for w in target_occs}

    # Index: ayah -> all roots present in it (for co-occurrence).
    ayah_roots = defaultdict(set)
    for w in words:
        if w["root"]:
            ayah_roots[(w["surah"], w["ayah"])].add(w["root"])

    # Map root -> arabic for co-occurrence display
    root_to_arabic = {}
    for w in words:
        if w["root"] and w["root"] not in root_to_arabic:
            root_to_arabic[w["root"]] = w["root_arabic"]

    # Lemma rollups.
    lemma_groups = defaultdict(list)
    for w in target_occs:
        lemma_groups[w["lemma"]].append(w)

    lemmas = []
    for lem, occs in sorted(lemma_groups.items(), key=lambda kv: -len(kv[1])):
        lemmas.append({
            "lemma": lem,
            "lemma_arabic": occs[0]["lemma_arabic"],
            "count": len(occs),
            "pos_distribution": dict(Counter(o["pos"] for o in occs).most_common()),
            "first_occurrence": occs[0]["location"],
            "occurrences": [
                {
                    "location": o["location"],
                    "form_arabic": o["form_arabic"],
                    "pos": o["pos"],
                }
                for o in occs
            ],
        })

    # Co-occurring roots: ayahs in which other roots appear together with target.
    co_root_counter = Counter()
    co_root_first_ayah = {}
    for ay in target_ayahs:
        for r in ayah_roots[ay]:
            if r == target_root:
                continue
            co_root_counter[r] += 1
            if r not in co_root_first_ayah or ay < co_root_first_ayah[r]:
                co_root_first_ayah[r] = ay

    co_occurring_roots = []
    for r, c in co_root_counter.most_common():
        co_occurring_roots.append({
            "root": r,
            "root_arabic": root_to_arabic.get(r, ""),
            "ayahs_together": c,
            "share": round(c / len(target_ayahs), 4),
            "first_together": list(co_root_first_ayah[r]),
        })

    # Distribution by surah.
    surah_counter = Counter(w["surah"] for w in target_occs)
    by_surah = []
    for s, c in surah_counter.most_common():
        meta = surah_meta[s]
        by_surah.append({
            "surah": s,
            "name_english": meta["name_english"],
            "name_arabic": meta["name_arabic"],
            "revelation": meta["revelation"],
            "occurrences": c,
        })

    by_revelation = Counter(surah_meta[w["surah"]]["revelation"] for w in target_occs)

    # All occurrences (flat) with ayah text and (optional) translation overlay.
    all_occurrences = []
    for w in target_occs:
        ay = (w["surah"], w["ayah"])
        ayah_id = f"{w['surah']}:{w['ayah']}"
        loc_id = f"{w['surah']}:{w['ayah']}:{w['word']}"
        rec = {
            "location": w["location"],
            "form_arabic": w["form_arabic"],
            "lemma": w["lemma"],
            "lemma_arabic": w["lemma_arabic"],
            "pos": w["pos"],
            "ayah_id": ayah_id,
            "ayah_arabic": ayah_text[ay],
            "surah_revelation": surah_meta[w["surah"]]["revelation"],
            "surah_name": surah_meta[w["surah"]]["name_english"],
        }
        # Display-only translation overlay. Plural by design — disagreement is signal.
        if wbw and loc_id in wbw:
            rec["literal_gloss"] = wbw[loc_id]
        if sentences:
            rec["translations"] = {sid: ayahs.get(ayah_id, "") for sid, ayahs in sentences.items()}
        all_occurrences.append(rec)

    pos_dist = dict(Counter(w["pos"] for w in target_occs).most_common())

    return {
        "root": target_root,
        "root_arabic": root_arabic,
        "stats": {
            "occurrences": len(target_occs),
            "lemmas": len(lemma_groups),
            "ayahs": len(target_ayahs),
            "surahs": len(surah_counter),
            "pos_distribution": pos_dist,
        },
        "lemmas": lemmas,
        "co_occurring_roots": co_occurring_roots,
        "distribution": {
            "by_surah": by_surah,
            "by_revelation": dict(by_revelation),
        },
        "all_occurrences": all_occurrences,
    }


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_concept.py <root_buckwalter>")
    target = sys.argv[1]

    print(f"loading words…")
    words = load_words()
    print(f"loading quran text…")
    ayah_text, surah_meta = load_quran()
    print(f"loading translations (display overlay)…")
    sentences, wbw = load_translations()
    print(f"  sources: {list(sentences.keys())}  word-by-word words: {len(wbw)}")
    print(f"building concept for root {target!r}…")
    concept = build_concept(target, words, ayah_text, surah_meta, sentences, wbw)

    out = OUT_DIR / f"{target}.json"
    with out.open("w") as f:
        json.dump(concept, f, ensure_ascii=False, indent=2)

    print(f"\nwrote {out}")
    print(f"  root:        {concept['root_arabic']} ({concept['root']})")
    print(f"  occurrences: {concept['stats']['occurrences']}")
    print(f"  lemmas:      {concept['stats']['lemmas']}")
    print(f"  ayahs:       {concept['stats']['ayahs']}")
    print(f"  surahs:      {concept['stats']['surahs']} / 114")
    print(f"  revelation:  {concept['distribution']['by_revelation']}")
    print(f"\n  top 10 co-occurring roots:")
    for c in concept["co_occurring_roots"][:10]:
        print(f"    {c['root_arabic']:6} ({c['root']:5})  ayahs={c['ayahs_together']:4}  share={c['share']:.2f}")


if __name__ == "__main__":
    main()
