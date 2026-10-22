# Gratitude (*shukr*): investigation index

## The answer in one sentence

The Quran teaches thanks as a response to God that is spoken in praise and glorification and done by using the gift well, never spoken alone; it meets seeking forgiveness not in the same sentence but through turning back (*tawba*, 46:15) and in God's names *Ghafūr Shakūr*.

## Where to start

- **To practise:** `practice-guide.md`. It covers the Quran's own words for each moment, what thanks asks you to do, and what the Quran does not ask.
- **For the full argument:** `concept-gratitude-deep.md`. It covers the vocabulary, the model, three verdicts, God the Thanker, how thanks sits with praise, glorification and forgiveness, the negative space and open questions.
- **For the evidence:** the two Phase-2 files, then the Phase-1 file a claim cites.

## File map

| Path | What it holds |
|---|---|
| `BRIEF.md` | Shared brief: scope, traps, Phase-0 findings, output rules |
| `0-structural/gratitude-structurals.md` | Phase-0 census: counts, purpose clauses, few/most, pairings (with CORRECTED notes) |
| `1-roots/concept-shkr-the-word-of-thanks.md` | `shkr`: forms, the first person, God the Thanker, `shkr` vs `kfr`, 14:7 |
| `1-roots/concept-hamd-praise.md` | `ḥmd`: the 23 *al-ḥamdu li-llāh* ayahs, *bi-ḥamdi*, *al-Ḥamīd*, *ḥamd* vs *shukr* |
| `1-roots/concept-nima-the-blessings.md` | *niʿma*, *ālāʾ*, *faḍl*, *mann*; remember / count / speak; 8:53 (ends with an orchestrator addendum) |
| `1-narratives/narrative-the-grateful.md` | Twelve portraits; 27:19 and 46:15 compared; thanking people |
| `1-narratives/narrative-the-ungrateful.md` | Saba', the town, Qārūn, the broken vows, self-crediting |
| `1-narratives/narrative-occasions-of-thanks.md` | The 14 purpose clauses; ease in the law; senses; daily things; rescue |
| `2-cross-cutting/research-how-the-quran-teaches-gratitude.md` | The spine: the model and three stress tests |
| `2-cross-cutting/research-thanks-praise-glorify-forgive.md` | The shared-ayah map, sequences, and the hereafter's last words |
| `concept-gratitude-deep.md` | Synthesis |
| `practice-guide.md` | Plain-language guide |

**Data and scripts:**
- `data/structural/gratitude-census.json` (built by `scripts/build_gratitude_census.py`);
- `data/structural/gratitude-versepack.json` (448 verses, built by `scripts/build_gratitude_versepack.py`);
- root profiles `data/concepts/$kr.json`, `data/concepts/Hmd-حمد.json` and `data/concepts/nEm.json`.

## Corrections log

Later files override earlier ones. "From → to" names the file corrected.

**Phase 0 and Phase 1**
1. `ḥmd` and `shkr` are **crossed, not paired** (31:12, 35:34). In each, a human act of one root meets God's name from the other. *(ḥamd file → structurals)*
2. Only **6:63 and 10:22** are danger vows at sea. 7:189 is a vow about a child. 31:32 leaves a remnant (*some are moderate*). *(ungrateful → structurals)*
3. *Niʿma* (blessing) is **50 tokens**. Another 18 are the praise verb *niʿma*, "how excellent", so it is not 68. *(blessings → structurals)*
4. **The prescribed words over a gift** are:
   - tasbīḥ (43:13-14);
   - ḥamd, then a request (23:28-29);
   - *mā shāʾa llāh* (18:39);
   - *awziʿnī* (27:19, 46:15);
   - takbīr *for having guided you* (2:185, 22:37).

   So it is not "43:13 only". *(orchestrator addendum and spine → blessings)*
5. **5:89 is "law made clear"**, not eased. 2:56 is a second life (*baʿathnā*), not a pardon. Forgiveness → thanks rests on **2:52 alone**. *(occasions → structurals)*
6. **God is never the subject of a `shkr` verb.** He appears only as *Shākir*/*Shakūr*, and through *mashkūr*. *(shkr file)*

**The spine's nine corrections** (`research-how-the-quran-teaches-gratitude.md`)

7. Thanks is paired with another purpose or command in **11 of 14** purpose clauses, not all. *(→ occasions)*
8. The ungrateful have **named feelings** (despair, exultation). What is never named is a *feeling of gratitude*. *(→ ungrateful)*
9. Ingratitude is **"an act or a sentence"**, not "mostly an act". *(→ ungrateful)*
10. **35:30 and 42:23 are not 14:7's positive half.** They reward deeds, and their *Shakūr* is God. *(→ shkr)*
11. **One reward for thanks is narrated** (54:34-35). Abraham is called grateful and then given good, with no causal link stated. *(→ shkr, ungrateful)*
12. ***Shukūr* at 25:62** is thanks a person wishes to give, not thanks "due from people". *(→ shkr)*
13. **3:144** names the grateful in defeat. *(→ ḥamd)*
14. **The takbīr extension**: *li-tukabbirū llāha ʿalā mā hadākum* joins the prescribed words. *(→ blessings)*
15. **`kbr` and `dhkr` share ayahs with `shkr`**, though `sbḥ` never does. *(→ structurals)*

**The thanks/praise/glorify/forgive file's four corrections**

16. **40:55's order is istighfār first**, then glorify with praise. So praise-before-istighfār holds in **3 of 4**. This corrects:
    - the ḥamd file ("order is fixed … in 40:55 and 110:3");
    - **the istighfār investigation's synthesis** (`notes/istighfar/concept-istighfar-deep.md`: "glorify with praise, then ask: 4×").
17. **52:26-28** is Paradise speech without *ḥamd*. *(→ ḥamd: "every recorded Paradise sentence is a ḥamd")*
18. **73:20's *lan tuḥṣūhu*** counts the night vigil, not the blessing.
19. **43:14's return is `qlb`**, not `twb`.

New data recorded in the same file:
- `shkr` × istighfār = 0, even within ±5 ayahs;
- `ḥmd` × `dhkr` = 0;
- *li-tukabbirū llāha ʿalā mā hadākum* occurs exactly 2×, both beside thanks.

**Made at synthesis**

20. **Narrowing.** The istighfār verb never comes within five ayahs of `shkr`. The *request* *ighfir* does, twice, in the same passage but not the same sentence:
    - 3:147, after 3:144-145;
    - 14:41, after 14:37 and 14:39.
21. **Reconciled counts.**
    - `dhkr` shares 3 `shkr` ayahs by its core lemmas (thanks/praise file) and 5 by the whole root (spine, which adds 14:5 and 25:62). Both are right.
    - *Al-ḥamdu li-llāh* is commanded with *say* 6×, counting Noah's 23:28. The structurals file lists Noah separately and gives 5.

## Rules this investigation kept

- The Arabic is ground truth, and translations are secondary.
- Hadith, tafsīr and fiqh are outside the evidence. The after-prayer ×33, the prostration of thanks, and "whoever does not thank people…" are named as traditional.
- Interpretations are marked **[interpretive]** and never promoted to findings.
