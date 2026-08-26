#!/usr/bin/env python3
"""Slim verse pack for the extraterrestrial-life / cosmology investigation.

Question behind it: does the Quran say there is life — specifically human life —
anywhere other than the earth? Emits data/structural/cosmos-versepack.json.
"""
import json, os

RANGES = {
    # The three parallel "scattered creatures" verses. The pronoun differs.
    "dabba-dispersal":   [(42, 29, 29), (31, 10, 10), (2, 164, 164), (45, 3, 5)],
    "dabba-all":         [(6, 38, 38), (11, 6, 6), (24, 45, 45), (16, 49, 49), (22, 18, 18),
                          (27, 82, 82), (35, 45, 45), (16, 61, 61), (29, 60, 60), (11, 56, 56)],
    # The verse the "seven earths" claim comes from, plus every seven-heavens verse.
    "seven-heavens":     [(65, 12, 12), (2, 29, 29), (67, 3, 5), (71, 15, 16), (78, 12, 13),
                          (17, 44, 44), (23, 17, 17), (23, 86, 86), (41, 9, 12)],
    # Who else is intelligent, according to the Quran?
    "jinn-and-mankind":  [(55, 14, 15), (55, 31, 33), (6, 128, 130), (51, 56, 56), (15, 26, 33),
                          (7, 11, 12), (18, 50, 50), (72, 1, 15), (46, 29, 32), (34, 12, 14)],
    "angels":            [(35, 1, 1), (66, 6, 6), (21, 19, 20), (42, 5, 5), (37, 164, 166)],
    # Universal prostration / glorification — who is included?
    "universal-worship": [(13, 15, 15), (55, 5, 7), (17, 44, 44), (24, 41, 41), (59, 24, 24),
                          (19, 93, 95), (30, 26, 26), (21, 19, 20)],
    # Cosmology proper
    "cosmogony":         [(21, 30, 33), (51, 47, 48), (41, 11, 12), (79, 27, 33), (7, 54, 54),
                          (32, 4, 5), (50, 6, 6), (2, 22, 22)],
    # Reaching beyond, and its limits
    "passing-beyond":    [(55, 33, 35), (15, 14, 18), (37, 6, 10), (67, 5, 5), (72, 8, 10),
                          (17, 93, 95), (6, 35, 35)],
    # "Worlds" — the plural that carries a lot of weight
    "the-worlds":        [(1, 1, 2), (26, 23, 24), (2, 47, 47), (45, 36, 37), (6, 45, 45), (7, 54, 54)],
    # Other-than-human communities and their accountability
    "communities":       [(6, 38, 38), (16, 68, 69), (27, 16, 19), (34, 10, 10), (38, 18, 19),
                          (24, 41, 41), (17, 44, 44)],
    # Life itself
    "life-and-water":    [(21, 30, 30), (24, 45, 45), (25, 54, 54), (86, 5, 8), (56, 57, 62)],
    # The gathering — does it include non-earthly creatures?
    "gathering":         [(42, 29, 29), (6, 38, 38), (81, 5, 5), (27, 87, 87), (18, 47, 47)],
}
TRANSLATIONS = ["saheeh", "khattab", "arberry", "pickthall"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS}
    out = {"note": "Slim verse pack for the cosmos / extraterrestrial-life investigation. "
                   "Arabic (Uthmani Hafs) + 4 translations.",
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
                verses.append({"ref": key, "surah_name": s["name_english"],
                               "revelation": s["revelation"], "arabic": arabic,
                               **{t: trans[t].get(key, "") for t in TRANSLATIONS}})
                seen.add(key)
        out["groups"][group] = verses
    out["verse_count"] = len(seen)
    dest = os.path.join(root, "data/structural/cosmos-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")


if __name__ == "__main__":
    main()
