#!/usr/bin/env python3
"""Phase-0 census for the hope-and-despair investigation. Deterministic.

  1. Lemma tables for the hope, despair, wishing, distress and relief roots.
  2. rjw split by sense (hope vs postpone vs edges), then each hope-occurrence by
     object and polarity — what the Quran says people hope FOR, and who does not hope.
  3. `asa (perhaps): who is the subject of the hoped-for act.
  4. TmE (aspiration) and yAs/qnT/bls (despair) by valence — praised, neutral, faulted.
  5. Pairings of hope with fear in one ayah.
  6. God answering (istajaba / ajaba with God as subject).
  7. The replacement pattern: God gives "better than" what was lost (bdl, khayran min).
  8. Hardship/ease (Esr + ysr) co-occurrence; "faraj" (relief) absent.
  9. Translator divergence over the core set.
Emits data/structural/hope-census.json.
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


ROOTS = {
    "hope": ["rjw", "TmE", "Aml", "Esy", "rgb"],
    "despair": ["yAs", "qnT", "bls"],
    "wishing": ["mny", "grr"],
    "distress": ["krb", "gmm", "Dyq", "whn", "Hzn", "hmm"],
    "relief": ["Esr", "ysr", "k$f", "njw", "rwH", "frj", "bdl"],
    "trust": ["wkl", "Sbr", "Znn"],
}

# --- rjw: sense, object, polarity (hand-annotated against Saheeh + Khattab) -------------
RJW_OTHER = {"7:111": "postpone (arjih)", "26:36": "postpone (arjih)", "33:51": "put aside (turji)",
             "9:106": "deferred (murjawn)", "69:17": "edges (arja')"}
RJW_HOPE = {  # ref: (object, polarity, who)
    "2:218": ("God's mercy", "+", "believers who emigrated and strove"),
    "4:104#1": ("from God what they do not hope", "+", "believers, wounded"),
    "4:104#2": ("from God", "-", "the enemy"),
    "10:7": ("the meeting with Us", "-", "the content with this world"),
    "10:11": ("the meeting with Us", "-", "deniers"),
    "10:15": ("the meeting with Us", "-", "deniers"),
    "11:62": ("a person (Salih)", "+", "Thamud, of Salih before his call"),
    "17:28": ("mercy from your Lord", "+", "the Prophet, empty-handed"),
    "17:57": ("His mercy", "+", "those invoked (angels/righteous) seeking nearness"),
    "18:110": ("the meeting with his Lord", "+", "anyone — conditional"),
    "24:60": ("marriage", "-", "older women"),
    "25:21": ("the meeting with Us", "-", "deniers"),
    "25:40": ("resurrection", "-", "deniers"),
    "28:86": ("that the Book be cast to you", "-", "the Prophet — given anyway, as mercy"),
    "29:5": ("the meeting with God", "+", "anyone — conditional"),
    "29:36": ("the Last Day", "+", "commanded by Shu'ayb"),
    "33:21": ("God and the Last Day", "+", "whoever takes the Prophet as model"),
    "35:29": ("a trade that will not perish", "+", "reciters, prayer, spenders"),
    "39:9": ("his Lord's mercy", "+", "the one devout in the night"),
    "45:14": ("the days of God", "-", "those believers must forgive"),
    "60:6": ("God and the Last Day", "+", "whoever takes Abraham's company as model"),
    "71:13": ("dignity/grandeur for God", "-", "Noah's people"),
    "78:27": ("a reckoning", "-", "the transgressors"),
}

# --- `asa: who is the subject of the hoped-for act ---------------------------------------
ESY = {
    "2:216": "general — perhaps you hate/love a thing (x2)",
    "2:246": "rebuke — would you perhaps not fight",
    "4:19": "general — perhaps you dislike [a wife] and God puts much good in it",
    "4:84": "GOD — perhaps God will restrain the disbelievers",
    "4:99": "GOD — perhaps God will pardon them",
    "5:52": "GOD — perhaps God will bring the opening",
    "7:129": "GOD — Moses: perhaps your Lord will destroy your enemy",
    "7:185": "general — perhaps their term has come near",
    "9:18": "human — perhaps they will be of the guided",
    "9:102": "GOD — perhaps God will turn to them",
    "12:21": "human — perhaps he will benefit us (Joseph's buyer)",
    "12:83": "GOD — Jacob: perhaps God will bring them all to me",
    "17:8": "GOD — perhaps your Lord will have mercy on you",
    "17:51": "general — perhaps it is near",
    "17:79": "GOD — perhaps your Lord will raise you to a praised station",
    "18:24": "GOD — perhaps my Lord will guide me nearer than this",
    "18:40": "GOD — perhaps my Lord will give me better than your garden",
    "19:48": "self-before-GOD — Abraham: perhaps I will not be unhappy in calling my Lord",
    "27:72": "general — perhaps it is close behind you",
    "28:9": "human — Pharaoh's wife: perhaps he will benefit us",
    "28:22": "GOD — Moses: perhaps my Lord will guide me to the right way",
    "28:67": "self — perhaps the one who repents will be among the successful",
    "47:22": "rebuke — would you perhaps sever kinship",
    "49:11": "general — perhaps they are better than them (x2)",
    "60:7": "GOD — perhaps God will put affection between you and your enemies",
    "66:5": "GOD — perhaps his Lord will give him wives better than you",
    "66:8": "GOD — perhaps your Lord will remove your misdeeds",
    "68:32": "GOD — perhaps our Lord will give us better than it",
}

# --- TmE valence --------------------------------------------------------------------------
TME = {"2:75": ("people's belief", "dashed — do you hope they will believe?"),
       "5:84": ("God admitting us with the righteous", "praised"),
       "7:46": ("entry to the Garden", "neutral — the people of the heights"),
       "7:56": ("— call on Him in fear and aspiration", "commanded"),
       "13:12": ("— lightning: fear and aspiration", "sign"),
       "26:51": ("God forgiving our sins", "praised — the magicians"),
       "26:82": ("God forgiving my sin", "praised — Abraham"),
       "30:24": ("— lightning: fear and aspiration", "sign"),
       "32:16": ("— call on their Lord in fear and aspiration", "praised"),
       "33:32": ("the diseased heart's desire", "faulted"),
       "70:38": ("entry to the Garden without deeds", "faulted"),
       "74:15": ("more", "faulted — greed")}

# --- despair valence ---------------------------------------------------------------------
DESPAIR = {
    "5:3": ("yAs", "disbelievers, of your religion", "neutral"),
    "11:9": ("yAs", "man, when mercy is withdrawn", "faulted — despairing, ungrateful"),
    "12:80": ("yAs", "Joseph's brothers, of the ruler", "neutral"),
    "12:87": ("yAs", "of God's rawh (relief)", "faulted — only the disbelievers"),
    "12:110": ("yAs", "the messengers, of their people", "unblamed — then Our help came"),
    "13:31": ("yAs", "the believers (= have they not known)", "neutral"),
    "17:83": ("yAs", "man, when evil touches him", "faulted"),
    "29:23": ("yAs", "deniers, of My mercy", "faulted"),
    "41:49": ("yAs+qnT", "man, when evil touches him", "faulted"),
    "60:13": ("yAs", "the angered-upon, of the hereafter", "faulted"),
    "65:4": ("yAs", "women, of menstruation", "neutral (legal)"),
    "15:55": ("qnT", "Abraham — do not be of the despairing", "forbidden"),
    "15:56": ("qnT", "of his Lord's mercy", "faulted — only the astray"),
    "30:36": ("qnT", "people, when evil afflicts them for their deeds", "faulted"),
    "39:53": ("qnT", "the self-wronging servants, of God's mercy", "forbidden"),
    "42:28": ("qnT", "people before rain", "unblamed — then He sends rain"),
    "6:44": ("bls", "the forgetful, seized suddenly", "punishment"),
    "23:77": ("bls", "under a door of severe punishment", "punishment"),
    "30:12": ("bls", "the criminals, when the Hour comes", "punishment"),
    "30:49": ("bls", "people before rain", "unblamed — then the rain"),
    "43:75": ("bls", "in the punishment", "punishment"),
}

# ayahs where God is the one who answers (istajaba / ajaba / mujib)
ANSWER_LEMMAS = {"{sotajaAba", ">ujiybat", "m~ujiyb"}
GOD_ANSWERS = ["2:186", "3:195", "8:9", "10:89", "11:61", "12:34", "21:76", "21:84", "21:88",
               "21:90", "27:62", "37:75", "40:60", "42:26"]

FEAR = {"xwf", "x$y", "H*r", "rhb", "wjl", "$fq"}
HOPE_SENSE_ROOTS = {"rjw", "TmE", "rgb"}


def main():
    W = [json.loads(l) for l in open(os.path.join(ROOT, "data/morphology/words.jsonl"))]
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    A = {f'{s["number"]}:{a["ayah"]}': norm(a["text"]) for s in q["surahs"] for a in s["ayahs"]}
    div = json.load(open(os.path.join(ROOT, "data/structural/translation-divergence.json")))
    by_root = defaultdict(list)
    roots_in = defaultdict(set)
    for w in W:
        r = w.get("root")
        if not r:
            continue
        ref = f'{w["surah"]}:{w["ayah"]}'
        by_root[r].append((ref, w["lemma"]))
        roots_in[ref].add(r)
    out = {"note": "Phase-0 census, hope & despair. See scripts/build_hope_census.py."}

    # 1. lemma tables
    lt = {}
    for fam, rs in ROOTS.items():
        for r in rs:
            occ = by_root[r]
            lt[r] = {"family": fam, "tokens": len(occ), "ayahs": len({o[0] for o in occ}),
                     "lemmas": Counter(o[1] for o in occ).most_common()}
    out["lemma_tables"] = lt

    # 2. rjw
    hope_refs = [o[0] for o in by_root["rjw"] if o[0] not in RJW_OTHER]
    pol = Counter(v[1] for v in RJW_HOPE.values())
    obj = Counter()
    for v in RJW_HOPE.values():
        o = v[0]
        cat = ("the meeting / Last Day / reckoning" if re.search("meeting|Last Day|resurrection|reckoning|days of God", o)
               else "God's mercy / from God" if re.search("mercy|from God|dignity", o)
               else "a trade that will not perish" if "trade" in o else "worldly: " + o)
        obj[(cat, v[1])] += 1
    out["rjw"] = {"non_hope_senses": RJW_OTHER, "hope_tokens": len(hope_refs),
                  "hope_annotation": RJW_HOPE, "polarity": dict(pol),
                  "object_x_polarity": {f"{k[0]} [{k[1]}]": n for k, n in obj.most_common()}}

    # 3. `asa
    esy_count = Counter(v.split(" — ")[0] for v in ESY.values())
    out["asa"] = {"tokens": len(by_root["Esy"]), "ayahs": len(ESY), "subject_counts": dict(esy_count),
                  "annotation": ESY}

    # 4. TmE + despair
    out["tama"] = TME
    out["despair"] = {"annotation": DESPAIR,
                      "valence": dict(Counter(v[2].split(" — ")[0].split(" (")[0] for v in DESPAIR.values()))}

    # 5. hope+fear pairing
    pair = []
    for ref, rs in roots_in.items():
        if rs & HOPE_SENSE_ROOTS and rs & FEAR and ref not in RJW_OTHER:
            pair.append((ref, sorted(rs & HOPE_SENSE_ROOTS), sorted(rs & FEAR)))
    out["hope_with_fear"] = sorted(pair, key=lambda x: key(x[0]))

    # 6. God answers
    out["god_answers"] = {"refs": GOD_ANSWERS,
                          "fa-stajabna_lahu_in_surah_21": [r for r in GOD_ANSWERS if r.startswith("21:")]}

    # 7. replacement pattern: "better than" given by God
    khayr_min = [r for r, t in A.items() if re.search(r"(خيرا|خير) (منه|منها|منكن|مما|من)", t)
                 and re.search(r"(يبدل|يوتي|يوتكم|بدلنا|نبدل)", t)]
    bdl_god = ["7:95", "18:81", "24:55", "25:70", "27:11", "66:5", "68:32", "70:41"]
    out["replacement"] = {"khayr_min_with_giving_verb": khayr_min, "bdl_god_gives_better": bdl_god,
                          "note": "27:36 is Solomon comparing gifts, not a replacement; 18:81 is al-Khidr's account"}

    # 8. hardship/ease
    esr = {o[0] for o in by_root["Esr"]}
    ysr = {o[0] for o in by_root["ysr"]}
    out["hardship_ease"] = {"Esr_ayahs": sorted(esr, key=key), "ysr_ayahs": len(ysr),
                            "both": sorted(esr & ysr, key=key),
                            "frj_lemmas": Counter(o[1] for o in by_root["frj"]).most_common(),
                            "frj_relief_sense": 0,
                            "rawh_refs": sorted({o[0] for o in by_root["rwH"] if o[1] == "r~awoH"}, key=key)}

    # 9. divergence
    core = sorted(set(RJW_HOPE_KEYS := [k.split("#")[0] for k in RJW_HOPE]) | set(ESY) | set(TME) | set(DESPAIR)
                  | set(GOD_ANSWERS) | {"94:5", "94:6", "65:7", "12:86", "26:62", "2:155", "2:156", "2:214", "9:40",
                                        "53:24", "4:32", "94:8", "9:59", "3:139", "57:23"}, key=key)
    sc = [(r, div[r]["scores"]["combined"]) for r in core if r in div]
    out["divergence_top"] = sorted(sc, key=lambda x: -x[1])[:15]

    dest = os.path.join(ROOT, "data/structural/hope-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print("wrote", dest)
    for r, v in lt.items():
        print(f"  {r:4} {v['family']:9} tok {v['tokens']:4} ay {v['ayahs']:4} {v['lemmas'][:4]}")
    print("rjw polarity", dict(pol)); print("rjw object", out["rjw"]["object_x_polarity"])
    print("asa", dict(esy_count)); print("despair", out["despair"]["valence"])
    print("hope+fear", out["hope_with_fear"])
    print("khayr_min", khayr_min); print("Esr&ysr", out["hardship_ease"]["both"])
    print("divergence", out["divergence_top"][:10])


if __name__ == "__main__":
    main()
