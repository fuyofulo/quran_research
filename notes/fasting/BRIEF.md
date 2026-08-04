# Fasting investigation — shared brief

> Read `notes/agent-context.md` FIRST (project conventions, Buckwalter, output rules), then this file.
> This is the investigation-specific brief. Do not read `notes/methodology-log.md`. Do not read other
> investigations' per-root files. Everything you need is here or in the data files listed below.

## Why this investigation exists

The person commissioning this research fasted seven consecutive days with the intention of getting
closer to Allah, and reports that it did not work. His diagnosis: he was not *intentional* about it —
he fasted, but did not do the things a fast is supposed to be built around. He wants to know:

1. **What does the Quran actually say about fasting?** Not the inherited practice — the text.
2. **What does science say about fasting?** Physiology, cognition, mood, behaviour.
3. **What have people actually experienced?** Accounts posted publicly about fasting and spiritual state.

The deliverable is not just description. It has to be *usable*: what would make a fast actually do the
thing 2:183 says it is for. Every file should end with something that survives contact with a real
person at 3pm on day four of a fast.

**Tone rule.** This is a believer researching his own practice, not an outsider studying a religion.
Write accordingly: direct, unhedged about what the text says, honest about where the text is silent.
Do not evangelise and do not editorialise about Islam. Report the text. Where you interpret, say so.

## Phase 0 findings (already established — do not re-derive)

The core root is **`Swm` (ص و م)** — capital S. Note the collision hazard: `swm` (س و م) is a
*different root* (sīma / branding / to impose). The concept profile is at
**`data/concepts/Swm-sad-fasting.json`** (non-standard filename because macOS is case-insensitive and
`Swm.json` would clobber `swm.json`). Do not run `build_concept.py Swm` — it will overwrite `swm.json`.

**`Swm` occurs 14 times in the entire Quran, across 11 ayahs, 6 surahs.** That is astonishingly few
for a pillar. The full occurrence list:

| Ref | Form | Lemma | What it is doing |
|---|---|---|---|
| 2:183 | ٱلصِّيَامُ | ṣiyām | the prescription + the stated purpose (*laʿallakum tattaqūn*) |
| 2:184 | تَصُومُوا۟ | yaṣum (V) | "and that you fast is better for you" |
| 2:185 | فَلْيَصُمْهُ | yaṣum (V) | "whoever witnesses the month, let him fast it" |
| 2:187 | ٱلصِّيَامِ | ṣiyām | "the night of the fast" |
| 2:187 | ٱلصِّيَامَ | ṣiyām | "then complete the fast until the night" |
| 2:196 | صِيَامٍ | ṣiyām | hajj: fasting as one option in a ransom-triad |
| 2:196 | فَصِيَامُ | ṣiyām | hajj: three days + seven = ten, substituting for an offering |
| 4:92 | فَصِيَامُ | ṣiyām | expiation for killing a believer by mistake |
| 5:89 | فَصِيَامُ | ṣiyām | expiation for a broken oath |
| 5:95 | صِيَامًا | ṣiyām | expiation for killing game in iḥrām |
| 58:4 | فَصِيَامُ | ṣiyām | expiation for ẓihār |
| 19:26 | صَوْمًا | ṣawm | **Maryam's fast — of SPEECH, while eating and drinking** |
| 33:35 | ٱلصَّٰٓئِمِينَ | ṣāʾimīn | the fasting men, in the list of ten |
| 33:35 | ٱلصَّٰٓئِمَٰتِ | ṣāʾimāt | the fasting women, in the list of ten |

**Three structural facts that fell out immediately. Build on these; do not just restate them.**

1. **The distribution is lopsided against Ramadan.** Only 5 of 14 occurrences concern the annual fast.
   **Five** concern *kaffāra* — expiation, a fast imposed as repair for something broken (4:92, 5:89,
   5:95, 58:4, and 2:196's substitution). One is a hajj substitute. One is an identity label. One is
   Maryam. The Quran's dominant grammatical mode for fasting is **restitution**, not devotion.

2. **13 of 14 occurrences are Medinan. The single Meccan one is 19:26 — the fast of silence.**
   The fast from *food* is entirely legislative/Medinan. The fast from *speech* is the Meccan one, and
   it is the only place the bare masdar `ṣawm` appears unqualified.

3. **2:186 sits inside the fasting passage.** Between the command to fast (185) and the rules of the
   fast (187), the Quran interrupts itself: *"And when My servants ask you about Me — indeed I am near.
   I respond to the call of the caller when he calls Me."* No other topic intrudes into the passage.
   The verse about **nearness to God** is embedded in the middle of the fasting instructions. This is
   almost certainly the answer to the commissioning question and it should be tested hard, not assumed.

## Data files for this investigation (use these; do NOT read whole corpus files)

| Path | What it is |
|---|---|
| `data/structural/fasting-versepack.json` | **Start here.** 131 verses — Arabic + all 4 translations — grouped by theme (`core-ramadan`, `expiation`, `maryam-silence`, `qadr-night`, `sabr-support`, `feeding-others`, `hunger-tests`, `taqwa-anchors`, `night-vigil`, `eating-limits`, `birr-definition`, `identity-list`, `servants-of-rahman`, `itikaf-idols`, `hajj-substitute`). This exists so you never have to open `quran.json`. |
| `data/structural/fasting-cooccurrence.json` | Root totals, everything sharing an ayah with `Swm`, the full root inventory of 2:183–187, and translator-divergence scores across the fasting verse set. |
| `data/concepts/Swm-sad-fasting.json` | The `Swm` profile. |
| `data/concepts/{wqy,Sbr,TEm,fdy,rqb,Ekf,rfv,xyT,qdr,hll,$hr,Edd,ysr}.json` | Supporting roots, already built. |

If you need a verse that is not in the versepack, pull it with Read + offset/limit on
`data/arabic/quran.json` or grep the translation JSONs — do not load whole files.

## Output rules specific to this investigation

- **Hard cap: 1,800 words per file.** Cut catalogue, keep depth. Overshoot is the standard failure.
- Open with a **100-word headline-finding block**. The synthesis reads only headlines first.
- Full Arabic + translation panels: **max 4 verses per file**. Everything else is `[surah:ayah]`.
- Mark the line between **data-grounded** (counts, lemma tables, divergence scores) and
  **interpretive** (what it means, theological framing). The reader is going to act on this.
- Do **not** append to `notes/methodology-log.md`. The orchestrator writes one meta-entry.
- End every file with a short section titled **"For the fast"** — what this file changes about how
  someone would actually fast. Two to five concrete lines. This is the point of the investigation.
- Write your file with the Write tool, then `ls` to confirm it exists.

## File map (so you know what your siblings are covering — don't duplicate them)

```
notes/fasting/
  0-structural/  fasting-structurals.md
  1-roots/       concept-Swm.md
                 concept-taqwa-wqy.md
                 concept-Sbr-and-hunger.md
                 concept-kaffara-ladder.md
                 concept-ramadan-qadr-night.md
  1-narratives/  narrative-2-183-187.md
                 narrative-maryam-sawm-silence.md
  2-cross-cutting/ research-how-fasting-builds-taqwa.md
                   research-fasting-negative-space.md
  3-external/    science-fasting-body.md
                 science-fasting-mind.md
                 stories-fasting-experiences.md
  concept-fasting-deep.md   (synthesis)
  practice-guide.md         (the deliverable)
  README.md
```
