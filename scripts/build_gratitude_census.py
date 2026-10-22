#!/usr/bin/env python3
"""Phase-0 census for the gratitude (shukr) investigation. Deterministic.

  1. Lemma tables: $kr (thanks), Hmd (praise), nEm (blessing), Alw (alaa'), fDl, mnn, kfr.
  2. $kr by person/mood: who is told to thank, who says "that I may thank", who is called
     grateful, and where God Himself is the Thanker (shakur / shakir).
  3. The purpose clause "that you may be grateful" — what each one follows.
  4. The few / the most: "little do you thank", "most of them do not thank".
  5. Thanks against kufr in one ayah; thanks paired with patience, remembrance, worship, faith.
  6. al-hamdu lillah: speaker and occasion; sabbih bi-hamd; the name al-Hamid and its pairs.
  7. Blessing: "remember the blessing of God" commands; 14:34 / 16:18; the alaa' refrain.
  8. Translator divergence over the core set.
Emits data/structural/gratitude-census.json.
"""
import json, os, re, unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(t):
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub("[ٱأإآ]", "ا", t).replace("ى", "ي").replace("ـ", "")
    # quran.json writes open-fathatan (U+08F0) tanwin with a SPACE before the alif — rejoin
    # it (see notes/agent-context.md, "Arabic text normalization").
    return re.sub(r" ا(?= |$)", "ا", t)


def key(r):
    return tuple(map(int, r.split(":")))


ROOTS = ["$kr", "Hmd", "nEm", "Alw", "fDl", "mnn", "kfr", "sbH", "*kr", "gfr", "Sbr", "zyd"]
EXPIATE = {"kaf~ara", "kaf~a`rap"}
PERSON = ("1S", "1P", "2MS", "2FS", "2MP", "3MS", "3FS", "3MP")

# What each "la`allakum tashkurun" (that you may be grateful) follows — hand-annotated.
PURPOSE = {
    "2:52": ("pardon after the calf", "forgiveness / second chance"),
    "2:56": ("revived after death (the thunderbolt)", "forgiveness / second chance"),
    "2:185": ("the fast: ease not hardship, complete the count, magnify God", "law eased"),
    "3:123": ("victory at Badr when few — so fear God", "rescue / victory"),
    "5:6": ("ablution and dry ablution: God wants no hardship, completes His favour", "law eased"),
    "5:89": ("expiation for oaths", "law eased"),
    "8:26": ("few and oppressed — sheltered, supported, provided", "rescue / victory"),
    "16:14": ("the sea subjected: fresh meat, ornaments, ships, His bounty", "creation subjected"),
    "16:78": ("born knowing nothing — given hearing, sight, hearts", "the senses"),
    "22:36": ("sacrificial camels subjected to you", "creation subjected"),
    "28:73": ("night for rest, day to seek His bounty", "creation subjected"),
    "30:46": ("winds bearing good news, rain, ships", "creation subjected"),
    "35:12": ("two seas, fresh meat, ornaments, ships", "creation subjected"),
    "45:12": ("the sea subjected for ships, His bounty", "creation subjected"),
}
FEW = {"7:10": "qalilan ma tashkurun", "23:78": "qalilan ma tashkurun", "32:9": "qalilan ma tashkurun",
       "67:23": "qalilan ma tashkurun", "34:13": "qalilun min `ibadiya al-shakur",
       "2:243": "aktharahum la yashkurun", "10:60": "aktharahum la yashkurun", "12:38": "aktharahum la yashkurun",
       "27:73": "aktharahum la yashkurun", "40:61": "aktharahum la yashkurun",
       "7:17": "Iblis: you will not find most of them grateful"}
GOD_THANKS = {"2:158": "shakir `alim", "4:147": "shakiran `alima", "35:30": "ghafur shakur",
              "35:34": "ghafur shakur (Paradise speech)", "42:23": "ghafur shakur", "64:17": "shakur halim",
              "17:19": "their effort is mashkur (thanked)", "76:22": "your effort is mashkur"}
CALLED_GRATEFUL = {"17:3": "Noah — `abdan shakura", "16:121": "Abraham — shakiran li-an`umih",
                   "34:13": "the family of David — told to work in thanks", "54:35": "Lot's family — man shakar",
                   "21:80": "David's armour — fa-hal antum shakirun?", "14:5": "sabbar shakur (sign for)",
                   "31:31": "sabbar shakur", "34:19": "sabbar shakur", "42:33": "sabbar shakur"}
VOWS = {"6:63": "rescue from darknesses of land and sea", "10:22": "ship in a storm",
        "7:189": "a couple asking for a sound child"}
HAMD_SPEAKERS = {
    "1:2": "the reciter (Fatiha)", "6:1": "opening — creation", "6:45": "after the wrongdoers' end",
    "7:43": "the people of Paradise", "10:10": "the people of Paradise — their last call",
    "14:39": "Abraham — sons in old age", "16:75": "after a parable", "17:111": "commanded: say",
    "18:1": "opening — the Book", "23:28": "Noah, commanded on boarding the ark",
    "27:15": "David and Solomon — knowledge", "27:59": "commanded: say", "27:93": "commanded: say",
    "29:63": "commanded: say — after they admit God sends rain", "31:25": "commanded: say — after they admit God created",
    "34:1": "opening — all in heavens and earth", "35:1": "opening — Creator", "35:34": "the people of Paradise — grief removed",
    "37:182": "closing of the surah", "39:29": "after a parable", "39:74": "the people of Paradise — promise fulfilled",
    "39:75": "closing — the angels; it is said: praise to God", "40:65": "call on Him sincerely — praise to God",
}


def main():
    W = [json.loads(l) for l in open(os.path.join(ROOT, "data/morphology/words.jsonl"))]
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    A = {f'{s["number"]}:{a["ayah"]}': norm(a["text"]) for s in q["surahs"] for a in s["ayahs"]}
    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    by_root = defaultdict(list)
    roots_in = defaultdict(set)
    shukr_tokens = []
    for w in W:
        r = w.get("root")
        if not r:
            continue
        ref = f'{w["surah"]}:{w["ayah"]}'
        if r == "kfr" and w["lemma"] in EXPIATE:
            r = "kfr-expiate"   # polysemy: kaffara / kaffara = expiate, not deny or be ungrateful
        by_root[r].append((ref, w["lemma"]))
        roots_in[ref].add(r)
        if r == "$kr":
            fl = w.get("flags") or []
            shukr_tokens.append({"ref": ref, "lemma": w["lemma"], "form": w["form_buckwalter"],
                                 "mood": next((x for x in ("IMPV", "IMPF", "PERF") if x in fl), "NOUN/PCPL"),
                                 "person": next((x for x in PERSON if x in fl), "")})
    out = {"note": "Phase-0 census, gratitude. See scripts/build_gratitude_census.py."}
    out["lemma_tables"] = {r: {"tokens": len(by_root[r]), "ayahs": len({o[0] for o in by_root[r]}),
                               "lemmas": Counter(o[1] for o in by_root[r]).most_common()} for r in ROOTS}
    shukr_ayahs = sorted({t["ref"] for t in shukr_tokens}, key=key)
    out["shukr"] = {
        "tokens": len(shukr_tokens), "ayahs": len(shukr_ayahs),
        "mood_person": Counter(f'{t["mood"]} {t["person"]}'.strip() for t in shukr_tokens).most_common(),
        "imperatives": [t["ref"] for t in shukr_tokens if t["mood"] == "IMPV"],
        "first_person": [t["ref"] for t in shukr_tokens if t["person"] in ("1S", "1P")],
        "be_among_the_grateful": [r for r in shukr_ayahs if re.search(r"(كن|تكون|لنكونن|ونكونن) من الشكرين", A[r])],
        "purpose_that_you_may_thank": PURPOSE,
        "purpose_categories": dict(Counter(v[1] for v in PURPOSE.values())),
        "purpose_check": [r for r in shukr_ayahs if re.search(r"لعلكم تشكرون", A[r])],
        "few_and_most": FEW, "god_the_thanker": GOD_THANKS, "called_grateful": CALLED_GRATEFUL,
        "vows_of_thanks_in_danger": VOWS,
        "thanks_to_people": {"31:14": "be grateful to Me and to your parents",
                             "76:9": "the righteous want from those they feed no reward and no thanks"},
        "benefit_to_self": [r for r in shukr_ayahs if re.search(r"يشكر لنفسه", A[r])],
    }
    # pairings in the same ayah
    pair = {}
    for r2 in ["kfr", "Sbr", "*kr", "Ebd", "Amn", "zyd", "nEm", "gfr", "Hmd", "sbH", "Alw", "fDl"]:
        pair[r2] = sorted([r for r in shukr_ayahs if r2 in roots_in[r]], key=key)
    out["shukr_pairs_same_ayah"] = {k: {"n": len(v), "refs": v} for k, v in pair.items()}
    # praise
    hamd = sorted([r for r, t in A.items() if "الحمد لله" in t], key=key)
    out["hamd"] = {
        "al_hamdu_lillah": {"n": len(hamd), "speaker_occasion": HAMD_SPEAKERS,
                            "missing_annotation": [r for r in hamd if r not in HAMD_SPEAKERS]},
        "bi_hamd": sorted([r for r, t in A.items() if "بحمد" in t], key=key),
        "sabbih_bi_hamd_with_istighfar": sorted([r for r, t in A.items() if "بحمد" in t and "استغفر" in t
                                                 or ("بحمد" in t and "يستغفرون" in t)], key=key),
        "al_hamid_pairs": Counter(m for t in A.values() for m in re.findall(r"(\S+) (?:ال)?حميد", t)
                                  if "حميد" in t).most_common(12),
    }
    # blessing
    out["blessing"] = {
        "remember_the_blessing": sorted([r for r, t in A.items() if re.search(r"اذكروا نعمت|واذكروا نعمت|اذكروا نعمة|اذكر نعمتي|اذكروا نعمتي|اذكرا نعمتي|اذكر نعمت", t)], key=key),
        "count_the_blessing": sorted([r for r, t in A.items() if re.search(r"تعدوا نعم", t)], key=key),
        "blessing_with_kufr": sorted([r for r in {o[0] for o in by_root["nEm"]} if "kfr" in roots_in[r]], key=key),
        "proclaim_it_93_11": A.get("93:11"),
        "alaa_refrain_55": sum(1 for r, t in A.items() if r.startswith("55:") and "فباي ءالاء ربكما تكذبان" in t),
        "alaa_total_tokens": len(by_root["Alw"]),
    }
    core = sorted(set(PURPOSE) | set(FEW) | set(GOD_THANKS) | set(CALLED_GRATEFUL) | set(VOWS)
                  | {"14:7", "2:152", "27:19", "27:40", "31:12", "31:14", "34:13", "39:7", "76:3", "93:11",
                     "14:34", "16:18", "46:15", "1:2", "10:10"}, key=key)
    out["divergence_top"] = sorted([(r, div[r]["scores"]["combined"]) for r in core if r in div],
                                   key=lambda x: -x[1])[:15]
    dest = os.path.join(ROOT, "data/structural/gratitude-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print("wrote", dest)
    for r, v in out["lemma_tables"].items():
        print(f"  {r:4} tok {v['tokens']:4} ay {v['ayahs']:4} {v['lemmas'][:4]}")
    s = out["shukr"]
    print("mood/person", s["mood_person"]); print("imperatives", s["imperatives"])
    print("first person", s["first_person"]); print("be among grateful", s["be_among_the_grateful"])
    print("purpose check", s["purpose_check"], "vs annotated", sorted(PURPOSE, key=key))
    print("purpose cats", s["purpose_categories"]); print("benefit to self", s["benefit_to_self"])
    print("pairs", {k: v["n"] for k, v in out["shukr_pairs_same_ayah"].items()})
    print("kfr refs", out["shukr_pairs_same_ayah"]["kfr"]["refs"]); print("Sbr refs", out["shukr_pairs_same_ayah"]["Sbr"]["refs"])
    print("hamd missing annot", out["hamd"]["al_hamdu_lillah"]["missing_annotation"])
    print("sabbih+istighfar", out["hamd"]["sabbih_bi_hamd_with_istighfar"]); print("hamid pairs", out["hamd"]["al_hamid_pairs"])
    print("blessing", {k: v for k, v in out["blessing"].items() if k != "proclaim_it_93_11"})
    print("divergence", out["divergence_top"][:8])


if __name__ == "__main__":
    main()
