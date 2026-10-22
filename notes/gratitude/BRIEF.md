# Gratitude (shukr) — shared brief

> Read `notes/agent-context.md` FIRST (conventions, Buckwalter, the tanwīn-alif normalization trap), then
> this, then `notes/gratitude/0-structural/gratitude-structurals.md`. Do NOT read `notes/methodology-log.md`.
> Do NOT read other investigations' files unless your prompt names one.

## Why this investigation exists

This investigation was asked for by the believer who commissioned the fasting, tahajjud, regret,
istighfār and hope investigations. In their words: *"I want you to start an in depth research on
gratefulness and thanking Allah, because asking for forgiveness and glorifying Him goes hand in hand."*

They want two things:
- **how the Quran teaches thanking God**, as a practice;
- **how thanks sits with seeking forgiveness, praise and glorification.**

**Privacy rule (hard).** This repository is public. Write nothing about the commissioner's personal
life. Refer to the reader as "the reader" or "someone".

**Tone.** Be direct, and honest about what the text says and where it is silent. Be warm, not
preachy. Mark every interpretation.

## Deliverables downstream of your file

1. A synthesis (`concept-gratitude-deep.md`).
2. **A plain-language practice guide** (`practice-guide.md`). It will use the Quran's own words of
   thanks and praise, organised by moment, and explain what thanks consists of.

Write with these in mind. Wherever your material gives a person something to *say* or *do*, name it.

## Phase-0 findings — established, build past them (details in the structurals file)

- **`shkr`: 75 tokens / 69 ayahs.**
  - Only **3 are first person**, and all are about *being enabled to* thank or *being tested whether*
    one will thank: 27:19, 46:15, 27:40. The text never shows a human saying "I thank You" with this
    root.
  - What people *say* is **`al-ḥamdu li-llāh`** (23 ayahs: 5 surah openings, 5 commanded "say", 4 by
    the people of Paradise, and prophets on a rescue or a gift).
- **7 imperatives to thank.** These are 2:152, 2:172, 16:114, 29:17, 31:12, 31:14 (*Me and your
  parents*) and 34:15. *Be among the grateful* is commanded at 7:144 and 39:66, and **vowed in danger
  then broken** at 6:63-64, 10:22-23 and 7:189-190.
- **14 *laʿallakum tashkurūn* ("that you may be grateful")**:
  - **creation put at your service** 6;
  - **the law made easy** 3 (2:185, the fast; 5:6, ablution; 5:89);
  - **forgiveness or a second chance** 2 (2:52, 2:56);
  - **rescue when few** 2 (3:123, 8:26);
  - **the senses** 1 (16:78).
- **The few and the most:**
  - *little do you thank* 4× (7:10, 23:78, 32:9, 67:23 — 3 of these after hearing, sight and hearts);
  - *few of My servants are grateful* (34:13);
  - *most do not thank* 5×;
  - Iblīs's boast (7:17).
- **God is *Shakūr* / *Shākir* 6×** (2:158, 4:147, 35:30, 35:34, 42:23, 64:17), and the believer's
  effort is *mashkūr* ("thanked") at 17:19 and 76:22. *Whoever thanks, thanks for himself* (27:40,
  31:12). God is *ghanī ḥamīd* 10×, often right after the ungrateful.
- **Thanks vs ingratitude in one ayah: 6** (2:152, 14:7, 27:40, 31:12, 39:7, 76:3). **14:7**: *if you
  thank, I will increase you.* Ingratitude's self-portrait is *I was given it only because of my
  knowledge* (28:78, 39:49), along with *kanūd* (100:6) and *kafūr*.
- **Companions of thanks:**
  - *ṣabbār shakūr* (very patient, very grateful) 4×: 14:5, 31:31, 34:19, 42:33;
  - remembrance (2:152), worship (2:172, 16:114, 29:17, 39:66) and faith (4:147).
  - **Thanks never shares an ayah with `sbḥ` (glorify), and shares one with `ḥmd` only 2× — crossed, not paired (31:12, 35:34).**
  - **But *bi-ḥamdi* + istighfār share an ayah 4×** (40:7, 40:55, 42:5, 110:3).
- **Blessing:**
  - *remember God's blessing* is commanded 12×;
  - *if you counted God's blessing you could not number it* appears twice with different endings:
    14:34 *man is unjust, ungrateful* / **16:18 *God is Forgiving, Merciful***;
  - *speak of your Lord's blessing* (93:11);
  - *outward and inward* (31:20);
  - *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* 31× (its verb is *deny*).

## Data — use these; do not open whole corpus files

| Path | What |
|---|---|
| `data/structural/gratitude-versepack.json` | **Start here.** 448 verses (Arabic, Saheeh, Khattab) in these groups: `shukr-all` (all 69), `purpose-contexts`, `the-grateful`, `the-ungrateful`, `praise`, `blessing`, `al-rahman` (55:1-78), `god-thanks`, `thanks-and-people`, `hand-in-hand`. |
| `data/structural/gratitude-census.json` | Lemma tables, `shukr` by mood/person, the purpose-clause annotation, the few/most, God the Thanker, pairings, praise, blessing, divergence. |
| `data/concepts/<root>.json` | Built: `$kr.json`, `Hmd-حمد.json` (**not** `HmD`/`hmd`), `nEm.json`, `kfr.json`, `fDl.json`, `mnn.json`. Build others with `python3 scripts/build_concept.py <root>`. |
| `data/arabic/quran.json` + `data/translations/{saheeh,khattab}.json` | Single-verse lookups only, by python one-liner. |

## Traps

- **`kfr` is three words**: *disbelieve*, *be ungrateful* and *expiate* (`kaffara`/`kaffāra`, 18 tokens).
  Decide *deny* vs *be ungrateful* by context. Do not count `kfr` as "ingratitude" by root.
- **`nʿm`** includes *cattle* (`anʿām`) and *bliss* (`naʿīm`). **`ḥmd`** includes *Aḥmad* and *maḥmūd*.
- **`ālāʾ`'s refrain verb is *tukadhdhibān*, "deny"**, not "be ungrateful". Translators vary.
- **The common claims that "*ḥamd* is broader than *shukr*" and that "*shukr* has three parts — heart,
  tongue, limbs" come from lexicography and tafsīr.** Name them as traditional and test them against
  the text. Never assume them.
- **Hadith is outside the evidence base**: "whoever does not thank people does not thank God", the
  prostration of thanks, and the after-prayer *subḥān Allāh / al-ḥamdu li-llāh / Allāhu akbar* ×33.
  Where a well-known practice is not in the Quran, saying so is a finding.
- **Normalization**: rejoin the detached tanwīn alif before any Arabic string search.

## Output rules

- **Hard cap 2,000 words per file.** Truncate rather than overshoot.
- Open with a **100-word headline block.**
- **Max 5 full Arabic + translation panels.** Cite everything else as `[s:a]`.
- Mark **data-grounded** vs **[interpretive]**.
- End with **"For practice"**: 3–6 plain lines on what this changes about how someone thanks God.
- Do not append to `notes/methodology-log.md`. Do not commit unless your prompt says so. Write with the
  Write tool, then `ls` to confirm.

## File map — do not duplicate your siblings

```
notes/gratitude/
  0-structural/   gratitude-structurals.md                  (orchestrator)
  1-roots/        concept-shkr-the-word-of-thanks.md        (shukr: forms, commands, purposes, few/most, God the Thanker, ingratitude's opposition)
                  concept-hamd-praise.md                    (al-ḥamdu li-llāh, bi-ḥamdi, al-Ḥamīd; ḥamd vs shukr tested)
                  concept-nima-the-blessings.md             (niʿma, ālāʾ, faḍl, mann: what the Quran lists as blessings; "remember", "count", "speak of")
  1-narratives/   narrative-the-grateful.md                 (Noah, Abraham, David's family, Solomon, Luqmān, the man at forty, Moses, Joseph, the Prophet, the righteous of 76)
                  narrative-the-ungrateful.md               (Saba', the town of 16:112, the two gardens, Qārūn, the broken vows at sea, self-attribution, kanūd)
                  narrative-occasions-of-thanks.md          (the 14 purposes; senses, food, night/day, sea, the fast, purification, forgiveness, rescue)
  2-cross-cutting/ research-how-the-quran-teaches-gratitude.md   (spine, Opus)
                   research-thanks-praise-glorify-forgive.md      (Opus — the commissioner's framing)
  concept-gratitude-deep.md   (synthesis)
  practice-guide.md           (plain-language guide)
  README.md
```
