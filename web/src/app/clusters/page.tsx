import Link from "next/link";
import fs from "fs/promises";
import path from "path";
import { Header } from "@/components/header-static";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CLUSTER_NAMES } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import type { ClustersData } from "@/lib/types";

async function loadClusters(): Promise<ClustersData> {
  const file = path.join(process.cwd(), "public/data/clusters.json");
  return JSON.parse(await fs.readFile(file, "utf-8"));
}

export default async function ClustersIndex() {
  const clusters = await loadClusters();
  const sorted = Object.entries(clusters)
    .map(([id, info]) => ({ id: parseInt(id), ...info }))
    .sort((a, b) => b.size - a.size);

  const named = sorted.filter((c) => CLUSTER_NAMES[c.id]);

  return (
    <div className="min-h-screen bg-background">
      <Header />
      <div className="pt-20 px-6 pb-16 max-w-5xl mx-auto">
        <div className="mb-2">
          <Link href="/" className="text-xs text-muted-foreground hover:text-foreground">
            ← Back to graph
          </Link>
        </div>
        <h1 className="text-3xl font-bold mb-2">Cluster catalog</h1>
        <p className="text-muted-foreground mb-8">
          {sorted.length} Louvain communities detected across 1,642 roots. {named.length} have been thematically deep-analyzed.
        </p>

        <h2 className="text-lg font-semibold mb-4">Named clusters</h2>
        <div className="grid sm:grid-cols-2 gap-3 mb-8">
          {named.map((c, i) => {
            const color = clusterColor(i);
            return (
              <Link key={c.id} href={`/cluster/${c.id}`}>
                <Card className="transition hover:border-foreground/30 cursor-pointer">
                  <CardContent className="p-4">
                    <div className="flex items-start gap-3">
                      <span
                        className="mt-1.5 h-3 w-3 rounded-full flex-shrink-0"
                        style={{ backgroundColor: color }}
                      />
                      <div className="flex-1 min-w-0">
                        <div className="font-semibold text-sm mb-1">{CLUSTER_NAMES[c.id]}</div>
                        <div className="text-xs text-muted-foreground mb-2">
                          {c.size} roots
                        </div>
                        <div className="text-xs font-arabic text-foreground/80" dir="rtl">
                          {c.members.slice(0, 5).map((m) => m.arabic).join(" · ")}
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
