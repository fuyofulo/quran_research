# Narrative: 2:183–187 — the fasting passage as a designed unit

## Headline finding (100 words)

Five verses, 175 Arabic words, opening and closing on *taqwā* (root `wqy`, exactly 2 occurrences, at 183 and 187 — a ring). 2:186 is the 4th of 5 verses — *not* the verse-count centre — but it is the first verse to open after the passage crosses its own word-count midpoint, and it is the shortest verse in the block. Its "I respond" / "let them respond" pivot is a verified single root (`jwb`, confirmed in morphology data), not a translation artifact. But the text never states that fasting causes nearness — that inference is placement-driven, not textual. The `yusr`/`Eusr` clause rules out suffering-as-purpose. `xyT` (3x in Quran) times the fast to a perceptual event, not a clock.

---

## 1. The architecture of the five verses

Each verse makes one move. Compact panels below (Arabic + Saheeh; other translations cited only where they diverge meaningfully).

**2:183 — prescription, precedent, purpose.**
كُتِبَ عَلَيْكُمُ ٱلصِّيَامُ كَمَا كُتِبَ عَلَى ٱلَّذِينَ مِن قَبْلِكُمْ لَعَلَّكُمْ تَتَّقُونَ
"Decreed upon you is fasting as it was decreed upon those before you — that you may become righteous [*tattaqūn*]."
This verse carries the **highest translator-divergence score in the entire passage** (0.7581 — data-grounded, from `fasting-cooccurrence.json`), higher even than 186. The disagreement clusters on *kutiba* — "decreed," "prescribed," "written" — a legal-register verb (root `ktb`) that resists a single English equivalent for something that is simultaneously law and inheritance.

**2:184 — the numbers, the exits, the nudge.** Numbered days (`Edd`, 2x in the passage — 184, 185). Illness and travel exempt outright; those who find it unsustainable get a ransom (`fdy` — feed a poor person). Then, almost an aside: *wa-an taṣūmū khayrun lakum* — "and that you fast is better for you." The verse legislates a way out, then discourages taking it — not a contradiction, a structure protecting the vulnerable while holding the higher standard.

**2:185 — naming, reasoning, ease, completion, gratitude.** 45 words — the longest verse before 187. Ramadan is named for the first and only time in the passage; the reason given is revelatory, not calendrical — *the Qur'an was sent down in it*. The illness/travel exemption repeats verbatim from 184. Then the ease clause (§3). Then three purpose clauses stack in one verse: "complete the count," "magnify God," "perhaps you will be grateful" — more than anywhere else in the passage.

**2:186 — the interruption.** See §2.

**2:187 — permissions, pardon, the thread, the limits.** By far the longest verse (65 words, 37% of the passage). Night intimacy permitted; the mutual-garment metaphor; the confession-then-pardon sequence (§4); the white/black thread (§5); *iʿtikāf* named for the only time in the passage; and the closing *ḥudūd Allāh* / *lā taqrabūhā* — before the final *laʿallahum yattaqūn*, closing the ring opened in 183.

**The ring, confirmed by data.** `wqy` (taqwā) occurs exactly twice in the passage's full root inventory (`roots_in_passage_2_183_187`), and those two occurrences are the opening word of purpose in 183 and the closing word of purpose in 187. Nothing else in the passage frames both ends. This is not interpretive — it is a count.

## 2. 2:186 as centre: does it hold?

**Verse position — not the centre.** Five verses; 186 is the *fourth*. The verse-count centre is 2:185. The widely-repeated claim that 2:186 sits at the exact middle of the fasting passage is false, and should be dropped rather than defended.

**Word position — close, not exact.** Arabic word counts per verse: 183=14, 184=34, 185=45, 186=17, 187=65 (total 175). The literal midpoint is word 87.5, which falls *inside 185* (words 49–93), about 6–7 words before 186 begins. 186 is not the word-mass centre — 187's outsized length (65 words) pulls the mass rightward. The honest, smaller claim: **186 is the first verse that opens after the passage crosses its own halfway point** — the hinge, not the centre of gravity.

**The vocabulary, verified in the morphology data (not just gloss).** Word-level lookup of 2:186 in `words.jsonl` confirms:
- Word 7 *ujību* ("I respond") — root `jwb`.
- Word 12 *fal-yastajībū* ("so let them respond") — **also root `jwb`**.
God's response-verb and the command to humanity's response-verb are morphologically the same root, form IV against form X of the same stem. This is a real, checkable fact, not a translator's flourish (Arberry alone renders both with "respond" in English; Saheeh uses "respond" / "respond," Pickthall breaks the pair — "answer" / "hear My call" — losing it entirely, which is itself informative about what gets lost in translation).
- The root `dEw` (call/invocation) appears **three times inside this one verse alone**: *daʿwata* (the call, noun), *al-dāʿ* (the caller), *daʿānī* (he calls Me) — a root saturating a 17-word verse.
- The root `qrb` pivots hard across one verse-boundary: *qarīb* ("I am near," 186, word 6) versus *taqrabūhā* ("do not approach [these limits]," 187, word 58). Same root, opposite valence — invitation to nearness, then a fence against approach — one verse apart. This is confirmed by direct lookup, not inference.

**What the placement does, and what it doesn't.** The structural case is solid: the passage interrupts a run of dietary law with a verse about supplication and divine nearness, at (or immediately after) its own midpoint, using a root (`jwb`) that literally means answering-in-kind. That supports a reading: *the discipline creates an opening; the one verse in the block that is not legislation says what to do with it — call, and expect an answer.*

**Honest verdict.** Stop here, don't push further. **2:186 never mentions fasting.** No `Swm` root, no hunger, no reference to the days just described. The causal chain — "fasting brings you near, therefore the verse about nearness sits in the middle" — is an inference from *placement*, not a claim the text makes (checked against Phase 0's 14-occurrence `Swm` inventory: nothing links `Swm` to `qrb` or `jwb` directly). The placement is measurable; the causal story explaining it is the most interpretive move in this file — plausible, but a leap the Quran doesn't narrate. The centring is data; "this is why" is theology built on the data, not the data itself.

## 3. The ease clause

يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ — "God intends ease for you, and does not intend hardship for you" (2:185).

`ysr` occurs 44 times across the Quran (`data/concepts/ysr.json`); its co-occurrence table shows it paired with `Esr` (hardship) **6 times total, and 2:185 is the first pairing** (`first_together: [2, 185]` — data-grounded). The two roots are Quranic antonyms that recur as a set formula, first minted here.

Read plainly: this sentence sits inside a command that makes people hungry and thirsty for a month. The Quran doesn't resolve that tension by denying it — it legislates hardship (fasting is mandatory) and in the same clause disclaims hardship as the point. What this rules out: **hardship is not the purpose.** Difficulty isn't sold as virtue-through-suffering — which is why 184's exemptions and ransom option exist, stated *before* the ease clause is stated as principle: the exemptions are downstream of a design philosophy, not a grudging loophole. What it does NOT rule out: that difficulty is an unavoidable byproduct, or that struggling through it is meaningful — the text is silent there. It forecloses only one claim: that hardship itself is the goal.

## 4. What 2:187 permits, and the psychology of it

عَلِمَ ٱللَّهُ أَنَّكُمْ كُنتُمْ تَخْتَانُونَ أَنفُسَكُمْ فَتَابَ عَلَيْكُمْ وَعَفَا عَنكُمْ — "God knew you were betraying/deceiving yourselves — so He turned to you and pardoned you."

The sequence matters: **knowledge of failure → pardon → relaxation**, in that order. The rule (no relations during the fasting nights) was evidently being broken; the text doesn't soften this ("God knew," not "some among you struggled"). But the pardon lands as complete and prior — *tāba* (turned/accepted repentance) and *Eafā* (pardoned) both precede the new permission — so the relaxation reads as a gift following forgiveness, not a shamed concession to weakness. The garment metaphor just before it — *hunna libāsun lakum wa-antum libāsun lahunna*, "they are a garment for you and you a garment for them" — reframes the very thing being illicitly done as mutual covering, not appetite management.

**`taqrabūhā` vs `taʿtadūhā` — a real distinction, checked.** 2:187 closes: *tilka ḥudūdu Allāhi fa-lā taqrabūhā* — "these are God's limits, so do not **approach** them" (root `qrb` — same root as "I am near" in 186, now inverted). 2:229, on divorce boundaries, closes with the identical formula but a different verb: *fa-lā taʿtadūhā* — "do not **transgress** them" (root `Edw`), confirmed against `data/arabic/quran.json`. Not interchangeable: `Edw` treats the boundary as a line — stay on your side. `qrb` treats it as a perimeter with a buffer — don't get near it. Right after a verse about a rule quietly being broken, the harder verb reads as a direct response: people didn't cross the line outright, they eroded it by getting close. The fix is a wider margin, not a stricter line.

## 5. The white thread / black thread

حَتَّىٰ يَتَبَيَّنَ لَكُمُ ٱلْخَيْطُ ٱلْأَبْيَضُ مِنَ ٱلْخَيْطِ ٱلْأَسْوَدِ مِنَ ٱلْفَجْرِ — "until the white thread becomes distinct to you from the black thread of dawn."

`xyT` occurs 3 times in the entire Quran: twice here (2:187), once at 7:40 — the camel and the needle's eye (`data/concepts/xyT.json`, confirmed). The verb is `yatabayyanu`, root `byn` — "becomes distinct/clear" — and `byn` isn't a one-off: it also produces *bayyinātin* ("clear proofs") describing the Qur'an in 185, and closes 187 again as *yubayyinu* ("God makes clear His signs"). Three uses of one root bracket the passage's second half: clarity of revelation (185) → clarity of dawn (187, mid-verse) → clarity of law (187, closing).

What this implies: the fast doesn't begin at a fixed clock hour — it begins at the moment a distinction becomes *perceptible*, a threshold defined by discrimination, not measurement. The same passage that names the month by sighting (*"whoever witnesses the month," 185*) times the day by sighting too. The whole apparatus of when the fast is "on" is anchored twice to perception, not to an administrative or astronomical instant — a real, repeated pattern, not a reading-in from one metaphor.

## For the fast

- The passage's stated purpose is *taqwā*, stated twice, framing everything between. If a fast isn't oriented toward that, on the text's own terms it isn't doing what 183 says fasting is for.
- Suffering is not the mechanism. 185 rules that out explicitly. Chasing difficulty for its own sake is not what this passage asks for.
- The rule about approaching limits, not just avoiding them, argues for building margin, not just discipline at the boundary itself.
- The fast's beginning is a threshold of perceptible distinction, not a stopwatch — worth taking literally, not just astronomically.
- 186's placement is real, its wordplay is real, but the text does not say "fasting → nearness." If that's the felt goal, it's an inference the reader supplies — worth naming honestly rather than assuming the text promised it.
