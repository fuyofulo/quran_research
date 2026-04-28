# Cognition co-occurrence graphs

> Interactive force-directed graph of root co-occurrence at the ayah level. Built by `scripts/build_graph.py`. Open the `index.html` files in any browser — no setup required.

## How to view

```bash
open /Users/fuyofulo/research/quran/notes/cognition/graph/index.html
open /Users/fuyofulo/research/quran/notes/cognition/graph-plus/index.html
```

(or just double-click in Finder)

## How to read the graph

- **Each node is a root.** Size scales with Quran-wide occurrence count (log scale).
- **Each edge is "appears together in N ayahs."** Edge thickness scales with co-occurrence count.
- **Color = detected community.** Detection uses greedy modularity on cosine-normalized weights (so high-frequency roots like Elm don't dominate).
- **Drag nodes** to reposition. **Hover** to see counts and top 5 co-occurring roots.
- Use the controls to filter weak edges, toggle labels, adjust layout strength.

## What we have

### `graph/` — cognition only (14 roots, 60 edges, 2 clusters)

The 14 cognitive roots from the original investigation. Two natural communities emerged from the data:

**Cluster 1 — the "process / reflection" community (11 roots):**
ذكر, بصر, نظر, سأل, وجد, قرأ, عقل, دبر, فقه, فكر, لبب
*(remember, sight, observe, ask, find, read, reason, ponder, comprehend, reflect, kernel-of-heart)*

These are operational verbs and the faculty (lubb). They're the "doing" cognitive vocabulary.

**Cluster 2 — the "authority / transgression" community (3 roots):**
علم, حكم, بغي
*(knowledge, wisdom/judgment, seek/transgress)*

These three cluster together because:
- علم + حكم is the al-ʿAlīm al-Ḥakīm divine-attribute pairing (71 ayahs together — by far the strongest edge in the entire graph)
- بغي (seek/transgress) appears in many of the same contexts — knowing/judging vs overreaching

The split is meaningful: **the Quran separates cognitive operations (Cluster 1) from cognitive AUTHORITY (Cluster 2).** Knowledge and judgment are divine attributes; reflection and observation are human acts.

### `graph-plus/` — cognition + 30 neighbors (44 roots, 901 edges, 3 clusters)

Adds the 30 most co-occurring non-cognitive roots (those appearing in many of the same ayahs as the cognitive seeds). This graph **reveals what was missed** from the original 14.

**Cluster 1 — the OBSERVATION / COSMOLOGY community (7 roots):**
نظر + شيا (will), أرض (earth), سماء (heaven), كل (every), رأي (see/think), موت (death)

The "look at the signs in heaven and earth" cluster. Only `nZr` from the original 14 lives here — it's the observational verb. **`rAy` (see/think) is a major root I missed in the original 14** — it appears 328 times and clusters tightly with observation. Worth adding as a 15th cognitive root.

**Cluster 2 — the CORE COGNITION community (19 roots, 11 cognitive seeds):**
علم, ذكر, حكم, بصر, سأل, قرأ, عقل, دبر, فقه, فكر, لبب + بين (clarify), آية (sign), جعل, نزل (send-down), سمع (hear), **قلب (heart)**, كثر, خلف

**Two huge confirmations and a missed root surface here:**
- ✅ **The heart-locus thesis is confirmed by the graph itself.** `qlb` (heart) clusters with the cognitive roots — independent structural validation of the agent investigation finding that real cognition is heart-located, not head-located.
- ✅ **`smE` (hear) joins cognition** — confirms the 17:36 accountability triad (hearing + sight + heart).
- ❌ **`byn` (clarify, 523×) was missed from the original 14.** It appears in 11 of 14 cognitive contexts and means "to make clear / disclose." This is the divine cognitive act of revealing meaning. Should be added.

**Cluster 3 — the DIVINE / PROPHETIC community (18 roots, 2 cognitive seeds):**
وجد, بغي + الله, قول, كون, ربب, امن (faith), قوم (people), اتي, كفر (disbelieve), رسل (messenger), عذب (punish), هدي (guide), حقق (truth), وقي (taqwa), عند, جنن, تبع (follow)

The theological/prophetic discourse cluster. `wjd` (encounter) and `bgy` (seek/transgress) live here because their dominant use is in divine encounter / prophetic narrative, not cognitive process. The graph shows them as semantically more "encounter with God" than "cognitive operation" — a useful re-classification.

## What the graph reveals about my original selection

The graph is partly a fairness audit on the original 14:

**Validations (cognitive analysis was on the right track):**
- The qlb-cognition cluster confirms heart-locus
- The smE-cognition cluster confirms the sensorium
- The Elm-Hkm pairing dominates as expected
- The nZr-cosmology cluster confirms "look at the signs"

**Misses (roots that should be in a v2 cognitive constellation):**
- **`byn` (بين, clarify, 523×)** — divine act of disclosure; appears in 11 of 14 cognitive contexts. Genuinely missing from the original 14.
- **`rAy` (راي, see/think, 328×)** — third "seeing" root after bSr and nZr; Arabic also uses it for "to think/opine" (`raʾyī` = "my view"). Missing.
- **`smE` (سمع, hear, 185×)** — included in the heart-locus investigation but not as a primary cognitive root in the constellation.

**Re-classifications (roots that may not be primarily cognitive):**
- `wjd` (find/encounter) and `bgy` (seek/transgress) cluster more with divine/prophetic discourse than with cognitive operation. They're cognitive *adjacent* but their center of gravity is elsewhere.

## Files

- `data.json` — raw graph data (nodes, edges, clusters)
- `index.html` — self-contained interactive D3.js visualization

## Reproducing

```bash
python3 scripts/build_graph.py cognition          # 14-root graph
python3 scripts/build_graph.py cognition-plus     # 14 + 30 neighbors
```

## Suggested follow-up investigations (from what the graph reveals)

1. **Re-do the cognitive constellation as v2** with `byn` and `rAy` added (and possibly `smE` promoted from sensorium-helper to primary). 16 roots instead of 14.
2. **Spawn a dedicated parallel agent on `byn`** — it's likely the missing-link "clarification" verb that sits between divine knowledge and human comprehension.
3. **Spawn a dedicated parallel agent on `rAy`** — the third seeing root, with the additional sense "to think/opine" that bSr and nZr lack.
4. **Use the graph as the SELECTION method for future investigations.** Pick a seed root or seed concept; let the graph (broader, e.g., 100-root) suggest membership; then deep-read the cluster.
