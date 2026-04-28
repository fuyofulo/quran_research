"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import dynamic from "next/dynamic";
import { Header } from "@/components/header";
import { ClusterLegend } from "@/components/cluster-legend";
import { NodeDetailSheet } from "@/components/node-detail-sheet";
import { SearchCommand } from "@/components/search-command";
import { GraphControls } from "@/components/graph-controls";
import { FocusedNodeChip } from "@/components/focused-node-chip";
import { loadGraphData, loadClustersData } from "@/lib/data-loader";
import type { ClustersData, GraphData, GraphNode } from "@/lib/types";

// Sigma uses WebGL; only load on the client.
const SigmaGraph = dynamic(
  () => import("@/components/graph/sigma-graph").then((m) => m.SigmaGraph),
  { ssr: false }
);

export default function Home() {
  const router = useRouter();
  const [graph, setGraph] = useState<GraphData | null>(null);
  const [clusters, setClusters] = useState<ClustersData | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [highlightCluster, setHighlightCluster] = useState<number | null>(null);
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [highlightNode, setHighlightNode] = useState<string | null>(null);
  const [searchOpen, setSearchOpen] = useState(false);
  const [minClusterSize, setMinClusterSize] = useState(3);
  const [edgeWeight, setEdgeWeight] = useState(5);

  useEffect(() => {
    Promise.all([loadGraphData(), loadClustersData()])
      .then(([g, c]) => {
        setGraph(g);
        setClusters(c);
      })
      .catch((e) => setError(String(e)));
  }, []);

  // Currently focused node (just for the header chip — not the same as selected/details)
  const [focusedNode, setFocusedNode] = useState<GraphNode | null>(null);

  // Listen for "open-node" events from neighbor clicks (these jump + show details)
  useEffect(() => {
    function handler(e: Event) {
      const ce = e as CustomEvent<GraphNode>;
      setFocusedNode(ce.detail);
      setHighlightNode(ce.detail.id);
      setSelectedNode(ce.detail);
    }
    window.addEventListener("open-node", handler);
    return () => window.removeEventListener("open-node", handler);
  }, []);

  // Clicking a node on the graph: just focus it (highlight + show connections).
  // To open the details panel, the user clicks the "Open details" button on
  // the focused-node chip (or hits Enter on the search palette).
  const handleClickNode = (n: GraphNode) => {
    setFocusedNode(n);
    setHighlightNode(n.id);
    setHighlightCluster(null);
  };

  // Open the details panel (separate from focusing)
  const handleOpenDetails = (n: GraphNode) => {
    setSelectedNode(n);
    setFocusedNode(n);
    setHighlightNode(n.id);
  };

  const handleSelectCluster = (id: number | null) => {
    setHighlightCluster(id);
    setHighlightNode(null);
    setFocusedNode(null);
    setSelectedNode(null);
  };

  const handleClearFocus = () => {
    setHighlightCluster(null);
    setHighlightNode(null);
    setFocusedNode(null);
  };

  return (
    <div className="h-screen w-screen overflow-hidden bg-background">
      <Header onSearchClick={() => setSearchOpen(true)} />
      <div className="absolute inset-0 top-14">
        {error && (
          <div className="flex h-full items-center justify-center text-destructive text-sm">
            Error: {error}
          </div>
        )}
        {!error && graph && (
          <SigmaGraph
            data={graph}
            minClusterSize={minClusterSize}
            edgeWeightThreshold={edgeWeight}
            highlightCluster={highlightCluster}
            highlightNode={highlightNode}
            onNodeClick={handleClickNode}
            onClusterClick={(id) => router.push(`/cluster/${id}`)}
            onBackgroundClick={handleClearFocus}
          />
        )}
        {!error && !graph && (
          <div className="flex h-full items-center justify-center text-muted-foreground text-sm">
            Loading graph...
          </div>
        )}
      </div>
      {clusters && graph && (
        <>
          <ClusterLegend
            clusters={clusters}
            highlightCluster={highlightCluster}
            onSelectCluster={handleSelectCluster}
            onOpenCluster={(id) => router.push(`/cluster/${id}`)}
          />
          <GraphControls
            minClusterSize={minClusterSize}
            onMinClusterSizeChange={setMinClusterSize}
            edgeWeight={edgeWeight}
            onEdgeWeightChange={setEdgeWeight}
          />
          <SearchCommand
            open={searchOpen}
            onOpenChange={setSearchOpen}
            nodes={graph.nodes}
            clusters={clusters}
            onSelectNode={handleClickNode}
            onSelectCluster={handleSelectCluster}
          />
        </>
      )}
      {graph && (
        <NodeDetailSheet
          node={selectedNode}
          graph={graph}
          onOpenChange={(open) => {
            if (!open) {
              setSelectedNode(null);
              // Note: we keep highlightNode + focusedNode so the focus persists
              // after closing the panel. Click background to fully clear.
            }
          }}
        />
      )}
      {focusedNode && (
        <FocusedNodeChip
          node={focusedNode}
          clusters={clusters}
          onOpenDetails={() => handleOpenDetails(focusedNode)}
          onClear={handleClearFocus}
        />
      )}
    </div>
  );
}
