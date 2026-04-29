# Research: The Disjoint Clocks of the Quran — Months, Generations, and the Missing Year

> Phase-2 cross-cutting investigation. Verifies and extends the Phase-1 finding that the Quran maintains two grammatically separated time-clocks (ritual-legal months and historical-judgment generations) and **systematically refuses to bridge them via years**, even though year-words exist and are used.

---

## 1. Headline — Two Clocks, No Bridge

The Quran organizes time around two non-overlapping vocabularies:

- **The $hr clock** — *shahr* "month," 21 occurrences in 17 ayahs across 9 surahs. Governs fasting, pilgrimage, sacred-month inviolability, ʿidda waiting periods, kaffāra atonement, and the canonical 12-month year. The *present-obligation* clock.
- **The qrn clock** — *qarn / qurūn* "generation," 23 occurrences in 22 ayahs across ~18 surahs (out of 36 total occurrences for the root, the rest being horn/companion/chained senses). Governs the *kam ahlaknā min qarnin* destruction-formula and the historical pacing of revelation. The *past-warning / future-accountability* clock.

**The two roots never share an ayah.** Verified directly against `data/morphology/words.jsonl`:

```
$hr ayahs (17): {2:185, 2:194, 2:197, 2:217, 2:226, 2:234, 4:92, 5:2, 5:97,
                 9:2, 9:5, 9:36, 34:12, 46:15, 58:4, 65:4, 97:3}
qrn ayahs (34): {4:38, 6:6, 10:13, 11:116, 14:49, 17:17, 18:83, 18:86, 18:94,
                 19:74, 19:98, 20:51, 20:128, 23:31, 23:42, 25:13, 25:38,
                 28:43, 28:45, 28:78, 32:26, 36:31, 37:51, 38:3, 38:38,
                 41:25, 43:13, 43:36, 43:38, 43:53, 46:17, 50:23, 50:27, 50:36}
INTERSECTION: ∅
```

The non-co-occurrence is structural, not statistical accident. With 17 and 34 ayahs scattered across the corpus, a uniform-random distribution would predict roughly 0.3 overlapping ayahs by chance, but the deeper signal is that the surahs that host both roots show a *consistent rhetorical separation*: when both clocks appear in one surah, they appear in *separate, non-adjacent rhetorical units* — except for one electrifying case (Sūrat al-Aḥqāf, [46:15] vs [46:17]) where they sit two ayahs apart and are placed in the mouths of *opposite moral types*. We return to this below.

The deeper structural finding is that **the missing bridge unit — the year — exists in the Quran's vocabulary but does not perform the bridge function**. Year-words appear (sana, ʿām), but they (a) never co-occur with qrn, (b) never co-occur with Ajl, (c) never co-occur with swE (the Hour), and (d) co-occur with $hr exactly once (at 46:15, gestation, where the year is biographical not calendrical). The Quran has years and chooses not to chronologize with them. **It is yearly-anonymous by design.**

---

## 2. Verification of the $hr / qrn Non-Co-Occurrence

### 2.1 The data

Programmatic check via `data/morphology/words.jsonl` (filtered by `root`): zero ayahs contain both roots. The 7 *surahs* that host both — 10, 17, 18, 20, 23, 32, 46 — keep them in different pericopes:

| Surah | qrn at | year-word at | $hr at |
|---|---|---|---|
| 10 (Yūnus)   | 13              | 5            | — |
| 17 (Isrāʾ)   | 17              | 12           | — |
| 18 (Kahf)    | 83, 86, 94      | 11, 25       | — |
| 20 (Ṭā-Hā)   | 51, 128         | 40           | — |
| 23 (Muʾminūn)| 31, 42          | 112          | — |
| 32 (Sajda)   | 26              | 5            | — |
| 46 (Aḥqāf)   | 17              | 15           | 15 |

The closest the two clocks come is **two ayahs**, at 46:15 ↔ 46:17. Read in sequence, the pericope is one of the most condensed ethical contrasts in the Quran:

- **[46:15]** — the *grateful son* speech. *His mother carried him with hardship and gave birth to him with hardship; and his bearing and weaning is **thirty months** (thalāthūna shahran) … until when he reaches his maturity and reaches **forty years** (arbaʿīna sanatan), he says: My Lord, enable me to be grateful…* The *grateful* son measures his life in months and years — the calendar of obligation.
- **[46:17]** — the *disrespectful son* speech. *And the one who says to his parents, 'Uff to you both! Do you promise me that I shall be brought forth, when **generations** (al-qurūn) have already passed away before me?'* The *ingrate* invokes *qurūn* (generations) as evidence *against* resurrection — the Quran's standard destruction-formula vocabulary, here weaponized into a denialist argument.

The pericope is a deliberate juxtaposition: **the calendar-clock belongs to the obedient subject; the generation-clock belongs to the denying subject.** The two clocks meet only by sitting next to each other in the textual rhetoric, never inside the same ayah, and they enter the verse precisely because they map two opposite moral postures toward time itself.

### 2.2 The semantic neighborhoods

The co-occurring root profiles confirmed in the previous concept analyses are mutually disjoint. To re-state for the bridging argument:

- *$hr* travels with: **Allah, knowledge, sacred (Hrm), fighting, the number four, fasting, mindfulness, people**. Lexicon of Medinan ritual law.
- *qrn* travels with: **before (qbl), destroy (hlk), say (qwl), be (kwn), after (bEd), see (rAy), first (Awl), originate (n$A), sin (jrm), remember (*kr)**. Lexicon of Meccan warning rhetoric.

There is no shared vocabulary partner in the top tiers. Cluster assignment confirms it: *$hr* sits alone in Cluster 19 (*Household Law & Lineage*), *qrn* sits in Cluster 4 (*Revelation, Speech & Disbelief*) alongside qbl/bEd/Awl/swE.

### 2.3 The Ajl extension

Even more striking: *Ajl* (appointed term) — the most semantically *flexible* time-root in the Quran (48 ayahs, lift-9.66 with Axr) — also **never co-occurs with qrn**, never co-occurs with year-words, and only co-occurs with $hr in two ayahs ([2:234, 65:4]) — both ʿidda verses where the appointed term *is* the months-count.

So the disjoint-clocks pattern is not a $hr/qrn quirk; it is a **systemic structural separation**. Ritual-legal time, historical-judgment time, and decreed-eschatological time form three boxes that the Quran's grammar declines to connect.

---

## 3. The Year-Word Inventory

### 3.1 Two roots, two senses

The Quran has *two distinct root-words* that translate to "year":

| Root | Lemmas | Total occ. | Ayahs | Notes |
|---|---|---|---|---|
| **snw** (س-ن-و) | *sanap* (sg.), *siniyn* (pl.), *sanaA* (lightning-flash, separate sense) | 20 | 19 | The default year-word; plural *sinīn* dominates |
| **Ewm** (ع-و-م) | *ʿām* (sg.), *ʿāmayn* (dual) | 9 | 7 | Reserved for *specifically calendrical* and biographical contexts |
| (snh) | *yatasannah* (verb, "to be aged/changed by years") | 1 | 1 | Hapax at [2:259], paronomastic with sana |

The 24:43 *sanā* at "*sanā barqih*" ("the flash of lightning") is a different sense of the snw root (radiance, not year) and is excluded from the year-count below; the year-bearing snw lemmas are 19 occurrences in 18 ayahs.

**Combined year-vocabulary: 19 (snw) + 9 (Ewm) − 1 (overlap at 29:14) = 27 word-tokens in 25 ayahs.**

That is *more* total occurrences than $hr (21) and almost as many as qrn (36). The year is not lexically scarce. It is *contextually contained*.

### 3.2 The contexts of *sana* and *sinīn* (snw)

Read together, the 19 year-bearing snw occurrences cluster into a small set of context types:

| Context type | Ayahs | Function |
|---|---|---|
| **Cosmic / hyperbolic durations** | [2:96] (1000-yr life-wish), [22:47] (a Day = 1000 years), [32:5] (a Day = 1000 years), [70:4] (a Day = 50,000 years), [29:14] (Noah 950 years) | The "year" as the *unit you count when you cannot fathom the scale*. Always paired with *mimmā taʿuddūn* — "of those which **you** count." |
| **Astronomical reckoning** | [10:5] (sun and moon — *li-taʿlamū ʿadada l-sinīn*), [17:12] (day and night — same formula) | The cosmological signs are *for you to count years and reckon* — but the Quran itself never does so. |
| **Famine / exile / trial** | [5:26] (40 years wandering), [7:130] (Pharaoh's people seized *bi-l-sinīn*, "with years of famine"), [12:42] (Joseph in prison "several years"), [12:47] (seven years of plenty), [26:205] (enjoyment for years) | Years as **suffering-duration** — the year is the unit of trial. |
| **Sleep / suspension** | [18:11] (cave-sleep "a number of years"), [18:25] (309 years in the cave) | Years as a unit of *unconsciousness* — the believer literally sleeps through the year-count. |
| **Biographical** | [20:40] (Moses years among Madyan), [26:18] (Pharaoh: "you remained years of your life among us"), [46:15] (40 years of maturity) | Years as *personal* lifespan, never as historical date. |
| **Politico-historical (one case)** | [30:4] (*fī biḍʿi sinīn* — "within three to nine years" Rome will conquer Persia) | The unique near-future political prediction. Indefinite paucal (*biḍʿ* = 3–9). Even here, no year is *named*. |

The pattern is unmistakable: **year-words appear in the Quran wherever a number is required (length of suffering, length of sleep, length of life, hyperbolic divine-time scaling), but never to date an event.** No surah is dated to a year. No prophet's mission is dated to a year. No revelation is dated to a year. The year is purely a *length-unit*, never a *position-marker*.

The most diagnostic phrase is *mimmā taʿuddūn* ("of those [years] which **you** count") at [22:47] and [32:5]. The Quran *attributes year-counting to "you," the audience*, while reserving *what* is being counted to a divine-Day measure. The year is the audience's instrument; the Day is God's. This is a deliberate epistemic split — the year-count is *yours*, and you are explicitly marked as its owner.

### 3.3 The contexts of *ʿām* (Ewm) — even more revealing

The 7 ayahs containing *ʿām* are remarkably specialized:

| Ayah | Context | Function of ʿām |
|---|---|---|
| **[2:259]** | The man who slept 100 years next to a ruined town | Hyperbolic resurrection-proof — God's death-and-revival of a single individual on a 100-year scale |
| **[9:28]** | "Let polytheists not approach the Sacred Mosque after **this their year** (*ʿāmihim hādhā*)" | The single proximate calendar reference in the Quran — but the year itself is *unnamed*; only its deictic *this-year* is given |
| **[9:37] ×2** | The nasīʾ abolition: "they make it lawful **one year** and unlawful **another year**" | Polemic against intercalation — the year as the *abused* unit being corrected |
| **[9:126]** | "Do they not see that they are tried every **year** (*kulli ʿāmin*) once or twice?" | Recurrence-pattern; the year as the unit of repeated trial |
| **[12:49]** | Joseph's interpretation: "after that will come a **year** (*ʿām*) in which people will be relieved" | Famine cycle resolution — the year as the unit of meteorological reversal |
| **[29:14]** | Noah: "a thousand *sanatin* less fifty *ʿāman*" | The *only* place sana and ʿām share a verse — and they are paired *contrastively* (one quantifies, the other corrects/specifies) |
| **[31:14]** | "His weaning is in **two years** (*ʿāmayn*)" | Biographical / parental — paralleling 46:15's months-then-years |

The split between sana and ʿām appears morphologically motivated — sana favors plural *sinīn* for *durations of trial, sleep, exile*, while ʿām favors singular *ʿām* for *cyclical / annual / hijri-deictic* references. But neither word ever *names a year*. **There is no occurrence of "in the year of X," "the year when Y happened," "the year [number]," anywhere in the Quran.** Even when *al-Fīl* (the Elephant) — the canonical pre-Islamic year-marker — is the subject of an entire surah ([105:1] *a-lam tara kayfa faʿala rabbuka bi-aṣḥābi l-fīl*), the Quran refuses to call it "the Year of the Elephant." It says *the people of the elephant*. The event is named; the year is not.

This is the negative-space finding the Phase-1 analysis predicted. The year-word slot is *occupied*, but its dating-function is *unoccupied*.

### 3.4 The 29:14 paradox — Noah's age

The single most telling ayah in the entire investigation: **[29:14]** *wa-laqad arsalnā Nūḥan ilā qawmihi fa-labitha fīhim alfa **sanatin** illā khamsīna **ʿāman*** — "We sent Noah to his people, and he remained among them a thousand *sanatin* minus fifty *ʿāman*."

Why two different year-words in a single arithmetical expression? The grammatical answer is that Arabic favors *ʿām* in a *fewer-by-N* (istithnāʾ) construction after sana — *alfa sanatin illā khamsīna ʿāman* reads more euphonically than the same word twice. The *structural* answer is that even at the maximal extreme of the year-scale (950 years!), the Quran goes out of its way to use **two distinct lexemes** rather than reify "the year" as a single named unit. The two year-words split the mathematical operation between them: one names the bulk (1000), the other names the subtraction (50). Even Noah's lifespan, the Quran's longest temporal duration, is told without ever letting "the year" become a singular reified noun.

This is the Quranic year in its purest form: **a number-unit that resists nominalization**. Hebrew has *shanah* and Greek *etos* used freely as singular nouns for "the year"; the Quran uses sana and ʿām almost always in *quantifying* (number + accusative) constructions, never as a free-standing referential noun (the Hijri-year sense).

---

## 4. The 9:37 *Nasīʾ* Abolition — Locking the Year to 12 Lunar Months

The single most important calendrical statement in the Quran is the pair **[9:36–37]**:

- **[9:36]** *inna ʿiddata l-shuhūri ʿinda Llāhi thnā ʿashara shahran fī kitābi Llāhi yawma khalaqa l-samāwāti wa-l-arḍa minhā arbaʿatun ḥurum* — "the count of months with God is twelve months in the book of God since the day He created the heavens and the earth; of them four are sacred."
- **[9:37]** *innamā l-nasīʾu ziyādatun fī l-kufri yuḍallu bihi lladhīna kafarū yuḥillūnahu **ʿāman** wa-yuḥarrimūnahu **ʿāman*** — "the *nasīʾ* (intercalary postponement) is an increase in disbelief … they make it lawful **one year** and unlawful **another year**."

These are the two ayahs in which $hr (the calendrical month) and the year-word *ʿām* occur in adjacent verses. The legal logic is fierce: pre-Islamic Arabs maintained a lunisolar calendar by inserting an extra "intercalary" month every two-or-three years, sliding the sacred months forward to keep them aligned with the seasons (so that the *ḥajj* would always fall in autumn, for example). The Quran abolishes the practice in two moves:

1. **9:36 — the synchronic claim.** There are **twelve** months in God's *kitāb* (registry) since creation. No more, no less. The count is fixed cosmologically.
2. **9:37 — the diachronic prohibition.** The intercalary "postponement" (*nasīʾ*) — an *adjustment of one year against another* — is *kufr*-augmenting. The two years are explicitly named as the units between which the *nasīʾ* operates: *they make it lawful **one year** and unlawful **another year***.

What this means structurally: **the Quran ratifies the year as exactly 12 lunar months and refuses any further year-engineering**. The year as a synchronization-device with the solar cycle is *theologically forbidden*. Once you fix the year at 12 lunar months, the Hijri year becomes *short* (354 days) — and over a 33-year cycle, every month rotates through every season. The Hajj will fall in summer, then spring, then winter, then autumn, in turn. **The Quran does not align ritual time with the solar / agricultural year.**

This decoupling is what makes the year *useless* as a historical or seasonal anchor. In a lunisolar system, "the year of X" is meaningful because the year is locked to the seasons (you remember "the harvest of year Y"). In the Quranic strictly-lunar system, the year drifts; it is a counter, not a context. **The Quran abolishes the only mechanism by which the year could function as a date-marker.**

This explains the negative space in Section 3: the Quran has year-words but no year-naming because *its own calendrical reform deprived the year of the structural property that makes naming useful*. A drifting lunar year is a pure number — the year of the elephant, in the Quranic frame, is just *a year* in which an elephant came; it has no place in a recurring solar-calendar pattern. The *event* is what anchors memory; the *year* is just an arithmetic counter.

---

## 5. The Historical-Time Vocabulary the Quran Uses Instead

If years do not anchor history in the Quran, what does?

### 5.1 Generations (qarn / qurūn) — the cohort-replacement clock

The dominant historical-time unit in the Quran is the *qarn* — a **cohort** of people-of-an-age. Crucially (per the qrn analysis), the Quran does not assign a duration to a qarn. Some classical lexicographers gloss it as "century," but no Quranic verse supports this. A qarn is *a people*, not *a length of time*. The destruction-formula *kam ahlaknā min qarnin* ("how many a generation We destroyed") never tells you *when* — only *that* and *how many*.

The 14 destruction-formula occurrences (per concept-qrn) show that the Quran's *primary mode of historical reference* is interrogative-evidentiary: *kam* ("how many?") + *ahlaknā* + *min qablihim*. The audience is invited to *count* generations without being given dates for any of them.

### 5.2 The ancients (al-awwalūn) — generational depth without numbers

The phrase *al-awwalūn* ("the ancients" / "the first ones") and its variants (*asāṭīr al-awwalīn* — "tales of the ancients," *ka-mā khalat al-awwalūn* — "as the ancients passed") functions as the Quran's *deep-past* marker. Per concept-Awl, *Awl* co-occurs heavily with *Axr* (last/other) and *qbl* (before) — building a relative ordering without absolute dating.

Note the rhetorical move at [46:17] (the disrespectful son): he uses *qurūn* in the same speech as *asāṭīr al-awwalīn* (in the surrounding pericope), conflating "generations passed" with "tales of the ancients." The Quran allows the conflation because both phrases do the same work — they index the past *categorically*, not chronologically.

### 5.3 Names of peoples — ethno-prophetic anchoring

The Quran's actual historical anchor is not a year but a **named people-with-prophet pair**: *qawm Nūḥ, ʿĀd, Thamūd, qawm Lūṭ, aṣḥāb Madyan, qawm Firʿawn, aṣḥāb al-Ukhdūd, aṣḥāb al-Fīl*, etc. These names appear hundreds of times and form the spine of the Quran's historical narrative. The name *replaces* the date.

This is structurally identical to how oral-tradition cultures everywhere anchor history — by *naming* the actor and the *event*, never by Cartesian-grid timestamping. The Quran's historiography is **narrative-ethnic**, not chronometric. It treats *who-it-happened-to* as more durable than *when-it-happened*.

### 5.4 Synthesis: a triple of historical-time markers

| Marker | What it says | What it omits |
|---|---|---|
| *qarn* (generation) | A cohort existed and was destroyed | When; how long the cohort was |
| *al-awwalūn* (the ancients) | The deep past is collectively present | Sequence, dates, named eras |
| *qawm X / aṣḥāb X* (named peoples) | A specific people were addressed by a specific prophet | Date of the encounter, calendar position |

**None of these three takes a year-input.** You cannot say *qarn 200 BCE* in Quranic Arabic; you cannot say *al-awwalūn of the third millennium*; you cannot say *qawm Nūḥ in year X*. The vocabulary is structurally year-resistant.

---

## 6. Why the Disjoint Clocks? — Theological Architecture

The hypothesis from the brief was that the Quran segregates ritual-legal time (months) from historical-judgment time (generations) because they do different theological work:

- **Months** govern PRESENT obligations (fasting, pilgrimage, sacred truce, ʿidda).
- **Generations** govern PAST warnings (destroyed peoples) and FUTURE accountability (every cohort tested).

A bridge unit (the year) would CHRONOLOGIZE both — letting you compute "X months until pilgrimage" against "Y years since Noah." The Quran refuses this computability.

The data support this hypothesis structurally:

1. **The grateful son (46:15) speaks in months and years**; the **disrespectful son (46:17) speaks in generations**. The two clocks map two moral postures. The Quran is not just separating registers; it is *associating* each register with a different mode of selfhood.

2. **The destruction-formula's calculated indeterminacy.** *Kam ahlaknā min qarnin* is rhetorically powerful precisely *because* it doesn't tell you when. The unbeliever cannot escape by saying "that was long ago; conditions are different now." The lack of a date keeps the warning *atemporally live*.

3. **The 9:37 abolition of *nasīʾ*.** The Quran could have ordered the lunar calendar to be aligned with the solar year (as Judaism does with intercalation, as Christianity does with Easter computation, as Hinduism does with adhik māsa). It explicitly forbids the alignment. **A year that drifts is a year that cannot anchor history.** The structural choice makes year-indexed historiography impossible *within* the Quranic framework.

4. **The audience-pronoun split at 22:47 / 32:5.** *Mimmā taʿuddūn* — "of those years **which you count**." God measures in Days (22:47, 32:5, 70:4); humans measure in years. The Quran *deflects* its own time-talk into a divine register, and assigns the year-count to the human audience. There is an explicit grammar of *whose clock this is*.

5. **The concept-Ajl extension.** Even *appointed terms* (Ajl), which one would expect to be the bridge-concept par excellence ("a term of N years"), never co-occur with year-words. Ajl is left as a *proper-name-of-a-duration* without a unit. When God appoints a term, he does not specify in years.

The composite picture: **the Quran refuses the computational regime that years-as-bridge would enable**. It is not careless about time; it is *deliberate* about which times are interconvertible. Months convert to days (Ramadan's 29-30 days, gestation's 30 months, kaffāra's 60 days); generations convert to peoples (qawm, ahl, ashāb); but the two sides are not bridged. The two clocks are functionally *separate measurement domains*.

This is not unique to time. Compare the rḥm pattern (mercy / wombs): two surface-meanings unified at root level, but kept in separate registers in actual deployment. Compare the qrn polysemy (generation / horn / companion / chained): one root, many surfaces, each surface in its own pericope. The Quran's deep grammar prefers **lexical compression with contextual segregation** — one root, many uses, but each use in its semantic compartment. The disjoint-clocks pattern is the time-system's instance of this general structural preference.

---

## 7. Year-Indexed vs Generation-Indexed Historiography — The Comparative Frame

Most major historiographic traditions are *year-indexed*:

- **Christian** — *Anno Domini* / *BC* — every event takes a year-coordinate. The Gospels themselves embed *in the fifteenth year of Tiberius Caesar* (Luke 3:1).
- **Hebrew Bible** — heavily year-indexed: *in the four-hundred-and-eightieth year after the children of Israel came out of Egypt, in the fourth year of Solomon's reign over Israel, in the month of Ziv, which is the second month, he began to build the house of the Lord* (1 Kings 6:1). Years, named months, regnal years — the full chronometric package.
- **Roman** — consular years, *ab urbe condita*.
- **Hindu / Buddhist** — yuga / kalpa cycles, regnal years; year-counting is ubiquitous.
- **Modern secular** — Julian/Gregorian calendar, ISO dates, CE/BCE.

**The Quran is the conspicuous outlier.** It introduces no era marker, no regnal date, no year-of-event. In the entire 6,236-ayah corpus, there is *one* deictic year-reference (*ʿāmihim hādhā*, "this their year," at 9:28), addressing the polytheists' final year of Mosque-access — and even that is unanchored to any year-number.

This is structurally distinctive. A religion whose scripture is *year-silent* organizes its historical consciousness around different anchors. In the Quranic frame:

- **You know when the past happened** by knowing *which people* it happened to (*qawm Nūḥ, ʿĀd, Thamūd*) and *how many* generations have passed since (*kam ahlaknā*).
- **You know when the future will happen** by knowing it is *near* (*qarīb*) and *unknown* (*lā yuʿallimuhā illā huwa*) — see swE.
- **You know when the present requires action** by knowing the *month* (Ramadan, sacred months, ʿidda) and the *day* (Friday, the Day of Judgment).

**Years are absent because they would do nothing the Quran wants done.** They would invite *computation* — "we are X years from creation, Y years from Noah, Z years until the Hour" — and computation is the move the Quran systematically blocks (see swE: the Hour's hour is hidden; see Ajl: the term is appointed but unspecified; see qrn: the generations are countable but undateable). **The Quran's time-grammar is not just yearly-anonymous; it is *anti-chronometric*.**

This connects to a broader theological move: the refusal to grant the human audience computational mastery of divine time. *Yasʾalūnaka ʿani l-sāʿati ayyāna mursāhā* — "they ask you about the Hour, when it is to be set" ([7:187]) — is met with *qul innamā ʿilmuhā ʿinda Llāh* — "say: its knowledge is only with God." The same pattern at [33:63], [41:47], [43:85], [79:42–44]. The Hour's date is withheld; the year-of-event is correspondingly absent. The same epistemic logic governs both the macro-eschatological time and the historical-narrative time: **God knows the years; you do not need to.**

---

## 8. Connection to Other "Calculated Indeterminacy" Patterns

The disjoint-clocks finding is one node in a larger network of Quranic calculated-indeterminacy patterns. To map them:

### 8.1 The Hour (*al-sāʿa*) — knowledge-withholding

Per concept-swE: the Hour is *qarīb* (near) but its *time* is not given. Twelve ayahs explicitly mark the Hour's timing as *known only to God*. This is the macro-eschatological instance.

### 8.2 The appointed term (*ajal*) — naming without quantifying

Per concept-Ajl: God *appoints* a term (*ajalan musamman*), but the Quran almost never quantifies the appointment in years. The term has a *name* (it is *appointed*), not a *number*. This is the meso-individual instance.

### 8.3 The generations (*qurūn*) — counting without dating

Per concept-qrn: *kam ahlaknā* — *how many* generations. The audience is asked to *count*, but never given a *when*. This is the macro-historical instance.

### 8.4 The night of power (*laylat al-qadr*) — naming without locating

[97:1–5]: the Night of Power exists, is "better than a thousand months" (the largest unit-multiple in the Quran), but its *exact date within Ramadan* is famously left unspecified. Tradition assigns it to one of the odd-numbered last-ten nights, but the Quran itself does not commit. Even within the only month it names (Ramadan), the Quran withholds the night's date.

### 8.5 The Hijri year — not in the Quran

The Hijri calendar — Year 1 = 622 CE = the Hijra — was instituted by the Caliph ʿUmar ibn al-Khaṭṭāb in 638 CE / Year 17 AH, *post-Quranic*. The Quran itself never numbers the years of the Prophet's mission. Even the Hijra event ([9:40] *idh akhrajahu lladhīna kafarū thāniya thnayn*) is not dated.

### 8.6 The al-Fīl reference — naming the event without the year

Pre-Islamic Arabs anchored memory by years-of-events: *ʿām al-fīl* (the Year of the Elephant), *ʿām al-ḥuzn* (the Year of Sorrow), etc. Surah 105 is entirely about the Elephant event — a paradigmatic *year-naming* event in Arabic memory. The Quran *names the event* (*aṣḥāb al-fīl*) but **drops the year-prefix**. *ʿĀm al-fīl* in Quranic Arabic becomes *aṣḥāb al-fīl*. The structural editing-out of the year is precise.

### 8.7 The *biḍʿ sinīn* of Rome — the unique near-future prediction

[30:2–4] *ghulibati l-Rūmu fī adnā l-arḍi wa-hum min baʿdi ghalabihim sa-yaghlibūn fī **biḍʿi sinīn*** — "Rome has been defeated in the nearest land, and after their defeat they will be victorious within **3-to-9 years**." This is the *only* Quranic time-prediction with a year-range. Note: the range is *paucal* (*biḍʿ* = the indefinite small number 3–9), not a definite count. Even when the Quran predicts in years, it predicts in a *number-with-irreducible-vagueness*. The exception confirms the rule.

### 8.8 Composite

| Domain | What is counted | What is withheld |
|---|---|---|
| Eschatology (swE) | The Hour exists, is near | When |
| Biography (Ajl) | A term is appointed | How many years |
| History (qrn) | How many generations were destroyed | When; how long ago |
| Calendar ($hr) | 12 months, 4 sacred | What year |
| Night of Power | One night out of Ramadan | Which night |
| Geopolitics (30:4) | The Roman victory will come | Within what *exact* year of 3–9 |

**The pattern is invariant.** Across six independent time-domains, the Quran provides a count without providing a coordinate. **Calculated indeterminacy is the Quran's general signature for time.** Years would violate this signature by providing coordinates everywhere; they are therefore systematically marginalized.

The disjoint-clocks finding is the *grammatical* expression of this theology. By keeping months and generations in separate ayahs, and by refusing to let year-words bridge them, the Quran enforces the calculated-indeterminacy signature at the level of root co-occurrence.

---

## 9. Rabbit Holes for Phase 3

### 9.1 Is the "you count" / "We count" split systematic?

The phrase *mimmā taʿuddūn* ("of those which you count") at 22:47 and 32:5 explicitly assigns year-counting to the second-person plural. Are there other time-units where the Quran flips agency? Map every occurrence of *ʿadda* (to count) and *ʿidda* (a count) and tabulate the agent — God or the audience. Hypothesis: God counts months and souls; humans count years and possessions.

### 9.2 The *kitāb* as the meta-clock

[9:36] says months are 12 *fī kitābi Llāh* ("in the book of God"). [33:6] says relatives have priority *fī kitābi Llāh*. [6:38] says *mā farraṭnā fī l-kitābi min shayʾ* — nothing is omitted from the Book. The Book is the Quran's master ledger. Does the *kitāb* metaphor *replace* the calendar function? Does writing-down replace dating? Worth a concept analysis of *ktb* in time-contexts.

### 9.3 The *dhr* outlier

The root *dhr* (دهر) appears only twice — [45:24] *wa-mā yuhlikunā illā l-dahr* (the disbelievers say "nothing destroys us but Time/Fate"), and [76:1] *hal atā ʿalā l-insāni ḥīnun mina l-dahri* ("has there come over man a span of time"). *Dahr* is the only Quranic word that comes close to *abstract time-as-such* (similar to Greek *chronos* or Sanskrit *kāla*). The disbelievers blame *dahr*; the Quran responds by quoting them disapprovingly. **This may be the Quran's explicit polemic against year-indexed time-as-fate.** Worth a deeper look — is *dahr* the disjoint-clocks finding's *negative space made explicit*?

### 9.4 The Hebrew/Aramaic comparison

Hebrew has *shanah* (year) and uses it constantly for dating. Aramaic has *shnāʾ* / *shenāʾ*. Both Semitic cousins use the cognate root S-N-(W) for year and *do* anchor events by year. The Quranic *sana* is etymologically the same word but functionally restricted. **Did the Quran inherit a fully-functional Semitic year-vocabulary and selectively de-functionalize it?** A comparative-Semitic study would test this directly.

### 9.5 Did pre-Islamic poetry use *ʿām* and *sana* for dating?

The Muʿallaqāt and pre-Islamic *qaṣīdas* are full of temporal references. If pre-Islamic poetry routinely says *ʿām* X or *sana* X to anchor events, then the Quran's avoidance is a *conscious revision* of inherited Arabic usage. If pre-Islamic poetry already avoided it, the Quran is following an existing oral-tradition convention. This is testable against the corpus of Jāhilī poetry.

### 9.6 The 309-year cave-sleep at 18:25

*Wa-labithū fī kahfihim thalātha miʾatin sinīn wa-zdādū tisʿan* — "they remained in their cave 300 years, and they exceeded by nine." Why specify 309? Classical commentary notes that 300 solar years ≈ 309 lunar years. **This may be the Quran's one explicit acknowledgment of solar-vs-lunar year arithmetic** — without ever naming it. Worth examining whether this is a *coded reference* to the very intercalation question that 9:37 abolishes.

### 9.7 The qarn / qarīn structural inversion (cross-link)

Per concept-qrn: *qarn* binds a person to a *temporal cohort*; *qarīn* binds a person to an *individual companion*. Both are *yokings*. If the Quran's time-grammar refuses to bridge group-time (qarn) and ritual-time ($hr) via the year, does its ethics-grammar similarly refuse to bridge group-loyalty (qarn-belonging) and individual-loyalty (qarīn-bond)? Test: are *qarn* and *qarīn* ever in the same ayah? (From the data: no — confirm and explore.)

### 9.8 The Day-as-thousand-years inversion

[22:47, 32:5] — a Day with God is 1000 years; [70:4] — a Day with God is 50,000 years. **The Day is the unit that absorbs all year-counts.** This reverses the human time-grammar (where many days make a year) into a divine time-grammar (where one Day exceeds many years). The year is, in the Quranic divine register, a *fraction of a Day*. This is the most radical move in the entire investigation: the year is not just unanchored historically — it is *cosmologically downgraded* below the day. Worth a dedicated analysis.

---

## 10. What's Data-Grounded vs Interpretive

**Data-grounded:**
- $hr ↔ qrn zero-overlap at the ayah level (verified directly)
- The 19-snw / 9-Ewm / 1-snh occurrence counts and the 25-ayah year-vocabulary footprint
- The Ajl ↔ qrn / Ajl ↔ year-words zero overlap
- The 7 surahs that host both $hr/qrn or year-words/qrn but never in shared ayahs
- The single 46:15 / 46:17 adjacency
- The *mimmā taʿuddūn* phrase at 22:47, 32:5
- The textual content of 9:36–37, 29:14, 18:25, 30:4, 105:1
- All time-root co-occurrence stats (from structural-time-cooccurrence.md)
- The lemma morphology of qaron vs qariyn vs muqarranīn etc. (from concept-qrn.md)

**Interpretive (LLM-supplied):**
- The "two clocks" theological framing (carried forward from Phase-1 concept-qrn analysis)
- The grateful-vs-disrespectful son reading of 46:15 ↔ 46:17 (visible in the text but my elevation as the *signature* moment)
- The "year is a counter, not a context" claim about the post-9:37 lunar calendar
- The "calculated indeterminacy" frame uniting swE, Ajl, qrn, Night of Power
- The "Day downgrades the year" reading of 22:47 + 32:5 + 70:4
- The cross-tradition comparison (Christian/Hebrew/Roman/Hindu year-indexing) — drawn from training, not the data
- The hypothesis that pre-Islamic poetry's year-usage would test whether the Quran is revising inherited convention
- The classification of *aṣḥāb al-fīl* vs *ʿām al-fīl* as a *deliberate editorial removal* of the year-prefix — defensible but not directly stated by the data
- The treatment of the *biḍʿ sinīn* at 30:4 as the "exception confirming the rule" — interpretive
- The *kitāb* as the meta-clock hypothesis — speculative

**The decisive move:** The instruction proposed verifying the disjoint-clocks finding by checking whether year-words might be the bridge. The data instead showed something stronger: **year-words exist, but they (a) systematically avoid the historical-judgment cluster (qrn, Ajl, swE) and (b) avoid the calendrical cluster ($hr) except in one biographical biological context (46:15)**. This is not an absence-of-bridge; it is an *active avoidance* of bridging. Once that was visible in the data, the 9:37 nasīʾ abolition snapped into place as the *constitutive* legal act that makes years incapable of bridging — by locking them to a drifting lunar count. The two findings together — the lexical avoidance and the legal abolition — gave the disjoint-clocks pattern a *grammar* and a *jurisprudence* simultaneously. The frame "calculated indeterminacy" was the unification that let the time-grammar be read as theology.

The methodological pattern reinforced from Entry 1 (rḥm): **the negative space — what a vocabulary refuses to do despite having the means — is where the Quranic structural grammar surfaces most decisively.** Years exist; they are not used to date. Months exist; they are not used to compute history. Generations exist; they are not assigned durations. The presence-of-vocabulary-with-absence-of-function is, again, the diagnostic pattern.
