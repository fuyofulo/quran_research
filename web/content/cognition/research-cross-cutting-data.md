# Cross-cutting investigation: Inter-root structural data

> **Source:** Cross-cutting Bash analyses (Phase 1, parallel to the deep-read agents), deep "research" investigation, 2026-04-26.
> **Method:** Direct Python queries over `data/morphology/words.jsonl` and concept JSONs.
> **Reproducible:** The exact scripts used are inline below.

This file collects the structural data that no single root analysis could produce — patterns visible only when comparing roots against each other.

## 1. Inter-cognitive-root co-occurrence matrix

Which cognitive roots appear together in the same ayah? The matrix shows count of ayahs where both roots co-occur.

```
       Elm   *kr   Hkm   bSr   nZr   sAl   wjd   bgy   qrA   Eql   dbr   fqh   fkr   lbb
علم      0    44    71    13     5    27    11    17     9     3     1     0     1     5
ذكر     44     0     9    11     4     8     0     7    11     1     3     2     2    10
حكم     71     9     0     2     1     2     2     7     3     0     0     0     0     2
بصر     13    11     2     0     4     1     2     3     0     1     1     1     1     0
نظر      5     4     1     4     0     2     2     1     0     1     0     2     0     0
سأل     27     8     2     1     2     0     0     1     2     2     1     0     1     0
وجد     11     0     2     2     2     0     0     4     2     0     2     1     0     0
بغي     17     7     7     3     1     1     4     0     2     0     0     0     0     1
قرأ      9    11     3     0     0     2     2     2     0     2     3     1     1     0
عقل      3     1     0     1     1     2     0     0     2     0     0     0     0     0
دبر      1     3     0     1     0     1     2     0     3     0     0     1     0     1
فقه      0     2     0     1     2     0     1     0     1     0     1     0     0     0
فكر      1     2     0     1     0     1     0     0     1     0     0     0     0     0
لبب      5    10     2     0     0     0     0     1     0     0     1     0     0     0
```

## 2. Top cognitive-root pairs (ranked by ayah co-occurrence)

| Pair | Ayahs together | Note |
|---|---|---|
| علم ~ حكم | **71** | The al-ʿAlīm al-Ḥakīm divine-attribute formula — dominant pairing in the Quran |
| علم ~ ذكر | 44 | Knowledge + remembrance |
| علم ~ سأل | 27 | Asking → knowing |
| علم ~ بغي | 17 | Knowledge + seeking (or transgressing) |
| علم ~ بصر | 13 | Knowing + seeing |
| علم ~ وجد | 11 | Knowing + finding |
| ذكر ~ بصر | 11 | Remembrance + sight |
| ذكر ~ قرأ | 11 | Remembrance + recitation |
| **ذكر ~ لبب** | **10** | **Remembrance + the kernel — 62.5% of all lbb ayahs!** |
| علم ~ قرأ | 9 | Knowing + reading |
| ذكر ~ حكم | 9 | Remembrance + judgment |
| ذكر ~ سأل | 8 | Remembrance + asking |
| ذكر ~ بغي | 7 | Remembrance + seeking |
| حكم ~ بغي | 7 | Wisdom + transgression |
| علم ~ لبب | 5 | Knowing + the kernel |
| علم ~ نظر | 5 | Knowing + observation |
| ذكر ~ نظر | 4 | Remembrance + looking |
| بصر ~ نظر | 4 | Insight + observation (notably low for "two seeing roots") |
| وجد ~ بغي | 4 | Finding + seeking |
| علم ~ عقل | 3 | Knowing + reasoning (notably low) |
| ذكر ~ دبر | 3 | Remembrance + pondering |
| حكم ~ قرأ | 3 | Judgment + recitation |
| بصر ~ بغي | 3 | Insight + seeking |
| قرأ ~ دبر | 3 | Recitation + pondering — the tadabbur cluster |
| ذكر ~ فكر | 2 | Remembrance + reflection |

## 3. Zero-co-occurrence pairs (cognitive roots that NEVER appear in the same ayah)

**31 cognitive-root pairs NEVER co-occur in any ayah** — the cognitive vocabulary is not a single semantic field but clusters of mostly-disjoint conceptual neighborhoods:

- علم (Elm) ~ فقه (fqh) — knowledge and deep comprehension never share an ayah
- ذكر (*kr) ~ وجد (wjd) — remembrance and finding never share an ayah
- حكم (Hkm) ~ عقل (Eql) — wisdom and reasoning never share an ayah
- حكم (Hkm) ~ دبر (dbr)
- حكم (Hkm) ~ فقه (fqh)
- حكم (Hkm) ~ فكر (fkr) — wisdom and reflection never share an ayah
- بصر (bSr) ~ قرأ (qrA)
- بصر (bSr) ~ لبب (lbb)
- نظر (nZr) ~ قرأ (qrA)
- نظر (nZr) ~ دبر (dbr)
- نظر (nZr) ~ فكر (fkr)
- نظر (nZr) ~ لبب (lbb)
- سأل (sAl) ~ وجد (wjd)
- سأل (sAl) ~ فقه (fqh)
- سأل (sAl) ~ لبب (lbb)
- وجد (wjd) ~ عقل (Eql)
- وجد (wjd) ~ فكر (fkr)
- وجد (wjd) ~ لبب (lbb)
- بغي (bgy) ~ عقل (Eql)
- بغي (bgy) ~ دبر (dbr)
- بغي (bgy) ~ فقه (fqh)
- بغي (bgy) ~ فكر (fkr)
- قرأ (qrA) ~ لبب (lbb)
- عقل (Eql) ~ دبر (dbr) — reasoning and pondering never share an ayah
- عقل (Eql) ~ فقه (fqh) — reasoning and deep comprehension never share an ayah
- عقل (Eql) ~ فكر (fkr) — reasoning and reflection never share an ayah
- عقل (Eql) ~ لبب (lbb) — reasoning and the kernel never share an ayah
- دبر (dbr) ~ فكر (fkr)
- فقه (fqh) ~ فكر (fkr)
- فقه (fqh) ~ لبب (lbb)
- فكر (fkr) ~ لبب (lbb)

**Eql (reason) is the most isolated:** it never co-occurs with dbr, fqh, fkr, or lbb. The "binding-of-inferences" verb stands apart from the other reflective/comprehensive cognitive roots.

## 4. Verb-form analysis per cognitive root (imperative vs indicative)

| Root | V total | perfect | imperfect | imperative | imperative% | passive |
|---|---|---|---|---|---|---|
| علم (Elm) | 425 | 60 | 334 | 31 | 7.3% | 4 |
| ذكر (*kr) | 154 | 27 | 71 | **56** | **36.4%** | 21 |
| حكم (Hkm) | 50 | 4 | 39 | 7 | 14.0% | 1 |
| بصر (bSr) | 33 | 4 | 25 | 4 | 12.1% | 1 |
| نظر (nZr) | 107 | 3 | 56 | **48** | **44.9%** | 6 |
| سأل (sAl) | 115 | 21 | 78 | 16 | 13.9% | 19 |
| وجد (wjd) | 106 | 39 | 67 | 0 | 0.0% | 1 |
| بغي (bgy) | 65 | 10 | 49 | 6 | 9.2% | 1 |
| قرأ (qrA) | 17 | 6 | 5 | 6 | **35.3%** | 2 |
| عقل (Eql) | 49 | 1 | 48 | 0 | 0.0% | 0 |
| دبر (dbr) | 12 | 4 | 8 | 0 | 0.0% | 0 |
| فقه (fqh) | 20 | 0 | 20 | 0 | 0.0% | 0 |
| فكر (fkr) | 18 | 1 | 17 | 0 | 0.0% | 0 |

**Most-commanded cognitive roots (highest imperative %):**
1. **نظر (nZr): 44.9%** — "Look! Consider!" — the Quran's signature attention-directing verb
2. **ذكر (*kr): 36.4%** — "Remember! Mention!"
3. **قرأ (qrA): 35.3%** — "Read!"
4. حكم (Hkm): 14.0%
5. سأل (sAl): 13.9%
6. بصر (bSr): 12.1%
7. بغي (bgy): 9.2%
8. علم (Elm): 7.3%

**Roots NEVER given as imperative verbs (0% imperative):**
- وجد (wjd) — find
- عقل (Eql) — reason
- دبر (dbr) — ponder
- فكر (fkr) — reflect
- فقه (fqh) — comprehend deeply

These five roots cannot be commanded. You cannot order someone to "find" or "comprehend" or "reason" — these are stative or descriptive, not imperative-able. The Quran is morphologically careful: it commands what can be commanded (look, remember, read) and merely describes the failure of what cannot be commanded (find, comprehend, reason).

## 5. Meccan vs Medinan distribution by cognitive root

| Root | Total | Meccan | Medinan | Meccan % |
|---|---|---|---|---|
| علم (Elm) | 854 | 495 | 359 | 58% |
| ذكر (*kr) | 292 | 216 | 76 | 74% |
| حكم (Hkm) | 210 | 93 | **117** | **44%** ← only Medinan-leaning |
| بصر (bSr) | 148 | 109 | 39 | 74% |
| نظر (nZr) | 129 | 99 | 30 | 77% |
| سأل (sAl) | 129 | 89 | 40 | 69% |
| وجد (wjd) | 107 | 59 | 48 | 55% |
| بغي (bgy) | 96 | 55 | 41 | 57% |
| قرأ (qrA) | 88 | 78 | 10 | 89% |
| عقل (Eql) | 49 | 30 | 19 | 61% |
| دبر (dbr) | 44 | 28 | 16 | 64% |
| فقه (fqh) | 20 | 10 | 10 | 50% |
| فكر (fkr) | 18 | 13 | 5 | 72% |
| لبب (lbb) | 16 | 8 | 8 | 50% |

**Ranking by Meccan dominance:**
- قرأ (qrA): 89% — the most Meccan, naturally — recitation is the foundational early act
- نظر (nZr): 77% — observation as Meccan empiricism
- ذكر (*kr): 74% — remembrance, especially of past nations
- بصر (bSr): 74% — insight as Meccan theme
- فكر (fkr): 72% — reflection
- سأل (sAl): 69% — asking (cosmological in Mecca)
- دبر (dbr): 64%
- عقل (Eql): 61%
- علم (Elm): 58%
- بغي (bgy): 57%
- وجد (wjd): 55%
- فقه (fqh): 50% (perfectly balanced)
- لبب (lbb): 50% (perfectly balanced — see lbb analysis)
- **حكم (Hkm): 44% — the unique inversion. Wisdom-as-judgment is a Medinan act.**

## 6. Surahs with highest cognitive-root density (occurrences per ayah)

| Surah | Name | Revelation | Cog count | Ayahs | Density |
|---|---|---|---|---|---|
| 60 | Al-Mumtahana | Medinan | 12 | 13 | **0.923** |
| 62 | Al-Jumu'a | Medinan | 10 | 11 | 0.909 |
| 49 | Al-Hujuraat | Medinan | 14 | 18 | 0.778 |
| 2 | Al-Baqara | Medinan | 200 | 286 | 0.699 |
| 24 | An-Noor | Medinan | 43 | 64 | 0.672 |
| 5 | Al-Maaida | Medinan | 76 | 120 | 0.633 |
| 102 | At-Takaathur | Meccan | 5 | 8 | 0.625 |
| 6 | Al-An'aam | Meccan | 100 | 165 | 0.606 |
| 12 | Yusuf | Meccan | 67 | 111 | 0.604 |
| 48 | Al-Fath | Medinan | 16 | 29 | 0.552 |
| 73 | Al-Muzzammil | Meccan | 11 | 20 | 0.550 |
| 59 | Al-Hashr | Medinan | 13 | 24 | 0.542 |
| 29 | Al-Ankaboot | Meccan | 37 | 69 | 0.536 |
| 47 | Muhammad | Medinan | 20 | 38 | 0.526 |
| 17 | Al-Israa | Meccan | 58 | 111 | 0.523 |

**Observations:**
- The top 3 by density are all Medinan, late community-formation surahs.
- Surah 60 (Al-Mumtahana) at 92.3% density: nearly every ayah contains a cognitive root. The surah is about loyalty/disloyalty — it requires sustained moral cognition.
- Surah Yusuf (12) — the great prophetic narrative — is the densest Meccan surah, full of finding (`wjd`), seeing (`bSr`), knowing (`Elm`).
- Surah 102 (At-Takaathur) is the smallest surah on the list (8 ayahs) — its density (62.5%) reflects its concentrated theme: "you are diverted by accumulation… you will SEE Hellfire, then SEE it with certainty of insight."

## Reproducibility

These analyses are reproducible by running:

```python
# Inter-root co-occurrence
import json
from collections import defaultdict
ayah_roots = defaultdict(set)
with open('/Users/fuyofulo/research/quran/data/morphology/words.jsonl') as f:
    for line in f:
        w = json.loads(line)
        if w.get('root'):
            ayah_roots[(w['surah'], w['ayah'])].add(w['root'])

COG = ['Elm', '*kr', 'Hkm', 'bSr', 'nZr', 'sAl', 'wjd', 'bgy', 'qrA', 'Eql', 'dbr', 'fqh', 'fkr', 'lbb']
co = {r: defaultdict(int) for r in COG}
for ay, roots in ayah_roots.items():
    cog_in = [r for r in COG if r in roots]
    for a in cog_in:
        for b in cog_in:
            if a != b:
                co[a][b] += 1
```

For verb-form analysis, query `data/morphology/words.jsonl` filtering by root and inspecting the `flags` field for `IMPV`/`PERF`/`IMPF` and `features` dict for `MOOD`/`PER`/`VOICE`.

For Meccan/Medinan and density: read each `data/concepts/<root>.json` `distribution.by_revelation` and combine with surah ayah-counts from `data/arabic/quran.json`.
