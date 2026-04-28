"""Build a semantic co-occurrence graph from QAC data.

Generic — takes a set of roots and produces an interactive HTML visualization
plus the underlying JSON.

Each ROOT is a node. Each EDGE is "appears together in N ayahs." Communities
detected via label-propagation (no external dependencies).

Usage:
    python3 scripts/build_graph.py cognition           # 14 cognitive roots only
    python3 scripts/build_graph.py cognition-plus      # cognitive roots + neighbors
    python3 scripts/build_graph.py custom <out_dir> <root1> <root2> ...
"""

import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDS = ROOT / "data" / "morphology" / "words.jsonl"

# The 14 cognitive roots from the cognition investigation
COG14 = [
    "Elm", "*kr", "Hkm", "bSr", "nZr", "sAl", "wjd", "bgy",
    "qrA", "Eql", "dbr", "fqh", "fkr", "lbb",
]
# bHv (1-occurrence outlier) excluded by default; can be added by user

# English glosses for top cognitive roots (used in node labels)
GLOSS = {
    "Elm": "knowledge",
    "*kr": "remember",
    "Hkm": "wisdom/judge",
    "bSr": "sight/insight",
    "nZr": "observe",
    "sAl": "ask",
    "wjd": "find/encounter",
    "bgy": "seek/transgress",
    "qrA": "read/recite",
    "Eql": "reason",
    "dbr": "ponder",
    "fqh": "comprehend",
    "fkr": "reflect",
    "lbb": "kernel-of-heart",
    "bHv": "scratch/research",
    # common neighbors (added by build_neighbors)
    "Alh": "Allah/divinity",
    "rbb": "Lord",
    "Ayy": "sign",
    "qwm": "people",
    "qwl": "speech",
    "kwn": "be",
    "Amn": "faith",
    "kfr": "disbelieve",
    "byn": "clarify",
    "ArD": "earth",
    "smw": "heaven",
    "rsl": "messenger",
    "ktb": "book/write",
    "qlb": "heart",
    "nzl": "send-down",
    "Aty": "give/come",
    "$yA": "thing/will",
    "rAy": "see/think",
    "smE": "hear",
    "Hyy": "life",
    "mwt": "death",
    "Ezz": "might",
    "gfr": "forgive",
}


def load_corpus():
    """Return: (ayah_roots, root_count, root_arabic)."""
    ayah_roots = defaultdict(set)
    root_count = Counter()
    root_arabic = {}
    with WORDS.open() as f:
        for line in f:
            w = json.loads(line)
            r = w.get("root")
            if not r:
                continue
            root_count[r] += 1
            root_arabic[r] = w["root_arabic"]
            ayah_roots[(w["surah"], w["ayah"])].add(r)
    return ayah_roots, root_count, root_arabic


def build_cooccurrence(roots_to_include, ayah_roots):
    """Build co-occurrence edges for the given root set."""
    edges = defaultdict(int)
    selected = set(roots_to_include)
    for ay, roots in ayah_roots.items():
        present = sorted(roots & selected)
        for a, b in combinations(present, 2):
            edges[(a, b)] += 1
    return dict(edges)


def find_neighbors(target_roots, ayah_roots, root_count, min_freq=30, min_cog_links=3):
    """Find non-target roots that co-occur with multiple target roots.

    These are candidate roots that *might* belong in the cognitive constellation
    but were excluded from the original 14."""
    target = set(target_roots)
    # For each non-target root, count how many target roots it co-occurs with
    # AND how many ayahs they share total
    co_with_targets = defaultdict(set)  # other_root -> set of target roots it shares an ayah with
    co_count = defaultdict(int)  # other_root -> total ayahs shared with any target
    for ay, roots in ayah_roots.items():
        targets_in_ayah = roots & target
        if not targets_in_ayah:
            continue
        for r in roots:
            if r in target:
                continue
            co_with_targets[r] |= targets_in_ayah
            co_count[r] += 1

    candidates = []
    for r, targets_shared in co_with_targets.items():
        if root_count[r] >= min_freq and len(targets_shared) >= min_cog_links:
            candidates.append({
                "root": r,
                "count": root_count[r],
                "cog_links": len(targets_shared),
                "co_count": co_count[r],
            })
    candidates.sort(key=lambda x: (-x["cog_links"], -x["co_count"]))
    return candidates


def detect_communities(nodes, edges, root_count):
    """Greedy modularity-based clustering. O(n^3) — only for small graphs (≤50).

    For dense small graphs (14-50 nodes), label propagation collapses to one
    label. Modularity finds sub-structure by maximizing the gap between
    actual and expected co-occurrence inside each community.

    We normalize edge weights by sqrt(count_a * count_b) — cosine-similarity-style
    adjustment that prevents very high-frequency roots (like Elm at 854) from
    dominating the modularity calculation.
    """
    if not edges:
        return {n: i for i, n in enumerate(nodes)}

    # Normalized edges (cosine-like)
    norm_edges = {}
    for (a, b), w in edges.items():
        ca = root_count.get(a, 1)
        cb = root_count.get(b, 1)
        norm_edges[(a, b)] = w / (ca * cb) ** 0.5

    adj = defaultdict(dict)
    for (a, b), w in norm_edges.items():
        adj[a][b] = w
        adj[b][a] = w

    m2 = sum(norm_edges.values()) * 2
    if m2 == 0:
        return {n: i for i, n in enumerate(nodes)}

    degree = {n: sum(adj[n].values()) for n in nodes}

    def modularity(community):
        Q = 0.0
        for n in nodes:
            for nb in adj[n]:
                if community[n] == community[nb]:
                    Q += adj[n][nb] - (degree[n] * degree[nb]) / m2
        return Q / m2

    community = {n: i for i, n in enumerate(nodes)}

    while True:
        best_gain = 1e-9
        best_pair = None
        comms = sorted(set(community.values()))
        current_q = modularity(community)
        for i, c1 in enumerate(comms):
            for c2 in comms[i + 1:]:
                trial = {n: (c2 if community[n] == c1 else community[n]) for n in nodes}
                gain = modularity(trial) - current_q
                if gain > best_gain:
                    best_gain = gain
                    best_pair = (c1, c2)
        if not best_pair:
            break
        c1, c2 = best_pair
        for n in nodes:
            if community[n] == c1:
                community[n] = c2

    seen = {}
    for n in sorted(nodes):
        c = community[n]
        if c not in seen:
            seen[c] = len(seen)
        community[n] = seen[c]
    return community


def louvain(nodes_list, edges, root_count):
    """Louvain Phase 1: weighted modularity-based community detection.

    O(m * iterations) — scales to thousands of nodes. The standard algorithm
    used for large graph clustering.

    Same cosine-style normalization as detect_communities, so high-frequency
    roots don't dominate.
    """
    if not edges:
        return {n: i for i, n in enumerate(nodes_list)}

    # Normalize weights (cosine similarity style)
    norm_edges = {}
    for (a, b), w in edges.items():
        ca = root_count.get(a, 1)
        cb = root_count.get(b, 1)
        norm_edges[(a, b)] = w / (ca * cb) ** 0.5

    # Build adjacency
    adj = defaultdict(dict)
    for (a, b), w in norm_edges.items():
        adj[a][b] = w
        adj[b][a] = w

    # Degrees
    deg = {n: sum(adj[n].values()) for n in nodes_list}

    # 2m (sum of all degrees = 2x sum of edge weights)
    twom = sum(deg.values())
    if twom == 0:
        return {n: i for i, n in enumerate(nodes_list)}

    # Initial: each node in own community
    community = {n: i for i, n in enumerate(nodes_list)}

    # Total degree per community (sigma_tot)
    sigma_tot = {i: deg[nodes_list[i]] for i in range(len(nodes_list))}

    # Phase 1: local moving
    iteration = 0
    while True:
        iteration += 1
        moved = 0
        for node in nodes_list:
            curr_c = community[node]
            ki = deg[node]

            # Weighted links from node to each community
            comm_w = defaultdict(float)
            for nb, w in adj[node].items():
                if nb != node:
                    comm_w[community[nb]] += w

            # Tentatively remove node from its current community
            sigma_tot[curr_c] = sigma_tot.get(curr_c, 0) - ki

            # Find best community to move to
            best_c = curr_c
            best_gain = 0.0

            for c, w_to_c in comm_w.items():
                # Modularity gain (formula: Δ ∝ w_to_c - ki * sigma_tot[c] / 2m)
                gain = w_to_c - ki * sigma_tot.get(c, 0) / twom
                if gain > best_gain:
                    best_gain = gain
                    best_c = c

            # Apply move (or restore if best is current)
            sigma_tot[best_c] = sigma_tot.get(best_c, 0) + ki
            community[node] = best_c
            if best_c != curr_c:
                moved += 1

        if moved == 0 or iteration >= 30:
            break

    # Renumber compactly
    seen = {}
    for n in nodes_list:
        c = community[n]
        if c not in seen:
            seen[c] = len(seen)
        community[n] = seen[c]
    return community


def build_graph_data(roots, ayah_roots, root_count, root_arabic, use_louvain=False):
    edges = build_cooccurrence(roots, ayah_roots)
    nodes_with_edges = set()
    for a, b in edges:
        nodes_with_edges.add(a)
        nodes_with_edges.add(b)
    # Include all requested roots, even orphans
    all_nodes = sorted(set(roots) | nodes_with_edges)
    if use_louvain or len(all_nodes) > 60:
        clusters = louvain(all_nodes, edges, root_count)
    else:
        clusters = detect_communities(all_nodes, edges, root_count)
    return {
        "nodes": [
            {
                "id": r,
                "arabic": root_arabic.get(r, "?"),
                "english": GLOSS.get(r, ""),
                "count": root_count.get(r, 0),
                "cluster": clusters[r],
            }
            for r in all_nodes
        ],
        "edges": [
            {"source": a, "target": b, "weight": w}
            for (a, b), w in sorted(edges.items(), key=lambda kv: -kv[1])
        ],
        "n_clusters": len(set(clusters.values())),
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>__TITLE__</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
    margin: 0; padding: 0;
    background: #fafaf7;
    color: #222;
  }
  .header {
    padding: 16px 24px;
    background: white;
    border-bottom: 1px solid #e5e5e0;
  }
  .header h1 { margin: 0 0 4px 0; font-size: 18px; font-weight: 600; }
  .header p { margin: 0; font-size: 13px; color: #666; }
  .controls {
    padding: 12px 24px;
    background: #fff;
    border-bottom: 1px solid #e5e5e0;
    font-size: 13px;
    display: flex;
    gap: 24px;
    align-items: center;
    flex-wrap: wrap;
  }
  .controls label { display: flex; gap: 8px; align-items: center; }
  #graph { width: 100vw; height: calc(100vh - 110px); }
  .node text {
    font-family: "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", "Amiri", system-ui, serif;
    font-size: 16px;
    pointer-events: none;
    text-anchor: middle;
    dominant-baseline: middle;
  }
  .node .gloss {
    font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
    font-size: 9px;
    fill: #333;
    text-anchor: middle;
  }
  .link { stroke-opacity: 0.4; }
  .link:hover { stroke-opacity: 1; }
  .tooltip {
    position: absolute;
    background: rgba(20,20,20,0.95);
    color: white;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 12px;
    pointer-events: none;
    line-height: 1.5;
    max-width: 260px;
    z-index: 1000;
  }
  .tooltip .arabic {
    font-family: "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", "Amiri", serif;
    font-size: 18px;
  }
  .legend {
    position: absolute;
    top: 130px;
    right: 24px;
    background: rgba(255,255,255,0.95);
    border: 1px solid #e5e5e0;
    padding: 10px 14px;
    border-radius: 4px;
    font-size: 12px;
    z-index: 100;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 3px 0;
  }
  .legend-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
</style>
</head>
<body>
<div class="header">
  <h1>__TITLE__</h1>
  <p>__SUBTITLE__</p>
</div>
<div class="controls">
  <label>Edge weight threshold:
    <input type="range" id="edgeThreshold" min="1" max="50" value="1" />
    <span id="edgeThresholdVal">1</span>
  </label>
  <label>Show labels:
    <input type="checkbox" id="showLabels" checked />
  </label>
  <label>Charge strength:
    <input type="range" id="chargeStrength" min="-1500" max="-50" value="-400" />
  </label>
  <button id="resetZoom">Reset view</button>
</div>
<div id="graph"></div>
<div id="legend" class="legend"></div>

<script>
const data = __DATA__;

const width = window.innerWidth;
const height = window.innerHeight - 110;

// Color scale for clusters
const clusterColors = [
  "#4a90e2", "#e74c3c", "#27ae60", "#f39c12", "#8e44ad",
  "#16a085", "#d35400", "#7f8c8d", "#c0392b", "#2c3e50",
];
function color(cluster) { return clusterColors[cluster % clusterColors.length]; }

// Node radius from count (log scale)
function radius(count) {
  return 6 + Math.log(Math.max(count, 1)) * 4;
}

const svg = d3.select("#graph").append("svg")
  .attr("width", width).attr("height", height);

const g = svg.append("g");

// Zoom
const zoom = d3.zoom().scaleExtent([0.2, 4]).on("zoom", (e) => g.attr("transform", e.transform));
svg.call(zoom);
d3.select("#resetZoom").on("click", () => svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity));

// Tooltip
const tooltip = d3.select("body").append("div").attr("class", "tooltip").style("display", "none");

const link = g.append("g").attr("stroke", "#666").selectAll("line").data(data.edges).join("line")
  .attr("class", "link")
  .attr("stroke-width", d => Math.sqrt(d.weight) * 0.7);

const node = g.append("g").selectAll("g").data(data.nodes).join("g").attr("class", "node");

node.append("circle")
  .attr("r", d => radius(d.count))
  .attr("fill", d => color(d.cluster))
  .attr("stroke", "white").attr("stroke-width", 1.5)
  .on("mouseover", (e, d) => {
    const adj = data.edges.filter(x => x.source.id === d.id || x.target.id === d.id || x.source === d.id || x.target === d.id);
    const top = adj.map(e => {
      const other = (e.source.id === d.id || e.source === d.id) ? (e.target.id || e.target) : (e.source.id || e.source);
      return {root: other, weight: e.weight};
    }).sort((a,b) => b.weight - a.weight).slice(0, 5);
    const arabicMap = Object.fromEntries(data.nodes.map(n => [n.id, n.arabic]));
    const html = `
      <div class="arabic">${d.arabic}</div>
      <b>${d.id}</b> ${d.english ? "— " + d.english : ""}<br>
      Quran-wide occurrences: ${d.count}<br>
      Cluster: ${d.cluster + 1}<br>
      <hr style="border-color: #555; margin: 6px 0;">
      <b>Top co-occurring (in this graph):</b><br>
      ${top.map(t => `${arabicMap[t.root]} (${t.root}): ${t.weight} ayahs`).join("<br>")}
    `;
    tooltip.style("display", "block").html(html);
  })
  .on("mousemove", (e) => tooltip.style("left", (e.pageX + 14) + "px").style("top", (e.pageY + 14) + "px"))
  .on("mouseout", () => tooltip.style("display", "none"))
  .call(d3.drag()
    .on("start", (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
    .on("drag", (e, d) => { d.fx = e.x; d.fy = e.y; })
    .on("end", (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; })
  );

const labelArabic = node.append("text").text(d => d.arabic);
const labelEng = node.append("text").attr("class", "gloss").attr("dy", d => radius(d.count) + 12).text(d => d.english);

const sim = d3.forceSimulation(data.nodes)
  .force("link", d3.forceLink(data.edges).id(d => d.id).distance(d => 100 / Math.sqrt(d.weight)).strength(0.4))
  .force("charge", d3.forceManyBody().strength(-400))
  .force("center", d3.forceCenter(width / 2, height / 2))
  .force("collision", d3.forceCollide().radius(d => radius(d.count) + 18))
  .on("tick", () => {
    link
      .attr("x1", d => d.source.x).attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
    node.attr("transform", d => `translate(${d.x},${d.y})`);
  });

// Controls
d3.select("#edgeThreshold").on("input", function() {
  const t = +this.value;
  d3.select("#edgeThresholdVal").text(t);
  link.style("display", d => d.weight >= t ? null : "none");
});
d3.select("#showLabels").on("change", function() {
  const show = this.checked;
  labelArabic.style("display", show ? null : "none");
  labelEng.style("display", show ? null : "none");
});
d3.select("#chargeStrength").on("input", function() {
  sim.force("charge").strength(+this.value);
  sim.alpha(0.5).restart();
});

// Legend
const clusters = [...new Set(data.nodes.map(n => n.cluster))].sort();
const legend = d3.select("#legend");
legend.append("div").style("font-weight", "600").style("margin-bottom", "6px").text(`${clusters.length} clusters detected`);
clusters.forEach(c => {
  const members = data.nodes.filter(n => n.cluster === c);
  const item = legend.append("div").attr("class", "legend-item");
  item.append("div").attr("class", "legend-dot").style("background", color(c));
  item.append("span").text(`Cluster ${c + 1} (${members.length}): ` + members.map(m => m.arabic).join(" · "));
});
</script>
</body>
</html>
"""


def write_html(graph_data, out_dir, title, subtitle):
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "data.json"
    with json_path.open("w") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    html = HTML_TEMPLATE.replace("__TITLE__", title) \
                        .replace("__SUBTITLE__", subtitle) \
                        .replace("__DATA__", json.dumps(graph_data, ensure_ascii=False))
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"  wrote {json_path}")
    print(f"  wrote {out_dir / 'index.html'}")


def cmd_cognition():
    """14 cognitive roots only."""
    print("loading corpus...")
    ayah_roots, root_count, root_arabic = load_corpus()
    print("building graph (14 cognitive roots)...")
    graph = build_graph_data(COG14, ayah_roots, root_count, root_arabic)
    print(f"  nodes: {len(graph['nodes'])}, edges: {len(graph['edges'])}, clusters: {graph['n_clusters']}")
    out = ROOT / "notes" / "cognition" / "graph"
    write_html(
        graph, out,
        title="Cognition root co-occurrence graph (14 roots)",
        subtitle="Nodes: cognitive roots (sized by Quran-wide occurrence). Edges: ayahs in which both roots appear (thickness = co-occurrence count). Clusters: detected via weighted label propagation. Drag nodes; hover for details.",
    )


CANVAS_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>__TITLE__</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif; margin: 0; background: #0f1115; color: #e8e8e8; overflow: hidden; }
  .header { padding: 12px 20px; background: #181b22; border-bottom: 1px solid #2a2e38; }
  .header h1 { margin: 0; font-size: 16px; font-weight: 600; color: #fff; }
  .header p { margin: 4px 0 0 0; font-size: 12px; color: #999; }
  .controls { padding: 8px 20px; background: #181b22; border-bottom: 1px solid #2a2e38; font-size: 12px; display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
  .controls label { display: flex; gap: 6px; align-items: center; color: #ccc; }
  .controls input[type=range] { width: 120px; }
  .controls input[type=text] { background: #2a2e38; color: #fff; border: 1px solid #444; padding: 4px 8px; border-radius: 3px; width: 200px; font-family: "SF Arabic", "Geeza Pro", system-ui, serif; font-size: 14px; }
  .controls button { background: #3b82f6; color: white; border: none; padding: 5px 12px; border-radius: 3px; cursor: pointer; font-size: 12px; }
  .controls button:hover { background: #2563eb; }
  #graph { display: block; cursor: grab; }
  #graph:active { cursor: grabbing; }
  .info-panel { position: absolute; top: 110px; right: 16px; width: 280px; background: rgba(24,27,34,0.95); border: 1px solid #2a2e38; border-radius: 6px; padding: 14px; font-size: 12px; max-height: calc(100vh - 140px); overflow-y: auto; z-index: 100; }
  .info-panel h3 { margin: 0 0 8px 0; font-size: 14px; }
  .info-panel .arabic { font-family: "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", "Amiri", serif; font-size: 22px; color: #fff; }
  .info-panel .meta { color: #999; margin: 4px 0 8px 0; }
  .info-panel .top-co { margin-top: 10px; padding-top: 10px; border-top: 1px solid #2a2e38; }
  .info-panel .top-co .row { display: flex; justify-content: space-between; padding: 2px 0; }
  .info-panel .top-co .row .a { font-family: "SF Arabic", "Geeza Pro", serif; font-size: 14px; }
  .info-panel .top-co .row .w { color: #999; font-size: 11px; }
  .legend { position: absolute; top: 110px; left: 16px; max-width: 220px; background: rgba(24,27,34,0.95); border: 1px solid #2a2e38; border-radius: 6px; padding: 10px 12px; font-size: 11px; max-height: calc(100vh - 140px); overflow-y: auto; z-index: 100; }
  .legend-title { font-weight: 600; margin-bottom: 6px; font-size: 12px; }
  .legend-item { display: flex; align-items: center; gap: 6px; margin: 2px 0; cursor: pointer; padding: 3px 4px; border-radius: 3px; }
  .legend-item:hover { background: #2a2e38; }
  .legend-item.active { background: #2a2e38; }
  .legend-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
  .legend-item.dimmed { opacity: 0.3; }
  .stats { position: absolute; bottom: 8px; left: 16px; font-size: 11px; color: #666; }
</style>
</head>
<body>
<div class="header">
  <h1>__TITLE__</h1>
  <p>__SUBTITLE__</p>
</div>
<div class="controls">
  <label>Edge weight ≥ <span id="edgeThresholdVal">3</span><input type="range" id="edgeThreshold" min="1" max="50" value="3" /></label>
  <label>Show labels <select id="labelMode"><option value="top">top 50</option><option value="all-zoomed">when zoomed</option><option value="hover">on hover</option><option value="none">none</option></select></label>
  <label>Search: <input type="text" id="search" placeholder="Arabic root, e.g. علم or rHm" /></label>
  <button id="resetView">Reset view</button>
  <button id="restartSim">Restart layout</button>
  <span style="color:#666">Drag: pan · Scroll: zoom · Click node: details</span>
</div>
<canvas id="graph"></canvas>
<div class="info-panel" id="info" style="display:none;"></div>
<div class="legend" id="legend"></div>
<div class="stats" id="stats"></div>

<script>
const data = __DATA__;

// Build maps
const nodeById = {};
data.nodes.forEach(n => { nodeById[n.id] = n; });
data.edges.forEach(e => {
  // Resolve to references for D3 force
  if (typeof e.source === "string") e.source = nodeById[e.source];
  if (typeof e.target === "string") e.target = nodeById[e.target];
});

// Compute neighbors for hover/click
const neighbors = {};
data.nodes.forEach(n => { neighbors[n.id] = new Map(); });
data.edges.forEach(e => {
  neighbors[e.source.id].set(e.target.id, e.weight);
  neighbors[e.target.id].set(e.source.id, e.weight);
});

// Cluster colors
const palette = [
  "#3b82f6", "#ef4444", "#10b981", "#f59e0b", "#8b5cf6",
  "#ec4899", "#06b6d4", "#84cc16", "#f97316", "#6366f1",
  "#14b8a6", "#eab308", "#a855f7", "#22c55e", "#0ea5e9",
  "#dc2626", "#7c3aed", "#65a30d", "#d97706", "#0891b2",
  "#be185d", "#059669", "#9333ea", "#ca8a04", "#1d4ed8",
];
const clusterColor = c => palette[c % palette.length];

// Cluster sizes for legend
const clusterCounts = {};
data.nodes.forEach(n => { clusterCounts[n.cluster] = (clusterCounts[n.cluster] || 0) + 1; });
const sortedClusters = Object.keys(clusterCounts).map(Number).sort((a,b) => clusterCounts[b] - clusterCounts[a]);

// Canvas setup
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight - 78;
}
resize();
window.addEventListener("resize", resize);

// Node radius (log scale)
function radius(count) { return 2 + Math.log(Math.max(count, 1)) * 1.4; }

// State
let transform = d3.zoomIdentity;
let edgeThreshold = 3;
let labelMode = "top";
let hoveredNode = null;
let selectedNode = null;
let highlightCluster = null;
let searchTerm = "";

// Force simulation
const sim = d3.forceSimulation(data.nodes)
  .force("link", d3.forceLink(data.edges).id(d => d.id)
      .distance(d => 30 + 60 / Math.sqrt(d.weight))
      .strength(d => Math.min(0.6, 0.04 * Math.log(d.weight + 1))))
  .force("charge", d3.forceManyBody().strength(d => -8 - radius(d.count) * 1.5).distanceMax(400))
  .force("center", d3.forceCenter(canvas.width / 2, canvas.height / 2))
  .force("collision", d3.forceCollide().radius(d => radius(d.count) + 1.5))
  .force("clusterX", d3.forceX(d => clusterX(d.cluster)).strength(0.04))
  .force("clusterY", d3.forceY(d => clusterY(d.cluster)).strength(0.04))
  .alphaDecay(0.012)
  .velocityDecay(0.5)
  .on("tick", draw);

// Compute cluster centroids on a circle
function clusterX(c) {
  const idx = sortedClusters.indexOf(c);
  const total = sortedClusters.length;
  return canvas.width / 2 + Math.cos(idx / total * 2 * Math.PI) * Math.min(canvas.width, canvas.height) * 0.32;
}
function clusterY(c) {
  const idx = sortedClusters.indexOf(c);
  const total = sortedClusters.length;
  return canvas.height / 2 + Math.sin(idx / total * 2 * Math.PI) * Math.min(canvas.width, canvas.height) * 0.32;
}

// Top nodes for label display
const topByFreq = [...data.nodes].sort((a,b) => b.count - a.count).slice(0, 50).map(n => n.id);
const topSet = new Set(topByFreq);

function shouldLabel(n) {
  if (labelMode === "none") return false;
  if (labelMode === "hover") return n === hoveredNode || n === selectedNode;
  if (labelMode === "top") return topSet.has(n.id) || n === hoveredNode || n === selectedNode;
  if (labelMode === "all-zoomed") return transform.k > 1.5 || n === hoveredNode || n === selectedNode;
  return false;
}

function nodeMatches(n) {
  if (!searchTerm) return false;
  return n.id.toLowerCase().includes(searchTerm.toLowerCase()) || n.arabic.includes(searchTerm) || (n.english && n.english.toLowerCase().includes(searchTerm.toLowerCase()));
}

function draw() {
  ctx.save();
  ctx.fillStyle = "#0f1115";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.translate(transform.x, transform.y);
  ctx.scale(transform.k, transform.k);

  // Edges
  ctx.lineCap = "round";
  for (const e of data.edges) {
    if (e.weight < edgeThreshold) continue;
    let alpha = 0.18;
    if (highlightCluster !== null) {
      if (e.source.cluster !== highlightCluster && e.target.cluster !== highlightCluster) alpha = 0.04;
    }
    if (selectedNode && (e.source === selectedNode || e.target === selectedNode)) alpha = 0.9;
    ctx.strokeStyle = `rgba(180,180,200,${alpha})`;
    ctx.lineWidth = Math.min(3, Math.sqrt(e.weight) * 0.4) / transform.k;
    ctx.beginPath();
    ctx.moveTo(e.source.x, e.source.y);
    ctx.lineTo(e.target.x, e.target.y);
    ctx.stroke();
  }

  // Nodes
  for (const n of data.nodes) {
    let alpha = 1;
    if (highlightCluster !== null && n.cluster !== highlightCluster) alpha = 0.2;
    if (searchTerm && !nodeMatches(n)) alpha *= 0.3;
    ctx.globalAlpha = alpha;
    ctx.fillStyle = clusterColor(n.cluster);
    ctx.beginPath();
    ctx.arc(n.x, n.y, radius(n.count), 0, 2 * Math.PI);
    ctx.fill();
    if (selectedNode === n || hoveredNode === n || nodeMatches(n)) {
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 2 / transform.k;
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  // Labels (in screen-space-aware font)
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  for (const n of data.nodes) {
    if (!shouldLabel(n)) continue;
    let alpha = 1;
    if (highlightCluster !== null && n.cluster !== highlightCluster) alpha = 0.3;
    if (searchTerm && !nodeMatches(n)) alpha *= 0.4;
    ctx.globalAlpha = alpha;
    const r = radius(n.count);
    const fs = Math.max(10, 14 - Math.log10(data.nodes.length)) / transform.k;
    ctx.font = `${Math.max(fs, 10/transform.k)}px "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", serif`;
    ctx.fillStyle = "rgba(255,255,255,0.95)";
    // Background for readability
    const text = n.arabic;
    const tw = ctx.measureText(text).width;
    const th = fs;
    ctx.fillStyle = "rgba(15,17,21,0.7)";
    ctx.fillRect(n.x - tw/2 - 2, n.y + r + 1, tw + 4, th + 2);
    ctx.fillStyle = "rgba(255,255,255,0.95)";
    ctx.fillText(text, n.x, n.y + r + th/2 + 2);
    ctx.globalAlpha = 1;
  }

  ctx.restore();
}

// Zoom and pan
const zoom = d3.zoom().scaleExtent([0.1, 8]).on("zoom", e => { transform = e.transform; draw(); });
d3.select(canvas).call(zoom);
d3.select("#resetView").on("click", () => { d3.select(canvas).transition().duration(500).call(zoom.transform, d3.zoomIdentity); });
d3.select("#restartSim").on("click", () => { sim.alpha(0.5).restart(); });

// Mouse position to graph coordinates
function getNodeAt(x, y) {
  const gx = (x - transform.x) / transform.k;
  const gy = (y - transform.y) / transform.k;
  let closest = null;
  let minD = Infinity;
  for (const n of data.nodes) {
    const dx = n.x - gx;
    const dy = n.y - gy;
    const r = radius(n.count) + 4;
    const d2 = dx*dx + dy*dy;
    if (d2 < r*r && d2 < minD) {
      minD = d2;
      closest = n;
    }
  }
  return closest;
}

canvas.addEventListener("mousemove", e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  const n = getNodeAt(x, y);
  if (n !== hoveredNode) { hoveredNode = n; draw(); }
  canvas.style.cursor = n ? "pointer" : (selectedNode ? "grab" : "grab");
});

canvas.addEventListener("click", e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  const n = getNodeAt(x, y);
  if (n) showInfo(n); else hideInfo();
});

function showInfo(n) {
  selectedNode = n;
  draw();
  const panel = document.getElementById("info");
  const top = [...neighbors[n.id].entries()]
    .sort((a,b) => b[1] - a[1]).slice(0, 15)
    .map(([id, w]) => {
      const nb = nodeById[id];
      return `<div class="row"><span class="a">${nb.arabic}</span><span class="w">${id} · ${w} ayahs</span></div>`;
    }).join("");
  panel.innerHTML = `
    <h3 style="color:${clusterColor(n.cluster)}">●&nbsp; <span class="arabic">${n.arabic}</span></h3>
    <div class="meta">
      <b>${n.id}</b>${n.english ? " — " + n.english : ""}<br>
      ${n.count} occurrences in Quran<br>
      Cluster ${n.cluster + 1} (${clusterCounts[n.cluster]} roots)
    </div>
    <div class="top-co">
      <b>Top co-occurring (any weight):</b>
      ${top || "<i>(none)</i>"}
    </div>
    <button onclick="hideInfo()" style="margin-top: 10px; background: #444; color: white; border: none; padding: 4px 10px; border-radius: 3px; cursor: pointer;">Close</button>
  `;
  panel.style.display = "block";
}
function hideInfo() {
  selectedNode = null;
  document.getElementById("info").style.display = "none";
  draw();
}
window.hideInfo = hideInfo;

// Controls
d3.select("#edgeThreshold").on("input", function() {
  edgeThreshold = +this.value;
  d3.select("#edgeThresholdVal").text(edgeThreshold);
  updateStats();
  draw();
});
d3.select("#labelMode").on("change", function() { labelMode = this.value; draw(); });
d3.select("#search").on("input", function() { searchTerm = this.value.trim(); draw(); });

// Legend
const legend = d3.select("#legend");
legend.append("div").attr("class", "legend-title").text(`${sortedClusters.length} clusters · ${data.nodes.length} nodes · ${data.edges.length} edges`);
sortedClusters.forEach(c => {
  // Get top-3 most-frequent members as a preview
  const members = data.nodes.filter(n => n.cluster === c).sort((a,b) => b.count - a.count);
  const preview = members.slice(0, 3).map(m => m.arabic).join(" · ");
  const item = legend.append("div").attr("class", "legend-item")
    .on("click", () => {
      highlightCluster = highlightCluster === c ? null : c;
      legend.selectAll(".legend-item").classed("active", false);
      if (highlightCluster !== null) d3.select(item.node()).classed("active", true);
      draw();
    });
  item.append("div").attr("class", "legend-dot").style("background", clusterColor(c));
  item.append("span").html(`<b>${c+1}</b> (${clusterCounts[c]}): ${preview}`);
});

function updateStats() {
  const visibleEdges = data.edges.filter(e => e.weight >= edgeThreshold).length;
  document.getElementById("stats").textContent = `Showing ${visibleEdges} of ${data.edges.length} edges (weight ≥ ${edgeThreshold})`;
}
updateStats();
</script>
</body>
</html>
"""


def write_canvas_html(graph_data, out_dir, title, subtitle):
    """Write canvas-based HTML for large graphs."""
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "data.json"
    with json_path.open("w") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    html = CANVAS_HTML_TEMPLATE.replace("__TITLE__", title) \
                                .replace("__SUBTITLE__", subtitle) \
                                .replace("__DATA__", json.dumps(graph_data, ensure_ascii=False))
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"  wrote {json_path}  ({json_path.stat().st_size / 1024 / 1024:.1f} MB)")
    print(f"  wrote {out_dir / 'index.html'}  ({(out_dir / 'index.html').stat().st_size / 1024 / 1024:.1f} MB)")


# Human-readable names for the 15 thematically-analyzed clusters.
# (See notes/full-quran-graph/clusters/cluster-NN-name.md for full analyses)
CLUSTER_NAMES = {
    4:  "Revelation, Speech & Disbelief",
    8:  "Allegiance & the Object of Worship",
    0:  "The Believers' Reward",
    5:  "The Commanded Self",
    19: "Household Law & Lineage",
    17: "Bodily Purity & Prayer",
    7:  "Sea-Rescue / Bounty / Gratitude",
    90: "Sin–Mercy Economy",
    96: "Dunya vs. Ākhirah",
    11: "Vegetative Signs / Reflective Gaze",
    66: "Jihād fī Sabīl Allāh",
    62: "The Prepared Fire",
    43: "Divine Will & Dominion",
    77: "Creation & the Appointed Term",
    75: "Witnessing the Visible Sign",
}


CLUSTER_AWARE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>__TITLE__</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif; margin: 0; background: #0a0d12; color: #e8e8e8; overflow: hidden; }
  .header { padding: 14px 22px; background: #131720; border-bottom: 1px solid #232938; }
  .header h1 { margin: 0; font-size: 17px; font-weight: 600; color: #fff; }
  .header p { margin: 4px 0 0 0; font-size: 12px; color: #8a93a3; }
  .controls { padding: 10px 22px; background: #131720; border-bottom: 1px solid #232938; font-size: 12px; display: flex; gap: 18px; align-items: center; flex-wrap: wrap; }
  .controls label { display: flex; gap: 7px; align-items: center; color: #ccc; }
  .controls input[type=range] { width: 110px; }
  .controls input[type=text] { background: #232938; color: #fff; border: 1px solid #3a4255; padding: 5px 9px; border-radius: 4px; width: 220px; font-family: "SF Arabic", "Geeza Pro", system-ui, serif; font-size: 14px; }
  .controls button { background: #4f7cff; color: white; border: none; padding: 6px 14px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: 500; }
  .controls button:hover { background: #3b66ec; }
  .controls button.toggle.active { background: #10b981; }
  #graph { display: block; cursor: grab; }
  #graph:active { cursor: grabbing; }
  .info-panel { position: absolute; top: 120px; right: 18px; width: 300px; background: rgba(19,23,32,0.97); border: 1px solid #232938; border-radius: 6px; padding: 16px; font-size: 12px; max-height: calc(100vh - 150px); overflow-y: auto; z-index: 100; box-shadow: 0 8px 24px rgba(0,0,0,0.4); }
  .info-panel h3 { margin: 0 0 8px 0; font-size: 14px; }
  .info-panel .arabic { font-family: "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", "Amiri", serif; font-size: 24px; color: #fff; }
  .info-panel .meta { color: #8a93a3; margin: 4px 0 8px 0; }
  .info-panel .top-co { margin-top: 12px; padding-top: 12px; border-top: 1px solid #232938; }
  .info-panel .top-co .row { display: flex; justify-content: space-between; padding: 3px 0; align-items: center; }
  .info-panel .top-co .row .a { font-family: "SF Arabic", "Geeza Pro", serif; font-size: 15px; }
  .info-panel .top-co .row .w { color: #8a93a3; font-size: 11px; }
  .legend { position: absolute; top: 100px; left: 14px; width: 230px; background: rgba(19,23,32,0.97); border: 1px solid #232938; border-radius: 6px; padding: 10px 12px; font-size: 11px; max-height: calc(100vh - 130px); overflow-y: auto; z-index: 100; transition: transform 0.2s ease, opacity 0.2s ease; }
  .legend.collapsed { transform: translateX(-260px); opacity: 0; pointer-events: none; }
  .legend-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .legend-title { font-weight: 600; font-size: 12px; color: #fff; }
  .legend-close { background: none; border: none; color: #8a93a3; cursor: pointer; font-size: 16px; padding: 0 4px; line-height: 1; }
  .legend-close:hover { color: #fff; }
  .legend-item { display: flex; align-items: center; gap: 7px; margin: 3px 0; cursor: pointer; padding: 3px 4px; border-radius: 3px; line-height: 1.25; }
  .legend-item:hover { background: #232938; }
  .legend-item.active { background: #2a334a; outline: 1px solid #4f7cff; }
  .legend-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
  .legend-name { font-weight: 500; color: #e8e8e8; font-size: 11px; }
  .legend-meta { color: #8a93a3; font-size: 9px; }
  .legend-toggle { position: absolute; top: 100px; left: 14px; width: 32px; height: 32px; background: rgba(19,23,32,0.97); border: 1px solid #232938; border-radius: 6px; color: #e8e8e8; cursor: pointer; display: flex; align-items: center; justify-content: center; z-index: 99; opacity: 0; pointer-events: none; transition: opacity 0.2s ease; font-size: 14px; }
  .legend-toggle.visible { opacity: 1; pointer-events: auto; }
  .legend-toggle:hover { background: #232938; }
  .stats { position: absolute; bottom: 10px; left: 14px; font-size: 11px; color: #5a6378; background: rgba(10,13,18,0.7); padding: 4px 8px; border-radius: 3px; }
  .help { position: absolute; bottom: 10px; right: 14px; font-size: 11px; color: #5a6378; background: rgba(10,13,18,0.7); padding: 4px 8px; border-radius: 3px; }
</style>
</head>
<body>
<div class="header">
  <h1>__TITLE__</h1>
  <p>__SUBTITLE__</p>
</div>
<div class="controls">
  <label>Cluster min size: <span id="minSizeVal">3</span><input type="range" id="minSize" min="1" max="50" value="3" /></label>
  <label>Edge weight ≥ <span id="edgeThresholdVal">5</span><input type="range" id="edgeThreshold" min="1" max="100" value="5" /></label>
  <label>Show: <select id="labelMode"><option value="named">named clusters only</option><option value="top">top 80 roots</option><option value="all">all roots (zoom)</option><option value="hover">on hover</option></select></label>
  <label>Search: <input type="text" id="search" placeholder="root, e.g. علم or rHm" /></label>
  <button id="resetView">Reset view</button>
  <button id="restartSim">Re-layout</button>
</div>
<canvas id="graph"></canvas>
<div class="info-panel" id="info" style="display:none;"></div>
<button class="legend-toggle" id="legendToggle" title="Show legend">☰</button>
<div class="legend" id="legend"></div>
<div class="stats" id="stats"></div>
<div class="help">drag: pan · scroll: zoom · click cluster: focus · click node: details</div>

<script>
const data = __DATA__;
const CLUSTER_NAMES = __CLUSTER_NAMES__;

// Resolve edge endpoints
const nodeById = {};
data.nodes.forEach(n => { nodeById[n.id] = n; });
data.edges.forEach(e => {
  if (typeof e.source === "string") e.source = nodeById[e.source];
  if (typeof e.target === "string") e.target = nodeById[e.target];
});

// Neighbors
const neighbors = {};
data.nodes.forEach(n => { neighbors[n.id] = new Map(); });
data.edges.forEach(e => {
  neighbors[e.source.id].set(e.target.id, e.weight);
  neighbors[e.target.id].set(e.source.id, e.weight);
});

// Cluster sizes
const clusterMembers = {};
data.nodes.forEach(n => { (clusterMembers[n.cluster] = clusterMembers[n.cluster] || []).push(n); });
const sortedClusters = Object.keys(clusterMembers).map(Number).sort((a,b) => clusterMembers[b].length - clusterMembers[a].length);

// Vibrant palette — 25 distinguishable colors
const palette = [
  "#5b8def", "#ff5e5b", "#22c55e", "#fbbf24", "#a855f7",
  "#ec4899", "#06b6d4", "#84cc16", "#f97316", "#818cf8",
  "#14b8a6", "#facc15", "#c084fc", "#34d399", "#0ea5e9",
  "#f87171", "#7c3aed", "#a3e635", "#fb923c", "#22d3ee",
  "#f472b6", "#10b981", "#d946ef", "#eab308", "#3b82f6",
];
function clusterColor(c) {
  // Pick stable color by sortedClusters index so largest clusters get most distinct colors
  const idx = sortedClusters.indexOf(c);
  return palette[idx % palette.length];
}

// Cluster centroids — pack each cluster as a circle whose radius scales with member count.
// Use d3.packSiblings for tight, non-overlapping placement (no wasted space).
const clusterCentroid = {};
const clusterCircles = sortedClusters.map(c => {
  const size = clusterMembers[c].length;
  // Radius proportional to sqrt(member count) so area scales linearly with members
  return { id: c, r: Math.max(8, Math.sqrt(size) * 12) };
});
d3.packSiblings(clusterCircles);
// Center the packed bundle on (0,0) — we'll offset to canvas center on draw
const xs = clusterCircles.map(c => c.x);
const ys = clusterCircles.map(c => c.y);
const cxOff = (Math.max(...xs) + Math.min(...xs)) / 2;
const cyOff = (Math.max(...ys) + Math.min(...ys)) / 2;
clusterCircles.forEach(c => {
  c.x -= cxOff;
  c.y -= cyOff;
  clusterCentroid[c.id] = { x: 0, y: 0, r: c.r, baseX: c.x, baseY: c.y };
});

// Canvas
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight - 90;
  // Center the packed cluster bundle on canvas
  const cx = canvas.width / 2;
  const cy = canvas.height / 2;
  sortedClusters.forEach(c => {
    const cc = clusterCentroid[c];
    cc.x = cx + cc.baseX;
    cc.y = cy + cc.baseY;
  });
}
resize();
window.addEventListener("resize", () => { resize(); sim.alpha(0.3).restart(); });

function radius(count) { return 2 + Math.log(Math.max(count, 1)) * 1.5; }

// State
let transform = d3.zoomIdentity;
let edgeThreshold = 5;
let minClusterSize = 3;
let labelMode = "named";
let hoveredNode = null;
let selectedNode = null;
let highlightCluster = null;
let searchTerm = "";

// Filter nodes by cluster size
function nodeVisible(n) {
  if (clusterMembers[n.cluster].length < minClusterSize) return false;
  return true;
}
function edgeVisible(e) {
  if (e.weight < edgeThreshold) return false;
  if (!nodeVisible(e.source) || !nodeVisible(e.target)) return false;
  // Hide inter-cluster edges to reduce visual noise (unless cluster highlighted or node selected)
  if (e.source.cluster !== e.target.cluster && !highlightCluster && !selectedNode) return false;
  if (highlightCluster !== null) {
    if (e.source.cluster !== highlightCluster && e.target.cluster !== highlightCluster) return false;
  }
  return true;
}

// Force simulation with strong cluster-anchored positioning.
// Higher cluster gravity (0.5) keeps members tightly packed in their cluster's circle.
// Charge limited to short range to prevent inter-cluster repulsion blowing things apart.
const sim = d3.forceSimulation(data.nodes)
  .force("link", d3.forceLink(data.edges).id(d => d.id)
      .distance(d => d.source.cluster === d.target.cluster ? 6 : 200)
      .strength(d => d.source.cluster === d.target.cluster ? 0.08 : 0.001))
  .force("charge", d3.forceManyBody().strength(d => -1 - radius(d.count) * 0.5).distanceMax(40))
  .force("clusterX", d3.forceX(d => clusterCentroid[d.cluster].x).strength(0.5))
  .force("clusterY", d3.forceY(d => clusterCentroid[d.cluster].y).strength(0.5))
  .force("collision", d3.forceCollide().radius(d => radius(d.count) + 0.5))
  .alphaDecay(0.025)
  .velocityDecay(0.6)
  .on("tick", draw);

const topByFreq = [...data.nodes].sort((a,b) => b.count - a.count).slice(0, 80).map(n => n.id);
const topSet = new Set(topByFreq);

function shouldLabel(n) {
  if (n === hoveredNode || n === selectedNode) return true;
  if (!nodeVisible(n)) return false;
  if (labelMode === "hover") return false;
  if (labelMode === "top") return topSet.has(n.id);
  if (labelMode === "all") return transform.k > 1.5;
  if (labelMode === "named") return false;  // only show cluster labels
  return false;
}

function nodeMatches(n) {
  if (!searchTerm) return false;
  return n.id.toLowerCase().includes(searchTerm.toLowerCase()) || n.arabic.includes(searchTerm) || (n.english && n.english.toLowerCase().includes(searchTerm.toLowerCase()));
}

function draw() {
  ctx.save();
  ctx.fillStyle = "#0a0d12";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.translate(transform.x, transform.y);
  ctx.scale(transform.k, transform.k);

  // 1. Cluster background "bubbles" — convex hull of each visible cluster, rendered as a soft glow
  for (const c of sortedClusters) {
    if (clusterMembers[c].length < minClusterSize) continue;
    const members = clusterMembers[c].filter(n => n.x !== undefined);
    if (members.length < 3) continue;
    const cc = clusterCentroid[c];
    if (highlightCluster !== null && c !== highlightCluster) continue;
    // Compute approximate cluster radius
    let maxD = 0;
    for (const n of members) {
      const dx = n.x - cc.x, dy = n.y - cc.y;
      const d = Math.sqrt(dx*dx + dy*dy);
      if (d > maxD) maxD = d;
    }
    const r = maxD + 12;
    const grd = ctx.createRadialGradient(cc.x, cc.y, 0, cc.x, cc.y, r);
    const col = clusterColor(c);
    grd.addColorStop(0, hexAlpha(col, highlightCluster === c ? 0.25 : 0.10));
    grd.addColorStop(1, hexAlpha(col, 0));
    ctx.fillStyle = grd;
    ctx.beginPath();
    ctx.arc(cc.x, cc.y, r, 0, 2 * Math.PI);
    ctx.fill();
  }

  // 2. Edges
  ctx.lineCap = "round";
  for (const e of data.edges) {
    if (!edgeVisible(e)) continue;
    let alpha = e.source.cluster === e.target.cluster ? 0.20 : 0.10;
    if (selectedNode && (e.source === selectedNode || e.target === selectedNode)) alpha = 0.95;
    ctx.strokeStyle = `rgba(180,190,210,${alpha})`;
    ctx.lineWidth = Math.min(2.5, Math.sqrt(e.weight) * 0.35) / transform.k;
    ctx.beginPath();
    ctx.moveTo(e.source.x, e.source.y);
    ctx.lineTo(e.target.x, e.target.y);
    ctx.stroke();
  }

  // 3. Nodes
  for (const n of data.nodes) {
    if (!nodeVisible(n)) continue;
    let alpha = 1;
    if (highlightCluster !== null && n.cluster !== highlightCluster) alpha = 0.15;
    if (searchTerm && !nodeMatches(n)) alpha *= 0.25;
    ctx.globalAlpha = alpha;
    ctx.fillStyle = clusterColor(n.cluster);
    ctx.beginPath();
    ctx.arc(n.x, n.y, radius(n.count), 0, 2 * Math.PI);
    ctx.fill();
    if (selectedNode === n || hoveredNode === n || nodeMatches(n)) {
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 2 / transform.k;
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
  }

  // 4. Cluster name labels at centroids
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  for (const c of sortedClusters) {
    if (clusterMembers[c].length < minClusterSize) continue;
    const name = CLUSTER_NAMES[c];
    if (!name && labelMode === "named") continue;
    const label = name || `Cluster ${c+1} (${clusterMembers[c].length})`;
    const cc = clusterCentroid[c];
    if (highlightCluster !== null && c !== highlightCluster) continue;
    const fs = Math.max(11, name ? 14 : 11) / transform.k;
    ctx.font = `${name ? '600' : '400'} ${Math.max(fs, 11/transform.k)}px -apple-system, system-ui, sans-serif`;
    const tw = ctx.measureText(label).width;
    const pad = 6 / transform.k;
    // Position slightly above centroid
    const ly = cc.y - 4 / transform.k;
    ctx.fillStyle = "rgba(10,13,18,0.80)";
    ctx.fillRect(cc.x - tw/2 - pad, ly - fs/2 - pad/2, tw + pad*2, fs + pad);
    ctx.fillStyle = name ? clusterColor(c) : "rgba(180,190,210,0.7)";
    ctx.fillText(label, cc.x, ly);
  }

  // 5. Per-node labels (if mode requires)
  for (const n of data.nodes) {
    if (!shouldLabel(n)) continue;
    let alpha = 1;
    if (highlightCluster !== null && n.cluster !== highlightCluster) alpha = 0.4;
    if (searchTerm && !nodeMatches(n)) alpha *= 0.4;
    ctx.globalAlpha = alpha;
    const r = radius(n.count);
    const fs = Math.max(10, 13 - Math.log10(data.nodes.length)) / transform.k;
    ctx.font = `${Math.max(fs, 10/transform.k)}px "SF Arabic", "Geeza Pro", "Noto Naskh Arabic", serif`;
    const text = n.arabic;
    const tw = ctx.measureText(text).width;
    ctx.fillStyle = "rgba(10,13,18,0.85)";
    ctx.fillRect(n.x - tw/2 - 2, n.y + r + 1, tw + 4, fs + 2);
    ctx.fillStyle = "#fff";
    ctx.fillText(text, n.x, n.y + r + fs/2 + 2);
    ctx.globalAlpha = 1;
  }

  ctx.restore();
}

function hexAlpha(hex, a) {
  // Convert "#rrggbb" to "rgba(r,g,b,a)"
  const r = parseInt(hex.slice(1,3), 16);
  const g = parseInt(hex.slice(3,5), 16);
  const b = parseInt(hex.slice(5,7), 16);
  return `rgba(${r},${g},${b},${a})`;
}

// Zoom and pan — wide range for zoom-out (see whole map) and zoom-in (inspect clusters)
const zoom = d3.zoom().scaleExtent([0.05, 40]).on("zoom", e => { transform = e.transform; draw(); });
d3.select(canvas).call(zoom);

function fitToScreen(durationMs = 600) {
  if (!data.nodes.length) return;
  const visible = data.nodes.filter(nodeVisible).filter(n => n.x !== undefined);
  if (!visible.length) return;
  const xs = visible.map(n => n.x), ys = visible.map(n => n.y);
  const minX = Math.min(...xs) - 30, maxX = Math.max(...xs) + 30;
  const minY = Math.min(...ys) - 30, maxY = Math.max(...ys) + 30;
  const w = maxX - minX, h = maxY - minY;
  const k = Math.min(canvas.width / w, canvas.height / h, 4) * 0.92;
  const tx = canvas.width / 2 - ((minX + maxX) / 2) * k;
  const ty = canvas.height / 2 - ((minY + maxY) / 2) * k;
  d3.select(canvas).transition().duration(durationMs).call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(k));
}

d3.select("#resetView").on("click", () => fitToScreen());
d3.select("#restartSim").on("click", () => sim.alpha(0.5).restart());

// Auto-fit on first stable tick
let initialFitDone = false;
sim.on("end", () => {
  if (!initialFitDone) { initialFitDone = true; fitToScreen(0); }
});
// Also fit after 2s as a safety net (in case sim doesn't fully end)
setTimeout(() => { if (!initialFitDone) { initialFitDone = true; fitToScreen(0); } }, 2000);

function getNodeAt(x, y) {
  const gx = (x - transform.x) / transform.k;
  const gy = (y - transform.y) / transform.k;
  let closest = null, minD = Infinity;
  for (const n of data.nodes) {
    if (!nodeVisible(n)) continue;
    const dx = n.x - gx, dy = n.y - gy;
    const r = radius(n.count) + 4;
    const d2 = dx*dx + dy*dy;
    if (d2 < r*r && d2 < minD) { minD = d2; closest = n; }
  }
  return closest;
}

function getClusterAt(x, y) {
  // Detect click on cluster label
  const gx = (x - transform.x) / transform.k;
  const gy = (y - transform.y) / transform.k;
  for (const c of sortedClusters) {
    if (clusterMembers[c].length < minClusterSize) continue;
    const cc = clusterCentroid[c];
    const dx = cc.x - gx, dy = cc.y - gy;
    if (dx*dx + dy*dy < (40/transform.k)**2) return c;
  }
  return null;
}

canvas.addEventListener("mousemove", e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left, y = e.clientY - rect.top;
  const n = getNodeAt(x, y);
  if (n !== hoveredNode) { hoveredNode = n; draw(); }
  canvas.style.cursor = n ? "pointer" : "grab";
});

canvas.addEventListener("click", e => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left, y = e.clientY - rect.top;
  const n = getNodeAt(x, y);
  if (n) { showInfo(n); return; }
  const c = getClusterAt(x, y);
  if (c !== null) {
    highlightCluster = highlightCluster === c ? null : c;
    legend.selectAll(".legend-item").classed("active", false);
    if (highlightCluster !== null) {
      legend.selectAll(".legend-item").filter(function(){return +this.dataset.c === highlightCluster;}).classed("active", true);
    }
    draw();
  } else {
    highlightCluster = null;
    legend.selectAll(".legend-item").classed("active", false);
    hideInfo();
  }
});

function showInfo(n) {
  selectedNode = n;
  draw();
  const panel = document.getElementById("info");
  const top = [...neighbors[n.id].entries()].sort((a,b) => b[1] - a[1]).slice(0, 15);
  const arabicMap = Object.fromEntries(data.nodes.map(n => [n.id, n.arabic]));
  const clusterName = CLUSTER_NAMES[n.cluster] || `Cluster ${n.cluster+1}`;
  panel.innerHTML = `
    <h3 style="color:${clusterColor(n.cluster)}">●&nbsp; <span class="arabic">${n.arabic}</span></h3>
    <div class="meta">
      <b>${n.id}</b>${n.english ? " — " + n.english : ""}<br>
      ${n.count} occurrences in Quran<br>
      <i>${clusterName}</i> (${clusterMembers[n.cluster].length} roots)
    </div>
    <div class="top-co">
      <b>Top co-occurring (any weight):</b>
      ${top.map(([id, w]) => `<div class="row"><span class="a">${arabicMap[id]}</span><span class="w">${id} · ${w} ayahs</span></div>`).join("")}
    </div>
    <button onclick="hideInfo()" style="margin-top: 12px; background: #232938; color: white; border: none; padding: 5px 11px; border-radius: 4px; cursor: pointer;">Close</button>
  `;
  panel.style.display = "block";
}
function hideInfo() {
  selectedNode = null;
  document.getElementById("info").style.display = "none";
  draw();
}
window.hideInfo = hideInfo;

// Controls
d3.select("#minSize").on("input", function() { minClusterSize = +this.value; d3.select("#minSizeVal").text(minClusterSize); updateStats(); draw(); });
d3.select("#edgeThreshold").on("input", function() { edgeThreshold = +this.value; d3.select("#edgeThresholdVal").text(edgeThreshold); updateStats(); draw(); });
d3.select("#labelMode").on("change", function() { labelMode = this.value; draw(); });
d3.select("#search").on("input", function() {
  searchTerm = this.value.trim();
  // Auto-pan to first matching node
  if (searchTerm) {
    const match = data.nodes.find(n => nodeMatches(n) && nodeVisible(n));
    if (match) {
      const rect = canvas.getBoundingClientRect();
      const newK = 2;
      const tx = rect.width/2 - match.x * newK;
      const ty = (rect.height - 90)/2 - match.y * newK;
      d3.select(canvas).transition().duration(400).call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(newK));
    }
  }
  draw();
});

// Legend with collapsible header
const legend = d3.select("#legend");
const header = legend.append("div").attr("class", "legend-header");
header.append("div").attr("class", "legend-title").text(`${sortedClusters.length} clusters · ${data.nodes.length} nodes`);
header.append("button").attr("class", "legend-close").attr("title", "Hide legend").text("×")
  .on("click", () => { legend.classed("collapsed", true); d3.select("#legendToggle").classed("visible", true); });

d3.select("#legendToggle").on("click", () => { legend.classed("collapsed", false); d3.select("#legendToggle").classed("visible", false); });

legend.append("div").style("color","#8a93a3").style("font-size","10px").style("margin-bottom","10px").text(`Click cluster to focus. × to hide.`);

const NAMED_COUNT = Object.keys(CLUSTER_NAMES).length;
legend.append("div").style("color","#8a93a3").style("font-size","10px").style("margin-bottom","6px").text(`▼ ${NAMED_COUNT} named clusters (deep-analyzed)`);

sortedClusters.forEach(c => {
  const members = clusterMembers[c];
  const name = CLUSTER_NAMES[c];
  if (!name) return;
  const preview = members.slice(0, 3).map(m => m.arabic).join(" · ");
  const item = legend.append("div").attr("class", "legend-item").attr("data-c", c)
    .on("click", () => {
      highlightCluster = highlightCluster === c ? null : c;
      legend.selectAll(".legend-item").classed("active", false);
      if (highlightCluster !== null) d3.select(item.node()).classed("active", true);
      draw();
    });
  item.append("div").attr("class", "legend-dot").style("background", clusterColor(c));
  const right = item.append("div").style("flex","1");
  right.append("div").attr("class", "legend-name").text(name);
  right.append("div").attr("class", "legend-meta").text(`${members.length} roots · ${preview}`);
});

legend.append("div").style("color","#8a93a3").style("font-size","10px").style("margin","12px 0 6px 0").text(`▼ Other detected clusters (unnamed)`);
sortedClusters.forEach(c => {
  const members = clusterMembers[c];
  if (CLUSTER_NAMES[c]) return;
  if (members.length < 3) return;
  const preview = members.slice(0, 3).map(m => m.arabic).join(" · ");
  const item = legend.append("div").attr("class", "legend-item").attr("data-c", c)
    .on("click", () => {
      highlightCluster = highlightCluster === c ? null : c;
      legend.selectAll(".legend-item").classed("active", false);
      if (highlightCluster !== null) d3.select(item.node()).classed("active", true);
      draw();
    });
  item.append("div").attr("class", "legend-dot").style("background", clusterColor(c));
  item.append("span").html(`<b>${members.length}</b>: ${preview}`);
});

function updateStats() {
  const visibleNodes = data.nodes.filter(nodeVisible).length;
  const visibleClusters = sortedClusters.filter(c => clusterMembers[c].length >= minClusterSize).length;
  const visibleEdges = data.edges.filter(edgeVisible).length;
  document.getElementById("stats").textContent = `Showing ${visibleClusters} clusters · ${visibleNodes} of ${data.nodes.length} nodes · ${visibleEdges} of ${data.edges.length} edges`;
}
updateStats();
</script>
</body>
</html>
"""


def write_cluster_aware_html(graph_data, out_dir, title, subtitle, filename="index.html"):
    """Write the cluster-aware visualization."""
    out_dir.mkdir(parents=True, exist_ok=True)
    html = CLUSTER_AWARE_HTML.replace("__TITLE__", title) \
                              .replace("__SUBTITLE__", subtitle) \
                              .replace("__DATA__", json.dumps(graph_data, ensure_ascii=False)) \
                              .replace("__CLUSTER_NAMES__", json.dumps(CLUSTER_NAMES))
    (out_dir / filename).write_text(html, encoding="utf-8")
    print(f"  wrote {out_dir / filename}  ({(out_dir / filename).stat().st_size / 1024 / 1024:.1f} MB)")


def cmd_all(min_edge_weight=2):
    """Build full Quran-wide co-occurrence graph (all 1,642 roots)."""
    print("loading corpus...")
    ayah_roots, root_count, root_arabic = load_corpus()
    all_roots = sorted(root_count.keys())
    print(f"  {len(all_roots)} unique roots, {sum(root_count.values())} root-bearing words")

    print("computing co-occurrence...")
    edges = build_cooccurrence(all_roots, ayah_roots)
    edge_count_full = len(edges)
    if min_edge_weight > 1:
        edges = {k: v for k, v in edges.items() if v >= min_edge_weight}
    print(f"  {edge_count_full} unique edges (full); {len(edges)} edges with weight >= {min_edge_weight}")

    print("running Louvain clustering...")
    nodes_with_edges = set()
    for a, b in edges:
        nodes_with_edges.add(a)
        nodes_with_edges.add(b)
    all_nodes = sorted(set(all_roots) | nodes_with_edges)
    clusters = louvain(all_nodes, edges, root_count)
    n_clusters = len(set(clusters.values()))
    print(f"  {n_clusters} clusters detected")
    # Cluster sizes
    cluster_sizes = Counter(clusters.values())
    print(f"  largest clusters: {cluster_sizes.most_common(10)}")

    graph = {
        "nodes": [
            {
                "id": r,
                "arabic": root_arabic.get(r, "?"),
                "english": GLOSS.get(r, ""),
                "count": root_count.get(r, 0),
                "cluster": clusters[r],
            }
            for r in all_nodes
        ],
        "edges": [
            {"source": a, "target": b, "weight": w}
            for (a, b), w in sorted(edges.items(), key=lambda kv: -kv[1])
        ],
        "n_clusters": n_clusters,
    }
    out = ROOT / "notes" / "full-quran-graph"
    # Save raw data
    with (out / "data.json").open("w") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    print(f"  wrote {out / 'data.json'}  ({(out / 'data.json').stat().st_size / 1024 / 1024:.1f} MB)")

    # New cluster-aware visualization (replaces the hairball)
    write_cluster_aware_html(
        graph, out,
        title=f"Quran semantic graph — {len(all_nodes)} roots, {n_clusters} clusters",
        subtitle=f"Cluster-aware layout: each Louvain community gets its own spatial neighborhood. Singletons hidden (slider to bring back). Click cluster names to focus. Click nodes for details.",
        filename="index.html",
    )

    # Save cluster catalog as plain JSON for downstream processing
    catalog = {}
    for cid in sorted(set(clusters.values())):
        members = sorted([n for n in graph["nodes"] if n["cluster"] == cid], key=lambda x: -x["count"])
        catalog[str(cid)] = {
            "size": len(members),
            "name": CLUSTER_NAMES.get(cid),
            "members": [
                {"root": m["id"], "arabic": m["arabic"], "count": m["count"]}
                for m in members
            ],
        }
    with (out / "clusters.json").open("w") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"  wrote {out / 'clusters.json'}  ({len(catalog)} clusters)")

    # Also build the macro view (cluster super-nodes)
    cmd_macro(graph, catalog)


def cmd_macro(graph=None, catalog=None):
    """Build a macro graph: each cluster is one super-node, edges are inter-cluster sums."""
    if graph is None:
        out = ROOT / "notes" / "full-quran-graph"
        with (out / "data.json").open() as f:
            graph = json.load(f)
        with (out / "clusters.json").open() as f:
            catalog = json.load(f)

    print("\nbuilding macro view (clusters as super-nodes)...")
    # Re-resolve edge endpoints (when loading from disk they're strings)
    nodeById = {n["id"]: n for n in graph["nodes"]}
    edges = []
    for e in graph["edges"]:
        s = e["source"] if isinstance(e["source"], str) else e["source"].get("id", e["source"])
        t = e["target"] if isinstance(e["target"], str) else e["target"].get("id", e["target"])
        edges.append({"source": s, "target": t, "weight": e["weight"]})

    # Aggregate edges by cluster pair
    cluster_of = {n["id"]: n["cluster"] for n in graph["nodes"]}
    inter_edges = defaultdict(int)
    for e in edges:
        ca, cb = cluster_of[e["source"]], cluster_of[e["target"]]
        if ca == cb:
            continue
        key = tuple(sorted([ca, cb]))
        inter_edges[key] += e["weight"]

    # Build super-nodes (only clusters with size >= 3 to avoid singletons)
    super_nodes = []
    for cid_str, info in catalog.items():
        cid = int(cid_str)
        if info["size"] < 3:
            continue
        super_nodes.append({
            "id": cid,
            "name": info.get("name") or f"Cluster {cid+1}",
            "size": info["size"],
            "top_members": [m["arabic"] for m in info["members"][:5]],
            "is_named": bool(info.get("name")),
            "cluster": cid,  # for color
        })

    super_edges = []
    visible_cluster_ids = {n["id"] for n in super_nodes}
    for (a, b), w in inter_edges.items():
        if a in visible_cluster_ids and b in visible_cluster_ids and w >= 2:
            super_edges.append({"source": a, "target": b, "weight": w})

    macro_graph = {
        "nodes": super_nodes,
        "edges": super_edges,
        "n_clusters": len(super_nodes),
    }
    print(f"  macro: {len(super_nodes)} super-nodes, {len(super_edges)} inter-cluster edges")

    out = ROOT / "notes" / "full-quran-graph"
    with (out / "macro-data.json").open("w") as f:
        json.dump(macro_graph, f, ensure_ascii=False, indent=2)

    # Render as a simpler HTML (smaller graph, can use SVG)
    write_macro_html(macro_graph, out)


MACRO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Macro view — Quran cluster connections</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif; margin: 0; background: #0a0d12; color: #e8e8e8; overflow: hidden; }
  .header { padding: 14px 22px; background: #131720; border-bottom: 1px solid #232938; }
  .header h1 { margin: 0; font-size: 17px; font-weight: 600; color: #fff; }
  .header p { margin: 4px 0 0 0; font-size: 12px; color: #8a93a3; }
  .header a { color: #5b8def; text-decoration: none; }
  .header a:hover { text-decoration: underline; }
  #graph { width: 100vw; height: calc(100vh - 70px); }
  .node { cursor: pointer; }
  .node-label { fill: #fff; font-size: 12px; font-weight: 500; pointer-events: none; text-anchor: middle; }
  .node-meta { fill: #8a93a3; font-size: 10px; pointer-events: none; text-anchor: middle; font-family: "SF Arabic", "Geeza Pro", system-ui, serif; }
  .link { stroke: rgba(180,190,210,0.25); }
  .link:hover { stroke: rgba(180,190,210,0.8); }
</style>
</head>
<body>
<div class="header">
  <h1>Macro view — clusters as super-nodes</h1>
  <p>Each circle is one Louvain cluster from the full Quran graph. Size = number of roots. Edges = total ayah-level connections between clusters. <a href="index.html">← back to detail view</a></p>
</div>
<svg id="graph"></svg>
<script>
const data = __DATA__;
const palette = ["#5b8def","#ff5e5b","#22c55e","#fbbf24","#a855f7","#ec4899","#06b6d4","#84cc16","#f97316","#818cf8","#14b8a6","#facc15","#c084fc","#34d399","#0ea5e9","#f87171","#7c3aed","#a3e635","#fb923c","#22d3ee","#f472b6","#10b981","#d946ef","#eab308","#3b82f6"];
const sortedNodes = [...data.nodes].sort((a,b) => b.size - a.size);
const colorMap = {};
sortedNodes.forEach((n, i) => { colorMap[n.id] = palette[i % palette.length]; });

const svg = d3.select("#graph");
const width = window.innerWidth;
const height = window.innerHeight - 70;
svg.attr("viewBox", `0 0 ${width} ${height}`);
const g = svg.append("g");
svg.call(d3.zoom().scaleExtent([0.3, 4]).on("zoom", e => g.attr("transform", e.transform)));

const sim = d3.forceSimulation(data.nodes)
  .force("link", d3.forceLink(data.edges).id(d => d.id).distance(d => 200 - Math.min(150, Math.sqrt(d.weight)*3)).strength(d => Math.min(0.4, Math.log(d.weight)/30)))
  .force("charge", d3.forceManyBody().strength(d => -800 - d.size * 30))
  .force("center", d3.forceCenter(width/2, height/2))
  .force("collision", d3.forceCollide().radius(d => 6 + Math.sqrt(d.size) * 5));

const link = g.append("g").selectAll("line").data(data.edges).join("line").attr("class", "link").attr("stroke-width", d => Math.sqrt(d.weight) * 0.4);
const node = g.append("g").selectAll("g").data(data.nodes).join("g").attr("class", "node")
  .call(d3.drag()
    .on("start", (e, d) => { if (!e.active) sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
    .on("drag", (e, d) => { d.fx = e.x; d.fy = e.y; })
    .on("end", (e, d) => { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));

node.append("circle")
  .attr("r", d => 6 + Math.sqrt(d.size) * 4)
  .attr("fill", d => colorMap[d.id])
  .attr("fill-opacity", d => d.is_named ? 0.95 : 0.5)
  .attr("stroke", d => d.is_named ? "#fff" : "#8a93a3")
  .attr("stroke-width", d => d.is_named ? 2 : 1);

node.append("text").attr("class", "node-label")
  .attr("dy", d => -(8 + Math.sqrt(d.size) * 4) - 6)
  .text(d => d.is_named ? d.name : `(unnamed, ${d.size} roots)`);
node.append("text").attr("class", "node-meta")
  .attr("dy", d => (8 + Math.sqrt(d.size) * 4) + 14)
  .text(d => d.top_members.slice(0,3).join(" · "));
node.append("title").text(d => `${d.name}\n${d.size} roots\n` + d.top_members.join(", "));

sim.on("tick", () => {
  link.attr("x1", d => d.source.x).attr("y1", d => d.source.y).attr("x2", d => d.target.x).attr("y2", d => d.target.y);
  node.attr("transform", d => `translate(${d.x},${d.y})`);
});
</script>
</body>
</html>
"""


def write_macro_html(macro_graph, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    html = MACRO_HTML.replace("__DATA__", json.dumps(macro_graph, ensure_ascii=False))
    (out_dir / "macro.html").write_text(html, encoding="utf-8")
    print(f"  wrote {out_dir / 'macro.html'}")


def cmd_cognition_plus():
    """14 cognitive roots + their structural neighbors."""
    print("loading corpus...")
    ayah_roots, root_count, root_arabic = load_corpus()
    print("finding non-cognitive roots that co-occur with 3+ cognitive roots (freq >= 30)...")
    neighbors = find_neighbors(COG14, ayah_roots, root_count, min_freq=30, min_cog_links=3)
    print(f"  found {len(neighbors)} candidate neighbors")
    print(f"  top 15 by cognitive-link count:")
    for n in neighbors[:15]:
        print(f"    {root_arabic[n['root']]:6} ({n['root']:5})  count={n['count']:5}  cog_links={n['cog_links']}/14  shared_ayahs={n['co_count']}")
    # Include top 30 neighbors
    extras = [n["root"] for n in neighbors[:30]]
    full = COG14 + extras
    print(f"\nbuilding graph ({len(full)} roots: 14 cognitive + 30 neighbors)...")
    graph = build_graph_data(full, ayah_roots, root_count, root_arabic)
    # Mark cognitive roots specially
    cog_set = set(COG14)
    for n in graph["nodes"]:
        n["is_cognitive_seed"] = n["id"] in cog_set
    print(f"  nodes: {len(graph['nodes'])}, edges: {len(graph['edges'])}, clusters: {graph['n_clusters']}")
    out = ROOT / "notes" / "cognition" / "graph-plus"
    write_html(
        graph, out,
        title="Cognition + neighbors co-occurrence graph",
        subtitle=f"14 original cognitive roots + 30 frequent neighbors (roots co-occurring with ≥3 cognitive roots, freq ≥30). Use this to spot cognitive roots that may have been missed in the original selection.",
    )


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_graph.py {cognition|cognition-plus|custom}")
    mode = sys.argv[1]
    if mode == "cognition":
        cmd_cognition()
    elif mode == "cognition-plus":
        cmd_cognition_plus()
    elif mode == "all":
        min_w = int(sys.argv[2]) if len(sys.argv) > 2 else 2
        cmd_all(min_edge_weight=min_w)
    else:
        sys.exit(f"unknown mode: {mode}")


if __name__ == "__main__":
    main()
