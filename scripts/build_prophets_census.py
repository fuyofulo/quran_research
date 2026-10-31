#!/usr/bin/env python3
"""Series census for the prophets investigations.

Question behind it: which people does the Quran name who are counted as prophets, how often and
where, and which of them does the text itself call a prophet (nabī) or messenger (rasūl / mursal)?
The common count is 25; some lists say 26 or more. This tests that against the text.
Emits data/structural/prophets-census.json.

Title evidence is hand-annotated (a title is often in the next verse, so same-ayah co-occurrence
misses it) and every reference is printed with its Saheeh line for checking.
"""
import collections, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# lemma (QAC Buckwalter) -> display name. Dhul-Kifl is not a PN in QAC (kifol, root kfl).
NAMES = [
    ("A^dam", "Adam"), ("<idoriys", "Idrīs"), ("nuwH", "Nūḥ (Noah)"), ("huwd", "Hūd"), ("Sa`liH2", "Ṣāliḥ"),
    ("<iboraAhiym", "Ibrāhīm (Abraham)"), ("luwT", "Lūṭ (Lot)"), ("<isomaAEiyl", "Ismāʿīl (Ishmael)"),
    ("<isoHaAq", "Isḥāq (Isaac)"), ("yaEoquwb", "Yaʿqūb (Jacob)"), ("yuwsuf", "Yūsuf (Joseph)"),
    (">ay~uwb", "Ayyūb (Job)"), ("$uEayob", "Shuʿayb"), ("muwsaY`", "Mūsā (Moses)"), ("ha`ruwn", "Hārūn (Aaron)"),
    ("KIFL", "Dhū l-Kifl"), ("daAwud", "Dāwūd (David)"), ("sulayoma`n", "Sulaymān (Solomon)"),
    ("<iloyaAs", "Ilyās (Elijah)"), ("{loyasaEa", "al-Yasaʿ (Elisha)"), ("yuwnus", "Yūnus (Jonah)"),
    ("zakariy~aA", "Zakariyyā (Zechariah)"), ("yaHoyaY`", "Yaḥyā (John)"), ("EiysaY", "ʿĪsā (Jesus)"),
    ("muHam~ad", "Muḥammad"),
]
EXTRA_LEMMAS = {"muHam~ad": [">aHomad"]}          # Aḥmad, 61:6
CANDIDATES = [("luqoma`n", "Luqmān"), ("QARNAYN", "Dhū l-Qarnayn"), ("Euzayor", "ʿUzayr (Ezra)")]

# Where the text itself gives the title. "list" = only by membership of 6:83-89 (and 4:163), whose 6:89 says
# "those are the ones to whom We gave the Book, judgment and prophethood".
TITLES = {
    "Adam": ("none", ["3:33 chosen", "2:30 khalīfa"]),
    "Idrīs": ("nabī", ["19:56"]),
    "Nūḥ (Noah)": ("rasūl", ["7:61", "26:107", "4:163 the prophets after him"]),
    "Hūd": ("rasūl", ["7:67", "26:125"]),
    "Ṣāliḥ": ("rasūl", ["26:143"]),
    "Ibrāhīm (Abraham)": ("nabī", ["19:41"]),
    "Lūṭ (Lot)": ("rasūl", ["37:133", "26:162"]),
    "Ismāʿīl (Ishmael)": ("rasūl + nabī", ["19:54"]),
    "Isḥāq (Isaac)": ("nabī", ["19:49", "37:112"]),
    "Yaʿqūb (Jacob)": ("nabī", ["19:49"]),
    "Yūsuf (Joseph)": ("rasūl (implied)", ["40:34", "6:84 list"]),
    "Ayyūb (Job)": ("list", ["6:84", "4:163 revealed to"]),
    "Shuʿayb": ("rasūl", ["26:178"]),
    "Mūsā (Moses)": ("rasūl + nabī", ["19:51"]),
    "Hārūn (Aaron)": ("nabī", ["19:53", "20:47 two messengers"]),
    "Dhū l-Kifl": ("none", ["21:85 among the patient", "38:48 among the best"]),
    "Dāwūd (David)": ("list", ["6:84", "17:55 among the prophets, given the Zabūr", "4:163"]),
    "Sulaymān (Solomon)": ("list", ["6:84", "4:163 revealed to"]),
    "Ilyās (Elijah)": ("rasūl", ["37:123"]),
    "al-Yasaʿ (Elisha)": ("list", ["6:86", "38:48 among the best"]),
    "Yūnus (Jonah)": ("rasūl", ["37:139", "4:163 revealed to"]),
    "Zakariyyā (Zechariah)": ("list", ["6:85"]),
    "Yaḥyā (John)": ("nabī", ["3:39"]),
    "ʿĪsā (Jesus)": ("rasūl + nabī", ["19:30", "4:171"]),
    "Muḥammad": ("rasūl + nabī", ["33:40", "3:144"]),
    "Luqmān": ("none", ["31:12 given wisdom"]),
    "Dhū l-Qarnayn": ("none", ["18:83-98"]),
    "ʿUzayr (Ezra)": ("none", ["9:30 named in a claim the verse rejects"]),
}
LISTS = {"6:83-89": [(6, 83, 89)], "4:163-165": [(4, 163, 165)], "al-Anbiyāʾ 21:48-91": [(21, 48, 91)],
         "Maryam 19:2-58": [(19, 2, 58)], "Ṣād 38:17-48": [(38, 17, 48)]}


def main():
    words = [json.loads(l) for l in open(os.path.join(ROOT, "data/morphology/words.jsonl"))]
    quran = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    rev = {s["number"]: s["revelation"] for s in quran["surahs"]}
    saheeh = json.load(open(os.path.join(ROOT, "data/translations/saheeh.json")))["ayahs"]

    tok = collections.defaultdict(list)
    for w in words:
        key, loc = None, (w["surah"], w["ayah"])
        if w["pos"] == "PN":
            key = w["lemma"]
        elif w["lemma"] == "kifol" and loc in {(21, 85), (38, 48)}:
            key = "KIFL"                                  # 57:28 kiflayn = "two portions"
        elif w["lemma"] == "qaron" and "qaronayo" in w["form_buckwalter"]:
            key = "QARNAYN"
        if key:
            tok[key].append(loc)
    for main_lemma, extra in EXTRA_LEMMAS.items():
        for e in extra:
            tok[main_lemma] += tok[e]

    def profile(lemma, name):
        locs = tok[lemma]
        ayahs = sorted(set(locs))
        by_surah = collections.Counter(s for s, _ in ayahs)
        in_lists = [k for k, spans in LISTS.items() if any(s == su and a1 <= a <= a2 for s, a in ayahs for su, a1, a2 in spans)]
        title, refs = TITLES[name]
        return {"name": name, "lemma": lemma, "tokens": len(locs), "ayahs": len(ayahs), "surahs": len(by_surah),
                "meccan_ayahs": sum(1 for s, _ in ayahs if rev[s] == "Meccan"),
                "medinan_ayahs": sum(1 for s, _ in ayahs if rev[s] == "Medinan"),
                "densest_surahs": by_surah.most_common(3), "in_lists": in_lists,
                "title": title, "title_refs": refs, "refs": [f"{s}:{a}" for s, a in ayahs]}

    named = [profile(l, n) for l, n in NAMES]
    cands = [profile(l, n) for l, n in CANDIDATES]
    out = {
        "note": "Prophets named in the Quran. Title evidence hand-annotated; 'list' = prophethood only by "
                "membership of 6:83-89 (6:89 'the Book, judgment and prophethood'). Candidates are people some "
                "lists add; the text never titles them.",
        "named_count": len(named),
        "titled_explicitly": sum(1 for p in named if p["title"] not in ("none", "list")),
        "titled_by_list_only": [p["name"] for p in named if p["title"] == "list"],
        "never_titled": [p["name"] for p in named if p["title"] == "none"],
        "unnamed_messengers": ["4:164", "40:78"],
        "named": sorted(named, key=lambda p: -p["ayahs"]),
        "candidates": cands,
    }
    dest = os.path.join(ROOT, "data/structural/prophets-census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}")
    print(f"named {out['named_count']}, explicit titles {out['titled_explicitly']}, list-only {out['titled_by_list_only']}, "
          f"never titled {out['never_titled']}")
    for p in out["named"] + cands:
        print(f"  {p['name']:24} {p['tokens']:4} tok {p['ayahs']:4} ayahs {p['surahs']:3} surahs  {p['title']:16} {p['densest_surahs']}")
    print("\ntitle refs, for checking:")
    for name, (title, refs) in TITLES.items():
        for r in refs:
            k = r.split(" ")[0].split("-")[0]
            print(f"  {name:24} {r:44} | {saheeh[k][:110]}")


if __name__ == "__main__":
    main()
