# Research-pipeline cost optimization plan

> Captures the cost diagnosis from 2026-04-28 and the planned optimizations to apply in the next investigation. The current per-investigation cost is ~3-5M tokens (~30 agent runs × 60-200k tokens each). Target after optimization: ~1.2-1.5M tokens (60-70% reduction) without meaningful quality loss.

## The diagnosis (where the tokens go)

| Phase | Current cost | Driver |
|-------|--------------|--------|
| Phase 0 — survey | ~30-50k | Orchestrator-only, deterministic, low cost |
| Phase 1a — root agents | 500k-1.5M | 6-8 agents × 60-200k each |
| Phase 1b — narrative agents (thematic only) | 400k-1.4M | 5-7 agents × 60-200k each |
| Structural pre-cuts | ~200k | 2 agents producing reusable data |
| Phase 2 — cross-cutting | 400k-1.4M | Each agent re-reads ~10 Phase-1 files |
| Phase 3 — rabbit holes | 300-750k | Often redundant with Phase 1+2 flagged work |
| Phase 4 — synthesis | 300-500k | Reads ALL files in full |
| Orchestrator overhead | 300-500k | Prompts, planning, README, logs |
| **Total** | **~3-5M tokens** | |

## The waste patterns (in order of leverage)

### 1. Output overshoot
Agents treat "~1500-2000 words" as "license to write 3000-7000 words." The synthesis was 9800 words against a 6000-8000 target. **~50% of output tokens are excess.**

### 2. Whole-file reads when a slice is needed
A root agent might need 50 ayahs from `quran.json` (which has 6,236 ayahs) and 2 translations of those ayahs. They Read the whole file. **30-60k wasted tokens per Phase-1 agent.**

### 3. Boilerplate in every prompt
Project context, file paths, Buckwalter rules, methodology rules — repeated in every agent prompt. **30-50k wasted tokens per investigation.**

### 4. Context pollution from prior investigations (USER FLAG — major)
Each new investigation's agents load `methodology-log.md` (now 1882 lines, growing) + cross-reference siblings from prior investigations + general accumulated context. **An agent doing teleportation work doesn't need methodology log Entries 1-4.** Probably **50-150k wasted tokens per investigation** in irrelevant context.

### 5. Cross-confirmation by full-file re-reading
A Phase-2 agent reads 10 Phase-1 files in full when it needs the headlines + one or two sections each. **50-150k wasted tokens per Phase-2 agent.**

### 6. All agents use Opus
Many tasks (Phase 0 surveys, methodology log entries, structural-data scripts, even some root analyses) would run fine on Haiku at ~5-10x lower cost.

### 7. Per-agent methodology log entries duplicate the orchestrator's meta-entry
30+ per-agent entries in the time investigation alone. The orchestrator's META-entry captures the same lessons. **30-50k wasted tokens per investigation.**

### 8. Phase 3 is high-cost but mostly redundant
Rabbit holes are mostly already flagged in Phase 1+2 file conclusions. Phase 3 surfaces SOME new findings but the marginal value per agent is lower than Phase 1+2.

### 9. Synthesis re-reads everything
36 files in full for the time synthesis. Could read summaries first, drill into 5-10 files for specific quotes. **100-200k wasted tokens.**

## The optimization plan (apply on next investigation)

### A. Output budget enforcement — high impact, easy
- Replace "~1500-2000 words" with "**MUST be under 2000 words; truncate findings rather than overshoot**"
- Add explicit "no full Arabic + 4 translations panels for more than 5 verses; cite [surah:ayah] and let the reader look up the data"
- Synthesis explicitly capped at "max 6000 words; one-line summary per concept file is enough"
- **Savings: ~50% of output tokens.**

### B. Slim agent reads — medium effort, high impact
- Per-agent prompts specify which ayah ranges from `quran.json` matter (use Read with offset/limit)
- Per-agent prompts list which translation files matter (often only 2-3 of the 4)
- Don't pass `words.jsonl` unless agent needs to do co-occurrence work
- **Savings: 30-60k tokens per Phase-1 agent (~300-500k total).**

### C. Context isolation — major (USER PRIORITY)
- **DO NOT pass full `methodology-log.md` to per-agent prompts.** Instead pass a 1-page "current methodology summary" extracted at investigation start.
- Each investigation gets its own scratchpad. Don't bleed context from prior investigations into new ones.
- Cross-investigation references use the SYNTHESIS files of prior investigations (not the per-root files) when they're load-bearing for the current work.
- The orchestrator should default to FRESH SESSIONS for new investigations rather than letting context carry forward.
- **Savings: 50-150k tokens per investigation.**

### D. Consolidated boilerplate — easy
- Create `notes/agent-context.md` — single document with project context, file paths, Buckwalter rules, methodology baseline. ~500 words.
- Per-agent prompts reference this once instead of repeating.
- **Savings: 30-50k tokens per investigation.**

### E. Mixed-model usage — easy, big savings on selected work
- **Haiku** for: Phase 0 survey scripts, structural data builds, methodology log appends, README updates, simple per-root analyses (small roots like dhr=2 occurrences)
- **Sonnet** for: most Phase 1 root agents, Phase 1 narrative agents, Phase 3 rabbit holes
- **Opus** for: Phase 2 cross-cutting (synthesis-style work), Phase 4 grand synthesis
- **Savings: 60-80% on the work that doesn't need Opus.**

### F. Skip per-agent methodology entries — trivial
- Agents do NOT append to methodology log
- Orchestrator writes ONE meta-entry per investigation at the end
- **Savings: 30-50k tokens per investigation.**

### G. Default-skip Phase 3 — trivial
- Phase 3 only runs if user specifically requests it OR Phase 2 surfaces a finding too rich for the synthesis to absorb
- Default: rabbit holes carried as OPEN QUESTIONS in synthesis
- **Savings: 300-750k tokens per investigation.**

### H. Synthesis reads summaries first — medium effort
- Each Phase-1 + Phase-2 file MUST have a 100-word "headline finding" block at the top
- Synthesis reads only the headline blocks first, then drills into 5-10 specific files for quotes
- **Savings: 100-200k tokens on synthesis pass.**

### I. Smaller batch sizes — orchestrator hygiene
- 3-4 agents per parallel batch (not 6-8)
- Reduces limit-thrashing and orchestrator overhead from retry-management
- Doesn't reduce TOTAL tokens but reduces wasted orchestrator turns

## Combined estimate

| Optimization | Token savings per investigation |
|--------------|---------------------------------|
| A. Output budget enforcement | ~800k-1.5M |
| B. Slim agent reads | ~300k-500k |
| C. Context isolation | ~50k-150k |
| D. Consolidated boilerplate | ~30k-50k |
| E. Mixed-model usage | savings depend on $ rate; possibly ~60% cost on selected agents |
| F. No per-agent methodology entries | ~30k-50k |
| G. Default-skip Phase 3 | ~300k-750k |
| H. Synthesis reads summaries | ~100k-200k |
| **Total** | **~1.6M-3.2M tokens saved per investigation** |

Result: per-investigation cost drops from ~3-5M tokens to ~1.2-1.8M tokens. **60-70% reduction.**

## What to do NEXT investigation as a test

1. Build the `notes/agent-context.md` consolidated doc first (one-time work, reusable)
2. Apply ALL of A, B, C, D, F, G, H from the start
3. Use mixed-model (E) — start with Haiku/Sonnet for Phase 0 + Phase 1 root agents on small roots; Opus only where genuinely needed
4. Compare token usage to the time/teleportation baseline
5. Check whether quality holds (cross-confirmation rate, headline-finding count, synthesis readability)

If quality holds at 1/3 the cost, the new pipeline is the new baseline.

## Open questions

- Can we BATCH-launch via a single agent that orchestrates sub-tasks, instead of N parallel root agents from the orchestrator? May reduce orchestrator overhead.
- Is there a way to share KV-cache across agents on the same data files? (Probably not at the API level, but worth checking.)
- Should the structural pre-cuts be PRE-BUILT once for the project rather than rebuilt per investigation? The cooccurrence + divergence patterns might generalize to ANY topic given a root list.
