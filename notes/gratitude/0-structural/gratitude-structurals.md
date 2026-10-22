# Gratitude — Phase-0 structurals (orchestrator)

> Census: `scripts/build_gratitude_census.py` → `data/structural/gratitude-census.json`.
> Verses: `scripts/build_gratitude_versepack.py` → `data/structural/gratitude-versepack.json` (448 verses, 10 groups).

## Headline

**The Quran almost never shows a human saying "thank you" to God with the word *shukr*.** Of 75 `shkr` tokens, only 3 are first person, and all 3 are asks or tests about thanking: *enable me to be grateful* (27:19, 46:15) and *to test me whether I will be grateful* (27:40). What people *say* is `al-ḥamdu li-llāh` (23×). Thanks is commanded (7 imperatives) and is the goal of 14 purpose clauses (*that you may be grateful*). Most of those follow **creation put at your service** (6) or **the law made easy** (3, including the end of the fasting verse, 2:185). The text says the grateful are **few** (5×) and that **most** do not thank (5×, plus Iblīs's boast, 7:17). **God Himself is called *Shakūr* / *Shākir*, the Thanker, 6×.**

---

## 1. Vocabulary (data-grounded)

| Root | Tokens / ayahs | Lemmas |
|---|---|---|
| `shkr` | 75 / 69 | `shakara` 46, `shākir` 14, `shakūr` 10, `mashkūr` 2, `shukūr` 2, `shukr` 1 |
| `ḥmd` | 63 / 61 | `ḥamd` 43, `ḥamīd` 17 |
| `nʿm` | 140 / 128 | `niʿma` (blessing) **50** + `niʿma` (*how excellent*, praise verb) 18 *(CORRECTED: were merged as 68)*, `anʿām` (cattle) 33, `anʿama` 17, `naʿīm` 17 |
| `ʾlw` (`ālāʾ`) | 37 / 37 | `ālāʾ` 34, **31 of them in Sūrat al-Raḥmān's refrain** |
| `fḍl` · `mnn` | 104 · 27 | bounty · favour conferred |
| `kfr` | 507 / 449 (after the expiation sense is removed) | `kafara`, `kufr`, `kafūr` 12, `kufūr` 3, `kufrān` |

**Polysemy traps.**
- **`kfr`** splits three ways: *disbelieve*, *be ungrateful* and *expiate*. **`kaffara` / `kaffāra` = expiate (18 tokens), now separated in the census.** Whether a given `kafara` means *deny* or *be ungrateful* is decided by context (`shukr` opposite, `niʿma` object), never by the root.
- **`nʿm`** includes `anʿām` (*cattle*, 33) and `naʿīm` (*bliss*, 17). Neither is "blessing" in the sense of a favour to be thanked for, though cattle are listed *as* a blessing in 16:5-8.
- **`ḥmd`** includes `Aḥmad` (61:6) and `maḥmūd` (17:79).

## 2. Who thanks, and how (data-grounded)

**By mood and person**:

| Form | Count |
|---|---|
| noun / participle | 29 |
| imperfect 2MP (*you thank*) | 20 |
| imperfect 3MP | 9 |
| imperative 2MP | 5 |
| imperative 2MS | 2 |
| imperfect 1S | 3 |
| imperfect 3MS | 3 |
| perfect | 4 |

- **Imperatives (7):** 2:152 (*remember Me, I will remember you; thank Me and do not be ungrateful*); 2:172 and 16:114 (*eat of the good things… and thank God, if it is Him you worship*); 29:17 (Abraham: *worship Him and thank Him*); 31:12 (to Luqmān); 31:14 (*thank Me and your parents*); 34:15 (to Saba').
- **Be among the grateful** (5): commanded to Moses (7:144) and the Prophet (39:66). The other three are **vowed in danger** (6:63, 10:22, 7:189), and each vow is followed by its breaking (6:64, 10:23, 7:190). *(CORRECTED by the ungrateful agent: only 6:63 and 10:22 are dangers at sea; 7:189 is a couple vowing thanks for a sound child. 31:32 leaves a remnant — `fa-minhum muqtaṣid` — so not every rescued person relapses.)*
- **First person, all three:** Solomon's *awziʿnī an ashkura* (27:19), the man at forty (46:15), and Solomon's *li-yabluwanī a-ashkuru am akfur* (27:40). **[interpretive]** The human "I" never says *I thank You*. It asks to be *enabled* to thank.
- **Called grateful:** Noah (*ʿabdan shakūrā*, 17:3) and Abraham (*shākiran li-anʿumih*, 16:121). The family of David is told *work in thanks* (*iʿmalū… shukrā*, 34:13), then: *few of My servants are grateful*.
- **Thanks to people:** once commanded, to parents beside God (31:14). It is once **refused**: the righteous feed others wanting *no reward and no thanks* (*shukūrā*, 76:9).
- **God the Thanker:**
  - *Shakūr*: 35:30, 35:34, 42:23, 64:17;
  - *Shākir*: 2:158, 4:147;
  - the believer's effort is *mashkūr*, "thanked": 17:19, 76:22.
- **The benefit is the thanker's**: *whoever thanks, thanks for himself* (27:40, 31:12). God is *ghanī ḥamīd*, free of need and praiseworthy (10×), often right after the ungrateful (14:8, 31:12, 39:7, 64:6).

## 3. "That you may be grateful": what precedes it (data-grounded, hand-annotated)

| Category | Refs |
|---|---|
| **Creation put at your service**: sea, ships, cattle, night and day, winds | 16:14, 22:36, 28:73, 30:46, 35:12, 45:12 |
| **The law made easy** | **2:185** (the fast: *God wants ease for you*), 5:6 (ablution, dry ablution: *God does not want hardship for you*), 5:89 (expiation for oaths) |
| **Forgiveness or a second chance** | 2:52 (pardon after the calf), 2:56 (revived after death) |
| **Rescue or victory when few** | 3:123 (Badr), 8:26 (sheltered when weak and afraid) |
| **The senses** | 16:78 (born knowing nothing, then given hearing, sight, hearts) |

*(CORRECTED by the occasions agent: 5:89 has no ease wording — it is "law made clear"; 2:56 is a second life, `baʿathnā`, not a pardon. Tally: creation 6, law eased 2 + made clear 1, forgiveness 1 + second life 1, rescue 2, senses 1. Forgiveness-to-thanks rests on 2:52 alone.)* **[interpretive]** The occasions for thanks include **being forgiven** (2:52), and the **easing of worship** (2:185, 5:6), not just its gifts. The fast's verse ends on *that you may be grateful*.

## 4. The few and the most (data-grounded)

- *qalīlan mā tashkurūn* ("little do you thank"): 7:10, 23:78, 32:9, 67:23. Three of these four follow **hearing, sight and hearts**.
- *qalīlun min ʿibādiya sh-shakūr*: 34:13.
- *aktharahum lā yashkurūn* ("most do not thank"): 2:243, 10:60, 12:38, 27:73, 40:61.
- Iblīs: *you will not find most of them grateful* (7:17).

## 5. Thanks against ingratitude, and its companions (data-grounded)

- **`shkr` × `kfr` in one ayah: 6.** They are 2:152, 14:7 (*if you thank, I will increase you; if you are ungrateful, My punishment is severe*), 27:40, 31:12, 39:7 and 76:3 (*whether grateful or ungrateful*).
- **Ingratitude's self-portrait**: *I was only given it because of knowledge I have* (Qārūn 28:78; and 39:49, where it comes **right after** a rescue). Also *inna l-insāna li-rabbihi la-kanūd* (100:6) and *la-kafūr* (22:66, 42:48, 43:15).
- **Thanks with patience: *ṣabbār shakūr* 4×** (14:5, 31:31, 34:19, 42:33): *in that are signs for everyone very patient, very grateful.*
- **Thanks with remembrance** (2:152), **worship** (2:172, 16:114, 29:17, 39:66) and **faith** (4:147: *what would God do with your punishment if you thank and believe?*). **Increase** comes at 14:7.
- **Thanks never shares an ayah with `sbḥ`** (tasbīḥ, glorification). It shares one with `ḥmd` only twice (31:12, 35:34) — *and in both the roots are crossed, not paired: the human uses one, God's name carries the other (CORRECTED by the ḥamd agent).*

## 6. Praise (data-grounded)

- ***al-ḥamdu li-llāh*: 23 ayahs.** By who says it:
  - **5 open a surah** (1, 6, 18, 34, 35).
  - **5 are commanded *say*** (17:111, 27:59, 27:93, 29:63, 31:25).
  - **4 are the people of Paradise** (7:43, 10:10 *their last call*, 35:34 *who removed grief from us*, 39:74).
  - Prophets: Noah on boarding the ark (23:28, commanded), Abraham for sons in old age (14:39), David and Solomon for knowledge (27:15).
  - Also after the wrongdoers' end (6:45, 37:182, 39:75).
- ***bi-ḥamdi* (glorify *with the praise of*): 15 ayahs.** **4 of them also contain `istighfār`**: 40:7, 40:55, 42:5, 110:3.
- **al-Ḥamīd pairs**: *ghanī ḥamīd* 10×, *ʿazīz ḥamīd* 3×, plus *walī*, *ḥakīm* and *majīd* once each.

## 7. Blessing (data-grounded)

- ***Remember the blessing of God (upon you)*: 12 commands.** These are 2:40, 2:47, 2:122, 2:231, 3:103, 5:7, 5:11, 5:20, 5:110, 14:6, 33:9 and 35:3. They go mostly to the Children of Israel and the believers, recalling a rescue or a union (3:103, *He joined your hearts*).
- ***If you counted God's blessing, you could not number it*: twice, with different endings.** 14:34 ends *man is very unjust, very ungrateful*. **16:18 ends *God is Forgiving, Merciful*.**
- **Proclaim it**: *as for the blessing of your Lord, speak of it* (93:11, divergence 0.784, the top of the core set).
- **Hidden and visible**: *He lavished His blessings on you, outward and inward* (31:20).
- ***fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān***: 31× in Sūrat al-Raḥmān. Its verb is *deny / call a lie*, not *be ungrateful*.

## 8. What Phase 1 should test

1. **Is *shukr* speech, deed, or state?** Speech would be *al-ḥamdu li-llāh*. Deed would be *work in thanks* (34:13) and *worship* (2:172). Test whether thanks is ever *only* words.
2. **Patience for hardship, thanks for ease?** *ṣabbār shakūr* suggests the split. Is thanks ever asked for *in* hardship, or patience *in* ease?
3. **14:7 "I will increase you"**: what kind of promise, and where is it shown?
4. **The opposite of thanks.** Is it denial, self-attribution (*because of my knowledge*), forgetting after rescue, or using the gift for disobedience? Count each.
5. **God the Thanker**: what does it mean that the Quran calls God *Shakūr*, and what does He "thank"?
6. **How thanks travels with praise, glorification, remembrance and seeking forgiveness** (the commissioner's own framing). Thanks never shares an ayah with tasbīḥ, yet *bi-ḥamd* + istighfār occur 4×. Map the actual sequences.

**Divergence (core set, top)**: 93:11 (0.784, *fa-ḥaddith*), 31:12, 14:34, 17:19, 2:158 (*shākir ʿalīm*), 3:123, 4:147, 67:23.
