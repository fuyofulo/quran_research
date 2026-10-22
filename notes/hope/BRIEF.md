# Hope and despair — shared brief

> Read `notes/agent-context.md` FIRST (conventions, Buckwalter, the tanwīn-alif normalization trap), then
> this, then `notes/hope/0-structural/hope-structurals.md`. Do NOT read `notes/methodology-log.md`.
> Do NOT read other investigations' files unless your prompt names one.

## Why this investigation exists

The believer who commissioned the fasting, tahajjud, regret and istighfār investigations asked for it.
It came out of a conversation about long trials and a long-held wish not yet granted. Their request:
*"let's do a proper investigation on hope and despair."* What they want from the Quran: **what it
says to someone who is losing hope** — what hope is, what despair is, what God says to people at
breaking point, and what to do with a wish that has not been given.

**Privacy rule (hard).** This repository is public. Write nothing about the commissioner's personal
life, and no guesses about it. The applied sections speak to *anyone* in a long trial or with an
unanswered wish. Refer to the reader as "the reader" or "someone", never "he" or "she".

**Tone.** Direct and honest about what the text says, and honest where it is silent. Warm, not
preachy. Do not promise what the Quran does not promise. Above all, do not promise that a specific
wish will be granted.

## Deliverables downstream of your file

1. A synthesis (`concept-hope-deep.md`).
2. **A plain-language guide for someone whose hope is running low** (`practice-guide.md`). Write
   with it in mind: wherever your material gives a person something to *say*, *do* or *hold onto*,
   name it.

## Phase-0 findings — established, build past them (details in the structurals file)

- **`rajā` (hope), 23 hope-sense tokens: the object is God's side in 19.** That means His mercy, the
  meeting with Him, the Last Day, or "from God". **11 of the 23 are negated**, and *"those who do not
  hope for the meeting with Us"* describes deniers 4× (10:7, 10:11, 10:15, 25:21); 7 of the 11 negations
  concern the hereafter. *(CORRECTED from "7×".)* **`rajā` has 0 first-person forms.** **Affirmed hope is tied to action**: 18:110,
  29:5, 33:21, 60:6, 2:218, 35:29, 39:9. Its only hope-sense imperative is 29:36. 4:104 sets both
  polarities in one verse.
- **`ʿasā` ("perhaps"), 28 ayahs, God is the subject in 15.** This is how prophets voice worldly hope
  in hard moments: 12:83, 28:22, 7:129, 18:24, 18:40, 68:32, 60:7. It also carries 2:216 and 4:19:
  *perhaps you hate a thing and it is good for you.*
- **Despair (`yʾs`/`qnṭ`, 16 ayahs): 10 are faulted or forbidden, 6 unblamed or neutral.** In the
  faulted cases the object is God's mercy, His *rawḥ*, His glad tidings, or the hereafter (6). The
  other 4 are the reflex *"when harm touches him"*: 11:9, 17:83, 30:36, 41:49. Each reflex is paired
  with exultation in ease, and 11:11 gives the exception: *those who are patient and do good.*
  **Unblamed**: the messengers' despair (12:110, object unstated in the Arabic), and people before rain (42:28).
  **`iblās` (`bls`) is end-despair**: 4 of its 5 cases are in punishment.
- ***ḥattā idhā* ("until, when…") runs both ways.** At the edge of despair, the messengers receive
  help (12:110, 9:118, cf. 2:214). The heedless are seized (6:44, 23:77).
- **Hope with fear** shares an ayah 7×: in prayer (7:56, 32:16, 21:90), in the devotee (17:57, 39:9),
  and in lightning (13:12, 30:24).
- **God answers**, 14 ayahs: including **four consecutive *fa-stajabnā lahu* in Sūrat al-Anbiyāʾ**
  (21:76, 84, 88, 90). And 10:89: *your prayer is answered — so stay straight.*
- **Replacement, "better than it"**: 8:70, 18:40, 18:81, 66:5, 68:32, 24:55, 25:70. The warning
  case is 7:95.
- **Hardship and ease** share 6 ayahs. At 94:5-6, ease is *with* hardship, stated twice; 94:8 then
  says *to your Lord turn your longing*. **`rgb` + to God** occurs 3×: 9:59, 68:32, 94:8.
- **`faraj` (relief) never occurs in the Quran.** Every `frj` token means chastity or rifts. The
  relief words are `rawḥ` (3×), `yusr`, `kashf al-ḍurr`, `najāt` and `makhraj` (65:2).
- **Grief (`ḥzn`, 42 ayahs)**: 18 are *do not grieve* or *let it not grieve you*, and 13 are the
  formula *no fear on them, nor will they grieve*. Jacob grieves and is not blamed (12:84-86).

## Data — use these; do not open whole corpus files

| Path | What |
|---|---|
| `data/structural/hope-versepack.json` | **Start here.** 525 verses, Arabic + Saheeh + Khattab, in groups: `hope-rjw`, `asa`, `aspiration-and-fear`, `wishing`, `despair`, `distress-and-rescue`, `ease`, `those-who-waited`, `the-prophet-consoled`, `shaken-communities`, `answers-and-wishes`, `grief` (all 42 `ḥzn` ayahs), `grief-synonyms`, `trust-and-nearness`. |
| `data/structural/hope-census.json` | Lemma tables, the `rajā` object/polarity annotation, `ʿasā` subjects, `ṭamaʿ` and despair valence, pairings, answers, replacement, hardship/ease, divergence. |
| `data/concepts/<root>.json` | Per-root profiles. Built: `rjw`, `TmE`, `rgb`, `mny`, `yAs`, `qnT`, `bls`, `Hzn`, `whn`, `Dyq`, `gmm`, `krb`, `ysr`, `njw`, `xwf`, `Sbr`, `wkl`, **`Esy-عسي`** (ʿasā), **`Esr-عسر`** (hardship). Build others with `python3 scripts/build_concept.py <root>`. **Case twins — use the disambiguated names**: `Esy-عسي.json` is ʿasā, while the legacy `ESy.json` is ʿaṣā (*disobey*); `Esr-عسر.json` is hardship, while `ESr.json` is *time/afternoon*; `qnT.json` is despair (قنط), while `qnt-قنت.json` is devout. |
| `data/arabic/quran.json` + `data/translations/{saheeh,khattab}.json` | Single-verse lookups only, by python one-liner. |

## Traps

- **`rjw` polysemy**: 7:111, 26:36, 33:51 (postpone), 9:106 (deferred), 69:17 (edges). These are not hope.
- **71:13** (*mā lakum lā tarjūna li-llāhi waqārā*): translators split between *hope for* and *fear/expect*. Note the split; don't build on either.
- **`ʿasā`**: the classical claim that *ʿasā from God is certain* is tafsīr. It is outside the evidence base: name it as a traditional view if at all, and never rest a finding on it.
- **`ghmm`** includes *ghamām* (clouds). **`mny`** includes *semen*. **`yʾs` 13:31** means "know". **`ṭmʿ`** includes greed. **`hmm` is the verb *hamma* (intend), not worry, except 3:154.** **57:23 is grief (`taʾsaw`), not despair** — Saheeh's "despair" misleads (also 12:69).
- **Normalization**: rejoin the detached tanwīn alif before any Arabic string search (see `agent-context.md`).
- **Do not import hadith or tafsīr** (e.g., "I am as My servant thinks of Me", "know that victory comes with patience, relief with distress"). If a well-known saying is *not* in the Quran, saying so is a finding.

## Output rules

- **Hard cap 2,000 words per file.** Truncate rather than overshoot.
- Open with a **100-word headline block.** The synthesis reads headlines first.
- **Max 5 full Arabic + translation panels**; cite everything else as `[s:a]`.
- Mark **data-grounded** (counts, tables) vs **[interpretive]**.
- End with **"For the one losing hope"**: 3–6 plain lines on what this gives a person to say, do, or hold onto. It must be faithful to the text and must not promise outcomes.
- Do not append to `notes/methodology-log.md`. Do not commit unless your prompt says so. Write with the Write tool, then `ls` to confirm.

## File map — do not duplicate your siblings

```
notes/hope/
  0-structural/   hope-structurals.md                       (orchestrator)
  1-roots/        concept-the-hope-words.md                 (rajā, ʿasā, ṭamaʿ, raghba, amal)
                  concept-the-despair-words.md              (yaʾs, qunūṭ, iblās; grief, wahn, ḍīq, ghamm, karb)
                  concept-ease-rescue-relief.md             (ʿusr/yusr, kashf, najāt, rawḥ, makhraj, faraj's absence)
  1-narratives/   narrative-those-who-waited.md             (Jacob, Zechariah, Abraham & Sarah, Job, Jonah, Moses's mother, Maryam, Moses, Joseph, Noah)
                  narrative-at-breaking-point.md            (the Prophet consoled; communities shaken; "do you think…"; thinking of God)
                  narrative-wishes-and-answers.md           (wishing vs hoping, answered and unanswered prayers, "better than it", 2:216)
  2-cross-cutting/ research-hope-and-despair.md             (spine, Opus)
                   research-when-the-wish-is-not-given.md   (Opus)
  concept-hope-deep.md   (synthesis)
  practice-guide.md      (plain-language guide)
  README.md
```
