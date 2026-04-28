# Full-Quran Semantic Graph — Master Index

> **What this folder is:** the catalog and analysis of the Quran's complete root co-occurrence graph — every Arabic root paired with every other root that appears with it in at least two ayahs, partitioned into communities by Louvain modularity, and read thematically by parallel agents.
>
> **Date of analysis:** 2026-04-26
> **Method:** root-level ayah co-occurrence → weighted undirected graph → Louvain community detection → per-cluster qualitative reading
> **Status:** 15 of 666 clusters analyzed in depth; the remaining 651 are smaller (mostly singletons of rare roots) and remain available in `clusters.json` for follow-up.

---

## 1. How to view the graph

Two complementary views — open whichever fits your question:

```bash
open notes/full-quran-graph/index.html    # full detail view (1,642 roots, cluster-aware layout)
open notes/full-quran-graph/macro.html    # macro view (clusters as super-nodes, ~90 nodes)
```

### `index.html` — the detail view

**v2 (cluster-aware layout).** Each Louvain cluster gets its own spatial centroid (Fibonacci spiral arrangement); nodes are forced toward their cluster's center. The result: the 15 named clusters appear as visually distinct neighborhoods rather than a single dense hairball.

Key features:
- **Default filter: cluster size ≥ 3.** The 527 singleton clusters (rare roots, mostly noise) are hidden by default. Slider in controls to bring them back.
- **Default edge filter: weight ≥ 5.** Most low-weight noise edges hidden. Slider to expand.
- **Cluster name labels at centroids.** The 15 thematically-analyzed clusters get prominent colored labels (e.g., "Revelation, Speech & Disbelief", "Vegetative Signs / Reflective Gaze"). Unnamed clusters labeled by ID + size.
- **Cluster background tints.** Subtle radial gradient around each centroid in its color, so cluster regions are visible at a glance.
- **Click cluster name (or legend entry) to focus.** Highlights one cluster, dims everything else, shows inter-cluster bridges.
- **Click any node** for full details (Arabic, root, frequency, top 15 co-occurring roots).
- **Search box** auto-pans the camera to the matching root.

### `macro.html` — the cluster super-node view

For a high-level overview without the noise: each of the ~90 clusters with ≥ 3 roots is collapsed to a single super-node (size proportional to member count). Inter-cluster edges (weight ≥ 2 ayahs) show how thematic territories connect to each other. The 15 named clusters are highlighted with white borders; unnamed clusters appear semi-transparent.

This is the view to start with if you want to see the *macro-structure* of the Quran's vocabulary before zooming into any one cluster.

---

## 2. Headline numbers

| metric | value |
|---|---|
| distinct Arabic roots in the Quran | **1,642** |
| co-occurrence edges (weight ≥ 2 ayahs) | **28,761** |
| Louvain communities detected | **666** |
| largest cluster (revelation & disbelief) | 191 roots |
| 15 large clusters analyzed in depth | 592 roots covered (≈36 % of all roots) |
| singletons / clusters of size ≤ 3 | ~480 (the long tail of rare-root noise) |

The graph is dramatically heavy-tailed: the top 15 clusters carry the vast majority of structurally significant roots, and the next ~50 clusters carry the rest of the substantive vocabulary. The remaining hundreds of clusters are mostly individual rare roots (hapax / dis-legomena) that didn't accumulate enough edges to merge.

---

## 3. Suggested reading order

A new reader should not start at cluster 0 and march down the IDs. Cluster IDs are arbitrary Louvain labels with no semantic ordering. Read in this order instead:

1. **Cluster 4 — Revelation, Speech & Disbelief** (`cluster-04-revelation-and-disbelief.md`). The largest cluster (191 roots) and the Quran's central narrative engine. Anchors everything else.
2. **Cluster 8 — Allegiance & the Object of Worship** (`cluster-08-allegiance-and-worship.md`). The theological axis (إله، عبد، ولي، شرك) that cluster 4 orbits.
3. **Cluster 0 — The Believers' Reward** (`cluster-00-believers-reward.md`). The single most formulaic cluster in the Quran — *al-ladhīna āmanū wa-ʿamilū l-ṣāliḥāt* literally became a community.
4. **Cluster 62 — The Prepared Fire** (`cluster-62-prepared-fire.md`). The negative pole that completes cluster 0; the eschatological recompense lexicon.
5. **Cluster 96 — Dunya vs. Ākhirah** (`cluster-96-dunya-akhirah.md`). The time-horizon morality between cluster 0 and cluster 62.
6. **Cluster 90 — The Sin–Mercy Economy** (`cluster-90-sin-mercy-economy.md`). The transactional circuit of repentance ↔ forgiveness — the verse-coda *innallāha ghafūrun raḥīm* made into a community.
7. **Cluster 77 — Creation and the Appointed Term** (`cluster-77-creation-and-term.md`). The lifecycle-as-resurrection-argument from dust to soul-taking.
8. **Cluster 43 — Divine Will & Dominion** (`cluster-43-divine-will-dominion.md`). The grammar of *kullu shayʾin qadīr* — universal-quantifier theology.
9. **Cluster 75 — Witnessing the Visible Sign** (`cluster-75-visible-sign.md`). The phenomenology of رأي and the meteorological proof-loop.
10. **Cluster 11 — Vegetative Signs & Reflection** (`cluster-11-vegetative-signs.md`). The validation cluster: فكر sits with palms and grapes, not with cognition. **Read alongside `notes/cognition/` if available.**
11. **Cluster 7 — The Sea-Rescue Cluster** (`cluster-07-sea-rescue.md`). A self-contained narrative grammar (storm → rescue → gratitude or transgression).
12. **Cluster 5 — The Commanded Self** (`cluster-05-commanded-self.md`). The interpersonal Madinan ethics layer (نفس، أمر، صبر، معروف).
13. **Cluster 19 — Household Law and Lineage** (`cluster-19-household-law.md`). The juristic-arithmetic cluster of inheritance and marriage.
14. **Cluster 17 — Bodily Purity** (`cluster-17-bodily-purity.md`). The wudu / tayammum micro-cluster — two ritual verses generating a whole community.
15. **Cluster 66 — Jihād fī Sabīl Allāh** (`cluster-66-jihad-fi-sabil-allah.md`). The Medinan operational vocabulary of struggle, spending, and emigration.

If you have time for only three: **4 → 0 → 11**. Cluster 4 gives you the rhetorical engine; cluster 0 gives you the formulaic core; cluster 11 gives you the most surprising structural finding (reflection-as-vegetative).

---

## 4. Cluster catalog (the 15 analyzed)

| ID | size | name | one-sentence summary | file |
|---:|---:|---|---|---|
| **4** | 191 | Revelation, Speech & Disbelief | The Quran's central revelation-and-response engine — God speaks, messengers convey, peoples deny or assent, history settles the account. | [cluster-04](clusters/cluster-04-revelation-and-disbelief.md) |
| **8** | 64 | Allegiance & the Object of Worship | The full relational vocabulary of devotional allegiance — whom you call, obey, trust, ally with, and worship, vs. whom you take "besides Him." | [cluster-08](clusters/cluster-08-allegiance-and-worship.md) |
| **0** | 62 | The Believers' Reward | The reward formula made graph — gravitational well around *al-ladhīna āmanū wa-ʿamilū l-ṣāliḥāt* pulling in gardens, rivers, eternal abiding, and their disgrace-shadows. | [cluster-00](clusters/cluster-00-believers-reward.md) |
| **5** | 40 | The Commanded Self | The lexicon of the commanded, tested, restrained self in domestic and civic life — moral psychology + deontic command + family-law procedure in one register. | [cluster-05](clusters/cluster-05-commanded-self.md) |
| **19** | 40 | Household Law and Lineage | Family-law vocabulary — kin terms, marriage and divorce machinery, fractional arithmetic of inheritance — held together by ذكر "male/remember" and مثل "the like of." | [cluster-19](clusters/cluster-19-household-law.md) |
| **17** | 33 | Bodily Purity & Prayer | The *wudu cluster* — body, washings, wipings, exempting states, the prayer they prepare for, and the moral polarity of purity radiating into eschatology. | [cluster-17](clusters/cluster-17-bodily-purity.md) |
| **7** | 25 | The Sea-Rescue Cluster | The sea-rescue grammar — storms, ships, drowning, dry land become parable for divine bounty (فضل) met by gratitude (شكر، خلص) or transgression (بغي، نسي). | [cluster-07](clusters/cluster-07-sea-rescue.md) |
| **90** | 24 | The Sin–Mercy Economy | The moral-transactional circuit where every named offense terminates in the formulaic divine response *innallāha ghafūrun raḥīm*. | [cluster-90](clusters/cluster-90-sin-mercy-economy.md) |
| **96** | 19 | Dunya vs. Ākhirah | The lexicon of time-horizon morality — fleeting, beautified, deluding dunyā vs. lasting ākhirah, plus verbs of seduction, distraction, and leaving. | [cluster-96](clusters/cluster-96-dunya-akhirah.md) |
| **75** | 18 | Witnessing the Visible Sign | The theater of the visible sign — رأي trained on storms, stars, cities, graves, where God displays evidence that strikes (صوب), emerges (خرج), almost (كاد) escapes the heedless. | [cluster-75](clusters/cluster-75-visible-sign.md) |
| **11** | 17 | Vegetative Signs & Reflection | The vegetative-sustenance field where فكر sits with palms, grapes, fruit, and harvest — *to reflect, in the Quran, is to stand before growing things.* | [cluster-11](clusters/cluster-11-vegetative-signs.md) |
| **66** | 17 | Jihād fī Sabīl Allāh | The Medinan grammar of struggle on God's path — going-forth, fighting, spending wealth, and the antagonist vocabulary of barring, sitting out, being held back. | [cluster-66](clusters/cluster-66-jihad-fi-sabil-allah.md) |
| **62** | 16 | The Prepared Fire | The pre-assembled rhetorical kit for narrating eschatological punishment — كفر as trigger, عذاب as substance, plus verbs of preparing, tasting, burning, humiliating. | [cluster-62](clusters/cluster-62-prepared-fire.md) |
| **43** | 13 | Divine Will & Dominion | The grammar of unconditioned divine prerogative — *kullu shayʾin qadīr*, the will-verb شاء, the dominion-noun ملك, and the bsT/qdr economic dyad. | [cluster-43](clusters/cluster-43-divine-will-dominion.md) |
| **77** | 13 | Creation & the Appointed Term | The lifecycle-and-deadline lexicon — dust → sperm-drop → clot → lump → child → maturity → soul-taking, recruited as proof-from-embryology for resurrection. | [cluster-77](clusters/cluster-77-creation-and-term.md) |

**Total roots covered:** 592 of 1,642 (~36 %).

---

## 5. Cross-cluster patterns — what's worth noticing

After reading all 15 in succession, several meta-patterns surface that are not visible from any single cluster.

### 5.1 The Quran clusters by *speech-act register*, not by topic

Surface-level "topics" (ritual, family, war, eschatology) are not what Louvain detected. What it detected are **stable speech-act registers**: the verse-coda register (cluster 90's "*ghafūrun raḥīm*"), the omni-quantifier register (cluster 43's "*kullu shayʾin*"), the deictic-evidential register (cluster 75's "*alam tara*"), the reward-formula register (cluster 0's "*al-ladhīna āmanū wa-ʿamilū*"), the prepared-punishment register (cluster 62's "*aʿtadnā lahum*"). Several clusters are essentially **a single repeated formula plus its shadow**. This is a graph-theoretic confirmation that the Quran is composed of recurring rhetorical templates whose vocabulary is *welded* by reuse — a finding consistent with classical observations about Quranic *iʿjāz* but rarely formalized so cleanly.

### 5.2 Two-node anchor verses generate whole clusters

Cluster 17 (bodily purity) is essentially Q 4:43 + Q 5:6 — two ritual-law verses with rare vocabulary so dense (لمس، غائط، يمم، صعيد، مسح، غسل) that the algorithm welded them into a 33-root community. Cluster 19's inheritance-arithmetic spine (نصف، ثلث، ربع، خمس، سدس، حظ) is largely Q 4:11–12. Cluster 96's emotional center is Q 3:185 (the *zuḥziḥa* verse). **Some clusters are essentially "verse-clusters" — communities formed because a small number of verses use very dense, rare vocabulary together.** This raises a methodological question worth flagging: how stable would these clusters be if those single anchor verses were removed?

### 5.3 The reward / punishment / mercy / will clusters interlock

Clusters 0, 62, 90, 96 form an interlocking eschatological *quartet*:

- **0** = reward (ايمن + عمل + جنة + نهر)
- **62** = punishment (كفر + عذب + سعر)
- **90** = mercy/forgiveness (رحم + غفر + توب)
- **96** = the moral choice (دنو + أخر + غرر + زين)

Louvain partitioned them — they are *separate* communities — but each one references the same axis from a different rhetorical angle. **Cluster 0 is the assertion, 62 is the threat, 90 is the conditional escape, and 96 is the warning.** A unified eschatological-economy analysis would re-merge them along their bridges (الذين كفروا appears in both 4 and 62; غفر bridges 90 and 0).

### 5.4 Polysemy is not an error; the graph reads it as content

Several clusters surface root-polysemies as *features*, not bugs:

- **بني** (cluster 5): "sons" + "build" — domestic kin meaning and architectural metaphor share the same ayahs about the moral edifice.
- **ذكر** (cluster 19): "male" + "remember/mention" — kinship contexts dominate.
- **دين** (cluster 19): "religion" + "debt" — *dayn* drags the root into family law.
- **برر** (cluster 7): *birr* (piety) + *barr* (dry land) — the homonymy is welded by Quranic wordplay.
- **حبب** (cluster 11): "love" + "grain/seed" — both pull toward the vegetative cluster.
- **دنو** (cluster 96): "lower/worldly" + "near/at-hand" (paradisal *qutūfuhā dāniyah*) — the same root names trap and reward.
- **جنب** (cluster 17): "side" + "junub (major impurity)" — body-as-ritual-instrument.
- **مهل** (cluster 62): "molten metal" + "respite" — bound by shared eschatological scene.

The graph is showing us where the Quran *exploits* root polysemy as a rhetorical resource. A purely lemma-disambiguated graph would lose this.

### 5.5 Narrative cycles smuggle vocabulary into thematic clusters

Cluster 4 absorbs نمل (ants, Solomon), نعج (ewes, David's parable), and رهط (clan, Salih's nine). Cluster 11 absorbs خون and عصبة because the Yusuf cycle's grain-dream binds agricultural and fraternal-treachery vocabulary. Cluster 19 absorbs Joseph-cycle words (جهز، فور، غبر) via the kinship narrative. **Narrative suras function as bridges that inject domain-specific vocabulary into thematic clusters.** This is structurally why the Quran's narrative passages don't feel "off-topic" — their lexica have been welded into the surrounding theological registers by repeated co-occurrence.

### 5.6 Negative-space vocabulary is consistently colocated with the positive

Cluster 66 (jihād) co-clusters with its antagonists (صدد، عوج، قعد، ضجع، حصر — barring, bending, sitting out, being held back). Cluster 0 (reward) co-clusters with حبط، خزي، سخط (nullification, disgrace, wrath). Cluster 8 (allegiance) co-clusters with شرك، زعم، ميل (association, false claim, deviation). The Quran's positive lexicons consistently **carry their negations as members of the same community**, not as separate clusters. The text appears to define virtues by what they are *not* as much as by what they are.

### 5.7 Madinan-juristic clusters are a distinct stratum

Three clusters (5, 17, 19, with 66 adjacent) have a recognizably Madinan signature — heavy in surahs 2, 4, 5, 33; dominated by legal-imperative syntax; populated by rare vocabulary that appears almost nowhere else (يمم، سدس، رفث، عضل، حرض). They form what could plausibly be called the *Madinan juristic stratum* of the graph. A diachronic re-analysis weighting roots by Nöldeke chronology would likely show these as a distinct generation.

---

## 6. Validations of prior investigations

The cluster graph **independently confirmed** several findings that earlier qualitative investigations in this project had argued for. Because the clustering is unsupervised and operates on raw co-occurrence, these convergences are non-trivial.

1. **Heart-as-locus of cognition** *(prior investigation in `notes/heart/` if present)* — The Quran's cognitive verbs (عقل، فقه، فكر، ذكر) cluster with bodily/affective vocabulary, not with abstract intellectual roots. **Cluster 11** specifically vindicates this for فكر: *fikr* sits with palms and grapes, not with *ʿilm* or *ʿaql*. Reflection in the Quran is, graph-theoretically, *something one does in the presence of growing things* — a vegetative concept, not an abstract one.

2. **`fkr` clustering with agriculture** — Validated explicitly. Cluster 11 is flagged in its own header as "**CRITICAL VALIDATION:** Independent confirmation of the cognition-investigation finding that *li-qawmin yatafakkarūn* attaches reflection to natural-world signs." The graph was built without any thematic supervision; it placed فكر next to نبت، ثمر، نخل، فجر، زرع، عنب، زيت. Earlier reading argued this from internal evidence (فكر's own neighbor list); the cluster graph confirms it from external evidence (no other cognitive root joined the cluster).

3. **`jhd` as physical-only struggle** — Validated. Cluster 66 (jihād fī sabīl Allāh) is exclusively the operational vocabulary of armed-and-economic struggle: قتل، نفر، هجر، نفق، مول، صدد. **There is no cognitive sense of jhd in any cluster.** This corroborates the earlier finding (`notes/cognition/research-negative-space.md` if present) that the Quran's *jhd* is not "intellectual struggle" but bodily-financial mobilization on God's path.

4. **`rAy` as evidential, not cognitive** — Validated, and given a structural location. Cluster 75 explicitly contains رأي and shows it co-clustering with weather (سحب، برق، ودق)، geography (بلد، أفق)، and eschatological staging (وقف، جدث، خرج). Cluster 75's header flags this: "rAy is the third 'seeing' root I identified as missed from the original 14 cognitive roots. It clusters HERE, NOT with cognition." The Quranic رأي is the verb of the *displayed sign* (*alam tara*), not of interior deliberation. The cognitive register owns بصر، نظر، فكر; the evidential-phenomenological register owns رأي.

5. **`rḥm` operates in two distinct registers** — Validated. The earlier `notes/mercy/concept-rhm.md` analysis identified an *attribute* mode of رحم (paired with Allah/Lord/Knowing). Cluster 90 surfaces a different mode: *transactional* رحم paired with sin-vocabulary (إثم، عدو، ضرر، فسق). These are the same root operating in two registers, and the graph respects the distinction.

These five convergences strengthen confidence that the per-concept investigations were detecting real structure, not artifacts of motivated reading.

---

## 7. The unanalyzed long tail (651 clusters)

The 15 analyzed clusters cover 592 of 1,642 roots (~36 %). The remaining 651 clusters are smaller, mostly singletons or pairs of rare roots that didn't accumulate enough edges to merge into larger communities. They include:

- **Hapax legomena** (roots appearing once in the entire Quran).
- **Pairs of rare roots** that share a single ayah and nothing else.
- **Small thematic micro-clusters** (size 4–10) which may carry interesting structure but were not prioritized for parallel-agent analysis.

To browse them: open `clusters.json`, search for cluster IDs not in {0, 4, 5, 7, 8, 11, 17, 19, 43, 62, 66, 75, 77, 90, 96}. The next ~30 largest unanalyzed clusters are likely the most promising — they are large enough to be coherent but small enough that the algorithm carved them off as distinct from the giants.

A reasonable follow-up would be to analyze the next 10–15 clusters in size order, which would push coverage past 50 % of all roots.

---

## 8. Suggested next investigations

Based on what the catalog reveals, the most promising next moves:

1. **Bridge analysis between clusters 0, 62, 90, 96.** These four form an eschatological quartet but Louvain split them. Identify the bridge roots (likely كفر، توب، ايمن، اخر) and quantify the inter-cluster edge density. This would test whether the four are genuinely separate communities or a single super-community fragmented at a low modularity threshold.

2. **Verse-template extraction.** Several clusters are essentially formula-clusters: cluster 0 is *al-ladhīna āmanū wa-ʿamilū l-ṣāliḥāt + tajrī min taḥtihā l-anhār*; cluster 62 is *aʿtadnā lahum ʿadhāban + alīman/muhīnan*; cluster 90 is the *innallāha ghafūrun raḥīm* coda. Build n-gram extractors to quantify what fraction of each cluster's edges collapse into ≤3 fixed templates.

3. **Anchor-verse stability test.** Re-run Louvain after removing high-density anchor verses (Q 4:11–12 for cluster 19; Q 4:43 + Q 5:6 for cluster 17; Q 3:185 for cluster 96). Do the clusters fragment, and along what fault lines? This would distinguish robust thematic clusters from artifacts of vocabulary-dense single verses.

4. **Polysemy disambiguation experiment.** Pick three high-impact polysemes (دين/دين, ذكر/ذكر, حبب/حبب, برر/برر) and split them into separate lemmas. Re-run clustering. Do the clusters split coherently along the semantic seam, or do both senses stay welded to the same community? This tests whether the polysemy is a graph artifact or a Quranic *device*.

5. **Diachronic (Meccan vs. Medinan) layering.** Tag every ayah by Nöldeke period and recompute per-cluster Madinan share. Hypothesis: clusters 5, 17, 19, 66, 90 will be heavily Madinan; clusters 7, 11, 75, 77 will be heavily Meccan. Quantifying this would let us read the cluster catalog as a window onto the Quran's compositional layers.

6. **The "negative-space" sub-graph.** Across clusters 0, 8, 66, 90, the antagonist vocabulary (حبط، شرك، صدد، إثم، فسق) consistently lives *inside* the positive cluster. Extract these antagonist roots, build a sub-graph among them, and see whether they form a coherent meta-cluster of "what virtue is not."

7. **The cognition cluster.** This README assumes the existence of a cognition cluster (containing علم، عقل، فقه، بصر، نظر) elsewhere in the partition. **It was not in the analyzed 15** — meaning either it's larger than expected and got absorbed into cluster 4, or it's smaller and was deferred. Locate it in `clusters.json` and analyze; this is the natural complement to clusters 11 and 75.

8. **Continue the per-concept deep dives** for the singletons that anchor each cluster. The cluster catalog has surfaced a number of high-leverage roots (شيا، كلل، حوط in cluster 43; مثل in cluster 19; بني in cluster 5; خرج in cluster 75) that deserve their own concept files.

---

## 9. Files in this folder

| file | description |
|---|---|
| `README.md` | (this file) master index and synthesis across the 15 analyzed clusters |
| `data.json` | full graph data — nodes (1,642 roots with frequencies and lemmas) and edges (28,761 weighted co-occurrences); ≈2.3 MB |
| `clusters.json` | all 666 Louvain communities with their member roots; lookup keyed by cluster ID |
| `index.html` | interactive D3 force-directed visualization of the full graph; open in a browser |
| `clusters/cluster-04-revelation-and-disbelief.md` | cluster 4 (191 roots) — the central revelation/denial engine |
| `clusters/cluster-08-allegiance-and-worship.md` | cluster 8 (64 roots) — devotional allegiance and false-worship vocabulary |
| `clusters/cluster-00-believers-reward.md` | cluster 0 (62 roots) — the *al-ladhīna āmanū* reward formula |
| `clusters/cluster-05-commanded-self.md` | cluster 5 (40 roots) — moral psychology + family-law procedure |
| `clusters/cluster-19-household-law.md` | cluster 19 (40 roots) — kinship, marriage, inheritance arithmetic |
| `clusters/cluster-17-bodily-purity.md` | cluster 17 (33 roots) — wudu/tayammum and the body in prayer |
| `clusters/cluster-07-sea-rescue.md` | cluster 7 (25 roots) — storm → rescue → gratitude/transgression |
| `clusters/cluster-90-sin-mercy-economy.md` | cluster 90 (24 roots) — sin/repentance/forgiveness/mercy circuit |
| `clusters/cluster-96-dunya-akhirah.md` | cluster 96 (19 roots) — time-horizon morality |
| `clusters/cluster-75-visible-sign.md` | cluster 75 (18 roots) — رأي and the meteorological sign-system |
| `clusters/cluster-11-vegetative-signs.md` | cluster 11 (17 roots) — *fkr* with palms and grapes (validation cluster) |
| `clusters/cluster-66-jihad-fi-sabil-allah.md` | cluster 66 (17 roots) — Medinan struggle/spending/emigration |
| `clusters/cluster-62-prepared-fire.md` | cluster 62 (16 roots) — the prepared-punishment lexicon |
| `clusters/cluster-43-divine-will-dominion.md` | cluster 43 (13 roots) — *kullu shayʾin qadīr* and divine prerogative |
| `clusters/cluster-77-creation-and-term.md` | cluster 77 (13 roots) — embryology as proof-of-resurrection |

---

*Compiled 2026-04-26 from parallel-agent analyses of the Louvain partition of the full Quran root co-occurrence graph.*
