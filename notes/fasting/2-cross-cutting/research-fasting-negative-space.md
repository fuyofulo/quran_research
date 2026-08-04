# Cross-cutting: the negative space of the Quranic fast

## Headline finding (100 words)

The Quran legislates an emptying and specifies almost nothing to put in it. Exhaustive root inventory of 2:183–187 (172 words, 60 roots, verified in `words.jsonl`): **no `Slw` (prayer), no `*kr` (remembrance), no `sbH`, no `qlb` (heart), no `nwr`, no `Ajr`, no `gfr`, no `jnn`.** `Swm` and `Slw` share **zero ayahs in the entire Quran**. No word for breaking a fast (`fTr` never touches a fasting verse); no `ʿīd`; no `suḥūr`. Meanwhile the same book calls self-imposed prohibition `iʿtidāʾ` (5:87) and says of monasticism *mā katabnāhā* — using the exact verb it used to prescribe the fast.

---

## How every absence below was verified

Three deterministic instruments: (a) the 60-root inventory of 2:183–187, recomputed from `data/morphology/words.jsonl` (172 words; matches `fasting-cooccurrence.json`'s `roots_in_passage_2_183_187`); (b) the full **133-root** set sharing any ayah with `Swm` across all 11 `Swm` ayahs, recomputed the same way; (c) whole-corpus root refs from `words.jsonl` per candidate root. Every claimed absence was searched by Buckwalter code in (a) and (b) and returned `False`.

---

## 1. No stated duration for a voluntary fast — and `taṭawwaʿ` probably isn't fasting

**Data-grounded.** Every number the Quran attaches to fasting is legislated and non-optional: a month (2:185), 3 days (5:89), 3+7=10 days (2:196), 2 consecutive months (4:92, 58:4), `ʿadl dhālika ṣiyāman` (5:95, unnumbered). **The only "seven" in the corpus is 2:196's** `wa-sabʿatin idhā rajaʿtum` — seven days *after returning from hajj*, the back half of a ten-day substitute for a sacrificial animal a pilgrim cannot afford. There is no seven-day devotional fast in the Quran. There is no Quranic number for a voluntary fast at all.

That leaves one candidate for voluntary fasting anywhere in the text: 2:184's `fa-man taṭawwaʿa khayran`.

> **2:184 (excerpt)** — وَعَلَى ٱلَّذِينَ يُطِيقُونَهُۥ فِدۡيَةࣱ طَعَامُ مِسۡكِينࣲۖ **فَمَن تَطَوَّعَ خَيۡرࣰا فَهُوَ خَيۡرࣱ لَّهُۥ**ۚ وَأَن تَصُومُواْ خَيۡرࣱ لَّكُمۡ
> *Saheeh:* "…a ransom of feeding a poor person. **And whoever volunteers excess** — it is better for him. But to fast is best for you…"
> *Khattab:* "…compensation by feeding a needy person. **But whoever volunteers to give more**, it is better for them. And to fast is better for you…"
> *Arberry:* "…a redemption by feeding a poor man. **Yet better it is for him who volunteers good**, and that you should fast is better for you…"
> *Pickthall:* "…a ransom: the feeding of a man in need — **but whoso doeth good of his own accord**, it is better for him: and that ye fast is better for you…"

**The referent is genuinely open, and three of four translators refuse to name it.** Only Khattab commits — and he commits to *giving*, not fasting.

Two data points push toward feeding. **Position**: the clause sits immediately after the *fidya* and immediately before `wa-an taṣūmū khayrun lakum` — a separate clause, introduced by `wa-`, naming fasting explicitly. If `taṭawwaʿa khayran` already meant "fast extra," that clause is redundant. Stronger: **`taṭawwaʿa` occurs exactly twice in the Quran** — 2:184 and **2:158**, in the identical formula `fa-man taṭawwaʿa khayran`. 2:158 is about ṣafā and marwā, with no fasting in view. The phrase is a reused general good-works formula, not a fasting term. (Verified: `TwE`, lemma `taTaw~aEa`, 2 occurrences.)

**Interpretive.** The one possible licence for voluntary fasting is a sentence that, on the evidence of its only twin, most likely means "whoever does extra good." Maryam's `nadhr` (19:26) is the sole narrated self-imposed fast — of speech, not food, narrated rather than commanded. **The text does not prescribe, number, or name a voluntary fast from food.**

## 2. No prescribed programme inside the fast

**Data-grounded, exhaustive.** I tagged every verb in 2:183–187 by mood. The passage contains **five imperatives, all in 2:187**: `bāshirūhunna` (have relations), `wa-btaghū` (seek what God has decreed), `wa-kulū` (eat), `wa-shrabū` (drink), `atimmū al-ṣiyām` (complete the fast). **Four of the five imperatives in the entire fasting passage are permissions to eat, drink and have sex.** The fifth says finish the fast.

The jussives add: `fal-yaṣumhu` (let him fast it, 185), `fal-yastajībū lī` + `wal-yuʾminū bī` (let them respond to Me and believe in Me, 186), plus two prohibitions (`lā tubāshirūhunna` during iʿtikāf, `lā taqrabūhā`). The purpose-subjunctives add `wa-li-tukmilū al-ʿidda` (complete the count — administrative) and `wa-li-tukabbirū Allāha ʿalā mā hadākum` (magnify God for guiding you).

So the complete positive devotional content of the Quran's fasting legislation is: **magnify God for guidance; respond to Him; believe in Him.** Three items. Nothing else.

And the roots that are *not* there, checked by code against the 60-root inventory: **`Slw` (prayer) — absent. `*kr` (dhikr) — absent. `sbH` — absent. `zkw` — absent. `qlb` (heart) — absent. `gfr` — absent. `Ajr` — absent. `jnn` (garden) — absent.** `qrA` occurs once, as the *noun* al-Qurʾān in 2:185; there is **no command to recite in the passage**. Widening to all 11 `Swm` ayahs: **`Swm` and `Slw` share zero ayahs in the whole Quran.** The Quran never once puts fasting and prayer in the same verse.

**Interpretive.** The Quran legislates the emptying with precision and leaves the filling unspecified. Everything the tradition puts inside Ramadan (tarāwīḥ, khatm al-Qurʾān, dhikr, nightly duʿāʾ) is built on ground the text left bare — not a criticism of the tradition, a statement about where the authority for a fast's *content* comes from, which is not this passage.

## 3. No experiential vocabulary — the Quran reserves it for hearing, not hunger

**Data-grounded.** Nothing in the 133-root `Swm` set encodes a felt state: no `nwr` (light), no `q$Er` (shiver), no `Tmn` (settling of the heart), no `qlb` at all, no `rwH`/`Rūḥ`, no `mlk` (angels), no `Hlw` (sweetness). The one affective phrase in any `Swm` ayah is 19:26's `wa-qarrī ʿaynan` — "let your eye be cooled" — and it is attached to `fa-kulī wa-shrabī`, **eat and drink**, not to the abstention.

What the Quran *does* give experiential language to:

> **39:23** — تَقۡشَعِرُّ مِنۡهُ جُلُودُ ٱلَّذِينَ يَخۡشَوۡنَ رَبَّهُمۡ ثُمَّ تَلِينُ جُلُودُهُمۡ وَقُلُوبُهُمۡ إِلَىٰ ذِكۡرِ ٱللَّهِ
> "The skins of those who fear their Lord shiver from it; then their skins and their hearts soften to the remembrance of God."

`q$Er` is a **hapax legomenon** — one occurrence in the Quran (verified, whole-corpus scan) — and it is spent on the effect of *hearing the Book*. Add 8:2 (`wajilat qulūbuhum`, hearts tremble at God's mention — root `wjl`, 5 occurrences, never with `Swm`), 13:28 (`taṭmaʾinnu al-qulūb bi-dhikri Allāh`), 73:6 (`nāshiʾat al-layl … ashaddu waṭʾan wa-aqwamu qīlā`), 17:79 (`maqāman maḥmūdā`), 32:16 (sides forsaking beds). **Every experiential state the Quran describes is attached to recitation, remembrance, or the night vigil. None is attached to fasting.**

**Interpretive.** If someone fasts and feels nothing, the Quran never promised otherwise. It attaches the shiver to the Book.

## 4. No asceticism — the text rejects the principle explicitly

This is the largest finding in the file, and the verb makes it.

> **57:27** — وَرَهۡبَانِيَّةً ٱبۡتَدَعُوهَا **مَا كَتَبۡنَٰهَا عَلَيۡهِمۡ**
> "And monasticism — they invented it; **We did not prescribe it upon them**."

`rahbāniyya` is a **hapax** (root `rhb`, 12 occurrences, this lemma once — verified). `ibtadaʿūhā` is root `bdE` — they innovated it. And `mā katabnāhā ʿalayhim` is root **`ktb`, lemma `kataba`** — **the identical lemma as 2:183's `kutiba ʿalaykumu al-ṣiyām`.** The Quran uses one verb to prescribe the fast and to disown monasticism, with the same preposition (`ʿalā`) on both. That is not a thematic parallel; it is the same word, checked in the morphology.

> **5:87** — لَا تُحَرِّمُواْ طَيِّبَٰتِ مَآ أَحَلَّ ٱللَّهُ لَكُمۡ **وَلَا تَعۡتَدُوٓاْ** إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلۡمُعۡتَدِينَ
> "Do not forbid the good things God has made lawful for you, **and do not transgress**. God does not love the transgressors."

**Data-grounded and decisive:** the verb paired with self-imposed prohibition is `taʿtadū`, root **`Edw`** — the Quran's word for *transgressing limits*. Renouncing the lawful is not classified as a lesser virtue; it is filed under transgression, in a verse whose four translators agree completely. 7:31 adds `wa-kulū wa-shrabū wa-lā tusrifū` — eat and drink, don't be excessive — and 7:32 asks `man ḥarrama zīnata Allāh?` ("who has forbidden God's adornment?"), a rhetorical question with no defensible answer.

**Interpretive, load-bearing:** the distinction is *who forbids, and for how long*. God may suspend the lawful — dated, bounded, dawn-to-night, one named month, with exits. **A person may not.** Ramadan is not an exception to 5:87; it demonstrates who holds that authority. A self-imposed fast undertaken as self-denial-for-its-own-sake runs against 5:87's grain, not with it. The fast is a *bounded suspension of the lawful by its owner*, not a renunciation of it.

## 5. No solitude requirement — and no community requirement either

**Data-grounded.** `jmE` (gather) is absent from the passage and from all 133 `Swm`-adjacent roots. There is no verse anywhere instructing people to fast together, to break the fast together, or to gather. There is also no instruction to withdraw. Grammatically, **the actual command to fast is singular** — 2:185's `fa-man shahida minkumu al-shahra fal-yaṣumhu`, third-person masculine singular — as are both exemption clauses (`fa-man kāna minkum marīḍan`).

The one spatial instruction in the entire passage is 2:187's `wa-antum ʿākifūna **fī al-masājid**` — *in the mosques*, plural, a communal space. Note its grammar: it appears inside a **prohibition** (`wa-lā tubāshirūhunna` — do not have relations while in iʿtikāf) as a circumstantial clause. **Iʿtikāf is never commanded in the Quran; it is presupposed and then regulated.** (`Ekf` root, 2:187, verified — and per the ramadan-qadr file, the same lemma names devotion to idols in 5 of its other 8 uses.)

Contrast **62:9**, which *does* command assembly — but for prayer, not fasting. And the corpus contains no `ʿīd` for the fast: `ʿīd` occurs **exactly once** (5:114, the disciples' table from heaven), and the root `fTr` — the root of *fiṭr*, breaking the fast — occurs 19 times, **none of them in a fasting verse** (all are God as `Fāṭir`, the `fiṭra`, or the sky splitting). **There is no Quranic word for breaking a fast, no Quranic ʿīd al-fiṭr, and no `suḥūr`** — 2:187's dawn word is `al-fajr`.

## 6. The exemptions are generous, repeated, and outnumber the restrictions

**Data-grounded, counted clause by clause across the five verses.**

| | Relief clauses | Restrictive clauses |
|---|---|---|
| 2:183 | 0 | 1 (`kutiba ʿalaykum`) |
| 2:184 | 3 (illness, travel, *fidya*) | 1 (`ayyāman maʿdūdāt`) |
| 2:185 | 3 (illness, travel, `yusr` not `ʿusr`) | 1 (`fal-yaṣumhu`) |
| 2:186 | — | — |
| 2:187 | 3 (night intimacy permitted; prior breach pardoned; eat and drink till dawn) | 3 (complete till night; no relations in iʿtikāf; don't approach the limits) |
| **Total** | **9** | **6** |

**Three of the five verses (184, 185, 187) contain an exemption, an easing, or a permission** — that is *every legislative verse after the bare decree*; the two that don't are the 14-word decree itself and 2:186, which isn't legislative. Illness and travel are stated **twice, verbatim**, in consecutive verses. And 2:185 states the principle behind the repetition: `yurīdu Allāhu bikumu al-yusra wa-lā yurīdu bikumu al-ʿusr`.

**Interpretive.** A legislator who repeats the exemptions verbatim in consecutive verses, states ease as a principle, then pardons the community for breaking the rule before relaxing it (2:187), is not treating difficulty as the payload. The 9:6 ratio and the doubled exemption are the text arguing against its own severity.

---

## What is the shape of the hole?

Put every absence in one frame. The Quran fixes the **container** with unusual precision: which month and why (a revelation happened in it), which hours (a perceptible dawn to night), what is suspended, who is excused, how it is made up, what it substitutes for. And it specifies the **contents** almost not at all: no prayer, no recitation command, no dhikr, no intention, no number for a voluntary fast, no promised reward, no described experience, no gathering, no solitude, no word for beginning or ending it.

**The shape of the hole is the shape of the fast's own hours.** The Quran empties a block of time and hands it over unfurnished. It rules out one thing about the furnishing — suffering is not it (`yurīdu Allāhu bikumu al-yusra`, and 5:87's `lā taʿtadū`) — and states one hope about the outcome, twice, with `laʿalla`: perhaps you will guard yourselves. Everything between the emptying and the hope is left to the person fasting.

That is not an oversight, and it is not permission to fill it with anything. It is a division of labour. **The text supplies the vacancy; you supply the occupancy** — and because the text never named the contents, the contents are the one part of a fast that is genuinely yours, and therefore the one part that can actually fail. Seven days of hunger with nothing put into the hole is not a fast that went wrong. On this evidence it is a fast that was never furnished.

## For the fast

- Fast lawfully, not ascetically. 5:87 files self-imposed prohibition under `iʿtidāʾ`; 57:27 uses the same verb to prescribe the fast and to disown monasticism. Renunciation as a virtue is a position this book already rejected.
- The Quran gives you three things to *do* in a fast — magnify God for guidance, respond to Him, believe. Everything else you put in is yours to choose and yours to be accountable for.
- Expect nothing to be felt. The shiver (39:23), the trembling heart (8:2), the settled heart (13:28) are attached to the Book and to remembrance. If you want those inside a fast, bring the Book into it — the fast will not produce them.
- Take the exits. Nine relief clauses to six restrictions, illness and travel stated twice, ease stated as principle. A fast you had to break is inside the text's design, not outside it.
- Don't build a devotional fast on a number. The Quran has no number for one; its only "seven days" is a hajj substitute. Whatever length you choose, choose it for a reason you can state.
- Fast alone or with others — the text requires neither. Its single spatial word is `fī al-masājid`, plural, and it arrives inside a prohibition regulating a retreat it never commanded.
- Furnish the hours before you enter them. That is the whole practical yield of this file.
