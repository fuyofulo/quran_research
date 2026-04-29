# Research: Hapax Day-Names — the Quran's Affect Catalog of the End

**Phase 3 rabbit-hole, Quran-TIME deep-dive**
**Method:** corpus search over `data/morphology/words.jsonl` (root-anchored on `ywm`, then partner-lemma frequency); cross-checked against four published English translations and `data/structural/translation-divergence.json`.
**Scope:** every `yawm + X` construction whose partner term occurs **exactly once** as the construct partner of `yawm`, plus a handful of repeated-but-rare comparators used as foils.

---

## 1. Headline

The Quran names the eschatological Day with a small, fixed vocabulary that everyone knows — *yawm al-qiyāma* (70x), *al-yawm al-ākhir* (26x), *yawm al-dīn* (13x), *yawm al-faṣl* (6x), *yawm al-ḥisāb* (4x). But running underneath that frozen credal layer is a much larger and stranger system: roughly **20 single-use coinages** in which the Day is named only once, never repeated, each name supplying a different psychological or scenic register. *yawm al-ḥasra* (Day of Regret), *yawm al-taghābun* (Day of Mutual Loss), *yawm al-tanād* (Day of Mutual Calling), *yawm al-āzifa* (Day of the Imminent), *yawm al-khurūj* (Day of Coming-Out), *yawm al-khulūd* (Day of Eternity), *yawm ʿaqīm* (Barren Day), *yawm al-waʿīd* (Day of the Threat), *yawm al-mawʿūd* (the Promised Day), *yawm al-ḥaqq* (the True Day) — and many more. Each is a *hapax legomenon* in this construct.

The argument of this note is that the hapax day-names are the Quran's **affect catalog of the End**: they refract a single referent (the Day) through a deliberately non-repeating sequence of emotional, sensory, social, and theological registers. The frozen names do credal work; the hapax names do **rhetorical, persuasive, sensory** work. Together they give the Day a shape that no single name can hold.

A second finding falls out of the same data: the hapax catalog is **lopsided**. Almost every hapax is built on regret, severity, distress, exposure, finality, and threat. There is **no** *yawm al-raḥma* (Day of Mercy), no *yawm al-naʿīm* (Day of Bliss), no *yawm al-ghufrān* (Day of Forgiveness), no *yawm al-salām* (Day of Peace), no *yawm al-jannah* (Day of the Garden) anywhere in the construct-partner position. Mercy, forgiveness, garden, and peace are *all over* the surrounding text — but they are not allowed to *name* the Day. The naming-of-the-Day is reserved for the registers of judgment and rupture. That asymmetry is itself a finding.

---

## 2. Verified hapax catalog

Method: I extracted every word with `root == ywm` (405 occurrences, ~131 distinct surface forms), then for each took the immediately following word's `lemma_arabic` as the construct partner, and counted. The results below are construct-partner hapax (count = 1 in this position). Where a *yawm + X* construction is a true single-use noun-coinage for the Day itself, it is in **bold**; non-eschatological singletons (e.g., *yawm al-ḥajj*, *yawm ḥaṣād*) are listed at the end for completeness.

### 2a. Definite-construct hapax day-names (the eschatological core)

| # | Citation | Arabic | Working translation | Surah revelation |
|---|---|---|---|---|
| 1 | **[19:39]** | يَوْمَ ٱلْحَسْرَةِ | **Day of Regret / Anguish** | Meccan |
| 2 | **[20:59]** | يَوْمُ ٱلزِّينَةِ | Day of the Festival / Adornment (Pharaoh contest) | Meccan |
| 3 | **[26:189]** | يَوْمِ ٱلظُّلَّةِ | Day of the [black] Cloud / Canopy (Shuʿayb's people) | Meccan |
| 4 | **[32:29]** | يَوْمَ ٱلْفَتْحِ | Day of the Decision / Conquest | Meccan |
| 5 | **[40:15]** | يَوْمَ ٱلتَّلَاقِ | **Day of Meeting / Encounter** | Meccan |
| 6 | **[40:18]** | يَوْمَ ٱلْءَازِفَةِ | **Day of the Imminent / the Approaching One** | Meccan |
| 7 | **[40:30]** | يَوْمِ ٱلْأَحْزَابِ | Day of the Confederates (the destroyed peoples) | Meccan |
| 8 | **[40:32]** | يَوْمَ ٱلتَّنَادِ | **Day of the Mutual Calling-Out** | Meccan |
| 9 | **[50:20]** | يَوْمُ ٱلْوَعِيدِ | **Day of the Threat / what was warned** | Meccan |
| 10 | **[50:34]** | يَوْمُ ٱلْخُلُودِ | **Day of Eternity / Immortality** | Meccan |
| 11 | **[50:42]** | يَوْمُ ٱلْخُرُوجِ | **Day of Coming-Out (from the graves)** | Meccan |
| 12 | **[62:9]** | يَوْمِ ٱلْجُمُعَةِ | Day of Congregation (Friday) — *liturgical, not eschatological* | Medinan |
| 13 | **[64:9]** | يَوْمُ ٱلتَّغَابُنِ | **Day of Mutual Loss / Mutual Disillusion** | Medinan |
| 14 | **[78:39]** | ٱلْيَوْمُ ٱلْحَقُّ | **the True Day / the Day of Truth** | Meccan |
| 15 | **[85:2]** | وَٱلْيَوْمِ ٱلْمَوْعُودِ | **the Promised Day** (oath formula) | Meccan |

### 2b. Indefinite hapax day-name coinages (yawm + qualifier, exactly once)

These are not construct chains with *al-* but they function as one-time naming-the-Day-by-attribute formulas.

| # | Citation | Arabic | Working translation | Surah |
|---|---|---|---|---|
| 16 | **[11:3]** | يَوْمٍ كَبِيرٍ | a Great Day | Hud (Meccan) |
| 17 | **[11:26]** | يَوْمٍ أَلِيمٍ | a Painful Day | Hud (Meccan) |
| 18 | **[11:77]** | يَوْمٌ عَصِيبٌ | a Distressing Day (Lot) | Hud (Meccan) |
| 19 | **[11:84]** | يَوْمٍ مُّحِيطٍ | an Encompassing Day (Shuʿayb) | Hud (Meccan) |
| 20 | **[11:103]** | يَوْمٌ مَّجْمُوعٌ … يَوْمٌ مَّشْهُودٌ | a Day-Gathered-For / a Witnessed Day | Hud (Meccan) |
| 21 | **[14:18]** | يَوْمٍ عَاصِفٍ | a Stormy Day (in simile, not the Day directly — but the construction is hapax) | Ibrahim (Meccan) |
| 22 | **[54:8]** | يَوْمٌ عَسِرٌ | a Hard Day (disbelievers' speech) | al-Qamar (Meccan) |
| 23 | **[54:19]** | يَوْمِ نَحْسٍ | a Day of Misfortune (ʿĀd) | al-Qamar (Meccan) |
| 24 | **[74:9]** | يَوْمٌ عَسِيرٌ | a Difficult Day | al-Muddaththir (Meccan) |
| 25 | **[76:10]** | يَوْمًا عَبُوسًا قَمْطَرِيرًا | a Frowning, Severe Day | al-Insan (Medinan) |
| 26 | **[76:27]** | يَوْمًا ثَقِيلًا | a Heavy Day | al-Insan (Medinan) |
| 27 | **[90:14]** | يَوْمٍ ذِى مَسْغَبَةٍ | a Day of severe hunger (charity context, not the Day proper) | al-Balad (Meccan) |

### 2c. Non-eschatological yawm-construct singletons (for completeness only)

| Citation | Arabic | Sense |
|---|---|---|
| [6:141] | يَوْمَ حَصَادِهِ | day of its harvest (zakat law) |
| [7:163] | يَوْمَ سَبْتِهِمْ | their Sabbath day |
| [8:41] | يَوْمَ ٱلْفُرْقَانِ | day of the Criterion (= Badr) |
| [9:3] | يَوْمَ ٱلْحَجِّ | Day of the [greater] Pilgrimage |
| [9:25] | يَوْمَ حُنَيْنٍ | Day of Hunayn |
| [9:36] | يَوْمَ خَلَقَ | day He created (the heavens) |
| [16:80] | يَوْمَ ظَعْنِكُمْ … وَيَوْمَ إِقَامَتِكُمْ | day of your travel / your stay |

These are interesting because they show the *yawm + X* construct is a fully **generative** linguistic device — it can name historical battles (*yawm Ḥunayn*), legal occasions (*yawm al-jumʿa*, *yawm ḥaṣād*), Mosaic episodes (*yawm al-zīna*), or the eschatological Day itself. The grammar is identical; the referent shifts. The Quran exploits this generativity.

### 2d. The four "frozen" comparators

For contrast, here are the *non*-hapax day-names — the credal vocabulary:

| Name | Count | First occurrences |
|---|---|---|
| *yawm al-qiyāma* | 70 | [2:85] etc. |
| *al-yawm al-ākhir* | 26 | [2:8] etc. |
| *yawm al-dīn* | 13 | [1:4] etc. |
| *yawm al-faṣl* | 6 | [37:21], [44:40], [77:13], [77:14], [77:38], [78:17] |
| *yawm al-ḥisāb* | 4 | [38:16], [38:26], [38:53], [40:27] |
| *yawm al-jamʿ* | 2 + variants | [42:7], [64:9] (+ 64:9 verb form, 11:103 *yawm majmūʿ*) |
| *yawm al-baʿth* | 2 | [30:56] (twice, same ayah) |
| *yawm al-waqt al-maʿlūm* | 2 | [15:38], [38:81] |

The frozen names are **almost all definite construct chains** with abstract nouns — *resurrection*, *the last*, *judgement*, *separation*, *reckoning*, *gathering*, *raising*, *the appointed time*. They are denotative, theological, repeatable. They could fit on a creed.

---

## 3. Reading each hapax in context

I quote the Day-naming verse plus the immediate envelope, with the four published translations. Where the four diverge sharply I flag it.

### 3.1 yawm al-ḥasra — "the Day of Regret" [19:39]

> فَأَنذِرْهُمْ يَوْمَ ٱلْحَسْرَةِ إِذْ قُضِىَ ٱلْأَمْرُ وَهُمْ فِى غَفْلَةٍ وَهُمْ لَا يُؤْمِنُونَ

- Saheeh: "warn them … of the Day of Regret, when the matter will be concluded; and [yet], they are in [a state of] heedlessness"
- Pickthall: "the Day of anguish when the case hath been decided"
- Khattab: "the Day of Regret, when all matters will be settled"
- Arberry: "the day of anguish, when the matter shall be determined"

Context: the surah has just (vv. 37–38) condemned the sectarians who differed about Jesus and described how clearly they will hear and see "the Day they come to Us." Then this verse names the Day **by what the disbelievers will feel on it**. *Ḥasra* in classical Arabic is the regret of someone who realises too late — when "the matter has been concluded" (*quḍiya al-amr*) and nothing more can be done. The naming is psychologically precise: the Day is named not by what happens *on* it but by the affect the heedless will feel *because* of it. **Translator divergence**: mid (Jaccard ~0.34–0.43); Pickthall and Arberry pick the more general "anguish," Saheeh and Khattab keep the sharper "regret."

### 3.2 yawm al-zīna — "the Day of the Festival" [20:59]

> قَالَ مَوْعِدُكُمْ يَوْمُ ٱلزِّينَةِ وَأَن يُحْشَرَ ٱلنَّاسُ ضُحًى

This one is **not** an eschatological day-name. Moses sets the appointment with Pharaoh's magicians for a public festival day (*yawm al-zīna*). I include it because it is a hapax *yawm + al-X* construct, and because the construct-grammar is identical to the eschatological hapax. The Quran can mint a one-time day-name for a story-internal occasion the same way it mints one for the End. The same generative grammar.

### 3.3 yawm ʿaqīm — "the Barren Day" [22:55]

> وَلَا يَزَالُ ٱلَّذِينَ كَفَرُوا۟ فِى مِرْيَةٍ مِّنْهُ حَتَّىٰ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةً أَوْ يَأْتِيَهُمْ عَذَابُ يَوْمٍ عَقِيمٍ

- Saheeh: "the punishment of a barren Day"
- Pickthall: "the doom of a disastrous day"
- Khattab: "the torment of a terminating Day"
- Arberry: "the chastisement of a barren day"

This is the most lexically contested hapax in the entire catalog (Khattab is the outlier with Jaccard 0.334; the others stay closer to "barren"). *ʿaqīm* normally means "sterile, infertile" (used of a barren woman or a barren wind). Here it names a Day in which **nothing can be born from it** — no further chance, no offspring of repentance, no second day after it. Pickthall avoids the metaphor entirely and reaches for "disastrous"; Khattab interprets it as "terminating" (no day-after). Arberry and Saheeh keep the etymological metaphor and let it work. The hapax forces the translator to choose: do you preserve the strange metaphor or do you flatten it to an affect-word? Three out of four flatten it to a plain pejorative; only "barren" preserves the actual semantic of fruitlessness.

### 3.4 yawm al-ẓulla — "the Day of the [black] Cloud" [26:189]

> فَكَذَّبُوهُ فَأَخَذَهُمْ عَذَابُ يَوْمِ ٱلظُّلَّةِ ۚ إِنَّهُۥ كَانَ عَذَابَ يَوْمٍ عَظِيمٍ

This is the punishment-Day of Shuʿayb's people — a meteorological cloud-day, hapax to that episode. *Ẓulla* is "shadow, canopy, awning"; the four translators read it as "black cloud," "gloom," "deadly cloud," "Shadow." Note: the verse pairs *yawm al-ẓulla* with *yawm ʿaẓīm* (a tremendous Day) — the named one and the assessed one stand side by side. This is one of those punishment-of-past-peoples days that *also* functions as a foreshadowing of the eschatological Day; Quranic story-time and end-time bleed.

### 3.5 yawm al-talāq — "the Day of Meeting" [40:15]

> رَفِيعُ ٱلدَّرَجَٰتِ ذُو ٱلْعَرْشِ يُلْقِى ٱلرُّوحَ مِنْ أَمْرِهِۦ عَلَىٰ مَن يَشَآءُ مِنْ عِبَادِهِۦ لِيُنذِرَ يَوْمَ ٱلتَّلَاقِ

The Day named *by the encounter* — hearts meeting Lord, all souls meeting each other, the unseen meeting the seen. *talāq* (form-VI verbal noun of *l-q-y*) is reciprocal: not *al-liqāʾ* ("the meeting") but *al-talāq* ("the mutual-meeting"). The reciprocal form matters: the Day is named for the moment when concealment ends and everyone meets everyone, including God. This is one of three hapax built on the *taFāʿul* reciprocal pattern in this surah cluster (*talāq*, *tanād*, *taghābun*) — see §4 for what that means.

### 3.6 yawm al-āzifa — "the Day of the Imminent" [40:18]

> وَأَنذِرْهُمْ يَوْمَ ٱلْءَازِفَةِ إِذِ ٱلْقُلُوبُ لَدَى ٱلْحَنَاجِرِ كَٰظِمِينَ

- Saheeh: "the Approaching Day, when hearts are at the throats"
- Pickthall: "the Day of the approaching (doom)"
- Khattab: "the approaching Day when the hearts will jump into the throats"
- Arberry: "the Day of the Imminent when, choking with anguish, the hearts are in the throats"

*āzifa* is an active feminine participle from *azifa* "to draw near, be at hand" — already used in [53:57] as a name for the Hour itself (*azifati l-āzifa*, "the Imminent has drawn near"). The naming-by-imminence has its own little subgrammar in the Quran (cf. *al-ḥāqqa*, *al-qāriʿa*, *al-ghāshiya*). Translator divergence: mid (Jaccard 0.34–0.43); only Arberry keeps the strange "Imminent" as a substantive.

### 3.7 yawm al-aḥzāb — "the Day of the Confederates" [40:30]

The believer-from-Pharaoh's-house warns: "I fear for you a fate like the day of the confederates — like the custom of Noah's people, ʿĀd, Thamud …" Here the Day-name is a **historical-typological** name: the Day of all the destroyed coalitions of past prophet-rejection. The Day of Judgement is being foreshadowed by a composite of past punishment days. Hapax-of-aggregation.

### 3.8 yawm al-tanād — "the Day of Mutual Calling-Out" [40:32]

> وَيَٰقَوْمِ إِنِّىٓ أَخَافُ عَلَيْكُمْ يَوْمَ ٱلتَّنَادِ ۞ يَوْمَ تُوَلُّونَ مُدْبِرِينَ

- Saheeh: "Day of Calling"
- Pickthall: "Day of Summoning"
- Khattab: "the Day all will be crying out ˹to each other˺"
- Arberry: "the Day of Invocation"

Khattab is the outlier (Jaccard 0.402). Like *talāq*, *tanād* is a *taFāʿul* reciprocal verbal noun — *not* "the calling" but "the mutual calling-out." The next ayah glosses it: "the Day you will turn your backs fleeing" — a panic-day on which everyone shouts to everyone else for help that no one can give. The four translators struggle: only Khattab brings out the reciprocal force ("crying out to each other"); the others domesticate it to a single calling-event. **The reciprocal form is the entire point** and it is the thing the translators most often lose.

### 3.9 yawm al-waʿīd — "the Day of the Threat" [50:20]

> وَنُفِخَ فِى ٱلصُّورِ ۚ ذَٰلِكَ يَوْمُ ٱلْوَعِيدِ

The Day named by **the speech-act that constituted it in advance**. Throughout the Quran God *threatens* (*waʿada* in its negative inflection, *waʿīd*); the Day is the redemption of those threats — the moment the *waʿīd* becomes the *yawm*. It is a Day named retrospectively-by-its-prediction. Compare 50:14 just above ("each one denied the messengers, so My threat came true").

### 3.10 yawm al-khulūd — "the Day of Eternity" [50:34]

> ٱدْخُلُوهَا بِسَلَٰمٍ ۖ ذَٰلِكَ يَوْمُ ٱلْخُلُودِ

This is the **single positive hapax** in the entire catalog. The righteous are told "Enter [the Garden] in peace — that is the Day of Eternity." Notice the structural asymmetry: even here, the Day is *not* called *yawm al-salām* (Day of Peace) or *yawm al-jannah* (Day of the Garden) — although both *salām* and entering-the-Garden are right there in the same verse. The naming is reserved for the *temporal* attribute (immortality) rather than the affective one (peace). The Day even here is named by its *length* not by its *flavour*. (And note: this verse has the *lowest divergence* of any hapax day-name — Jaccard 0.65–0.77 across translators, regime "low." When all four translators agree, it is precisely the one positive hapax. The credal repertoire for paradise is settled in a way the credal repertoire for judgement is not.)

### 3.11 yawm al-khurūj — "the Day of Coming-Out" [50:42]

> يَوْمَ يَسْمَعُونَ ٱلصَّيْحَةَ بِٱلْحَقِّ ۚ ذَٰلِكَ يَوْمُ ٱلْخُرُوجِ

Saheeh: "the Day of Emergence [from the graves]." The Day named by **a single verb of motion** — *xrj* (to come out). Note the deliberate cluster in surah 50 (Qaaf): *yawm al-waʿīd* [50:20], *yawm al-khulūd* [50:34], *yawm al-khurūj* [50:42] — three consecutive hapax day-names in one short Meccan surah. See §6.

### 3.12 yawm al-jumʿa — "the Day of Friday" [62:9]

The only Medinan-civic hapax day-name. *Jumʿa* (gathering) shares root *jmE* with *yawm al-jamʿ* — but here the gathering is liturgical-weekly, not eschatological. The same root is used in the surah-name and in the Friday-prayer law. This one hapax tells us the same construct-grammar that names the Day-of-the-Gathering (eschatological) also names the Day-of-the-Gathering-for-prayer (liturgical). The grammar is the same; the gathering is the figure.

### 3.13 yawm al-taghābun — "the Day of Mutual Loss / Mutual Disillusion" [64:9]

> يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ

The third *taFāʿul* reciprocal day-name, and the surah it titles. *Ghabn* in commercial Arabic is "to be cheated in a transaction"; *taghābun* is the reciprocal — every party in the transaction discovers it was cheated. The translators reach for very different glosses: Saheeh "Deprivation," Pickthall "mutual disillusion," Khattab "mutual loss and gain," Arberry "Mutual Fraud." The verse is dense: *the Day He will gather you for the Day of Gathering — that is the Day of Mutual-Loss*. Three day-names in one verse, the third one hapax. The Day of Gathering and the Day of Mutual-Loss are the **same** Day — the Quran is saying *the gathering is, by another name, a mutual-loss-discovery*.

### 3.14 al-yawm al-ḥaqq — "the True Day" [78:39]

> ذَٰلِكَ ٱلْيَوْمُ ٱلْحَقُّ ۖ فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا

After the spectacular cosmic theatre of surah al-Naba (the Spirit and the angels in rows, the silent permission-to-speak), the Day is named simply *al-yawm al-ḥaqq* — "the True Day," "the Real Day," "the Day-that-actually-is." It is the single most ontologically-loaded hapax. The Day is named by what it **is**, not what it **does**. (Khattab is divergent here, glossing as "ultimate truth" rather than the more austere "the True Day.")

### 3.15 al-yawm al-mawʿūd — "the Promised Day" [85:2]

> وَٱلسَّمَآءِ ذَاتِ ٱلْبُرُوجِ ۞ وَٱلْيَوْمِ ٱلْمَوْعُودِ ۞ وَشَاهِدٍ وَمَشْهُودٍ

Sworn-by in an oath formula. Like *yawm al-waʿīd*, the Day is named by its **prior speech-act of promising/threatening** — but here it is in the participial passive (*mawʿūd*, "the one promised"), making the Day itself the **object** of God's promise. (Lowest divergence regime: Jaccard 0.52–0.79.)

### 3.16–3.27 The indefinite hapax (yawm + adjective)

**[11:3] yawm kabīr** — a Great Day. Stated by Hud as a warning.
**[11:26] yawm alīm** — a Painful Day (Noah to his people).
**[11:77] yawm ʿaṣīb** — a Distressing Day (Lot, when the angel-guests arrive).
**[11:84] yawm muḥīṭ** — an Encompassing Day (Shuʿayb).
**[11:103] yawm majmūʿ … yawm mashhūd** — a Day-Gathered-For, a Witnessed Day.

Five hapax day-names in a single surah (surah Hud). Each is delivered as a prophet's warning to his rejecting people. This is a **structural feature of surah 11**: each prophet-rejection cycle is closed with its own one-time naming of the Day. Hud is the dense node of this entire phenomenon.

**[14:18] yawm ʿāṣif** — a Stormy Day. Used in a *simile* — disbelievers' deeds are like ash that wind blows on a stormy day. Borderline case; the Day-name is metaphorical, not direct.

**[54:8] yawm ʿasir** / **[54:19] yawm naḥs** / **[74:9] yawm ʿasīr** — a Hard Day, a Day of Misfortune, a Difficult Day. Note that *ʿasir* (54:8) and *ʿasīr* (74:9) are **morphologically distinct adjectives from the same root** *Esr* — both occur exactly once. The Quran tolerates both forms but uses each only once. Surah 54 puts *yawm ʿasir* (eschatological, in the disbelievers' future speech) next to *yawm naḥs* (historical, the punishment of ʿĀd). The two hapax do the same job in two time-frames.

**[76:10] yawm ʿabūs qamṭarīr** — a Frowning, Severe Day. A double-adjective hapax: the Day has a *face* (frowning, *ʿabūs*) and a *grip* (severe, *qamṭarīr*). The most facialised day-name in the corpus.

**[76:27] yawm thaqīl** — a Heavy Day. The Day named by its weight. Disbelievers "love the immediate (*ʿājila*) and leave behind them a Heavy Day." The contrast is **light-and-quick / heavy-and-slow** — the *yawm thaqīl* is the gravity that the *ʿājila* refuses.

**[90:14] yawm dhī masghaba** — a Day of severe hunger. Charity-context (feeding the orphan on a famine day), not eschatological proper, but lexically a hapax day-construct.

---

## 4. Affect-register clustering

Once you lay the names side by side, they cluster into a small number of psychological registers. These are not authorial labels — they are emergent groupings.

### Cluster A — Regret, loss, sterility (*nothing-can-be-done* register)
- *yawm al-ḥasra* [19:39] — Day of Regret
- *yawm al-taghābun* [64:9] — Day of Mutual Loss
- *yawm ʿaqīm* [22:55] — Barren Day (nothing-can-issue-from-it)

These three name the Day by its **closure**. The matter has been concluded (*quḍiya al-amr*); the cheat has been discovered; nothing further can be born. They share an aspectual structure: looking-back-at-a-finished-thing.

### Cluster B — Approach, imminence, weight (*it-is-coming* register)
- *yawm al-āzifa* [40:18] — Day of the Imminent
- *yawm al-mawʿūd* [85:2] — the Promised Day
- *yawm al-waʿīd* [50:20] — Day of the Threat
- *yawm thaqīl* [76:27] — Heavy Day

These name the Day by its **futurity-pressing-on-the-present**. Mass, weight, threat, promise, imminence: a Day that *leans on you now*.

### Cluster C — Reciprocal social events (*everyone-with-everyone* register)
- *yawm al-talāq* [40:15] — Day of Mutual Meeting
- *yawm al-tanād* [40:32] — Day of Mutual Calling
- *yawm al-taghābun* [64:9] — Day of Mutual Loss/Discovery
- *yawm al-jamʿ* [42:7, 64:9] — Day of Gathering (rare, not strict hapax)

All four use the *taFāʿul* / *jamʿ* morphology that **encodes reciprocity or assemblage**. The Day is named by what it does to the social fabric: collapses it inward, makes everyone face everyone.

### Cluster D — Movement, motion, exit (*bodies-in-motion* register)
- *yawm al-khurūj* [50:42] — Day of Coming-Out
- *yawm al-fatḥ* [32:29] — Day of Decision/Opening
- *yawm al-ẓulla* [26:189] — Day of the Cloud (overhead motion of weather)

The Day is named by motion: bodies emerging from graves, things being opened, a cloud descending.

### Cluster E — Severity, harshness, weather (*physical-distress* register)
- *yawm ʿasir* [54:8] / *yawm ʿasīr* [74:9] — Hard Day / Difficult Day
- *yawm naḥs* [54:19] — Day of Misfortune
- *yawm ʿaṣīb* [11:77] — Distressing Day
- *yawm ʿabūs qamṭarīr* [76:10] — Frowning, Severe Day
- *yawm ʿāṣif* [14:18] — Stormy Day
- *yawm muḥīṭ* [11:84] — Encompassing Day
- *yawm alīm* [11:26] — Painful Day
- *yawm kabīr* [11:3] — Great Day

This is the largest cluster. The Day is named by its harshness as if it were weather — stormy, encompassing, difficult, frowning, painful, great. It is felt as a physical event with a face.

### Cluster F — Truth, eternity, finality (*ontology* register)
- *al-yawm al-ḥaqq* [78:39] — the True Day
- *yawm al-khulūd* [50:34] — Day of Eternity
- *yawm mashhūd* [11:103] — Witnessed Day

These are the most ontological names. The Day is named by **what it is**: real, eternal, witnessed.

### Cluster G — Threats and confederations (*historical-typology* register)
- *yawm al-aḥzāb* [40:30] — Day of the Confederates
- *yawm al-furqān* [8:41] — Day of the Criterion (= Badr)
- (cf. non-hapax *yawm al-baʿth*, *yawm al-jamʿ*)

The Day is named by reference to past punishment-coalitions or to a single decisive day in salvation history.

The clusters are not exhaustive and they overlap: *yawm al-taghābun* is in A and C; *yawm al-mawʿūd* is in B and overlaps with the credal frozen layer; *yawm muḥīṭ* sits between E and B.

But the dominant register is unmistakable. **Out of ~22 eschatological hapax day-names, only one (*yawm al-khulūd*) names the Day in a positive register**, and even that one names it by *length* not by *bliss*.

---

## 5. Why hapax? Testing the hypotheses

The brief floated four hypotheses. The data either supports or qualifies each.

### H1. Rhetorical economy — "the rhetoric of the unique"
**Supported.** Each hapax sits at a moment of intense address: *fa-andhirhum* ("warn them") opens *yawm al-ḥasra*, *yawm al-āzifa*, *yawm al-talāq*. The hapax day-name is a rhetorical *coup*: a name the audience has not heard before, used at the climax of a warning. The novelty does the persuasive work; reusing the name would dilute it.

### H2. Affect saturation — "no single image of the Day"
**Strongly supported.** The Quran is meticulously refusing to give the Day one image. It names it 22+ different ways in the hapax layer alone, plus 5+ ways in the frozen layer. This is the opposite of the rabbinic/Christian liturgical pattern where the Day collapses into a few canonical names (*Yom Hadin*, *Dies Irae*, *Day of the Lord*). The Quran's pattern is *aspectual proliferation*. The hapax names refuse the audience the comfort of having "the name" of the Day, the way frozen credal names eventually do.

### H3. Surah-fingerprinting — "each surah gets its own day-name"
**Partially supported, with one big counter-example.** Most hapax cluster as 1 per surah, distributed widely (e.g., 19, 22, 26, 32, 62, 64, 78, 85). This fits H3. **But surah Hud (11) has *five* hapax day-names**, and surah Qaaf (50) has *three*, and surah Ghafir (40) has *four*. So the rule is closer to: most surahs that touch eschatology have either zero hapax day-names or one — but a small number of surahs are **dense hapax clusters**, where the proliferation itself is structural to the surah's argument. Hud is the densest: every prophet-rejection cycle is closed with its own naming-of-the-Day.

### H4. Negative-space construction — "the Day exceeds any single name"
**Strongly supported.** The hapax catalog is the *Quran's own demonstration* that no single name suffices. Each name is followed by another name. *yawm al-jamʿ* (gathering) is glossed as *yawm al-taghābun* (mutual-loss); *yawm al-khurūj* (coming-out) is glossed as *yawm yasmaʿūn al-ṣayḥa bi-l-ḥaqq* (the day they hear the cry in truth). The text is constantly **renaming** what it has just named. The hapax pattern is the literary form of "no one name is enough."

---

## 6. Surah distribution

I sorted the hapax day-names by surah and revelation type:

| Surah | Hapax count | Period | Notes |
|---|---|---|---|
| 11 (Hud) | 5 | Meccan (mid–late) | densest cluster — one per prophet-cycle |
| 40 (Ghafir) | 4 | Meccan (late) | the *taFāʿul* trio + *aḥzāb* |
| 50 (Qaaf) | 3 | Meccan (mid) | *waʿīd*, *khulūd*, *khurūj* in 22 ayahs |
| 76 (al-Insan) | 2 | Medinan | *ʿabūs qamṭarīr*, *thaqīl* |
| 54 (al-Qamar) | 2 | Meccan | *ʿasir*, *naḥs* |
| 19, 20, 22, 26, 32, 62, 64, 74, 78, 85, 90, 14 | 1 each | various | distributed singletons |

**Findings:**

(i) **Hapax day-names are overwhelmingly Meccan** (~22 of 27, including the borderline ones). The Medinan exceptions are *yawm al-jumʿa* (62:9, liturgical), *yawm al-taghābun* (64:9, late-Meccan-or-Medinan), and *yawm ʿabūs qamṭarīr* / *yawm thaqīl* (76, possibly Meccan by some chronologies). The hapax-coining habit is a mid- and late-Meccan rhetorical practice that is largely abandoned (or absorbed into frozen vocabulary) by the Medinan period.

(ii) **The densest hapax surahs are warning-surahs centered on past-prophet-cycles**: Hud (Hud, Noah, Lot, Shuʿayb), Ghafir (Pharaoh's believing kinsman warning his people), Qaaf (general warning + resurrection theatre). The hapax day-name is the **rhetorical climax of a prophet's warning to his people**. It is a *speech-act in the mouth of a warner*. This explains why most Medinan surahs (which are concerned with community life, law, and Prophetic guidance rather than imminent-threat warning) do not coin them.

(iii) **Most hapax day-names occur in one of the standard Meccan apocalyptic surahs (40s–80s) — but not in the very-early oath-cluster (90s–114).** The very-early surahs use a different naming convention: instead of *yawm al-X* coinages, they use stand-alone *al-X* names — *al-qāriʿa* (the Calamity), *al-ghāshiya* (the Overwhelming), *al-ḥāqqa* (the Reality), *al-wāqiʿa* (the Inevitable). These are often surah-titles, and they're feminine substantive participles standing alone — the Day-as-an-event-named-by-its-character without the *yawm* prefix. So there are actually **two parallel naming systems**: the very-early *al-X* substantive system, and the mid-late *yawm al-X* construct system. The hapax catalog lives in the second system.

---

## 7. Frozen versus live names — credal versus rhetorical

The hypothesis was: the frozen names (*qiyāma*, *dīn*, *ākhir*, *faṣl*, *ḥisāb*) are CREDAL (they go in liturgy and doctrine); the hapax names are RHETORICAL (they go in persuasion).

**The data fits.**

- **Frozen names are stable across translators.** Translation divergence is low for *yawm al-qiyāma* and *yawm al-dīn*; everyone says "Day of Resurrection" and "Day of Judgement/Recompense." These names have entered the credal infrastructure of all three Abrahamic English-translation traditions.
- **Hapax names diverge sharply.** Of the 16 strict-construct hapax above, **all 16 fall in the "mid" or "low" divergence regime**, but the spread within "mid" is wide and translator-outliers are common (Khattab outlier on *ʿaqīm*, *tanād*, *ḥaqq*, *thaqīl*, *mawʿūd*; Arberry outlier on *zīna*, *fatḥ*, *ʿasir*, *majmūʿ*; Pickthall outlier on *ʿasīr*). When there is no translation precedent and no creedal anchor, every translator reaches for a different gloss.
- **Frozen names appear in formula and liturgy.** *al-yawm al-ākhir* is part of the credal formula "*āmana bi-llāhi wa-l-yawm al-ākhir*" (believe in God and the Last Day) — used 14+ times. The hapax never appear in such formulas.
- **Hapax names appear in the mouths of warners.** *yawm al-ḥasra*, *yawm al-āzifa*, *yawm al-talāq*, *yawm al-tanād* are all introduced with *fa-andhirhum* / *innī akhāfu ʿalaykum* ("warn them" / "I fear for you") — the speech-form of admonition. The frozen names show up in third-person assertion ("on the Day of Resurrection We will…"), not in second-person warning. Different speech-acts use different parts of the vocabulary.

The split is functional. Frozen vocabulary stabilises a community's *belief about* the Day. Live vocabulary destabilises an audience's *posture toward* the Day. The Quran maintains both registers in parallel.

---

## 8. Translation divergence on hapax names — quantified

From `data/structural/translation-divergence.json`, summary regime distribution of the 28 hapax verses I checked:

- **Low divergence**: 50:34 (*khulūd*), 74:9 (*ʿasīr*), 76:10 (*ʿabūs qamṭarīr*), 85:2 (*mawʿūd*) — 4 verses
- **Mid divergence**: 24 verses
- **High divergence**: 0 verses

That the hapax day-names are *not* in the high-divergence regime is itself interesting — they are difficult, but not catastrophically so. The translators reach for different glosses (different colour-words, different metaphors), but they agree on the broad domain.

The most contested hapax (lowest mean Jaccard among the four):
1. **22:55 *ʿaqīm*** — Khattab's "terminating" vs. others' "barren/disastrous" (Khattab Jaccard 0.334)
2. **40:32 *tanād*** — Khattab's "crying out to each other" vs. others' "Calling/Summoning" (Khattab Jaccard 0.402)
3. **76:27 *thaqīl*** — Khattab's "weighty" vs. others' "grave/grievous/heavy" (Khattab Jaccard 0.222)
4. **90:14 *masghaba*** — translators range from "severe hunger" (Saheeh) to "famine" (Khattab) to "hunger" (Pickthall) to "a day of hunger" (Arberry)
5. **78:39 *al-ḥaqq*** — Khattab's "ultimate truth" vs. others' "True Day"

Pattern: **Khattab is the most frequent outlier** — he tends to *interpret* the hapax (telling the reader what the metaphor means) where the others *preserve* it (giving the reader the metaphor and letting it work). On *ʿaqīm* he tells you what a barren day is *for* (it terminates); on *tanād* he tells you who is calling whom (each other); on *thaqīl* he tells you the day is consequential (weighty). This is a translation philosophy decision: Khattab's "Clear Quran" is committed to clarity-over-strangeness, and the hapax day-names are precisely the place that decision shows.

**Arberry, by contrast, preserves the strangeness most reliably** — "the Day of the Imminent," "the Day of Mutual Fraud," "the Day of Invocation" — but at the cost of comprehensibility. The hapax names are the site where translation philosophies most visibly diverge.

---

## 9. The "yawm al-X" pattern as a generative rhetorical device

Across the corpus, *yawm + X* is a fully productive linguistic construct. The Quran uses it to name:

- the eschatological Day in many registers (the catalog above)
- past historical episodes: *yawm Ḥunayn* [9:25], *yawm al-furqān = Badr* [8:41], *yawm al-aḥzāb* [40:30]
- Mosaic-era episodes: *yawm al-zīna* [20:59], *yawm al-sabt* [7:163]
- liturgical occasions: *yawm al-jumʿa* [62:9], *yawm al-ḥajj* [9:3]
- legal occasions: *yawm ḥaṣād* [6:141, harvest-zakat]
- everyday time: *yawm ẓaʿnikum wa yawm iqāmatikum* [16:80, your travel-day and your stay-day]
- creation: *yawm khalaqa* [9:36]

The same construct-grammar covers all of these. Once we see this, the hapax eschatological day-names look less like a closed set and more like **the eschatological deployment of an open productive grammar**. The Quran does not have a fixed list of names for the Day; it has a generative rule (*yawm + X*) and applies it locally as the rhetorical situation requires.

This explains why a single ayah like 64:9 can stack three day-names in twelve words: *yawma yajmaʿukum li-yawmi l-jamʿi dhālika yawmu l-taghābuni* — "the Day He gathers you for the Day of Gathering — that is the Day of Mutual Loss." The construct-grammar is so productive that the text can multiply names mid-ayah without strain.

It also connects to the Phase-2 finding (in `notes/time/research-eschatological-architecture.md`) that the Quran segments the End by **aspect, not sequence**. Each *yawm al-X* names a *facet* of the Day, not a *stage within* the Day. The Day is one event with many names because it is one event with many faces, each faced toward a different audience and a different concern.

---

## 10. Negative space — what the Day is NEVER named

I checked every ayah in which a *ywm*-rooted word is followed by a noun whose root is in the positive-affect set (*rḥm, nʿm, jnn, slm, rzq, brk, ḥsn, Tyb, rḍw, gfr*). The findings:

- **No *yawm al-raḥma*** (Day of Mercy). Anywhere.
- **No *yawm al-naʿīm*** (Day of Bliss). Anywhere.
- **No *yawm al-ghufrān*** (Day of Forgiveness). Anywhere.
- **No *yawm al-jazāʾ*** (Day of Reward) — though there is a verbal phrase *al-yawma tujzawna* ("today you are recompensed," 4 occurrences).
- **No *yawm al-salām*** (Day of Peace). The closest is 50:34 ("Enter it *bi-salām* — that is the Day of Eternity"); peace is in the verse, but the Day is not named by it.
- **No *yawm al-jannah*** (Day of the Garden). 57:12 has "yawma tarā l-muʾminīna … bushrākum al-yawma jannāt" — but *jannāt* there is the **content of the announcement**, not the construct partner of *yawm*.
- **No *yawm al-rizq*** (Day of Provision). The Garden has *rizq* in it, but the Day is not named by the provisioning.

Compare this to what the Day IS named: regret, loss, mutual-betrayal, imminence, threat, encompassment, hardness, distress, frowning, weight, severity, barrenness, gloom, storm, panic, calling-out, mass-meeting, coming-out-of-graves, eternity, truth.

This asymmetry is *the* finding. The Quran reserves the **naming-of-the-Day** for the registers of judgement, severity, and rupture, even as the **content-of-the-Day** includes mercy, garden, peace, forgiveness, and reward. **Mercy is in the Day; mercy is not the name of the Day.**

Possible readings:

- **Pastoral**: a name is what you call something when you address it. The audience the Quran is addressing — the heedless, the rejecting, the Meccan disbelievers — needs to be addressed in the register of warning. Mercy is for the believer who has already turned; warning is for the one who has not.
- **Theological**: God's mercy is *not* a counter-event to the Day, the way fire is. Mercy is the *condition* in which the Day occurs (every surah opens with the Merciful), not a property of the Day itself. The Day is the moment when Mercy gives way (provisionally, for the rejecting) to justice. So you would not name it for what *encloses* it; you would name it for what is *inside* it.
- **Rhetorical**: the unfilled position — where *yawm al-raḥma* could go — is exactly the position the audience expects to be filled. By refusing to fill it, the text refuses to let the audience metabolise the Day into something they can name comfortingly. The empty slot is doing work.

I think the third reading is closest. The Quran's hapax catalog *as a totality* is a refusal-to-name-the-Day-comfortingly. The single positive hapax (*yawm al-khulūd*) is for those *already in the Garden* — i.e., it is a name spoken from the other side of the Day. The Day-from-this-side is never named in mercy-words. From-the-other-side it can be.

---

## 11. Rabbit holes for further investigation

In rough priority order:

(a) **The *taFāʿul* reciprocal-day cluster.** *talāq* [40:15], *tanād* [40:32], *taghābun* [64:9] all use the same morphology (*taFāʿul*, form-VI verbal noun). All three are reciprocal. All three are hapax-as-day-names. There may be a *fourth* that I missed — check whether *taʾāmur*, *taqātul*, *tabāyun*, *tanāzuʿ* etc. ever attach to *yawm*. The reciprocal pattern itself is doing systematic work.

(b) **Surah Hud as a hapax-day-name laboratory.** Five hapax day-names in a single surah is anomalous. Read Hud as a structural unit and trace the prophet-cycle ↔ day-name pairing: each rejected prophet's people get their own naming-of-the-Day. Is the unique day-name *for that people* or *from that prophet's mouth*?

(c) **The Meccan-vs-Medinan pivot.** The hapax-coining habit drops off in Medinan surahs. Why? Hypothesis: Medinan rhetoric is community-formative rather than warning-rhetorical, so it leans on the credal-frozen layer for stability rather than the live-hapax layer for shock. Test by looking at whether the hapax-counts correlate inversely with surah revelation order in the conventional chronologies.

(d) **The *al-X* feminine-substantive system in early Meccan surahs.** The very early surahs (~85–114) use a *different* day-naming system: *al-qāriʿa*, *al-ghāshiya*, *al-ḥāqqa*, *al-wāqiʿa*, *al-azifa*. These are surah-titles. They differ from *yawm al-X* in that they (i) drop *yawm*, (ii) are themselves the substantive, (iii) are typically also surah-names. This is a *third* day-naming layer. Map it.

(e) **Translator philosophy diagnostic.** Khattab as the consistent "interpret-and-flatten" outlier; Arberry as the "preserve-strangeness" outlier; Saheeh and Pickthall mostly in the middle. The hapax day-names are an unusually clean test-bed for this; more general claims about each translator's philosophy could be made by extending the analysis to *all* hapax constructions, not just day-names.

(f) **The single positive hapax (*yawm al-khulūd*) and its low divergence.** This verse has the lowest divergence regime of any hapax day-name (Jaccard 0.65–0.77). The translators agree because the credal repertoire for paradise *is* settled — there is one canonical English gloss for *khulūd* ("eternity/immortality") and everyone uses it. By contrast the credal repertoire for judgement is plural. This asymmetry-of-translation-stability is itself a finding worth pursuing.

(g) **Cross-reference with the punishment-of-past-peoples cycle.** Many hapax day-names attach to a specific past-people destruction (*ẓulla* = Shuʿayb, *naḥs* = ʿĀd, *aḥzāb* = the destroyed coalitions). These historical-punishment days are *typologically* the End-Day. The hapax naming holds the historical event and the eschatological event in the same name. This is a major theological move — the historical-typological structure of Quranic eschatology should be its own deep-dive.

(h) **The *waʿd*/*waʿīd* speech-act layer.** *yawm al-waʿīd* and *yawm al-mawʿūd* both name the Day by reference to a *prior speech-act of God* (a threat or a promise). The Day is the moment a speech-act becomes an event. This is an interesting linguistic-philosophical structure: the Day is constituted-in-advance by being-spoken-of-in-advance. Worth a separate note on how the Quran uses speech-acts to constitute eschatological time.

(i) **What about *layla* (night)?** Layla also has rare construct names (*laylat al-qadr*, *layla mubāraka*). Compare the hapax-night system to the hapax-day system. (Possibly already covered in `notes/time/concept-lyl.md` — check.)

(j) **The "two-day" pattern.** Several hapax constructions name *two* Days at once (50:34 and 50:42 in the same passage; 64:9's three-day stack). Is there a structural rule about how many day-names a single surah can stack before the rhetorical effect breaks down?

---

## Files referenced

- `/Users/fuyofulo/research/quran/data/morphology/words.jsonl` — hapax verification (root=`ywm`, partner-lemma frequency)
- `/Users/fuyofulo/research/quran/data/translations/{saheeh,pickthall,khattab,arberry}.json` — context and divergence
- `/Users/fuyofulo/research/quran/data/structural/translation-divergence.json` — divergence regime per ayah
- `/Users/fuyofulo/research/quran/data/metadata/surahs.json` — Meccan/Medinan classification
- `/Users/fuyofulo/research/quran/notes/time/concept-ywm.md` — base concept node
- `/Users/fuyofulo/research/quran/notes/time/research-eschatological-architecture.md` — the Phase-2 catalog this builds on
