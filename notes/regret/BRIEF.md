# Regret investigation — shared brief

> Read `notes/agent-context.md` FIRST (project conventions, Buckwalter, output rules), then this,
> then `notes/regret/0-structural/regret-structurals.md` (the Phase-0 pre-cut — ~1,800 words).
> Do NOT read `notes/methodology-log.md`. Do NOT read other investigations' files unless your
> prompt names one.

## Why this investigation exists

The person who commissioned it asked: *"What are the things the Quran has mentioned that humans will
regret, maybe in this life, maybe in the hereafter? If we have a list of all of them, we can
reverse-engineer what actions could cause them and what feelings could cause them. That way I can
introspect myself — am I making decisions that will lead to those regrets?"*

So there are three deliverables downstream of your file:
1. **A complete list** of every regret the Quran names.
2. **A reverse-engineering** of each: the actions that lead there, and the inner states behind them.
3. **A self-examination instrument** built from (1) and (2).

Write for all three. He has said this is collaborative and open-ended — he will work on the
reverse-engineering with us afterwards. So **precision about what the text actually says matters
more than completeness of interpretation.** Leave clear seams where a human can push further.

**Tone.** A believer examining his own life. Direct, unhedged about what the text says, honest
where it is silent. Do not preach, do not frighten, do not console. Report the text, and mark where
you interpret.

## The reverse-engineering protocol — use it for every regret you handle

For each regret, extract these five fields. **Fields 3 and 5 are where agents go wrong.**

| # | Field | Rule |
|---|---|---|
| 1 | **Who, when** | Speaker; setting L (this life) / D (at death or as punishment arrives) / H (hereafter) |
| 2 | **What they regret — in their own words** | Quote the Arabic phrase, then gloss. The object of the wish. |
| 3 | **The cause the TEXT states** | Only a clause that is actually in the verse or its passage: `ʿalā mā farraṭtu`, `laqad aḍallanī ʿan al-dhikr`, `innā aṭaʿnā sādatanā`, `law kunnā nasmaʿu aw naʿqilu`, `mā aẓunnu an tabīda hādhihi abadā`. If the text states no cause, write **"no cause stated"** — that is a finding. |
| 4 | **The action pattern** | What they did or failed to do, as the passage shows it. |
| 5 | **The inner state** | **Two columns, kept apart.** (a) *Named* — a state the text names with a word (`ghafla` heedlessness, `kibr`/`istakbara` arrogance, `ẓann` assumption, `amānī` wishful thinking, `rayb` doubt, `ḥubb` love of …, `hawā` desire, `sukhriya` mockery, `ʿajala` haste). Give the word and ref. (b) *Inferred* — your reading of a state the text implies but does not name. Mark it **[inferred]**. Never promote (b) to (a). |

The person wants to know *what feelings* cause regret. The Quran names some, implies some, and is
silent on others. All three are useful to him if — and only if — they are kept separate.

## Phase 0 findings — established, do not re-derive. Build past them.

Full detail in `0-structural/regret-structurals.md`. The essentials:

- **65 core ayahs; 56 are regret over one's own conduct.** Setting: **H 34 · D 10 · L 12**.
  Meccan 46 / Medinan 10. (17:29 `maḥsūr` excluded after Phase 1 — it means *depleted*.) Speaker: plural dominant in the hereafter (16 P / 9 S / 9 narrated).
- **Two words, two worlds.** `nādim` (5×) is this-life only, and **all 5 take `aṣbaḥa`** (*became* —
  CORRECTED: not "woke up to"; only 2 of 28 `aṣbaḥa` ayahs are literal morning). `nadāma` (2×) is hereafter only, both the identical clause *they concealed
  regret when they saw the punishment* (10:54, 34:33). `ḥasra` (8× + `yā ḥasratā` 39:56) spans both
  and is also used for lament over others (35:8, 36:30) and for a regret God *makes* (3:156, 8:36).
- **Regret is triggered by seeing.** `rAy` in 12/56 self-regret ayahs (lift ×4.5); *seeing the
  punishment* in 8 ayahs; 2:167 *God will show them their deeds as regrets*; 50:22.
- **The wish has four shapes** [orchestrator classification]: undo / return / separate / unexist.
- **The hands**: all three regret gestures are hand-gestures (25:27, 18:42, 7:149); 78:40 and 89:24
  embed *what the hands sent forward* inside the regret speech.
- **Same confession, two outcomes**: `innā kunnā ẓālimīn` at 7:5 / 21:14 / 21:46 (too late) vs 68:29
  (this life, followed by hope at 68:32).
- **`min qabli an yaʾtiya`** (*before there comes*) 8× — the text pre-empts regret by name.
- **Three registers**: regret that converts (repentance) · regret that cannot (too late) · regret the
  Quran forbids (`lā taʾsaw ʿalā mā fātakum` 57:23; 3:153; 35:8; the "if only" of fate made into
  ḥasra at 3:156). Plus sorrow it praises (9:92).

## Data files — use these; do NOT open whole corpus files

| Path | What it is |
|---|---|
| `data/structural/regret-versepack.json` | **Start here.** 390 verses, Arabic + Saheeh + Khattab, in 16 groups. **Read only your groups**, e.g. `python3 -c "import json;d=json.load(open('data/structural/regret-versepack.json'));[print(v['ref'],v['arabic'],'|',v['saheeh']) for g in ['layta'] for v in d['groups'][g]]"` |
| `data/structural/regret-census.json` | Marker inventory with refs, the annotated core set, root lift, translator divergence. |
| `data/morphology/words.jsonl` | Only if you need morphology (person, mood, lemma). Stream it with a script; never Read it. |
| `data/translations/{arberry,pickthall}.json` | Only for a specific verse whose translation you are contesting. |

Groups: `lexical-ndm`, `lexical-hasra`, `layta`, `woe-cry`, `return-requests`, `wish-wadda`,
`hand-gestures`, `neglect-farrata`, `confession`, `the-window`, `this-life-narratives`,
`blame-dialogues`, `forbidden-or-praised-sorrow`, `hands-sent-forward`, `loss-and-taghabun`,
`stated-causes`.

## Traps specific to this vocabulary

- **`Hsr` is polysemous**: `ḥasra` (regret) vs `yastaḥsirūn` (21:19) / `ḥasīr` (67:4) = *weariness*.
  17:29 `maḥsūr` is contested between the two — say which reading you take and why.
- **`wyl`** — `yā waylatā` at 11:72 is Sarah's astonishment, not regret. The woe-cry is not always
  remorse; check the context.
- **`layta` is not always regret**: 19:23 (Maryam, innocent distress), 36:26 (the martyr wishing his
  people knew), 28:79 (envy). Classify; don't count blindly.
- **`SbH` (صبح, morning) ≠ `sbH` (سبح, glorify).** The `aṣbaḥa` finding is `SbH`. Case-sensitive.
- **Agents in this project have miscounted before.** Every count you state, compute with a script or
  list the refs so it can be checked.
- **Hadith, tafsīr and later theology are outside the evidence base.** If you know a famous reading
  (e.g. what Cain regretted), you may name it as "the traditional reading" but argue from the text.

## Output rules

- **Hard cap: 2,000 words per file** unless your prompt says otherwise. Truncate rather than overshoot.
- Open with a **100-word headline-finding block**. The synthesis reads headlines first.
- Full Arabic + translation panels: **max 5 verses per file**. Everything else `[surah:ayah]`.
- Mark **data-grounded** (counts, lemma facts, clauses quoted) vs **interpretive**.
- Do **not** append to `notes/methodology-log.md`.
- End every file with **"For introspection"** — 3–6 concrete questions or checks a person could
  actually run on their own life, derived from your material. This investigation is applied; that
  section is the point. Questions, not sermons.
- Write with the Write tool, then `ls` to confirm.

## File map — don't duplicate your siblings

```
notes/regret/
  0-structural/    regret-structurals.md                  (orchestrator, done)
  1-roots/         concept-ndm-hsr-the-two-words.md       nadam, nādim, ḥasra, maḥsūr; aṣbaḥa; asarrū
                   concept-the-speech-of-regret.md        layta, woe-cry, return-requests, wadda-law; God's replies
  1-narratives/    narrative-regret-in-this-life.md       Cain, garden-owner, garden-people, calf, Thamūd,
                                                          Joseph's brothers, the three left behind, 49:6, 4:73, 28:79
                   narrative-blame-and-companions.md      followers vs leaders, the friend, the companion-devil, Satan's speech
                   narrative-the-closing-window.md        death-bed, late belief, 4:17-18, 10:90-98, the replies
                   narrative-stated-causes.md             74:38-48, 69:30-37, 89:15-24, 57:12-15 … the self-diagnoses
  2-cross-cutting/ research-the-regret-catalog.md         SPINE: the complete list + reverse-engineering
                   research-regret-that-works.md          converts / too late / forbidden — the three registers
  concept-regret-deep.md      (synthesis)
  self-examination.md         (the introspection instrument)
  README.md
```
