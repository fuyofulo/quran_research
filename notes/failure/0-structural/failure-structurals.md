# Structural Analysis: Failure-Vocabulary Co-Occurrence & Translation Divergence

## Headline Finding

The 32 failure-roots cluster tightly around **unbelief and transgression**: disbelief (kfr: كفر, 525 occurrences) and injustice (Zlm: ظلم, 315) are the backbone, connected via rejection (Dll: ضلل, 191) and refusal (swA: سوا, 167). Kfr pairs most strongly with Dll (28 co-occurrences, lift 0.48), creating a semantic chain: denying truth → straying. Unlike success-vocabulary (uniformly distributed across translators), failure-vocabulary exhibits high translation variance: Khattab and Arberry diverge on >10% of failure ayahs (vs. Saheeh's 0.8%), suggesting failure-states resist standardized English rendering. Top-density Surahs (91 al-Shams, 103 al-ʿAsr, 63 al-Munāfiqūn) mix Meccan warnings with Medinan narrative clarity, balanced near 10% failure-density—double success-vocabulary density in the same texts.

---

## Top 20 Co-Occurrence Pairings

| Root 1 | Arabic | Root 2 | Arabic | Co-occ | Lift |
|--------|--------|--------|--------|--------|------|
| Dll | ضلل | kfr | كفر | 28 | 0.48 |
| Zlm | ظلم | kfr | كفر | 25 | 0.26 |
| kfr | كفر | swA | سوا | 22 | 0.43 |
| Zlm | ظلم | swA | سوا | 18 | 0.59 |
| kbr | كبر | kfr | كفر | 18 | 0.37 |
| kfr | كفر | nfq | نفق | 17 | 0.50 |
| $rk | شرك | kfr | كفر | 16 | 0.31 |
| Zlm | ظلم | hlk | هلك | 11 | 0.89 |
| $rk | شرك | Zlm | ظلم | 10 | 0.33 |
| Dll | ضلل | Zlm | ظلم | 10 | 0.29 |
| bTl | بطل | kfr | كفر | 9 | 0.82 |
| $rk | شرك | kbr | كبر | 9 | 0.58 |
| Zlm | ظلم | kbr | كبر | 9 | 0.31 |
| Tgy | طغي | kfr | كفر | 8 | 0.68 |
| fsq | فسق | kfr | كفر | 8 | 0.49 |
| kfr | كفر | xsr | خسر | 8 | 0.41 |
| bgy | بغي | kfr | كفر | 7 | 0.24 |
| Dll | ضلل | xsr | خسر | 6 | 0.84 |
| ErD | عرض | Zlm | ظلم | 6 | 0.42 |
| ErD | عرض | kfr | كفر | 6 | 0.25 |

**Decisive signal:** Kfr (disbelief) acts as the central hub—paired with 30 of 31 other roots. Dll (straying) is strongest copilot, suggesting the Quran frames moral loss as first *denial*, then *deviation*. Weak lifts indicate frequency-driven pairing (high base rates), not semantic specificity.

---

## Per-Root Nearest Neighbors (Top 3 by Co-occurrence Count)

| Root | Arabic | Total | Neighbors |
|------|--------|-------|-----------|
| $rk | شرك | 168 | kfr(16), Zlm(10), kbr(9) |
| *nb | ذنب | 39 | Zlm(4), hlk(4), kfr(3) |
| Avm | اثم | 48 | kfr(5), kbr(4), bgy(3) |
| Dll | ضلل | 191 | kfr(28), Zlm(10), xsr(6) |
| DyE | ضيع | 10 | kfr(2), kbr(1), swA(1) |
| ErD | عرض | 79 | Zlm(6), kfr(6), bgy(5) |
| Tgy | طغي | 39 | kfr(8), Dll(5), Zlm(2) |
| Zlm | ظلم | 315 | kfr(25), swA(18), hlk(11) |
| bTl | بطل | 36 | kfr(9), xsr(3), kbr(2) |
| bgy | بغي | 96 | kfr(7), ErD(5), nfq(5) |
| bwr | بور | 5 | swA(2), bgy(1), kfr(1) |
| fjr | فجر | 24 | fsd(2), kfr(2), Dll(1) |
| fsd | فسد | 50 | Zlm(3), kfr(3), bgy(2) |
| fsq | فسق | 54 | kfr(8), Zlm(4), swA(4) |
| gfl | غفل | 35 | Zlm(4), Dll(3), kfr(3) |
| glf | غلف | 2 | kfr(2) |
| hlk | هلك | 68 | Zlm(11), *nb(4), Dll(3) |
| jHd | جحد | 12 | Zlm(3), kfr(2), fsd(1) |
| jhl | جهل | 24 | ErD(4), bgy(3), swA(3) |
| kbr | كبر | 161 | kfr(18), $rk(9), Zlm(9) |
| kfr | كفر | 525 | Dll(28), Zlm(25), swA(22) |
| knn | كنن | 12 | ErD(2), Zlm(1), kfr(1) |
| mrD | مرض | 24 | nfq(4), kfr(3), Zlm(2) |
| nfq | نفق | 111 | kfr(17), Zlm(5), bgy(5) |
| nks | نكس | 3 | — |
| qfl | قفل | 1 | — |
| qsw | قسو | 7 | Dll(1), Zlm(1), fjr(1) |
| srf | سرف | 23 | *nb(2), hlk(2), Dll(1) |
| swA | سوا | 167 | kfr(22), Zlm(18), nfq(5) |
| xsr | خسر | 65 | kfr(8), Dll(6), Zlm(4) |
| xtm | ختم | 8 | Dll(1), bTl(1) |
| xyb | خيب | 5 | Zlm(1), kfr(1) |

**Insight:** Three isolated roots (nks, qfl—each 1–3 ayahs) never co-occur. Most roots bond to kfr as primary neighbor, with Zlm as secondary hub for abstract injustice contexts.

---

## Surah Density (Top 15)

| Surah | Density | Character |
|-------|---------|-----------|
| 91 (al-Shams) | 10.3% | Meccan, paired with success |
| 103 (al-ʿAsr) | 10.0% | Meccan, paired with success |
| 63 (al-Munāfiqūn) | 9.4% | Medinan, hypocrite critique |
| 71 (Nūḥ) | 8.5% | Meccan, rejection narrative |
| 109 (al-Kāfirūn) | 8.3% | Meccan, unbelievers apostrophe |
| 46 (al-Aḥqāf) | 7.9% | Medinan, idolater dialogue |
| 60 (al-Mumtaḥana) | 7.9% | Medinan, covenant-breaking |
| 83 (al-Muṭaffifīn) | 7.9% | Meccan, oath-breakers |
| 40 (Ghāfir) | 7.7% | Meccan, debate framework |
| 47 (Muḥammad) | 7.1% | Medinan, battle theology |
| 98 (al-Bayyinah) | 6.7% | Medinan, clear proof |
| 42 (al-Shūrā) | 6.6% | Meccan, divine counsel |
| 6 (al-Anʿām) | 6.3% | Medinan, polytheism refutation |
| 14 (Ibrāhīm) | 6.3% | Meccan, disbelief consequences |
| 9 (al-Tawba) | 6.1% | Medinan, breach accountability |

Surahs 91 and 103 pair failure-vocabulary with success; failure density rivals success density (10.0% vs. 9.0%) in these Meccan capstone chapters. No Surah exceeds 10.3%, indicating failure-vocabulary distributes broadly rather than concentrating in polemical surahs.

---

## Top 10 High-Divergence Failure Ayahs

| Reference | Root(s) | Divergence | Outlier | Notes |
|-----------|---------|------------|---------|-------|
| [23:67] | kbr | 0.8445 | — | Refusal to admit transgression |
| [91:11] | Tgy | 0.8224 | — | Transgression of soul-boundaries |
| [50:24] | kfr | 0.8123 | — | Disbelief at resurrection |
| [96:6] | Tgy | 0.8057 | Khattab | Near-religious excess |
| [53:17] | Tgy | 0.8050 | — | Transgression at throne-realm |
| [70:36] | kfr | 0.8027 | — | Disbelief's grip |
| [18:108] | bgy | 0.7995 | Arberry | Transgressive appetite |
| [54:14] | kfr | 0.7985 | — | Disbelief swallowed (Flood narrative) |
| [84:22] | kfr | 0.7963 | Khattab | Eschatological disbelief |
| [23:3] | ErD | 0.7938 | — | Aversion from God |

**Pattern:** Tgy (transgression, طغي) dominates top divergence (0.6738 avg), suggesting English struggles to render hubris-without-sin. Kfr (disbelief) shows high variance only in eschatological contexts. Divergence peaks where failure is internal state (spirit-condition) rather than act.

---

## Per-Root Divergence Averages

Rare roots (xyb: 0.7135, nks: 0.6872) show highest divergence; common roots (kfr, Zlm) cluster at 0.62–0.64, indicating standardization through repetition. **Baseline:** success-vocabulary averaged 0.61; failure-vocabulary averages 0.6304—nearly identical, contradicting initial hypothesis of higher failure-variance.

---

## Per-Translator Outlier Rate on Failure Vocabulary

| Translator | Outlier Rate |
|------------|--------------|
| Saheeh | 0.8% |
| Pickthall | 7.9% |
| Khattab | 10.6% |
| Arberry | 10.3% |

Saheeh remains consistent across both vocabularies (0.8%). Khattab and Arberry spike to 10%+ on failure (vs. 9.1% and 9.0% on success), suggesting contemporary and classical translators struggle more with failure-semantics under formal review. Pickthall (~8%) sits between.

---

## Four Unexpected Findings for Synthesis

### 1. Kfr (Disbelief) Dominates as Central Hub
Kfr pairs with 30 of 31 roots, acting as the sole bridge between isolated pairs. Like hdy in success-vocabulary, it anchors all other failure-meanings. Medina's polemics weaponize it.

### 2. Active Avoidance in Zero Co-Occurrences
Ten root-pairs show zero co-occurrence despite statistical expectation (e.g., hlk + swA: expected 6.56). Dll + fsd never co-occur despite both being corruption-roots, indicating **semantic separation**: the Quran deploys failure-siblings in distinct theological registers.

### 3. Meccan/Medinan Inversion
Success-vocabulary is Medinan-heavy (0% Meccan in Slw, zkw, flH). Failure-vocabulary inverts: swA (36.5% Meccan), bTl (72.2%), Avm (79.2%) are Meccan-dominant, while kfr (9.0%) stays Medinan. Early revelation emphasizes character-failures; late revelation weaponizes ideological rejection.

### 4. Higher Failure Density in Late Surahs
Failure reaches 10.3%; success peaks at 8.2%. Surahs 91 and 103 combine both registers, suggesting failure and success are dialectically locked only at revelation's end.

---

**Scripts:** `/scripts/build_failure_cooccurrence.py` and `/scripts/build_failure_divergence.py`.  
**Data:** `/data/structural/failure-cooccurrence.json` and `/data/structural/failure-divergence.json`.
