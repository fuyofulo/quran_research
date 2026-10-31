#!/usr/bin/env python3
"""Slim verse pack for the Sulaymān (Solomon) investigation.

Agents read their groups and never open quran.json. Groups follow the Phase-0 census
(scripts/build_sulaiman_census.py). Emits data/structural/sulaiman-versepack.json.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RANGES = {
    # The longest telling: knowledge, the ant, the hoopoe, the queen of Sabaʾ, the throne, the palace.
    "naml":            [(27, 15, 44)],
    # David's trial and his verdict, then Solomon's horses, trial and kingdom, then Job (shared formulas).
    "sad":             [(38, 17, 44)],
    # David's gifts, Solomon's gifts, "work in thanks", his death; then the people of Sabaʾ.
    "saba":            [(34, 10, 19)],
    # The field judgment, David's mountains and birds, the wind, the divers; then Job.
    "anbiya":          [(21, 78, 84)],
    # The devils, sorcery, Hārūt and Mārūt: "Solomon did not disbelieve".
    "baqarah":         [(2, 101, 103)],
    # Where Solomon stands among the prophets, and David's frame.
    "lists-and-david": [(4, 163, 165), (6, 83, 90), (17, 55, 55), (2, 251, 251), (5, 78, 78)],
    # Highest translator divergence in the story (census), with all four translations.
    "hotspots":        [(38, 31, 34), (38, 40, 40), (27, 17, 17), (27, 29, 29), (27, 32, 32), (27, 37, 37), (27, 43, 43)],
}
TRANSLATIONS = ["saheeh", "khattab"]
HOTSPOT_EXTRA = ["pickthall", "arberry"]


def main():
    q = json.load(open(os.path.join(ROOT, "data/arabic/quran.json")))
    surahs = {s["number"]: s for s in q["surahs"]}
    trans = {t: json.load(open(os.path.join(ROOT, f"data/translations/{t}.json")))["ayahs"]
             for t in TRANSLATIONS + HOTSPOT_EXTRA}
    out = {"note": "Slim verse pack for the Sulaymān investigation. Arabic (Uthmani Hafs) + Saheeh + Khattab; "
                   "the hotspots group adds Pickthall and Arberry. Read only your groups. NOTE: Arabic open-fathatan "
                   "tanwin is written with a space before its alif; rejoin before any string search.", "groups": {}}
    seen = set()
    for group, spans in RANGES.items():
        names = TRANSLATIONS + (HOTSPOT_EXTRA if group == "hotspots" else [])
        verses = []
        for su, a1, a2 in spans:
            s = surahs[su]
            for a in range(a1, a2 + 1):
                k = f"{su}:{a}"
                arabic = next(x["text"] for x in s["ayahs"] if x["ayah"] == a)
                verses.append({"ref": k, "surah_name": s["name_english"], "arabic": arabic,
                               **{t: trans[t].get(k, "") for t in names}})
                seen.add(k)
        out["groups"][group] = verses
    out["verse_count"] = len(seen)
    dest = os.path.join(ROOT, "data/structural/sulaiman-versepack.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"wrote {dest}: {len(seen)} unique verses")
    for g, v in out["groups"].items():
        print(f"  {g:16} {len(v)}")


if __name__ == "__main__":
    main()
