#!/usr/bin/env python3
"""Slim verse pack for the regret investigation.

Question behind it: what does the Quran say humans will regret — in this life and in
the hereafter — and what actions and inner states lead there? Emits
data/structural/regret-versepack.json. Agents read their groups from this file and
never open quran.json.

Groups are built from the Phase-0 census (scripts/build_regret_census.py): every
occurrence of the regret nouns (ndm, Hsr), the wish particle (layta), the woe-cry
(yā waylatā / yā waylanā), the return-requests, the counterfactual wadda-law, the
hand-gestures, plus the narrative passages they sit in. Context verses included.
"""
import json, os

RANGES = {
    # The two regret nouns. nadam (7) and hasra (9 + the contested mahsur).
    "lexical-ndm":        [(5, 27, 31), (5, 51, 53), (23, 37, 41), (26, 155, 158), (49, 6, 6),
                           (10, 53, 54), (34, 31, 33)],
    "lexical-hasra":      [(2, 165, 167), (3, 154, 156), (3, 168, 168), (6, 31, 31), (8, 36, 36),
                           (17, 29, 29), (19, 39, 39), (35, 8, 8), (36, 30, 30), (39, 53, 59),
                           (69, 48, 50)],
    # The wish particle layta: all 14 occurrences, with context.
    "layta":              [(4, 72, 73), (6, 27, 28), (18, 42, 43), (19, 23, 23), (25, 27, 29),
                           (28, 79, 82), (33, 64, 68), (36, 26, 27), (43, 36, 39), (69, 25, 29),
                           (78, 40, 40), (89, 21, 26)],
    # The woe-cry. 11:72 (Sarah) is a control: surprise, not regret.
    "woe-cry":            [(18, 49, 49), (21, 11, 15), (21, 46, 46), (21, 96, 97), (36, 51, 53),
                           (37, 19, 21), (11, 72, 72)],
    # Requests to be sent back / given more time — and God's replies.
    "return-requests":    [(26, 96, 102), (23, 99, 100), (23, 105, 108), (32, 12, 14), (35, 36, 37),
                           (7, 53, 53), (14, 44, 45), (40, 10, 12), (42, 44, 47), (63, 9, 11)],
    # wadda + law: counterfactual wishing. 2:96 is a control (wish for long life).
    "wish-wadda":         [(3, 30, 30), (4, 42, 42), (15, 2, 3), (70, 8, 14), (2, 96, 96)],
    # The bodily gestures of regret. 3:119 is a control (biting fingertips in rage).
    "hand-gestures":      [(25, 27, 27), (18, 42, 42), (7, 148, 149), (3, 119, 119)],
    # farrata — "what I neglected". 6:38 and 6:61 are controls (God / angels do not neglect).
    "neglect-farrata":    [(6, 31, 31), (39, 56, 56), (12, 80, 80), (6, 61, 61), (6, 38, 38)],
    # Confession formulas: innā kunnā zālimīn / khāti'īn, zalamtu nafsī.
    "confession":         [(7, 4, 5), (68, 29, 32), (12, 91, 92), (12, 97, 98), (67, 6, 11),
                           (9, 102, 102), (7, 22, 23), (28, 15, 16), (21, 87, 88), (38, 24, 25),
                           (3, 135, 136), (11, 45, 47)],
    # When regret stops working: the window, late belief, "before it comes".
    "the-window":         [(4, 17, 18), (10, 90, 92), (10, 98, 98), (40, 84, 85), (6, 158, 158),
                           (44, 10, 16), (34, 51, 54), (30, 57, 57), (40, 52, 52), (32, 29, 29),
                           (2, 254, 254), (14, 31, 31), (30, 43, 43), (59, 18, 19), (50, 19, 22),
                           (79, 34, 36)],
    # This-life regret narratives (full passages).
    "this-life-narratives": [(18, 32, 44), (68, 17, 33), (7, 148, 153), (9, 117, 118),
                             (12, 77, 80), (20, 85, 97)],
    # The blame dialogues: followers vs leaders, the companion, Satan's speech.
    "blame-dialogues":    [(7, 37, 39), (14, 21, 22), (40, 47, 50), (41, 29, 29), (38, 55, 64),
                           (37, 27, 33), (37, 50, 57), (50, 23, 29), (2, 166, 167), (34, 31, 33),
                           (25, 27, 29), (43, 36, 39), (33, 64, 68)],
    # Regret the Quran tells people NOT to have, and grief it praises.
    "forbidden-or-praised-sorrow": [(57, 22, 23), (3, 153, 153), (3, 156, 156), (3, 168, 168),
                                    (5, 26, 26), (5, 68, 68), (35, 8, 8), (18, 6, 6), (26, 3, 3),
                                    (12, 84, 87), (9, 92, 92)],
    # What the hands sent forward — the deed-ledger the gestures point at.
    "hands-sent-forward": [(78, 40, 40), (89, 24, 24), (59, 18, 18), (18, 57, 57), (2, 95, 95),
                           (62, 7, 7), (3, 182, 182), (22, 10, 10)],
    # Passages where the regretful (or God) itemise the CAUSES. Reverse-engineering material.
    "stated-causes":      [(74, 38, 48), (69, 30, 37), (89, 15, 24), (57, 12, 15), (39, 59, 60),
                           (7, 50, 51), (45, 33, 35), (75, 20, 25), (76, 27, 27), (87, 16, 17),
                           (79, 37, 39), (18, 28, 28), (63, 9, 9), (102, 1, 8), (6, 130, 130),
                           (83, 14, 14), (18, 35, 36), (68, 17, 28)],
    # Loss and the Day of mutual dispossession.
    "loss-and-taghabun":  [(64, 9, 10), (39, 15, 15), (42, 45, 45), (18, 103, 105), (103, 1, 3),
                           (79, 10, 14)],
}
TRANSLATIONS = ["saheeh", "khattab"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS}
    out = {"note": "Slim verse pack for the regret investigation. Arabic (Uthmani Hafs) + "
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
    dest = os.path.join(root, "data/structural/regret-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")
    for g, v in out["groups"].items():
        print(f"  {g:30} {len(v)}")


if __name__ == "__main__":
    main()
