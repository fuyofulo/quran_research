#!/usr/bin/env python3
"""Detect ayah echoes, refrains, near-duplicates, and shared formulas in the Quran.

Outputs:
  data/structural/ayah-echoes.json
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QURAN_JSON = ROOT / "data" / "arabic" / "quran.json"
OUT_JSON = ROOT / "data" / "structural" / "ayah-echoes.json"

# ---------- Normalization ----------

# Arabic diacritics + tatweel + small markings
DIACRITICS = re.compile(
    r"[ً-ٰٟۖ-ۭؐ-ؚ࣓-ࣿـ]"
)
# Quranic small letters & rare marks left over
EXTRA_MARKS = re.compile(r"[۪ۜ۟۠ۨ-ۭ]")


def strip_diacritics(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = DIACRITICS.sub("", text)
    text = EXTRA_MARKS.sub("", text)
    return text


def normalize_letters(text: str) -> str:
    """Aggressive normalization for fuzzy matching."""
    t = strip_diacritics(text)
    # Strip zero-width / bidi / format marks
    t = re.sub(r"[​-‏‪-‮⁠﻿]", "", t)
    # Alif variants -> bare alif
    t = re.sub(r"[آأإٱٲٳ]", "ا", t)
    # Alif maksura -> ya
    t = t.replace("ى", "ي")
    # Ta marbuta -> ha
    t = t.replace("ة", "ه")
    # Hamza on waw / ya -> bare
    t = t.replace("ؤ", "و").replace("ئ", "ي")
    # Standalone hamza removed
    t = t.replace("ء", "")
    # Collapse whitespace
    t = re.sub(r"\s+", " ", t).strip()
    return t


def tokenize(text: str) -> list[str]:
    text = normalize_letters(text)
    return [tok for tok in text.split(" ") if tok]


# ---------- Load corpus ----------

def load_ayahs():
    data = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    ayahs = []  # list of (surah, ayah, raw_text, norm_text, tokens)
    for surah in data["surahs"]:
        snum = surah["number"]
        for a in surah["ayahs"]:
            raw = a["text"]
            norm = normalize_letters(raw)
            toks = norm.split(" ") if norm else []
            ayahs.append({
                "surah": snum,
                "ayah": a["ayah"],
                "key": f"{snum}:{a['ayah']}",
                "raw": raw,
                "raw_clean": strip_diacritics(raw),  # keeps alif variants etc.
                "norm": norm,
                "tokens": toks,
            })
    return ayahs


# ---------- N-grams ----------

def word_ngrams(tokens: list[str], n: int) -> list[tuple[str, ...]]:
    if len(tokens) < n:
        return []
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


# ---------- Refrains: identical / near-identical full ayahs ----------

def find_refrains(ayahs):
    by_norm = defaultdict(list)
    for a in ayahs:
        if len(a["tokens"]) >= 2:  # ignore single-word ayahs (mostly muqattaat)
            by_norm[a["norm"]].append(a)
    refrains = []
    for norm, occurrences in by_norm.items():
        if len(occurrences) >= 2:
            # Display canonical with diacritics from first occurrence
            refrains.append({
                "phrase": occurrences[0]["raw"],
                "phrase_normalized": norm,
                "occurrences": [
                    {"surah": o["surah"], "ayah": o["ayah"]} for o in occurrences
                ],
                "count": len(occurrences),
            })
    refrains.sort(key=lambda r: -r["count"])
    return refrains


# ---------- Common closing & opening formulas ----------

def find_endings(ayahs, n_words: int, min_count: int):
    counter = Counter()
    examples = defaultdict(list)
    for a in ayahs:
        if len(a["tokens"]) >= n_words:
            ending = tuple(a["tokens"][-n_words:])
            counter[ending] += 1
            if len(examples[ending]) < 5:
                examples[ending].append({"surah": a["surah"], "ayah": a["ayah"], "text": a["raw"]})
    out = []
    for phrase, count in counter.most_common():
        if count < min_count:
            break
        out.append({
            "phrase_normalized": " ".join(phrase),
            "phrase": " ".join(phrase),
            "count": count,
            "n_words": n_words,
            "examples": examples[phrase][:3],
        })
    return out


def find_openings(ayahs, n_words: int, min_count: int):
    counter = Counter()
    examples = defaultdict(list)
    for a in ayahs:
        if len(a["tokens"]) >= n_words:
            opening = tuple(a["tokens"][:n_words])
            counter[opening] += 1
            if len(examples[opening]) < 5:
                examples[opening].append({"surah": a["surah"], "ayah": a["ayah"], "text": a["raw"]})
    out = []
    for phrase, count in counter.most_common():
        if count < min_count:
            break
        out.append({
            "phrase_normalized": " ".join(phrase),
            "phrase": " ".join(phrase),
            "count": count,
            "n_words": n_words,
            "examples": examples[phrase][:3],
        })
    return out


# ---------- Near-duplicate pairs via shingling + LSH-ish bucketing ----------

def find_near_duplicates(ayahs, n=5, min_jaccard=0.6, min_ayah_len=6):
    """Use word 5-gram shingles. Bucket ayahs by shared 5-grams and only
    score pairs that share at least one rare-ish 5-gram, then verify with
    Jaccard on the full shingle set."""

    # Build shingle sets
    shingles_by_idx: dict[int, set] = {}
    for i, a in enumerate(ayahs):
        toks = a["tokens"]
        if len(toks) < min_ayah_len:
            continue
        shingles_by_idx[i] = set(word_ngrams(toks, n))

    # Inverted index shingle -> list of ayah idx
    inv = defaultdict(list)
    for i, sh in shingles_by_idx.items():
        for s in sh:
            inv[s].append(i)

    # Candidate pairs from shared shingles, but skip ultra-common shingles
    # (which would explode the candidate set without adding signal).
    candidate_pairs = set()
    SHINGLE_CAP = 200  # skip shingles appearing in more than this many ayahs
    for s, idxs in inv.items():
        if len(idxs) < 2 or len(idxs) > SHINGLE_CAP:
            continue
        for i, j in combinations(idxs, 2):
            if i < j:
                candidate_pairs.add((i, j))
    print(f"  candidate pairs: {len(candidate_pairs):,}")

    # Score pairs
    pairs = []
    for i, j in candidate_pairs:
        si, sj = shingles_by_idx[i], shingles_by_idx[j]
        score = jaccard(si, sj)
        if score >= min_jaccard:
            ai, aj = ayahs[i], ayahs[j]
            if ai["norm"] == aj["norm"]:
                continue  # exact dups handled by refrains
            shared_shingles = si & sj
            # Pick the longest contiguous shared run as representative
            shared_ngrams_text = sorted(
                {" ".join(s) for s in shared_shingles}, key=lambda x: -len(x)
            )[:3]
            # Word diff
            wi, wj = set(ai["tokens"]), set(aj["tokens"])
            unique_to_a = list(wi - wj)
            unique_to_b = list(wj - wi)
            pairs.append({
                "ayah_a": ai["key"],
                "ayah_b": aj["key"],
                "similarity": round(score, 4),
                "len_a": len(ai["tokens"]),
                "len_b": len(aj["tokens"]),
                "text_a": ai["raw"],
                "text_b": aj["raw"],
                "shared_phrases": shared_shingles_text if False else shared_ngrams_text,
                "unique_to_a": unique_to_a,
                "unique_to_b": unique_to_b,
            })

    pairs.sort(key=lambda p: -p["similarity"])
    return pairs


# ---------- Echo graph: ayahs that echo many other ayahs ----------

def build_echo_graph(near_duplicates, refrains):
    echoes = defaultdict(list)  # ayah_key -> list of (other_key, score, kind)

    for r in refrains:
        keys = [f"{o['surah']}:{o['ayah']}" for o in r["occurrences"]]
        for k in keys:
            for other in keys:
                if other != k:
                    echoes[k].append({"other": other, "score": 1.0, "kind": "refrain"})

    for p in near_duplicates:
        echoes[p["ayah_a"]].append({
            "other": p["ayah_b"], "score": p["similarity"], "kind": "near_dup"
        })
        echoes[p["ayah_b"]].append({
            "other": p["ayah_a"], "score": p["similarity"], "kind": "near_dup"
        })

    return echoes


# ---------- Main ----------

def main():
    ayahs = load_ayahs()
    print(f"Loaded {len(ayahs)} ayahs")

    print("Finding identical refrains...")
    refrains = find_refrains(ayahs)
    print(f"  {len(refrains)} repeated identical ayahs")

    print("Finding common closings (3-word and 4-word)...")
    closings_3 = find_endings(ayahs, n_words=3, min_count=10)
    closings_4 = find_endings(ayahs, n_words=4, min_count=5)
    closings_2 = find_endings(ayahs, n_words=2, min_count=20)

    print("Finding common openings...")
    openings_2 = find_openings(ayahs, n_words=2, min_count=15)
    openings_3 = find_openings(ayahs, n_words=3, min_count=8)

    print("Finding near-duplicate pairs (this is the slow part)...")
    near_dups = find_near_duplicates(ayahs, n=4, min_jaccard=0.5, min_ayah_len=5)
    print(f"  {len(near_dups)} near-duplicate pairs (jaccard >= 0.5)")

    # Trim to top 200 for the json file (keeps it bounded)
    top_near_dups = near_dups[:200]

    # Identify near-dups that differ by exactly one word in either direction
    one_word_diffs = []
    for p in near_dups:
        if len(p["unique_to_a"]) <= 2 and len(p["unique_to_b"]) <= 2 and p["similarity"] >= 0.7:
            one_word_diffs.append(p)
    one_word_diffs = one_word_diffs[:60]

    print("Building echo graph...")
    echoes = build_echo_graph(near_dups, refrains)

    # Top high-echo ayahs
    high_echo = []
    for k, lst in echoes.items():
        # Deduplicate by 'other'
        seen = {}
        for e in lst:
            if e["other"] not in seen or e["score"] > seen[e["other"]]["score"]:
                seen[e["other"]] = e
        unique_echoes = list(seen.values())
        high_echo.append({
            "ayah": k,
            "n_echoes": len(unique_echoes),
            "echoes": sorted(unique_echoes, key=lambda x: -x["score"])[:15],
        })
    high_echo.sort(key=lambda x: -x["n_echoes"])
    high_echo_top = high_echo[:80]

    # Internal echo per surah (echoes within same surah)
    internal_echo = Counter()
    for p in near_dups:
        sa = int(p["ayah_a"].split(":")[0])
        sb = int(p["ayah_b"].split(":")[0])
        if sa == sb:
            internal_echo[sa] += 1
    for r in refrains:
        surahs_in = [o["surah"] for o in r["occurrences"]]
        c_by_surah = Counter(surahs_in)
        for s, c in c_by_surah.items():
            if c >= 2:
                internal_echo[s] += c * (c - 1) // 2  # pair count

    internal_echo_list = [
        {"surah": s, "internal_echo_pairs": c}
        for s, c in internal_echo.most_common(25)
    ]

    # Cross-surah echo network (count of shared near-dup pairs between surah pairs)
    cross_surah = Counter()
    for p in near_dups:
        sa = int(p["ayah_a"].split(":")[0])
        sb = int(p["ayah_b"].split(":")[0])
        if sa != sb:
            key = tuple(sorted((sa, sb)))
            cross_surah[key] += 1
    cross_surah_list = [
        {"surah_a": k[0], "surah_b": k[1], "shared_pairs": v}
        for k, v in cross_surah.most_common(40)
    ]

    output = {
        "_meta": {
            "ayah_total": len(ayahs),
            "method": "word 5-gram shingling, jaccard >= 0.6 for near-dups; normalization strips diacritics, unifies alif/ya/ta-marbuta variants",
            "min_ayah_len": 6,
        },
        "refrains": refrains,
        "common_closings_3w": closings_3[:60],
        "common_closings_4w": closings_4[:40],
        "common_closings_2w": closings_2[:60],
        "common_openings_2w": openings_2[:60],
        "common_openings_3w": openings_3[:40],
        "near_duplicates": top_near_dups,
        "one_word_diff_pairs": one_word_diffs,
        "high_echo_ayahs": high_echo_top,
        "internal_echo_surahs": internal_echo_list,
        "cross_surah_echo_pairs": cross_surah_list,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
