"""Parse the Quranic Arabic Corpus (QAC) morphology file.

Input:
  data/raw/qac/quranic-corpus-morphology-0.4.txt

Outputs (data/morphology/):
  segments.jsonl   — one JSON record per morphological segment (~128k lines)
  words.jsonl      — segments grouped per word, ~78k lines
  roots.json       — root -> {count, occurrences[], lemmas[], pos_dist}
  lemmas.json      — lemma -> {count, occurrences[], root, pos_dist}
  stats.json       — counts: surahs, ayahs, words, segments, roots, lemmas

Each segment has:
  location: [surah, ayah, word, segment]
  segment_type: PREFIX | STEM | SUFFIX
  form_buckwalter, form_arabic
  tag: morphological tag (POS-ish, e.g. N, V, P, PN, DET)
  pos, lemma, root  (only present on STEM segments, when annotated)
  features: dict of remaining features (e.g. M/F gender, NOM/ACC/GEN case, etc.)
  flags: list of bare flags (e.g. STEM, M, GEN)
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from buckwalter import to_arabic

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "raw" / "qac" / "quranic-corpus-morphology-0.4.txt"
OUT = ROOT / "data" / "morphology"
OUT.mkdir(parents=True, exist_ok=True)

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")

# Load POS legend (English tag -> Arabic name + classical category).
# Built once at import; lookups are O(1) via dict.
with (OUT / "pos_legend.json").open() as _f:
    _POS_LEGEND = json.load(_f)["tags"]


def pos_arabic(tag):
    return _POS_LEGEND.get(tag, {}).get("pos_arabic")


def pos_category(tag):
    return _POS_LEGEND.get(tag, {}).get("category")


def parse_location(s: str):
    m = LOC_RE.match(s)
    if not m:
        raise ValueError(f"bad location: {s!r}")
    return tuple(int(x) for x in m.groups())


def parse_features(s: str):
    """Split FEATURES by '|'. Each chunk is either KEY:VALUE or a bare flag.
    Special: the segment type (PREFIX/STEM/SUFFIX) is always first."""
    parts = s.split("|")
    seg_type = parts[0]
    pos = lemma = root = None
    features = {}
    flags = []
    for p in parts[1:]:
        if not p:
            continue
        if ":" in p:
            k, v = p.split(":", 1)
            if k == "POS":
                pos = v
            elif k == "LEM":
                lemma = v
            elif k == "ROOT":
                root = v
            else:
                features[k] = v
        else:
            flags.append(p)
    return seg_type, pos, lemma, root, features, flags


def parse():
    segments = []
    skipped = 0
    with SRC.open() as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("LOCATION"):
                skipped += 1
                continue
            try:
                loc_str, form, tag, feats = line.split("\t")
            except ValueError:
                skipped += 1
                continue
            surah, ayah, word, seg = parse_location(loc_str)
            seg_type, pos, lemma, root, features, flags = parse_features(feats)
            segments.append({
                "location": [surah, ayah, word, seg],
                "surah": surah,
                "ayah": ayah,
                "word": word,
                "segment": seg,
                "segment_type": seg_type,
                "form_buckwalter": form,
                "form_arabic": to_arabic(form),
                "tag": tag,
                "pos": pos,
                "pos_arabic": pos_arabic(pos) if pos else None,
                "pos_category": pos_category(pos) if pos else None,
                "lemma": lemma,
                "lemma_arabic": to_arabic(lemma) if lemma else None,
                "root": root,
                "root_arabic": to_arabic(root) if root else None,
                "features": features,
                "flags": flags,
            })
    print(f"parsed {len(segments)} segments (skipped {skipped} non-data lines)")
    return segments


def write_jsonl(records, path):
    with path.open("w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {path.name}  ({len(records)} records)")


def group_into_words(segments):
    """Group segments into words. Each word = all segments sharing
    (surah, ayah, word). The 'primary' segment is the STEM."""
    by_word = defaultdict(list)
    for s in segments:
        by_word[(s["surah"], s["ayah"], s["word"])].append(s)

    words = []
    for key in sorted(by_word.keys()):
        segs = sorted(by_word[key], key=lambda s: s["segment"])
        stem = next((s for s in segs if s["segment_type"] == "STEM"), None)
        full_form_buck = "".join(s["form_buckwalter"] for s in segs)
        words.append({
            "location": list(key),
            "surah": key[0],
            "ayah": key[1],
            "word": key[2],
            "form_buckwalter": full_form_buck,
            "form_arabic": to_arabic(full_form_buck),
            "segment_count": len(segs),
            "pos": stem["pos"] if stem else None,
            "pos_arabic": stem["pos_arabic"] if stem else None,
            "pos_category": stem["pos_category"] if stem else None,
            "lemma": stem["lemma"] if stem else None,
            "lemma_arabic": stem["lemma_arabic"] if stem else None,
            "root": stem["root"] if stem else None,
            "root_arabic": stem["root_arabic"] if stem else None,
            "tag": stem["tag"] if stem else None,
            "features": stem["features"] if stem else {},
            "flags": stem["flags"] if stem else [],
            "segments": [
                {
                    "segment": s["segment"],
                    "segment_type": s["segment_type"],
                    "form_buckwalter": s["form_buckwalter"],
                    "form_arabic": s["form_arabic"],
                    "tag": s["tag"],
                    "pos": s["pos"],
                    "features": s["features"],
                    "flags": s["flags"],
                }
                for s in segs
            ],
        })
    print(f"grouped into {len(words)} words")
    return words


def build_root_index(words):
    """root (Buckwalter) -> aggregated info."""
    roots = defaultdict(lambda: {
        "root": None,
        "root_arabic": None,
        "count": 0,
        "lemmas": Counter(),
        "pos_dist": Counter(),
        "occurrences": [],
    })
    for w in words:
        if not w["root"]:
            continue
        r = roots[w["root"]]
        r["root"] = w["root"]
        r["root_arabic"] = w["root_arabic"]
        r["count"] += 1
        if w["lemma"]:
            r["lemmas"][w["lemma"]] += 1
        if w["pos"]:
            r["pos_dist"][w["pos"]] += 1
        r["occurrences"].append({
            "location": w["location"],
            "form_arabic": w["form_arabic"],
            "lemma": w["lemma"],
            "lemma_arabic": w["lemma_arabic"],
            "pos": w["pos"],
        })

    out = {}
    for k, v in roots.items():
        out[k] = {
            "root": v["root"],
            "root_arabic": v["root_arabic"],
            "count": v["count"],
            "lemmas": dict(v["lemmas"].most_common()),
            "pos_dist": dict(v["pos_dist"].most_common()),
            "occurrences": v["occurrences"],
        }
    print(f"built root index: {len(out)} unique roots")
    return out


def build_lemma_index(words):
    lemmas = defaultdict(lambda: {
        "lemma": None,
        "lemma_arabic": None,
        "root": None,
        "root_arabic": None,
        "count": 0,
        "pos_dist": Counter(),
        "occurrences": [],
    })
    for w in words:
        if not w["lemma"]:
            continue
        l = lemmas[w["lemma"]]
        l["lemma"] = w["lemma"]
        l["lemma_arabic"] = w["lemma_arabic"]
        l["root"] = w["root"]
        l["root_arabic"] = w["root_arabic"]
        l["count"] += 1
        if w["pos"]:
            l["pos_dist"][w["pos"]] += 1
        l["occurrences"].append({
            "location": w["location"],
            "form_arabic": w["form_arabic"],
            "pos": w["pos"],
        })

    out = {}
    for k, v in lemmas.items():
        out[k] = {
            "lemma": v["lemma"],
            "lemma_arabic": v["lemma_arabic"],
            "root": v["root"],
            "root_arabic": v["root_arabic"],
            "count": v["count"],
            "pos_dist": dict(v["pos_dist"].most_common()),
            "occurrences": v["occurrences"],
        }
    print(f"built lemma index: {len(out)} unique lemmas")
    return out


def build_stats(segments, words, roots, lemmas):
    surahs = {s["surah"] for s in segments}
    ayahs = {(s["surah"], s["ayah"]) for s in segments}
    words_with_root = sum(1 for w in words if w["root"])
    words_with_lemma = sum(1 for w in words if w["lemma"])
    return {
        "surahs": len(surahs),
        "ayahs": len(ayahs),
        "words": len(words),
        "segments": len(segments),
        "words_with_root": words_with_root,
        "words_with_lemma": words_with_lemma,
        "unique_roots": len(roots),
        "unique_lemmas": len(lemmas),
    }


if __name__ == "__main__":
    segments = parse()
    words = group_into_words(segments)
    roots = build_root_index(words)
    lemmas = build_lemma_index(words)
    stats = build_stats(segments, words, roots, lemmas)

    write_jsonl(segments, OUT / "segments.jsonl")
    write_jsonl(words, OUT / "words.jsonl")
    with (OUT / "roots.json").open("w") as f:
        json.dump(roots, f, ensure_ascii=False, indent=2)
    print(f"wrote roots.json  ({len(roots)} roots)")
    with (OUT / "lemmas.json").open("w") as f:
        json.dump(lemmas, f, ensure_ascii=False, indent=2)
    print(f"wrote lemmas.json  ({len(lemmas)} lemmas)")
    with (OUT / "stats.json").open("w") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"stats: {stats}")
