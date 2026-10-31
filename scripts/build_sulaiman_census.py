#!/usr/bin/env python3
"""Phase-0 census for the Sulaymān (Solomon) investigation.

Question behind it: where does the Quran tell Solomon's story, what beings and gifts fill it, which
words carry it (knowledge, thanks, test, kingdom, turning back), what does it share word-for-word with
David and Job, and where do translators disagree? Emits data/structural/sulaiman-census.json.
"""
import collections, json, os, re, statistics, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Solomon's own passages (his name, or the narrative that carries it).
PASSAGES = {
    "2:102 the devils and sorcery": [(2, 102, 102)],
    "21:78-82 the field, the wind, the divers": [(21, 78, 82)],
    "27:15-44 the ant, the hoopoe, the queen": [(27, 15, 44)],
    "34:12-14 the wind, the copper, his death": [(34, 12, 14)],
    "38:30-40 the horses, the trial, the kingdom": [(38, 30, 40)],
}
# Roots that name the beings, gifts and themes of the story. Buckwalter, case-sensitive.
ROOTS = {
    "beings": {"Tyr": "birds", "nml": "ant", "hdhd": "hoopoe", "jnn": "jinn", "$Tn": "devils", "Efr": "ʿifrīt",
               "Sfn": "horses standing (ṣāfināt)", "jwd": "swift steeds (jiyād)", "jsd": "a body (jasad)", "dbb": "creature of the earth", "jnd": "armies"},
    "gifts": {"rwH": "wind (rīḥ)", "qTr": "molten copper", "Er$": "throne", "SrH": "palace", "mlk": "kingdom / king",
              "sxr": "subjected", "wrv": "inherit", "ETw": "give / gift"},
    "knowledge": {"Elm": "knowledge", "fhm": "understanding", "Hkm": "judgment / wisdom", "nTq": "speech",
                  "ktb": "book / letter", "gyb": "the unseen"},
    "the inner life": {"$kr": "thanks", "blw": "test", "ftn": "trial", "Hmd": "praise", "gfr": "forgive",
                       "Awb": "turning back (awwāb)", "nwb": "turning back (anāba)", "DHk": "smile / laugh",
                       "slm": "submission", "Zlm": "wrong (oneself)", "Hbb": "love", "rDw": "please"},
}
# Fixed phrases to look for corpus-wide (diacritic-stripped Arabic).
PHRASES = {"niʿma l-ʿabd (what an excellent servant)": "نعم العبد",
           "la-zulfā wa ḥusna maʾāb (nearness and a good return)": "لزلفي وحسن ماب",
           "awwāb (always turning back)": "اواب"}


def strip(t):
    t = re.sub(r"ࣰ (?=[اى])", "ࣰ", t)
    t = "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))
    t = t.replace("ٱ", "ا").replace("ى", "ي").replace("ٰ", "")
    t = re.sub("[ۖ-ۭـ‎‏]", "", t)
    return re.sub(r" ا(?= |$)", "ا", t)


def main():
    words = [json.loads(l) for l in open(os.path.join(ROOT, "data/morphology/words.jsonl"))]
    quran = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    arabic = {(s["number"], a["ayah"]): a["text"] for s in quran["surahs"] for a in s["ayahs"]}
    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    echoes = json.load(open(os.path.join(ROOT, "data/structural/ayah-echoes.json")))

    in_passage = {}
    for name, spans in PASSAGES.items():
        for s, a1, a2 in spans:
            for a in range(a1, a2 + 1):
                in_passage[(s, a)] = name
    name_ayahs = sorted({(w["surah"], w["ayah"]) for w in words if w["lemma"] == "sulayoma`n"})
    david = sorted({(w["surah"], w["ayah"]) for w in words if w["lemma"] == "daAwud"})

    roots = {}
    for group, rs in ROOTS.items():
        roots[group] = {}
        for r, gloss in rs.items():
            hits = [(w["surah"], w["ayah"]) for w in words if w["root"] == r and (w["surah"], w["ayah"]) in in_passage]
            corpus = sum(1 for w in words if w["root"] == r)
            roots[group][r] = {"gloss": gloss, "tokens_in_story": len(hits), "tokens_in_quran": corpus,
                               "ayahs": sorted({f"{s}:{a}" for s, a in hits}, key=lambda k: tuple(map(int, k.split(":"))))}

    phrases = {}
    for label, p in PHRASES.items():
        phrases[label] = [f"{s}:{a}" for (s, a), t in arabic.items() if p in strip(t)]

    combined = {k: v["scores"]["combined"] for k, v in div.items() if isinstance(v, dict) and "scores" in v}
    ranked = sorted(combined.values())
    pct = lambda x: round(100 * sum(1 for y in ranked if y <= x) / len(ranked), 1)
    story_div = sorted(((combined[f"{s}:{a}"], f"{s}:{a}") for (s, a) in in_passage if f"{s}:{a}" in combined), reverse=True)

    keys = {f"{s}:{a}" for s, a in in_passage}
    near = [d for d in echoes["near_duplicates"] if d["ayah_a"] in keys or d["ayah_b"] in keys]

    out = {
        "note": "Phase-0 census for Sulaymān. Story = the five passages below. Root counts are tokens inside "
                "those passages vs the whole Quran. Divergence = combined score from translation-divergence.json "
                "with its corpus percentile.",
        "name": {"tokens": sum(1 for w in words if w["lemma"] == "sulayoma`n"), "ayahs": [f"{s}:{a}" for s, a in name_ayahs]},
        "passages": {n: sum(a2 - a1 + 1 for _, a1, a2 in sp) for n, sp in PASSAGES.items()},
        "story_ayahs": len(in_passage),
        "with_david_same_ayah": [f"{s}:{a}" for s, a in name_ayahs if (s, a) in set(david)],
        "david_ayahs": [f"{s}:{a}" for s, a in david],
        "saba_named": [f"{w['surah']}:{w['ayah']}" for w in words if w["lemma"] == "saba<"],
        "surah_titles_from_the_story": {"27": "an-Naml, The Ant (27:18)", "34": "Sabaʾ, the people of the queen's land (27:22, 34:15)"},
        "roots": roots,
        "shared_phrases": phrases,
        "divergence_top": [{"ref": k, "combined": v, "percentile": pct(v)} for v, k in story_div[:12]],
        "divergence_story_median": statistics.median(v for v, _ in story_div),
        "divergence_corpus_median": statistics.median(ranked),
        "near_duplicates": [{"a": d["ayah_a"], "b": d["ayah_b"], "similarity": d["similarity"]} for d in near],
    }
    dest = os.path.join(ROOT, "data/structural/sulaiman-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}")
    print("name:", out["name"]); print("passages:", out["passages"], "total", out["story_ayahs"])
    print("with David:", out["with_david_same_ayah"]); print("Saba:", out["saba_named"])
    for g, rs in roots.items():
        print(g, {r: (v["tokens_in_story"], v["tokens_in_quran"]) for r, v in rs.items()})
    print("phrases:", phrases)
    print("divergence top:", out["divergence_top"][:8]); print("medians story/corpus:", out["divergence_story_median"], out["divergence_corpus_median"])
    print("near duplicates:", out["near_duplicates"])


if __name__ == "__main__":
    main()
