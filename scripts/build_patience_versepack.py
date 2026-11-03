#!/usr/bin/env python3
"""Slim verse pack for the patience (sabr) investigation.

Agents read their groups and never open quran.json. `sbr-all` is every ayah with the root Sbr
(from data/structural/patience-census.json); the other groups add the context each agent needs.
Emits data/structural/patience-versepack.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RANGES = {
    # The vocabulary next to patience: panic, haste, weakening, swallowed grief, standing firm, despair.
    "neighbours": [(70, 19, 23), (14, 21, 21), (17, 11, 11), (21, 37, 37), (3, 134, 134), (3, 139, 139),
                   (12, 84, 87), (16, 58, 58), (68, 48, 48), (8, 45, 45), (15, 55, 56), (39, 53, 53),
                   (11, 9, 11), (41, 49, 49), (20, 114, 114), (75, 16, 16)],
    # The patient ones and their stories.
    "figures": [(12, 16, 18), (12, 83, 90), (12, 100, 100), (21, 83, 86), (38, 41, 44), (18, 60, 82),
                (37, 99, 107), (7, 120, 128), (2, 246, 251), (68, 46, 50), (14, 9, 13), (6, 33, 35),
                (46, 35, 35), (31, 12, 19), (54, 23, 31), (7, 85, 88), (11, 49, 49), (19, 64, 65)],
    # Every command to the Prophet, with the verses around it.
    "prophet-commands": [(10, 108, 109), (11, 112, 115), (16, 125, 128), (18, 27, 28), (20, 129, 132),
                         (30, 58, 60), (38, 16, 17), (40, 55, 55), (40, 77, 78), (46, 35, 35), (50, 38, 40),
                         (52, 45, 49), (68, 48, 52), (70, 4, 7), (73, 9, 11), (74, 1, 7), (76, 23, 26)],
    # Patience asked of the community.
    "community": [(2, 45, 46), (2, 153, 157), (2, 177, 177), (3, 120, 120), (3, 125, 125), (3, 139, 147),
                  (3, 186, 186), (3, 200, 200), (8, 45, 46), (8, 65, 66), (16, 126, 126), (47, 31, 31),
                  (103, 1, 3), (90, 11, 18), (29, 2, 3)],
    # What is promised to the patient.
    "rewards": [(13, 20, 24), (16, 96, 96), (23, 109, 111), (25, 63, 76), (28, 52, 54), (28, 79, 80),
                (39, 10, 10), (41, 33, 36), (76, 5, 12), (32, 24, 24), (7, 137, 137), (16, 110, 110),
                (33, 35, 35), (42, 36, 43)],
}
TRANSLATIONS = ["saheeh", "khattab"]
HOTSPOT_EXTRA = ["pickthall", "arberry"]


def main():
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    census = json.load(open(os.path.join(ROOT, "data/structural/patience-census.json")))
    trans = {t: json.load(open(os.path.join(ROOT, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS + HOTSPOT_EXTRA}
    out = {"note": "Slim verse pack for the patience investigation. Arabic (Uthmani Hafs) + Saheeh + Khattab; "
                   "the hotspots group adds Pickthall and Arberry. Read only your groups. NOTE: Arabic open-fathatan "
                   "tanwin is written with a space before its alif; rejoin before any string search.", "groups": {}}

    def verse(su, a, names):
        s = surahs[su]
        k = f"{su}:{a}"
        return {"ref": k, "surah_name": s["name_english"], "revelation": s["revelation"],
                "arabic": next(x["text"] for x in s["ayahs"] if x["ayah"] == a),
                **{t: trans[t].get(k, "") for t in names}}

    seen = set()
    refs = [tuple(map(int, r.split(":"))) for r in census["sbr"]["ayah_list"]]
    out["groups"]["sbr-all"] = [verse(su, a, TRANSLATIONS) for su, a in refs]
    seen |= {f"{su}:{a}" for su, a in refs}
    for group, spans in RANGES.items():
        out["groups"][group] = [verse(su, a, TRANSLATIONS) for su, a1, a2 in spans for a in range(a1, a2 + 1)]
        seen |= {v["ref"] for v in out["groups"][group]}
    hot = [tuple(map(int, r.split(":"))) for r, _, _ in census["divergence"]["top"]]
    out["groups"]["hotspots"] = [verse(su, a, TRANSLATIONS + HOTSPOT_EXTRA) for su, a in hot]
    out["verse_count"] = len(seen)
    dest = os.path.join(ROOT, "data/structural/patience-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses")
    for g, v in out["groups"].items():
        print(f"  {g:17} {len(v)}")


if __name__ == "__main__":
    main()
