"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import Graph from "graphology";
import Sigma from "sigma";
import { packSiblings } from "d3-hierarchy";
import type { GraphData, GraphNode } from "@/lib/types";
import { clusterColor, hexAlpha } from "@/lib/cluster-colors";
import { CLUSTER_NAMES } from "@/lib/cluster-names";

interface Props {
  data: GraphData;
  minClusterSize?: number;
  edgeWeightThreshold?: number;
  highlightCluster?: number | null;
  highlightNode?: string | null;
  onNodeClick?: (node: GraphNode) => void;
  onClusterClick?: (clusterId: number) => void;
  onBackgroundClick?: () => void;
}

interface NodeAttrs {
  x: number;
  y: number;
  size: number;
  color: string;
  label: string;
  cluster: number;
  count: number;
  english: string;
  arabic: string;
  root: string;
  hidden?: boolean;
  highlighted?: boolean;
  zIndex?: number;
}

interface EdgeAttrs {
  size: number;
  color: string;
  weight: number;
  hidden?: boolean;
}

export function SigmaGraph({
  data,
  minClusterSize = 3,
  edgeWeightThreshold = 5,
  highlightCluster = null,
  highlightNode = null,
  onNodeClick,
  onClusterClick,
  onBackgroundClick,
}: Props) {
  const containerRef = useRef<HTMLDivElement>(null);
  const sigmaRef = useRef<Sigma | null>(null);
  const graphRef = useRef<Graph | null>(null);
  // sigmaReady state triggers overlay components to mount AFTER sigma init,
  // so their event listeners on sigma + camera attach properly.
  const [sigmaReady, setSigmaReady] = useState(false);

  // Stable cluster ranking and centroids (computed once per dataset)
  const layoutData = useMemo(() => {
    const clusterMembers = new Map<number, GraphNode[]>();
    for (const n of data.nodes) {
      if (!clusterMembers.has(n.cluster)) clusterMembers.set(n.cluster, []);
      clusterMembers.get(n.cluster)!.push(n);
    }

    const sortedClusters = [...clusterMembers.keys()].sort(
      (a, b) => clusterMembers.get(b)!.length - clusterMembers.get(a)!.length
    );

    const clusterRank = new Map<number, number>();
    sortedClusters.forEach((c, i) => clusterRank.set(c, i));

    // Pack cluster bubbles tightly using d3.packSiblings.
    // Each cluster's circle radius scales with sqrt(member count) so
    // larger clusters get more area. packSiblings produces a non-overlapping
    // arrangement with no wasted space — much better than a Fibonacci spiral
    // when the cluster count distribution is uneven.
    const packInputs = sortedClusters.map((c) => {
      const size = clusterMembers.get(c)!.length;
      // Larger floor so even singleton clusters have room
      return { id: c, r: Math.max(10, Math.sqrt(size) * 12) };
    });
    const packed = packSiblings(packInputs);
    // Center the packed bundle on (0,0)
    const xs = packed.map((p) => p.x);
    const ys = packed.map((p) => p.y);
    const cxOff = (Math.max(...xs) + Math.min(...xs)) / 2;
    const cyOff = (Math.max(...ys) + Math.min(...ys)) / 2;
    const centroids = new Map<number, { x: number; y: number; r: number; rank: number }>();
    packed.forEach((p, i) => {
      centroids.set(p.id, {
        x: p.x - cxOff,
        y: p.y - cyOff,
        r: p.r,
        rank: i,
      });
    });

    return { clusterMembers, sortedClusters, clusterRank, centroids };
  }, [data]);

  // Initialize Sigma graph (runs once per data change)
  useEffect(() => {
    if (!containerRef.current) return;

    const graph = new Graph<NodeAttrs, EdgeAttrs>({ multi: false });
    const { clusterRank, centroids, clusterMembers } = layoutData;

    // Group members per cluster so we can pack them in spiral within each.
    // This produces deterministic, cluster-respecting positions without
    // relying on a force layout (which would re-merge clusters).
    const PHI = Math.PI * (3 - Math.sqrt(5));
    const clusterPosIndex = new Map<number, number>();

    for (const n of data.nodes) {
      const centroid = centroids.get(n.cluster)!;
      const idx = (clusterPosIndex.get(n.cluster) ?? 0);
      clusterPosIndex.set(n.cluster, idx + 1);

      // Sunflower (vogel) distribution within cluster's radius
      const total = clusterMembers.get(n.cluster)!.length;
      const t = (idx + 0.5) / total;
      const r = centroid.r * Math.sqrt(t);
      const angle = idx * PHI;

      graph.addNode(n.id, {
        x: centroid.x + Math.cos(angle) * r,
        y: centroid.y + Math.sin(angle) * r,
        size: Math.max(1.8, Math.log(n.count + 1) * 1.6),
        color: clusterColor(clusterRank.get(n.cluster)!),
        label: n.arabic,
        cluster: n.cluster,
        count: n.count,
        english: n.english,
        arabic: n.arabic,
        root: n.id,
      });
    }

    // Add edges (no force layout will move them — purely visual)
    for (const e of data.edges) {
      const sId = typeof e.source === "string" ? e.source : e.source.id;
      const tId = typeof e.target === "string" ? e.target : e.target.id;
      if (graph.hasNode(sId) && graph.hasNode(tId)) {
        try {
          graph.addEdge(sId, tId, {
            size: Math.min(2.5, Math.sqrt(e.weight) * 0.3),
            color: hexAlpha("#aab5c5", 0.12),
            weight: e.weight,
          });
        } catch {
          // duplicate edge — ignore
        }
      }
    }

    // Create Sigma instance — WebGL renderer
    const sigma = new Sigma(graph, containerRef.current, {
      labelColor: { color: "#ffffff" },
      labelFont: '"SF Arabic", "Geeza Pro", "Noto Naskh Arabic", "Amiri", system-ui, serif',
      labelSize: 13,
      labelWeight: "500",
      labelDensity: 0.45,
      labelGridCellSize: 60,
      defaultEdgeColor: hexAlpha("#aab5c5", 0.1),
      defaultNodeColor: "#666",
      renderEdgeLabels: false,
      minCameraRatio: 0.05,
      maxCameraRatio: 50,
      defaultDrawNodeLabel: (context, settings, data) => {
        if (!data.label) return;
        const size = settings.labelSize;
        context.font = `${settings.labelWeight} ${size}px ${settings.labelFont}`;
        const w = context.measureText(data.label).width;
        const x = data.x + data.size + 4;
        const y = data.y + size / 3;
        // background pill
        context.fillStyle = "rgba(10,13,18,0.85)";
        context.fillRect(x - 3, y - size + 2, w + 6, size + 2);
        context.fillStyle = "#ffffff";
        context.fillText(data.label, x, y);
      },
    });

    // Click handlers
    sigma.on("clickNode", ({ node }) => {
      const attrs = graph.getNodeAttributes(node);
      onNodeClick?.({
        id: node,
        arabic: attrs.arabic,
        english: attrs.english,
        count: attrs.count,
        cluster: attrs.cluster,
      });
    });

    sigma.on("clickStage", () => {
      onBackgroundClick?.();
    });

    // Hover effects: dim non-neighbors
    let hoveredNode: string | null = null;
    sigma.on("enterNode", ({ node }) => {
      hoveredNode = node;
      sigma.refresh({ skipIndexation: true });
    });
    sigma.on("leaveNode", () => {
      hoveredNode = null;
      sigma.refresh({ skipIndexation: true });
    });

    // Reducer functions for highlight state
    sigma.setSetting("nodeReducer", (node, data) => {
      const res = { ...data };
      if (hoveredNode) {
        const isNeighbor = node === hoveredNode || graph.areNeighbors(node, hoveredNode);
        if (!isNeighbor) {
          res.color = hexAlpha(data.color, 0.18);
          res.label = "";
        } else {
          res.zIndex = 1;
        }
      }
      return res;
    });

    sigma.setSetting("edgeReducer", (edge, data) => {
      const res = { ...data };
      if (hoveredNode && !graph.hasExtremity(edge, hoveredNode)) {
        res.hidden = true;
      }
      return res;
    });

    sigmaRef.current = sigma;
    graphRef.current = graph;
    setSigmaReady(true);

    // Center camera on full graph after a brief delay (allow layout to settle)
    setTimeout(() => {
      const camera = sigma.getCamera();
      camera.animatedReset({ duration: 300 });
    }, 100);

    return () => {
      setSigmaReady(false);
      sigma.kill();
      sigmaRef.current = null;
      graphRef.current = null;
    };
  }, [data, layoutData, onNodeClick, onBackgroundClick]);

  // Apply filters when they change
  useEffect(() => {
    const sigma = sigmaRef.current;
    const graph = graphRef.current;
    if (!sigma || !graph) return;

    const { clusterMembers } = layoutData;

    sigma.setSetting("nodeReducer", (node, data) => {
      const res = { ...data };
      const clusterSize = clusterMembers.get(data.cluster)?.length ?? 0;
      // Filter by cluster size
      if (clusterSize < minClusterSize) {
        res.hidden = true;
        return res;
      }
      // Cluster highlight: dim non-cluster nodes
      if (highlightCluster !== null && data.cluster !== highlightCluster) {
        res.color = hexAlpha(data.color, 0.12);
        res.label = "";
      }
      // Node focus: keep selected + neighbors visible. HIDE everything else.
      // (Alpha-dimming via rgba colors is unreliable in Sigma WebGL — hiding is
      // more cooperative with the renderer and gives clearer visual feedback.)
      if (highlightNode) {
        if (node === highlightNode) {
          res.zIndex = 3;
          res.size = Math.max(data.size, 9);
          res.label = data.arabic;
        } else if (graph.hasNode(highlightNode) && graph.areNeighbors(highlightNode, node)) {
          res.zIndex = 2;
          res.size = Math.max(data.size, data.size * 1.2);
        } else {
          res.hidden = true;
        }
      }
      return res;
    });

    sigma.setSetting("edgeReducer", (edge, data) => {
      const res = { ...data };
      // By default: hide ALL edges. Only show when something is focused
      // (cluster click or node hover). 28k edges drawn at once washes out
      // the entire visualization. Edges should be a "drill-in" feature.
      if (highlightCluster === null && !highlightNode) {
        res.hidden = true;
        return res;
      }
      // Filter weak edges
      if (data.weight < edgeWeightThreshold) {
        res.hidden = true;
        return res;
      }
      // Hide edges between hidden nodes
      const sCluster = graph.getNodeAttribute(graph.source(edge), "cluster");
      const tCluster = graph.getNodeAttribute(graph.target(edge), "cluster");
      const sHidden = (clusterMembers.get(sCluster)?.length ?? 0) < minClusterSize;
      const tHidden = (clusterMembers.get(tCluster)?.length ?? 0) < minClusterSize;
      if (sHidden || tHidden) {
        res.hidden = true;
        return res;
      }
      // Cluster focus mode: only show edges touching that cluster
      if (highlightCluster !== null) {
        if (sCluster !== highlightCluster && tCluster !== highlightCluster) {
          res.hidden = true;
          return res;
        }
        if (sCluster === highlightCluster && tCluster === highlightCluster) {
          res.color = hexAlpha("#ffffff", 0.18);
        } else {
          res.color = hexAlpha("#ffffff", 0.08);
        }
      }
      // Node focus mode: only edges touching the node
      if (highlightNode) {
        if (graph.source(edge) !== highlightNode && graph.target(edge) !== highlightNode) {
          res.hidden = true;
          return res;
        }
        res.color = hexAlpha("#ffffff", 0.4);
        res.size = Math.max(res.size, 1.5);
      }
      return res;
    });

    sigma.refresh({ skipIndexation: true });
  }, [minClusterSize, edgeWeightThreshold, highlightCluster, highlightNode, layoutData]);

  // Camera fly-to when highlightNode changes (search-pan)
  useEffect(() => {
    const sigma = sigmaRef.current;
    const graph = graphRef.current;
    if (!sigma || !graph || !highlightNode || !graph.hasNode(highlightNode)) return;

    const attrs = graph.getNodeAttributes(highlightNode);
    const camera = sigma.getCamera();
    camera.animate(
      { x: attrs.x, y: attrs.y, ratio: 0.15 },
      { duration: 600 }
    );
  }, [highlightNode]);

  // Camera focus on cluster
  useEffect(() => {
    const sigma = sigmaRef.current;
    const graph = graphRef.current;
    if (!sigma || !graph || highlightCluster === null) return;

    const centroid = layoutData.centroids.get(highlightCluster);
    if (!centroid) return;
    const camera = sigma.getCamera();
    camera.animate(
      { x: centroid.x, y: centroid.y, ratio: 0.4 },
      { duration: 600 }
    );
  }, [highlightCluster, layoutData.centroids]);

  return (
    <div className="relative w-full h-full">
      {/* Cluster glow layer (BEHIND sigma canvas) */}
      {sigmaReady && (
        <ClusterGlowOverlay
          sigmaRef={sigmaRef}
          layoutData={layoutData}
          minClusterSize={minClusterSize}
          highlightCluster={highlightCluster}
        />
      )}
      {/* Sigma WebGL canvas */}
      <div ref={containerRef} className="sigma-container absolute inset-0" />
      {/* Cluster name labels (ABOVE sigma canvas) */}
      {sigmaReady && (
        <ClusterLabelsOverlay
          sigmaRef={sigmaRef}
          layoutData={layoutData}
          minClusterSize={minClusterSize}
          highlightCluster={highlightCluster}
          onClusterClick={onClusterClick}
        />
      )}
    </div>
  );
}

/* Subtle radial-gradient glow behind each cluster, rendered as positioned
   <div>s that follow the Sigma camera. Sits behind the sigma canvas
   (which is transparent) so nodes appear inside the glow regions. */
function ClusterGlowOverlay({
  sigmaRef,
  layoutData,
  minClusterSize,
  highlightCluster,
}: {
  sigmaRef: React.RefObject<Sigma | null>;
  layoutData: {
    clusterMembers: Map<number, GraphNode[]>;
    sortedClusters: number[];
    clusterRank: Map<number, number>;
    centroids: Map<number, { x: number; y: number; r: number; rank: number }>;
  };
  minClusterSize: number;
  highlightCluster: number | null;
}) {
  const [, force] = useState(0);
  useEffect(() => {
    const sigma = sigmaRef.current;
    if (!sigma) return;
    const camera = sigma.getCamera();
    const handler = () => force((v) => v + 1);
    camera.on("updated", handler);
    sigma.on("afterRender", handler);
    return () => {
      camera.off("updated", handler);
      sigma.off("afterRender", handler);
    };
  }, [sigmaRef]);

  const sigma = sigmaRef.current;
  if (!sigma) return null;

  const camera = sigma.getCamera();
  // Approximate scale: viewport pixels per graph unit
  // Sigma's ratio = how many graph units fit per viewport unit; lower = zoomed in
  const dims = sigma.getDimensions();
  const baseSize = Math.min(dims.width, dims.height);
  const scale = baseSize / camera.ratio / 12; // empirical factor for nice glow size

  // Only render the highlighted cluster's glow. Rendering all 70+ glows
  // simultaneously creates a grey wash everywhere (alpha compositing of
  // many overlapping radial gradients = grey). The default look should be
  // pure dark with crisp cluster bubbles.
  if (highlightCluster === null) return null;
  const centroid = layoutData.centroids.get(highlightCluster);
  const members = layoutData.clusterMembers.get(highlightCluster);
  if (!centroid || !members || members.length < minClusterSize) return null;

  const screen = sigma.graphToViewport({ x: centroid.x, y: centroid.y });
  const screenR = centroid.r * scale * 2;
  const rank = layoutData.clusterRank.get(highlightCluster)!;
  const color = clusterColor(rank);

  return (
    <div className="pointer-events-none absolute inset-0 z-0">
      <div
        className="absolute rounded-full transition-opacity duration-300"
        style={{
          left: screen.x - screenR,
          top: screen.y - screenR,
          width: screenR * 2,
          height: screenR * 2,
          background: `radial-gradient(circle, ${hexAlpha(color, 0.45)} 0%, ${hexAlpha(color, 0.18)} 35%, transparent 75%)`,
          filter: "blur(4px)",
        }}
      />
    </div>
  );
}

function ClusterLabelsOverlay({
  sigmaRef,
  layoutData,
  minClusterSize,
  highlightCluster,
  onClusterClick,
}: {
  sigmaRef: React.RefObject<Sigma | null>;
  layoutData: {
    clusterMembers: Map<number, GraphNode[]>;
    sortedClusters: number[];
    clusterRank: Map<number, number>;
    centroids: Map<number, { x: number; y: number; r: number; rank: number }>;
  };
  minClusterSize: number;
  highlightCluster: number | null;
  onClusterClick?: (clusterId: number) => void;
}) {
  const [, force] = useState(0);
  const overlayRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const sigma = sigmaRef.current;
    if (!sigma) return;
    const camera = sigma.getCamera();
    const handler = () => force((v) => v + 1);
    camera.on("updated", handler);
    sigma.on("afterRender", handler);
    return () => {
      camera.off("updated", handler);
      sigma.off("afterRender", handler);
    };
  }, [sigmaRef]);

  const sigma = sigmaRef.current;
  if (!sigma) return null;

  return (
    <div ref={overlayRef} className="pointer-events-none absolute inset-0 z-10">
      {[...layoutData.centroids.entries()].map(([clusterId, centroid]) => {
        const members = layoutData.clusterMembers.get(clusterId)!;
        if (members.length < minClusterSize) return null;
        if (!CLUSTER_NAMES[clusterId]) return null;
        if (highlightCluster !== null && clusterId !== highlightCluster) return null;

        const screen = sigma.graphToViewport({ x: centroid.x, y: centroid.y });
        const rank = layoutData.clusterRank.get(clusterId)!;
        return (
          <button
            key={clusterId}
            type="button"
            onClick={() => onClusterClick?.(clusterId)}
            className="pointer-events-auto absolute -translate-x-1/2 -translate-y-1/2 whitespace-nowrap rounded-md border border-white/10 bg-black/70 px-2 py-1 text-xs font-semibold backdrop-blur-sm transition hover:bg-black/90 hover:border-white/30"
            style={{
              left: screen.x,
              top: screen.y,
              color: clusterColor(rank),
            }}
          >
            {CLUSTER_NAMES[clusterId]}
          </button>
        );
      })}
    </div>
  );
}
