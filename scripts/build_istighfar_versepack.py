#!/usr/bin/env python3
"""Slim verse pack for the istighfar (seeking forgiveness) investigation.

Question behind it: how does the Quran teach a person to seek God's forgiveness —
in what words, when, with what, for whom, and to what effect? Emits
data/structural/istighfar-versepack.json. Agents read their groups and never open
quran.json. Groups follow the Phase-0 census (scripts/build_istighfar_census.py).
"""
import json, os

RANGES = {
    # Every quoted forgiveness petition: the 17 `ighfir` imperatives to God, the conditional
    # forms (7:23, 11:47), ghufranaka (2:285), Ibrahim's hope (26:82), Isa's (5:118).
    "petitions":          [(2, 285, 286), (3, 16, 17), (3, 146, 148), (3, 191, 194), (7, 23, 23),
                           (7, 150, 151), (7, 155, 156), (11, 45, 47), (14, 40, 41), (23, 109, 111),
                           (23, 118, 118), (26, 82, 87), (28, 15, 17), (38, 34, 35), (40, 7, 9),
                           (59, 10, 10), (60, 4, 5), (66, 8, 8), (71, 26, 28), (2, 127, 128),
                           (5, 116, 118), (21, 87, 88)],
    # istaghfiru (2MP): the eight commands to a community — five of them in prophets' sermons.
    "commands-plural":    [(2, 198, 199), (11, 1, 4), (11, 50, 52), (11, 61, 61), (11, 88, 90),
                           (41, 6, 6), (71, 5, 12), (73, 20, 20)],
    # istaghfir (2MS/2FS): commands to one person — for himself, or for others.
    "commands-singular":  [(3, 159, 159), (4, 105, 107), (9, 80, 80), (24, 62, 62), (40, 55, 55),
                           (47, 19, 19), (48, 11, 11), (60, 12, 12), (110, 1, 3), (12, 28, 29),
                           (12, 97, 98)],
    # istighfar narrated: who does it, when, after what.
    "narrated":           [(3, 133, 136), (51, 15, 19), (4, 64, 64), (4, 110, 112), (5, 73, 74),
                           (8, 33, 33), (27, 45, 46), (18, 55, 55), (38, 24, 25), (42, 5, 5)],
    # Confession of one's own wrong (zalamtu nafsi and kin).
    "confession":         [(7, 22, 23), (28, 16, 16), (21, 87, 87), (27, 44, 44), (2, 54, 54),
                           (3, 135, 135), (4, 110, 110), (12, 91, 92), (12, 97, 97), (68, 29, 32)],
    # istighfar for others — and where it is forbidden or futile.
    "for-others":         [(9, 80, 80), (9, 84, 84), (9, 113, 114), (63, 5, 6), (19, 46, 48),
                           (60, 4, 4), (26, 86, 86), (12, 97, 98), (40, 7, 9), (42, 5, 5),
                           (59, 10, 10), (71, 28, 28), (14, 41, 41), (47, 19, 19)],
    # What it is said to produce.
    "fruits":             [(11, 3, 3), (11, 52, 52), (71, 10, 12), (8, 33, 33), (27, 46, 46),
                           (4, 64, 64), (4, 110, 110), (3, 136, 136), (11, 61, 61), (11, 90, 90)],
    # When: time-anchored istighfar.
    "when":               [(3, 17, 17), (51, 17, 18), (40, 55, 55), (2, 198, 200), (73, 20, 20),
                           (110, 1, 3), (50, 39, 40), (52, 48, 49)],
    # Repentance (tawba): its commands, conditions, and the window.
    "tawba":              [(4, 17, 18), (66, 8, 8), (24, 31, 31), (2, 160, 160), (25, 68, 71),
                           (9, 104, 104), (9, 117, 118), (42, 25, 26), (39, 53, 55), (5, 39, 39),
                           (6, 54, 54), (16, 119, 119), (20, 82, 82), (3, 89, 90), (4, 146, 146)],
    # How God describes His own forgiveness — and its limits.
    "divine-forgiveness": [(4, 48, 48), (4, 116, 116), (53, 32, 32), (13, 6, 6), (41, 43, 43),
                           (85, 14, 14), (40, 3, 3), (15, 49, 50), (7, 156, 156), (11, 114, 114),
                           (4, 31, 31), (57, 21, 21), (3, 31, 31), (8, 29, 29), (33, 70, 71),
                           (61, 10, 12), (71, 4, 4), (39, 5, 5), (2, 284, 284)],
    # Forgiving others — the human side of the same root.
    "forgiving-others":   [(24, 22, 22), (42, 37, 37), (42, 40, 40), (42, 43, 43), (45, 14, 14),
                           (64, 14, 14), (2, 109, 109), (2, 237, 237), (3, 134, 134), (5, 13, 13),
                           (7, 199, 199), (15, 85, 85), (43, 89, 89), (2, 263, 263)],
}
TRANSLATIONS = ["saheeh", "khattab"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS}
    out = {"note": "Slim verse pack for the istighfar investigation. Arabic (Uthmani Hafs) + "
                   "Saheeh International + Khattab. Read only your groups.",
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
    dest = os.path.join(root, "data/structural/istighfar-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")
    for g, v in out["groups"].items():
        print(f"  {g:22} {len(v)}")


if __name__ == "__main__":
    main()
