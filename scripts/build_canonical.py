"""Build canonical Quran data: merge surah metadata + ayah text into one structured file.

Inputs:
  data/raw/quran.json                       — fawazahmed0 Uthmani Hafs (6236 ayahs)
  data/raw/quran-uthmani.txt                — Tanzil Uthmani plain text
  data/metadata/surahs.json                 — alquran.cloud meta (114 surahs)

Outputs:
  data/arabic/quran.json                    — canonical: 114 surahs, each with meta + ayahs
  data/arabic/quran-uthmani.clean.txt       — Tanzil text with license comments stripped
  data/arabic/by-surah/NNN-<slug>.txt       — one plain-text file per surah
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
META = ROOT / "data" / "metadata"
OUT = ROOT / "data" / "arabic"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "by-surah").mkdir(parents=True, exist_ok=True)


def load_ayahs():
    with (RAW / "quran.json").open() as f:
        return json.load(f)["quran"]


def load_surah_meta():
    with (META / "surahs.json").open() as f:
        d = json.load(f)
    return {s["number"]: s for s in d["data"]["surahs"]["references"]}


def slugify(name: str) -> str:
    s = name.lower().replace("'", "").replace("’", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def build_canonical():
    ayahs = load_ayahs()
    meta = load_surah_meta()

    surahs = []
    by_num = {}
    for a in ayahs:
        n = a["chapter"]
        if n not in by_num:
            by_num[n] = []
        by_num[n].append({"ayah": a["verse"], "text": a["text"]})

    for n in sorted(by_num):
        m = meta[n]
        surahs.append({
            "number": n,
            "name_arabic": m["name"],
            "name_english": m["englishName"],
            "name_translation": m["englishNameTranslation"],
            "revelation": m["revelationType"],
            "ayah_count": m["numberOfAyahs"],
            "ayahs": by_num[n],
        })

    canonical = {
        "source": "fawazahmed0/quran-api (Uthmani Hafs) + alquran.cloud meta",
        "ayah_total": sum(len(s["ayahs"]) for s in surahs),
        "surah_total": len(surahs),
        "surahs": surahs,
    }

    out = OUT / "quran.json"
    with out.open("w") as f:
        json.dump(canonical, f, ensure_ascii=False, indent=2)
    print(f"wrote {out}  ({canonical['surah_total']} surahs, {canonical['ayah_total']} ayahs)")

    return surahs


def strip_tanzil_comments():
    src = RAW / "quran-uthmani.txt"
    dst = OUT / "quran-uthmani.clean.txt"
    lines = [ln for ln in src.read_text().splitlines() if ln and not ln.startswith("#")]
    dst.write_text("\n".join(lines) + "\n")
    print(f"wrote {dst}  ({len(lines)} lines)")


def write_per_surah(surahs):
    for s in surahs:
        slug = slugify(s["name_english"])
        path = OUT / "by-surah" / f"{s['number']:03d}-{slug}.txt"
        header = f"# {s['number']}. {s['name_english']} ({s['name_arabic']}) — {s['name_translation']}\n# {s['revelation']} · {s['ayah_count']} ayahs\n\n"
        body = "\n".join(f"{a['ayah']}. {a['text']}" for a in s["ayahs"])
        path.write_text(header + body + "\n")
    print(f"wrote {len(surahs)} per-surah files to {OUT / 'by-surah'}")


if __name__ == "__main__":
    surahs = build_canonical()
    strip_tanzil_comments()
    write_per_surah(surahs)
