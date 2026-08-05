# Tahajjud / night-worship investigation — shared brief

> Read `notes/agent-context.md` FIRST (project conventions, Buckwalter, output rules), then this.
> Do NOT read `notes/methodology-log.md`. Do NOT read other investigations' per-root files.
> The one exception is named explicitly in the comparison agent's prompt.

## Why this investigation exists

The same person who commissioned the fasting investigation (`notes/fasting/`) is now asking about
tahajjud. His framing: *"when it comes to fasting and tahajjud I think tahajjud is extremely hard. I
just want to learn more about tahajjud and how it is different from fasting according to the Quran."*

He asked for maximum depth. Take it.

Two deliverables sit downstream of your file: a synthesis, and a **direct comparison between the
Quranic night-vigil and the Quranic fast**. Write with the comparison in mind — wherever your
material bears on how night-worship differs from fasting in *kind* (not just in difficulty), say so.

**Tone.** A believer researching his own practice. Direct, unhedged about what the text says, honest
where it is silent. Do not evangelise, do not editorialise, do not preach. Report the text, and mark
where you interpret.

## Phase 0 findings — established, do not re-derive. Build past these.

### The shape of the corpus

**`hjd` (ه ج د) occurs EXACTLY ONCE in the entire Quran** — `wa-mina al-layli fa-tahajjad bihi
nāfilatan lak` at **17:79**. One word, one verse. The entire named practice of "tahajjud" rests on a
single hapax.

But the *described* practice is everywhere. The night-worship vocabulary is large:
`lyl` 92 · `*kr` 292 · `dEw` 212 · `sbH` 92 · `sjd` 92 · `qwm` 660 · `Slw` 99 · `gfr` 234.

**This is the inverse of the fasting corpus**, where the named practice (`Swm`, 14×) is small and the
legislation is concentrated. Here the name is a hapax and the practice is diffuse. That asymmetry is
the investigation's opening question, not its answer.

### The single most important structural fact found in Phase 0

I measured, for every worship-root, what share of its ayahs also contain `lyl` (night):

| Root | Sense | Ayahs with night / total | Share |
|---|---|---|---|
| `nfl` | supererogatory | 1 / 3 | 33.3% |
| **`sbH`** | **glorify (tasbīḥ)** | **9 / 87** | **10.3%** |
| `sjd` | prostrate | 7 / 81 | 8.6% |
| `qnt` | stand devoutly | 1 / 12 | 8.3% |
| `qwm` | stand | 22 / 597 | 3.7% |
| `Slw` | **prayer (ṣalāh)** | **3 / 90** | **3.3%** |
| `tlw` | recite | 1 / 61 | 1.6% |
| `*kr` | remember | 4 / 264 | 1.5% |
| `dEw` | supplicate | 2 / 182 | 1.1% |
| `gfr` | forgive | 2 / 202 | 1.0% |
| `rtl` | recite measuredly | 0 / 2 | 0% |

**The Quran's characteristic night-worship verb is `sabbiḥ` (glorify), not `ṣalli` (pray).** Three
times more night-attached than ṣalāh. Test this hard — it may be the spine of the whole investigation.
`sbH` night refs: 17:1, 20:130, 21:20, 21:33, 36:40, 41:38, 50:40, 52:49, 76:26.

### The second structural fact

Of the 81 ayahs containing `lyl`, the **most frequent companion by far is `nhr` (day) — 42 of 81.**
Then `qwm` 22, `$ms` (sun) 12, `qmr` (moon) 10, `smw` (sky) 10, `sxr` (subjected) 8.

**More than half of the Quran's night-verses are cosmological, not devotional** — night as a *sign*,
paired with day, alternating, subjected. Any claim about "the Quran's night" has to reckon with the
fact that its dominant register is astronomical, not liturgical. Quantify the split before
interpreting it.

### Translator divergence — where the Arabic resists English

Highest-divergence verses in the night corpus (scores in
`data/structural/tahajjud-cooccurrence.json`):

| Ref | Divergence | What they fight over |
|---|---|---|
| **73:1** | **0.933** | `al-muzzammil` — the highest-divergence verse in the entire set |
| 73:7 | 0.917 | `sabḥan ṭawīlā` |
| 26:219 | 0.877 | `taqallubaka fī al-sājidīn` |
| 73:4 | 0.869 | `rattili al-Qurʾāna tartīlā` |
| 50:40 | 0.841 | `adbāra al-sujūd` |
| 73:6 | 0.829 | `nāshiʾat al-layl` / `ashaddu waṭʾan` |
| 3:17 | 0.828 | `al-mustaghfirīna bi-l-asḥār` |

**Surah 73's opening is the most contested passage in the corpus.** Five of the top eight are from it.

### Hapax density

54 lemmas in the night vocabulary occur exactly once. Note especially that **17:78–79 is packed with
them**: `dulūk` (the sun's decline, 1×), `tahajjad` (1×), `maḥmūd` (1×, in `maqāman maḥmūdā`). Three
unique words in two verses. Also `nāshiʾat` (73:6, 1×), `waṭʾ` (73:6, 1×), `yahjaʿūn` (51:17, 1×).

## Data files — use these, do NOT open whole corpus files

| Path | What it is |
|---|---|
| `data/structural/tahajjud-versepack.json` | **Start here.** 184 verses, Arabic + 4 translations, grouped: `tahajjud-verse`, `muzzammil-founding`, `muddaththir-parallel`, `two-portraits`, `night-standing`, `command-to-glorify`, `prayer-timing`, `witnessed-standing`, `sleep-as-sign`, `night-oaths`, `night-as-sign`, `night-of-descent`, `night-of-journey`, `dhikr-general`, `dua-and-nearness`, `istighfar-predawn`, `fasting-for-compare`. |
| `data/structural/tahajjud-cooccurrence.json` | Root totals, everything sharing an ayah with `lyl`, the worship-vs-night table above, the hapax census, pairwise co-occurrence, divergence scores. |
| `data/concepts/<root>.json` | Per-root profiles. Built already: `hjd`, `hjE`, `n$A`, `wTA`, `rtl`, `Any`, `zlf`, `DjE`, `nwm`, `rqd`, `sjd`, `tlw`, `dlk`, `njm`, `ASl`, `bkr`, `gsq`, plus pre-existing `lyl`, `qwm`, `Slw`, `*kr`, `dEw`, `gfr`, `Hmd`, `nfl`, `xwf`, `TmE`, `jnb`, `qll`, `fjr`. |

**Two disambiguated filenames** (macOS is case-insensitive; these roots have case twins):
- **`data/concepts/sbH-سبح.json`** — glorify. NOT `SbH.json`, which is صبح, *morning*.
- **`data/concepts/qnt-قنت.json`** — devoutly obedient. NOT `qnT.json`, which is قنط, *despair*.

## Traps specific to this vocabulary

- **`sbH` ≠ `SbH`.** سبح (glorify, 92) vs صبح (morning, 45). Different roots entirely.
- **`sHr` (س ح ر) is polysemous and dangerous.** It carries BOTH *siḥr* (magic/sorcery) AND *saḥar* /
  *asḥār* (the pre-dawn hour). Disambiguate by **lemma**, never by root.
  **CORRECTED 2026-08-05:** an earlier version of this brief listed `saHaru` as a second pre-dawn
  lemma. That was wrong, and two agents caught it independently. `saHaru` is a **verb meaning "to
  bewitch"** (7:116, 7:132, 23:89) and belongs entirely to the magic sense. The pre-dawn sense is
  carried by **exactly one lemma, `saHar` (N), with exactly three occurrences: 3:17, 51:18, 54:34.**
  Two are pre-dawn forgiveness-seeking; the third is Lot's family being rescued at pre-dawn.
- **`qwm` is huge (660) and mostly means "a people"** (`qawm`, 383). The standing-sense is a minority.
  The lemma table is your disambiguator.
- **`Any`** gives `ānāʾ al-layl` (the hours of the night) — only 3 occurrences, easy to miss.

## Output rules

- **Hard cap: 2,000 words per file** unless your prompt says otherwise. Cut catalogue, keep depth.
- Open with a **100-word headline-finding block**. The synthesis reads headlines first.
- Full Arabic + translation panels: **max 5 verses per file**. Everything else is `[surah:ayah]`.
- Mark **data-grounded** (counts, lemma tables, divergence scores) vs **interpretive** (what it means).
- Do **not** append to `notes/methodology-log.md`.
- End every file with **"For the night"** — 3–6 concrete lines on what this changes about how someone
  would actually pray at night. This investigation is applied; that section is the point.
- Write with the Write tool, then `ls` to confirm.

## File map — don't duplicate your siblings

```
notes/tahajjud/
  0-structural/   tahajjud-structurals.md            (orchestrator)
  1-roots/        concept-hjd-the-one-verse.md
                  concept-lyl-the-night.md
                  concept-sbH-tasbih.md
                  concept-postures-sjd-qwm-qnt.md
                  concept-sleep-vocabulary.md
                  concept-dhikr-dua-istighfar-night.md
  1-narratives/   narrative-surah-73-muzzammil.md
                  narrative-17-78-82-tahajjud.md
                  narrative-two-portraits-51-32.md
                  narrative-ibad-al-rahman-25.md
                  narrative-night-as-divine-timing.md
  2-cross-cutting/ research-why-night.md
                   research-what-is-promised.md
                   research-the-relaxation-73-20.md
                   research-tahajjud-vs-fasting.md
  3-rabbit-holes/ rabbit-maqam-mahmud.md
                  rabbit-nashiat-al-layl.md
                  rabbit-ashar-istighfar.md
                  rabbit-sleep-as-death.md
  concept-tahajjud-deep.md   (synthesis)
  README.md
```
