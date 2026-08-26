# Life beyond earth — shared brief

> Read `notes/agent-context.md` FIRST, then this. Do NOT read `notes/methodology-log.md`.
> Do NOT read other investigations' per-root files.

## Why this investigation exists

The commissioner asks: *"Does the Quran talk about life outside of human, outside of earth? Are
there humans elsewhere in the universe, or is it just on earth?"* He adds that he once heard a
scholar say **there are seven or eight earth-like planets where humans reside**, could not place the
source, and wants it checked properly because "it's not something that is plainly written in the
Quran, so it needs some research."

So there are two deliverables: **what the Quran actually says about life beyond the earth**, and
**an honest verdict on the specific claim he was told.**

**Tone.** A believer checking something he half-remembers. Be direct. Do not flatter the claim and
do not sneer at it. If the text supports it, say so; if it is an extrapolation, say exactly which
verse it is extrapolated from and what the verse does and does not state. Mark interpretation.

**Hard rule.** This project reads the Quranic text directly and treats **hadith, tafsīr, and modern
"scientific miracle" literature as outside its evidence base.** That matters more here than anywhere
else in the project, because almost all popular claims of this kind come from exactly those sources.
Where you reference them, label them as outside the evidence base — never as evidence.

## Phase 0 findings — verified, do not re-derive

### 1. The pronoun audit — the single most important finding

The Quran has **four parallel "God scattered creatures" verses** using the verb `baththa` and the
noun `dābba`. I checked the pronoun in each against the morphology segments:

| Ref | Clause | Pronoun | Refers to |
|---|---|---|---|
| **42:29** | `wa-mā **baththa fīhimā** min dābba` | **`3D` — DUAL** | **the heavens AND the earth** |
| 31:10 | `wa-**baththa fīhā** min kulli dābba` | `3FS` — singular | the earth |
| 2:164 | `wa-**baththa fīhā** min kulli dābba` | `3FS` — singular | the earth |
| 45:4 | `wa-mā **yabuththu** min dābba` | (no locative pronoun) | unspecified |

**42:29 is the only verse in the Quran that places moving creatures in the heavens using a dual
pronoun.** Full verse: *"And among His signs is the creation of the heavens and the earth, and what
He has scattered throughout them both of creatures — and He is able to gather them whenever He
wills."* Note the final clause: `wa-huwa ʿalā jamʿihim idhā yashāʾu qadīr` — a **gathering** of those
creatures. This is the load-bearing verse of the whole investigation.

### 2. `dābba` is the being-word most attached to the heavens

Share of each being-root's ayahs that also contain `samāwāt` (the plural heavens):

| Root | Sense | With heavens / total | Share |
|---|---|---|---|
| **`dbb`** | **moving creature** | **7 / 18** | **38.9%** |
| `mlk` | angel | 41 / 191 | 21.5% |
| `nws` | people | 20 / 225 | 8.9% |
| `b$r` | human being | 9 / 119 | 7.6% |
| `jnn` | jinn | 8 / 196 | 4.1% |
| **`Ans`** | **human / insān** | **2 / 93** | **2.1%** |

**The creature-word is twice as heaven-attached as angels and eighteen times more than the
human-word.** Whatever the Quran puts in the heavens, it is not described with the vocabulary it
uses for human beings.

### 3. 65:12 is almost certainly the source of the claim he heard

`Allāhu alladhī khalaqa sabʿa samāwātin **wa-mina al-arḍi mithlahunna** yatanazzalu al-amru
**baynahunna**` — *"God is He who created seven heavens, and of the earth the like of them. The
command descends between them."*

Verified from the morphology: `mithlahunna` carries `3FP` (feminine plural) and `baynahunna` carries
`3FP` — both refer back to the seven heavens. So the verse says *of the earth, the like of them [in
number]*. **It does not contain the word "seven" a second time, does not say "planets," and says
nothing whatsoever about inhabitants.** Any claim about people living on seven earths is built on
top of this verse, not stated in it. Establish that precisely and fairly.

## Data files — use these, do NOT open whole corpus files

| Path | What |
|---|---|
| `data/structural/cosmos-versepack.json` | **Start here.** 157 verses, Arabic + 4 translations, grouped: `dabba-dispersal`, `dabba-all`, `seven-heavens`, `jinn-and-mankind`, `angels`, `universal-worship`, `cosmogony`, `passing-beyond`, `the-worlds`, `communities`, `life-and-water`, `gathering`. |
| `data/structural/cosmos-cooccurrence.json` | The pronoun audit, the being-vs-heavens table, human/heaven shared ayahs, `samāwāt` neighbours, divergence scores. |
| `data/concepts/<root>.json` | Per-root profiles; build any you need with `python3 scripts/build_concept.py <root>` (it now auto-disambiguates case-colliding roots). |

## Traps

- **`jnn` is polysemous and mostly NOT jinn.** 201 occurrences but `janna` (garden) is 147. The jinn
  senses are `jinn` (22), `jinna` (10), `jānn` (7). Use the lemma table.
- **`smw` includes `ism` (name), 39 occurrences.** Filter to `samāʾ`/`samāwāt`.
- **`rwH` gives both `rīḥ` (wind, 29) and `rūḥ` (spirit, 21).** Different senses, one root.
- **`Ealamin` ("worlds") is from `Elm`**, not a separate root, and sits inside an 854-occurrence root.
- Highest-divergence verses in this set: 51:47, 67:3, 55:33, 42:29, 45:4, 41:12.

## Output rules

- **Cap: 2,000 words per file** unless your prompt says otherwise. 100-word headline block on top.
- Max 5 Arabic panels. Cite `[surah:ayah]` for everything else.
- **Mark data-grounded vs interpretive.** This will be acted on.
- End each file with **"What this settles"** — 3–5 lines stating plainly what a reader can and cannot
  conclude from your material. Blunt. No hedging padding.
- Write with the Write tool (or a Bash heredoc), then `ls` to confirm.

## File map

```
notes/cosmos/
  0-structural/  cosmos-structurals.md            (orchestrator)
  1-roots/       concept-dbb-dabba.md
                 concept-smw-seven-heavens.md
                 concept-human-words-and-origin.md
                 concept-jinn-angels-other-beings.md
  1-narratives/  narrative-65-12-seven-earths-claim.md
                 narrative-55-33-passing-beyond.md
  2-cross-cutting/ research-is-there-life-beyond-earth.md
                   research-cosmology-negative-space.md
  concept-cosmos-deep.md
  README.md
```
