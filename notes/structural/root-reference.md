# Quranic Root Reference (1,642 roots)

Comprehensive lookup table for every Arabic root attested in the Quran. Built from `data/morphology/roots.json` (counts, lemmas, POS, occurrences), `notes/full-quran-graph/clusters.json` (Louvain clusters + 15 named clusters), `notes/full-quran-graph/data.json` (co-occurrence edges weighted by ayah count), and `data/metadata/surahs.json` (Meccan/Medinan classification).

**Source files:**
- JSON: `data/structural/root-reference.json` (full data, dict keyed by buckwalter root)
- CSV: `data/structural/root-reference.csv` (sortable spreadsheet view)

---

## Quick stats

- Total roots: **1642**
- Total occurrences: **49,967**
- Total clusters: **666** (named: 15)
- Roots without a cluster: **0**

**Notable-flag counts:**

| Flag | Count |
|---|---:|
| noun-only | 561 |
| high inter-cluster connectivity | 522 |
| rare (2-5 occurrences) | 503 |
| confined to 1 surah | 459 |
| single occurrence | 395 |
| verb-only | 235 |
| bridge (5+ neighbor clusters) | 222 |
| high Meccan concentration | 131 |
| high Medinan concentration | 33 |
| appears in 80+ surahs | 7 |
| proper-noun-only | 5 |

---

## Top 50 roots by frequency

| # | Root | Arabic | Count | Cluster | Notable |
|---:|---|---|---:|---|---|
| 1 | `Alh` | اله | 2,851 | Allegiance & the Object of Worship | high inter-cluster connectivity (131 clusters); appears in 80+ surahs |
| 2 | `qwl` | قول | 1,722 | Revelation, Speech & Disbelief | high inter-cluster connectivity (128 clusters); appears in 80+ surahs |
| 3 | `kwn` | كون | 1,390 | Revelation, Speech & Disbelief | high inter-cluster connectivity (127 clusters); appears in 80+ surahs |
| 4 | `rbb` | ربب | 980 | Revelation, Speech & Disbelief | noun-only; high inter-cluster connectivity (113 clusters); appears in 80+ surahs |
| 5 | `Amn` | امن | 879 | The Believers' Reward | high inter-cluster connectivity (110 clusters) |
| 6 | `Elm` | علم | 854 | Revelation, Speech & Disbelief | high inter-cluster connectivity (107 clusters); appears in 80+ surahs |
| 7 | `qwm` | قوم | 660 | Allegiance & the Object of Worship | high inter-cluster connectivity (100 clusters) |
| 8 | `Aty` | اتي | 549 | Revelation, Speech & Disbelief | high inter-cluster connectivity (99 clusters) |
| 9 | `kfr` | كفر | 525 | The Prepared Fire | high inter-cluster connectivity (98 clusters) |
| 10 | `byn` | بين | 523 | Revelation, Speech & Disbelief | high inter-cluster connectivity (93 clusters) |
| 11 | `$yA` | شيا | 519 | Divine Will & Dominion | high inter-cluster connectivity (102 clusters) |
| 12 | `rsl` | رسل | 513 | Revelation, Speech & Disbelief | high inter-cluster connectivity (83 clusters) |
| 13 | `ArD` | ارض | 461 | cluster 1 | noun-only; high inter-cluster connectivity (98 clusters); appears in 80+ surahs |
| 14 | `ywm` | يوم | 405 | cluster 78 | high inter-cluster connectivity (86 clusters) |
| 15 | `Ayy` | ايي | 382 | Revelation, Speech & Disbelief | noun-only; high inter-cluster connectivity (82 clusters) |
| 16 | `smw` | سمو | 381 | cluster 1 | high inter-cluster connectivity (82 clusters); appears in 80+ surahs |
| 17 | `kll` | كلل | 377 | Divine Will & Dominion | high inter-cluster connectivity (94 clusters) |
| 18 | `E*b` | عذب | 373 | The Prepared Fire | high inter-cluster connectivity (88 clusters) |
| 19 | `Eml` | عمل | 360 | The Believers' Reward | high inter-cluster connectivity (77 clusters) |
| 20 | `jEl` | جعل | 346 | cluster 44 | high inter-cluster connectivity (96 clusters) |
| 21 | `rHm` | رحم | 339 | Sin–Mercy Economy | high inter-cluster connectivity (72 clusters) |
| 22 | `rAy` | راي | 328 | Witnessing the Visible Sign | high inter-cluster connectivity (102 clusters) |
| 23 | `ktb` | كتب | 319 | Revelation, Speech & Disbelief | high inter-cluster connectivity (80 clusters) |
| 24 | `hdy` | هدي | 316 | Allegiance & the Object of Worship | high inter-cluster connectivity (66 clusters) |
| 25 | `Zlm` | ظلم | 315 | Revelation, Speech & Disbelief | high inter-cluster connectivity (76 clusters) |
| 26 | `nfs` | نفس | 298 | The Commanded Self | high inter-cluster connectivity (82 clusters) |
| 27 | `qbl` | قبل | 294 | Revelation, Speech & Disbelief | high inter-cluster connectivity (85 clusters) |
| 28 | `nzl` | نزل | 293 | Revelation, Speech & Disbelief | high inter-cluster connectivity (76 clusters) |
| 29 | `*kr` | ذكر | 292 | Household Law & Lineage | high inter-cluster connectivity (74 clusters) |
| 30 | `Hqq` | حقق | 287 | Revelation, Speech & Disbelief | high inter-cluster connectivity (72 clusters) |
| 31 | `k*b` | كذب | 282 | Revelation, Speech & Disbelief | high inter-cluster connectivity (47 clusters) |
| 32 | `jyA` | جيا | 278 | Revelation, Speech & Disbelief | verb-only; high inter-cluster connectivity (79 clusters) |
| 33 | `Ebd` | عبد | 275 | Allegiance & the Object of Worship | high inter-cluster connectivity (68 clusters) |
| 34 | `Ax*` | اخذ | 273 | cluster 95 | high inter-cluster connectivity (79 clusters) |
| 35 | `xlq` | خلق | 261 | Creation & the Appointed Term | high inter-cluster connectivity (59 clusters) |
| 36 | `wqy` | وقي | 258 | The Commanded Self | high inter-cluster connectivity (60 clusters) |
| 37 | `Axr` | اخر | 250 | Dunya vs. Ākhirah | high inter-cluster connectivity (68 clusters) |
| 38 | `Amr` | امر | 248 | The Commanded Self | high inter-cluster connectivity (76 clusters) |
| 39 | `nws` | نوس | 241 | Revelation, Speech & Disbelief | noun-only; high inter-cluster connectivity (81 clusters) |
| 40 | `bEd` | بعد | 235 | Revelation, Speech & Disbelief | high inter-cluster connectivity (74 clusters) |
| 41 | `gfr` | غفر | 234 | Sin–Mercy Economy | high inter-cluster connectivity (60 clusters) |
| 42 | `wly` | ولي | 232 | Allegiance & the Object of Worship | high inter-cluster connectivity (63 clusters) |
| 43 | `dEw` | دعو | 212 | Allegiance & the Object of Worship | high inter-cluster connectivity (59 clusters) |
| 44 | `Hkm` | حكم | 210 | Revelation, Speech & Disbelief | high inter-cluster connectivity (60 clusters) |
| 45 | `mlk` | ملك | 206 | Divine Will & Dominion | high inter-cluster connectivity (71 clusters) |
| 46 | `jnn` | جنن | 201 | The Believers' Reward | high inter-cluster connectivity (59 clusters) |
| 47 | `End` | عند | 201 | The Believers' Reward | high inter-cluster connectivity (66 clusters) |
| 48 | `xyr` | خير | 196 | The Commanded Self | high inter-cluster connectivity (64 clusters) |
| 49 | `nwr` | نور | 194 | The Believers' Reward | high inter-cluster connectivity (63 clusters) |
| 50 | `Hsn` | حسن | 194 | The Believers' Reward | high inter-cluster connectivity (68 clusters) |

---

## All roots by cluster

Named clusters first (ordered by total token count), then unnamed clusters by size, then roots with no cluster assignment. Each row: root (buckwalter) — arabic — count — notable.

### Named clusters

### Cluster 4: Revelation, Speech & Disbelief

_191 roots, 15,512 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qwl` | قول | 1,722 | 84 | 0.725 | high inter-cluster connectivity (128 clusters); appears in 80+ surahs |
| `kwn` | كون | 1,390 | 86 | 0.662 | high inter-cluster connectivity (127 clusters); appears in 80+ surahs |
| `rbb` | ربب | 980 | 94 | 0.778 | noun-only; high inter-cluster connectivity (113 clusters); appears in 80+ surahs |
| `Elm` | علم | 854 | 85 | 0.58 | high inter-cluster connectivity (107 clusters); appears in 80+ surahs |
| `Aty` | اتي | 549 | 72 | 0.617 | high inter-cluster connectivity (99 clusters) |
| `byn` | بين | 523 | 71 | 0.581 | high inter-cluster connectivity (93 clusters) |
| `rsl` | رسل | 513 | 69 | 0.538 | high inter-cluster connectivity (83 clusters) |
| `Ayy` | ايي | 382 | 59 | 0.757 | noun-only; high inter-cluster connectivity (82 clusters) |
| `ktb` | كتب | 319 | 61 | 0.486 | high inter-cluster connectivity (80 clusters) |
| `Zlm` | ظلم | 315 | 59 | 0.67 | high inter-cluster connectivity (76 clusters) |
| `qbl` | قبل | 294 | 64 | 0.629 | high inter-cluster connectivity (85 clusters) |
| `nzl` | نزل | 293 | 60 | 0.563 | high inter-cluster connectivity (76 clusters) |
| `Hqq` | حقق | 287 | 59 | 0.669 | high inter-cluster connectivity (72 clusters) |
| `k*b` | كذب | 282 | 68 | 0.748 | high inter-cluster connectivity (47 clusters) |
| `jyA` | جيا | 278 | 62 | 0.748 | verb-only; high inter-cluster connectivity (79 clusters) |
| `nws` | نوس | 241 | 53 | 0.494 | noun-only; high inter-cluster connectivity (81 clusters) |
| `bEd` | بعد | 235 | 57 | 0.553 | high inter-cluster connectivity (74 clusters) |
| `Hkm` | حكم | 210 | 57 | 0.443 | high inter-cluster connectivity (60 clusters) |
| `tbE` | تبع | 172 | 51 | 0.651 | high inter-cluster connectivity (52 clusters) |
| `Awl` | اول | 170 | 54 | 0.694 | high inter-cluster connectivity (55 clusters) |
| `kvr` | كثر | 167 | 51 | 0.617 | high inter-cluster connectivity (61 clusters) |
| `$hd` | شهد | 160 | 48 | 0.45 | high inter-cluster connectivity (43 clusters) |
| `nbA` | نبا | 160 | 47 | 0.444 | high inter-cluster connectivity (58 clusters) |
| `bED` | بعض | 158 | 38 | 0.487 | noun-only; high inter-cluster connectivity (47 clusters) |
| `Sdq` | صدق | 155 | 49 | 0.51 | high inter-cluster connectivity (48 clusters) |
| `wEd` | وعد | 151 | 51 | 0.768 | high inter-cluster connectivity (49 clusters) |
| `slm` | سلم | 140 | 48 | 0.593 | high inter-cluster connectivity (47 clusters) |
| `n*r` | نذر | 130 | 50 | 0.869 | high Meccan concentration; high inter-cluster connectivity (35 clusters) |
| `jmE` | جمع | 129 | 45 | 0.651 | high inter-cluster connectivity (47 clusters) |
| `nZr` | نظر | 129 | 48 | 0.767 | high inter-cluster connectivity (47 clusters) |
| `sAl` | سال | 129 | 47 | 0.69 | high inter-cluster connectivity (44 clusters) |
| `xlf` | خلف | 127 | 40 | 0.646 | high inter-cluster connectivity (54 clusters) |
| `Ahl` | اهل | 127 | 40 | 0.583 | noun-only; high inter-cluster connectivity (65 clusters) |
| `b$r` | بشر | 123 | 47 | 0.699 | high inter-cluster connectivity (44 clusters) |
| `Ezz` | عزز | 119 | 47 | 0.597 | high inter-cluster connectivity (39 clusters) |
| `Amm` | امم | 118 | 42 | 0.686 | high inter-cluster connectivity (45 clusters) |
| `Abw` | ابو | 117 | 37 | 0.795 | noun-only; high inter-cluster connectivity (43 clusters) |
| `rjE` | رجع | 104 | 42 | 0.731 | high inter-cluster connectivity (41 clusters) |
| `$dd` | شدد | 102 | 48 | 0.559 | high inter-cluster connectivity (48 clusters) |
| `qrA` | قرا | 88 | 42 | 0.886 | high Meccan concentration; high inter-cluster connectivity (35 clusters) |
| `kyf` | كيف | 83 | 37 | 0.735 | high inter-cluster connectivity (30 clusters) |
| `Eqb` | عقب | 80 | 32 | 0.575 | high inter-cluster connectivity (33 clusters) |
| `wHy` | وحي | 78 | 33 | 0.885 | high Meccan concentration; high inter-cluster connectivity (30 clusters) |
| `klm` | كلم | 75 | 32 | 0.613 | high inter-cluster connectivity (42 clusters) |
| `frq` | فرق | 72 | 30 | 0.417 | high inter-cluster connectivity (30 clusters) |
| `Znn` | ظنن | 69 | 32 | 0.696 | high inter-cluster connectivity (34 clusters) |
| `hlk` | هلك | 68 | 40 | 0.838 | high inter-cluster connectivity (23 clusters) |
| `bEv` | بعث | 67 | 33 | 0.731 | high inter-cluster connectivity (27 clusters) |
| `jrm` | جرم | 66 | 36 | 0.909 | high Meccan concentration; high inter-cluster connectivity (25 clusters) |
| `xsr` | خسر | 65 | 35 | 0.708 | high inter-cluster connectivity (24 clusters) |
| `tlw` | تلو | 63 | 33 | 0.571 | high inter-cluster connectivity (26 clusters) |
| `sHr` | سحر | 63 | 27 | 0.937 | high Meccan concentration; high inter-cluster connectivity (22 clusters) |
| `qDy` | قضي | 63 | 29 | 0.778 | high inter-cluster connectivity (28 clusters) |
| `gyb` | غيب | 60 | 35 | 0.7 | high inter-cluster connectivity (26 clusters) |
| `fry` | فري | 60 | 24 | 0.883 | high Meccan concentration; high inter-cluster connectivity (22 clusters) |
| `rdd` | ردد | 59 | 30 | 0.593 | high inter-cluster connectivity (36 clusters) |
| `qry` | قري | 57 | 26 | 0.825 | noun-only; high inter-cluster connectivity (29 clusters) |
| `swE` | سوع | 49 | 27 | 0.857 | high Meccan concentration; high inter-cluster connectivity (22 clusters) |
| `x$y` | خشي | 48 | 24 | 0.458 | high inter-cluster connectivity (24 clusters) |
| `bdl` | بدل | 44 | 25 | 0.523 | high inter-cluster connectivity (24 clusters) |
| `fSl` | فصل | 43 | 24 | 0.86 | high Meccan concentration; high inter-cluster connectivity (27 clusters) |
| `mkr` | مكر | 43 | 14 | 0.767 | high inter-cluster connectivity (15 clusters) |
| `qwy` | قوي | 42 | 25 | 0.714 | high inter-cluster connectivity (19 clusters) |
| `$Er` | شعر | 40 | 23 | 0.75 | high inter-cluster connectivity (21 clusters) |
| `mlA` | ملا | 40 | 18 | 0.95 | high Meccan concentration; high inter-cluster connectivity (23 clusters) |
| `*nb` | ذنب | 39 | 26 | 0.564 | noun-only; high inter-cluster connectivity (24 clusters) |
| `slT` | سلط | 39 | 27 | 0.795 | high inter-cluster connectivity (22 clusters) |
| `hwy` | هوي | 38 | 22 | 0.684 | high inter-cluster connectivity (20 clusters) |
| `sbq` | سبق | 37 | 24 | 0.811 | high inter-cluster connectivity (18 clusters) |
| `Alw` | الو | 37 | 6 | 0.081 | high Medinan concentration; bridge (6 clusters) |
| `ryb` | ريب | 36 | 26 | 0.556 | high inter-cluster connectivity (19 clusters) |
| `bTl` | بطل | 36 | 24 | 0.611 | high inter-cluster connectivity (23 clusters) |
| `Hdv` | حدث | 36 | 28 | 0.75 | high inter-cluster connectivity (21 clusters) |
| `qrn` | قرن | 36 | 20 | 0.944 | high Meccan concentration; high inter-cluster connectivity (16 clusters) |
| `Hjj` | حجج | 33 | 10 | 0.303 | high inter-cluster connectivity (22 clusters) |
| `brk` | برك | 32 | 22 | 0.875 | high Meccan concentration; high inter-cluster connectivity (21 clusters) |
| `Srf` | صرف | 30 | 17 | 0.833 | high inter-cluster connectivity (25 clusters) |
| `qSS` | قصص | 30 | 14 | 0.767 | high inter-cluster connectivity (13 clusters) |
| `jdl` | جدل | 29 | 16 | 0.655 | high inter-cluster connectivity (15 clusters) |
| `dry` | دري | 29 | 21 | 0.897 | verb-only; high Meccan concentration; bridge (9 clusters) |
| `yqn` | يقن | 28 | 19 | 0.821 | high inter-cluster connectivity (17 clusters) |
| `xlw` | خلو | 28 | 18 | 0.429 | high inter-cluster connectivity (17 clusters) |
| `Ejb` | عجب | 27 | 17 | 0.519 | high inter-cluster connectivity (17 clusters) |
| `syr` | سير | 27 | 21 | 0.815 | high inter-cluster connectivity (16 clusters) |
| `Hwl` | حول | 25 | 19 | 0.68 | high inter-cluster connectivity (21 clusters) |
| `lsn` | لسن | 25 | 18 | 0.68 | noun-only; high inter-cluster connectivity (15 clusters) |
| `jhl` | جهل | 24 | 17 | 0.625 | high inter-cluster connectivity (15 clusters) |
| `srf` | سرف | 23 | 17 | 0.87 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `gwy` | غوي | 22 | 11 | 0.955 | high Meccan concentration; bridge (5 clusters) |
| `Erb` | عرب | 22 | 15 | 0.5 | high inter-cluster connectivity (16 clusters) |
| `Avr` | اثر | 21 | 16 | 0.81 | high inter-cluster connectivity (11 clusters) |
| `mry` | مري | 20 | 16 | 0.85 | high Meccan concentration; bridge (6 clusters) |
| `Hzb` | حزب | 20 | 13 | 0.55 | noun-only; high inter-cluster connectivity (10 clusters) |
| `mkn` | مكن | 18 | 12 | 0.833 | bridge (9 clusters) |
| `nqm` | نقم | 17 | 12 | 0.706 | bridge (5 clusters) |
| `lbb` | لبب | 16 | 10 | 0.5 | noun-only; high inter-cluster connectivity (11 clusters) |
| `sTr` | سطر | 16 | 14 | 0.875 | high Meccan concentration; bridge (5 clusters) |
| `kff` | كفف | 15 | 9 | 0.2 | high inter-cluster connectivity (13 clusters) |
| `$kk` | شكك | 15 | 11 | 0.933 | noun-only; high Meccan concentration; bridge (6 clusters) |
| `rAf` | راف | 13 | 8 | 0.154 | high inter-cluster connectivity (11 clusters) |
| `bgt` | بغت | 13 | 10 | 0.846 | noun-only; bridge (7 clusters) |
| `jHd` | جحد | 12 | 10 | 1.0 | verb-only; high Meccan concentration; bridge (6 clusters) |
| `$yE` | شيع | 12 | 9 | 0.917 | high Meccan concentration; bridge (6 clusters) |
| `nTq` | نطق | 12 | 9 | 1.0 | high Meccan concentration |
| `zbr` | زبر | 11 | 10 | 0.818 | bridge (5 clusters) |
| `frr` | فرر | 11 | 9 | 0.636 |  |
| `$fq` | شفق | 11 | 9 | 0.818 | bridge (5 clusters) |
| `rjz` | رجز | 10 | 7 | 0.8 | noun-only; bridge (6 clusters) |
| `dmr` | دمر | 10 | 8 | 0.9 | high Meccan concentration; bridge (5 clusters) |
| `gnm` | غنم | 9 | 6 | 0.333 | bridge (8 clusters) |
| `srq` | سرق | 9 | 4 | 0.667 |  |
| `knz` | كنز | 9 | 6 | 0.667 |  |
| `trf` | ترف | 8 | 7 | 1.0 | high Meccan concentration |
| `nsk` | نسك | 7 | 3 | 0.143 | noun-only; high Medinan concentration; bridge (5 clusters) |
| `skr` | سكر | 7 | 5 | 0.571 |  |
| `wEy` | وعي | 7 | 4 | 1.0 | high Meccan concentration |
| `mkv` | مكث | 7 | 7 | 0.857 | high Meccan concentration |
| `tsE` | تسع | 7 | 5 | 1.0 | noun-only; high Meccan concentration |
| `Asr` | اسر | 6 | 4 | 0.0 | high Medinan concentration; bridge (5 clusters) |
| `Ady` | ادي | 6 | 4 | 0.167 |  |
| `Hmr` | حمر | 6 | 6 | 0.667 | noun-only |
| `dAb` | داب | 6 | 5 | 0.5 | noun-only |
| `drs` | درس | 6 | 5 | 0.833 |  |
| `lHq` | لحق | 6 | 6 | 0.667 | verb-only |
| `sdd` | سدد | 6 | 4 | 0.667 |  |
| `qfw` | قفو | 5 | 4 | 0.2 | verb-only; rare (5 occ.) |
| `Hsd` | حسد | 5 | 4 | 0.4 | rare (5 occ.) |
| `sbT` | سبط | 5 | 4 | 0.2 | noun-only; rare (5 occ.) |
| `lwy` | لوي | 5 | 3 | 0.0 | rare (5 occ.); high Medinan concentration |
| `lyn` | لين | 5 | 5 | 0.6 | rare (5 occ.) |
| `HyS` | حيص | 5 | 5 | 0.8 | noun-only; rare (5 occ.) |
| `$rE` | شرع | 5 | 4 | 0.8 | rare (5 occ.); bridge (6 clusters) |
| `Sdf` | صدف | 5 | 2 | 1.0 | rare (5 occ.); high Meccan concentration |
| `xrS` | خرص | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |
| `gwv` | غوث | 5 | 4 | 0.8 | verb-only; rare (5 occ.) |
| `mDy` | مضي | 5 | 5 | 0.8 | rare (5 occ.) |
| `zhq` | زهق | 5 | 3 | 0.6 | rare (5 occ.); bridge (8 clusters) |
| `lzm` | لزم | 5 | 5 | 0.8 | rare (5 occ.) |
| `zll` | زلل | 4 | 3 | 0.25 | verb-only; rare (4 occ.) |
| `nsx` | نسخ | 4 | 4 | 0.5 | rare (4 occ.) |
| `bdE` | بدع | 4 | 4 | 0.5 | rare (4 occ.) |
| `dlw` | دلو | 4 | 3 | 0.75 | rare (4 occ.) |
| `$wr` | شور | 4 | 4 | 0.5 | rare (4 occ.) |
| `nml` | نمل | 4 | 2 | 0.75 | noun-only; rare (4 occ.) |
| `lmm` | لمم | 4 | 4 | 0.75 | rare (4 occ.) |
| `jdr` | جدر | 4 | 3 | 0.5 | noun-only; rare (4 occ.) |
| `$yx` | شيخ | 4 | 4 | 1.0 | rare (4 occ.) |
| `mjd` | مجد | 4 | 3 | 1.0 | rare (4 occ.) |
| `gyv` | غيث | 4 | 4 | 0.75 | rare (4 occ.) |
| `zwl` | زول | 4 | 2 | 1.0 | rare (4 occ.) |
| `Ejm` | عجم | 4 | 3 | 1.0 | rare (4 occ.) |
| `dHD` | دحض | 4 | 4 | 1.0 | rare (4 occ.) |
| `rtl` | رتل | 4 | 2 | 1.0 | rare (4 occ.) |
| `SrH` | صرح | 4 | 3 | 1.0 | noun-only; rare (4 occ.) |
| `nEj` | نعج | 4 | 1 | 1.0 | noun-only; rare (4 occ.); confined to 1 surah |
| `lfw` | لفو | 3 | 3 | 0.667 | verb-only; rare (3 occ.) |
| `xyT` | خيط | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |
| `x*l` | خذل | 3 | 3 | 0.667 | rare (3 occ.) |
| `$nA` | شنا | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |
| `slx` | سلخ | 3 | 3 | 0.667 | verb-only; rare (3 occ.) |
| `Hfw` | حفو | 3 | 3 | 0.667 | rare (3 occ.) |
| `rhT` | رهط | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |
| `Sbw` | صبو | 3 | 2 | 1.0 | rare (3 occ.) |
| `fqd` | فقد | 3 | 2 | 1.0 | verb-only; rare (3 occ.) |
| `brH` | برح | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |
| `$kw` | شكو | 3 | 3 | 0.333 | rare (3 occ.) |
| `xft` | خفت | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |
| `rqm` | رقم | 3 | 2 | 1.0 | rare (3 occ.) |
| `$TT` | شطط | 3 | 3 | 1.0 | rare (3 occ.) |
| `vll` | ثلل | 3 | 1 | 1.0 | noun-only; rare (3 occ.); confined to 1 surah |
| `EDD` | عضض | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `kyn` | كين | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `glw` | غلو | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |
| `Evr` | عثر | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `qrTs` | قرطس | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `qdw` | قدو | 2 | 2 | 1.0 | rare (2 occ.) |
| `bTr` | بطر | 2 | 2 | 0.5 | rare (2 occ.) |
| `nkS` | نكص | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `jbb` | جبب | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `lqT` | لقط | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |
| `bEr` | بعر | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `Sfd` | صفد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `HZr` | حظر | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `Hff` | حفف | 2 | 2 | 1.0 | rare (2 occ.) |
| `h$m` | هشم | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `gTw` | غطو | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `Arb` | ارب | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |
| `Azr` | ازر | 2 | 2 | 0.5 | rare (2 occ.) |
| `nf$` | نفش | 2 | 2 | 1.0 | rare (2 occ.) |
| `qyD` | قيض | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |
| `A$r` | اشر | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 8: Allegiance & the Object of Worship

_64 roots, 6,084 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Alh` | اله | 2,851 | 86 | 0.383 | high inter-cluster connectivity (131 clusters); appears in 80+ surahs |
| `qwm` | قوم | 660 | 79 | 0.688 | high inter-cluster connectivity (100 clusters) |
| `hdy` | هدي | 316 | 62 | 0.652 | high inter-cluster connectivity (66 clusters) |
| `Ebd` | عبد | 275 | 57 | 0.825 | high inter-cluster connectivity (68 clusters) |
| `wly` | ولي | 232 | 55 | 0.431 | high inter-cluster connectivity (63 clusters) |
| `dEw` | دعو | 212 | 55 | 0.788 | high inter-cluster connectivity (59 clusters) |
| `Dll` | ضلل | 191 | 56 | 0.738 | high inter-cluster connectivity (52 clusters) |
| `$rk` | شرك | 168 | 44 | 0.696 | high inter-cluster connectivity (45 clusters) |
| `nSr` | نصر | 158 | 46 | 0.418 | high inter-cluster connectivity (45 clusters) |
| `dwn` | دون | 144 | 46 | 0.757 | high inter-cluster connectivity (44 clusters) |
| `TwE` | طوع | 129 | 40 | 0.434 | high inter-cluster connectivity (40 clusters) |
| `lys` | ليس | 89 | 33 | 0.539 | verb-only; high inter-cluster connectivity (41 clusters) |
| `wkl` | وكل | 70 | 29 | 0.629 | high inter-cluster connectivity (27 clusters) |
| `Zhr` | ظهر | 59 | 30 | 0.559 | high inter-cluster connectivity (44 clusters) |
| `ndw` | ندو | 53 | 26 | 0.849 | high inter-cluster connectivity (24 clusters) |
| `SrT` | صرط | 45 | 25 | 0.733 | noun-only; high inter-cluster connectivity (18 clusters) |
| `jwb` | جوب | 43 | 23 | 0.767 | high inter-cluster connectivity (16 clusters) |
| `kfy` | كفي | 33 | 15 | 0.424 | high inter-cluster connectivity (15 clusters) |
| `Ejz` | عجز | 26 | 21 | 0.769 | high inter-cluster connectivity (13 clusters) |
| `mny` | مني | 21 | 10 | 0.286 | high inter-cluster connectivity (13 clusters) |
| `k$f` | كشف | 20 | 14 | 1.0 | high Meccan concentration; high inter-cluster connectivity (16 clusters) |
| `mll` | ملل | 18 | 11 | 0.5 | high inter-cluster connectivity (11 clusters) |
| `nwb` | نوب | 18 | 11 | 0.889 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `zEm` | زعم | 17 | 10 | 0.824 | high inter-cluster connectivity (10 clusters) |
| `Hrv` | حرث | 14 | 7 | 0.571 | bridge (9 clusters) |
| `ESm` | عصم | 13 | 10 | 0.385 | high inter-cluster connectivity (10 clusters) |
| `Hlf` | حلف | 13 | 5 | 0.077 | high Medinan concentration; bridge (8 clusters) |
| `Hnf` | حنف | 12 | 9 | 0.5 | noun-only; bridge (5 clusters) |
| `jby` | جبي | 12 | 12 | 0.833 | high inter-cluster connectivity (10 clusters) |
| `$qw` | شقو | 12 | 7 | 1.0 | high Meccan concentration |
| `sfh` | سفه | 11 | 5 | 0.455 | bridge (7 clusters) |
| `fAy` | فاي | 11 | 6 | 0.182 | noun-only; bridge (8 clusters) |
| `Trq` | طرق | 11 | 6 | 0.818 | noun-only |
| `wrd` | ورد | 11 | 7 | 0.909 | high Meccan concentration |
| `nkv` | نكث | 7 | 5 | 0.429 | bridge (5 clusters) |
| `myl` | ميل | 6 | 1 | 0.0 | high Medinan concentration; confined to 1 surah |
| `lHd` | لحد | 6 | 6 | 0.833 |  |
| `zwr` | زور | 6 | 5 | 0.667 |  |
| `Ent` | عنت | 5 | 5 | 0.0 | rare (5 occ.); high Medinan concentration; bridge (6 clusters) |
| `nq*` | نقذ | 5 | 4 | 0.6 | verb-only; rare (5 occ.) |
| `Trd` | طرد | 5 | 3 | 1.0 | rare (5 occ.); high Meccan concentration |
| `Srx` | صرخ | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |
| `bwr` | بور | 5 | 4 | 0.8 | rare (5 occ.) |
| `SdE` | صدع | 5 | 5 | 0.8 | rare (5 occ.) |
| `vbr` | ثبر | 5 | 3 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `qnTr` | قنطر | 4 | 2 | 0.0 | rare (4 occ.) |
| `Amd` | امد | 4 | 4 | 0.5 | noun-only; rare (4 occ.) |
| `rkn` | ركن | 4 | 3 | 1.0 | rare (4 occ.) |
| `tbb` | تبب | 4 | 3 | 1.0 | rare (4 occ.) |
| `smr` | سمر | 4 | 2 | 1.0 | rare (4 occ.) |
| `ljj` | لجج | 4 | 4 | 0.75 | rare (4 occ.) |
| `ASr` | اصر | 3 | 3 | 0.333 | noun-only; rare (3 occ.) |
| `qrH` | قرح | 3 | 1 | 0.0 | noun-only; rare (3 occ.); confined to 1 surah |
| `Anf` | انف | 3 | 2 | 0.0 | noun-only; rare (3 occ.) |
| `ljA` | لجا | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |
| `zjw` | زجو | 3 | 3 | 0.667 | rare (3 occ.) |
| `wvn` | وثن | 3 | 2 | 0.667 | noun-only; rare (3 occ.) |
| `$fw` | شفو | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |
| `Hw*` | حوذ | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |
| `hmn` | همن | 2 | 2 | 0.0 | rare (2 occ.) |
| `vxn` | ثخن | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |
| `Hw$` | حوش | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `Err` | عرر | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |
| `$TA` | شطا | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 0: The Believers' Reward

_62 roots, 3,845 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Amn` | امن | 879 | 77 | 0.431 | high inter-cluster connectivity (110 clusters) |
| `Eml` | عمل | 360 | 68 | 0.611 | high inter-cluster connectivity (77 clusters) |
| `jnn` | جنن | 201 | 70 | 0.682 | high inter-cluster connectivity (59 clusters) |
| `End` | عند | 201 | 62 | 0.542 | high inter-cluster connectivity (66 clusters) |
| `nwr` | نور | 194 | 62 | 0.5 | high inter-cluster connectivity (63 clusters) |
| `Hsn` | حسن | 194 | 50 | 0.624 | high inter-cluster connectivity (68 clusters) |
| `SlH` | صلح | 180 | 54 | 0.628 | high inter-cluster connectivity (46 clusters) |
| `swA` | سوا | 167 | 45 | 0.665 | high inter-cluster connectivity (56 clusters) |
| `EZm` | عظم | 128 | 50 | 0.469 | high inter-cluster connectivity (48 clusters) |
| `dxl` | دخل | 126 | 45 | 0.484 | high inter-cluster connectivity (46 clusters) |
| `jzy` | جزي | 118 | 47 | 0.754 | high inter-cluster connectivity (42 clusters) |
| `nhr` | نهر | 113 | 51 | 0.575 | high inter-cluster connectivity (50 clusters) |
| `Ajr` | اجر | 108 | 39 | 0.556 | high inter-cluster connectivity (45 clusters) |
| `SHb` | صحب | 97 | 47 | 0.732 | high inter-cluster connectivity (38 clusters) |
| `xld` | خلد | 87 | 40 | 0.494 | high inter-cluster connectivity (35 clusters) |
| `rDw` | رضو | 73 | 32 | 0.288 | high inter-cluster connectivity (40 clusters) |
| `jry` | جري | 64 | 43 | 0.484 | high inter-cluster connectivity (33 clusters) |
| `DEf` | ضعف | 52 | 21 | 0.481 | high inter-cluster connectivity (32 clusters) |
| `tHt` | تحت | 51 | 30 | 0.392 | high inter-cluster connectivity (29 clusters) |
| `Thr` | طهر | 31 | 18 | 0.226 | high inter-cluster connectivity (27 clusters) |
| `wdd` | ودد | 29 | 18 | 0.345 | high inter-cluster connectivity (24 clusters) |
| `fwz` | فوز | 29 | 21 | 0.345 | high inter-cluster connectivity (14 clusters) |
| `Abd` | ابد | 28 | 15 | 0.179 | high inter-cluster connectivity (14 clusters) |
| `vwb` | ثوب | 28 | 15 | 0.357 | high inter-cluster connectivity (19 clusters) |
| `xzy` | خزي | 26 | 15 | 0.538 | high inter-cluster connectivity (15 clusters) |
| `Hdd` | حدد | 25 | 12 | 0.16 | high inter-cluster connectivity (12 clusters) |
| `whb` | وهب | 25 | 12 | 0.84 | high inter-cluster connectivity (10 clusters) |
| `ldn` | لدن | 18 | 10 | 0.667 | bridge (8 clusters) |
| `Awb` | اوب | 17 | 8 | 0.824 | high inter-cluster connectivity (11 clusters) |
| `HbT` | حبط | 16 | 12 | 0.312 | verb-only; high inter-cluster connectivity (12 clusters) |
| `vwy` | ثوي | 14 | 10 | 0.786 | noun-only; high inter-cluster connectivity (10 clusters) |
| `ETw` | عطو | 14 | 11 | 0.786 | bridge (5 clusters) |
| `qrD` | قرض | 13 | 6 | 0.231 | bridge (7 clusters) |
| `DyE` | ضيع | 10 | 8 | 0.6 | verb-only; bridge (9 clusters) |
| `dfE` | دفع | 10 | 8 | 0.4 | bridge (5 clusters) |
| `zlf` | زلف | 10 | 8 | 1.0 | high Meccan concentration |
| `dwm` | دوم | 9 | 6 | 0.444 | bridge (7 clusters) |
| `bEl` | بعل | 7 | 5 | 0.286 | bridge (6 clusters) |
| `grf` | غرف | 7 | 5 | 0.714 |  |
| `Emd` | عمد | 7 | 7 | 0.429 | bridge (9 clusters) |
| `zlzl` | زلزل | 6 | 4 | 0.0 | high Medinan concentration |
| `Hmy` | حمي | 6 | 5 | 0.333 | bridge (5 clusters) |
| `tbr` | تبر | 6 | 4 | 1.0 | high Meccan concentration |
| `xdE` | خدع | 5 | 3 | 0.0 | rare (5 occ.); high Medinan concentration |
| `qrf` | قرف | 5 | 3 | 0.8 | rare (5 occ.) |
| `qTr` | قطر | 5 | 5 | 0.6 | noun-only; rare (5 occ.) |
| `sxT` | سخط | 4 | 4 | 0.0 | rare (4 occ.) |
| `smm` | سمم | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |
| `nfl` | نفل | 4 | 3 | 0.5 | noun-only; rare (4 occ.) |
| `bwl` | بول | 4 | 3 | 0.5 | noun-only; rare (4 occ.) |
| `syl` | سيل | 4 | 2 | 0.5 | rare (4 occ.) |
| `Ezr` | عزر | 3 | 3 | 0.333 | verb-only; rare (3 occ.) |
| `ZmA` | ظما | 3 | 3 | 0.333 | rare (3 occ.) |
| `xbt` | خبت | 3 | 2 | 0.333 | rare (3 occ.) |
| `$Am` | شام | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |
| `mHS` | محص | 2 | 1 | 0.0 | verb-only; rare (2 occ.); confined to 1 surah |
| `Sgw` | صغو | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `klw` | كلو | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `zlq` | زلق | 2 | 2 | 1.0 | rare (2 occ.) |
| `rss` | رسس | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `rwD` | روض | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `mHn` | محن | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |

### Cluster 5: The Commanded Self

_40 roots, 2,005 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nfs` | نفس | 298 | 63 | 0.547 | high inter-cluster connectivity (82 clusters) |
| `wqy` | وقي | 258 | 63 | 0.45 | high inter-cluster connectivity (60 clusters) |
| `Amr` | امر | 248 | 61 | 0.617 | high inter-cluster connectivity (76 clusters) |
| `xyr` | خير | 196 | 55 | 0.526 | high inter-cluster connectivity (64 clusters) |
| `bny` | بني | 184 | 53 | 0.549 | high inter-cluster connectivity (65 clusters) |
| `fEl` | فعل | 108 | 44 | 0.583 | high inter-cluster connectivity (41 clusters) |
| `Sbr` | صبر | 103 | 45 | 0.689 | high inter-cluster connectivity (44 clusters) |
| `Erf` | عرف | 70 | 26 | 0.286 | high inter-cluster connectivity (35 clusters) |
| `nsw` | نسو | 59 | 16 | 0.153 | noun-only; high inter-cluster connectivity (39 clusters) |
| `nhy` | نهي | 56 | 26 | 0.5 | high inter-cluster connectivity (28 clusters) |
| `flH` | فلح | 40 | 24 | 0.575 | high inter-cluster connectivity (25 clusters) |
| `blw` | بلو | 38 | 25 | 0.553 | high inter-cluster connectivity (24 clusters) |
| `nkr` | نكر | 37 | 26 | 0.622 | high inter-cluster connectivity (15 clusters) |
| `jnH` | جنح | 34 | 14 | 0.206 | high inter-cluster connectivity (35 clusters) |
| `msk` | مسك | 27 | 17 | 0.63 | high inter-cluster connectivity (21 clusters) |
| `wEZ` | وعظ | 25 | 14 | 0.44 | high inter-cluster connectivity (18 clusters) |
| `fH$` | فحش | 24 | 15 | 0.542 | noun-only; high inter-cluster connectivity (19 clusters) |
| `Tlq` | طلق | 23 | 10 | 0.348 | high inter-cluster connectivity (16 clusters) |
| `frD` | فرض | 18 | 7 | 0.056 | high Medinan concentration; high inter-cluster connectivity (13 clusters) |
| `vbt` | ثبت | 18 | 11 | 0.444 | high inter-cluster connectivity (15 clusters) |
| `Sfw` | صفو | 17 | 12 | 0.471 | bridge (9 clusters) |
| `swm` | سوم | 15 | 10 | 0.533 | high inter-cluster connectivity (12 clusters) |
| `$hw` | شهو | 13 | 13 | 0.846 | bridge (9 clusters) |
| `Ewn` | عون | 11 | 8 | 0.545 | bridge (6 clusters) |
| `jml` | جمل | 11 | 9 | 0.818 | bridge (5 clusters) |
| `*bH` | ذبح | 9 | 6 | 0.556 | high inter-cluster connectivity (10 clusters) |
| `Ezm` | عزم | 9 | 7 | 0.444 | bridge (6 clusters) |
| `rgb` | رغب | 8 | 7 | 0.5 |  |
| `srH` | سرح | 7 | 3 | 0.143 | high Medinan concentration; bridge (7 clusters) |
| `frg` | فرغ | 6 | 6 | 0.667 |  |
| `qSd` | قصد | 6 | 5 | 0.667 |  |
| `$HH` | شحح | 5 | 4 | 0.0 | rare (5 occ.); high Medinan concentration; bridge (6 clusters) |
| `HyD` | حيض | 4 | 2 | 0.0 | rare (4 occ.) |
| `swl` | سول | 4 | 3 | 0.75 | verb-only; rare (4 occ.) |
| `xfD` | خفض | 4 | 4 | 1.0 | rare (4 occ.) |
| `Erw` | عرو | 3 | 3 | 0.667 | rare (3 occ.) |
| `Ass` | اسس | 3 | 1 | 0.0 | verb-only; rare (3 occ.); confined to 1 surah |
| `rfv` | رفث | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `EDl` | عضل | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |
| `bxE` | بخع | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 19: Household Law & Lineage

_40 roots, 1,636 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*kr` | ذكر | 292 | 71 | 0.74 | high inter-cluster connectivity (74 clusters) |
| `mvl` | مثل | 169 | 50 | 0.609 | high inter-cluster connectivity (57 clusters) |
| `wld` | ولد | 102 | 39 | 0.539 | high inter-cluster connectivity (42 clusters) |
| `dyn` | دين | 101 | 40 | 0.485 | high inter-cluster connectivity (35 clusters) |
| `qrb` | قرب | 96 | 41 | 0.521 | high inter-cluster connectivity (49 clusters) |
| `Axw` | اخو | 96 | 31 | 0.604 | noun-only; high inter-cluster connectivity (45 clusters) |
| `zwj` | زوج | 81 | 43 | 0.519 | high inter-cluster connectivity (49 clusters) |
| `rjl` | رجل | 73 | 32 | 0.603 | noun-only; high inter-cluster connectivity (41 clusters) |
| `wHd` | وحد | 68 | 35 | 0.721 | high inter-cluster connectivity (32 clusters) |
| `Drb` | ضرب | 58 | 28 | 0.517 | high inter-cluster connectivity (44 clusters) |
| `trk` | ترك | 43 | 20 | 0.558 | high inter-cluster connectivity (25 clusters) |
| `mrA` | مرا | 38 | 22 | 0.632 | high inter-cluster connectivity (23 clusters) |
| `wrv` | ورث | 35 | 20 | 0.771 | high inter-cluster connectivity (16 clusters) |
| `wSy` | وصي | 32 | 13 | 0.5 | high inter-cluster connectivity (15 clusters) |
| `vlv` | ثلث | 32 | 20 | 0.438 | high inter-cluster connectivity (29 clusters) |
| `Anv` | انث | 30 | 17 | 0.633 | noun-only; high inter-cluster connectivity (16 clusters) |
| `vny` | ثني | 29 | 18 | 0.621 | high inter-cluster connectivity (30 clusters) |
| `Edl` | عدل | 28 | 11 | 0.464 | high inter-cluster connectivity (21 clusters) |
| `E$r` | عشر | 27 | 19 | 0.556 | high inter-cluster connectivity (27 clusters) |
| `HDr` | حضر | 25 | 16 | 0.64 | high inter-cluster connectivity (13 clusters) |
| `qsT` | قسط | 25 | 15 | 0.36 | high inter-cluster connectivity (21 clusters) |
| `ytm` | يتم | 23 | 12 | 0.348 | high inter-cluster connectivity (19 clusters) |
| `rbE` | ربع | 22 | 11 | 0.227 | high inter-cluster connectivity (20 clusters) |
| `$hr` | شهر | 21 | 9 | 0.19 | noun-only; high inter-cluster connectivity (23 clusters) |
| `rbS` | ربص | 17 | 7 | 0.353 | bridge (8 clusters) |
| `xms` | خمس | 8 | 7 | 0.375 | noun-only; bridge (5 clusters) |
| `gbr` | غبر | 8 | 7 | 1.0 | noun-only; high Meccan concentration; bridge (5 clusters) |
| `nSf` | نصف | 7 | 3 | 0.286 | high inter-cluster connectivity (10 clusters) |
| `HZZ` | حظظ | 7 | 5 | 0.286 | noun-only; high inter-cluster connectivity (10 clusters) |
| `rdy` | ردي | 6 | 6 | 0.833 |  |
| `zjr` | زجر | 6 | 3 | 1.0 | high Meccan concentration |
| `sds` | سدس | 5 | 3 | 0.2 | noun-only; rare (5 occ.); bridge (5 clusters) |
| `frd` | فرد | 5 | 4 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `fwr` | فور | 4 | 4 | 0.75 | rare (4 occ.) |
| `qld` | قلد | 4 | 3 | 0.5 | noun-only; rare (4 occ.); bridge (7 clusters) |
| `jhz` | جهز | 4 | 1 | 1.0 | rare (4 occ.); confined to 1 surah |
| `Aff` | افف | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `TEn` | طعن | 2 | 2 | 0.0 | rare (2 occ.) |
| `mlq` | ملق | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `khn` | كهن | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 90: Sin–Mercy Economy

_24 roots, 1,469 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rHm` | رحم | 339 | 62 | 0.667 | high inter-cluster connectivity (72 clusters) |
| `gfr` | غفر | 234 | 56 | 0.423 | high inter-cluster connectivity (60 clusters) |
| `mwt` | موت | 165 | 53 | 0.6 | high inter-cluster connectivity (50 clusters) |
| `gyr` | غير | 154 | 46 | 0.61 | high inter-cluster connectivity (68 clusters) |
| `Edw` | عدو | 106 | 34 | 0.443 | high inter-cluster connectivity (61 clusters) |
| `twb` | توب | 87 | 25 | 0.264 | high inter-cluster connectivity (33 clusters) |
| `Drr` | ضرر | 74 | 31 | 0.581 | high inter-cluster connectivity (38 clusters) |
| `fsq` | فسق | 54 | 23 | 0.37 | high inter-cluster connectivity (29 clusters) |
| `nfE` | نفع | 50 | 31 | 0.64 | high inter-cluster connectivity (30 clusters) |
| `Avm` | اثم | 48 | 21 | 0.271 | high inter-cluster connectivity (30 clusters) |
| `qsm` | قسم | 33 | 24 | 0.788 | high inter-cluster connectivity (14 clusters) |
| `ESy` | عصي | 32 | 23 | 0.562 | high inter-cluster connectivity (27 clusters) |
| `Esy` | عسي | 30 | 16 | 0.5 | verb-only; high inter-cluster connectivity (19 clusters) |
| `lHm` | لحم | 12 | 10 | 0.583 | noun-only; high inter-cluster connectivity (14 clusters) |
| `dmw` | دمو | 10 | 7 | 0.5 | noun-only; bridge (8 clusters) |
| `bht` | بهت | 8 | 6 | 0.125 | high Medinan concentration; bridge (8 clusters) |
| `qnT` | قنط | 6 | 5 | 1.0 | high Meccan concentration |
| `HrS` | حرص | 5 | 5 | 0.4 | rare (5 occ.) |
| `xnzr` | خنزر | 5 | 4 | 0.4 | noun-only; rare (5 occ.); bridge (5 clusters) |
| `hll` | هلل | 5 | 4 | 0.4 | rare (5 occ.); bridge (5 clusters) |
| `ksw` | كسو | 5 | 4 | 0.2 | rare (5 occ.); bridge (9 clusters) |
| `syH` | سيح | 3 | 2 | 0.0 | rare (3 occ.) |
| `sfk` | سفك | 2 | 1 | 0.0 | verb-only; rare (2 occ.); confined to 1 surah |
| `jnf` | جنف | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 43: Divine Will & Dominion

_13 roots, 1,439 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$yA` | شيا | 519 | 73 | 0.601 | high inter-cluster connectivity (102 clusters) |
| `kll` | كلل | 377 | 74 | 0.642 | high inter-cluster connectivity (94 clusters) |
| `mlk` | ملك | 206 | 63 | 0.592 | high inter-cluster connectivity (71 clusters) |
| `qdr` | قدر | 132 | 58 | 0.652 | high inter-cluster connectivity (49 clusters) |
| `rzq` | رزق | 123 | 44 | 0.65 | high inter-cluster connectivity (48 clusters) |
| `HwT` | حوط | 28 | 18 | 0.643 | high inter-cluster connectivity (18 clusters) |
| `bsT` | بسط | 25 | 15 | 0.64 | high inter-cluster connectivity (18 clusters) |
| `xTf` | خطف | 7 | 6 | 0.571 | bridge (6 clusters) |
| `fr$` | فرش | 6 | 6 | 0.667 |  |
| `fwj` | فوج | 5 | 5 | 0.8 | noun-only; rare (5 occ.) |
| `dxr` | دخر | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |
| `mzq` | مزق | 4 | 1 | 1.0 | rare (4 occ.); confined to 1 surah |
| `mHw` | محو | 3 | 3 | 0.667 | verb-only; rare (3 occ.) |

### Cluster 62: The Prepared Fire

_16 roots, 1,166 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kfr` | كفر | 525 | 77 | 0.444 | high inter-cluster connectivity (98 clusters) |
| `E*b` | عذب | 373 | 68 | 0.622 | high inter-cluster connectivity (88 clusters) |
| `Alm` | الم | 75 | 42 | 0.48 | high inter-cluster connectivity (38 clusters) |
| `*wq` | ذوق | 63 | 32 | 0.762 | high inter-cluster connectivity (28 clusters) |
| `hwn` | هون | 26 | 19 | 0.538 | high inter-cluster connectivity (23 clusters) |
| `sEr` | سعر | 19 | 15 | 0.684 | bridge (8 clusters) |
| `Etd` | عتد | 16 | 10 | 0.562 | bridge (7 clusters) |
| `fdy` | فدي | 13 | 10 | 0.308 | high inter-cluster connectivity (17 clusters) |
| `jwr` | جور | 13 | 10 | 0.462 | bridge (8 clusters) |
| `E*r` | عذر | 12 | 8 | 0.583 | bridge (7 clusters) |
| `Hrq` | حرق | 9 | 8 | 0.444 | bridge (6 clusters) |
| `wbl` | وبل | 8 | 6 | 0.125 | high Medinan concentration; bridge (8 clusters) |
| `mhl` | مهل | 6 | 5 | 1.0 | high Meccan concentration |
| `kbt` | كبت | 3 | 2 | 0.0 | verb-only; rare (3 occ.) |
| `hTE` | هطع | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `mHq` | محق | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |

### Cluster 17: Bodily Purity & Prayer

_33 roots, 896 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ydy` | يدي | 120 | 47 | 0.492 | noun-only; high inter-cluster connectivity (56 clusters) |
| `wjd` | وجد | 107 | 32 | 0.551 | high inter-cluster connectivity (51 clusters) |
| `Slw` | صلو | 99 | 37 | 0.404 | high inter-cluster connectivity (41 clusters) |
| `AHd` | احد | 85 | 33 | 0.553 | noun-only; high inter-cluster connectivity (42 clusters) |
| `wjh` | وجه | 78 | 38 | 0.564 | high inter-cluster connectivity (41 clusters) |
| `mwh` | موه | 63 | 41 | 0.762 | noun-only; high inter-cluster connectivity (38 clusters) |
| `zkw` | زكو | 59 | 29 | 0.424 | high inter-cluster connectivity (29 clusters) |
| `Tyb` | طيب | 50 | 23 | 0.42 | high inter-cluster connectivity (29 clusters) |
| `qdm` | قدم | 48 | 37 | 0.604 | high inter-cluster connectivity (22 clusters) |
| `jnb` | جنب | 33 | 21 | 0.606 | high inter-cluster connectivity (20 clusters) |
| `mrD` | مرض | 24 | 13 | 0.125 | high Medinan concentration; high inter-cluster connectivity (23 clusters) |
| `xbv` | خبث | 16 | 9 | 0.312 | bridge (7 clusters) |
| `Hrj` | حرج | 15 | 9 | 0.133 | high Medinan concentration; high inter-cluster connectivity (16 clusters) |
| `sfr` | سفر | 12 | 9 | 0.417 | high inter-cluster connectivity (11 clusters) |
| `ymm` | يمم | 11 | 7 | 0.727 | high inter-cluster connectivity (10 clusters) |
| `rjs` | رجس | 10 | 7 | 0.4 | noun-only; high inter-cluster connectivity (10 clusters) |
| `SEd` | صعد | 9 | 8 | 0.667 | bridge (9 clusters) |
| `nkl` | نكل | 5 | 5 | 0.4 | noun-only; rare (5 occ.) |
| `ESr` | عصر | 5 | 4 | 0.8 | rare (5 occ.) |
| `lms` | لمس | 5 | 5 | 0.4 | verb-only; rare (5 occ.); bridge (5 clusters) |
| `rfq` | رفق | 5 | 3 | 0.6 | noun-only; rare (5 occ.); bridge (5 clusters) |
| `$hb` | شهب | 5 | 4 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `myz` | ميز | 4 | 4 | 0.5 | verb-only; rare (4 occ.) |
| `gsl` | غسل | 4 | 4 | 0.5 | rare (4 occ.); bridge (6 clusters) |
| `msH` | مسح | 4 | 3 | 0.25 | rare (4 occ.); bridge (5 clusters) |
| `mhn` | مهن | 4 | 4 | 1.0 | rare (4 occ.) |
| `ftl` | فتل | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |
| `nDr` | نضر | 3 | 3 | 0.667 | noun-only; rare (3 occ.) |
| `gwT` | غوط | 2 | 2 | 0.0 | noun-only; rare (2 occ.); bridge (5 clusters) |
| `rks` | ركس | 2 | 1 | 0.0 | verb-only; rare (2 occ.); confined to 1 surah |
| `ksl` | كسل | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |
| `gdr` | غدر | 2 | 1 | 1.0 | verb-only; rare (2 occ.); confined to 1 surah |
| `kbb` | كبب | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 96: Dunya vs. Ākhirah

_19 roots, 856 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Axr` | اخر | 250 | 64 | 0.612 | high inter-cluster connectivity (68 clusters) |
| `Hyy` | حيي | 184 | 50 | 0.663 | high inter-cluster connectivity (54 clusters) |
| `dnw` | دنو | 133 | 46 | 0.541 | high inter-cluster connectivity (57 clusters) |
| `mtE` | متع | 70 | 38 | 0.614 | high inter-cluster connectivity (37 clusters) |
| `zyn` | زين | 46 | 28 | 0.696 | high inter-cluster connectivity (29 clusters) |
| `w*r` | وذر | 45 | 29 | 0.8 | verb-only; high inter-cluster connectivity (23 clusters) |
| `grr` | غرر | 27 | 14 | 0.63 | high inter-cluster connectivity (18 clusters) |
| `bqy` | بقي | 21 | 16 | 0.857 | high Meccan concentration; bridge (8 clusters) |
| `lEb` | لعب | 20 | 13 | 0.75 | high inter-cluster connectivity (15 clusters) |
| `lhw` | لهو | 16 | 13 | 0.625 | high inter-cluster connectivity (14 clusters) |
| `xwD` | خوض | 12 | 7 | 0.667 | bridge (8 clusters) |
| `brj` | برج | 7 | 6 | 0.429 |  |
| `nwq` | نوق | 7 | 6 | 1.0 | noun-only; high Meccan concentration; bridge (9 clusters) |
| `xlT` | خلط | 6 | 6 | 0.667 | high inter-cluster connectivity (11 clusters) |
| `zxrf` | زخرف | 4 | 4 | 1.0 | noun-only; rare (4 occ.); bridge (5 clusters) |
| `zHzH` | زحزح | 2 | 2 | 0.0 | rare (2 occ.) |
| `rsx` | رسخ | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |
| `Hbs` | حبس | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |
| `qTf` | قطف | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 66: Jihād fī Sabīl Allāh

_17 roots, 765 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sbl` | سبل | 176 | 47 | 0.426 | noun-only; high inter-cluster connectivity (68 clusters) |
| `qtl` | قتل | 170 | 33 | 0.218 | high inter-cluster connectivity (64 clusters) |
| `nfq` | نفق | 111 | 31 | 0.117 | high Medinan concentration; high inter-cluster connectivity (50 clusters) |
| `mwl` | مول | 86 | 38 | 0.372 | noun-only; high inter-cluster connectivity (43 clusters) |
| `Sdd` | صدد | 42 | 23 | 0.452 | high inter-cluster connectivity (25 clusters) |
| `jhd` | جهد | 41 | 19 | 0.268 | high inter-cluster connectivity (23 clusters) |
| `qEd` | قعد | 31 | 15 | 0.387 | high inter-cluster connectivity (18 clusters) |
| `hjr` | هجر | 31 | 17 | 0.29 | high inter-cluster connectivity (21 clusters) |
| `A*y` | اذي | 24 | 10 | 0.167 | high inter-cluster connectivity (17 clusters) |
| `nfr` | نفر | 18 | 10 | 0.556 | high inter-cluster connectivity (13 clusters) |
| `Ewj` | عوج | 9 | 7 | 0.889 | noun-only; high Meccan concentration; bridge (7 clusters) |
| `HSr` | حصر | 6 | 5 | 0.167 | bridge (7 clusters) |
| `rSd` | رصد | 6 | 4 | 0.667 | bridge (5 clusters) |
| `drA` | درا | 5 | 5 | 0.2 | verb-only; rare (5 occ.); bridge (6 clusters) |
| `DjE` | ضجع | 3 | 3 | 0.333 | noun-only; rare (3 occ.) |
| `HrD` | حرض | 3 | 3 | 0.333 | rare (3 occ.); bridge (5 clusters) |
| `fjj` | فجج | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 75: Witnessing the Visible Sign

_18 roots, 704 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rAy` | راي | 328 | 72 | 0.738 | high inter-cluster connectivity (102 clusters) |
| `xrj` | خرج | 182 | 56 | 0.56 | high inter-cluster connectivity (64 clusters) |
| `Swb` | صوب | 77 | 27 | 0.325 | high inter-cluster connectivity (34 clusters) |
| `kwd` | كود | 24 | 19 | 0.667 | verb-only; high inter-cluster connectivity (20 clusters) |
| `bld` | بلد | 19 | 15 | 0.895 | noun-only; high Meccan concentration; high inter-cluster connectivity (19 clusters) |
| `xll` | خلل | 13 | 11 | 0.692 | noun-only; high inter-cluster connectivity (13 clusters) |
| `TmE` | طمع | 12 | 10 | 0.667 | high inter-cluster connectivity (11 clusters) |
| `sHb` | سحب | 11 | 10 | 0.636 | high inter-cluster connectivity (16 clusters) |
| `brq` | برق | 6 | 5 | 0.333 | high inter-cluster connectivity (10 clusters) |
| `vwr` | ثور | 5 | 4 | 0.8 | verb-only; rare (5 occ.); bridge (5 clusters) |
| `fwt` | فوت | 5 | 5 | 0.4 | rare (5 occ.) |
| `kwkb` | كوكب | 5 | 5 | 0.8 | noun-only; rare (5 occ.) |
| `wqf` | وقف | 4 | 3 | 1.0 | rare (4 occ.) |
| `rkm` | ركم | 3 | 3 | 0.333 | rare (3 occ.) |
| `jdv` | جدث | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `Afq` | افق | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `wdq` | ودق | 2 | 2 | 0.5 | noun-only; rare (2 occ.); bridge (5 clusters) |
| `Dgn` | ضغن | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 7: Sea-Rescue / Bounty / Gratitude

_25 roots, 671 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fDl` | فضل | 104 | 32 | 0.404 | high inter-cluster connectivity (46 clusters) |
| `bgy` | بغي | 96 | 41 | 0.573 | high inter-cluster connectivity (46 clusters) |
| `njw` | نجو | 84 | 31 | 0.798 | high inter-cluster connectivity (32 clusters) |
| `$kr` | شكر | 75 | 35 | 0.733 | high inter-cluster connectivity (39 clusters) |
| `nsy` | نسي | 45 | 20 | 0.733 | high inter-cluster connectivity (26 clusters) |
| `bHr` | بحر | 42 | 25 | 0.81 | noun-only; high inter-cluster connectivity (23 clusters) |
| `brr` | برر | 32 | 18 | 0.562 | high inter-cluster connectivity (22 clusters) |
| `xlS` | خلص | 31 | 17 | 0.839 | high inter-cluster connectivity (16 clusters) |
| `flk` | فلك | 25 | 20 | 0.92 | noun-only; high Meccan concentration; high inter-cluster connectivity (22 clusters) |
| `lbs` | لبس | 23 | 13 | 0.783 | high inter-cluster connectivity (18 clusters) |
| `grq` | غرق | 23 | 18 | 0.913 | high Meccan concentration; high inter-cluster connectivity (12 clusters) |
| `SnE` | صنع | 20 | 14 | 0.8 | high inter-cluster connectivity (19 clusters) |
| `xTb` | خطب | 12 | 11 | 0.917 | high Meccan concentration; bridge (9 clusters) |
| `drk` | درك | 12 | 9 | 0.75 | bridge (8 clusters) |
| `Hly` | حلي | 9 | 8 | 0.667 | bridge (8 clusters) |
| `mwj` | موج | 7 | 5 | 0.714 | bridge (9 clusters) |
| `mrj` | مرج | 6 | 3 | 0.333 |  |
| `Hwt` | حوت | 5 | 4 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `xSS` | خصص | 4 | 4 | 0.0 | rare (4 occ.); bridge (6 clusters) |
| `krb` | كرب | 4 | 3 | 1.0 | noun-only; rare (4 occ.) |
| `$Hn` | شحن | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `sjr` | سجر | 3 | 3 | 1.0 | rare (3 occ.) |
| `wsl` | وسل | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |
| `Trw` | طرو | 2 | 2 | 1.0 | rare (2 occ.) |
| `mxr` | مخر | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 77: Creation & the Appointed Term

_13 roots, 545 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xlq` | خلق | 261 | 75 | 0.824 | high inter-cluster connectivity (59 clusters) |
| `blg` | بلغ | 77 | 36 | 0.636 | high inter-cluster connectivity (38 clusters) |
| `wfy` | وفي | 66 | 27 | 0.53 | high inter-cluster connectivity (37 clusters) |
| `Ajl` | اجل | 56 | 29 | 0.696 | high inter-cluster connectivity (29 clusters) |
| `trb` | ترب | 22 | 18 | 0.818 | high inter-cluster connectivity (12 clusters) |
| `xSm` | خصم | 18 | 12 | 0.722 | bridge (6 clusters) |
| `nSH` | نصح | 13 | 6 | 0.846 | bridge (7 clusters) |
| `nTf` | نطف | 12 | 11 | 0.833 | noun-only; high inter-cluster connectivity (10 clusters) |
| `Elq` | علق | 7 | 6 | 0.714 | noun-only; bridge (7 clusters) |
| `Tlb` | طلب | 4 | 3 | 0.5 | rare (4 occ.) |
| `Tfl` | طفل | 4 | 3 | 0.25 | noun-only; rare (4 occ.); bridge (6 clusters) |
| `mDg` | مضغ | 3 | 2 | 0.667 | noun-only; rare (3 occ.) |
| `Eyy` | عيي | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |

### Cluster 11: Vegetative Signs / Reflective Gaze

_17 roots, 306 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hbb` | حبب | 95 | 35 | 0.358 | high inter-cluster connectivity (43 clusters) |
| `nbt` | نبت | 26 | 21 | 0.769 | high inter-cluster connectivity (21 clusters) |
| `vmr` | ثمر | 24 | 12 | 0.708 | high inter-cluster connectivity (23 clusters) |
| `fjr` | فجر | 24 | 16 | 0.75 | high inter-cluster connectivity (17 clusters) |
| `nxl` | نخل | 20 | 16 | 0.8 | noun-only; high inter-cluster connectivity (16 clusters) |
| `fkh` | فكه | 19 | 12 | 0.842 | bridge (7 clusters) |
| `fkr` | فكر | 18 | 13 | 0.722 | verb-only; high inter-cluster connectivity (14 clusters) |
| `xwn` | خون | 16 | 8 | 0.188 | bridge (7 clusters) |
| `zrE` | زرع | 14 | 12 | 0.786 | high inter-cluster connectivity (13 clusters) |
| `$bh` | شبه | 12 | 6 | 0.417 | bridge (9 clusters) |
| `Enb` | عنب | 11 | 10 | 0.818 | noun-only; high inter-cluster connectivity (10 clusters) |
| `zyt` | زيت | 7 | 5 | 0.714 | noun-only; bridge (7 clusters) |
| `HSd` | حصد | 6 | 6 | 1.0 | high Meccan concentration; bridge (8 clusters) |
| `ESb` | عصب | 5 | 4 | 0.8 | rare (5 occ.) |
| `rmn` | رمن | 3 | 2 | 0.667 | noun-only; rare (3 occ.) |
| `j*E` | جذع | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |
| `bhj` | بهج | 3 | 3 | 0.667 | rare (3 occ.); bridge (7 clusters) |

### Unnamed clusters (by size)

### Cluster 78: (unnamed)

_13 roots, 652 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ywm` | يوم | 405 | 75 | 0.723 | high inter-cluster connectivity (86 clusters) |
| `Edd` | عدد | 57 | 26 | 0.368 | high inter-cluster connectivity (28 clusters) |
| `mrr` | مرر | 35 | 22 | 0.686 | high inter-cluster connectivity (21 clusters) |
| `glb` | غلب | 31 | 18 | 0.581 | high inter-cluster connectivity (17 clusters) |
| `lbv` | لبث | 31 | 17 | 0.871 | high Meccan concentration; high inter-cluster connectivity (16 clusters) |
| `Alf` | الف | 22 | 12 | 0.318 | high inter-cluster connectivity (14 clusters) |
| `snw` | سنو | 20 | 17 | 0.8 | high inter-cluster connectivity (18 clusters) |
| `HSy` | حصي | 11 | 10 | 0.818 | bridge (9 clusters) |
| `mAy` | ماي | 10 | 5 | 0.2 | noun-only; bridge (7 clusters) |
| `Ewm` | عوم | 9 | 5 | 0.333 | noun-only; bridge (5 clusters) |
| `Erj` | عرج | 9 | 8 | 0.667 | high inter-cluster connectivity (13 clusters) |
| `DHw` | ضحو | 7 | 5 | 1.0 | high Meccan concentration |
| `Etb` | عتب | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |

### Cluster 46: (unnamed)

_12 roots, 201 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Akl` | اكل | 109 | 40 | 0.606 | high inter-cluster connectivity (56 clusters) |
| `sbE` | سبع | 28 | 16 | 0.786 | high inter-cluster connectivity (18 clusters) |
| `fty` | فتي | 21 | 7 | 0.714 | high inter-cluster connectivity (18 clusters) |
| `bqr` | بقر | 9 | 3 | 0.444 | noun-only; bridge (6 clusters) |
| `xDr` | خضر | 8 | 7 | 0.625 | high inter-cluster connectivity (10 clusters) |
| `snbl` | سنبل | 5 | 2 | 0.6 | noun-only; rare (5 occ.) |
| `sHt` | سحت | 4 | 2 | 0.25 | rare (4 occ.); bridge (5 clusters) |
| `ybs` | يبس | 4 | 3 | 1.0 | rare (4 occ.) |
| `smn` | سمن | 4 | 3 | 1.0 | rare (4 occ.) |
| `Tbq` | طبق | 4 | 3 | 1.0 | rare (4 occ.) |
| `*Ab` | ذاب | 3 | 1 | 1.0 | noun-only; rare (3 occ.); confined to 1 surah |
| `Ejf` | عجف | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 59: (unnamed)

_12 roots, 274 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kbr` | كبر | 161 | 57 | 0.764 | high inter-cluster connectivity (54 clusters) |
| `*rr` | ذرر | 38 | 21 | 0.658 | noun-only; high inter-cluster connectivity (22 clusters) |
| `vql` | ثقل | 28 | 19 | 0.679 | high inter-cluster connectivity (16 clusters) |
| `Sgr` | صغر | 13 | 11 | 0.769 | high inter-cluster connectivity (12 clusters) |
| `Srr` | صرر | 6 | 5 | 0.667 | bridge (5 clusters) |
| `mqt` | مقت | 6 | 4 | 0.667 | noun-only |
| `grm` | غرم | 6 | 5 | 0.667 | noun-only |
| `fzE` | فزع | 6 | 4 | 1.0 | high Meccan concentration |
| `sAm` | سام | 3 | 2 | 0.667 | verb-only; rare (3 occ.) |
| `nkf` | نكف | 3 | 1 | 0.0 | verb-only; rare (3 occ.); confined to 1 surah |
| `Ezb` | عزب | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |
| `xrdl` | خردل | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 191: (unnamed)

_12 roots, 431 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `smE` | سمع | 185 | 57 | 0.622 | high inter-cluster connectivity (54 clusters) |
| `bSr` | بصر | 148 | 62 | 0.736 | high inter-cluster connectivity (56 clusters) |
| `n$A` | نشا | 28 | 14 | 0.929 | high Meccan concentration; high inter-cluster connectivity (17 clusters) |
| `fAd` | فاد | 16 | 13 | 1.0 | noun-only; high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `jld` | جلد | 13 | 6 | 0.462 | bridge (7 clusters) |
| `lgw` | لغو | 11 | 11 | 0.818 | bridge (8 clusters) |
| `qbD` | قبض | 9 | 6 | 0.667 |  |
| `xtm` | ختم | 8 | 7 | 0.75 | bridge (9 clusters) |
| `Hss` | حسس | 6 | 4 | 0.667 |  |
| `zfr` | زفر | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `nSt` | نصت | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |
| `lmH` | لمح | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 209: (unnamed)

_12 roots, 182 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `brA` | برا | 31 | 20 | 0.355 | high inter-cluster connectivity (17 clusters) |
| `Tyr` | طير | 29 | 19 | 0.724 | high inter-cluster connectivity (26 clusters) |
| `wqE` | وقع | 24 | 16 | 0.875 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `nfx` | نفخ | 20 | 17 | 0.85 | high Meccan concentration; high inter-cluster connectivity (16 clusters) |
| `r$d` | رشد | 19 | 9 | 0.789 | high inter-cluster connectivity (13 clusters) |
| `Swr` | صور | 19 | 17 | 0.737 | bridge (9 clusters) |
| `Sff` | صفف | 14 | 11 | 0.786 | bridge (9 clusters) |
| `Tyn` | طين | 12 | 11 | 0.833 | noun-only; high inter-cluster connectivity (11 clusters) |
| `khf` | كهف | 6 | 1 | 1.0 | noun-only; high Meccan concentration; bridge (7 clusters); confined to 1 surah |
| `hyA` | هيا | 4 | 3 | 0.5 | rare (4 occ.); bridge (8 clusters) |
| `kmh` | كمه | 2 | 2 | 0.0 | noun-only; rare (2 occ.); bridge (7 clusters) |
| `brS` | برص | 2 | 2 | 0.0 | noun-only; rare (2 occ.); bridge (7 clusters) |

### Cluster 34: (unnamed)

_11 roots, 434 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nEm` | نعم | 140 | 61 | 0.643 | high inter-cluster connectivity (50 clusters) |
| `Ans` | انس | 97 | 52 | 0.825 | high inter-cluster connectivity (45 clusters) |
| `ErD` | عرض | 79 | 35 | 0.671 | high inter-cluster connectivity (33 clusters) |
| `mss` | مسس | 61 | 29 | 0.705 | high inter-cluster connectivity (30 clusters) |
| `$rr` | شرر | 31 | 22 | 0.613 | noun-only; high inter-cluster connectivity (18 clusters) |
| `yAs` | ياس | 13 | 9 | 0.615 | bridge (9 clusters) |
| `bhm` | بهم | 3 | 2 | 0.0 | noun-only; rare (3 occ.); bridge (5 clusters) |
| `nAy` | ناي | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |
| `qbs` | قبس | 3 | 3 | 0.667 | rare (3 occ.) |
| `lgb` | لغب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `Tmv` | طمث | 2 | 1 | 0.0 | verb-only; rare (2 occ.); confined to 1 surah |

### Cluster 44: (unnamed)

_11 roots, 381 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jEl` | جعل | 346 | 66 | 0.775 | high inter-cluster connectivity (96 clusters) |
| `ndd` | ندد | 6 | 5 | 0.667 | noun-only; bridge (9 clusters) |
| `dHr` | دحر | 4 | 3 | 1.0 | noun-only; rare (4 occ.) |
| `rHl` | رحل | 4 | 2 | 1.0 | noun-only; rare (4 occ.) |
| `sqf` | سقف | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |
| `jzA` | جزا | 3 | 3 | 0.667 | noun-only; rare (3 occ.) |
| `str` | ستر | 3 | 3 | 1.0 | rare (3 occ.) |
| `$yb` | شيب | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `sll` | سلل | 3 | 3 | 0.667 | rare (3 occ.) |
| `nsb` | نسب | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `gvw` | غثو | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 95: (unnamed)

_11 roots, 419 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ax*` | اخذ | 273 | 55 | 0.626 | high inter-cluster connectivity (79 clusters) |
| `dwr` | دور | 55 | 27 | 0.509 | high inter-cluster connectivity (30 clusters) |
| `SbH` | صبح | 45 | 25 | 0.756 | high inter-cluster connectivity (20 clusters) |
| `SyH` | صيح | 13 | 9 | 0.923 | noun-only; high Meccan concentration; bridge (6 clusters) |
| `rjf` | رجف | 8 | 5 | 0.875 | high Meccan concentration |
| `ndm` | ندم | 7 | 6 | 0.571 | noun-only; bridge (8 clusters) |
| `jvm` | جثم | 5 | 3 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `gwr` | غور | 4 | 3 | 0.5 | noun-only; rare (4 occ.) |
| `nSy` | نصي | 4 | 3 | 0.75 | noun-only; rare (4 occ.) |
| `Srm` | صرم | 3 | 1 | 1.0 | rare (3 occ.); confined to 1 surah |
| `dwl` | دول | 2 | 2 | 0.0 | rare (2 occ.) |

### Cluster 1: (unnamed)

_10 roots, 884 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ArD` | ارض | 461 | 80 | 0.707 | noun-only; high inter-cluster connectivity (98 clusters); appears in 80+ surahs |
| `smw` | سمو | 381 | 81 | 0.703 | high inter-cluster connectivity (82 clusters); appears in 80+ surahs |
| `fTr` | فطر | 20 | 17 | 1.0 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `drr` | درر | 4 | 4 | 0.75 | rare (4 occ.) |
| `$An` | شان | 4 | 4 | 0.5 | noun-only; rare (4 occ.) |
| `rqy` | رقي | 4 | 3 | 1.0 | rare (4 occ.) |
| `fzz` | فزز | 3 | 1 | 1.0 | verb-only; rare (3 occ.); confined to 1 surah |
| `mwr` | مور | 3 | 2 | 1.0 | rare (3 occ.) |
| `nbE` | نبع | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |
| `dxn` | دخن | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 24: (unnamed)

_10 roots, 234 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lyl` | ليل | 92 | 49 | 0.804 | high inter-cluster connectivity (39 clusters) |
| `sxr` | سخر | 42 | 21 | 0.786 | high inter-cluster connectivity (26 clusters) |
| `$ms` | شمس | 33 | 28 | 0.848 | noun-only; high inter-cluster connectivity (21 clusters) |
| `qmr` | قمر | 27 | 23 | 0.889 | noun-only; high Meccan concentration; high inter-cluster connectivity (15 clusters) |
| `wlj` | ولج | 14 | 8 | 0.429 | high inter-cluster connectivity (12 clusters) |
| `njm` | نجم | 13 | 12 | 0.846 | noun-only; bridge (8 clusters) |
| `lmz` | لمز | 4 | 3 | 0.25 | rare (4 occ.) |
| `srj` | سرج | 4 | 4 | 0.75 | noun-only; rare (4 occ.) |
| `kwr` | كور | 3 | 2 | 1.0 | verb-only; rare (3 occ.) |
| `srmd` | سرمد | 2 | 1 | 1.0 | noun-only; rare (2 occ.); bridge (7 clusters); confined to 1 surah |

### Cluster 71: (unnamed)

_10 roots, 269 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rwd` | رود | 148 | 47 | 0.527 | high inter-cluster connectivity (52 clusters) |
| `krh` | كره | 41 | 21 | 0.341 | high inter-cluster connectivity (17 clusters) |
| `tmm` | تمم | 22 | 12 | 0.455 | high inter-cluster connectivity (20 clusters) |
| `Swm` | صوم | 14 | 6 | 0.071 | high Medinan concentration; high inter-cluster connectivity (24 clusters) |
| `Aby` | ابي | 13 | 8 | 0.538 | verb-only; high inter-cluster connectivity (13 clusters) |
| `fwh` | فوه | 13 | 10 | 0.231 | noun-only; high inter-cluster connectivity (13 clusters) |
| `Dyf` | ضيف | 6 | 5 | 1.0 | high Meccan concentration |
| `kml` | كمل | 5 | 3 | 0.2 | rare (5 occ.); high inter-cluster connectivity (11 clusters) |
| `wfq` | وفق | 4 | 3 | 0.5 | rare (4 occ.) |
| `TfA` | طفا | 3 | 3 | 0.0 | verb-only; rare (3 occ.) |

### Cluster 28: (unnamed)

_9 roots, 248 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qlb` | قلب | 168 | 48 | 0.345 | high inter-cluster connectivity (65 clusters) |
| `$qq` | شقق | 28 | 21 | 0.5 | high inter-cluster connectivity (13 clusters) |
| `Tmn` | طمن | 13 | 11 | 0.385 | bridge (9 clusters) |
| `TbE` | طبع | 11 | 9 | 0.545 | verb-only; bridge (8 clusters) |
| `zyg` | زيغ | 9 | 7 | 0.333 | bridge (5 clusters) |
| `qsw` | قسو | 7 | 6 | 0.286 | bridge (7 clusters) |
| `rbT` | ربط | 5 | 4 | 0.4 | rare (5 occ.) |
| `wjl` | وجل | 5 | 4 | 0.6 | rare (5 occ.) |
| `Hnjr` | حنجر | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 73: (unnamed)

_8 roots, 225 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lqy` | لقي | 146 | 53 | 0.753 | high inter-cluster connectivity (60 clusters) |
| `Afk` | افك | 30 | 21 | 0.8 | high inter-cluster connectivity (16 clusters) |
| `rbw` | ربو | 20 | 12 | 0.45 | high inter-cluster connectivity (18 clusters) |
| `ESw` | عصو | 12 | 6 | 0.917 | noun-only; high Meccan concentration; high inter-cluster connectivity (15 clusters) |
| `Hbl` | حبل | 7 | 5 | 0.571 | noun-only |
| `hzz` | هزز | 5 | 5 | 0.8 | verb-only; rare (5 occ.); high inter-cluster connectivity (10 clusters) |
| `lqf` | لقف | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |
| `vEb` | ثعب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 82: (unnamed)

_8 roots, 137 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gny` | غني | 73 | 44 | 0.63 | high inter-cluster connectivity (30 clusters) |
| `nkH` | نكح | 23 | 6 | 0.043 | high Medinan concentration; high inter-cluster connectivity (20 clusters) |
| `fqr` | فقر | 14 | 11 | 0.214 | high inter-cluster connectivity (13 clusters) |
| `bxl` | بخل | 12 | 6 | 0.083 | high Medinan concentration; bridge (5 clusters) |
| `Eqd` | عقد | 7 | 5 | 0.286 | bridge (6 clusters) |
| `Eff` | عفف | 4 | 3 | 0.0 | rare (4 occ.); bridge (6 clusters) |
| `Amw` | امو | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |
| `Eyl` | عيل | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 156: (unnamed)

_8 roots, 256 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hml` | حمل | 64 | 29 | 0.641 | high inter-cluster connectivity (31 clusters) |
| `ftn` | فتن | 60 | 32 | 0.567 | high inter-cluster connectivity (32 clusters) |
| `lEn` | لعن | 41 | 18 | 0.268 | high inter-cluster connectivity (26 clusters) |
| `wzr` | وزر | 27 | 11 | 0.963 | high Meccan concentration; high inter-cluster connectivity (12 clusters) |
| `wDE` | وضع | 26 | 18 | 0.346 | high inter-cluster connectivity (28 clusters) |
| `H*r` | حذر | 21 | 12 | 0.19 | high inter-cluster connectivity (22 clusters) |
| `rDE` | رضع | 11 | 5 | 0.182 | bridge (6 clusters) |
| `Hrf` | حرف | 6 | 5 | 0.0 | high Medinan concentration; high inter-cluster connectivity (11 clusters) |

### Cluster 162: (unnamed)

_8 roots, 260 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sjd` | سجد | 92 | 32 | 0.587 | high inter-cluster connectivity (57 clusters) |
| `zyd` | زيد | 61 | 32 | 0.656 | high inter-cluster connectivity (29 clusters) |
| `ftH` | فتح | 38 | 25 | 0.632 | high inter-cluster connectivity (23 clusters) |
| `bwb` | بوب | 27 | 17 | 0.778 | noun-only; high inter-cluster connectivity (18 clusters) |
| `xTA` | خطا | 22 | 13 | 0.682 | high inter-cluster connectivity (15 clusters) |
| `rkE` | ركع | 13 | 8 | 0.231 | bridge (9 clusters) |
| `bls` | بلس | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |
| `HTT` | حطط | 2 | 2 | 0.5 | noun-only; rare (2 occ.); bridge (7 clusters) |

### Cluster 174: (unnamed)

_8 roots, 177 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hrm` | حرم | 83 | 25 | 0.422 | high inter-cluster connectivity (39 clusters) |
| `Hll` | حلل | 51 | 21 | 0.255 | high inter-cluster connectivity (32 clusters) |
| `zyl` | زيل | 10 | 10 | 0.4 | verb-only; high inter-cluster connectivity (14 clusters) |
| `zny` | زني | 9 | 4 | 0.222 | bridge (6 clusters) |
| `slf` | سلف | 8 | 7 | 0.375 | bridge (9 clusters) |
| `Syd` | صيد | 6 | 1 | 0.0 | high Medinan concentration; bridge (9 clusters); confined to 1 surah |
| `wTA` | وطا | 6 | 4 | 0.167 | bridge (7 clusters) |
| `kEb` | كعب | 4 | 2 | 0.25 | rare (4 occ.); bridge (5 clusters) |

### Cluster 9: (unnamed)

_7 roots, 137 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$Tn` | شطن | 88 | 36 | 0.602 | high inter-cluster connectivity (43 clusters) |
| `Ew*` | عوذ | 17 | 14 | 0.882 | high Meccan concentration; bridge (7 clusters) |
| `rjm` | رجم | 14 | 12 | 0.929 | high Meccan concentration; bridge (7 clusters) |
| `nzg` | نزغ | 6 | 4 | 1.0 | high Meccan concentration; bridge (5 clusters) |
| `xTw` | خطو | 5 | 3 | 0.2 | noun-only; rare (5 occ.); bridge (6 clusters) |
| `mrd` | مرد | 5 | 5 | 0.4 | rare (5 occ.) |
| `gwS` | غوص | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 67: (unnamed)

_7 roots, 221 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sbH` | سبح | 92 | 49 | 0.739 | high inter-cluster connectivity (37 clusters) |
| `Hmd` | حمد | 63 | 40 | 0.794 | high inter-cluster connectivity (28 clusters) |
| `gdw` | غدو | 16 | 13 | 0.75 | high inter-cluster connectivity (15 clusters) |
| `E$w` | عشو | 14 | 11 | 0.857 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `wSf` | وصف | 14 | 7 | 1.0 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `bkr` | بكر | 12 | 11 | 0.5 | bridge (6 clusters) |
| `ASl` | اصل | 10 | 10 | 0.4 | bridge (7 clusters) |

### Cluster 126: (unnamed)

_7 roots, 155 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ehd` | عهد | 46 | 17 | 0.348 | high inter-cluster connectivity (23 clusters) |
| `qTE` | قطع | 36 | 23 | 0.556 | high inter-cluster connectivity (29 clusters) |
| `wvq` | وثق | 34 | 13 | 0.206 | high inter-cluster connectivity (27 clusters) |
| `wSl` | وصل | 12 | 7 | 0.5 | bridge (9 clusters) |
| `rEy` | رعي | 10 | 9 | 0.6 | bridge (8 clusters) |
| `nqD` | نقض | 9 | 7 | 0.333 | high inter-cluster connectivity (12 clusters) |
| `Slb` | صلب | 8 | 7 | 0.625 | high inter-cluster connectivity (12 clusters) |

### Cluster 127: (unnamed)

_7 roots, 134 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `byt` | بيت | 73 | 29 | 0.384 | high inter-cluster connectivity (36 clusters) |
| `jbl` | جبل | 41 | 33 | 0.854 | noun-only; high Meccan concentration; high inter-cluster connectivity (25 clusters) |
| `dkk` | دكك | 7 | 4 | 1.0 | high Meccan concentration |
| `nsf` | نسف | 5 | 2 | 1.0 | rare (5 occ.); high Meccan concentration |
| `nHt` | نحت | 4 | 4 | 1.0 | verb-only; rare (4 occ.) |
| `Etq` | عتق | 2 | 1 | 0.0 | rare (2 occ.); confined to 1 surah |
| `Ehn` | عهن | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 35: (unnamed)

_6 roots, 151 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qll` | قلل | 76 | 33 | 0.553 | high inter-cluster connectivity (36 clusters) |
| `$ry` | شري | 25 | 8 | 0.16 | verb-only; high inter-cluster connectivity (19 clusters) |
| `ktm` | كتم | 21 | 7 | 0.095 | verb-only; high Medinan concentration; high inter-cluster connectivity (16 clusters) |
| `vmn` | ثمن | 19 | 13 | 0.421 | high inter-cluster connectivity (15 clusters) |
| `Ey$` | عيش | 8 | 8 | 1.0 | noun-only; high Meccan concentration |
| `glf` | غلف | 2 | 2 | 0.0 | noun-only; rare (2 occ.); bridge (6 clusters) |

### Cluster 97: (unnamed)

_6 roots, 102 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rwH` | روح | 57 | 40 | 0.789 | high inter-cluster connectivity (36 clusters) |
| `wdy` | ودي | 12 | 11 | 0.667 | noun-only; bridge (5 clusters) |
| `Ayd` | ايد | 11 | 9 | 0.182 | high inter-cluster connectivity (12 clusters) |
| `qds` | قدس | 10 | 7 | 0.3 | high inter-cluster connectivity (11 clusters) |
| `ESf` | عصف | 7 | 6 | 0.857 | high Meccan concentration |
| `Twy` | طوي | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |

### Cluster 131: (unnamed)

_6 roots, 129 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Elw` | علو | 70 | 41 | 0.786 | high inter-cluster connectivity (30 clusters) |
| `Hjr` | حجر | 21 | 14 | 0.619 | high inter-cluster connectivity (19 clusters) |
| `mTr` | مطر | 15 | 9 | 0.867 | high Meccan concentration; bridge (7 clusters) |
| `sfl` | سفل | 10 | 9 | 0.6 | bridge (7 clusters) |
| `whn` | وهن | 9 | 7 | 0.444 |  |
| `sjl` | سجل | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |

### Cluster 169: (unnamed)

_6 roots, 83 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `HfZ` | حفظ | 44 | 23 | 0.705 | high inter-cluster connectivity (24 clusters) |
| `qnt` | قنت | 13 | 8 | 0.231 | high inter-cluster connectivity (11 clusters) |
| `frj` | فرج | 9 | 8 | 0.556 | high inter-cluster connectivity (11 clusters) |
| `Swt` | صوت | 8 | 4 | 0.625 | noun-only |
| `wsT` | وسط | 5 | 4 | 0.4 | rare (5 occ.) |
| `gDD` | غضض | 4 | 3 | 0.25 | verb-only; rare (4 occ.); bridge (5 clusters) |

### Cluster 175: (unnamed)

_6 roots, 54 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hmm` | حمم | 21 | 15 | 0.857 | high Meccan concentration; high inter-cluster connectivity (11 clusters) |
| `rAs` | راس | 18 | 15 | 0.611 | noun-only; high inter-cluster connectivity (19 clusters) |
| `Sbb` | صبب | 5 | 4 | 0.8 | rare (5 occ.) |
| `gsq` | غسق | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |
| `Hlq` | حلق | 3 | 3 | 0.333 | rare (3 occ.); bridge (7 clusters) |
| `nks` | نكس | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 202: (unnamed)

_6 roots, 198 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xwf` | خوف | 124 | 42 | 0.621 | high inter-cluster connectivity (49 clusters) |
| `Hzn` | حزن | 42 | 25 | 0.619 | high inter-cluster connectivity (27 clusters) |
| `hwd` | هود | 21 | 10 | 0.476 | high inter-cluster connectivity (17 clusters) |
| `jwE` | جوع | 5 | 5 | 0.8 | rare (5 occ.) |
| `SbA` | صبا | 3 | 3 | 0.0 | proper-noun-only; rare (3 occ.); bridge (5 clusters) |
| `wjs` | وجس | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |

### Cluster 10: (unnamed)

_5 roots, 55 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hyv` | حيث | 31 | 14 | 0.484 | high inter-cluster connectivity (29 clusters) |
| `Ezl` | عزل | 10 | 8 | 0.6 | high inter-cluster connectivity (10 clusters) |
| `vqf` | ثقف | 6 | 6 | 0.0 | verb-only; high Medinan concentration; bridge (8 clusters) |
| `$Tr` | شطر | 5 | 1 | 0.0 | rare (5 occ.); high Medinan concentration; bridge (9 clusters); confined to 1 surah |
| `rgd` | رغد | 3 | 2 | 0.333 | rare (3 occ.) |

### Cluster 12: (unnamed)

_5 roots, 160 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `swy` | سوي | 83 | 48 | 0.687 | high inter-cluster connectivity (40 clusters) |
| `Er$` | عرش | 33 | 25 | 0.848 | high inter-cluster connectivity (21 clusters) |
| `$fE` | شفع | 31 | 19 | 0.742 | high inter-cluster connectivity (20 clusters) |
| `stt` | ستت | 8 | 8 | 0.75 | noun-only; high inter-cluster connectivity (11 clusters) |
| `xwy` | خوي | 5 | 5 | 0.6 | rare (5 occ.) |

### Cluster 23: (unnamed)

_5 roots, 123 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ymn` | يمن | 71 | 34 | 0.563 | high inter-cluster connectivity (38 clusters) |
| `TlE` | طلع | 19 | 13 | 0.895 | high Meccan concentration; high inter-cluster connectivity (16 clusters) |
| `lwm` | لوم | 14 | 10 | 0.857 | high Meccan concentration; bridge (9 clusters) |
| `$ml` | شمل | 12 | 9 | 1.0 | high Meccan concentration; bridge (9 clusters) |
| `fyA` | فيا | 7 | 5 | 0.143 | verb-only; high Medinan concentration; bridge (7 clusters) |

### Cluster 31: (unnamed)

_5 roots, 54 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$rb` | شرب | 39 | 22 | 0.718 | high inter-cluster connectivity (29 clusters) |
| `brd` | برد | 5 | 5 | 0.8 | noun-only; rare (5 occ.) |
| `hnA` | هنا | 4 | 4 | 0.75 | rare (4 occ.) |
| `swg` | سوغ | 3 | 3 | 1.0 | rare (3 occ.) |
| `l**` | لذذ | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 36: (unnamed)

_5 roots, 108 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eql` | عقل | 49 | 30 | 0.612 | verb-only; high inter-cluster connectivity (33 clusters) |
| `Emy` | عمي | 33 | 22 | 0.667 | high inter-cluster connectivity (18 clusters) |
| `Smm` | صمم | 15 | 13 | 0.6 | bridge (7 clusters) |
| `bkm` | بكم | 6 | 5 | 0.5 | noun-only; bridge (5 clusters) |
| `$tt` | شتت | 5 | 5 | 0.4 | rare (5 occ.) |

### Cluster 65: (unnamed)

_5 roots, 145 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `A*n` | اذن | 102 | 38 | 0.451 | high inter-cluster connectivity (47 clusters) |
| `fqh` | فقه | 20 | 12 | 0.5 | verb-only; high inter-cluster connectivity (14 clusters) |
| `knn` | كنن | 12 | 11 | 0.917 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `wqr` | وقر | 9 | 8 | 0.889 | high Meccan concentration; bridge (8 clusters) |
| `SbE` | صبع | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 84: (unnamed)

_5 roots, 69 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Any` | اني | 36 | 25 | 0.556 | high inter-cluster connectivity (26 clusters) |
| `glm` | غلم | 13 | 8 | 0.923 | noun-only; high Meccan concentration; bridge (9 clusters) |
| `Etw` | عتو | 10 | 7 | 0.9 | high Meccan concentration |
| `Eqr` | عقر | 8 | 7 | 0.875 | high Meccan concentration; bridge (5 clusters) |
| `jsm` | جسم | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 86: (unnamed)

_5 roots, 57 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gDb` | غضب | 24 | 15 | 0.542 | high inter-cluster connectivity (19 clusters) |
| `bwA` | بوا | 17 | 12 | 0.471 | high inter-cluster connectivity (19 clusters) |
| `lwH` | لوح | 6 | 4 | 1.0 | noun-only; high Meccan concentration; bridge (5 clusters) |
| `mSr` | مصر | 5 | 4 | 0.8 | rare (5 occ.); bridge (5 clusters) |
| `Asf` | اسف | 5 | 5 | 1.0 | rare (5 occ.); high Meccan concentration |

### Cluster 94: (unnamed)

_5 roots, 159 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bAs` | باس | 73 | 33 | 0.493 | high inter-cluster connectivity (40 clusters) |
| `Awy` | اوي | 36 | 23 | 0.528 | high inter-cluster connectivity (27 clusters) |
| `Syr` | صير | 29 | 22 | 0.31 | high inter-cluster connectivity (19 clusters) |
| `glZ` | غلظ | 13 | 10 | 0.308 | high inter-cluster connectivity (11 clusters) |
| `DrE` | ضرع | 8 | 4 | 1.0 | high Meccan concentration; bridge (6 clusters) |

### Cluster 107: (unnamed)

_5 roots, 33 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `byD` | بيض | 12 | 10 | 0.75 | high inter-cluster connectivity (10 clusters) |
| `swd` | سود | 10 | 8 | 0.5 | bridge (9 clusters) |
| `kZm` | كظم | 6 | 6 | 0.833 | noun-only |
| `jyb` | جيب | 3 | 3 | 0.667 | noun-only; rare (3 occ.); bridge (7 clusters) |
| `Dmm` | ضمم | 2 | 2 | 1.0 | verb-only; rare (2 occ.); bridge (6 clusters) |

### Cluster 153: (unnamed)

_5 roots, 94 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eyn` | عين | 65 | 37 | 0.785 | high inter-cluster connectivity (42 clusters) |
| `Hwr` | حور | 13 | 10 | 0.462 | bridge (7 clusters) |
| `fyD` | فيض | 9 | 7 | 0.333 | verb-only; bridge (6 clusters) |
| `Tms` | طمس | 5 | 5 | 0.8 | verb-only; rare (5 occ.) |
| `dmE` | دمع | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 164: (unnamed)

_5 roots, 34 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `slk` | سلك | 12 | 11 | 1.0 | verb-only; high Meccan concentration; high inter-cluster connectivity (11 clusters) |
| `lwn` | لون | 9 | 5 | 0.778 | noun-only; bridge (8 clusters) |
| `HTm` | حطم | 6 | 5 | 0.833 |  |
| `Sfr` | صفر | 5 | 5 | 0.6 | rare (5 occ.); bridge (5 clusters) |
| `hyj` | هيج | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |

### Cluster 199: (unnamed)

_5 roots, 94 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qrr` | قرر | 38 | 22 | 0.763 | high inter-cluster connectivity (21 clusters) |
| `Hyn` | حين | 35 | 23 | 0.829 | high inter-cluster connectivity (22 clusters) |
| `fDD` | فضض | 9 | 6 | 0.111 | high Medinan concentration; bridge (8 clusters) |
| `hbT` | هبط | 8 | 4 | 0.5 | verb-only; bridge (7 clusters) |
| `wdE` | ودع | 4 | 4 | 0.75 | rare (4 occ.) |

### Cluster 229: (unnamed)

_5 roots, 45 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bdw` | بدو | 31 | 16 | 0.419 | high inter-cluster connectivity (27 clusters) |
| `bgD` | بغض | 5 | 3 | 0.0 | noun-only; rare (5 occ.); high Medinan concentration; high inter-cluster connectivity (10 clusters) |
| `wrq` | ورق | 4 | 4 | 1.0 | noun-only; rare (4 occ.) |
| `Tfq` | طفق | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |
| `xSf` | خصف | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |

### Cluster 242: (unnamed)

_5 roots, 65 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wzn` | وزن | 23 | 14 | 0.783 | high inter-cluster connectivity (15 clusters) |
| `xff` | خفف | 17 | 13 | 0.588 | high inter-cluster connectivity (11 clusters) |
| `kyl` | كيل | 16 | 7 | 1.0 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `bDE` | بضع | 7 | 2 | 1.0 | noun-only; high Meccan concentration |
| `qsTs` | قسطس | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 14: (unnamed)

_4 roots, 60 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sdr` | صدر | 46 | 31 | 0.674 | high inter-cluster connectivity (29 clusters) |
| `$fy` | شفي | 6 | 6 | 0.833 | bridge (5 clusters) |
| `$rH` | شرح | 5 | 5 | 1.0 | verb-only; rare (5 occ.); high Meccan concentration; bridge (5 clusters) |
| `Hwj` | حوج | 3 | 3 | 0.667 | noun-only; rare (3 occ.) |

### Cluster 51: (unnamed)

_4 roots, 94 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*hb` | ذهب | 56 | 30 | 0.643 | high inter-cluster connectivity (33 clusters) |
| `swr` | سور | 17 | 13 | 0.353 | high inter-cluster connectivity (10 clusters) |
| `Hrr` | حرر | 15 | 10 | 0.2 | noun-only; high inter-cluster connectivity (11 clusters) |
| `lAlA` | لالا | 6 | 6 | 0.5 | noun-only; bridge (5 clusters) |

### Cluster 54: (unnamed)

_4 roots, 56 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*ll` | ذلل | 24 | 17 | 0.583 | high inter-cluster connectivity (22 clusters) |
| `x$E` | خشع | 17 | 16 | 0.647 | high inter-cluster connectivity (11 clusters) |
| `rhq` | رهق | 10 | 7 | 1.0 | high Meccan concentration; bridge (6 clusters) |
| `qtr` | قتر | 5 | 5 | 0.8 | rare (5 occ.) |

### Cluster 120: (unnamed)

_4 roots, 61 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sqy` | سقي | 25 | 19 | 0.72 | high inter-cluster connectivity (21 clusters) |
| `bTn` | بطن | 25 | 18 | 0.6 | high inter-cluster connectivity (24 clusters) |
| `Ebr` | عبر | 9 | 8 | 0.556 | high inter-cluster connectivity (14 clusters) |
| `lbn` | لبن | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 130: (unnamed)

_4 roots, 110 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `srr` | سرر | 44 | 33 | 0.682 | high inter-cluster connectivity (29 clusters) |
| `xfy` | خفي | 34 | 21 | 0.559 | high inter-cluster connectivity (24 clusters) |
| `jhr` | جهر | 16 | 13 | 0.625 | high inter-cluster connectivity (10 clusters) |
| `Eln` | علن | 16 | 12 | 0.688 | high inter-cluster connectivity (13 clusters) |

### Cluster 151: (unnamed)

_4 roots, 58 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Twf` | طوف | 41 | 22 | 0.341 | high inter-cluster connectivity (27 clusters) |
| `hmm` | همم | 9 | 6 | 0.333 | verb-only; bridge (8 clusters) |
| `Ewr` | عور | 4 | 2 | 0.0 | noun-only; rare (4 occ.); bridge (7 clusters) |
| `kwb` | كوب | 4 | 4 | 0.75 | noun-only; rare (4 occ.) |

### Cluster 157: (unnamed)

_4 roots, 124 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `skn` | سكن | 69 | 40 | 0.565 | high inter-cluster connectivity (46 clusters) |
| `TEm` | طعم | 48 | 26 | 0.542 | high inter-cluster connectivity (29 clusters) |
| `Twq` | طوق | 4 | 2 | 0.0 | rare (4 occ.) |
| `HDD` | حضض | 3 | 3 | 1.0 | verb-only; rare (3 occ.) |

### Cluster 161: (unnamed)

_4 roots, 33 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `HSn` | حصن | 18 | 7 | 0.167 | high inter-cluster connectivity (23 clusters) |
| `rmy` | رمي | 9 | 5 | 0.222 | verb-only; bridge (5 clusters) |
| `sfH` | سفح | 4 | 3 | 0.25 | rare (4 occ.); high inter-cluster connectivity (11 clusters) |
| `xdn` | خدن | 2 | 2 | 0.0 | noun-only; rare (2 occ.); bridge (5 clusters) |

### Cluster 183: (unnamed)

_4 roots, 63 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sEy` | سعي | 30 | 20 | 0.667 | high inter-cluster connectivity (21 clusters) |
| `mdn` | مدن | 17 | 11 | 0.765 | high inter-cluster connectivity (12 clusters) |
| `Hrb` | حرب | 11 | 9 | 0.273 | high inter-cluster connectivity (11 clusters) |
| `qSw` | قصو | 5 | 5 | 0.8 | rare (5 occ.); bridge (5 clusters) |

### Cluster 188: (unnamed)

_4 roots, 142 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hsb` | حسب | 109 | 40 | 0.495 | high inter-cluster connectivity (43 clusters) |
| `srE` | سرع | 23 | 14 | 0.478 | high inter-cluster connectivity (20 clusters) |
| `klb` | كلب | 6 | 3 | 0.833 | noun-only |
| `jrH` | جرح | 4 | 3 | 0.5 | rare (4 occ.); bridge (5 clusters) |

### Cluster 236: (unnamed)

_4 roots, 103 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fwq` | فوق | 43 | 27 | 0.628 | high inter-cluster connectivity (35 clusters) |
| `rfE` | رفع | 29 | 21 | 0.586 | high inter-cluster connectivity (23 clusters) |
| `drj` | درج | 20 | 16 | 0.55 | high inter-cluster connectivity (18 clusters) |
| `Twr` | طور | 11 | 9 | 0.727 | noun-only; high inter-cluster connectivity (10 clusters) |

### Cluster 239: (unnamed)

_4 roots, 74 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Zll` | ظلل | 33 | 20 | 0.788 | high inter-cluster connectivity (26 clusters) |
| `mnn` | منن | 27 | 20 | 0.667 | high inter-cluster connectivity (14 clusters) |
| `gmm` | غمم | 11 | 8 | 0.455 | noun-only; high inter-cluster connectivity (12 clusters) |
| `slw` | سلو | 3 | 3 | 0.667 | noun-only; rare (3 occ.); bridge (6 clusters) |

### Cluster 307: (unnamed)

_4 roots, 52 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `frH` | فرح | 22 | 13 | 0.636 | high inter-cluster connectivity (17 clusters) |
| `rkb` | ركب | 15 | 13 | 0.8 | high inter-cluster connectivity (13 clusters) |
| `xyl` | خيل | 9 | 9 | 0.444 | high inter-cluster connectivity (10 clusters) |
| `fxr` | فخر | 6 | 5 | 0.333 | bridge (6 clusters) |

### Cluster 411: (unnamed)

_4 roots, 59 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kyd` | كيد | 35 | 16 | 0.886 | high Meccan concentration; high inter-cluster connectivity (19 clusters) |
| `sbb` | سبب | 11 | 6 | 0.818 | bridge (8 clusters) |
| `mlw` | ملو | 10 | 8 | 0.4 |  |
| `mtn` | متن | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 20: (unnamed)

_3 roots, 35 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$jr` | شجر | 27 | 19 | 0.778 | high inter-cluster connectivity (23 clusters) |
| `wsws` | وسوس | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration; bridge (5 clusters) |
| `zqm` | زقم | 3 | 3 | 1.0 | proper-noun-only; rare (3 occ.) |

### Cluster 55: (unnamed)

_3 roots, 31 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rqb` | رقب | 24 | 14 | 0.458 | high inter-cluster connectivity (21 clusters) |
| `*mm` | ذمم | 5 | 3 | 0.6 | noun-only; rare (5 occ.) |
| `All` | الل | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 57: (unnamed)

_3 roots, 54 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `H$r` | حشر | 43 | 28 | 0.791 | high inter-cluster connectivity (22 clusters) |
| `*rA` | ذرا | 6 | 6 | 1.0 | verb-only; high Meccan concentration; bridge (6 clusters) |
| `wzE` | وزع | 5 | 3 | 1.0 | verb-only; rare (5 occ.); high Meccan concentration; bridge (7 clusters) |

### Cluster 58: (unnamed)

_3 roots, 22 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dyq` | ضيق | 13 | 10 | 0.692 | bridge (9 clusters) |
| `*rE` | ذرع | 5 | 4 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |
| `rHb` | رحب | 4 | 2 | 0.5 | rare (4 occ.) |

### Cluster 76: (unnamed)

_3 roots, 8 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `frt` | فرت | 3 | 3 | 1.0 | rare (3 occ.) |
| `Ajj` | اجج | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `mlH` | ملح | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 93: (unnamed)

_3 roots, 26 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hlm` | حلم | 21 | 16 | 0.429 | high inter-cluster connectivity (17 clusters) |
| `Dgv` | ضغث | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |
| `Awh` | اوه | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 128: (unnamed)

_3 roots, 53 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ejl` | عجل | 47 | 25 | 0.787 | high inter-cluster connectivity (22 clusters) |
| `jsd` | جسد | 4 | 4 | 1.0 | rare (4 occ.) |
| `xwr` | خور | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 135: (unnamed)

_3 roots, 38 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Emr` | عمر | 24 | 14 | 0.625 | high inter-cluster connectivity (23 clusters) |
| `Twl` | طول | 10 | 10 | 0.6 | bridge (8 clusters) |
| `r*l` | رذل | 4 | 4 | 0.75 | noun-only; rare (4 occ.); bridge (5 clusters) |

### Cluster 137: (unnamed)

_3 roots, 28 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gll` | غلل | 16 | 12 | 0.5 | high inter-cluster connectivity (14 clusters) |
| `Enq` | عنق | 9 | 8 | 0.778 | noun-only; bridge (6 clusters) |
| `slsl` | سلسل | 3 | 3 | 0.667 | noun-only; rare (3 occ.) |

### Cluster 147: (unnamed)

_3 roots, 62 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fsd` | فسد | 50 | 23 | 0.66 | high inter-cluster connectivity (31 clusters) |
| `bxs` | بخس | 7 | 6 | 0.857 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `Evw` | عثو | 5 | 5 | 0.8 | verb-only; rare (5 occ.); bridge (5 clusters) |

### Cluster 148: (unnamed)

_3 roots, 80 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ewd` | عود | 63 | 39 | 0.81 | high inter-cluster connectivity (28 clusters) |
| `bdA` | بدا | 15 | 11 | 0.933 | verb-only; high Meccan concentration; bridge (9 clusters) |
| `twr` | تور | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 176: (unnamed)

_3 roots, 29 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `snn` | سنن | 21 | 11 | 0.524 | noun-only; bridge (9 clusters) |
| `SlSl` | صلصل | 4 | 2 | 0.75 | noun-only; rare (4 occ.) |
| `HmA` | حما | 4 | 2 | 1.0 | rare (4 occ.) |

### Cluster 190: (unnamed)

_3 roots, 26 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hsr` | حسر | 12 | 12 | 0.75 | high inter-cluster connectivity (11 clusters) |
| `frT` | فرط | 8 | 6 | 1.0 | high Meccan concentration; bridge (5 clusters) |
| `krr` | كرر | 6 | 6 | 0.833 | noun-only |

### Cluster 234: (unnamed)

_3 roots, 32 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Trf` | طرف | 11 | 11 | 0.727 | noun-only; bridge (9 clusters) |
| `qSr` | قصر | 11 | 9 | 0.545 | bridge (7 clusters) |
| `nqS` | نقص | 10 | 9 | 0.7 | high inter-cluster connectivity (10 clusters) |

### Cluster 273: (unnamed)

_3 roots, 55 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dbr` | دبر | 44 | 31 | 0.636 | high inter-cluster connectivity (27 clusters) |
| `qmS` | قمص | 6 | 1 | 1.0 | noun-only; high Meccan concentration; confined to 1 surah |
| `qdd` | قدد | 5 | 2 | 1.0 | rare (5 occ.); high Meccan concentration |

### Cluster 408: (unnamed)

_3 roots, 15 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sqT` | سقط | 8 | 8 | 0.875 | high Meccan concentration; bridge (5 clusters) |
| `ksf` | كسف | 5 | 5 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration; bridge (5 clusters) |
| `rTb` | رطب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 415: (unnamed)

_3 roots, 65 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbr` | خبر | 52 | 31 | 0.462 | high inter-cluster connectivity (28 clusters) |
| `lTf` | لطف | 8 | 8 | 0.75 | bridge (6 clusters) |
| `n$z` | نشز | 5 | 3 | 0.0 | rare (5 occ.); high Medinan concentration; bridge (5 clusters) |

### Cluster 460: (unnamed)

_3 roots, 36 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nSb` | نصب | 32 | 19 | 0.469 | high inter-cluster connectivity (23 clusters) |
| `zlm` | زلم | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |
| `xmS` | خمص | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 586: (unnamed)

_3 roots, 32 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `swq` | سوق | 17 | 13 | 0.882 | high Meccan concentration; high inter-cluster connectivity (19 clusters) |
| `xzn` | خزن | 13 | 11 | 0.923 | noun-only; high Meccan concentration; high inter-cluster connectivity (12 clusters) |
| `zmr` | زمر | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 33: (unnamed)

_2 roots, 36 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `grb` | غرب | 19 | 13 | 0.579 | high inter-cluster connectivity (14 clusters) |
| `$rq` | شرق | 17 | 13 | 0.647 | high inter-cluster connectivity (10 clusters) |

### Cluster 42: (unnamed)

_2 roots, 37 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gfl` | غفل | 35 | 21 | 0.771 | high inter-cluster connectivity (26 clusters) |
| `$xS` | شخص | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 56: (unnamed)

_2 roots, 15 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xrr` | خرر | 12 | 10 | 0.917 | verb-only; high Meccan concentration; high inter-cluster connectivity (14 clusters) |
| `*qn` | ذقن | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 74: (unnamed)

_2 roots, 6 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Afl` | افل | 4 | 1 | 1.0 | rare (4 occ.); confined to 1 surah |
| `bzg` | بزغ | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 85: (unnamed)

_2 roots, 16 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wkA` | وكا | 11 | 10 | 0.727 | bridge (7 clusters) |
| `Ark` | ارك | 5 | 4 | 0.8 | noun-only; rare (5 occ.) |

### Cluster 88: (unnamed)

_2 roots, 35 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rjw` | رجو | 28 | 21 | 0.714 | high inter-cluster connectivity (20 clusters) |
| `Asw` | اسو | 7 | 5 | 0.143 | high Medinan concentration; bridge (8 clusters) |

### Cluster 102: (unnamed)

_2 roots, 17 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `DHk` | ضحك | 10 | 8 | 0.9 | high Meccan concentration |
| `bky` | بكي | 7 | 6 | 0.857 | high Meccan concentration |

### Cluster 111: (unnamed)

_2 roots, 17 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wqd` | وقد | 11 | 10 | 0.364 | high inter-cluster connectivity (13 clusters) |
| `DwA` | ضوا | 6 | 5 | 0.5 | high inter-cluster connectivity (10 clusters) |

### Cluster 125: (unnamed)

_2 roots, 43 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Efw` | عفو | 35 | 11 | 0.171 | high inter-cluster connectivity (26 clusters) |
| `SfH` | صفح | 8 | 6 | 0.5 | bridge (7 clusters) |

### Cluster 129: (unnamed)

_2 roots, 14 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ekf` | عكف | 9 | 7 | 0.556 | high inter-cluster connectivity (11 clusters) |
| `Snm` | صنم | 5 | 5 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration; bridge (5 clusters) |

### Cluster 132: (unnamed)

_2 roots, 46 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Tgy` | طغي | 39 | 27 | 0.744 | high inter-cluster connectivity (22 clusters) |
| `Emh` | عمه | 7 | 7 | 0.857 | verb-only; high Meccan concentration |

### Cluster 133: (unnamed)

_2 roots, 13 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xwl` | خول | 8 | 5 | 0.375 | high inter-cluster connectivity (11 clusters) |
| `Emm` | عمم | 5 | 3 | 0.0 | noun-only; rare (5 occ.); high Medinan concentration; high inter-cluster connectivity (10 clusters) |

### Cluster 142: (unnamed)

_2 roots, 15 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nb*` | نبذ | 12 | 10 | 0.667 | verb-only; bridge (7 clusters) |
| `Ery` | عري | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 145: (unnamed)

_2 roots, 56 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ysr` | يسر | 44 | 27 | 0.614 | high inter-cluster connectivity (24 clusters) |
| `Esr` | عسر | 12 | 9 | 0.583 | bridge (9 clusters) |

### Cluster 159: (unnamed)

_2 roots, 13 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xsf` | خسف | 8 | 7 | 1.0 | verb-only; high Meccan concentration; bridge (6 clusters) |
| `HSb` | حصب | 5 | 5 | 1.0 | noun-only; rare (5 occ.); high Meccan concentration |

### Cluster 166: (unnamed)

_2 roots, 18 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rhb` | رهب | 12 | 10 | 0.417 | high inter-cluster connectivity (10 clusters) |
| `Hbr` | حبر | 6 | 4 | 0.333 | bridge (5 clusters) |

### Cluster 172: (unnamed)

_2 roots, 40 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wry` | وري | 32 | 25 | 0.625 | high inter-cluster connectivity (22 clusters) |
| `Hjb` | حجب | 8 | 8 | 0.875 | noun-only; high Meccan concentration; bridge (6 clusters) |

### Cluster 200: (unnamed)

_2 roots, 44 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hzA` | هزا | 34 | 21 | 0.706 | high inter-cluster connectivity (17 clusters) |
| `Hyq` | حيق | 10 | 9 | 1.0 | verb-only; high Meccan concentration; bridge (7 clusters) |

### Cluster 203: (unnamed)

_2 roots, 13 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SEq` | صعق | 11 | 8 | 0.636 | high inter-cluster connectivity (11 clusters) |
| `rEd` | رعد | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 205: (unnamed)

_2 roots, 30 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `n$r` | نشر | 21 | 18 | 0.905 | high Meccan concentration; high inter-cluster connectivity (12 clusters) |
| `SHf` | صحف | 9 | 8 | 0.889 | noun-only; high Meccan concentration |

### Cluster 214: (unnamed)

_2 roots, 51 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jHm` | جحم | 26 | 18 | 0.769 | noun-only; high inter-cluster connectivity (10 clusters) |
| `Sly` | صلي | 25 | 21 | 0.8 | high inter-cluster connectivity (10 clusters) |

### Cluster 220: (unnamed)

_2 roots, 6 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SrSr` | صرصر | 3 | 3 | 1.0 | rare (3 occ.) |
| `nHs` | نحس | 3 | 3 | 0.667 | rare (3 occ.); bridge (5 clusters) |

### Cluster 243: (unnamed)

_2 roots, 10 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qbr` | قبر | 8 | 8 | 0.625 |  |
| `bEvr` | بعثر | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |

### Cluster 246: (unnamed)

_2 roots, 20 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jbr` | جبر | 10 | 9 | 0.8 | bridge (9 clusters) |
| `bT$` | بطش | 10 | 8 | 1.0 | high Meccan concentration |

### Cluster 257: (unnamed)

_2 roots, 12 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `brhn` | برهن | 8 | 7 | 0.75 | noun-only |
| `hAt` | هات | 4 | 4 | 0.75 | verb-only; rare (4 occ.) |

### Cluster 259: (unnamed)

_2 roots, 19 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qhr` | قهر | 10 | 9 | 0.9 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `brz` | برز | 9 | 8 | 0.667 | high inter-cluster connectivity (14 clusters) |

### Cluster 268: (unnamed)

_2 roots, 27 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dbb` | دبب | 18 | 14 | 0.722 | noun-only; high inter-cluster connectivity (18 clusters) |
| `bvv` | بثث | 9 | 9 | 0.778 | bridge (8 clusters) |

### Cluster 269: (unnamed)

_2 roots, 24 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `byE` | بيع | 15 | 8 | 0.067 | high Medinan concentration; high inter-cluster connectivity (16 clusters) |
| `tjr` | تجر | 9 | 7 | 0.111 | noun-only; high Medinan concentration; high inter-cluster connectivity (10 clusters) |

### Cluster 282: (unnamed)

_2 roots, 18 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kfl` | كفل | 10 | 8 | 0.6 | bridge (8 clusters) |
| `dll` | دلل | 8 | 6 | 0.875 | high Meccan concentration; bridge (8 clusters) |

### Cluster 291: (unnamed)

_2 roots, 24 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nzE` | نزع | 20 | 16 | 0.7 | high inter-cluster connectivity (15 clusters) |
| `f$l` | فشل | 4 | 2 | 0.0 | verb-only; rare (4 occ.); bridge (5 clusters) |

### Cluster 318: (unnamed)

_2 roots, 31 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `g$w` | غشو | 29 | 23 | 0.759 | high inter-cluster connectivity (24 clusters) |
| `nEs` | نعس | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 332: (unnamed)

_2 roots, 23 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nyl` | نيل | 12 | 7 | 0.25 | high inter-cluster connectivity (11 clusters) |
| `gyZ` | غيظ | 11 | 8 | 0.273 | high inter-cluster connectivity (10 clusters) |

### Cluster 362: (unnamed)

_2 roots, 12 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jdd` | جدد | 10 | 8 | 0.9 | high Meccan concentration; high inter-cluster connectivity (10 clusters) |
| `rft` | رفت | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 367: (unnamed)

_2 roots, 49 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `krm` | كرم | 47 | 29 | 0.723 | high inter-cluster connectivity (22 clusters) |
| `jll` | جلل | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 369: (unnamed)

_2 roots, 18 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wqt` | وقت | 13 | 10 | 0.846 | bridge (5 clusters) |
| `jlw` | جلو | 5 | 4 | 0.8 | rare (5 occ.) |

### Cluster 373: (unnamed)

_2 roots, 34 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jnd` | جند | 29 | 18 | 0.69 | noun-only; high inter-cluster connectivity (20 clusters) |
| `jwz` | جوز | 5 | 5 | 0.8 | verb-only; rare (5 occ.); bridge (7 clusters) |

### Cluster 390: (unnamed)

_2 roots, 9 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kAs` | كاس | 6 | 5 | 0.667 | noun-only |
| `mzj` | مزج | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |

### Cluster 398: (unnamed)

_2 roots, 18 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mhd` | مهد | 16 | 13 | 0.625 | high inter-cluster connectivity (12 clusters) |
| `khl` | كهل | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 401: (unnamed)

_2 roots, 40 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wsE` | وسع | 32 | 15 | 0.406 | high inter-cluster connectivity (21 clusters) |
| `klf` | كلف | 8 | 7 | 0.5 | bridge (7 clusters) |

### Cluster 406: (unnamed)

_2 roots, 70 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ksb` | كسب | 67 | 27 | 0.567 | verb-only; high inter-cluster connectivity (30 clusters) |
| `rhn` | رهن | 3 | 3 | 0.667 | noun-only; rare (3 occ.) |

### Cluster 422: (unnamed)

_2 roots, 11 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sry` | سري | 8 | 8 | 1.0 | high Meccan concentration; bridge (6 clusters) |
| `lft` | لفت | 3 | 3 | 1.0 | verb-only; rare (3 occ.); bridge (5 clusters) |

### Cluster 434: (unnamed)

_2 roots, 26 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `m$y` | مشي | 23 | 14 | 0.783 | high inter-cluster connectivity (19 clusters) |
| `mrH` | مرح | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 440: (unnamed)

_2 roots, 37 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mdd` | مدد | 32 | 24 | 0.781 | high inter-cluster connectivity (20 clusters) |
| `nfd` | نفد | 5 | 4 | 1.0 | rare (5 occ.); high Meccan concentration |

### Cluster 443: (unnamed)

_2 roots, 19 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mnE` | منع | 17 | 16 | 0.765 | high inter-cluster connectivity (12 clusters) |
| `xrb` | خرب | 2 | 2 | 0.0 | rare (2 occ.) |

### Cluster 448: (unnamed)

_2 roots, 19 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rsw` | رسو | 14 | 13 | 0.929 | high Meccan concentration; high inter-cluster connectivity (13 clusters) |
| `myd` | ميد | 5 | 4 | 0.6 | rare (5 occ.); bridge (7 clusters) |

### Cluster 486: (unnamed)

_2 roots, 18 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sbt` | سبت | 9 | 6 | 0.667 | bridge (5 clusters) |
| `nwm` | نوم | 9 | 9 | 0.778 | noun-only; high inter-cluster connectivity (10 clusters) |

### Cluster 492: (unnamed)

_2 roots, 14 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `q*f` | قذف | 9 | 6 | 0.778 | verb-only; bridge (5 clusters) |
| `rEb` | رعب | 5 | 5 | 0.2 | noun-only; rare (5 occ.); bridge (8 clusters) |

### Cluster 515: (unnamed)

_2 roots, 7 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xsA` | خسا | 4 | 4 | 0.75 | rare (4 occ.) |
| `qrd` | قرد | 3 | 3 | 0.333 | noun-only; rare (3 occ.) |

### Cluster 567: (unnamed)

_2 roots, 19 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sjn` | سجن | 12 | 3 | 1.0 | high Meccan concentration; high inter-cluster connectivity (15 clusters) |
| `xmr` | خمر | 7 | 5 | 0.286 | noun-only; high inter-cluster connectivity (14 clusters) |

### Cluster 2: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$Eb` | شعب | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 3: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$El` | شعل | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 6: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$Hm` | شحم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 13: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$fh` | شفه | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 15: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$gf` | شغف | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 16: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$gl` | شغل | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 18: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$hq` | شهق | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 21: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$kl` | شكل | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 22: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$ks` | شكس | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 25: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$mt` | شمت | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 26: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$mx` | شمخ | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 27: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$mz` | شمز | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 29: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$r*m` | شرذم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 30: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$rT` | شرط | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 32: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$rd` | شرد | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 37: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$tw` | شتو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 38: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$wZ` | شوظ | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 39: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$wb` | شوب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 40: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$wk` | شوك | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 41: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$wy` | شوي | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 45: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `$yd` | شيد | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 47: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*Am` | ذام | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 48: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*En` | ذعن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 49: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*b*b` | ذبذب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 50: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*bb` | ذبب | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 52: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*hl` | ذهل | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 53: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*kw` | ذكو | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 60: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*rw` | ذرو | 3 | 2 | 1.0 | rare (3 occ.) |

### Cluster 61: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*wd` | ذود | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 63: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*xr` | ذخر | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 64: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `*yE` | ذيع | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 68: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Abb` | ابب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 69: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Abl` | ابل | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 70: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Abq` | ابق | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 72: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Add` | ادد | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 79: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Alt` | الت | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 80: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Aml` | امل | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 81: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Amt` | امت | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 83: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Anm` | انم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 87: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Asn` | اسن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 89: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Avl` | اثل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 91: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Avv` | اثث | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 92: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Awd` | اود | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 98: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Aym` | ايم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 99: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Azf` | ازف | 3 | 2 | 1.0 | rare (3 occ.) |

### Cluster 100: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Azz` | ازز | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 101: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `DAn` | ضان | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 103: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `DbH` | ضبح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 104: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ddd` | ضدد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 105: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `DfdE` | ضفدع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 106: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `DhA` | ضها | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 108: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dmr` | ضمر | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 109: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dnk` | ضنك | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 110: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dnn` | ضنن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 112: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dyr` | ضير | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 113: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Dyz` | ضيز | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 114: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `EDd` | عضد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 115: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `EDw` | عضو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 116: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ETf` | عطف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 117: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ETl` | عطل | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 118: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `EbA` | عبا | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 119: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ebqr` | عبقر | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 121: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ebs` | عبس | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 122: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ebv` | عبث | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 123: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eds` | عدس | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 124: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Efr` | عفر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 134: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Emq` | عمق | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 136: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Enkb` | عنكب | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 138: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Enw` | عنو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 139: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eqm` | عقم | 4 | 3 | 0.75 | rare (4 occ.) |

### Cluster 140: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Erjn` | عرجن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 141: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Erm` | عرم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 143: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `EsEs` | عسعس | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 144: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Esl` | عسل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 146: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Etl` | عتل | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 149: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ewl` | عول | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 150: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ewq` | عوق | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 152: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eyb` | عيب | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 154: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Eyr` | عير | 3 | 1 | 1.0 | noun-only; rare (3 occ.); confined to 1 surah |

### Cluster 155: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Ezw` | عزو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 158: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `HSHS` | حصحص | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 160: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `HSl` | حصل | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 163: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `HTb` | حطب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 165: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hbk` | حبك | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 167: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hdb` | حدب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 168: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hdq` | حدق | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 170: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hfd` | حفد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 171: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hfr` | حفر | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 173: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hjz` | حجز | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 177: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hn*` | حنذ | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 178: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hnk` | حنك | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 179: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hnn` | حنن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 180: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hnv` | حنث | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 181: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hqb` | حقب | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 182: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hqf` | حقف | 1 | 1 | 1.0 | proper-noun-only; single occurrence; confined to 1 surah |

### Cluster 184: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hrd` | حرد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 185: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hrk` | حرك | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 186: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hrs` | حرس | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 187: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hry` | حري | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 189: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hsm` | حسم | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 192: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Htm` | حتم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 193: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hvv` | حثث | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 194: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hwb` | حوب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 195: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hwy` | حوي | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 196: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hwz` | حوز | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 197: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hyd` | حيد | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 198: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hyf` | حيف | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 201: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Hyr` | حير | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 204: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SEr` | صعر | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 206: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sbg` | صبغ | 3 | 2 | 0.333 | noun-only; rare (3 occ.) |

### Cluster 207: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sdy` | صدي | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 208: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SfSf` | صفصف | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 210: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sfn` | صفن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 211: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Shr` | صهر | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 212: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Skk` | صكك | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 213: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sld` | صلد | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 215: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SmE` | صمع | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 216: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Smd` | صمد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 217: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Smt` | صمت | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 218: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Snw` | صنو | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 219: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SrE` | صرع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 221: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SwE` | صوع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 222: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Swf` | صوف | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 223: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sxr` | صخر | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 224: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Sxx` | صخخ | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 225: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `SyS` | صيص | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 226: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Syf` | صيف | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 227: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `THw` | طحو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 228: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Tff` | طفف | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 230: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `TlH` | طلح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 231: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Tll` | طلل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 232: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Tmm` | طمم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 233: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `TrH` | طرح | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 235: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Twd` | طود | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 237: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ZEn` | ظعن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 238: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `Zfr` | ظفر | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 240: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `b*r` | بذر | 3 | 1 | 1.0 | rare (3 occ.); confined to 1 surah |

### Cluster 241: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bAr` | بار | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 244: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bHv` | بحث | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 245: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bSl` | بصل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 247: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bTA` | بطا | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 248: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bdn` | بدن | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 249: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bdr` | بدر | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 250: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bgl` | بغل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 251: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bhl` | بهل | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 252: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bjs` | بجس | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 253: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `blE` | بلع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 254: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bnn` | بنن | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 255: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bqE` | بقع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 256: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bql` | بقل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 258: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `brm` | برم | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 260: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bsl` | بسل | 2 | 1 | 1.0 | verb-only; rare (2 occ.); confined to 1 surah |

### Cluster 261: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bsm` | بسم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 262: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bsq` | بسق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 263: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bsr` | بسر | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 264: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `bss` | بسس | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 265: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `btk` | بتك | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 266: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `btl` | بتل | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 267: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `btr` | بتر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 270: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `byd` | بيد | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 271: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dEE` | دعع | 3 | 2 | 1.0 | rare (3 occ.) |

### Cluster 272: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dHw` | دحو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 274: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dfA` | دفا | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 275: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dfq` | دفق | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 276: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dhm` | دهم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 277: (unnamed)

_1 roots, 5 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dhn` | دهن | 5 | 4 | 0.8 | rare (5 occ.) |

### Cluster 278: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dhq` | دهق | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 279: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dhr` | دهر | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 280: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dhy` | دهي | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 281: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dlk` | دلك | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 283: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dmdm` | دمدم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 284: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dmg` | دمغ | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 285: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dnr` | دنر | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 286: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `drhm` | درهم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 287: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dsr` | دسر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 288: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dss` | دسس | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 289: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dsw` | دسو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 290: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `dvr` | دثر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 292: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fDH` | فضح | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 293: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fDw` | فضو | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 294: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fSH` | فصح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 295: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fSm` | فصم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 296: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fZZ` | فظظ | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 297: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fhm` | فهم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 298: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fjw` | فجو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 299: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fkk` | فكك | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 300: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fln` | فلن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 301: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `flq` | فلق | 4 | 3 | 1.0 | rare (4 occ.) |

### Cluster 302: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fnd` | فند | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 303: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fnn` | فنن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 304: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fny` | فني | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 305: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fqE` | فقع | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 306: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `frE` | فرع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 308: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `frh` | فره | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 309: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `frv` | فرث | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 310: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fsH` | فسح | 3 | 1 | 0.0 | verb-only; rare (3 occ.); confined to 1 surah |

### Cluster 311: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fsr` | فسر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 312: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ftA` | فتا | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 313: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ftq` | فتق | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 314: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ftr` | فتر | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 315: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fwD` | فوض | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 316: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fwm` | فوم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 317: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `fyl` | فيل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 319: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gSS` | غصص | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 320: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gSb` | غصب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 321: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gT$` | غطش | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 322: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gbn` | غبن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 323: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gdq` | غدق | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 324: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `glq` | غلق | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 325: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gly` | غلي | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 326: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gmD` | غمض | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 327: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gmr` | غمر | 4 | 3 | 1.0 | noun-only; rare (4 occ.) |

### Cluster 328: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gmz` | غمز | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 329: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `grw` | غرو | 2 | 2 | 0.0 | verb-only; rare (2 occ.) |

### Cluster 330: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gwl` | غول | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 331: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gyD` | غيض | 2 | 2 | 0.5 | verb-only; rare (2 occ.) |

### Cluster 333: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gzl` | غزل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 334: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `gzw` | غزو | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 335: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `h$$` | هشش | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 336: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hDm` | هضم | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 337: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hbw` | هبو | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 338: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hdd` | هدد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 339: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hdhd` | هدهد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 340: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hdm` | هدم | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 341: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hjE` | هجع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 342: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hjd` | هجد | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 343: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hlE` | هلع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 344: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hmd` | همد | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 345: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hmr` | همر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 346: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hms` | همس | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 347: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hmz` | همز | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 348: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hrE` | هرع | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |

### Cluster 349: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hrb` | هرب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 350: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hwr` | هور | 2 | 1 | 0.0 | rare (2 occ.); confined to 1 surah |

### Cluster 351: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hyl` | هيل | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 352: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hym` | هيم | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 353: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hyt` | هيت | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 354: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hzl` | هزل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 355: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `hzm` | هزم | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 356: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `j**` | جذذ | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 357: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `j*w` | جذو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 358: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jAr` | جار | 3 | 2 | 1.0 | verb-only; rare (3 occ.) |

### Cluster 359: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jbh` | جبه | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 360: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jbn` | جبن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 361: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jbt` | جبت | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 363: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jfA` | جفا | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 364: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jfn` | جفن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 365: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jfw` | جفو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 366: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jlb` | جلب | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 368: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jls` | جلس | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 370: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jmH` | جمح | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 371: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jmd` | جمد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 372: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jmm` | جمم | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 374: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jny` | جني | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 375: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jrE` | جرع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 376: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jrd` | جرد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 377: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jrf` | جرف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 378: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jrr` | جرر | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 379: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jrz` | جرز | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 380: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jss` | جسس | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 381: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jvv` | جثث | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 382: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jvw` | جثو | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 383: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jwd` | جود | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 384: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jwf` | جوف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 385: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jws` | جوس | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 386: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jww` | جوو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 387: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jyd` | جيد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 388: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `jzE` | جزع | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 389: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `k$T` | كشط | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 391: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kbd` | كبد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 392: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kbkb` | كبكب | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 393: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kdH` | كدح | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 394: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kdr` | كدر | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 395: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kdy` | كدي | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 396: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kfA` | كفا | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 397: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kft` | كفت | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 399: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `klA` | كلا | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 400: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `klH` | كلح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 402: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kmm` | كمم | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 403: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `knd` | كند | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 404: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kns` | كنس | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 405: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `krs` | كرس | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 407: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ksd` | كسد | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 409: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kvb` | كثب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 410: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `kwy` | كوي | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 412: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lHf` | لحف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 413: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lHn` | لحن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 414: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lHy` | لحي | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 416: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lZy` | لظي | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 417: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lbd` | لبد | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 418: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ldd` | لدد | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 419: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lfH` | لفح | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 420: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lfZ` | لفظ | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 421: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lff` | لفف | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 423: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lhb` | لهب | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 424: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lhm` | لهم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 425: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lhv` | لهث | 2 | 1 | 1.0 | verb-only; rare (2 occ.); confined to 1 surah |

### Cluster 426: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lqH` | لقح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 427: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lqb` | لقب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 428: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lqm` | لقم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 429: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lw*` | لوذ | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 430: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lwt` | لوت | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 431: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lyt` | ليت | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 432: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `lzb` | لزب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 433: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `m$j` | مشج | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 435: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mEn` | معن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 436: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mEy` | معي | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 437: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mEz` | معز | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 438: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mHl` | محل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 439: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mTw` | مطو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 441: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mjs` | مجس | 1 | 1 | 0.0 | proper-noun-only; single occurrence; confined to 1 surah |

### Cluster 442: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mkw` | مكو | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 444: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `msd` | مسد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 445: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `msw` | مسو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 446: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `msx` | مسخ | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 447: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mxD` | مخض | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 449: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `myr` | مير | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 450: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `mzn` | مزن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 451: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `n$T` | نشط | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 452: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nDd` | نضد | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 453: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nDj` | نضج | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 454: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nDx` | نضخ | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 455: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nEl` | نعل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 456: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nEq` | نعق | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 457: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nHb` | نحب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 458: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nHl` | نحل | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 459: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nHr` | نحر | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 461: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nTH` | نطح | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 462: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nbT` | نبط | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 463: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nbz` | نبز | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 464: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nf*` | نفذ | 3 | 1 | 0.0 | verb-only; rare (3 occ.); confined to 1 surah |

### Cluster 465: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nfH` | نفح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 466: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nfv` | نفث | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 467: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nfy` | نفي | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 468: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ngD` | نغض | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 469: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nhj` | نهج | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 470: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `njd` | نجد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 471: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `njs` | نجس | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 472: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nkb` | نكب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 473: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nkd` | نكد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 474: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nmm` | نمم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 475: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nqE` | نقع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 476: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nqb` | نقب | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 477: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nqr` | نقر | 4 | 2 | 0.5 | rare (4 occ.) |

### Cluster 478: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nsA` | نسا | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 479: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nsl` | نسل | 4 | 4 | 0.75 | rare (4 occ.) |

### Cluster 480: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nsr` | نسر | 1 | 1 | 1.0 | proper-noun-only; single occurrence; confined to 1 surah |

### Cluster 481: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ntq` | نتق | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 482: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nvr` | نثر | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 483: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nw$` | نوش | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 484: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nwA` | نوا | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 485: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nwS` | نوص | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 487: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nwn` | نون | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 488: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nwy` | نوي | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 489: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nxr` | نخر | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 490: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `nzf` | نزف | 2 | 2 | 1.0 | verb-only; rare (2 occ.) |

### Cluster 491: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `q$Er` | قشعر | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 493: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qDD` | قضض | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 494: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qDb` | قضب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 495: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qEr` | قعر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 496: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qHm` | قحم | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 497: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qSf` | قصف | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 498: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qSm` | قصم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 499: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qTT` | قطط | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 500: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qTmr` | قطمر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 501: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qbH` | قبح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 502: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qdH` | قدح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 503: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qfl` | قفل | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 504: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qlE` | قلع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 505: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qlm` | قلم | 4 | 4 | 0.75 | noun-only; rare (4 occ.) |

### Cluster 506: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qly` | قلي | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 507: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qmE` | قمع | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 508: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qmH` | قمح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 509: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qmTr` | قمطر | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 510: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qml` | قمل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 511: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qnE` | قنع | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 512: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qnw` | قنو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 513: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qny` | قني | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 514: (unnamed)

_1 roots, 5 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qrE` | قرع | 5 | 3 | 0.8 | noun-only; rare (5 occ.) |

### Cluster 516: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qsr` | قسر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 517: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qss` | قسس | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 518: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qvA` | قثا | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 519: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qwE` | قوع | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 520: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qwb` | قوب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 521: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qws` | قوس | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 522: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qwt` | قوت | 2 | 2 | 0.5 | noun-only; rare (2 occ.) |

### Cluster 523: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `qyl` | قيل | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 524: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rHq` | رحق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 525: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rSS` | رصص | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 526: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rbH` | ربح | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 527: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rdA` | ردا | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 528: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rdf` | ردف | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 529: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rdm` | ردم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 530: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rfd` | رفد | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 531: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rfrf` | رفرف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 532: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rgm` | رغم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 533: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rhw` | رهو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 534: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rjj` | رجج | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 535: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rkD` | ركض | 3 | 2 | 1.0 | verb-only; rare (3 occ.) |

### Cluster 536: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rkd` | ركد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 537: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rkz` | ركز | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 538: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rmH` | رمح | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 539: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rmd` | رمد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 540: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rmm` | رمم | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 541: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rmz` | رمز | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 542: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rqd` | رقد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 543: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rqq` | رقق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 544: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rtE` | رتع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 545: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rtq` | رتق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 546: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rwE` | روع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 547: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rwg` | روغ | 3 | 2 | 1.0 | verb-only; rare (3 occ.) |

### Cluster 548: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `rxw` | رخو | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 549: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ry$` | ريش | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 550: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ryE` | ريع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 551: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ryn` | رين | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 552: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sEd` | سعد | 2 | 1 | 1.0 | rare (2 occ.); confined to 1 surah |

### Cluster 553: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sHl` | سحل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 554: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sHq` | سحق | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 555: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sTH` | سطح | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 556: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sTw` | سطو | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 557: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sbg` | سبغ | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 558: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sdr` | سدر | 4 | 3 | 1.0 | noun-only; rare (4 occ.) |

### Cluster 559: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sdy` | سدي | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 560: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sfE` | سفع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 561: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sfn` | سفن | 4 | 2 | 1.0 | noun-only; rare (4 occ.) |

### Cluster 562: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sgb` | سغب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 563: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `shl` | سهل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 564: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `shm` | سهم | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 565: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `shr` | سهر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 566: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `shw` | سهو | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 568: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sjw` | سجو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 569: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `skb` | سكب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 570: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `skt` | سكت | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 571: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `slH` | سلح | 4 | 1 | 0.0 | noun-only; rare (4 occ.); confined to 1 surah |

### Cluster 572: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `slb` | سلب | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 573: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `slq` | سلق | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 574: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `smd` | سمد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 575: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `smk` | سمك | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 576: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `snd` | سند | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 577: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `snh` | سنه | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 578: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `snm` | سنم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 579: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `sqm` | سقم | 2 | 1 | 1.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 580: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `srb` | سرب | 4 | 4 | 0.5 | noun-only; rare (4 occ.) |

### Cluster 581: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `srbl` | سربل | 3 | 2 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 582: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `srd` | سرد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 583: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `srdq` | سردق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 584: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `swH` | سوح | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 585: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `swT` | سوط | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 587: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `syb` | سيب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 588: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tEs` | تعس | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 589: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tfv` | تفث | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 590: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tll` | تلل | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 591: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tqn` | تقن | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 592: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `trq` | ترق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 593: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tyh` | تيه | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 594: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `tyn` | تين | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 595: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vbT` | ثبط | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 596: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vby` | ثبي | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 597: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vjj` | ثجج | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 598: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vqb` | ثقب | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 599: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vrb` | ثرب | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 600: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vry` | ثري | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 601: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `vyb` | ثيب | 1 | 1 | 0.0 | single occurrence; confined to 1 surah |

### Cluster 602: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `w$y` | وشي | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 603: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wAd` | واد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 604: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wAl` | وال | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 605: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wDn` | وضن | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 606: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wH$` | وحش | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 607: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wSb` | وصب | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 608: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wSd` | وصد | 3 | 3 | 1.0 | rare (3 occ.) |

### Cluster 609: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wTn` | وطن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 610: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wTr` | وطر | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 611: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wbq` | وبق | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 612: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wbr` | وبر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 613: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wfD` | وفض | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 614: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wfd` | وفد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 615: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wfr` | وفر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 616: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `whj` | وهج | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 617: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `why` | وهي | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 618: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wjb` | وجب | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 619: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wjf` | وجف | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 620: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wkd` | وكد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 621: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wkz` | وكز | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 622: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wny` | وني | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 623: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wq*` | وقذ | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 624: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wqb` | وقب | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 625: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wsm` | وسم | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 626: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wsn` | وسن | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 627: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wsq` | وسق | 2 | 1 | 1.0 | verb-only; rare (2 occ.); confined to 1 surah |

### Cluster 628: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wtd` | وتد | 3 | 3 | 1.0 | noun-only; rare (3 occ.) |

### Cluster 629: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wtn` | وتن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 630: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `wtr` | وتر | 3 | 3 | 0.667 | rare (3 occ.) |

### Cluster 631: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `x$b` | خشب | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 632: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xDE` | خضع | 2 | 2 | 0.5 | rare (2 occ.) |

### Cluster 633: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xDd` | خضد | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 634: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xTT` | خطط | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 635: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbA` | خبا | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 636: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbT` | خبط | 1 | 1 | 0.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 637: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbl` | خبل | 2 | 2 | 0.0 | noun-only; rare (2 occ.) |

### Cluster 638: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbw` | خبو | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 639: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xbz` | خبز | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 640: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xdd` | خدد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 641: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xlE` | خلع | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 642: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xmT` | خمط | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 643: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xmd` | خمد | 2 | 2 | 1.0 | noun-only; rare (2 occ.) |

### Cluster 644: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xnq` | خنق | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 645: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xns` | خنس | 2 | 2 | 1.0 | rare (2 occ.) |

### Cluster 646: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xrTm` | خرطم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 647: (unnamed)

_1 roots, 4 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xrq` | خرق | 4 | 3 | 1.0 | verb-only; rare (4 occ.) |

### Cluster 648: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xtr` | ختر | 1 | 1 | 1.0 | single occurrence; confined to 1 surah |

### Cluster 649: (unnamed)

_1 roots, 5 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xyb` | خيب | 5 | 4 | 0.8 | rare (5 occ.) |

### Cluster 650: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `xym` | خيم | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 651: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `ynE` | ينع | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 652: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `yqZ` | يقظ | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 653: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zHf` | زحف | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 654: (unnamed)

_1 roots, 3 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zbd` | زبد | 3 | 1 | 0.0 | noun-only; rare (3 occ.); confined to 1 surah |

### Cluster 655: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zbn` | زبن | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 656: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zff` | زفف | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 657: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zhd` | زهد | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 658: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zhr` | زهر | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 659: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zjj` | زجج | 2 | 1 | 0.0 | noun-only; rare (2 occ.); confined to 1 surah |

### Cluster 660: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zmhr` | زمهر | 1 | 1 | 0.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 661: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zml` | زمل | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 662: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `znm` | زنم | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 663: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zrq` | زرق | 1 | 1 | 1.0 | noun-only; single occurrence; confined to 1 surah |

### Cluster 664: (unnamed)

_1 roots, 1 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zry` | زري | 1 | 1 | 1.0 | verb-only; single occurrence; confined to 1 surah |

### Cluster 665: (unnamed)

_1 roots, 2 total occurrences_

| Root | Arabic | Count | n_surahs | Meccan share | Notable |
|---|---|---:|---:|---:|---|
| `zwd` | زود | 2 | 1 | 0.0 | rare (2 occ.); confined to 1 surah |

---

## Data quality issues

### Visually-similar roots (case-collision groups)

Buckwalter encoding distinguishes Arabic letters by case (e.g. `s`=س, `S`=ص; `d`=د, `D`=ض; `t`=ت, `T`=ط; `h`=ه, `H`=ح; `z`=ز, `Z`=ظ; `E`=ع, `e`=unused). Many real Quranic roots collide on case-insensitive comparison. **None of these are duplicates** — each row is a distinct lexeme — but anyone doing string lookups must be case-sensitive.

Total case-collision groups: **137**.

| Group | Members (root → arabic, count) |
|---|---|
| `zlm` | `Zlm` → ظلم (315) / `zlm` → زلم (2) |
| `nws` | `nwS` → نوص (1) / `nws` → نوس (241) |
| `bed` | `bED` → بعض (158) / `bEd` → بعد (235) |
| `hsn` | `HSn` → حصن (18) / `Hsn` → حسن (194) |
| `dll` | `Dll` → ضلل (191) / `dll` → دلل (8) |
| `sme` | `SmE` → صمع (1) / `smE` → سمع (185) |
| `slh` | `SlH` → صلح (180) / `slH` → سلح (4) |
| `tbe` | `TbE` → طبع (11) / `tbE` → تبع (172) |
| `nsr` | `nSr` → نصر (158) / `nsr` → نسر (1) |
| `bsr` | `bSr` → بصر (148) / `bsr` → بسر (2) |
| `rwd` | `rwD` → روض (2) / `rwd` → رود (148) |
| `ezm` | `EZm` → عظم (128) / `Ezm` → عزم (9) |
| `nhr` | `nHr` → نحر (1) / `nhr` → نهر (113) |
| `hsb` | `HSb` → حصب (5) / `Hsb` → حسب (109) |
| `edw` | `EDw` → عضو (1) / `Edw` → عدو (106) |
| `slw` | `Slw` → صلو (99) / `slw` → سلو (3) |
| `shb` | `SHb` → صحب (97) / `sHb` → سحب (11) |
| `sbh` | `SbH` → صبح (45) / `sbH` → سبح (92) |
| `why` | `wHy` → وحي (78) / `why` → وهي (1) |
| `drr` | `Drr` → ضرر (74) / `drr` → درر (4) |
| `hmd` | `Hmd` → حمد (63) / `hmd` → همد (1) |
| `shr` | `Shr` → صهر (2) / `sHr` → سحر (63) / `shr` → سهر (1) |
| `zhr` | `Zhr` → ظهر (59) / `zhr` → زهر (1) |
| `edd` | `EDD` → عضض (2) / `EDd` → عضد (2) / `Edd` → عدد (57) |
| `hll` | `Hll` → حلل (51) / `hll` → هلل (5) |
| `swe` | `SwE` → صوع (1) / `swE` → سوع (49) |
| `sdr` | `Sdr` → صدر (46) / `sdr` → سدر (4) |
| `nsy` | `nSy` → نصي (4) / `nsy` → نسي (45) |
| `srr` | `Srr` → صرر (6) / `srr` → سرر (44) |
| `sxr` | `Sxr` → صخر (3) / `sxr` → سخر (42) |
| `sdd` | `Sdd` → صدد (42) / `sdd` → سدد (6) |
| `jhd` | `jHd` → جحد (12) / `jhd` → جهد (41) |
| `hwy` | `Hwy` → حوي (2) / `hwy` → هوي (38) |
| `btl` | `bTl` → بطل (36) / `btl` → بتل (2) |
| `zll` | `Zll` → ظلل (33) / `zll` → زلل (4) |
| `qsm` | `qSm` → قصم (1) / `qsm` → قسم (33) |
| `esy` | `ESy` → عصي (32) / `Esy` → عسي (30) |
| `nsb` | `nSb` → نصب (32) / `nsb` → نسب (3) |
| `hjr` | `Hjr` → حجر (21) / `hjr` → هجر (31) |
| `srf` | `Srf` → صرف (30) / `srf` → سرف (23) |
| `qss` | `qSS` → قصص (30) / `qss` → قسس (1) |
| `syr` | `Syr` → صير (29) / `syr` → سير (27) |
| `sbe` | `SbE` → صبع (2) / `sbE` → سبع (28) |
| `hwt` | `HwT` → حوط (28) / `Hwt` → حوت (5) |
| `edl` | `EDl` → عضل (2) / `Edl` → عدل (28) |
| `nbt` | `nbT` → نبط (1) / `nbt` → نبت (26) |
| `wde` | `wDE` → وضع (26) / `wdE` → ودع (4) |
| `hdd` | `HDD` → حضض (3) / `Hdd` → حدد (25) / `hdd` → هدد (1) |
| `mrd` | `mrD` → مرض (24) / `mrd` → مرد (5) |
| `sre` | `SrE` → صرع (1) / `srE` → سرع (23) |
| `tmm` | `Tmm` → طمم (1) / `tmm` → تمم (22) |
| `frh` | `frH` → فرح (22) / `frh` → فره (1) |
| `hmm` | `Hmm` → حمم (21) / `hmm` → همم (9) |
| `snw` | `Snw` → صنو (2) / `snw` → سنو (20) |
| `ftr` | `fTr` → فطر (20) / `ftr` → فتر (3) |
| `swr` | `Swr` → صور (19) / `swr` → سور (17) |
| `ser` | `SEr` → صعر (1) / `sEr` → سعر (19) |
| `frd` | `frD` → فرض (18) / `frd` → فرد (5) |
| `vbt` | `vbT` → ثبط (1) / `vbt` → ثبت (18) |
| `hbt` | `HbT` → حبط (16) / `hbT` → هبط (8) |
| `str` | `sTr` → سطر (16) / `str` → ستر (3) |
| `smm` | `Smm` → صمم (15) / `smm` → سمم (4) |
| `swm` | `Swm` → صوم (14) / `swm` → سوم (15) |
| `etw` | `ETw` → عطو (14) / `Etw` → عتو (10) |
| `qrd` | `qrD` → قرض (13) / `qrd` → قرد (3) |
| `qnt` | `qnT` → قنط (6) / `qnt` → قنت (13) |
| `hwr` | `Hwr` → حور (13) / `hwr` → هور (2) |
| `syh` | `SyH` → صيح (13) / `syH` → سيح (3) |
| `wsl` | `wSl` → وصل (12) / `wsl` → وسل (2) |
| `rhb` | `rHb` → رحب (4) / `rhb` → رهب (12) |
| `sfr` | `Sfr` → صفر (5) / `sfr` → سفر (12) |
| `hsr` | `HSr` → حصر (6) / `Hsr` → حسر (12) |
| `lhm` | `lHm` → لحم (12) / `lhm` → لهم (1) |
| `esr` | `ESr` → عصر (5) / `Esr` → عسر (12) |
| `byd` | `byD` → بيض (12) / `byd` → بيد (1) |
| `tyn` | `Tyn` → طين (12) / `tyn` → تين (1) |
| `ntq` | `nTq` → نطق (12) / `ntq` → نتق (1) |
| `sfh` | `SfH` → صفح (8) / `sfH` → سفح (4) / `sfh` → سفه (11) |
| `twr` | `Twr` → طور (11) / `twr` → تور (2) |
| `sbb` | `Sbb` → صبب (5) / `sbb` → سبب (11) |
| `hrb` | `Hrb` → حرب (11) / `hrb` → هرب (1) |
| `trf` | `Trf` → طرف (11) / `trf` → ترف (8) |
| `qsr` | `qSr` → قصر (11) / `qsr` → قسر (1) |
| `trq` | `Trq` → طرق (11) / `trq` → ترق (1) |
| `dmr` | `Dmr` → ضمر (1) / `dmr` → دمر (10) |
| `rhq` | `rHq` → رحق (1) / `rhq` → رهق (10) |
| `sbt` | `sbT` → سبط (5) / `sbt` → سبت (9) |
| `sed` | `SEd` → صعد (9) / `sEd` → سعد (2) |
| `xms` | `xmS` → خمص (2) / `xms` → خمس (8) |
| `slb` | `Slb` → صلب (8) / `slb` → سلب (1) |
| `frt` | `frT` → فرط (8) / `frt` → فرت (3) |
| `xsf` | `xSf` → خصف (2) / `xsf` → خسف (8) |
| `swt` | `Swt` → صوت (8) / `swT` → سوط (1) |
| `qsw` | `qSw` → قصو (5) / `qsw` → قسو (7) |
| `bde` | `bDE` → بضع (7) / `bdE` → بدع (4) |
| `srh` | `SrH` → صرح (4) / `srH` → سرح (7) |
| `nsf` | `nSf` → نصف (7) / `nsf` → نسف (5) |
| `hzz` | `HZZ` → حظظ (7) / `hzz` → هزز (5) |
| `dhw` | `DHw` → ضحو (7) / `dHw` → دحو (1) |
| `ndd` | `nDd` → نضد (3) / `ndd` → ندد (6) |
| `asr` | `ASr` → اصر (3) / `Asr` → اسر (6) |
| `hsd` | `HSd` → حصد (6) / `Hsd` → حسد (5) |
| `hmr` | `Hmr` → حمر (6) / `hmr` → همر (1) |
| `mhl` | `mHl` → محل (1) / `mhl` → مهل (6) |
| `htm` | `HTm` → حطم (6) / `Htm` → حتم (1) |
| `xde` | `xDE` → خضع (2) / `xdE` → خدع (5) |
| `hrs` | `HrS` → حرص (5) / `Hrs` → حرس (1) |
| `qtr` | `qTr` → قطر (5) / `qtr` → قتر (5) |
| `snm` | `Snm` → صنم (5) / `snm` → سنم (1) |
| `qdd` | `qDD` → قضض (1) / `qdd` → قدد (5) |
| `$tt` | `$TT` → شطط (3) / `$tt` → شتت (5) |
| `hyd` | `HyD` → حيض (4) / `Hyd` → حيد (1) |
| `dhr` | `dHr` → دحر (4) / `dhr` → دهر (2) |
| `slsl` | `SlSl` → صلصل (4) / `slsl` → سلسل (3) |
| `sfn` | `Sfn` → صفن (1) / `sfn` → سفن (4) |
| `mhn` | `mHn` → محن (2) / `mhn` → مهن (4) |
| `sbg` | `Sbg` → صبغ (3) / `sbg` → سبغ (2) |
| `xbt` | `xbT` → خبط (1) / `xbt` → خبت (3) |
| `fzz` | `fZZ` → فظظ (1) / `fzz` → فزز (3) |
| `hrd` | `HrD` → حرض (3) / `Hrd` → حرد (1) |
| `zfr` | `Zfr` → ظفر (2) / `zfr` → زفر (3) |
| `nks` | `nkS` → نكص (2) / `nks` → نكس (3) |
| `rkd` | `rkD` → ركض (3) / `rkd` → ركد (1) |
| `wtr` | `wTr` → وطر (2) / `wtr` → وتر (3) |
| `fsh` | `fSH` → فصح (1) / `fsH` → فسح (3) |
| `bsl` | `bSl` → بصل (1) / `bsl` → بسل (2) |
| `sdy` | `Sdy` → صدي (2) / `sdy` → سدي (1) |
| `btr` | `bTr` → بطر (2) / `btr` → بتر (1) |
| `hdm` | `hDm` → هضم (2) / `hdm` → هدم (1) |
| `etl` | `ETl` → عطل (2) / `Etl` → عتل (2) |
| `rss` | `rSS` → رصص (1) / `rss` → رسس (2) |
| `xdd` | `xDd` → خضد (1) / `xdd` → خدد (2) |
| `tll` | `Tll` → طلل (1) / `tll` → تلل (1) |
| `shl` | `sHl` → سحل (1) / `shl` → سهل (1) |
| `wtn` | `wTn` → وطن (1) / `wtn` → وتن (1) |
| `wfd` | `wfD` → وفض (1) / `wfd` → وفد (1) |
| `smd` | `Smd` → صمد (1) / `smd` → سمد (1) |

Of particular note: `ESy` (عصي, disobedience, 32 occ.) vs `Esy` (عسي, 'perhaps', 30 occ.) — flagged in cluster-90 analysis as easy to confuse.

### Roots with missing lemma Arabic forms

_None found in the top-3 lemmas of any root._

### Roots missing from clusters.json

_All 1,642 roots are assigned to a cluster — no inconsistency between roots.json and clusters.json._

### Cluster size vs. listed members

_No mismatches — every cluster's `size` field matches its member list._

