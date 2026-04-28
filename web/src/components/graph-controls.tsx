"use client";

import { Sliders } from "lucide-react";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

interface Props {
  minClusterSize: number;
  onMinClusterSizeChange: (n: number) => void;
  edgeWeight: number;
  onEdgeWeightChange: (n: number) => void;
}

export function GraphControls({ minClusterSize, onMinClusterSizeChange, edgeWeight, onEdgeWeightChange }: Props) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <Button
        size="icon"
        variant="outline"
        className="fixed right-4 top-20 z-30 h-9 w-9 bg-background/90 backdrop-blur"
        title="Graph filters"
        onClick={() => setOpen(true)}
      >
        <Sliders className="h-4 w-4" />
      </Button>
      <Sheet open={open} onOpenChange={setOpen}>
        <SheetContent side="right" className="w-80 p-6">
          <SheetHeader className="mb-4 p-0">
            <SheetTitle>Graph filters</SheetTitle>
          </SheetHeader>
          <div className="space-y-6">
            <div>
              <div className="flex items-center justify-between mb-2">
                <label className="text-xs font-medium">
                  Cluster min size
                </label>
                <span className="text-xs tabular-nums text-muted-foreground">
                  {minClusterSize}
                </span>
              </div>
              <input
                type="range"
                min="1"
                max="50"
                value={minClusterSize}
                onChange={(e) => onMinClusterSizeChange(parseInt(e.target.value))}
                className="w-full"
              />
              <p className="mt-1 text-[10px] text-muted-foreground">
                Hide clusters with fewer than this many roots. Default 3 (cuts singleton noise).
              </p>
            </div>
            <div>
              <div className="flex items-center justify-between mb-2">
                <label className="text-xs font-medium">
                  Edge weight ≥
                </label>
                <span className="text-xs tabular-nums text-muted-foreground">
                  {edgeWeight} ayahs
                </span>
              </div>
              <input
                type="range"
                min="2"
                max="100"
                value={edgeWeight}
                onChange={(e) => onEdgeWeightChange(parseInt(e.target.value))}
                className="w-full"
              />
              <p className="mt-1 text-[10px] text-muted-foreground">
                Hide edges weaker than this. Default 5 (keeps meaningful connections).
              </p>
            </div>
          </div>
        </SheetContent>
      </Sheet>
    </>
  );
}
