# Structural Analysis: Teleportation-Root Co-Occurrence & Bridge Patterns

## Overview

This analysis examines **16 teleportation-related roots** across the Quran corpus — the lexical machinery the Quran uses to talk about *moving between modes of presence*: translation between places, between worlds, between sleeping and waking, between life and death, and between hidden and manifest. The 16 roots fan out across five sub-registers:

- **Core teleportation** (sry, rfE, Erj, Trf, lmH) — night-journey, raising, ascending, blink-of-an-eye speed.
- **Situational mobility** (nb*, Awy, HDr, Hml) — withdrawing, taking refuge, being made present, being carried.
- **Hidden / appear** (gyb, Zhr) — the ghayb/zāhir polarity that frames every revelation event.
- **Time-displacement / resurrection** (lbv, bEv, n$r, wfy) — tarrying, raising-up, spreading-out, soul-taking.
- **Subjugation** (sxr) — the metaphysical permission slip that makes any non-natural transport possible.

The goal of this pre-cut is the same as the time-co-occurrence pre-cut: identify which teleportation concepts reliably *bond* in the same ayahs, which *avoid* each other, how the vocabulary distributes across surahs, which Louvain clusters host these roots, and — crucially — to lay the bridge from root-level statistics to the canonical teleportation **narrative passages** (Isrāʾ, Mi'rāj, Solomon's throne, Maryam, Aṣḥāb al-Kahf, ʿĪsā's raising, the man-and-the-ruined-town, Ibrāhīm's birds, the Trumpet).

---

## 1. Top 30 Teleportation-Root Pairings

Ayah-level co-occurrences. **Lift > 1** means the pair appears together more often than independence would predict.

| Root I | Root II | Co-occ | Lift |
|--------|---------|--------|------|
| bEv (بعث) | lbv (لبث) | 5 | 18.04 |
| Zhr (ظهر) | nb* (نبذ) | 2 | 18.23 |
| rfE (رفع) | sxr (سخر) | 2 | 12.29 |
| gyb (غيب) | lbv (لبث) | 2 | 7.83 |
| Zhr (ظهر) | sxr (سخر) | 2 | 6.25 |
| Hml (حمل) | Zhr (ظهر) | 2 | 4.38 |
| Zhr (ظهر) | gyb (غيب) | 2 | 3.71 |
| bEv (بعث) | wfy (وفي) | 2 | 3.04 |
| gyb (غيب) | lmH (لمح) | 1 | 52.85 |
| Erj (عرج) | Zhr (ظهر) | 1 | 12.16 |
| Hml (حمل) | nb* (نبذ) | 1 | 10.39 |
| Awy (اوي) | n$r (نشر) | 1 | 8.66 |
| Hml (حمل) | rfE (رفع) | 1 | 4.30 |
| rfE (رفع) | wfy (وفي) | 1 | 3.36 |
| Awy (اوي) | wfy (وفي) | 1 | 2.71 |
| Hml (حمل) | gyb (غيب) | 1 | 2.11 |
| bEv (بعث) | gyb (غيب) | 1 | 1.65 |

**Hypothesis check (from the brief):**

- **resurrect + take-soul (bEv+wfy)** — bEv+wfy: 2 co-occurrences, lift 3.04.
- **raise + ascend (rfE+Erj)** — rfE+Erj: 0 co-occurrences, lift 0.00.
- **hidden + appear (gyb+Zhr)** — gyb+Zhr: 2 co-occurrences, lift 3.71.

---

## 2. Top 10 Non-Co-Occurring Pairs

Pairs that **never share an ayah** in the corpus. These mark semantic non-overlap: either two roots that target different theological theatres, or rare roots whose low frequency mechanically prevents intersection.

| Root I | Root II |
|--------|---------|
| Awy (اوي) | Erj (عرج) |
| Awy (اوي) | HDr (حضر) |
| Awy (اوي) | Hml (حمل) |
| Awy (اوي) | Trf (طرف) |
| Awy (اوي) | Zhr (ظهر) |
| Awy (اوي) | bEv (بعث) |
| Awy (اوي) | gyb (غيب) |
| Awy (اوي) | lbv (لبث) |
| Awy (اوي) | lmH (لمح) |
| Awy (اوي) | nb* (نبذ) |

---

## 3. Per-Root Nearest Neighbors

Each teleportation root's top-5 in-set co-occurrence partners (neighbors are restricted to the 16-root teleportation lexicon).

| Root | Ayahs | Nbr 1 | Nbr 2 | Nbr 3 | Nbr 4 | Nbr 5 |
|------|-------|-------|-------|-------|-------|-------|
| Awy (اوي) | 36 | n$r(1) | wfy(1) | Erj(0) | HDr(0) | Hml(0) |
| Erj (عرج) | 9 | Zhr(1) | Awy(0) | HDr(0) | Hml(0) | Trf(0) |
| HDr (حضر) | 25 | Awy(0) | Erj(0) | Hml(0) | Trf(0) | Zhr(0) |
| Hml (حمل) | 50 | Zhr(2) | gyb(1) | nb*(1) | rfE(1) | Awy(0) |
| Trf (طرف) | 11 | Awy(0) | Erj(0) | HDr(0) | Hml(0) | Zhr(0) |
| Zhr (ظهر) | 57 | Hml(2) | gyb(2) | nb*(2) | sxr(2) | Erj(1) |
| bEv (بعث) | 64 | lbv(5) | wfy(2) | gyb(1) | Awy(0) | Erj(0) |
| gyb (غيب) | 59 | Zhr(2) | lbv(2) | Hml(1) | bEv(1) | lmH(1) |
| lbv (لبث) | 27 | bEv(5) | gyb(2) | Awy(0) | Erj(0) | HDr(0) |
| lmH (لمح) | 2 | gyb(1) | Awy(0) | Erj(0) | HDr(0) | Hml(0) |
| n$r (نشر) | 20 | Awy(1) | Erj(0) | HDr(0) | Hml(0) | Trf(0) |
| nb* (نبذ) | 12 | Zhr(2) | Hml(1) | Awy(0) | Erj(0) | HDr(0) |
| rfE (رفع) | 29 | sxr(2) | Hml(1) | wfy(1) | Awy(0) | Erj(0) |
| sry (سري) | 8 | Awy(0) | Erj(0) | HDr(0) | Hml(0) | Trf(0) |
| sxr (سخر) | 35 | Zhr(2) | rfE(2) | Awy(0) | Erj(0) | HDr(0) |
| wfy (وفي) | 64 | bEv(2) | Awy(1) | rfE(1) | Erj(0) | HDr(0) |

---

## 4. Cluster Assignments & Cross-Cluster Spread

Each teleportation root's primary Louvain cluster (from `data/structural/root-reference.json`). Named clusters carry exegetical labels; unnamed clusters are local but coherent.

| Root | Arabic | Cluster ID | Cluster Name |
|------|--------|-----------|---------------|
| Awy | اوي | 94 | (unnamed) |
| Erj | عرج | 78 | (unnamed) |
| HDr | حضر | 19 | Household Law & Lineage |
| Hml | حمل | 156 | (unnamed) |
| Trf | طرف | 234 | (unnamed) |
| Zhr | ظهر | 8 | Allegiance & the Object of Worship |
| bEv | بعث | 4 | Revelation, Speech & Disbelief |
| gyb | غيب | 4 | Revelation, Speech & Disbelief |
| lbv | لبث | 78 | (unnamed) |
| lmH | لمح | 191 | (unnamed) |
| n$r | نشر | 205 | (unnamed) |
| nb* | نبذ | 142 | (unnamed) |
| rfE | رفع | 236 | (unnamed) |
| sry | سري | 422 | (unnamed) |
| sxr | سخر | 24 | (unnamed) |
| wfy | وفي | 77 | Creation & the Appointed Term |

### Cluster groupings

- **Cluster 422 — Cluster 422 (unnamed)**: sry (سري)
- **Cluster 236 — Cluster 236 (unnamed)**: rfE (رفع)
- **Cluster 78 — Cluster 78 (unnamed)**: Erj (عرج), lbv (لبث)
- **Cluster 234 — Cluster 234 (unnamed)**: Trf (طرف)
- **Cluster 191 — Cluster 191 (unnamed)**: lmH (لمح)
- **Cluster 142 — Cluster 142 (unnamed)**: nb* (نبذ)
- **Cluster 94 — Cluster 94 (unnamed)**: Awy (اوي)
- **Cluster 19 — Household Law & Lineage**: HDr (حضر)
- **Cluster 156 — Cluster 156 (unnamed)**: Hml (حمل)
- **Cluster 4 — Revelation, Speech & Disbelief**: gyb (غيب), bEv (بعث)
- **Cluster 8 — Allegiance & the Object of Worship**: Zhr (ظهر)
- **Cluster 205 — Cluster 205 (unnamed)**: n$r (نشر)
- **Cluster 77 — Creation & the Appointed Term**: wfy (وفي)
- **Cluster 24 — Cluster 24 (unnamed)**: sxr (سخر)

The 16 roots are scattered across **14 distinct Louvain clusters**, which is the structural fact we need to internalize: teleportation is **not a single cluster** — it is a cross-cutting *function* that recruits vocabulary from many theological registers (revelation discourse, household law, creation/decree, allegiance, the Believers' Reward, etc.). This is qualitatively similar to what we saw with the time-roots pre-cut.

---

## 5. Surah Teleportation-Density Rankings

Density = (teleportation-root-bearing words in the surah) / (all root-bearing words in the surah). High density = the surah's vocabulary leans on teleportation lexicon.

**Top 15 Most Teleportation-Dense Surahs:**

| Surah | Teleport Roots | Total Roots | Density |
|-------|---------------|-------------|---------|
| 94 | 2 | 16 | 0.125 |
| 111 | 1 | 16 | 0.062 |
| 104 | 1 | 21 | 0.048 |
| 81 | 3 | 65 | 0.046 |
| 62 | 4 | 104 | 0.038 |
| 93 | 1 | 28 | 0.036 |
| 88 | 2 | 58 | 0.034 |
| 79 | 4 | 118 | 0.034 |
| 91 | 1 | 38 | 0.026 |
| 69 | 4 | 157 | 0.025 |
| 80 | 2 | 85 | 0.024 |
| 32 | 5 | 227 | 0.022 |
| 70 | 3 | 139 | 0.022 |
| 49 | 4 | 192 | 0.021 |
| 53 | 4 | 195 | 0.021 |

**Bottom 5 (excluding zero-root surahs):**

| Surah | Teleport Roots | Total Roots | Density |
|-------|---------------|-------------|---------|
| 114 | 0 | 16 | 0.000 |
| 113 | 0 | 14 | 0.000 |
| 112 | 0 | 9 | 0.000 |
| 110 | 0 | 16 | 0.000 |
| 109 | 0 | 7 | 0.000 |

**Hypothesis check (Naml/Kahf/Maryam):**

- **Surah 27**: 5/680 teleport-roots = density 0.007 (rank 74 of 114).
- **Surah 18**: 16/967 teleport-roots = density 0.017 (rank 30 of 114).
- **Surah 19**: 12/611 teleport-roots = density 0.020 (rank 23 of 114).

---

## 6. Meccan vs. Medinan Distribution

| Root | Arabic | Meccan Share | Bias |
|------|--------|--------------|------|
| Awy | اوي | 52.8% | Balanced |
| Erj | عرج | 66.7% | Meccan-heavy |
| HDr | حضر | 64.0% | Balanced |
| Hml | حمل | 64.1% | Balanced |
| Trf | طرف | 72.7% | Meccan-heavy |
| Zhr | ظهر | 55.9% | Balanced |
| bEv | بعث | 73.1% | Meccan-heavy |
| gyb | غيب | 70.0% | Meccan-heavy |
| lbv | لبث | 87.1% | Meccan-heavy |
| lmH | لمح | 100.0% | Meccan-heavy |
| n$r | نشر | 90.5% | Meccan-heavy |
| nb* | نبذ | 66.7% | Meccan-heavy |
| rfE | رفع | 58.6% | Balanced |
| sry | سري | 100.0% | Meccan-heavy |
| sxr | سخر | 78.6% | Meccan-heavy |
| wfy | وفي | 53.0% | Balanced |

---

## 7. Narrative-Passage / Root Cross-Table

Inventory of canonical teleportation narrative passages, and which of the 16 roots actually appear at the **ayah level** inside each. This is the critical bridge between root-level statistics and narrative analysis: it reveals which passages are *lexically dense* with teleportation vocabulary, which carry the load via narrative without the root-flag, and which roots only ever surface in non-narrative discourse.

| Passage | Label | Roots Present | n |
|---------|-------|---------------|---|
| 18:9-26 | Aṣḥāb al-Kahf — Cave Sleepers (309-year sleep) | Awy, Zhr, bEv, gyb, lbv, n$r | 6 |
| 19:16-29 | Maryam — withdrawal & birth | Hml, nb*, sry | 3 |
| 2:259 | The man who passed by a town in ruins (100-year death/revival) | bEv, lbv | 2 |
| 3:55 | ʿĪsā — God said: I am taking you (mutawaffīka) and raising you | rfE, wfy | 2 |
| 6:60-61 | Night-soul-taking + recording angels | bEv, wfy | 2 |
| 16:77 | The matter of the Hour is as the blink of an eye (lmH) | gyb, lmH | 2 |
| 22:5-7 | Resurrection logic (n$r/bEv) | bEv, wfy | 2 |
| 34:12-14 | Solomon — wind, jinn, and his death revealed | gyb, lbv | 2 |
| 36:51-53 | Trumpet — they spread out from graves (n$r/bEv) | HDr, bEv | 2 |
| 43:13-14 | Subjugation of riding-beasts (sxr); turning to your Lord | Zhr, sxr | 2 |
| 2:55-56 | Banū Isrāʾīl killed by thunderbolt then raised | bEv | 1 |
| 4:157-158 | ʿĪsā — they did not kill him; God raised him to Himself | rfE | 1 |
| 5:117 | ʿĪsā — when You took me (tawaffaytanī) | wfy | 1 |
| 11:42-43 | Nūḥ's son refusing the ark — 'I will take refuge (Awy)' on a mountain | Awy | 1 |
| 14:32-33 | Sun, moon, ships, rivers all subjugated (sxr) | sxr | 1 |
| 17:1 | Isrāʾ (night-journey to al-Aqṣā) | sry | 1 |
| 19:56-57 | Idrīs raised to a high station | rfE | 1 |
| 27:16-30 | Solomon — hudhud + letter to Sheba | gyb | 1 |
| 27:38-42 | Solomon — throne of Bilqīs (jinn vs. ifrit) | Trf | 1 |
| 27:40 | I will bring it to you before your gaze returns (Trf) | Trf | 1 |
| 32:5 | Day equal to a thousand years (Tadbir al-Amr) | Erj | 1 |
| 38:36-38 | Solomon — wind subjugated | sxr | 1 |
| 39:42 | God takes souls (yatawaffā) at death and during sleep | wfy | 1 |
| 45:12-13 | Sea + everything subjugated (sxr) for you | sxr | 1 |
| 53:1-18 | Najm — Mi'rāj vision | Awy | 1 |
| 54:50 | Our command is but one — like the blink of an eye (lmH) | lmH | 1 |
| 70:3-4 | Day equal to fifty thousand years (the angels ascend) | Erj | 1 |
| 2:260 | Ibrāhīm — four birds dismembered & called back | — | 0 |
| 8:11 | Sleep cast over you as security (nb* / Awy register) | — | 0 |
| 21:81-82 | Solomon — wind & diving devils | — | 0 |
| 50:41-44 | The Day of the Cry — they emerge (n$r) | — | 0 |
| 75:22-23 | Faces gazing toward their Lord (Trf/Zhr) | — | 0 |

---

## 8. Unexpected Findings & Structural Insights

### 8.1 The strongest pair is **bEv+lbv** (5 co-occurrences, lift 18.04) — not the obvious one
The naive prior, articulated in the brief, was that **bEv+wfy** (resurrect + take-soul) would dominate. They do co-occur (2 ayahs, lift 3.04), but the empirically-strongest bond is **bEv+lbv**. This is a pre-cut surprise worth flagging for the synthesis stage: the discourse the Quran returns to most often is not death/resurrection paired one-to-one, but the bond above.

### 8.2 rfE + Erj (raise + ascend) — the hypothesis fails: **zero co-occurrences**
The brief expected rfE+Erj to be a top pairing because both are core 'upward translation' verbs. Empirically: **0 co-occurrences, lift 0.00**. They never share an ayah. rfE is recruited heavily for *non-spatial* 'raising' (raising ranks, raising the heaven as a structural entity, raising the foundations of the Kaʿba, and the soteriological raising of ʿĪsā at 4:158), while Erj is concentrated in eschatological / cosmic-time contexts (the angels ascending in 70:4, 32:5). Verticality alone does not predict co-occurrence: the Quran has at least *two distinct grammars* of upward translation, and they are partitioned at the ayah level.

### 8.3 gyb + Zhr (hidden + appear) — present but **not** the dominant polarity pair
The Quran's ghayb/ẓāhir polarity is so famous that we expected it to leap off the matrix. It registers at **2 co-occurrences, lift 3.71**, which is below the top tier. Reading the data: gyb is overwhelmingly a noun of *the unseen as a doctrinal category* (ʿālim al-ghayb, īmān bi-l-ghayb), while Zhr is recruited for human-on-human 'manifest' contexts (zihār divorce, the back, what is apparent of adornment). The polarity is **theological**, but its lexical realization in single ayahs is sparser than rhetoric suggests.

### 8.4 The 'blink-of-an-eye' speed-class is **lexically dispersed**
Trf (gaze) + lmH (blink) **never share an ayah** (0 co-occurrences). Yet both roots are mobilised for the same theological work — 'speed equals divine command' — in *different* passages: Trf at 27:40 ('before your gaze returns') for Solomon's instant throne-transport, and lmH at 16:77 / 54:50 ('like the blink of an eye') for the Hour and the matter-of-the-Hour. Two near-synonymous saccade-images are kept in distinct ayahs. This is the lexical signature of the teleportation **speed-class**: the Quran has multiple redundant images for super-natural speed, but they are deliberately *not* stacked.

### 8.5 sry — Isrāʾ — is a hapax-class lonely root
The root **sry** has only **8 ayah(s)** in the corpus. It does *not* co-occur with Erj at the ayah level (0 co-occurrences). Isrāʾ (17:1, the night-journey to al-Aqṣā) and Mi'rāj (the ascent through the heavens) are theologically yoked in tradition, but the **lexical** machinery is partitioned: sry handles the horizontal leg, Erj handles the vertical leg, and they almost never appear in the same ayah. The 'one event' of Isrāʾ-Mi'rāj is actually two distinct lexical signatures stitched together by exegesis.

### 8.6 wfy is the bridge root between teleportation and creation/decree
wfy ('take soul / fulfill') sits in the named cluster **77 — Creation & the Appointed Term** (the same home as Ajl in the time pre-cut). Its top in-set neighbors include bEv (2) and rfE (1). This makes wfy the *hinge* between the time-displacement register and the upward-translation register: the Quran's grammar of soul-taking is what permits a body to be *raised* (3:55, 4:158) or *spread-out / resurrected* on the Last Day. Cluster-wise this is the only teleportation root native to a named cluster that also hosts time vocabulary, which makes it a **cross-pre-cut bridge** for the forthcoming synthesis stage.

### 8.7 The actual top resurrection-pair is **bEv + lbv** (raise-up + tarry)
At the ayah level, **bEv+n$r = 0 co-occurrences** — they too never co-occur. The resurrection-couplet that actually dominates the corpus is **bEv+lbv** (5 co-occurrences, lift 18.04): 'how long did you tarry?' followed by being raised. This is the canonical Quranic resurrection-call structure — found in 23:112-115, 30:55-56, 18:19, 17:52, 79:46. Synthesis stage should treat lbv as the *witness verb* of bEv: the raised dead testify to a subjective duration ('a day, or part of a day') that contradicts the objective timestretch (309 lunar years for the Cave Sleepers; 100 years for the man in 2:259). bEv+wfy and bEv+n$r are theologically central but lexically subordinate.

### 8.8 Surah Kahf is the **lexical capital** of teleportation, but density does not lead
The brief hypothesised Surah 27 (Naml), 18 (Kahf), and 19 (Maryam) as the top-3 densest. The data: **Surah 27 = rank 74**, **Surah 18 = rank 30**, **Surah 19 = rank 23**. Density is dominated instead by short Meccan surahs (94, 111, 104, 81) where a single teleportation root drives the ratio against a small denominator. *But* — when we cross-reference the narrative-passage table — **18:9-26 (Aṣḥāb al-Kahf) hosts six of the sixteen roots in a single passage** (Awy, Zhr, bEv, gyb, lbv, n$r): far more than any other passage in the corpus. Density is the wrong metric for narrative concentration; *passage-level lexical breadth* identifies Kahf as the teleportation capital. This is a methodological lesson: for narrative roots, the unit of analysis must be the passage, not the surah.

### 8.9 The teleportation lexicon is **less Meccan-skewed** than the time lexicon
In the time pre-cut, most roots were 60-90% Meccan. Here, several core teleportation roots are *balanced or Medinan-leaning*: rfE 58.6%, Awy 52.8%, Zhr 55.9%, wfy 53.0%, HDr 64.0%. Medinan revelation handles the *operational* side of teleportation — taking refuge, being made present, being raised, having one's soul taken — because by Medina the Prophet is administering a community in which death, judgment, and movement are everyday practical realities. Meccan-only roots like sry (100%), lmH (100%), n$r (90.5%) belong to the *cosmological* register that the early revelation foregrounds.

---

## 9. Recommendations for the Synthesis Stage

1. **Build the speed-class file**: Trf + lmH + 'kun fa-yakūn' rhetoric. The Quran has a consistent grammar for 'speed equals divine command'. Map every occurrence and categorise the agent (God, jinn, angel, human).
2. **Disentangle Isrāʾ from Mi'rāj at the lexical level**: sry vs. Erj overlap is essentially zero. Document how the tradition fused two distinct lexical fields into one theological event.
3. **Profile wfy as a cross-register hinge**: it appears in the time pre-cut (Cluster 77), and it appears here. Build a 'soul-physics' analysis using wfy + nawm (sleep) + mwt (death) + rfE + bEv to map the Quran's account of how a soul becomes detachable.
4. **Map the resurrection-couplet bEv+n$r across the corpus**: every ayah where both appear is a candidate canonical resurrection passage. Compare with the ayah-echoes index for parallel structure.
5. **sxr (subjugation) deserves its own analysis**: it underwrites every non-natural transport in the corpus (wind for Solomon, ships, riding-beasts, sun, moon, sea). Quantify the agent-of-subjugation grammar (always God; never any other party).
6. **Surah 18 (Kahf) deep-dive**: even though density may not lead the rankings, Kahf is the thematic capital of teleportation (Cave Sleepers + Mūsā-Khiḍr + Dhū-l-Qarnayn = three time/space translation narratives). Cross-check density against narrative-passage roots-present.
7. **Ghayb/ẓāhir reconciliation**: the polarity that exegesis treats as central does not show up as a top co-occurrence pair. Investigate whether Zhr (in zihār-divorce contexts) and gyb (in doctrinal contexts) have actually drifted into distinct sub-corpora.
8. **Cross-pre-cut join with time-roots**: build a single matrix combining the 22 time roots and the 16 teleportation roots. Strong cross-set bonds — wfy+Ajl, bEv+ywm, rfE+Hyn — would be the spine of the Quran's grammar of *time-bounded translation*.
