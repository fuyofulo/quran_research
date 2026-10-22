# Istighfār: how the Quran teaches seeking forgiveness

**The answer in one sentence.** The Quran teaches istighfār as a request spoken directly to God ("my
Lord, forgive me", "our Lord, forgive us"), made at once after a wrong and also without waiting for
one, by a person who is not knowingly persisting, and followed by turning back (tawba) and setting
right; it fixes no number, no commanded hour and no required feeling.

## Where to start

- **To practise it:** [`practice-guide.md`](practice-guide.md). Plain language, twelve of the Quran's
  own prayers with Arabic, sound and meaning, and a suggested daily routine.
- **To see the method and how it was tested:**
  [`2-cross-cutting/research-how-the-quran-teaches-istighfar.md`](2-cross-cutting/research-how-the-quran-teaches-istighfar.md),
  the spine.
- **For the full picture with every count:** [`concept-istighfar-deep.md`](concept-istighfar-deep.md),
  the synthesis.

## File map

| File | What it holds |
|---|---|
| [`BRIEF.md`](BRIEF.md) | Shared brief for all agents: the question, Phase-0 facts, traps, data files |
| [`0-structural/istighfar-structurals.md`](0-structural/istighfar-structurals.md) | Phase 0: lemma table, imperative audit, petition list, root lift, divine-name counts (with CORRECTED passages) |
| [`1-roots/concept-gfr-root-and-names.md`](1-roots/concept-gfr-root-and-names.md) | Form X vs form I, the three `astaghfiru`, human forgiving, divine-name pairings (found the 56→71 undercount) |
| [`1-roots/concept-the-petitions.md`](1-roots/concept-the-petitions.md) | The 22 quoted petitions in one table: address, ground, request, voice, closing name |
| [`1-narratives/narrative-prophets-seeking-forgiveness.md`](1-narratives/narrative-prophets-seeking-forgiveness.md) | Adam to the Prophet: occasion, speed, accompaniments, whether a grant is recorded |
| [`1-narratives/narrative-commanded-and-its-fruits.md`](1-narratives/narrative-commanded-and-its-fruits.md) | The plural commands, istighfār vs tawba, the fruits, the practitioners (3:135), the times, the refusals |
| [`1-narratives/narrative-for-others-and-forgiving-others.md`](1-narratives/narrative-for-others-and-forgiving-others.md) | Seeking for kin and believers, where it is barred or void, people forgiving people |
| [`2-cross-cutting/research-how-the-quran-teaches-istighfar.md`](2-cross-cutting/research-how-the-quran-teaches-istighfar.md) | **Spine.** Two stress tests and the method: whom, what, voice, when, with what, for whom, what follows, what blocks |
| [`2-cross-cutting/research-istighfar-negative-space.md`](2-cross-cutting/research-istighfar-negative-space.md) | What the text does not say: formula, ḥiṭṭa, counts, times, fiqh conditions, tears, intermediaries, "too big" |
| [`concept-istighfar-deep.md`](concept-istighfar-deep.md) | Phase-4 synthesis (≈3,800 words) |
| [`practice-guide.md`](practice-guide.md) | Plain-language practice guide (≈3,000 words) |

**Data and scripts:** `data/structural/istighfar-census.json` (lemmas, verb forms, petition table,
pairings), `data/structural/istighfar-versepack.json` (195 verses, 11 groups), both built by
`scripts/build_istighfar_census.py` and `scripts/build_istighfar_versepack.py`.

## Corrections log

- **Order of the glorify-with-praise / istighfār pairing (found 2026-10-22 by the gratitude investigation):** the pairing occurs 4×, but praise comes first in only 3 — at 40:55 istighfār comes first. Corrected in the synthesis.

Every claim the investigation corrected in itself. Where files disagree, the later file wins.

| # | Claim | Corrected to | Found in |
|---|---|---|---|
| 1 | `ghafūr raḥīm` in 56 ayahs | **71** (15 `kāna ghafūran raḥīman` missed); also `tawwāb raḥīm` 7→9 and `ʿafuww ghafūr` 3→4 | names file |
| 1a | *Cause:* a data bug | `quran.json` writes open-fathatan tanwīn with a space before the final alif (2,054 tokens, 1,533 ayahs), so exact-string formula searches miss them. Fixed in both census scripts, and the fix was added to `notes/agent-context.md` | names file → Phase 0 |
| 2 | Mercy asked in 10 petitions | **7** (28:16 is the narrator's names, 40:7 the ground, 59:10 the closing name) | petitions file |
| 3 | `Zlm` confession in 3 petitions | **2** (7:23, 28:16); at 71:28 the `ẓālimīn` are others | petitions file |
| 4 | "22 petitions" | **17 `ighfir` requests**; the other 5 are conditional (7:23, 11:47, 5:118), a noun (2:285) or a hope (26:82) | petitions file |
| 5 | 3:147 spoken by prophets | spoken by the `ribbiyyūn`, believers who fought with prophets | petitions file |
| 6 | "Istighfār closes worship and success" | **narrowed:** true of position (5 of 6 timed), not of reason; each ending names a lack, and the success cases name a `dhanb`. What holds: *istighfār does not wait for a known wrong* | prophets, commands files; Phase 0 |
| 7 | 40:55 times the istighfār | its *evening and morning* attach to `sabbiḥ` | commands file |
| 8 | All six commands to non-believers carry worldly promises | **3** (11:3, 11:52, 71:10–12); 11:61 and 11:90 close on names, 41:6 on a woe | both Phase-2 files |
| 9 | 16 prophetic units, 8 unoccasioned | **15 and 7**: 48:1–2 is a grant, not an act of seeking | spine |
| 10 | Tawba's fruits hedged, istighfār's flat | not a real contrast: hedges are rare in both (4 of 60, 1 of 37) | spine |
| 11 | No istighfār verse carries a third act | holds for `aṣlaḥa` and `ʿamila ṣāliḥan`, but 41:6 joins `istaqīmū` to it | spine |
| 12 | `Ghafūr`/`Tawwāb` never close a human petition | true only of forgiveness petitions; see 2:128 and 14:36 | spine |
| 13 | Nobody seeks for others without himself | true of petitions; false for the Prophet's commanded istighfār (3:159, 24:62, 60:12) and the promises | spine |
| 14 | The ḥiṭṭa is *the* prescribed formula | the only one given to a community; 23:118 is a second, to the Prophet | negative space |
| 15 | 28:17 is the only behavioural vow | only among prophets; the magicians' vow (20:72) is another | negative space |
| 16 | (tahajjud synthesis) pre-dawn istighfār is the only devotion pinned to an hour | true only outside ṣalāt, which has named hours (24:58, 17:78) | negative space |
| 17 | "Many prophets seek forgiveness for others" | they *ask God* in the imperative; `astaghfiru` appears only in promises | for-others file |
| 18 | 7:23 is Adam's | a dual: Adam and his wife | prophets file |
| 19 | 23:118 is five words | **six**, tying 28:16 and 26:86; 2:285's `ghufrānaka rabbanā` (two words) is shorter | synthesis |
| 20 | `tāba ʿalā` in 16 / 19 verses | **22**, God always the subject (adds 9:15, 9:27, 33:73); `tāba ilā` 12 confirmed | synthesis |

## Not yet done

No divergence-panel pass was run on the highest-divergence verses (3:17, 51:18, 8:33). The synthesis's
Open questions list what the text leaves unreconciled, including 4:48 beside 39:53 and 25:68–70.
