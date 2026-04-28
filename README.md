# Quran Research

Long-term, first-principles study of the Quran: semantics, vocabulary, knowledge graphs, historical context.

## Layout

```
data/
  raw/          # untouched downloads (Tanzil, fawazahmed0, QAC)
  arabic/       # canonical text — quran.json, clean Uthmani, per-surah files
  metadata/     # surahs, juzs, sajdas, etc.
  morphology/   # QAC: segments.jsonl, words.jsonl, roots.json, lemmas.json, stats.json
scripts/
  build_canonical.py     # text + metadata
  buckwalter.py          # Arabic <-> Buckwalter conversion
  parse_morphology.py    # QAC -> structured JSON + indexes
notes/
```

## Morphology (QAC v0.4)

Word-by-word morphological annotation from the Quranic Arabic Corpus (Kais Dukes, GPL).

- **`data/morphology/words.jsonl`** — 77,429 words. Each: location `[surah, ayah, word]`, `form_arabic`, `pos`, `lemma`, `root`, plus per-segment breakdown.
- **`data/morphology/roots.json`** — 1,642 roots. Each: `root_arabic`, `count`, `lemmas{}`, `pos_dist{}`, `occurrences[]`.
- **`data/morphology/lemmas.json`** — 4,832 lemmas. Each: `lemma_arabic`, `root`, `count`, `occurrences[]`.
- **`data/morphology/segments.jsonl`** — 128,219 segments (full PREFIX+STEM+SUFFIX detail).
- **`data/morphology/stats.json`** — totals.

Forms are stored in both Buckwalter (the QAC native ASCII encoding) and Arabic Unicode. Use `scripts/buckwalter.py` to convert.

## Canonical data

- **`data/arabic/quran.json`** — 114 surahs, each with metadata (name, revelation type, ayah count) and grouped ayahs in Uthmani Hafs script. Use this for any programmatic work.
- **`data/arabic/by-surah/NNN-<slug>.txt`** — one plain-text file per surah, easy to read or grep.
- **`data/arabic/quran-uthmani.clean.txt`** — flat 6236-line file (one ayah per line), Tanzil Uthmani.

## Sources

- [Tanzil.net](https://tanzil.net) — Uthmani + simple plain text and XML. Canonical reference for many academic projects.
- [fawazahmed0/quran-api](https://github.com/fawazahmed0/quran-api) — Uthmani Hafs JSON.
- [alquran.cloud API](https://alquran.cloud/api) — surah/juz/sajda/ruku metadata.

## Reproducing

```bash
python3 scripts/build_canonical.py
```

Regenerates everything in `data/arabic/` from `data/raw/` + `data/metadata/`.

## Counts

114 surahs · 6236 ayahs · Uthmani Hafs script.
