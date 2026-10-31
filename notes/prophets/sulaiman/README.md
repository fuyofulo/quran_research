# Sulaymān (Solomon)

The first investigation in the **Prophets series** (`notes/prophets/`). It asks who Solomon is in the
Quran, as the Quran tells it: what happens, what the text attaches to each episode, and what popular
retellings add. The evidence base is the Arabic text (Uthmani Hafs) and QAC morphology, searched by
script. Translations are a secondary layer, and hadith, tafsīr and Isrāʾīliyyāt are excluded, named only
as tradition.

## Headline

Solomon is named 17 times in 7 surahs; his story fills 50 verses, 30 of them in an-Naml. He holds the title of prophet only through the lists (4:163, 6:84-89). He is given wind, jinn,
copper and bird-speech, and every gift carries a God-ward line. His sentence *hādhā min faḍli
rabbī li-yabluwanī* (27:40, once in the Quran) names both the source of power and its purpose: a test of
thanks (7 of the Quran's 75 *shukr*). He checks, and is checked. He confesses his one lapse (38:32). The ring,
the demon, the wives and Bilqīs are not in the text.

## Files

| File | What it is |
|---|---|
| `BRIEF.md` | Shared brief for all agents: purpose, Phase-0 facts, traps, output rules. |
| `0-structural/sulaiman-structurals.md` | Census: passages, counts, hapaxes, shared formulas, divergence hotspots, prophethood status. |
| `1-narratives/narrative-the-ant-the-hoopoe-and-the-queen.md` | 27:15-44: speaking turns, gift and acknowledgement, the hoopoe, the letter and basmala, the queen. |
| `1-narratives/narrative-the-horses-the-trial-and-the-kingdom.md` | 38:30-40, 34:12-14, 21:81-82: the Ṣād frame beside David and Job, the horses, *jasad*, the prayer, the gifts, his death. |
| `1-narratives/narrative-judgment-inheritance-and-defence.md` | 21:78-80, 27:15-16, 2:101-103, David's frame, the lists: *fhm*, inheritance, the defence, prophethood. |
| `2-cross-cutting/research-what-kind-of-king.md` | Phase 2: gift and answer, the other men of power, power named as a test, lapse and return, limits. |
| `concept-sulaiman-deep.md` | Phase-4 synthesis (6 Arabic panels). |
| `story-guide.md` | Plain-language retelling for a first-time reader: 10 episodes, what the Quran does not say, what it teaches. |
| `data/structural/sulaiman-census.json` | Passage, root and phrase counts (from `scripts/build_sulaiman_census.py`). |
| `data/structural/sulaiman-versepack.json` | 92 verses with Arabic, Saheeh and Khattab; hotspots add Pickthall and Arberry (from `scripts/build_sulaiman_versepack.py`). |
| `data/structural/prophets-census.json` | Series census of the 25 named prophets (from `scripts/build_prophets_census.py`). |

## Key findings

1. **Location and status.** He is named in 16 ayahs; 7 of them also name David. No verse titles him on
   his own. He is one of 5 prophets (of 25) who hold the title only through 4:163 and 6:84-89.
2. **Every gift has a God-ward line.** In an-Naml Solomon speaks it; elsewhere God does. *Hādhā min
   faḍli rabbī* occurs only at 27:40.
3. **Source and purpose.** Pharaoh, Qārūn and the garden-owner answer with *lī*, *ʿindī* and *anā*.
   Dhū l-Qarnayn, Solomon's nearest double, names the source (18:98); the two alone have *qiṭr*, and
   both refuse payment. Only Solomon also names the purpose, the test (*li-yabluwanī*).
4. **Thanks is the densest theme.** His verses hold 7 of the Quran's 75 *shukr*, and 2 of its 3
   first-person *shukr* (27:19, 27:40). Thanks is also commanded as work (34:13).
5. **An-Naml is a story of checking.** *Nẓr* ×5 and *rjʿ* ×3 are shared out among the king, the council
   and the queen. The hoopoe's 60-word speech is the longest in the passage, and the queen has the last
   word. 27:30 is the only full basmala inside a surah's running text. She submits *maʿa Sulaymān*,
   with him, not to him.
6. **The horses (38:31-33).** The text leans to "good things" (not "horses"), "away from" the
   remembrance (as in all 11 other uses of *ʿan dhikr*), the horses (not the sun) as what is hidden,
   and stroking (not striking). There is no sun, no sword and no sin word.
7. **The trial (38:34-35).** *Jasad* is never a corpse in its 4 uses. *Fatannā* is a test. He asks
   forgiveness before power, and his is the only request in the Quran for a kingdom. His forgiveness is
   never narrated, but 38:40 closes with David's post-forgiveness formula, which is unique to the two of
   them.
8. **Father and son.** *Fa-fahhamnāhā* (21:79) is a once-only verb, followed at once by *wa-kullan
   ātaynā ḥukman wa-ʿilmā*. "Solomon inherited David" (27:16) sits beside knowledge and *faḍl*, not
   treasure. Ṣād gives David and Solomon one frame word for word; Solomon shares *niʿma l-ʿabd … awwāb*
   with Job.
9. **The defence (2:102).** *Wa-mā kafara Sulaymān* (the Quran's only *wa-mā kafara*) answers an
   implied charge that his power was sorcery. The *mā* of *wa-mā unzila* is relative in QAC, but it can
   also be read as negative.
10. **The limits of power (34:14).** A creature of the earth reveals his death; the jinn did not know
    the unseen; no duration is given. *Al-ʿadhāb al-muhīn* occurs elsewhere only for Israel under
    Pharaoh (44:30).

## Corrections log

**Marked CORRECTED in the investigation files**
1. **Structurals §3** (corrected by the judgment agent). *Awwāb* "5× in the Quran, 4 in Ṣād" counts the
   singular only. The lemma adds the plural *awwābīn* (17:25), and the verb *awwibī* is said to the
   mountains with David (34:10).
2. **Ant file, headline and §4** (corrected in Phase 2 §7). Of *nẓr* ×5 and *rjʿ* ×3, Solomon speaks
   *nẓr* at 27:27, 28, 41 and *rjʿ* at 27:28, 37. The council (27:33) and the queen (27:35) speak the
   rest. This strengthens the point that the king is not the only checker.
3. **Horses file §3** (corrected in Phase 2 §7). God's first-person *ftn* verbs number 9, not 7: 6:53,
   20:40, 20:85, 20:131, 29:3, 38:24, 38:34, 44:17, 72:17. Re-verified in Phase 4 against `words.jsonl`.
4. **Horses file §2** (corrected in Phase 2 §7). *Sūq* at 48:29 is a plant's stalks, not legs. The
   "legs" sense rests on *sāq* (27:44, 68:42, 75:29) and on *aʿnāq*. The stroking reading stands.

**Orchestrator notes**

5. Two of the three Sonnet narrative files (the queen; judgment and defence) had Arabic typed in a
   non-Uthmani spelling: 11 panels, none verbatim. The orchestrator replaced them by script with the exact
   source text from `data/arabic/quran.json`. The horses file was verbatim from the start.
6. *Awwāb* is 5× in the singular; the lemma adds the plural at 17:25 and the verb at 34:10. The BRIEF's
   "awwāb 5×" should be read as singular-only (see item 1).
7. Saheeh renders *al-ḥikma* in 2:251 as "prophethood"; the Arabic is "wisdom".
8. Khattab renders *shayāṭīn* in 21:82 as "jinn"; the Arabic is "devils" (34:12 says *min al-jinn*).
9. Saheeh and Arberry add "the sun" at 38:32, which the Arabic does not have.

**Phase-4 data notes** (none changes a conclusion)

10. The QAC lemmatises *bi-l-sūqi* at 38:33 under *sūq* (`s~uwq`), the lemma of *aswāq*, "markets"
    (25:7, 25:20), and of *sūqihi*, "its stalk" (48:29). It does not put it under *sāq*, "shin" (27:44,
    68:42, 75:29). A lemma search for "legs" will miss 38:33.
11. A plain string search for *qiṭr* also catches *qaṭirān*, "pitch" (14:50). *Qiṭr* itself occurs only
    at 18:96 and 34:12, as the files say.
12. **Re-verified by script in Phase 4:**
    - the full basmala occurs only at 1:1 and 27:30;
    - *ʿan dhikr* ×12; *bi-ghayri ḥisāb* ×7; *tajrī bi-amrihi* ×2; *lam tuḥiṭ bihi* ×2;
      *al-ʿadhāb al-muhīn* ×2; *ḥukman wa-ʿilmā* ×4; singular *khalīfa* ×2; *rabbi ghfir lī* ×3;
      *jasad* ×4; *kursī* ×2; *la-zulfā* ×2; *niʿma l-ʿabd* ×2; *innaka anta l-wahhāb* ×2;
    - *wa-mā kafara*, *faḍli rabbī*, *al-faḍlu l-mubīn*, *tabassama* and *al-khabʾ* ×1 each;
    - *ṣfn* and *jwd* each occur only at 38:31;
    - the hoopoe's speech is 60 words;
    - the ant file's 320 spoken words = the 307 in its table + 4 (*qīla*) + 9 (the letter);
    - *mulk* is asked for in an imperative only at 38:35. The people's request in 2:246 is for a king
      (*malik*), not a kingdom.

## Open questions

1. Whose voice is 27:42b, *wa-ūtīnā l-ʿilma min qablihā*: Solomon's side, or the queen's?
2. Is *wa-kadhālika yafʿalūn* (27:34) the queen's rule, or God's aside?
3. Can anything inside the Quran bound the *jasad* (38:34) beyond "an unexplained body, never a corpse"?
4. Solomon's forgiveness is implied by the formula, while David's is narrated (38:25). Does the
   difference carry meaning?
5. What did Solomon inherit (27:16): standing and knowledge, or kingship too?
6. Is the Sabaʾ of the lost gardens (34:15-19) the queen's people? The text shares the name and the
   *ẓulm* of the self, but never joins them.
7. Does *bi-ghayri ḥisāb* (38:39) qualify his giving, or the gift?
8. For the series: is there a pattern to which prophets are titled directly, and which only by list
   (David, Solomon, Job, Elisha, Zechariah)?
9. Is Ṣād's David–Solomon–Job sequence a teaching on kinds of return, or a grouping of three *awwāb*?
