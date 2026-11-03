# Patience (ṣabr): shared brief

> Read `notes/agent-context.md` FIRST (conventions, Buckwalter, the tanwīn-alif normalization trap), then
> this, then `notes/patience/0-structural/patience-structurals.md`. Do NOT read `notes/methodology-log.md`.
> Do NOT read other investigations' files unless your prompt names one.

## Why this investigation exists

The commissioner asked for an in-depth study of patience, in the same way as the earlier topics. They
want to know **what the Quran itself calls patience**: who is patient in it, what they do and feel, what
they are told, what they are promised, and what patience is *not*. The study comes out of reading about
Job (*"We found him patient… always turning back"*, 38:44).

**Privacy rule (hard).** This repository is public. Write nothing about the commissioner's personal
life. Refer to the reader as "the reader" or "someone in a long hardship".

**Tone.** Direct, honest about what the text says and where it is silent. Warm, not preachy. Never tell
the reader what they should feel. Mark every interpretation.

## Deliverables downstream of your file

1. A synthesis (`concept-patience-deep.md`).
2. **A plain-language practice guide** (`practice-guide.md`) for someone in a long hardship. It covers what
   patience is in the Quran, what it is not, the Quran's own words to say, and the people to remember.
   Warm, simple English. Every fact kept.

Write with these in mind. Wherever your material gives the reader a clear line to hold, a person to
remember, or a thing patience is *not*, name it.

## Phase-0 findings: established, build past them (details in the structurals file)

- **103 tokens / 93 ayahs / 45 surahs; 62 are verbs.** Lemmas: *ṣabara* 58, *ṣābir* 20, *ṣabr* 15,
  *ṣabbār* 4, *iṣṭabara* 3, *ṣābirū*, *ṣābira* and *ṣābirāt* 1 each.
- **29 imperative tokens in 28 ayahs. 20 are to the Prophet, 19 of them Meccan.** Each carries a second
  clause: "over what they say", "for your Lord's judgment", "God's promise is true", "until God judges",
  "beautiful patience", "your patience is only through God". 4 are joined to *glorify with praise*.
- **Misdirected patience in 7 ayahs** (2:61, 2:175, 14:21, 25:42, 38:6, 41:24, 52:16). Patience is
  weighed by its object.
- **Formulas:**
  - *God is with the patient* 4×; *loves the patient* 1× (3:146); *good news* 1× (2:155);
  - *for what they endured* 6×; *ṣabbārin shakūr* 4×;
  - *ṣabr jamīl* 3× (12:18, 12:83, 70:5); *pour patience upon us* 2× (2:250, 7:126);
  - *matters of resolve* 3×; *without account* for the patient only at 39:10;
  - *you will find me, God willing, …*: Moses (18:69), Abraham's unnamed son (37:102), the unnamed old man of Midian (28:27, no ṣ-b-r). (CORRECTED)
- **Never in the same ayah as patience:** despair (*yaʾs*, *qunūṭ*) and forbearance (*ḥilm*). Grief only 16:127.
- **God is never the subject of ṣ-b-r**; *al-Ṣabūr* is not a Quranic name.
- **Densest passage:** 18:60-82 (7 tokens), patience with what one does not understand (18:68).
- **Divergence:** patience verses translate less steadily than the corpus (median 0.649 vs 0.635).
  Hotspots: 42:43 (97th pct), 3:200, 41:35, 3:17, 18:68, 13:24, 68:48, 73:10.

## Data: use these; do not open whole corpus files

| Path | What |
|---|---|
| `data/structural/patience-versepack.json` | **Start here.** 285 verses (Arabic, Saheeh, Khattab). Groups: `sbr-all` (all 93 ṣ-b-r ayahs), `neighbours` (panic, haste, weakening, swallowed grief, despair), `figures` (Jacob, Joseph, Job, 18:60-82, Ishmael, the magicians, Ṭālūt, Jonah, the messengers, Luqmān, Ṣāliḥ, Shuʿayb), `prophet-commands` (every command to the Prophet with its surroundings), `community`, `rewards`, `hotspots` (adds Pickthall and Arberry). |
| `data/structural/patience-census.json` | Lemma, mood and person tables, addressees, objects, formulas, pairings, neighbours, divergence. |
| `data/morphology/words.jsonl` | Only by grep/python for a specific root or lemma. |
| `data/arabic/quran.json` + `data/translations/{saheeh,khattab}.json` | Single-verse lookups outside the pack only, by python one-liner. |

## Traps

- **Hadith, tafsīr and later ethics are outside the evidence base.** Name them as tradition when you
  meet them; never import them as the Quran's own. Common imports:
  - "patience is half of faith";
  - "patience is at the first blow";
  - the three kinds of patience;
  - *al-Ṣabūr* as a divine name;
  - "patience means not complaining".

  Test each against the text. "The Quran is silent on this" is a finding.
- **Do not read "patience" as passivity or silence without checking.** Test it against the fighting
  verses (2:249-250, 3:146, 8:45-46, 8:65-66), restraint from retaliation (16:126, 42:43), and the
  complaints of patient people (12:86, 21:83).
- **Do not count adjacency as co-occurrence.** 12:83 (*ṣabr jamīl*) and 12:84 (eyes white with grief)
  are neighbours, not one ayah. Say which you mean.
- **"With" and "for" are different.** *maʿa ṣ-ṣābirīn* (God is with), *li-ḥukmi rabbika* (for your Lord's
  judgment), *ʿalā mā* (over what). Keep the prepositions.
- **Normalization:** rejoin the detached tanwīn alif before any Arabic string search.

## Output rules

- **Hard cap 2,000 words per file.** Truncate rather than overshoot.
- Open with a **100-word headline block.**
- **Max 5 full Arabic + translation panels.** Cite everything else as `[s:a]`.
- **Copy Arabic exactly from the versepack or `data/arabic/quran.json` by script. Never type Arabic from
  memory.** The orchestrator checks every Arabic run against the source.
- Mark **data-grounded** vs **[interpretive]**.
- End with **"For the practice guide"**: 3–6 plain lines on what this file gives the guide.
- Do not append to `notes/methodology-log.md`. Do not commit. Write with the Write tool, then `ls` to
  confirm. For scratch files use `mktemp -d`, never a shared `/tmp` path.

## File map: do not duplicate your siblings

```
notes/patience/
  0-structural/    patience-structurals.md                 (orchestrator)
  1-roots/         concept-sbr-the-word.md                  (the word: forms, objects, misdirected patience, neighbours, negative space)
  1-narratives/    narrative-the-patient-ones.md            (the people: Jacob, Job, Joseph, Moses and the man of knowledge, Ishmael, the magicians, Ṭālūt, the messengers, Luqmān, Jonah)
                   narrative-commands-and-promises.md       (the 20 commands to the Prophet, the community, the promises, the time words)
  2-cross-cutting/ research-what-patience-is-and-is-not.md  (Opus: grief and complaint, knowledge, time, action and restraint, thanks, prayer, turning back)
  concept-patience-deep.md   (synthesis)
  practice-guide.md          (plain-language guide)
  README.md
```
