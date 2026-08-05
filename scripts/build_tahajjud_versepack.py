#!/usr/bin/env python3
"""Slim verse pack for the tahajjud / night-worship investigation.

Emits data/structural/tahajjud-versepack.json so Phase-1 agents never open
quran.json (6,236 ayahs) or the four full translation files.
"""
import json, os

RANGES = {
    "tahajjud-verse":      [(17, 76, 82)],
    "muzzammil-founding":  [(73, 1, 11), (73, 20, 20)],
    "muddaththir-parallel":[(74, 1, 7)],
    "two-portraits":       [(51, 15, 23), (32, 15, 19)],
    "night-standing":      [(39, 9, 9), (3, 113, 117), (3, 15, 17), (25, 63, 68), (25, 73, 77)],
    "command-to-glorify":  [(50, 38, 40), (52, 48, 49), (76, 23, 26), (20, 130, 130),
                            (40, 55, 55), (30, 17, 18), (3, 41, 41), (19, 11, 11), (38, 18, 18)],
    "prayer-timing":       [(11, 114, 115), (17, 78, 79), (2, 238, 239), (4, 103, 103), (24, 58, 58)],
    "witnessed-standing":  [(26, 217, 220), (96, 19, 19), (7, 205, 206), (3, 190, 194)],
    "sleep-as-sign":       [(30, 23, 23), (25, 47, 47), (39, 42, 42), (6, 60, 60), (78, 9, 11),
                            (18, 18, 18), (8, 11, 11)],
    "night-oaths":         [(89, 1, 5), (92, 1, 4), (93, 1, 3), (91, 1, 4), (84, 16, 19), (81, 17, 18)],
    "night-as-sign":       [(10, 67, 67), (27, 86, 86), (28, 71, 73), (40, 61, 61), (36, 37, 40),
                            (17, 12, 12), (73, 7, 7)],
    "night-of-descent":    [(97, 1, 5), (44, 1, 6), (2, 185, 185)],
    "night-of-journey":    [(17, 1, 1), (20, 77, 77), (26, 52, 52), (44, 23, 23), (11, 81, 81), (15, 65, 65)],
    "dhikr-general":       [(13, 28, 28), (33, 41, 42), (2, 152, 152), (29, 45, 45), (62, 9, 10),
                            (24, 36, 37), (63, 9, 9), (87, 14, 15)],
    "dua-and-nearness":    [(2, 186, 186), (40, 60, 60), (7, 55, 56), (17, 110, 110), (50, 16, 16)],
    "istighfar-predawn":   [(51, 18, 18), (3, 17, 17), (12, 98, 98), (71, 10, 12)],
    "fasting-for-compare": [(2, 183, 187), (33, 35, 35), (19, 26, 26), (22, 37, 37), (35, 10, 10), (3, 92, 92)],
}
TRANSLATIONS = ["saheeh", "khattab", "arberry", "pickthall"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS}

    out = {"note": "Slim verse pack for the tahajjud investigation. Arabic (Uthmani Hafs) + 4 "
                   "translations. The `fasting-for-compare` group exists so the comparison agent "
                   "does not have to reopen the fasting pack.",
           "groups": {}}
    seen = set()
    for group, spans in RANGES.items():
        verses = []
        for (su, a1, a2) in spans:
            s = surahs[su]
            for a in range(a1, a2 + 1):
                key = f"{su}:{a}"
                arabic = next((x["text"] for x in s["ayahs"] if x["ayah"] == a), None)
                if arabic is None:
                    continue
                verses.append({
                    "ref": key, "surah_name": s["name_english"],
                    "revelation": s["revelation"], "arabic": arabic,
                    **{t: trans[t].get(key, "") for t in TRANSLATIONS},
                })
                seen.add(key)
        out["groups"][group] = verses

    out["verse_count"] = len(seen)
    dest = os.path.join(root, "data/structural/tahajjud-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")


if __name__ == "__main__":
    main()
