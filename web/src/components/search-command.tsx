"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
} from "@/components/ui/command";
import type { ClustersData, GraphNode } from "@/lib/types";
import { CLUSTER_NAMES } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";

interface Props {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  nodes: GraphNode[];
  clusters: ClustersData;
  onSelectNode: (node: GraphNode) => void;
  onSelectCluster: (id: number) => void;
}

export function SearchCommand({ open, onOpenChange, nodes, clusters, onSelectNode, onSelectCluster }: Props) {
  const router = useRouter();
  const [query, setQuery] = useState("");

  useEffect(() => {
    function down(e: KeyboardEvent) {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        onOpenChange(!open);
      }
    }
    document.addEventListener("keydown", down);
    return () => document.removeEventListener("keydown", down);
  }, [open, onOpenChange]);

  // Cluster rank
  const rankMap = new Map<number, number>();
  Object.entries(clusters)
    .sort((a, b) => b[1].size - a[1].size)
    .forEach(([id], i) => rankMap.set(parseInt(id), i));

  const filteredNodes = query
    ? nodes
        .filter(
          (n) =>
            n.id.toLowerCase().includes(query.toLowerCase()) ||
            n.arabic.includes(query) ||
            (n.english && n.english.toLowerCase().includes(query.toLowerCase()))
        )
        .slice(0, 30)
    : nodes.sort((a, b) => b.count - a.count).slice(0, 20);

  const namedClusters = Object.entries(clusters)
    .map(([id, c]) => ({ id: parseInt(id), ...c }))
    .filter((c) => CLUSTER_NAMES[c.id])
    .filter(
      (c) =>
        !query ||
        CLUSTER_NAMES[c.id].toLowerCase().includes(query.toLowerCase())
    )
    .sort((a, b) => b.size - a.size);

  return (
    <CommandDialog open={open} onOpenChange={onOpenChange}>
      <CommandInput
        placeholder="Search Arabic root or cluster..."
        value={query}
        onValueChange={setQuery}
      />
      <CommandList>
        <CommandEmpty>No results found.</CommandEmpty>
        {namedClusters.length > 0 && (
          <CommandGroup heading="Clusters">
            {namedClusters.map((c) => (
              <CommandItem
                key={`c-${c.id}`}
                value={`cluster-${c.id}-${CLUSTER_NAMES[c.id]}`}
                onSelect={() => {
                  onSelectCluster(c.id);
                  onOpenChange(false);
                }}
              >
                <span
                  className="h-2.5 w-2.5 rounded-full"
                  style={{ backgroundColor: clusterColor(rankMap.get(c.id)!) }}
                />
                <span className="font-medium">{CLUSTER_NAMES[c.id]}</span>
                <span className="ml-auto text-xs text-muted-foreground">
                  {c.size} roots
                </span>
              </CommandItem>
            ))}
          </CommandGroup>
        )}
        {filteredNodes.length > 0 && (
          <>
            <CommandSeparator />
            <CommandGroup heading={query ? "Roots" : "Top roots by frequency"}>
              {filteredNodes.map((n) => (
                <CommandItem
                  key={`n-${n.id}`}
                  value={`${n.id}-${n.arabic}-${n.english}`}
                  onSelect={() => {
                    onSelectNode(n);
                    onOpenChange(false);
                  }}
                >
                  <span
                    className="h-2 w-2 rounded-full"
                    style={{ backgroundColor: clusterColor(rankMap.get(n.cluster)!) }}
                  />
                  <span className="font-arabic text-base" dir="rtl">{n.arabic}</span>
                  <code className="text-[10px] text-muted-foreground font-mono">
                    {n.id}
                  </code>
                  {n.english && (
                    <span className="text-xs text-muted-foreground truncate">
                      — {n.english}
                    </span>
                  )}
                  <span className="ml-auto text-xs text-muted-foreground">
                    {n.count}
                  </span>
                </CommandItem>
              ))}
            </CommandGroup>
          </>
        )}
      </CommandList>
    </CommandDialog>
  );
}
