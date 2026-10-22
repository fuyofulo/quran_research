#!/usr/bin/env python3
"""Slim verse pack for the hope-and-despair investigation.

Question behind it: what does the Quran say about hope and despair — what hope is, what it is
for, what despair is and which kind is faulted, what God says to people at breaking point,
and how wishes and unanswered prayers are treated? Emits data/structural/hope-versepack.json.
Agents read their groups and never open quran.json. Groups follow the Phase-0 census
(scripts/build_hope_census.py).
"""
import json, os

RANGES = {
    # Every hope-sense occurrence of rjw (23 tokens / 22 ayahs) with minimal context.
    "hope-rjw":           [(2, 218, 218), (4, 104, 104), (10, 7, 8), (10, 11, 11), (10, 15, 15), (11, 62, 62),
                           (17, 28, 28), (17, 57, 57), (18, 110, 110), (24, 60, 60), (25, 21, 21), (25, 40, 40),
                           (28, 86, 86), (29, 5, 5), (29, 36, 36), (33, 21, 21), (35, 29, 30), (39, 9, 9),
                           (45, 14, 14), (60, 6, 6), (71, 13, 13), (78, 27, 27)],
    # `asa — "perhaps": 28 ayahs; 15 have God as the subject of the hoped-for act.
    "asa":                [(2, 216, 216), (2, 246, 246), (4, 19, 19), (4, 84, 84), (4, 99, 99), (5, 52, 52),
                           (7, 129, 129), (7, 185, 185), (9, 18, 18), (9, 102, 102), (12, 21, 21), (12, 83, 83),
                           (17, 8, 8), (17, 51, 51), (17, 79, 79), (18, 23, 24), (18, 39, 41), (19, 48, 48),
                           (27, 72, 72), (28, 9, 9), (28, 22, 22), (28, 67, 67), (47, 22, 22), (49, 11, 11),
                           (60, 7, 7), (66, 5, 5), (66, 8, 8), (68, 32, 32)],
    # Aspiration (TmE), longing (rgb), long hope (amal), and hope paired with fear.
    "aspiration-and-fear": [(2, 75, 75), (5, 83, 84), (7, 46, 46), (7, 55, 56), (13, 12, 13), (26, 50, 51),
                            (26, 78, 82), (30, 24, 24), (32, 15, 17), (33, 32, 32), (70, 38, 38), (74, 15, 15),
                            (21, 89, 90), (9, 59, 59), (68, 32, 32), (94, 7, 8), (15, 3, 3), (18, 46, 46),
                            (17, 57, 57), (39, 9, 9)],
    # Wishing (tamanni, amani) and delusion (ghurur) — hope without ground.
    "wishing":            [(2, 78, 78), (2, 94, 96), (2, 111, 112), (3, 143, 143), (4, 32, 32), (4, 119, 124),
                           (22, 52, 53), (28, 79, 82), (53, 24, 25), (57, 13, 15), (62, 6, 7), (15, 88, 88),
                           (20, 131, 131), (17, 11, 11), (10, 11, 11), (31, 33, 33), (35, 5, 5), (3, 185, 185)],
    # Despair: yAs, qnT, bls with the surrounding verses that name its cause and its exception.
    "despair":            [(5, 3, 3), (6, 44, 45), (11, 9, 11), (12, 80, 80), (12, 83, 87), (12, 110, 110),
                           (13, 31, 31), (15, 53, 56), (17, 83, 84), (23, 77, 77), (29, 23, 23), (30, 12, 12),
                           (30, 33, 36), (30, 48, 50), (39, 53, 54), (41, 49, 51), (42, 27, 28), (43, 74, 76),
                           (60, 13, 13), (65, 4, 4)],
    # Distress and rescue: karb, ghamm, dayq, wahn, kashf al-durr, the sea, the cave.
    "distress-and-rescue": [(6, 63, 64), (21, 76, 77), (37, 75, 76), (37, 114, 116), (3, 153, 154), (20, 40, 40),
                            (21, 87, 88), (9, 25, 26), (9, 40, 40), (9, 117, 118), (11, 12, 12), (15, 97, 99),
                            (16, 127, 128), (26, 13, 13), (27, 70, 70), (3, 139, 146), (4, 104, 104), (47, 35, 35),
                            (27, 62, 62), (10, 12, 12), (10, 107, 107), (6, 17, 17), (16, 53, 54), (39, 38, 38),
                            (10, 103, 103), (26, 61, 62), (3, 173, 175), (33, 9, 12), (33, 22, 22)],
    # Ease with hardship, and the consolation surahs.
    "ease":               [(93, 1, 11), (94, 1, 8), (65, 2, 7), (2, 185, 185), (2, 286, 286), (92, 5, 10),
                           (87, 8, 8), (2, 280, 280), (7, 95, 95), (24, 55, 55), (25, 70, 70)],
    # Those who waited: individual long waits and their endings.
    "those-who-waited":   [(12, 16, 18), (12, 83, 87), (12, 93, 100), (3, 38, 41), (19, 2, 11), (11, 69, 73),
                           (15, 51, 56), (51, 24, 30), (14, 39, 39), (21, 83, 84), (38, 41, 44), (37, 139, 148),
                           (68, 48, 50), (28, 7, 13), (20, 37, 40), (19, 16, 26), (28, 21, 28), (12, 33, 34),
                           (54, 9, 15), (11, 36, 37), (10, 88, 89), (26, 61, 67), (12, 101, 101)],
    # The Prophet at breaking point, and how he is consoled.
    "the-prophet-consoled": [(6, 33, 35), (18, 6, 6), (26, 3, 4), (35, 8, 8), (20, 1, 3), (10, 65, 65), (36, 76, 76),
                             (52, 48, 49), (15, 94, 99), (16, 127, 128), (11, 12, 12), (17, 73, 75), (28, 86, 86),
                             (31, 23, 23), (3, 176, 176), (5, 41, 41), (6, 10, 10), (13, 32, 32)],
    # Communities at breaking point, the "do you think" questions, and what they thought of God.
    "shaken-communities": [(2, 155, 157), (2, 214, 214), (2, 249, 251), (3, 139, 148), (3, 152, 154), (3, 172, 175),
                           (3, 186, 186), (8, 9, 10), (9, 16, 16), (29, 1, 11), (47, 31, 31), (67, 2, 2),
                           (21, 35, 35), (89, 15, 20), (48, 4, 6), (48, 12, 12), (41, 22, 23), (33, 9, 25),
                           (12, 110, 110), (6, 42, 45), (7, 94, 95), (7, 168, 168)],
    # Prayers answered, prayers not granted as asked, and the wish that would have harmed.
    "answers-and-wishes": [(2, 186, 186), (40, 60, 60), (27, 62, 62), (42, 26, 27), (10, 88, 89), (11, 61, 61),
                           (12, 34, 34), (3, 195, 195), (11, 45, 47), (9, 113, 114), (2, 216, 216), (4, 19, 19),
                           (60, 7, 7), (66, 5, 5), (68, 17, 33), (18, 32, 44), (18, 79, 82), (8, 70, 70),
                           (57, 22, 23), (64, 11, 11), (3, 26, 27), (42, 49, 50), (13, 26, 26), (17, 18, 21),
                           (28, 79, 82), (19, 4, 6), (21, 89, 90), (17, 11, 11)],
    # Grief (Hzn): every ayah — commands not to grieve, and who grieves.
    # Grief (Hzn): every one of its 42 ayahs — commands not to grieve, and who grieves.
    "grief":              [(2, 38, 38), (2, 62, 62), (2, 112, 112), (2, 262, 262), (2, 274, 274), (2, 277, 277),
                           (3, 139, 139), (3, 153, 153), (3, 170, 170), (3, 176, 176), (5, 41, 41), (5, 69, 69),
                           (6, 33, 33), (6, 48, 48), (7, 35, 35), (7, 49, 49), (9, 40, 40), (9, 92, 92),
                           (10, 62, 62), (10, 65, 65), (12, 13, 13), (12, 84, 84), (12, 86, 86), (15, 88, 88),
                           (16, 127, 127), (19, 24, 24), (20, 40, 40), (21, 103, 103), (27, 70, 70), (28, 7, 8),
                           (28, 13, 13), (29, 33, 33), (31, 23, 23), (33, 51, 51), (35, 34, 34), (36, 76, 76),
                           (39, 61, 61), (41, 30, 30), (43, 68, 68), (46, 13, 13), (58, 10, 10)],
    # Near-synonyms of grief: ta'sa (Asw, "sorrow", 4x) and ibta'asa (bAs, "be distressed", 2x).
    "grief-synonyms":     [(5, 26, 26), (5, 68, 68), (7, 93, 93), (57, 22, 23), (11, 36, 36), (12, 69, 69)],
    # Trust and "God is enough": tawakkul, hasbuna, God's nearness.
    "trust-and-nearness": [(3, 173, 174), (9, 51, 51), (9, 59, 59), (9, 129, 129), (39, 36, 38), (65, 3, 3),
                           (8, 62, 64), (14, 11, 12), (11, 88, 88), (2, 186, 186), (50, 16, 16), (56, 85, 85),
                           (20, 46, 46), (2, 153, 153), (8, 46, 46), (13, 28, 28), (11, 61, 61), (34, 50, 50)],
}
TRANSLATIONS = ["saheeh", "khattab"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS}
    out = {"note": "Slim verse pack for the hope-and-despair investigation. Arabic (Uthmani Hafs) + "
                   "Saheeh International + Khattab. Read only your groups. NOTE: Arabic open-fathatan "
                   "tanwin is written with a space before its alif; rejoin before any string search.",
           "groups": {}}
    seen = set()
    for group, spans in RANGES.items():
        verses, gseen = [], set()
        for (su, a1, a2) in spans:
            s = surahs[su]
            for a in range(a1, a2 + 1):
                key = f"{su}:{a}"
                arabic = next((x["text"] for x in s["ayahs"] if x["ayah"] == a), None)
                if arabic is None or key in gseen:
                    continue
                gseen.add(key)
                verses.append({"ref": key, "surah_name": s["name_english"],
                               "revelation": s["revelation"], "arabic": arabic,
                               **{t: trans[t].get(key, "") for t in TRANSLATIONS}})
                seen.add(key)
        out["groups"][group] = verses
    out["verse_count"] = len(seen)
    dest = os.path.join(root, "data/structural/hope-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")
    for g, v in out["groups"].items():
        print(f"  {g:22} {len(v)}")


if __name__ == "__main__":
    main()
