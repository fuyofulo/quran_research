# Sulaymān (Solomon): shared brief

> Read `notes/agent-context.md` FIRST (conventions, Buckwalter, the tanwīn-alif normalization trap), then
> this, then `notes/prophets/sulaiman/0-structural/sulaiman-structurals.md`. Do NOT read `notes/methodology-log.md`.
> Do NOT read other investigations' files unless your prompt names one.

## Why this investigation exists

This is the first of a series on the prophets named in the Quran, one at a time. The person who
commissioned it is "very interested in his story". They want to know **who Solomon is in the Quran, as
the Quran tells it**: what happened, in what order the text gives it, what each episode teaches, and
what the Quran does *not* say that popular retellings add.

**Privacy rule (hard).** This repository is public. Write nothing about the commissioner's personal
life. Refer to the reader as "the reader" or "someone".

**Tone.** Be direct, and honest about what the text says and where it is silent. Be warm, not
preachy. Mark every interpretation.

## Deliverables downstream of your file

1. A synthesis (`concept-sulaiman-deep.md`).
2. **A plain-language story guide** (`story-guide.md`). It retells Solomon's life from the Quran alone,
   in warm, simple English for someone new to it. Each episode is followed by what it shows, and a box
   lists "what the Quran does not say".

Write with these in mind. Wherever your material gives the reader a clear episode, a line worth
remembering, or something to take into life, name it.

## Phase-0 findings: established, build past them (details in the structurals file)

- **17 tokens / 16 ayahs / 7 surahs.**
  - The story is in 5 passages, 50 verses: 27:15-44 (30), 38:30-40 (11), 21:78-82 (5), 34:12-14 (3) and 2:102 (1).
  - David is in the same ayah 7 times.
  - Sabaʾ is named twice (27:22, 34:15).
- **Never titled "prophet" or "messenger" by himself.** His prophethood comes through 4:163 (*We revealed
  to … Solomon*) and 6:84-89 (*the Book, judgment and prophethood*).
- **Thanks is the densest theme.**
  - 7 of the Quran's 75 *shukr* tokens: 27:19, 27:40 ×3, 34:13 ×2, and 21:80.
  - 2 of its 3 first-person *shukr* are his: *enable me to be grateful* (27:19), and *to test me whether
    I will be grateful or ungrateful* (27:40).
- **Hapax**: *fhm* only at 21:79 (*We made Solomon understand it*). Also *hudhud*, *ʿifrīt*,
  *ṣāfināt* and *jiyād*.
- **Shared formulas**:
  - *niʿma l-ʿabdu innahu awwāb* only for Solomon (38:30) and Job (38:44).
  - *la-zulfā wa ḥusna maʾāb* only for David (38:25) and Solomon (38:40).
  - *awwāb* 5× in the Quran, 4 of them in Ṣād.
- **Divergence**:
  - The story translates more steadily than average (median 0.613 vs 0.635).
  - Hotspots: 38:40 (97th pct), 38:31 (92nd), 27:37, 27:43, 27:32, 27:29, 27:17, 38:32.

## Data: use these; do not open whole corpus files

| Path | What |
|---|---|
| `data/structural/sulaiman-versepack.json` | **Start here.** 92 verses (Arabic, Saheeh, Khattab). Groups: `naml` (27:15-44), `sad` (38:17-44: David's trial, Solomon, Job), `saba` (34:10-19), `anbiya` (21:78-84), `baqarah` (2:101-103), `lists-and-david` (4:163-165, 6:83-90, 17:55, 2:251, 5:78), `hotspots` (adds Pickthall and Arberry). |
| `data/structural/sulaiman-census.json` | Passages, root counts in story vs Quran, shared phrases, divergence ranks. |
| `data/structural/prophets-census.json` | The 25 named prophets, counts and title evidence. |
| `data/morphology/words.jsonl` | Only by grep/python for a specific root or lemma (e.g. the four uses of *jasad*). |
| `data/arabic/quran.json` + `data/translations/{saheeh,khattab}.json` | Single-verse lookups outside the pack only, by python one-liner. |

## Traps

- **Popular retellings come from outside the Quran.** Hadith, tafsīr and the *Isrāʾīliyyāt* are outside
  the evidence base. Name them as tradition when you meet them, test them against the text, and never
  import them as fact. They include:
  - the ring and the demon (often called Ṣakhr) who took Solomon's throne;
  - the queen's name, Bilqīs, and a marriage to her;
  - the glass floor built to see her legs;
  - Solomon leaning dead on his staff for a year;
  - the 70 or 100 wives, and the half-born child laid on his throne;
  - "bring back the sun" for the horses;
  - Hārūt and Mārūt with Zuhra;
  - the Temple.
  Saying "the Quran is silent on this" is a finding.
- **38:31-33 is genuinely open.**
  - Whether *khayr* in *ḥubb al-khayr* means "good things", "wealth" or "horses".
  - Whether the subject of *tawārat bi-l-ḥijāb* is the sun or the horses.
  - Whether *masḥ bi-l-sūqi wa-l-aʿnāq* is striking or stroking.
  Give each reading, the grammar for it, and which the text favours. Do not settle it by tradition.
- **38:34 *jasad*.** Use its other three uses (7:148, 20:88, 21:8) to bound the word. Do not fill it in.
- **2:102 *wa mā unzila ʿalā l-malakayn*.** The *mā* can be relative ("what was sent down") or
  negative ("nor was it sent down"). Name both.
- **"We" in 27:16** (*ʿullimnā manṭiq al-ṭayr*) may be royal, or David and Solomon together. Say which the
  context supports.
- **Normalization**: rejoin the detached tanwīn alif before any Arabic string search.

## Output rules

- **Hard cap 2,000 words per file.** Truncate rather than overshoot.
- Open with a **100-word headline block.**
- **Max 5 full Arabic + translation panels.** Cite everything else as `[s:a]`.
- Mark **data-grounded** vs **[interpretive]**.
- End with **"For the story guide"**: 3–6 plain lines on the episodes and lessons this file gives the
  retelling.
- Do not append to `notes/methodology-log.md`. Do not commit. Write with the Write tool, then `ls` to
  confirm. For scratch files use `mktemp -d`, never a shared `/tmp` path.

## File map: do not duplicate your siblings

```
notes/prophets/sulaiman/
  0-structural/    sulaiman-structurals.md                              (orchestrator)
  1-narratives/    narrative-the-ant-the-hoopoe-and-the-queen.md        (27:15-44)
                   narrative-the-horses-the-trial-and-the-kingdom.md    (38:30-40, 34:12-14, 21:81-82)
                   narrative-judgment-inheritance-and-defence.md        (21:78-80, 27:15-16, 2:102, the lists, David's frame: 38:17-26, 34:10-11, 2:251)
  2-cross-cutting/ research-what-kind-of-king.md                        (Opus: power, thanks, test, turning back; against the Quran's other men of power)
  concept-sulaiman-deep.md   (synthesis)
  story-guide.md             (plain-language retelling)
  README.md
```
