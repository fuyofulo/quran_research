"use client";

import { useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import type { ClustersData } from "@/lib/types";
import { CLUSTER_NAMES } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import { cn } from "@/lib/utils";

interface Props {
  clusters: ClustersData;
  highlightCluster: number | null;
  onSelectCluster: (id: number | null) => void;
  onOpenCluster?: (id: number) => void;
}

export function ClusterLegend({ clusters, highlightCluster, onSelectCluster, onOpenCluster }: Props) {
  const [open, setOpen] = useState(true);

  // Build sorted list with rank assigned by size
  const entries = Object.entries(clusters)
    .map(([id, info]) => ({ id: parseInt(id), ...info }))
    .sort((a, b) => b.size - a.size);

  // Assign rank for color
  const rankMap = new Map<number, number>();
  entries.forEach((e, i) => rankMap.set(e.id, i));

  const named = entries.filter((e) => e.size >= 3 && CLUSTER_NAMES[e.id]);
  const unnamed = entries.filter((e) => e.size >= 3 && !CLUSTER_NAMES[e.id]);

  return (
    <>
      <Button
        size="icon"
        variant="outline"
        className={cn(
          "fixed left-4 top-20 z-30 h-9 w-9 transition-opacity bg-background/90 backdrop-blur",
          open && "pointer-events-none opacity-0"
        )}
        onClick={() => setOpen(true)}
        title="Show legend"
      >
        <ChevronRight className="h-4 w-4" />
      </Button>
      <aside
        className={cn(
          "fixed left-4 top-20 z-20 flex h-[calc(100vh-6rem)] w-72 flex-col rounded-lg border border-border/40 bg-background/85 backdrop-blur-md shadow-lg transition-transform",
          !open && "-translate-x-[calc(100%+2rem)]"
        )}
      >
        <div className="flex items-center justify-between p-3 pb-2">
          <div>
            <div className="text-sm font-semibold">Clusters</div>
            <div className="text-xs text-muted-foreground">
              {entries.length} total · {named.length} named
            </div>
          </div>
          <Button
            size="icon"
            variant="ghost"
            className="h-7 w-7"
            onClick={() => setOpen(false)}
            title="Hide legend"
          >
            <ChevronLeft className="h-4 w-4" />
          </Button>
        </div>
        <Separator />
        <ScrollArea className="flex-1">
          <div className="px-2 py-2">
            <div className="mb-2 px-2 text-[10px] uppercase tracking-wide text-muted-foreground">
              Named clusters (deep-analyzed)
            </div>
            {named.map((c) => (
              <ClusterRow
                key={c.id}
                id={c.id}
                name={CLUSTER_NAMES[c.id]!}
                size={c.size}
                preview={c.members.slice(0, 3).map((m) => m.arabic).join(" · ")}
                color={clusterColor(rankMap.get(c.id)!)}
                active={highlightCluster === c.id}
                onClick={() => onSelectCluster(highlightCluster === c.id ? null : c.id)}
                onOpen={() => onOpenCluster?.(c.id)}
              />
            ))}
            {unnamed.length > 0 && (
              <>
                <div className="mt-4 mb-2 px-2 text-[10px] uppercase tracking-wide text-muted-foreground">
                  Other detected clusters
                </div>
                {unnamed.map((c) => (
                  <ClusterRow
                    key={c.id}
                    id={c.id}
                    name={`Cluster ${c.id + 1}`}
                    size={c.size}
                    preview={c.members.slice(0, 3).map((m) => m.arabic).join(" · ")}
                    color={clusterColor(rankMap.get(c.id)!)}
                    active={highlightCluster === c.id}
                    dim
                    onClick={() => onSelectCluster(highlightCluster === c.id ? null : c.id)}
                  />
                ))}
              </>
            )}
          </div>
        </ScrollArea>
      </aside>
    </>
  );
}

function ClusterRow({
  name,
  size,
  preview,
  color,
  active,
  dim,
  onClick,
  onOpen,
}: {
  id: number;
  name: string;
  size: number;
  preview: string;
  color: string;
  active: boolean;
  dim?: boolean;
  onClick: () => void;
  onOpen?: () => void;
}) {
  return (
    <div
      className={cn(
        "group mb-1 flex cursor-pointer items-start gap-2 rounded-md px-2 py-2 transition hover:bg-muted/60",
        active && "bg-muted/80 ring-1 ring-primary/50",
        dim && "opacity-60"
      )}
      onClick={onClick}
    >
      <div
        className="mt-1 h-3 w-3 flex-shrink-0 rounded-full"
        style={{ backgroundColor: color }}
      />
      <div className="flex-1 min-w-0">
        <div className="text-xs font-medium leading-tight truncate">{name}</div>
        <div className="text-[10px] text-muted-foreground leading-tight">
          {size} roots · <span dir="rtl" className="font-arabic">{preview}</span>
        </div>
      </div>
      {onOpen && (
        <Button
          size="sm"
          variant="ghost"
          className="h-6 px-2 text-[10px] opacity-0 group-hover:opacity-100"
          onClick={(e) => {
            e.stopPropagation();
            onOpen();
          }}
        >
          Open →
        </Button>
      )}
    </div>
  );
}
