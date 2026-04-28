"""Fetch word-by-word English glosses from quran.com API.

The /verses/by_chapter endpoint returns each ayah with its words, where each
word has:
  - location:    "surah:ayah:word"  (aligned with QAC word boundaries)
  - text_uthmani: Arabic
  - translation.text: literal English gloss

114 calls (one per chapter). Saves raw responses to data/raw/translations/quran-com-wbw/
so re-processing doesn't re-fetch.
"""

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "raw" / "translations" / "quran-com-wbw"
OUT.mkdir(parents=True, exist_ok=True)

URL = (
    "https://api.quran.com/api/v4/verses/by_chapter/{chapter}"
    "?words=true&word_translation_language=en"
    "&word_fields=text_uthmani,location"
    "&per_page=300"
)


def fetch_chapter(n):
    out_path = OUT / f"{n:03d}.json"
    if out_path.exists() and out_path.stat().st_size > 1000:
        return "cached"
    req = urllib.request.Request(
        URL.format(chapter=n),
        headers={
            "Accept": "application/json",
            "User-Agent": "quran-research/0.1 (https://github.com/research-personal)",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    out_path.write_bytes(data)
    return "fetched"


def main():
    for n in range(1, 115):
        try:
            status = fetch_chapter(n)
        except Exception as e:
            print(f"  chapter {n:3}: FAIL ({e})")
            continue
        if status == "fetched":
            time.sleep(0.3)  # be polite
        if n % 10 == 0 or n == 1:
            print(f"  chapter {n:3}: {status}")
    print(f"\ndone. files in {OUT}")


if __name__ == "__main__":
    main()
