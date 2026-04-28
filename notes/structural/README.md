# Structural analyses

> Computational analyses across the entire Quran corpus. These are not narrative investigations of one concept — they're aggregate views that surface research-priority questions, build reference indexes, and reveal patterns invisible from any single root or cluster.
>
> **Date:** 2026-04-26
> **Method:** 5 parallel agents, each writing Python over existing data (morphology, translations, clusters, full-quran-graph). Outputs both raw JSON (in `data/structural/`) and written analysis (in this folder).

---

## Files (5 analyses)

### 1. [`surah-signatures.md`](surah-signatures.md)
**Per-surah cluster composition** — what each of the 114 surahs is structurally about.

For each surah: percentage of root-bearing vocabulary in each Louvain cluster, dominant cluster, thematic concentration score (mono- vs poly-thematic).

**Top findings:**
- Most mono-thematic surahs are long Medinan ones (Al-Baqara Gini 0.83, An-Nisa 0.83) — huge vocabulary concentrated in few clusters.
- **Highest single-cluster domination: Al-Kafirun (109) — 67% Worship cluster.** Matches its content perfectly.
- Al-Fatiha = 35% Worship + 22% Sin/Mercy. The opening surah sits at the worship-mercy axis.
- Al-Qadr at 23.8% "Divine Will & Dominion" — matches its tradition as the Night of Decree.
- The "Revelation, Speech & Disbelief" cluster dominates almost every long surah → the Quran's vocabulary is structurally saturated with discursive/revelatory speech-acts.

**Use case:** Look up "what is surah X about?" with data instead of intuition. Or query "give me the top 5 surahs by jihad-cluster density."

Data: `data/structural/surah-signatures.json` (832 KB, all 114 surahs)

---

### 2. [`translation-divergence.md`](translation-divergence.md)
**Per-ayah translation divergence map** — surfaces the verses where translators most disagree.

Computes string + lexical + length divergence across Saheeh / Pickthall / Khattab / Arberry for all 6,236 ayahs. Identifies outlier translators per ayah. Sorts by divergence.

**Top findings:**
- **Khattab is the most frequent outlier** (13.3% of all ayahs, 17.3% of high-divergence ones).
- **High-divergence territory dominated by short Meccan oath surahs** (Juz' 30: An-Nazi'at, Al-Adiyat, At-Takwir, Al-Mursalat). These are the oblique apocalyptic-cosmological texts.
- **SURPRISE — stable theology:** heavy theological terms (Throne, decree, six-day creation) often produce LOW divergence. Translation tradition has settled.
- **SURPRISE — hidden complexity:** cryptic narrative beats with no obvious flag (100:5 "center collectively" vs "cleaving with a host", 77:33 "yellowish camels" vs "golden herds" vs "black camels") show high divergence. Mundane-looking, English-difficult.
- **Legal verses translate stably** (only 1% of high-divergence). Disagreement is in apocalyptic/cosmological imagery and oath-formulas, not law.

**Top research-priority verses (by divergence):** 100:5, 79:4, 81:16, 36:59, 77:33, 23:67, 51:9, 52:12, 38:11, 79:2, 91:11, 37:12, 53:53, 74:18, 77:30 — listed in the report with all four translations side-by-side.

**Use case:** Pick any of these as the next focused-Arabic-study verse.

Data: `data/structural/translation-divergence.json` (2.9 MB) + meta file with cutoffs.

---

### 3. [`cluster-bridges.md`](cluster-bridges.md)
**Cross-cluster bridge roots** — the load-bearing connectors that span multiple Quranic semantic territories.

For each root, computes Shannon entropy of its co-occurrence cluster distribution. High entropy = root that ties many clusters together. Plus pairwise inter-cluster connection strength.

**Top findings:**
- **Top bridges are SENSORY-PHYSICAL roots, not theological hubs.** sqy (water), mwh (water), Akl (eat), $rb (drink), Eyn (eye/spring). The Quran routes between thematic territories through reused images of water, food, sight, and motion — not through abstract theology.
- High-frequency roots (Alh, qwl, Amn, kwn) are FREQUENCY HUBS but not entropy bridges (their distribution stays concentrated near home cluster).
- **Most central named cluster: "Revelation, Speech & Disbelief"** (11,396 shared ayahs across 14 partners) — the Quran's meta-cluster, the discursive frame everything else is narrated through.
- **Most isolated named cluster: "Vegetative Signs / Reflective Gaze"** (792 shared ayahs total — 14× less central than the most central).
- The Quran has **two distinct creation discourses** — cosmic (xlq/Ajl) vs local (nbt/zrE) — that rarely interlace. Only 17 ayahs of overlap.
- **Surprising bridge: Bodily Purity & Prayer ↔ Jihād fī Sabīl Allāh** (86 ayahs, bridged by Slw + nfq + qwm). The famous "establish prayer and spend in Allah's path" coupling. Worship and warfare are stitched together by spending and the act of standing.

**Use case:** When investigating any cluster, the bridge roots tell you what other concepts you'll find tangled in. They're high-value research targets.

Data: `data/structural/cluster-bridges.json` (124 KB, top 100 bridges + 30 cluster pairs + 15×15 matrix).

---

### 4. [`ayah-echoes.md`](ayah-echoes.md)
**Quran refrains, repeated formulas, and near-duplicate verses.**

Normalizes Arabic, n-gram-shingles all 6,236 ayahs, finds Jaccard ≥ 0.5 pairs. Identifies refrains, common openings/closings, near-duplicates with one-word differences.

**Top findings:**
- **92 refrains** identified (259 ayah occurrences = 4.2% of corpus is refrain material).
- **Surah 55 (Ar-Rahman) has 466 internal echo pairs** — the famous *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain (31 occurrences).
- **Surah 26 has 105 internal echoes** — seven prophet vignettes with shared four-couplet refrain.
- **Surah 7 (Al-A'rāf) is the densest cross-surah hub** — a sourcebook of prophet-destruction templates redeployed in 11, 23, 26, 29.
- **Most common opener: "يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ"** (88 occurrences) — the address-to-believers formula.
- **Most common closing (outside Surah 55's refrain): "عَلَىٰ كُلِّ شَيۡءٍ قَدِيرٌ"** (32×).
- **One-word differences carry meaning:** 6:151 vs 17:31 reverses "you and them" / "them and you" based on whether poverty is present vs feared. The Quran is precise — word changes between near-duplicates are semantic editorial moves.
- 23 one-word-difference pairs identified for editorial significance.

**Use case:** The Quran's repetition is structural, not redundant. The echoes catalog lets you ask "what changes between these two near-duplicate verses, and why?"

Data: `data/structural/ayah-echoes.json` (392 KB).

---

### 5. [`root-reference.md`](root-reference.md)
**Comprehensive per-root reference** — all 1,642 roots in one searchable index.

For each root: arabic, count, lemmas, POS, cluster, surah coverage, Meccan share, top co-occurring roots, bridge status, notable flags. Listed by frequency and by cluster.

**Quick stats:**
- **49,967 root-bearing words** total
- **561 noun-only roots, 235 verb-only, 5 proper-noun-only**
- **395 single-occurrence roots** (24% of all roots)
- **459 roots confined to a single surah**
- **522 roots qualify as "high inter-cluster connectivity"** (10+ neighbor clusters)
- **7 roots appear in 80+ surahs**: Alh, qwl, kwn, rbb, Elm, ArD, smw

**Notable data quality issue (worth knowing about):**
- **137 case-collision groups** in the buckwalter root encoding. Buckwalter is case-sensitive (s=س vs S=ص) and many real roots become indistinguishable under case-insensitive comparison. Examples: Zlm/zlm, ESy/Esy. Important caveat for any string-matching code touching root names.
- The cluster-90 "ESy/Esy duplication" turned out to be a case-collision rather than a true duplicate — both encode real, distinct roots.

**Use case:** Look up any root quickly. Or browse by cluster ("show me all roots in the Sin-Mercy Economy cluster").

Data: `data/structural/root-reference.json` (1.4 MB) + CSV (354 KB).

---

## Cross-cutting observations

A few patterns visible across all 5 analyses:

1. **The Quran's center of gravity is "Revelation, Speech & Disbelief".** Surah signatures show it dominates almost every long surah. Cluster bridges show it as the most central. Echo analysis shows the address-to-believers formula as the dominant opener. The Quran is, structurally, *a text about itself being received, denied, or believed*.

2. **Sensory-physical imagery is the connective tissue.** Cluster bridges and echo analysis both show that water, food, sight, and motion roots are what tie the Quran's themes together. Abstract theology rides on concrete metaphor.

3. **Small Meccan surahs are translator-resistant.** Translation divergence shows the highest-disagreement verses are short Meccan oath surahs. Surah signatures show these are the most poly-thematic. Both confirm: the early Meccan corpus is doing oblique, multi-vocal work that resists clean rendering.

4. **Legal verses are surprisingly stable across translators**, while apocalyptic and cosmological verses are not. This inverts what you'd expect — fiqh discourse has settled English, while the most theologically-loaded narrative beats remain contested.

5. **The Quran is precise even in its repetition.** One-word differences between near-duplicate verses (e.g., 6:151 vs 17:31's poverty inversion) are not stylistic variation but editorial precision. This validates Quranic claims of textual integrity at a structural level.

---

## What to do with this

These five files are **research instruments**, not finished investigations. Each one surfaces a sorted list of "things worth investigating." Suggested next moves:

- **Pick a top-divergence verse** (from translation-divergence.md) and run a focused Arabic study on it.
- **Pick a surah with surprising cluster signature** (from surah-signatures.md) and investigate why.
- **Pick a bridge root** (from cluster-bridges.md) and run a concept investigation on it — those roots tie multiple clusters together so they're high-leverage.
- **Pick a near-duplicate pair** (from ayah-echoes.md) and analyze the meaning of the one-word change.
- **Use root-reference.md as a quick-lookup index** for any root we're working with.

---

## Reproducibility

Each analysis was produced by a single Python script using only stdlib + the existing data files. The agent reports document the methodology choices (especially the divergence scoring and the bridge entropy definition).

To regenerate any analysis, the underlying scripts can be reconstructed from the methodology documented in each `.md` file. Some agents kept their scripts in `/tmp/` or `scripts/` — check the report for path.
