# Istighfār investigation — shared brief

> Read `notes/agent-context.md` FIRST, then this, then `notes/istighfar/0-structural/istighfar-structurals.md`
> (Phase 0, ~1,500 words). Do NOT read `notes/methodology-log.md`. Do NOT read other investigations'
> files unless your prompt names one.

## Why this investigation exists

The person who commissioned it asked, in one line: *"I want to research how the Quran teaches us to do
istighfār."* He is a believer who has just finished an investigation on regret here (whose finding
was that the Quran never commands regret, but commands *return* — repentance and seeking forgiveness).
He now wants the practice itself: **how to seek forgiveness the way the Quran teaches it.**

Deliverables downstream of your file: a synthesis, and a **plain-language practice guide** — the
Quran's own words for seeking forgiveness, when to use them, what goes with them, and what the text
says they lead to. Write with that guide in mind. Wherever your material answers *what words, when,
how, with what, for whom, to what effect*, say so plainly.

**Tone.** A believer improving his own practice. Direct, unhedged about what the text says, honest
where it is silent. Do not preach. Report the text, and mark where you interpret.

## Phase 0 findings — established, do not re-derive. Build past them.

- **`astaghfiru` (I seek forgiveness) occurs exactly 3× — 12:98, 19:47, 60:4 — all for SOMEONE ELSE,
  all future.** Self-directed istighfār, wherever the Quran quotes it, is **addressed to God in the
  imperative: `rabbi ighfir lī`** — 17 `ighfir` imperatives + 7:23, 11:47 (conditional), 2:285
  (`ghufrānaka`), 26:82 (hope), 5:118 (ʿĪsā, for others) = **22 quoted petitions**.
- **`istighfār` the noun occurs once** (9:114) — an istighfār Ibrāhīm abandoned. `mustaghfirīn` once
  (3:17), `ghufrān` once (2:285).
- **19 `istaghfir-` imperatives**: 8 plural (5 in prophets' sermons; 4 in Sūrat Hūd, all with
  `istaghfirū rabbakum thumma tūbū ilayhi`), 10 singular (8 to the Prophet — 4 for himself, 4 for
  others), 1 feminine (12:29).
- **Glorify + praise + seek forgiveness**: a fixed triad, 4× (40:7, 42:5 angels; 40:55, 110:3 commanded).
- **Mercy is asked alongside forgiveness in 7 petitions (CORRECTED from 10); faith is the stated ground in 6**
  (*our Lord, we have believed, so forgive us* — 3:16, 3:193).
- **Kin**: istighfār for father, brother, parents, sons in 8 ayahs.
- **Core 59 ayahs, 30 Meccan / 29 Medinan.**
- **[interpretive, to be tested]**: several of the times given for istighfār are **endings that follow
  worship or success** — the last part of the night (3:17, 51:18), after ʿArafa (2:199), the close of
  the night-prayer surah (73:20), after victory (110:3).

## Data files — use these; do NOT open whole corpus files

| Path | What it is |
|---|---|
| `data/structural/istighfar-versepack.json` | **Start here.** 195 verses, Arabic + Saheeh + Khattab, 11 groups. **Read only your groups**: `python3 -c "import json;d=json.load(open('data/structural/istighfar-versepack.json'));[print(v['ref'],v['arabic'],'|',v['saheeh']) for g in ['petitions'] for v in d['groups'][g]]"` |
| `data/structural/istighfar-census.json` | Lemmas + refs, verb forms by tense/person, the petition table, root lift, divine-name pairings, divergence. |
| `data/concepts/gfr.json`, `twb.json`, `Efw.json`, `rHm.json` | Root profiles. |
| `data/morphology/words.jsonl` | Only via a streaming script, for person/mood/lemma. Never Read it. |
| Single verses outside the pack | `python3 -c "import json;q=json.load(open('data/arabic/quran.json'));s=json.load(open('data/translations/saheeh.json'))['ayahs'];r='4:17';su,a=map(int,r.split(':'));print(next(x['text'] for x in q['surahs'][su-1]['ayahs'] if x['ayah']==a),'|',s[r])"` |

Groups: `petitions`, `commands-plural`, `commands-singular`, `narrated`, `confession`, `for-others`,
`fruits`, `when`, `tawba`, `divine-forgiveness`, `forgiving-others`.

## Traps

- **`kfr` is polysemous inside the petitions**: `kaffir ʿannā` (*expiate*, 3:193) vs `al-kāfirīn`
  (*disbelievers*, 2:286, 3:147). **`nwr`** too: `al-nār` (*the Fire*) vs `nūr` (*light*). Lemma-level only.
- **`ghafara` has human subjects too** (42:37, 45:14, 64:14 — people forgiving people). Don't count
  every `ghafara` as God's.
- **Form X `istaghfara` ≠ form I `ghafara`.** One is the human seeking; the other is the forgiving.
- **The Prophet as addressee**: a 2MS command may be to the Prophet specifically. Say whether a
  practice is general or addressed to him (the tahajjud investigation found night imperatives were
  all 2MS to the Prophet — check for the same pattern here, don't assume it).
- **Agents in this project have miscounted before.** Compute every count with a script or list refs.
- **Hadith, tafsīr and later fiqh are outside the evidence base** — including the famous formulas
  (*sayyid al-istighfār*, "astaghfirullāh" ×100) and the fiqh conditions of tawba (regret, cessation,
  resolve, restitution). You may name them as "the traditional practice" to say whether the Quran
  states them, but argue from the text.

## Output rules

- **Hard cap: 2,000 words per file** unless your prompt says otherwise. Truncate rather than overshoot.
- Open with a **100-word headline-finding block**.
- Full Arabic + translation panels: **max 5 verses per file**. Everything else `[surah:ayah]`.
- Mark **data-grounded** vs **interpretive**.
- If you find a claim in the structurals or in a sibling file that the text does not support, **say
  so and correct it** in your file.
- Do **not** append to `notes/methodology-log.md`.
- End every file with **"For practice"** — 3–6 concrete lines on what this changes about how someone
  would actually seek forgiveness. That section is the point.
- Write with the Write tool, then `ls` to confirm.

## File map

```
notes/istighfar/
  0-structural/    istighfar-structurals.md                      (orchestrator, done)
  1-roots/         concept-gfr-root-and-names.md                 lemmas, form X vs I, astaghfiru ×3, the divine names
                   concept-the-petitions.md                      the 22 quoted petitions, anatomised
  1-narratives/    narrative-prophets-seeking-forgiveness.md     Adam, Noah, Ibrāhīm, Moses, David, Sulaymān, Yūnus, Jacob, the Prophet
                   narrative-commanded-and-its-fruits.md         the commands, istighfār → tawba, the fruits, the times
                   narrative-for-others-and-forgiving-others.md  for kin / believers / by angels; forbidden; forgiving people
  2-cross-cutting/ research-how-the-quran-teaches-istighfar.md   SPINE: the method, built and attacked
                   research-istighfar-negative-space.md          what the Quran does not say
  concept-istighfar-deep.md   (synthesis)
  practice-guide.md           (plain-language guide)
  README.md
```
