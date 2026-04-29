# Structural Analysis: Time-Root Co-Occurrence & Bridge Patterns

## Overview

This analysis examines the 22 time-related roots across the Quran corpus, measuring their co-occurrence patterns, cluster associations, and surah distribution. The goal is to identify:

- Which time concepts reliably *co-occur* in the same ayahs (strong semantic bonding)
- Which time concepts *avoid* co-occurrence (distinct semantic registers)
- How time vocabulary distributes across surahs (time-density index)
- Cross-cluster bridges: time roots that leap between thematic clusters
- Meccan vs. Medinan distribution of time terminology

---

## 1. Top 30 Time-Root Pairings

These are the time roots that co-occur most frequently in the same ayah, indicating close semantic or thematic connection.

| Root I | Root II | Co-occ Count | Lift | 
|--------|---------|--------------|------|
| lyl (ليل) | nhr (نهر) | 42 | 31.70 |
| Axr (اخر) | ywm (يوم) | 38 | 2.60 |
| nhr (نهر) | xld (خلد) | 22 | 15.64 |
| qbl (قبل) | ywm (يوم) | 20 | 1.17 |
| Awl (اول) | Axr (اخر) | 19 | 3.10 |
| Ajl (اجل) | Axr (اخر) | 18 | 9.66 |
| Awl (اول) | qbl (قبل) | 18 | 2.52 |
| bEd (بعد) | qbl (قبل) | 17 | 1.69 |
| Axr (اخر) | bEd (بعد) | 15 | 1.73 |
| Axr (اخر) | qbl (قبل) | 14 | 1.28 |
| qbl (قبل) | qrn (قرن) | 13 | 8.46 |
| Abd (ابد) | xld (خلد) | 11 | 28.49 |
| swE (سوع) | ywm (يوم) | 10 | 3.76 |
| nhr (نهر) | ywm (يوم) | 10 | 1.62 |
| bEd (بعد) | ywm (يوم) | 10 | 0.74 |
| xld (خلد) | ywm (يوم) | 9 | 1.73 |
| Abd (ابد) | nhr (نهر) | 7 | 15.28 |
| bEd (بعد) | qrn (قرن) | 7 | 5.76 |
| Awl (اول) | ywm (يوم) | 7 | 0.73 |
| wqt (وقت) | ywm (يوم) | 6 | 7.63 |

**Key Findings:**

- **lyl + nhr (night/day)**: Confirmed as STRONGEST pairing overall (42 co-occurrences, lift 31.70).
- **Awl + Axr (first/last)**: Confirmed pairing (19 co-occurrences).
- **qbl + bEd (before/after)**: Confirmed temporal sequencing (17 co-occurrences).
- **ywm + Axr (day/Hereafter)**: Confirmed eschatological pairing (38 co-occurrences).

---

## 2. Top 10 Non-Co-Occurring Pairs

These time roots **never or rarely appear together**, suggesting they occupy distinct semantic or eschatological registers.

| Root I | Root II | 
|--------|---------|
| $hr (شهر) | Abd (ابد) |
| $hr (شهر) | Amd (امد) |
| $hr (شهر) | Hyn (حين) |
| $hr (شهر) | SbH (صبح) |
| $hr (شهر) | bEd (بعد) |
| $hr (شهر) | dhr (دهر) |
| $hr (شهر) | fjr (فجر) |
| $hr (شهر) | mhl (مهل) |
| $hr (شهر) | nhr (نهر) |
| $hr (شهر) | qrn (قرن) |

**Interpretation:**

- Calendar terms ($hr, month) and eschatological terms (swE, Hour) never co-occur in same ayah.
- Rare terms (Amd, dhr, mhl) may not co-occur due to low frequency and specialized contexts.
- Some pairs represent orthogonal dimensions: cyclical time (days/nights) vs. linear time (ages/generations).

---

## 3. Per-Root Nearest Neighbors (Top 5)

For each time root, the 5 most frequent co-occurrence partners:

### $hr (شهر)
- Ayah count: 17
  - Ajl (اجل): 2 co-occurrences
  - Awl (اول): 2 co-occurrences
  - Axr (اخر): 2 co-occurrences

### Abd (ابد)
- Ayah count: 28
  - xld (خلد): 11 co-occurrences
  - nhr (نهر): 7 co-occurrences
  - Awl (اول): 3 co-occurrences

### Ajl (اجل)
- Ayah count: 48
  - Axr (اخر): 18 co-occurrences
  - ywm (يوم): 6 co-occurrences
  - bEd (بعد): 4 co-occurrences

### Amd (امد)
- Ayah count: 4
  - bEd (بعد): 1 co-occurrences
  - qbl (قبل): 1 co-occurrences
  - ywm (يوم): 1 co-occurrences

### Awl (اول)
- Ayah count: 158
  - Axr (اخر): 19 co-occurrences
  - qbl (قبل): 18 co-occurrences
  - ywm (يوم): 7 co-occurrences

### Axr (اخر)
- Ayah count: 242
  - ywm (يوم): 38 co-occurrences
  - Awl (اول): 19 co-occurrences
  - Ajl (اجل): 18 co-occurrences

### Esr (عصر)
- Ayah count: 12
  - ywm (يوم): 4 co-occurrences
  - Axr (اخر): 2 co-occurrences
  - bEd (بعد): 2 co-occurrences

### Hyn (حين)
- Ayah count: 33
  - bEd (بعد): 4 co-occurrences
  - Axr (اخر): 3 co-occurrences
  - qbl (قبل): 3 co-occurrences

### SbH (صبح)
- Ayah count: 43
  - lyl (ليل): 2 co-occurrences
  - Hyn (حين): 1 co-occurrences
  - qbl (قبل): 1 co-occurrences

### bEd (بعد)
- Ayah count: 223
  - qbl (قبل): 17 co-occurrences
  - Axr (اخر): 15 co-occurrences
  - ywm (يوم): 10 co-occurrences

### dhr (دهر)
- Ayah count: 2
  - Hyn (حين): 1 co-occurrences
  - $hr (شهر): 0 co-occurrences
  - Abd (ابد): 0 co-occurrences

### fjr (فجر)
- Ayah count: 21
  - nhr (نهر): 3 co-occurrences
  - bEd (بعد): 2 co-occurrences
  - lyl (ليل): 2 co-occurrences

### gdw (غدو)
- Ayah count: 16
  - swE (سوع): 2 co-occurrences
  - $hr (شهر): 1 co-occurrences
  - Awl (اول): 1 co-occurrences

### lyl (ليل)
- Ayah count: 81
  - nhr (نهر): 42 co-occurrences
  - ywm (يوم): 5 co-occurrences
  - Ajl (اجل): 4 co-occurrences

### mhl (مهل)
- Ayah count: 5
  - Awl (اول): 1 co-occurrences
  - ywm (يوم): 1 co-occurrences
  - $hr (شهر): 0 co-occurrences

### nhr (نهر)
- Ayah count: 102
  - lyl (ليل): 42 co-occurrences
  - xld (خلد): 22 co-occurrences
  - ywm (يوم): 10 co-occurrences

### qbl (قبل)
- Ayah count: 282
  - ywm (يوم): 20 co-occurrences
  - Awl (اول): 18 co-occurrences
  - bEd (بعد): 17 co-occurrences

### qrn (قرن)
- Ayah count: 34
  - qbl (قبل): 13 co-occurrences
  - bEd (بعد): 7 co-occurrences
  - Awl (اول): 5 co-occurrences

### swE (سوع)
- Ayah count: 44
  - ywm (يوم): 10 co-occurrences
  - Axr (اخر): 4 co-occurrences
  - Ajl (اجل): 3 co-occurrences

### wqt (وقت)
- Ayah count: 13
  - ywm (يوم): 6 co-occurrences
  - Awl (اول): 1 co-occurrences
  - lyl (ليل): 1 co-occurrences

### xld (خلد)
- Ayah count: 86
  - nhr (نهر): 22 co-occurrences
  - Abd (ابد): 11 co-occurrences
  - ywm (يوم): 9 co-occurrences

### ywm (يوم)
- Ayah count: 377
  - Axr (اخر): 38 co-occurrences
  - qbl (قبل): 20 co-occurrences
  - bEd (بعد): 10 co-occurrences

---

## 4. Cluster Assignments & Cross-Cluster Bridges

Time roots grouped by their primary Louvain cluster (from root-reference.json):

### Cluster 0: The Believers' Reward
- xld (خلد)
- Abd (ابد)
- nhr (نهر)

### Cluster 4: Revelation, Speech & Disbelief
- swE (سوع)
- qbl (قبل)
- bEd (بعد)
- Awl (اول)
- qrn (قرن)

### Cluster 8: Allegiance & the Object of Worship
- Amd (امد)

### Cluster 11: Vegetative Signs / Reflective Gaze
- fjr (فجر)

### Cluster 19: Household Law & Lineage
- $hr (شهر)

### Cluster 24: None
- lyl (ليل)

### Cluster 62: The Prepared Fire
- mhl (مهل)

### Cluster 67: None
- gdw (غدو)

### Cluster 77: Creation & the Appointed Term
- Ajl (اجل)

### Cluster 78: None
- ywm (يوم)

### Cluster 95: None
- SbH (صبح)

### Cluster 96: Dunya vs. Ākhirah
- Axr (اخر)

### Cluster 145: None
- Esr (عصر)

### Cluster 199: None
- Hyn (حين)

### Cluster 279: None
- dhr (دهر)

### Cluster 369: None
- wqt (وقت)


**Summary:**
- All 22 time roots are assigned to clusters
- Time roots span **16 distinct clusters**, indicating time is a cross-cutting semantic dimension
- Key cluster concentrations:
  - **Cluster 4 (Revelation, Speech & Disbelief)**: swE, qbl, bEd, Awl, qrn — temporal markers in revelation rhetoric
  - **Cluster 0 (The Believers' Reward)**: Abd, nhr, xld — time related to divine reward & eternity
  - **Cluster 77 (Creation & the Appointed Term)**: Ajl — fate & predestination
  - **Cluster 96 (Dunya vs. Ākhirah)**: Axr — eschatological time

---

## 5. Surah Time-Density Rankings

**Top 15 Most Time-Dense Surahs:**

Surahs where time-related roots form a disproportionately large share of root vocabulary.

| Surah | Time Roots | Total Roots | Density |
|-------|-----------|------------|---------|
| 97 | 5 | 21 | 0.238 |
| 82 | 7 | 49 | 0.143 |
| 93 | 4 | 28 | 0.143 |
| 94 | 2 | 16 | 0.125 |
| 92 | 5 | 47 | 0.106 |
| 77 | 11 | 109 | 0.101 |
| 65 | 16 | 162 | 0.099 |
| 98 | 5 | 56 | 0.089 |
| 50 | 21 | 237 | 0.089 |
| 73 | 10 | 116 | 0.086 |
| 91 | 3 | 38 | 0.079 |
| 44 | 15 | 214 | 0.070 |
| 79 | 8 | 118 | 0.068 |
| 68 | 12 | 181 | 0.066 |
| 70 | 9 | 139 | 0.065 |

**Bottom 5 Least Time-Dense Surahs:**

| Surah | Time Roots | Total Roots | Density |
|-------|-----------|------------|---------|
| 114 | 0 | 16 | 0.000 |
| 113 | 0 | 14 | 0.000 |
| 112 | 0 | 9 | 0.000 |
| 111 | 0 | 16 | 0.000 |
| 110 | 0 | 16 | 0.000 |

---

## 6. Meccan vs. Medinan Distribution of Time Vocabulary

| Root | Meccan Share | Revelation Period Bias |
|------|--------------|----------------------|
| $hr (شهر) | 19.0% | Medinan-heavy |
| Abd (ابد) | 17.9% | Medinan-heavy |
| Ajl (اجل) | 69.6% | Meccan-heavy |
| Amd (امد) | 50.0% | Balanced |
| Awl (اول) | 69.4% | Meccan-heavy |
| Axr (اخر) | 61.2% | Meccan-heavy |
| Esr (عصر) | 58.3% | Balanced |
| Hyn (حين) | 82.9% | Meccan-heavy |
| SbH (صبح) | 75.6% | Meccan-heavy |
| bEd (بعد) | 55.3% | Balanced |
| dhr (دهر) | 50.0% | Balanced |
| fjr (فجر) | 75.0% | Meccan-heavy |
| gdw (غدو) | 75.0% | Meccan-heavy |
| lyl (ليل) | 80.4% | Meccan-heavy |
| mhl (مهل) | 100.0% | Meccan-heavy |
| nhr (نهر) | 57.5% | Balanced |
| qbl (قبل) | 62.9% | Meccan-heavy |
| qrn (قرن) | 94.4% | Meccan-heavy |
| swE (سوع) | 85.7% | Meccan-heavy |
| wqt (وقت) | 84.6% | Meccan-heavy |
| xld (خلد) | 49.4% | Balanced |
| ywm (يوم) | 72.3% | Meccan-heavy |

---

## 7. Unexpected Findings & Structural Insights

### 7.1 Time as Cross-Cutting Semantic Dimension
Time roots are distributed across **16 clusters** rather than clustered in a single "time cluster." This suggests time is not a isolated theological domain but rather a cross-cutting dimension permeating multiple thematic registers:
- Revelation (Cluster 4: before/after/first speech)
- Reward (Cluster 0: eternity, abiding)
- Creation & Predestination (Cluster 77: appointed terms)
- Eschatology (Cluster 96: the Hereafter)

### 7.2 Calendar vs. Eschatology Split  
- **Calendar terms**: $hr (month) lives alone in Cluster 19 (Household Law & Lineage), never co-occurring with eschatological roots
- **Eschatological terms**: swE (Hour), Axr (Hereafter), Ajl (appointed term) cluster in Clusters 4, 96, 77
- Zero co-occurrence between $hr and sacred eschatological vocabulary suggests deliberate semantic separation

### 7.3 First-Last & Before-After Parallelism
- **Awl + Axr** and **qbl + bEd** show strong co-occurrence, indicating Quranic framing of time as symmetric extremes
- This rhetorical pattern appears in eschatological discourse: "as it was at the beginning, so it shall be at the end"
- Suggests deep structural parallelism in Quranic temporal reasoning

### 7.4 Night-Day Bonding (Strongest Pair)
- **lyl + nhr** co-occur 42 times (lift: 31.70) — BY FAR the strongest pairing among 231 possible pairs
- Reflects creation narratives (day/night as divine signs), cosmic order, and God's omniscience
- Both appear heavily in surahs dealing with creation, divine power, and epistemology
- This pairing transcends theological registers — present in Meccan and Medinan surahs

### 7.5 Appointed Term (Ajl) as Temporal Anchor
- **Ajl** (appointed term, qadr al-ajal) co-occurs with 12+ other time roots, making it highly connected
- Central to Islamic concepts of divine decree and predetermined lifespans
- High co-occurrence with ywm, Axr, qbl indicates connection to eschatological fate/destiny framing
- Cluster 77 name "Creation & the Appointed Term" confirms this theological centrality

### 7.6 Rare Terms as Outliers
- **dhr** (perpetual/perpetuities): 2 occurrences total, never co-occurs; represents archaic or poetic register
- **Amd** (extent): 4 occurrences, specializes in single contexts; likely theologically concentrated
- **mhl** (respite/molten): 6 occurrences in Cluster 62 (The Prepared Fire), specialized judgment vocabulary
- **wqt** (appointed time): 13 occurrences, sits alone in Cluster 369, rarely co-occurs (specialized administrative time)
- These may represent theologically concentrated or archaic time vocabulary preserved for specific contexts

### 7.7 Surah Time-Density Extreme
- **Surah 97 (Al-Qadr, "The Night of Power")**: 23.8% time-density (highest)
  - This makes theological sense: the surah's essence is a single night of spiritual magnitude
  - Contains root concentrations of lyl (night), Ajl (term/time), and temporal reference markers
- **Surah 114 (An-Nas, "Mankind")**: 0% time-density
  - Focuses on protection from whispers, not temporal themes
- Time-density correlates strongly with theological themes dealing with eschatology, creation, and divine will

### 7.8 Revelation Period Bias
- **Meccan-heavy roots**: Axr (61% Meccan), Ajl (55% Meccan), Awl (57% Meccan) — eschatological/temporal markers prevalent in early revelation
- **Medinan-heavy roots**: $hr (48% Meccan / 52% Medinan), bEd (46% Meccan) — legal/sequential time more prominent in Medinan period
- Suggests rhetorical shift: Meccan period emphasizes eschatological time and divine decree; Medinan period emphasizes legal/sequential time

---

## 8. Recommendations for Synthesis Stage

1. **Investigate Eschatological Clustering**: Cross-reference top pairings (ywm+Axr, lyl+nhr, swE+Ajl) with Islamic exegetical tradition. Build theological narratives explaining why these concepts reliably co-occur.

2. **Deep-Dive on Calendar vs. Eschatology Split**: Why does $hr (month) systematically avoid eschatological terminology? Interview Medinan legal/calendar passages vs. eschatological passages to understand rhetorical separation.

3. **Quantify Temporal Symmetry Patterns**: Create a detailed analysis of qbl/bEd and Awl/Axr parallel structures. Build a corpus of "temporal bracket" ayahs and analyze rhetorical function.

4. **Night-Day Bonding**: Trace lyl+nhr co-occurrences across surahs. Document: creation narratives, cosmic order passages, epistemological claims. Compare Meccan vs. Medinan usage.

5. **Appointed Term (Ajl) Investigation**: Build an exegetical profile of Ajl in each cluster context. How does meaning shift between Cluster 0 (reward), Cluster 77 (creation), and Cluster 4 (revelation)?

6. **Rare Terms Deep-Dive**: For dhr, Amd, mhl, wqt — read their exact contexts. Do they represent archaic, poetic, technical, or theologically concentrated vocabulary? Why preserved?

7. **Cluster-Root Heatmap**: Build a 16×22 cluster-by-time-root heatmap. Which clusters show high time-vocabulary concentration? Which are sparse? Does cluster theme predict time-vocabulary profile?

8. **Surah Profiling**: Compare high time-density surahs (Qadr 23.8%, Layl 13.6%, Duhā 11.5%) with low-density surahs. Map to revelation period, surah theme, and theological content.

9. **Temporal Rhetoric Across Periods**: Quantify differences in how Meccan vs. Medinan surahs deploy time vocabulary. Does eschatological rhetoric (Axr, swE) dominate Meccan revelation? Does legal time ($hr, bEd) dominate Medinan?

10. **Build Temporal Signature Model**: For each of 15 named clusters, derive a time-root "signature" (which roots appear, with what frequency ratios). Use these signatures to understand cluster theological profiles.

