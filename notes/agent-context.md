# Agent context — read once, do not repeat in prompts

> Single source of truth for boilerplate that was being repeated in every agent prompt across investigations. Per-agent prompts now reference this file ("read `notes/agent-context.md` first") instead of inlining ~500 words of context per agent. Saves ~30-50k tokens per investigation.

## The project

First-principles study of the Quran: build a root-anchored knowledge graph, treat Arabic text as ground truth, treat translations as a strictly-secondary annotation layer, surface structural patterns invisible to single-pass reading. Working directory: `/Users/fuyofulo/research/quran/`.

Each investigation lives in its own folder under `notes/<topic>/` with subfolders `0-structural/`, `1-roots/`, `1-narratives/` (thematic only), `2-cross-cutting/`, `3-rabbit-holes/` (optional), plus `concept-<topic>-deep.md` synthesis and `README.md` index at the top.

## Data files

| Path | Use when |
|------|----------|
| `data/concepts/<root>.json` | Per-root deterministic profile (lemmas, POS, occurrences, co-roots, distribution). **Always your starting point for a root agent.** |
| `data/morphology/words.jsonl` | 77,429 words with root + lemma + POS. Use ONLY for cross-occurrence work — it's huge; don't load if you just need one root. |
| `data/morphology/{roots.json, lemmas.json, segments.jsonl}` | Roots index, lemmas index, morphology segments. Reference, not bulk. |
| `data/morphology/pos_legend.json` | All 33 QAC POS tags with Arabic names + classical 3-way (ism / fiʿl / ḥarf). |
| `data/arabic/quran.json` | Canonical Uthmani Hafs Arabic, by surah. **Use Read with offset/limit to pull specific ayah ranges, not the whole file.** |
| `data/translations/{saheeh,pickthall,khattab,arberry,word-by-word}.json` | Strictly-secondary English layer. Pull only the translations you need for the verses you're analyzing. |
| `data/structural/translation-divergence.json` | Per-ayah divergence scores. Cite scores; don't re-derive. |
| `data/structural/ayah-echoes.json` | Refrains, near-duplicates, formulas. |
| `data/structural/cluster-bridges.json` | Louvain cluster assignments + bridge edges. |
| `data/structural/root-reference.json` | All 1,642 roots with stats. Quick lookup. |
| `scripts/build_concept.py <root>` | Generates a concept JSON for any root (run as `python3 scripts/build_concept.py <buckwalter-code>`). |

## Buckwalter conventions (case-sensitive — do not lowercase)

`A=ا`, `b=ب`, `t=ت`, `v=ث`, `j=ج`, `H=ح`, `x=خ`, `d=د`, `*=ذ`, `r=ر`, `z=ز`, `s=س`, `$=ش`, `S=ص`, `D=ض`, `T=ط`, `Z=ظ`, `E=ع`, `g=غ`, `f=ف`, `q=ق`, `k=ك`, `l=ل`, `m=م`, `n=ن`, `h=ه`, `w=و`, `y=ي`. Capital letters are emphatic/distinct consonants.

**Critical:** s ≠ S (sīn vs ṣād), d ≠ D, t ≠ T, z ≠ Z, h ≠ H, e is NOT used (E = ʿayn). Filenames may include literal `*` and `$` — pass them literally.

**137 case-collision groups** exist in the Buckwalter encoding (e.g., Zlm/zlm, ESy/Esy). Never use case-insensitive comparison on root names.

## Methodology baseline (patterns that have held across all investigations)

1. **Lemma table first.** Every root analysis surfaces its main insight from the lemma table (frequency-sorted). Look for outlier lemmas (the rare one in a high-count root, dominant morphological pattern, etc.). This has been the decisive move in every Phase-1 root agent.

2. **Translator divergence is a research signal, not noise.** Where translators disagree is where the meaning resists English rendering — high-divergence verses are research-priority. Use `data/structural/translation-divergence.json` for scores.

3. **Surface negative space.** What the Quran does NOT say is as informative as what it does. Across investigations, the cleanest findings have come from absences (no year-as-bridge, no during/middle vocabulary, no mechanism description for teleportation, etc.).

4. **Don't stop at the first interesting finding.** Go one layer deeper at minimum. Cross-confirm against another root or another passage if possible.

5. **Cite [surah:ayah] throughout.** Quote Arabic where decisive — but don't pad with full Arabic + 4 translations for every verse. Inline panels are expensive; reserve them for the load-bearing 3-7 verses.

6. **Distinguish data-grounded from interpretive.** Data-grounded: counts, lemma tables, co-occurrence numbers, divergence scores. Interpretive: cluster names, "this means X," theological framing. Mark the line in your analysis.

## Output rules

- **HARD WORD CAPS.** When the prompt says "1500-2000 words," that means MAX 2000 — truncate findings rather than overshoot. Agents have historically run 2-3x over; this is the single biggest source of waste.
- **Inline Arabic + 4-translation panels: max 5 verses per file.** For other cited verses, just `[surah:ayah]` — readers can look up.
- **No methodology-log entries from per-agent files.** The orchestrator writes ONE meta-entry per investigation. Skip the per-agent log appends.
- **File structure:** headline finding → stats → lemma table (if root) → formulas → semantic field → translation divergence → negative space → verses for direct study → rabbit holes for synthesis to absorb.
- **Required header.** Open every file with a 100-word "Headline finding" block. The synthesis agent reads only headlines first; you make their job possible.
- **Use Write tool to save the file.** The Explore agent type cannot write — confirm your agent type has Write before promising file output.

## Context isolation (load only what's relevant)

- Do **not** read `notes/methodology-log.md` in full. The relevant baseline is in this file. If the orchestrator's per-agent prompt cites a specific entry, read just that entry.
- Cross-investigation references should use the SYNTHESIS files only (`notes/<topic>/concept-<topic>-deep.md`), not per-root or per-narrative files from prior investigations.
- Within the current investigation, read SIBLING file headlines first; drill into specific sections only when needed.
- Don't bleed findings from prior investigations into your analysis unless they're load-bearing for THIS root/narrative. Cite once if needed, move on.

## The 4-phase pipeline (so you know where you fit)

1. **Phase 0** — orchestrator survey. Verify roots, build missing concept profiles. You won't be invoked here.
2. **Phase 1a (root agents)** — one agent per root or root-cluster. You get a concept JSON + sibling references + specific research questions. Output: `notes/<topic>/1-roots/concept-<root>.md`.
3. **Phase 1b (narrative agents, thematic investigations only)** — one agent per Quranic passage cluster. Output: `notes/<topic>/1-narratives/narrative-<topic>.md`.
4. **Structural pre-cuts** (parallel with Phase 1) — co-occurrence + divergence agents. Output: `notes/<topic>/0-structural/...md` + `data/structural/<topic>-...json`.
5. **Phase 2 (cross-cutting)** — synthesizes across Phase 1 files. Output: `notes/<topic>/2-cross-cutting/research-<theme>.md`.
6. **Phase 3 (rabbit holes, optional)** — focused follow-ups on Phase 2 findings. SKIPPED BY DEFAULT — only runs if user requests or finding is too rich for synthesis to absorb.
7. **Phase 4 (synthesis)** — one agent reads all headlines + drills into key files, writes `notes/<topic>/concept-<topic>-deep.md` + folder `README.md`.

## Self-check before returning

- [ ] Output under the word cap (truncate if over)
- [ ] 100-word headline-finding block at the top
- [ ] [surah:ayah] citations throughout
- [ ] Arabic quoted only for the load-bearing 3-7 verses
- [ ] No methodology-log appends from this agent
- [ ] File written to disk (verified with Bash `ls`)
- [ ] No bleed of irrelevant prior-investigation context

## Common pitfalls

- **Buckwalter case-collision.** Never use case-insensitive comparison. Verify Buckwalter against `data/morphology/lemmas.json` if the root looks like it might collide (Zlm/zlm, SbH/sbH, ESy/Esy, etc.).
- **Polysemous roots.** Many roots have multiple distinct senses (nhr = day + river; qrn = generation + horn + companion + pair; mhl = respite + molten metal). Lemma table is the disambiguator.
- **Whole-file reads.** `quran.json` is large; use Read with offset/limit. `words.jsonl` is huge; use grep via Bash if you only need specific roots.
- **Sibling files may not exist yet** if your agent runs before another in the same batch. Don't rely on sibling files unless the orchestrator's prompt explicitly says they exist.
- **Output overshoot is the most common failure.** When in doubt, cut sections, not depth — keep the headline finding sharp and trim the supporting catalogue.

## Model selection (if you're the orchestrator)

- **Haiku**: Phase 0 surveys, structural data builds, methodology log appends, README updates, simple single-occurrence root analyses.
- **Sonnet**: most Phase 1a / 1b agents, Phase 3 rabbit holes, divergence-panel agents.
- **Opus**: Phase 2 cross-cutting (synthesis-style work across multiple files), Phase 4 grand synthesis.

Most work is Sonnet-tier. Reserve Opus for the genuinely cross-cutting passes.
