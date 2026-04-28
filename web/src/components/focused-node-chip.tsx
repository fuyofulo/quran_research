"use client";

import { useMemo } from "react";
import { X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { CLUSTER_NAMES } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import type { ClustersData, GraphNode } from "@/lib/types";

interface Props {
  node: GraphNode;
  clusters: ClustersData;
  onOpenDetails: () => void;
  onClear: () => void;
}

/** Floating chip at the top of the graph showing the currently-focused node
    + a button to open the full details panel. Click X to clear focus. */
export function FocusedNodeChip({ node, clusters, onOpenDetails, onClear }: Props) {
  const rank = useMemo(() => {
    const sorted = Object.entries(clusters).sort((a, b) => b[1].size - a[1].size);
    return sorted.findIndex(([cid]) => parseInt(cid) === node.cluster);
  }, [clusters, node.cluster]);

  const color = clusterColor(rank);
  const clusterName = CLUSTER_NAMES[node.cluster] ?? `Cluster ${node.cluster + 1}`;

  return (
    <div className="fixed top-20 left-1/2 -translate-x-1/2 z-30 flex items-center gap-2 rounded-full border border-border/40 bg-background/95 backdrop-blur-md shadow-lg px-2 py-1.5">
      <span
        className="ml-1 h-2.5 w-2.5 rounded-full"
        style={{ backgroundColor: color }}
        aria-hidden
      />
      <span className="font-arabic text-lg leading-none" dir="rtl">{node.arabic}</span>
      <code className="text-[10px] text-muted-foreground font-mono">{node.id}</code>
      {node.english && (
        <span className="text-xs text-muted-foreground">— {node.english}</span>
      )}
      <span className="text-[10px] text-muted-foreground tabular-nums">
        {node.count} occ
      </span>
      <span className="hidden sm:inline text-[10px] text-muted-foreground/70">·</span>
      <span className="hidden sm:inline text-[10px] text-muted-foreground truncate max-w-[180px]">
        {clusterName}
      </span>
      <Button
        size="sm"
        variant="default"
        className="ml-2 h-7 text-xs"
        onClick={onOpenDetails}
      >
        Open details →
      </Button>
      <Button
        size="icon"
        variant="ghost"
        className="h-7 w-7"
        onClick={onClear}
        title="Clear selection"
      >
        <X className="h-3.5 w-3.5" />
      </Button>
    </div>
  );
}
