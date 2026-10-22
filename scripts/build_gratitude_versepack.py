#!/usr/bin/env python3
"""Slim verse pack for the gratitude (shukr) investigation.

Question behind it: how does the Quran teach a person to thank God — what thanks is, what it is
for, who is called grateful, what ingratitude looks like, and how thanks travels with praise,
glorification, remembrance and seeking forgiveness? Emits data/structural/gratitude-versepack.json.
Agents read their groups and never open quran.json. Groups follow the Phase-0 census
(scripts/build_gratitude_census.py).
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RANGES = {
    # Every ayah of the root $kr (69), filled in automatically below.
    "shukr-all": [],
    # The verses leading up to each "that you may be grateful" (14).
    "purpose-contexts":   [(2, 51, 52), (2, 55, 56), (2, 183, 185), (3, 123, 123), (5, 6, 6), (5, 89, 89),
                           (8, 26, 26), (16, 14, 14), (16, 78, 78), (22, 36, 37), (28, 71, 73), (30, 46, 46),
                           (35, 12, 12), (45, 12, 13)],
    # Those the Quran calls grateful or shows thanking — with and without the word.
    "the-grateful":       [(17, 1, 3), (16, 120, 123), (27, 15, 19), (27, 38, 40), (34, 10, 13), (21, 78, 80),
                           (31, 12, 19), (46, 15, 16), (7, 143, 145), (39, 64, 66), (93, 6, 11), (76, 5, 12),
                           (54, 33, 35), (12, 38, 38), (12, 100, 101), (14, 35, 41), (23, 28, 29), (3, 144, 145),
                           (2, 151, 152), (2, 172, 172), (16, 114, 114), (29, 16, 17)],
    # Ingratitude: blessing denied, self-attributed, forgotten after rescue.
    "the-ungrateful":     [(34, 15, 19), (16, 112, 113), (14, 28, 34), (16, 53, 55), (16, 71, 72), (16, 83, 83),
                           (18, 32, 44), (28, 76, 82), (39, 49, 50), (41, 50, 51), (17, 66, 69), (10, 21, 23),
                           (29, 65, 67), (31, 32, 32), (30, 33, 34), (7, 189, 190), (6, 63, 64), (2, 211, 211),
                           (14, 6, 8), (39, 7, 8), (89, 15, 17), (100, 6, 8), (80, 17, 23), (22, 66, 66),
                           (42, 48, 48), (43, 15, 15), (17, 83, 83), (17, 89, 89), (25, 50, 50), (11, 9, 10),
                           (7, 10, 10), (23, 78, 78), (32, 9, 9), (67, 23, 23), (56, 63, 74), (36, 33, 35),
                           (36, 71, 73), (7, 16, 17), (2, 243, 243), (10, 60, 60), (27, 73, 73), (40, 61, 61)],
    # Praise: every "al-hamdu lillah", every "bi-hamdi", and the name al-Hamid.
    "praise":             [(1, 1, 7), (6, 1, 1), (6, 45, 45), (7, 43, 43), (10, 9, 10), (14, 39, 39), (16, 75, 75),
                           (17, 111, 111), (18, 1, 1), (23, 28, 28), (27, 15, 15), (27, 59, 59), (27, 93, 93),
                           (29, 63, 63), (31, 25, 25), (34, 1, 1), (35, 1, 1), (35, 34, 34), (37, 180, 182),
                           (39, 29, 29), (39, 73, 75), (40, 65, 65), (2, 30, 30), (13, 13, 13), (15, 98, 99),
                           (17, 44, 44), (17, 52, 52), (20, 130, 130), (25, 58, 58), (32, 15, 15), (40, 7, 7),
                           (40, 55, 55), (42, 5, 5), (50, 39, 40), (52, 48, 49), (110, 1, 3), (30, 17, 18),
                           (64, 1, 1), (28, 70, 70), (45, 36, 36), (2, 267, 267), (4, 131, 131), (11, 73, 73),
                           (14, 1, 1), (14, 8, 8), (22, 24, 24), (22, 64, 64), (31, 26, 26), (34, 6, 6),
                           (35, 15, 15), (41, 42, 42), (42, 28, 28), (57, 24, 24), (60, 6, 6), (64, 6, 6),
                           (85, 8, 8), (9, 112, 112), (61, 6, 6), (3, 188, 188), (17, 79, 79)],
    # Blessing: "remember God's blessing", the uncountable blessing, al-Nahl's catalogue, al-Rahman.
    "blessing":           [(2, 40, 40), (2, 47, 47), (2, 122, 122), (2, 231, 231), (3, 103, 103), (5, 3, 3),
                           (5, 7, 7), (5, 11, 11), (5, 20, 20), (5, 110, 110), (14, 6, 6), (33, 9, 9), (35, 3, 3),
                           (16, 3, 18), (16, 80, 81), (31, 20, 20), (93, 11, 11), (12, 6, 6), (48, 2, 2),
                           (102, 8, 8), (2, 150, 150), (8, 53, 53), (14, 32, 34), (16, 53, 53), (37, 57, 57),
                           (68, 2, 2), (68, 49, 49), (52, 29, 29), (4, 69, 69), (1, 7, 7), (19, 58, 58),
                           (17, 70, 70), (45, 13, 13)],
    "al-rahman":          [(55, 1, 78)],
    # God who thanks: shakur, shakir, an effort "thanked".
    "god-thanks":         [(2, 158, 158), (4, 147, 147), (35, 29, 34), (42, 23, 23), (64, 17, 17), (17, 18, 19),
                           (76, 22, 22), (14, 7, 7), (39, 7, 7), (31, 12, 12), (27, 40, 40), (3, 144, 145)],
    # Thanks to people — parents, and the righteous who want none.
    "thanks-and-people":  [(31, 14, 15), (46, 15, 17), (76, 8, 10), (2, 237, 237), (17, 23, 24), (27, 19, 19)],
    # Thanks with praise, glorification, remembrance, worship and seeking forgiveness.
    "hand-in-hand":       [(2, 152, 152), (40, 7, 9), (40, 55, 55), (42, 5, 5), (110, 1, 3), (50, 39, 40),
                           (52, 48, 49), (15, 98, 99), (20, 130, 130), (3, 190, 194), (3, 17, 17), (51, 17, 18),
                           (33, 41, 43), (2, 185, 185), (22, 36, 37), (39, 66, 66), (2, 172, 172), (16, 114, 114),
                           (29, 17, 17), (10, 10, 10), (7, 43, 43), (35, 34, 35), (39, 74, 75), (27, 19, 19),
                           (46, 15, 15), (11, 3, 3), (71, 10, 12), (14, 7, 7), (4, 147, 147), (8, 33, 33)],
}
TRANSLATIONS = ["saheeh", "khattab"]


def main():
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(ROOT, f"data/translations/{t}.json")))["ayahs"] for t in TRANSLATIONS}
    shukr = sorted({(w["surah"], w["ayah"]) for w in map(json.loads, open(os.path.join(ROOT, "data/morphology/words.jsonl")))
                    if w.get("root") == "$kr"})
    RANGES["shukr-all"] = [(s, a, a) for s, a in shukr]
    out = {"note": "Slim verse pack for the gratitude investigation. Arabic (Uthmani Hafs) + Saheeh + Khattab. "
                   "Read only your groups. NOTE: Arabic open-fathatan tanwin is written with a space before its "
                   "alif; rejoin before any string search.", "groups": {}}
    seen = set()
    for group, spans in RANGES.items():
        verses, gseen = [], set()
        for (su, a1, a2) in spans:
            s = surahs[su]
            for a in range(a1, a2 + 1):
                k = f"{su}:{a}"
                arabic = next((x["text"] for x in s["ayahs"] if x["ayah"] == a), None)
                if arabic is None or k in gseen:
                    continue
                gseen.add(k)
                verses.append({"ref": k, "surah_name": s["name_english"], "revelation": s["revelation"],
                               "arabic": arabic, **{t: trans[t].get(k, "") for t in TRANSLATIONS}})
                seen.add(k)
        out["groups"][group] = verses
    out["verse_count"] = len(seen)
    dest = os.path.join(ROOT, "data/structural/gratitude-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")
    for g, v in out["groups"].items():
        print(f"  {g:20} {len(v)}")


if __name__ == "__main__":
    main()
