"use client";

import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetDescription } from "@/components/ui/sheet";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { buttonVariants } from "@/components/ui/button";
import type { GraphData, GraphNode } from "@/lib/types";
import { CLUSTER_NAMES, CLUSTER_SLUGS } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import Link from "next/link";
import { useMemo } from "react";

interface Props {
  node: GraphNode | null;
  graph: GraphData;
  onOpenChange: (open: boolean) => void;
}

export function NodeDetailSheet({ node, graph, onOpenChange }: Props) {
  const neighbors = useMemo(() => {
    if (!node) return [];
    const nodeMap = new Map(graph.nodes.map((n) => [n.id, n]));
    const counts = new Map<string, number>();
    for (const e of graph.edges) {
      const sId = typeof e.source === "string" ? e.source : e.source.id;
      const tId = typeof e.target === "string" ? e.target : e.target.id;
      if (sId === node.id) counts.set(tId, e.weight);
      else if (tId === node.id) counts.set(sId, e.weight);
    }
    return [...counts.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, 20)
      .map(([id, weight]) => ({ node: nodeMap.get(id), weight }))
      .filter((x) => x.node);
  }, [node, graph]);

  // Cluster rank for color
  const rankMap = useMemo(() => {
    const sizes = new Map<number, number>();
    for (const n of graph.nodes) {
      sizes.set(n.cluster, (sizes.get(n.cluster) || 0) + 1);
    }
    const sorted = [...sizes.entries()].sort((a, b) => b[1] - a[1]);
    const m = new Map<number, number>();
    sorted.forEach(([id], i) => m.set(id, i));
    return m;
  }, [graph]);

  const clusterName = node ? CLUSTER_NAMES[node.cluster] ?? `Cluster ${node.cluster + 1}` : "";
  const clusterSlug = node ? CLUSTER_SLUGS[node.cluster] : null;
  const color = node ? clusterColor(rankMap.get(node.cluster)!) : "#666";

  return (
    <Sheet open={!!node} onOpenChange={onOpenChange}>
      <SheetContent side="right" className="w-96 flex flex-col p-0">
        {node && (
          <>
            <SheetHeader className="p-6 pb-4">
              <div className="flex items-center gap-2 text-xs text-muted-foreground">
                <span
                  className="inline-block h-2 w-2 rounded-full"
                  style={{ backgroundColor: color }}
                />
                <span>{clusterName}</span>
              </div>
              <SheetTitle className="font-arabic text-4xl text-foreground" dir="rtl">
                {node.arabic}
              </SheetTitle>
              <SheetDescription className="flex items-center gap-2 text-sm">
                <code className="rounded bg-muted px-1.5 py-0.5 font-mono text-xs">
                  {node.id}
                </code>
                {node.english && (
                  <span className="text-muted-foreground">— {node.english}</span>
                )}
              </SheetDescription>
              <div className="flex flex-wrap gap-2 mt-2">
                <Badge variant="secondary">{node.count} occurrences</Badge>
                {clusterSlug && (
                  <Link href={`/cluster/${node.cluster}`}>
                    <Badge variant="outline" className="cursor-pointer hover:bg-muted">
                      View cluster →
                    </Badge>
                  </Link>
                )}
              </div>
            </SheetHeader>
            <Separator />
            <ScrollArea className="flex-1 px-6 py-4">
              <div className="space-y-4">
                <div>
                  <div className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
                    Top co-occurring roots
                  </div>
                  <div className="space-y-1">
                    {neighbors.map(({ node: nb, weight }) => (
                      nb && (
                        <button
                          key={nb.id}
                          type="button"
                          className="flex w-full items-center justify-between rounded-md px-2 py-1.5 text-left transition hover:bg-muted"
                          onClick={() => {
                            // Switch to the new node by re-emitting
                            window.dispatchEvent(new CustomEvent("open-node", { detail: nb }));
                          }}
                        >
                          <div className="flex items-center gap-2 min-w-0">
                            <span
                              className="h-2 w-2 flex-shrink-0 rounded-full"
                              style={{ backgroundColor: clusterColor(rankMap.get(nb.cluster)!) }}
                            />
                            <span className="font-arabic text-base" dir="rtl">{nb.arabic}</span>
                            <code className="text-[10px] text-muted-foreground font-mono">{nb.id}</code>
                          </div>
                          <span className="text-xs text-muted-foreground tabular-nums">
                            {weight} ayahs
                          </span>
                        </button>
                      )
                    ))}
                  </div>
                </div>
              </div>
            </ScrollArea>
            <div className="border-t p-4">
              <Link
                href={`/root/${encodeURIComponent(node.id)}`}
                className={buttonVariants({ variant: "default", size: "sm" }) + " w-full"}
              >
                Open root analysis →
              </Link>
            </div>
          </>
        )}
      </SheetContent>
    </Sheet>
  );
}
