# Cluster Bridges — Where Quranic Semantic Territories Meet

This analysis identifies the **bridge roots** that knit the Quran's 666 Louvain
communities together and maps how the 15 named clusters connect to one another.
Inputs are the per-ayah morphology (`data/morphology/words.jsonl`), the cluster
assignments and names (`notes/full-quran-graph/clusters.json`), and the root
co-occurrence graph (`notes/full-quran-graph/data.json`).

A **bridge score** is the Shannon entropy of a root's cluster-of-co-occurrences
distribution. A root whose ayah neighbours all live in one cluster scores low;
a root whose neighbours are scattered across many clusters scores high. We
filter to roots with `count >= 5` and `n_clusters_touched >= 2` so trivial rare
roots cannot top the list by accident.

## Top 30 bridge roots (highest cross-cluster span)

| # | Root | Arabic | Count | Clusters touched | Entropy | Primary cluster | What it bridges |
|---|------|--------|-------|------------------|---------|-----------------|-----------------|
| 1 | sqy | سقي (water/give-drink) | 25 | 67 | 3.54 | C120 | water-as-mercy ↔ paradise rivers ↔ punishment (boiling water) |
| 2 | mwh | موه (water) | 63 | 107 | 3.53 | Bodily Purity & Prayer | ablution ↔ creation ↔ paradise ↔ flood ↔ vegetation |
| 3 | Akl | اكل (eat) | 109 | 114 | 3.50 | C46 | lawful food ↔ paradise food ↔ "consuming wealth wrongfully" ↔ orphan's property |
| 4 | $rb | شرب (drink) | 39 | 72 | 3.49 | C31 | paradise drink ↔ punishment drink ↔ Bedouin she-camel ↔ ablution |
| 5 | Eyn | عين (eye/spring) | 65 | 80 | 3.46 | C153 | spring of water ↔ vision/eye ↔ houris ↔ "under our eyes" |
| 6 | jbl | جبل (mountain) | 41 | 81 | 3.45 | C127 | Sinai ↔ Day of Judgement (mountains scattered) ↔ creation signs |
| 7 | Zll | ظلل (shade) | 33 | 60 | 3.44 | C239 | paradise shade ↔ "shade of the smoke" hell ↔ Sinai cloud |
| 8 | Hbb | حبب (love/grain) | 95 | 103 | 3.40 | Vegetative Signs | grain/seed ↔ love-of-Allah ↔ love-of-dunya ↔ charity |
| 9 | Drb | ضرب (strike/coin a likeness) | 58 | 99 | 3.40 | Household Law | striking the wife ↔ striking the rock ↔ "Allah strikes a parable" |
| 10 | xrj | خرج (bring forth/exit) | 182 | 136 | 3.39 | Witnessing the Visible Sign | bring forth from earth ↔ from grave ↔ exile/expulsion ↔ harvest |
| 11 | sjd | سجد (prostrate) | 92 | 88 | 3.38 | C162 | prayer-prostration ↔ angels prostrating to Adam ↔ stars/trees prostrating |
| 12 | lyl | ليل (night) | 92 | 91 | 3.38 | C24 | Night of Decree ↔ tahajjud ↔ day/night signs ↔ Isra |
| 13 | jEl | جعل (make/appoint) | 346 | 172 | 3.37 | C44 | the universal "we made/appointed" verb — touches everything |
| 14 | $jr | شجر (tree) | 27 | 58 | 3.36 | C20 | forbidden tree ↔ Zaqqum ↔ olive ↔ tree-of-Bayʿa |
| 15 | Hml | حمل (carry/bear) | 64 | 88 | 3.36 | C156 | Noah's ark ↔ pregnancy ↔ "carrying the trust" |
| 16 | TlE | طلع (rise/sprout) | 19 | 51 | 3.35 | C23 | sun-rising ↔ Zaqqum-shoots ↔ "let him not look upon …" |
| 17 | rAy | راي (see) | 328 | 155 | 3.35 | Witnessing the Visible Sign | dream-vision ↔ "have you not seen" ↔ ocular signs of disbelief |
| 18 | skn | سكن (dwell/calm) | 69 | 89 | 3.33 | C157 | Adam's dwelling ↔ marriage tranquillity ↔ sakīna in battle |
| 19 | nbt | نبت (vegetate) | 26 | 62 | 3.33 | Vegetative Signs | resurrection-as-vegetation ↔ Mary's "good growth" ↔ creation signs |
| 20 | $rr | شرر (evil/spark) | 31 | 54 | 3.31 | C34 | the evil-spark of hell ↔ moral evil ↔ shar/khayr dichotomy |
| 21 | fwq | فوق (above) | 43 | 71 | 3.31 | C236 | above the Throne ↔ above the heads ↔ "a hand above their hands" |
| 22 | kll | كلل (every/whole) | 377 | 173 | 3.29 | Divine Will & Dominion | the universal quantifier — bridges by ubiquity |
| 23 | ArD | ارض (earth) | 461 | 183 | 3.29 | C1 | every domain that mentions creation, walking, dominion, harvest |
| 24 | g$w | غشو (cover/overwhelm) | 29 | 54 | 3.28 | C318 | the covering of night ↔ the overwhelming Day ↔ veil over hearts |
| 25 | TEm | طعم (food) | 48 | 79 | 3.28 | C157 | feeding the poor ↔ paradise food ↔ Zaqqum ↔ fast |
| 26 | bSr | بصر (sight/insight) | 148 | 103 | 3.28 | C191 | physical sight ↔ inner insight ↔ "Allah is seeing" |
| 27 | wDE | وضع (lay down/place) | 26 | 65 | 3.28 | C156 | laying down arms ↔ giving birth ↔ scales placed on Day of Judgement |
| 28 | $kr | شكر (gratitude) | 75 | 77 | 3.28 | Sea-Rescue / Bounty | the gratitude-axis between rescue, bounty, and worship |
| 29 | fjr | فجر (split open / dawn) | 24 | 46 | 3.28 | Vegetative Signs | dawn-prayer ↔ split rock with springs ↔ moral fujur |
| 30 | Hsb | حسب (reckon/account) | 109 | 100 | 3.28 | C188 | "Allah is sufficient" ↔ Day of Reckoning ↔ "do they reckon …" |

**Pattern.** The strongest bridges are not the obvious theological hubs
(`Alh`, `Amn`, `qwl`). Those are *frequency hubs* — they co-occur with
everything because they appear everywhere — but their cluster-distribution is
still concentrated around their home cluster's neighbours. The strongest
bridges are **physical / sensory roots**: water (`mwh`, `sqy`, `$rb`), eating
(`Akl`, `TEm`), trees (`$jr`, `nbt`, `Hbb`), mountains (`jbl`), shade
(`Zll`), seeing (`bSr`, `rAy`), exiting (`xrj`), striking (`Drb`).
**The Quran routes between thematic territories through sense-data and
physical action.** A water-image carries the reader from ablution to paradise
to punishment to creation in the span of a single root.

## Top 20 inter-cluster connections (named clusters)

Ranked by number of ayahs that contain at least one root from each cluster.

| # | Cluster A | Cluster B | Shared ayahs | Top bridge roots |
|---|-----------|-----------|--------------|------------------|
| 1 | Revelation, Speech & Disbelief | Allegiance & the Object of Worship | **2497** | Alh, qwl, kwn, qwm, Elm |
| 2 | The Believers' Reward | Revelation, Speech & Disbelief | 1722 | Alh, Amn, qwl, kwn, rbb |
| 3 | The Believers' Reward | Allegiance & the Object of Worship | 1220 | Alh, Amn, qwl, kwn, qwm |
| 4 | Revelation, Speech & Disbelief | The Commanded Self | 1120 | Alh, qwl, kwn, **nfs**, rbb |
| 5 | Revelation, Speech & Disbelief | Household Law & Lineage | 937 | Alh, qwl, kwn, ***kr** (remembrance/lineage), Elm |
| 6 | Revelation, Speech & Disbelief | Sin–Mercy Economy | 858 | Alh, **rHm**, qwl, kwn, rbb |
| 7 | The Commanded Self | Allegiance & the Object of Worship | 814 | Alh, qwl, kwn, nfs, Amn |
| 8 | Revelation, Speech & Disbelief | Divine Will & Dominion | 811 | Alh, **$yA** (will), **kll**, qwl, kwn |
| 9 | Revelation, Speech & Disbelief | The Prepared Fire | 682 | **kfr**, Alh, **E*b** (punishment), qwl, kwn |
| 10 | Allegiance & the Object of Worship | Sin–Mercy Economy | 639 | Alh, rHm, qwl, kwn, **gfr** (forgive) |
| 11 | Allegiance & the Object of Worship | Household Law & Lineage | 636 | Alh, qwl, kwn, qwm, Amn |
| 12 | Allegiance & the Object of Worship | Divine Will & Dominion | 603 | Alh, $yA, kll, qwl, Elm |
| 13 | The Believers' Reward | The Commanded Self | 561 | Alh, Amn, kwn, qwl, **wqy** (guard) |
| 14 | Revelation, Speech & Disbelief | Bodily Purity & Prayer | 541 | Alh, qwl, kwn, **ydy** (hand), qwm |
| 15 | Allegiance & the Object of Worship | The Prepared Fire | 493 | Alh, kfr, E*b, qwl, kwn |
| 16 | Revelation, Speech & Disbelief | Witnessing the Visible Sign | 464 | **rAy**, Alh, qwl, **xrj**, kwn |
| 17 | Revelation, Speech & Disbelief | Dunya vs. Ākhirah | 464 | Alh, **Axr** (last), qwl, **Hyy** (life), kwn |
| 18 | The Believers' Reward | Sin–Mercy Economy | 448 | Alh, Amn, rHm, kwn, qwl |
| 19 | Revelation, Speech & Disbelief | Jihād fī Sabīl Allāh | 425 | Alh, **sbl** (path), qwl, kwn, **qtl** (kill) |
| 20 | The Believers' Reward | Household Law & Lineage | 422 | Alh, Amn, qwl, kwn, rbb |

**`Alh` (الله, Allah)** appears as a top bridge in *every single one of the 20
strongest cluster pairs*. It is the gravitational centre. The two next-most
universal bridges are `qwl` (saying) and `kwn` (being) — the verbs that
narrate everything else. After the universal trio, each pair has a **signature
bridge** that is unique to it: `nfs` for "Speech ↔ Self", `kfr` and `E*b` for
"Speech ↔ Fire", `sbl` and `qtl` for "Speech ↔ Jihad", `rHm` and `gfr` for
"Worship ↔ Mercy", `$yA` and `kll` for "Speech ↔ Will". Reading down the
"signature" column is essentially a one-line summary of each pair's theology.

## Inter-cluster centrality (named clusters only)

| Rank | Cluster | Total shared ayahs | Partners (of 14) |
|------|---------|--------------------|------------------|
| 1 | **Revelation, Speech & Disbelief** | 11,396 | 14 |
| 2 | Allegiance & the Object of Worship | 8,972 | 14 |
| 3 | The Believers' Reward | 6,578 | 14 |
| 4 | The Commanded Self | 4,535 | 14 |
| 5 | Household Law & Lineage | 3,771 | 14 |
| 6 | Sin–Mercy Economy | 3,660 | 14 |
| 7 | Divine Will & Dominion | 3,438 | 14 |
| 8 | The Prepared Fire | 2,824 | 14 |
| 9 | Bodily Purity & Prayer | 2,390 | 14 |
| 10 | Dunya vs. Ākhirah | 2,077 | 14 |
| 11 | Jihād fī Sabīl Allāh | 2,034 | 14 |
| 12 | Witnessing the Visible Sign | 1,960 | 14 |
| 13 | Sea-Rescue / Bounty / Gratitude | 1,700 | 14 |
| 14 | Creation & the Appointed Term | 1,411 | 14 |
| 15 | **Vegetative Signs / Reflective Gaze** | 792 | 14 |

Every named cluster touches every other named cluster at least once — the 15
clusters form a complete graph. But the disparity in connection volume is
striking: the most-central cluster (Revelation/Speech) participates in
**~14× more co-occurring ayahs** than the most peripheral (Vegetative Signs).

**The most central named cluster is "Revelation, Speech & Disbelief".** It is
the discursive frame the Quran narrates everything *through* — every other
theme (worship, reward, fire, jihad, household law, mercy) gets verbalised in
the speech-act vocabulary of qwl/kwn/nzl/Aty/byn. It is the Quran's
meta-cluster.

**The most isolated named cluster is "Vegetative Signs / Reflective Gaze".**
It is small (17 roots) and sits inside passages dedicated to nature-as-
evidence. Its strongest external link is to "Revelation, Speech & Disbelief"
(151 ayahs, via `Hbb`-grain, `nbt`-vegetation, and the framing verbs). Its
weakest is to "Creation & the Appointed Term" (only 17 ayahs) — surprising,
because both seem to be "creation" themes. The reason: "Creation & Appointed
Term" centres on `xlq` (cosmogonic creation) and `Ajl` (term/deadline), which
operate at cosmic scale, whereas Vegetative Signs is the local agronomic
vocabulary (`zrE`, `nbt`, `vmr`, `Enb`). They are two different "creation"
discourses that the Quran rarely mixes.

Also peripheral: **Creation & the Appointed Term** (1,411) and **Sea-Rescue /
Bounty / Gratitude** (1,700). These are tightly self-contained narrative
modes — Creation tends to occur in formulaic cosmological openings, and Sea-
Rescue is mostly tied to its own boat-storm-deliverance scene.

## Surprising bridges and missing bridges

**Surprise 1: Bodily Purity & Prayer ↔ Jihād fī Sabīl Allāh** (86 ayahs).
Not a top-30 connection by volume, but the bridge-root list is theologically
striking. After the universal `Alh`, the top bridges are `nfq` (spend, 28),
`qwm` (stand, 25), `Slw` (prayer, 24), and `wjd` (find, 22). These ayahs
are the famous "**establish prayer and spend in Allah's path**"
combinations (e.g. 2:3, 8:3, 9:71). Prayer and warfare are bridged by
*economic action* — spending — and by the *act of standing* (`qwm`), which
serves both as ritual posture and battlefield posture. The fact that this
bridge exists *at all* (and via these specific roots) is the Quranic ethic
of integrated worship-as-struggle in compressed form.

**Surprise 2: Vegetative Signs ↔ The Prepared Fire** (only 30 ayahs).
The bridge roots are `Hbb` (love/grain) and `kfr` (disbelief). Two readings:
"the disbelievers love this passing life like vegetation that withers" — i.e.
vegetation is invoked rhetorically to indict the disbeliever. Vegetation is
almost never invoked alongside hellfire directly; when the two co-occur, it
is parabolic.

**Surprise 3: Sin–Mercy Economy ↔ Bodily Purity & Prayer** (133 ayahs).
The bridge roots `rHm`, `gfr`, `byn` show that ritual prayer is consistently
framed as the *site of forgiveness* — not as a separate ritual sphere but as
the space where the sin-mercy transaction happens.

**Surprise 4: Divine Will & Dominion ↔ Creation & Appointed Term** (121
ayahs). The bridge is `xlq` (create), `$yA` (will), `kll` (every), `mlk`
(king). These ayahs are the cosmological power-claims: "He created
everything and He wills, owns everything." Two clusters that look alike
*are* alike — and the bridge roots are the few words that bind them.

**Missing bridge: Sea-Rescue ↔ Vegetative Signs** (only 25 ayahs).
Both are "sign-of-Allah" narrative modes (rescue at sea, growth on land), but
they are almost never deployed together. The Quran deploys them as
*alternative* arguments rather than parallel ones in any given ayah.

**Missing bridge: Creation & Appointed Term ↔ Vegetative Signs** (only 17
ayahs). As noted above, the Quran has *two distinct creation discourses*: a
cosmic-scale one (heaven/earth/term) and a local-scale one (seed/sprout/
fruit). They appear in different surahs and rarely interlace.

## Low-frequency outsized bridges (the "small but pivotal" roots)

These roots appear under 50 times yet score in the top of the bridge index —
they punch far above their frequency.

| Root | Arabic | Count | Entropy | Touches | Note |
|------|--------|-------|---------|---------|------|
| sqy | سقي | 25 | 3.54 | 67 clusters | water-as-mercy / paradise-rivers / hell-water |
| Zll | ظلل | 33 | 3.44 | 60 | shade as paradisiacal *and* hellish symbol |
| $jr | شجر | 27 | 3.36 | 58 | a single root carrying Eden's tree, Zaqqum, the Bayʿa tree |
| TlE | طلع | 19 | 3.35 | 51 | "rising" — sun, Zaqqum-shoots, gaze |
| nbt | نبت | 26 | 3.33 | 62 | Mary's "good growth", resurrection-as-vegetation |
| g$w | غشو | 29 | 3.28 | 54 | "covering" — night, veil over hearts, the overwhelming Day |
| wDE | وضع | 26 | 3.28 | 65 | place / lay down arms / give birth / scales |
| fjr | فجر | 24 | 3.28 | 46 | dawn-prayer / split rock / moral fujur |

These are *high-value research targets*: each one is a single Arabic root
that the Quran reuses across radically different scenes, holding distant
themes together by image.

## Takeaway

The Quranic semantic graph is bound together by three overlapping layers:

1. **Theological frequency hubs** — `Alh`, `qwl`, `kwn`, `Amn`, `rbb` —
   that participate in every cluster pair but whose distribution stays
   concentrated near their home cluster.
2. **Discursive bridges** — `qwl`, `nzl`, `Aty`, `byn` — that route the
   speech-act framing of the Quran across all thematic territory. This is
   why Cluster 4 (Revelation/Speech) is the Quran's meta-cluster.
3. **Sensory-image bridges** — `mwh`, `Akl`, `Drb`, `xrj`, `rAy`, `Zll`,
   `Hbb`, `sjd`, `nbt` — physical roots that the Quran deliberately
   redeploys across paradise, hell, creation, ritual, and ethics. These
   are the *load-bearing connective tissue*: a single image (water,
   shade, fruit, eye) ties otherwise distant clusters into a unified
   imaginative world.

For follow-up research the highest-leverage roots are those in layer 3 —
the sense-image bridges, especially the low-frequency outsized ones
(`sqy`, `Zll`, `$jr`, `TlE`, `nbt`). They are the seams.
