# Ayah Echoes — Refrains, Near-Duplicates, and Formulaic Repetition

A computational map of where the Quran repeats itself.

**Method.** All 6,236 ayahs are normalized (diacritics stripped; alif/ya/ta-marbuta variants unified; zero-width marks removed) and tokenized on whitespace. Ayahs whose normalized text matches exactly are grouped as **refrains**. For every other ayah pair we score Jaccard similarity on word 4-gram shingles (with shingles >200 occurrences capped to keep the candidate set tractable) and keep pairs at ≥ 0.5 with at least 5 tokens per ayah. Frequent leading/trailing word n-grams give us **opening and closing formulas**. Raw output: [`data/structural/ayah-echoes.json`](../../data/structural/ayah-echoes.json).

## 1. The 10 most-repeated phrases

| # | Count | Phrase | Where |
|---|------:|--------|-------|
| 1 | 31 | فَبِأَيِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ — *"which of your Lord's favors will you both deny?"* | Surah 55 (Ar-Rahmān), every other ayah from 13 to 77 |
| 2 | 11 | وَيۡلٌ يَوۡمَئِذٍ لِّلۡمُكَذِّبِينَ — *"woe that day to the deniers!"* | Surah 77 (Al-Mursalāt) |
| 3 | 8 | وَإِنَّ رَبَّكَ لَهُوَ ٱلۡعَزِيزُ ٱلرَّحِيمُ — *"your Lord — He is the Mighty, the Merciful"* | Surah 26, closing each prophet cycle |
| 4 | 8 | فَٱتَّقُواْ ٱللَّهَ وَأَطِيعُونِ — *"so fear Allah and obey me"* | Surah 26, every messenger to his people |
| 5 | 6 | وَيَقُولُونَ مَتَىٰ هَٰذَا ٱلۡوَعۡدُ إِن كُنتُمۡ صَٰدِقِينَ — disbelievers' standing taunt | scattered: 10:48, 21:38, 27:71, 34:29, 36:48, 67:25 |
| 6 | 6 | إِنَّ فِي ذَٰلِكَ لَأٓيَةً وَمَا كَانَ أَكۡثَرُهُم مُّؤۡمِنِينَ — *"a sign — yet most are not believers"* | Surah 26, marking each vignette |
| 7 | 5 | إِنِّي لَكُمۡ رَسُولٌ أَمِينٌ — *"I am to you a trustworthy messenger"* | Surah 26 |
| 8 | 5 | وَمَآ أَسۡـَٔلُكُمۡ عَلَيۡهِ مِنۡ أَجۡرٍ... | Surah 26, prophets refusing payment |
| 9 | 4 | وَلَقَدۡ يَسَّرۡنَا ٱلۡقُرۡءَانَ لِلذِّكۡرِ فَهَلۡ مِن مُّدَّكِرٍ | Surah 54 (Al-Qamar) |
| 10 | 4 | إِنَّا كَذَٰلِكَ نَجۡزِي ٱلۡمُحۡسِنِينَ | Surah 37, after each prophet's deliverance |

**92 distinct refrains, 259 occurrences** (~4.2% of the corpus is verbatim repetition). Three surahs dominate: Ar-Rahmān (55), Ash-Shu'arā' (26), and Al-Mursalāt (77).

## 2. Top near-duplicate pairs (non-identical)

Word-level differences carry the meaning — these are not careless reuse.

| Sim | A ↔ B | What changes |
|----:|-------|--------------|
| 0.83 | **39:72 ↔ 40:76** "ٱدۡخُلُوٓاْ أَبۡوَٰبَ جَهَنَّمَ..." | 39:72 prefixes **قِيلَ** (narrated); 40:76 is direct command |
| 0.83 | **26:24 ↔ 44:7** "رَبُّ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضِ..." | 26:24 frames as **Mūsā's speech** to Pharaoh; 44:7 as direct revelation |
| 0.83 | **23:82 ↔ 37:16** "أَءِذَا مِتۡنَا..." | Resurrection objection, once attributed (**قَالُوٓاْ**), once free-standing |
| 0.78 | **27:80 ↔ 30:52** "إِنَّكَ لَا تُسۡمِعُ ٱلۡمَوۡتَىٰ..." | Identical except for connective **fa-** |
| 0.75 | **7:78 / 7:91 ↔ 29:37** "فَأَخَذَتۡهُمُ ٱلرَّجۡفَةُ..." | **Same earthquake template** — used for Thamūd in 7:78, Madyan in 7:91 / 29:37 |
| 0.71 | **26:8 / 67 / 103 / 121 / 174 ↔ 26:158** | Surah 26's "إِنَّ فِي ذَٰلِكَ لَأٓيَةً..." refrain, with **فَأَخَذَهُمُ ٱلۡعَذَابُ** prepended only where the destruction is being narrated |
| 0.71 | **11:39 ↔ 39:40** "مَن يَأۡتِيهِ عَذَابࣱ يُخۡزِيهِ..." | Same warning spoken by **Nūḥ** in 11:39, by the **Prophet ﷺ** in 39:40 |
| 0.67 | **6:151 ↔ 17:31** | Prohibition of infanticide. **6:151:** *"We provide for you and them"* (parents first, *present* poverty). **17:31:** *"We provide for them and you"* (children first, *feared* poverty). Word order tracks the cause. |
| 0.67 | **2:120 ↔ 2:145** "وَلَئِنِ ٱتَّبَعۡتَ أَهۡوَآءَهُم..." | "Follow not their desires" warning, twice within Al-Baqarah, different referents |
| 0.67 | **3:103 ↔ 8:63** "وَأَلَّفَ بَيۡنَ قُلُوبِكُمۡ..." | "He united your hearts" — community vs. emigrant–helper alliance |
| 0.65 | **6:151 ↔ 17:34 / 6:152** | "Do not approach the orphan's wealth..." — identical legal formula in two surahs |
| 0.62 | **4:163 ↔ 33:7** | The covenant of the prophets, listed twice with overlapping but reordered rosters |
| 0.62 | **3:84 ↔ 2:136** | The "we believe in Allah and what was revealed..." creed, once spoken *by* believers, once spoken *to* People of the Book |
| 0.60 | **7:12 ↔ 38:75** | Allah's question to Iblīs — slight wording differences across the two narratives |
| 0.60 | **2:65 ↔ 7:166** | Sabbath-breakers turned to apes — shared punishment formula, different framing |
| 0.55 | **20:121 ↔ 7:22** | Adam's sin in two retellings — 7:22 emphasizes shame, 20:121 disobedience |

(Full list of 65 pairs in the JSON.)

## 3. Top closing formulas (last 3-4 words)

| # | Phrase | Gloss |
|--:|--------|-------|
| 32 | عَلَىٰ كُلِّ شَيۡءٍ قَدِيرٌ | "over all things, Powerful" |
| 28 | إِن كُنتُمۡ صَٰدِقِينَ | "if you are truthful" |
| 18 | مَا كَانُواْ يَعۡمَلُونَ | "what they used to do" |
| 16 | هُمۡ فِيهَا خَٰلِدُونَ | "they will abide therein" |
| 15 | إِن كُنتُمۡ مُّؤۡمِنِينَ | "if you are believers" |
| 15 | بِمَا كُنتُمۡ تَعۡمَلُونَ | "for what you used to do" |
| 14 | ٱللَّهَ غَفُورٌ رَّحِيمٌ | the canonical mercy seal |
| 13 | إِنَّ ٱللَّهَ غَفُورٌ رَّحِيمٌ | (with emphatic *inna*) |
| 12 | عَلَيۡهِمۡ وَلَا هُمۡ يَحۡزَنُونَ | "nor will they grieve" |
| 11 | أَكۡثَرُ ٱلنَّاسِ لَا يَعۡلَمُونَ | "most people do not know" |
| 10 | ٱلنَّارِ هُمۡ فِيهَا خَٰلِدُونَ | "the Fire — they will abide therein" |
| 10 | لَا يَهۡدِي ٱلۡقَوۡمَ ٱلظَّٰلِمِينَ | "He does not guide the wrongdoers" |
| 10 | مَا كَانُواْ بِهِۦ يَسۡتَهۡزِءُونَ | "what they used to mock" |
| 9 | وَلَٰكِنَّ أَكۡثَرَهُمۡ لَا يَعۡلَمُونَ | "but most of them do not know" |
| 8 | ٱللَّهَ مَا لَا تَعۡلَمُونَ | "from Allah what you do not know" |

The two-word divine-name pairs (غَفُورٌ رَّحِيمٌ, عَلِيمٌ حَكِيمٌ, سَمِيعٌ عَلِيمٌ, عَزِيزٌ حَكِيمٌ…) are the Quran's prosodic spine — collectively closing several hundred verses.

## 4. Top opening formulas (first 2-3 words)

| # | Phrase | Gloss |
|--:|--------|-------|
| 88 | يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ | "O you who believe" — launches most legal verses |
| 73 | إِنَّ ٱلَّذِينَ | "indeed those who…" |
| 31 | أَلَمۡ تَرَ | "have you not seen…" — rhetorical-question opener |
| 28 | إِنَّ ٱللَّهَ | "indeed Allah…" |
| 26 | قَالَ رَبِّ | "he said: my Lord…" — opens prophet-prayers |
| 26 | وَهُوَ ٱلَّذِي | "and He is the one who…" |
| 25 | هُوَ ٱلَّذِي | "He is the one who…" |
| 17 | إِنَّ ٱلَّذِينَ كَفَرُواْ | "indeed those who disbelieved…" |
| 16 | إِنَّ ٱلَّذِينَ ءَامَنُواْ | "indeed those who believed…" — structural counterpart |
| 13 | وَإِذَا قِيلَ لَهُمۡ | "and when it is said to them…" — opens disputations |
| 12 | إِنَّ فِي ذَٰلِكَ | "indeed in that…" — sign-formula opener |
| 12 | وَمَآ أَدۡرَىٰكَ مَا | "and what will make you know what [X] is?" |
| 11 | وَلَقَدۡ ءَاتَيۡنَا مُوسَىٰ | "and we surely gave Moses…" |
| 11 | وَيۡلٌ يَوۡمَئِذٍ | "woe that day…" (Surah 77 opener variant) |
| 10 | وَقَالَ ٱلَّذِينَ كَفَرُواْ | "and those who disbelieved said…" |

## 5. Surahs with the highest internal echo

| Surah | Internal pairs | Why |
|-------|---------------:|-----|
| **55 Ar-Rahmān** | 466 | The 31× "فبأي آلاء..." refrain alone produces C(31,2)=465 pairs — this surah is structured *as* a litany |
| **26 Ash-Shu'arā'** | 105 | Seven prophet vignettes (Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shu'ayb) each closed by the same four refrain-couplets |
| **77 Al-Mursalāt** | 45 | "ويل يومئذ للمكذبين" repeated 10× as eschatological hammer |
| **37 As-Sāffāt** | 16 | Prophet vignettes closed by rotating refrains |
| **54 Al-Qamar** | 9 | "ولقد يسرنا القرآن للذكر..." closes each punishment narrative |

The pattern: **the most internally echoing surahs are litanies or parallel-vignette compositions.** Linear narrative surahs (12 Yūsuf, 18 Al-Kahf) score zero on internal echo despite their length.

## 6. Cross-surah echo network

The most-shared-text surah pairs cluster in the prophet-narrative tradition:

| Pair | Shared pairs | Theme |
|------|-------------:|-------|
| **7 ↔ 11** | 2 | Both sweep the Nūḥ–Hūd–Ṣāliḥ–Lūṭ–Shu'ayb cycle |
| **7 ↔ 23** | 2 | "We sent Nūḥ to his people…" frame; resurrection-objection |
| **7 ↔ 29** | 2 | The earthquake-punishment closing for different peoples |
| **23 ↔ 37** | 2 | The "أَءِذَا مِتۡنَا" resurrection objection |
| **27 ↔ 30** | 2 | The "إِنَّكَ لَا تُسۡمِعُ ٱلۡمَوۡتَىٰ" prophetic-consolation pair |
| **39 ↔ 40** | 2 | "ٱدۡخُلُوٓاْ أَبۡوَٰبَ جَهَنَّمَ" hellfire formula |
| 26↔44, 11↔39, 30↔39, 33↔48, 6↔10, 16↔21, 16↔45, 3↔19, 3↔24 | 1 each | Mixed legal, theological, and narrative reuse |

**Surah 7 (Al-A'rāf) is the densest cross-surah hub** — a sourcebook of prophet-destruction templates redeployed in 11, 23, 26, and 29. **Surah 26 is its surah-internal counterpart**: it concentrates within itself what 7 distributes across the corpus.

## 7. One-word-difference flags — the precise edits

Where near-duplicates differ by exactly one token, the dominant pattern is a **causal connective** (وَ, فَ) or **speech attribution** (قَالَ / قَالُوٓاْ / قِيلَ) being added or dropped:

- **قِيلَ ٱدۡخُلُوٓاْ ↔ ٱدۡخُلُوٓاْ** (39:72 ↔ 40:76) — narrated vs. direct command.
- **قَالَ رَبُّ ٱلسَّمَٰوَٰتِ ↔ رَبُّ ٱلسَّمَٰوَٰتِ** (26:24 ↔ 44:7) — Mūsā's speech vs. revealed declaration.
- **قَالُوٓاْ أَءِذَا ↔ أَءِذَا** (23:82 ↔ 37:16) — disbelievers' objection attributed vs. quoted.
- **إِنَّكَ ↔ فَإِنَّكَ** (27:80 ↔ 30:52) — bare assertion vs. consequence-marked.
- **(فَكَذَّبُوهُ) فَأَخَذَتۡهُمُ ٱلرَّجۡفَةُ** (7:78/91 ↔ 29:37) — does the verse name the cause (belying) or jump to the effect (earthquake)?
- Within Surah 26: same closing refrain with or without **فَأَخَذَهُمُ ٱلۡعَذَابُ** prefix, depending on whether that vignette has already narrated the destruction.

A specific pair worth flagging: **6:151 vs. 17:31** on infanticide. 6:151: *"We provide for you and them"* — parents addressed first, *present* poverty. 17:31: *"We provide for them and you"* — children first, *feared* poverty. **The word order tracks the cause being addressed.** The Quran's near-duplicates are precise editorial moves, not loose paraphrase.

## Headline numbers

- **6,236** ayahs total · **92** distinct refrains · **259** verbatim-repeat ayah occurrences (~4.2% of corpus)
- **65** near-duplicate pairs at Jaccard ≥ 0.5
- **Surah 55** alone produces **466** internal echo pairs; surahs 26, 77, 37, 54 are the other litany-structured chapters
- **88** ayahs open with **يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُواْ** — the single most common opener
- **32** ayahs close with **عَلَىٰ كُلِّ شَيۡءٍ قَدِيرٌ** — the single most common closing (excluding Surah 55's refrain)
- The Quran repeats itself in three modes: **litany** (55, 77), **parallel-vignette refrain** (26, 37), and **cross-surah punishment template** (the 7-cluster).
