#!/usr/bin/env python3
"""Build a slim verse pack for the fasting investigation.

Emits data/structural/fasting-versepack.json and notes/fasting/0-structural/versepack.md
so Phase-1 agents can read ~60 verses instead of quran.json (6,236 ayahs) + 4 full
translation files. Optimization B (slim agent reads) from notes/research-optimization-plan.md.
"""
import json, os

RANGES = {
    "core-ramadan": [(2, 183, 187)],
    "hajj-substitute": [(2, 196, 197)],
    "expiation": [(4, 92, 92), (5, 89, 89), (5, 95, 95), (58, 1, 4)],
    "maryam-silence": [(19, 16, 26)],
    "identity-list": [(33, 35, 35)],
    "qadr-night": [(97, 1, 5), (44, 1, 6), (2, 189, 189)],
    "sabr-support": [(2, 45, 45), (2, 153, 153), (3, 200, 200), (103, 1, 3)],
    "birr-definition": [(2, 177, 177)],
    "eating-limits": [(7, 31, 31), (5, 87, 88), (20, 81, 81), (6, 141, 141)],
    "night-vigil": [(73, 1, 8), (73, 20, 20), (17, 79, 79), (51, 15, 19), (32, 15, 17)],
    "feeding-others": [(76, 5, 12), (90, 11, 18), (69, 30, 34), (107, 1, 7), (89, 17, 20)],
    "servants-of-rahman": [(25, 63, 68)],
    "hunger-tests": [(2, 155, 157), (7, 130, 130), (16, 112, 112), (106, 1, 4)],
    "taqwa-anchors": [(49, 13, 13), (22, 37, 37), (2, 197, 197), (65, 2, 4), (7, 26, 26)],
    "itikaf-idols": [(2, 187, 187), (7, 138, 138), (21, 52, 53), (20, 91, 97)],
}

TRANSLATIONS = ["saheeh", "khattab", "arberry", "pickthall"]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q = json.load(open(os.path.join(root, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {}
    for t in TRANSLATIONS:
        trans[t] = json.load(open(os.path.join(root, f"data/translations/{t}.json")))["ayahs"]

    out = {"note": "Slim verse pack for the fasting investigation. Arabic (Uthmani Hafs) "
                   "+ 4 translations for every verse an agent should need.",
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
                    "ref": key,
                    "surah_name": s["name_english"],
                    "revelation": s["revelation"],
                    "arabic": arabic,
                    **{t: trans[t].get(key, "") for t in TRANSLATIONS},
                })
                seen.add(key)
        out["groups"][group] = verses

    out["verse_count"] = len(seen)
    os.makedirs(os.path.join(root, "data/structural"), exist_ok=True)
    dest = os.path.join(root, "data/structural/fasting-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses across {len(RANGES)} groups")


if __name__ == "__main__":
    main()
