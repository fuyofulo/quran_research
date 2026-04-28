"""Normalize all 5 translation sources into a uniform schema.

Inputs:
  data/raw/translations/saheeh.json     — alquran.cloud format
  data/raw/translations/pickthall.json  — alquran.cloud format
  data/raw/translations/arberry.json    — alquran.cloud format
  data/raw/translations/khattab.json    — fawazahmed0 format
  data/raw/translations/quran-com-wbw/  — 114 chapter files (quran.com format)

Outputs (data/translations/):
  saheeh.json, pickthall.json, arberry.json, khattab.json
    — full-sentence translations, keyed by "S:A" (e.g. "1:1")
    {
      "source": "Saheeh International",
      "ayahs": { "1:1": "In the name of Allah…", ... }
    }

  word-by-word.json
    — literal English glosses, keyed per word location "S:A:W"
    {
      "source": "quran.com word-by-word",
      "words": { "1:1:1": "In (the) name", "1:1:2": "(of) Allah", ... }
    }

The Arabic text is NOT stored in these files (it lives in data/arabic/).
These are display-only annotations on the canonical Arabic.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "translations"
OUT = ROOT / "data" / "translations"
OUT.mkdir(parents=True, exist_ok=True)


def from_alquran_cloud(path, source_name, source_id):
    """alquran.cloud: data.surahs[].ayahs[] with {numberInSurah, text}"""
    with path.open() as f:
        d = json.load(f)
    ayahs = {}
    for s in d["data"]["surahs"]:
        sn = s["number"]
        for a in s["ayahs"]:
            ayahs[f"{sn}:{a['numberInSurah']}"] = a["text"]
    return {"source": source_name, "source_id": source_id, "count": len(ayahs), "ayahs": ayahs}


def from_fawazahmed(path, source_name, source_id):
    """fawazahmed0: {quran: [{chapter, verse, text}]}"""
    with path.open() as f:
        d = json.load(f)
    ayahs = {}
    for a in d["quran"]:
        ayahs[f"{a['chapter']}:{a['verse']}"] = a["text"]
    return {"source": source_name, "source_id": source_id, "count": len(ayahs), "ayahs": ayahs}


# Match QAC location pattern (filter out verse-number markers from quran.com)
LOC_RE = re.compile(r"^\d+:\d+:\d+$")


def from_quran_com_wbw(dir_path, source_name, source_id):
    """quran.com per-chapter: verses[].words[] with {location, translation.text, char_type_name}"""
    words = {}
    for n in range(1, 115):
        with (dir_path / f"{n:03d}.json").open() as f:
            d = json.load(f)
        for v in d["verses"]:
            for w in v["words"]:
                loc = w.get("location", "")
                if not LOC_RE.match(loc):
                    continue  # skip verse-number markers etc.
                # skip "end" markers explicitly
                if w.get("char_type_name") == "end":
                    continue
                tr = (w.get("translation") or {}).get("text", "") or ""
                words[loc] = tr
    return {"source": source_name, "source_id": source_id, "count": len(words), "words": words}


def main():
    sources = [
        ("saheeh.json",    "Saheeh International",    "saheeh"),
        ("pickthall.json", "Pickthall (1930)",        "pickthall"),
        ("arberry.json",   "A.J. Arberry (1955)",     "arberry"),
    ]
    for raw_name, name, sid in sources:
        d = from_alquran_cloud(RAW / raw_name, name, sid)
        out = OUT / f"{sid}.json"
        with out.open("w") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"  {sid:18}  {d['count']} ayahs  →  {out}")

    d = from_fawazahmed(RAW / "khattab.json", "The Clear Quran (Mustafa Khattab, 2016)", "khattab")
    out = OUT / "khattab.json"
    with out.open("w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"  {'khattab':18}  {d['count']} ayahs  →  {out}")

    d = from_quran_com_wbw(RAW / "quran-com-wbw", "quran.com word-by-word", "word-by-word")
    out = OUT / "word-by-word.json"
    with out.open("w") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"  {'word-by-word':18}  {d['count']} words  →  {out}")


if __name__ == "__main__":
    main()
