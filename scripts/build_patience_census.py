#!/usr/bin/env python3
"""Phase-0 census for the patience (sabr) investigation. Deterministic.

  1. Lemma table for Sbr; mood / person; Meccan vs Medinan.
  2. Imperatives and who they are addressed to (hand-annotated).
  3. What follows the word: patience over (EalaY), for (li-), until (Hatta), with (maEa).
  4. Misdirected patience: the uses the text does not praise (hand-annotated).
  5. Formulas: "with the patient", "for what they endured", sabbar shakur, sabr jamil, "pour patience",
     "matters of resolve", "you will find me, God willing", "without account", "twice".
  6. Pairings in the same ayah (prayer, taqwa, thanks, reliance, truth, mercy, certainty, forgiveness...).
  7. The neighbouring and contrasting vocabulary: panic, haste, weakening, swallowing grief, forbearance,
     standing firm, despair.
  8. Densest passage (18:60-82), the commands to the Prophet and what follows each, divergence, echoes.
Emits data/structural/patience-census.json.
"""
import json, os, re, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(t):
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub("[ٱأإآ]", "ا", t).replace("ى", "ي").replace("ـ", "").replace("ة", "ه")
    t = re.sub("[ۖ-ۭ]", "", t)
    # quran.json writes open-fathatan (U+08F0) tanwin with a SPACE before the alif — rejoin
    # it (see notes/agent-context.md, "Arabic text normalization").
    return re.sub(r" ا(?= |$)", "ا", t)


def key(r):
    return tuple(map(int, r.split(":")))


PERSON = ("1S", "1P", "2MS", "2FS", "2MP", "3MS", "3FS", "3MP")

# Every imperative of Sbr, and who is told (hand-annotated from context).
IMPV_ADDRESSEE = {
    "3:200": "the believers (isbiru, sabiru)", "7:87": "Shu`ayb to both groups of his people: until God judges",
    "7:128": "Moses to his people: seek help through God and be patient", "8:46": "the believers, in battle",
    "10:109": "the Prophet: until God judges", "11:49": "the Prophet, after Noah's story: the end is for the mindful",
    "11:115": "the Prophet: God does not lose the reward of those who do good", "16:127": "the Prophet: your patience is only through God",
    "18:28": "the Prophet: keep yourself patient with those who call on their Lord", "19:65": "the Prophet: worship Him and be steadfast in His worship (istabir)",
    "20:130": "the Prophet: over what they say; glorify with praise", "20:132": "the Prophet: enjoin prayer on your family and be steadfast in it (istabir)",
    "30:60": "the Prophet: God's promise is true", "31:17": "Luqman to his son: over what befalls you",
    "38:6": "MISDIRECTED: the chiefs to each other: be patient over your gods", "38:17": "the Prophet: over what they say; remember David",
    "40:55": "the Prophet: God's promise is true; ask forgiveness; glorify", "40:77": "the Prophet: God's promise is true",
    "46:35": "the Prophet: as the messengers of resolve were patient; do not hasten", "50:39": "the Prophet: over what they say; glorify",
    "52:16": "MISDIRECTED: the damned: be patient or not, it is the same", "52:48": "the Prophet: for your Lord's judgment; you are in Our eyes; glorify",
    "54:27": "Salih: watch them and be steadfast (istabir)", "68:48": "the Prophet: for your Lord's judgment; not like the man of the fish",
    "70:5": "the Prophet: beautiful patience", "73:10": "the Prophet: over what they say; leave them graciously",
    "74:7": "the Prophet: for your Lord", "76:24": "the Prophet: for your Lord's judgment; do not obey the sinner",
}
# Patience the text does not praise: its object or its owner is wrong, or it no longer helps.
MISDIRECTED = {
    "2:61": "Israel: 'we will never be patient with one kind of food'",
    "2:175": "'how patient they are for the Fire!' (afaal of wonder)",
    "14:21": "the weak in Hell: 'whether we panic or are patient, there is no escape'",
    "25:42": "the deniers: 'he nearly led us from our gods, had we not been patient over them'",
    "38:6": "the chiefs: 'be patient over your gods'",
    "41:24": "'if they are patient, the Fire is their abode'",
    "52:16": "'be patient or not, it is the same for you'",
}
PREP = {"EalaY`": "over (EalaY)", "EalaY": "over (EalaY)", "EalayohaA": "over (EalaY)", "EalaY`^": "over (EalaY)",
        "Hat~aY`": "until (Hatta)", "maEa": "with (maEa)"}
FORMULAS = {
    "with_the_patient (maEa al-sabirin)": r"مع الصبرين",
    "loves_the_patient": r"يحب الصبرين",
    "give_good_news_to_the_patient": r"بشر الصبرين",
    "for_what_they_endured (bima sabaru / sabartum)": r"بما صبر",
    "sabbar_shakur": r"صبار شكور",
    "sabr_jamil": r"صبر جميل|صبرا جميلا",
    "pour_patience_upon_us": r"افرغ علينا صبرا",
    "matters_of_resolve (min `azm al-umur)": r"عزم الامور",
    "you_will_find_me_god_willing": r"ستجدني ان شا",
    "without_account (bi-ghayri hisab)": r"بغير حساب",
    "your_lords_judgment (li-hukmi rabbik)": r"لحكم ربك",
    "gods_promise_is_true": r"ان وعد الله حق",
    "only_the_patient_are_granted_it": r"(ولا|وما) يلقىها|(ولا|وما) يلقيها|يلقيها الا|يلقىها الا",
    "advised_one_another_to_patience": r"تواصوا بالصبر",
    "until_god_judges": r"حتي يحكم الله",
}
PAIR_ROOTS = {"Slw": "prayer", "wqy": "mindfulness (taqwa)", "$kr": "thanks", "wkl": "reliance", "Hqq": "truth",
              "rHm": "mercy", "yqn": "certainty", "gfr": "forgiveness", "Ezm": "resolve", "jzy": "recompense",
              "Ajr": "reward", "Hzn": "grief", "sbH": "glorify", "Hmd": "praise", "wEd": "promise", "Hkm": "judgment",
              "blw": "test (bala')", "ftn": "trial (fitna)", "Elm": "knowledge", "xbr": "knowledge (khubr)",
              "nSr": "help", "tqw": "taqwa", "Hbb": "love", "b$r": "good news", "Emn": "faith (dupe)", "Amn": "faith"}
NEIGHBOURS = {"jzE": "panic (jaza`)", "hlE": "restless (halu`)", "Ejl": "haste", "whn": "weakening",
              "kZm": "swallowing (grief, anger)", "Hlm": "forbearance (hilm)", "vbt": "standing firm",
              "qnT": "despair (qunut)", "yAs": "despair (ya's)", "rbT": "binding / stationing", "Hzn": "grief"}


def main():
    W = [json.loads(l) for l in open(os.path.join(ROOT, "data/morphology/words.jsonl"))]
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    A = {f'{s["number"]}:{a["ayah"]}': norm(a["text"]) for s in q["surahs"] for a in s["ayahs"]}
    REV = {s["number"]: s["revelation"] for s in q["surahs"]}
    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    echoes = json.load(open(os.path.join(ROOT, "data/structural/ayah-echoes.json")))
    roots_in = defaultdict(set)
    by_root = defaultdict(list)
    toks = []
    for i, w in enumerate(W):
        r = w.get("root")
        if not r:
            continue
        ref = f'{w["surah"]}:{w["ayah"]}'
        roots_in[ref].add(r)
        by_root[r].append(ref)
        if r == "Sbr":
            fl = w.get("flags") or []
            nxt = W[i + 1]["form_buckwalter"] if i + 1 < len(W) and W[i + 1]["surah"] == w["surah"] and W[i + 1]["ayah"] == w["ayah"] else ""
            nxt2 = W[i + 2]["form_buckwalter"] if i + 2 < len(W) and W[i + 2]["ayah"] == w["ayah"] else ""
            toks.append({"ref": ref, "lemma": w["lemma"], "form": w["form_buckwalter"], "pos": w["pos"],
                         "mood": next((x for x in ("IMPV", "IMPF", "PERF") if x in fl), "NOUN/PCPL"),
                         "person": next((x for x in PERSON if x in fl), ""), "next": nxt, "next2": nxt2,
                         "revelation": REV[w["surah"]]})
    ayahs = sorted({t["ref"] for t in toks}, key=key)
    out = {"note": "Phase-0 census, patience (sabr). See scripts/build_patience_census.py."}
    out["sbr"] = {
        "tokens": len(toks), "ayahs": len(ayahs), "surahs": len({a.split(":")[0] for a in ayahs}),
        "lemmas": Counter(t["lemma"] for t in toks).most_common(),
        "mood_person": Counter(f'{t["mood"]} {t["person"]}'.strip() for t in toks).most_common(),
        "verbal_tokens": sum(1 for t in toks if t["pos"] == "V"),
        "revelation_tokens": dict(Counter(t["revelation"] for t in toks)),
        "revelation_ayahs": dict(Counter(REV[int(a.split(":")[0])] for a in ayahs)),
        "by_surah_top": Counter(t["ref"].split(":")[0] for t in toks).most_common(10),
        "ayah_list": ayahs,
    }
    impv = sorted({t["ref"] for t in toks if t["mood"] == "IMPV"}, key=key)
    out["imperatives"] = {
        "tokens": sum(1 for t in toks if t["mood"] == "IMPV"), "ayahs": impv,
        "singular_2MS": sorted({t["ref"] for t in toks if t["mood"] == "IMPV" and t["person"] == "2MS"}, key=key),
        "plural_2MP": sorted({t["ref"] for t in toks if t["mood"] == "IMPV" and t["person"] == "2MP"}, key=key),
        "addressee": IMPV_ADDRESSEE, "missing_annotation": [r for r in impv if r not in IMPV_ADDRESSEE],
        "to_the_prophet": sorted([r for r, v in IMPV_ADDRESSEE.items() if v.startswith("the Prophet")], key=key),
        "to_the_prophet_by_revelation": dict(Counter(REV[int(r.split(":")[0])] for r, v in IMPV_ADDRESSEE.items() if v.startswith("the Prophet"))),
    }
    objs = defaultdict(list)
    for t in toks:
        lab = PREP.get(t["next"])
        if not lab and t["next"].startswith(("liHukomi", "lirab~ika", "liEiba`datihi", "liEibaAdatihi")):
            lab = "for (li-)"
        if not lab and t["next"] == "nafosaka" and t["next2"] == "maEa":
            lab = "with (maEa)"
        if lab:
            objs[lab].append(t["ref"])
    out["what_follows"] = {k: sorted(set(v), key=key) for k, v in objs.items()}
    out["misdirected"] = MISDIRECTED
    out["formulas"] = {k: sorted([r for r, t in A.items() if re.search(p, t)], key=key) for k, p in FORMULAS.items()}
    out["pairs_same_ayah"] = {f"{r2} {lab}": sorted([a for a in ayahs if r2 in roots_in[a]], key=key)
                              for r2, lab in PAIR_ROOTS.items() if r2 in by_root}
    out["neighbours"] = {f"{r2} {lab}": {"tokens": len(by_root[r2]), "ayahs": sorted(set(by_root[r2]), key=key)[:60],
                                         "with_Sbr_same_ayah": sorted({a for a in by_root[r2] if "Sbr" in roots_in[a]}, key=key)}
                         for r2, lab in NEIGHBOURS.items()}
    kh = [t for t in toks if t["ref"].startswith("18:") and 60 <= key(t["ref"])[1] <= 82]
    out["densest_passage_18_60_82"] = {"tokens": len(kh), "refs": [t["ref"] for t in kh],
                                       "share_of_all": round(len(kh) / len(toks), 3)}
    out["god_as_subject_of_Sbr"] = "none: no Sbr verb has God as its subject, and al-Sabur is not a Quranic name (hand-checked against ayah_list)"
    near = [e for e in echoes["near_duplicates"] if e["ayah_a"] in ayahs or e["ayah_b"] in ayahs]
    out["near_duplicates"] = [(e["ayah_a"], e["ayah_b"], e["similarity"]) for e in near]
    scored = [(r, div[r]["scores"]["combined"]) for r in ayahs if r in div]
    allsc = sorted(v["scores"]["combined"] for v in div.values())
    pct = lambda x: round(100 * sum(1 for s in allsc if s <= x) / len(allsc))
    sc = sorted(s for _, s in scored)
    out["divergence"] = {"median_sbr": sc[len(sc) // 2], "median_corpus": allsc[len(allsc) // 2],
                         "top": [(r, s, pct(s)) for r, s in sorted(scored, key=lambda x: -x[1])[:12]]}
    dest = os.path.join(ROOT, "data/structural/patience-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print("wrote", dest)
    s = out["sbr"]
    print("tokens", s["tokens"], "ayahs", s["ayahs"], "surahs", s["surahs"], "verbal", s["verbal_tokens"])
    print("lemmas", s["lemmas"]); print("mood/person", s["mood_person"])
    print("rev tokens", s["revelation_tokens"], "rev ayahs", s["revelation_ayahs"], "top surahs", s["by_surah_top"])
    i = out["imperatives"]
    print("impv tokens", i["tokens"], "ayahs", len(i["ayahs"]), "missing", i["missing_annotation"])
    print("to prophet", len(i["to_the_prophet"]), i["to_the_prophet_by_revelation"])
    print("follows", {k: len(v) for k, v in out["what_follows"].items()}, out["what_follows"])
    for k, v in out["formulas"].items():
        print(" ", k, v)
    print("pairs", {k: len(v) for k, v in out["pairs_same_ayah"].items() if v})
    for k, v in out["neighbours"].items():
        print(" ", k, v["tokens"], "withSbr", v["with_Sbr_same_ayah"])
    print("18:60-82", out["densest_passage_18_60_82"])
    print("near dups", out["near_duplicates"])
    print("divergence", out["divergence"])


if __name__ == "__main__":
    main()
