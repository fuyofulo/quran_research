import { notFound } from "next/navigation";
import Link from "next/link";
import fs from "fs/promises";
import path from "path";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Header } from "@/components/header-static";
import { Badge } from "@/components/ui/badge";
import { buttonVariants } from "@/components/ui/button";
import { CLUSTER_NAMES, CLUSTER_SLUGS } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import type { ClustersData } from "@/lib/types";

interface Params { params: Promise<{ id: string }> }

async function loadClusters(): Promise<ClustersData> {
  const file = path.join(process.cwd(), "public/data/clusters.json");
  return JSON.parse(await fs.readFile(file, "utf-8"));
}

async function loadClusterNote(id: number): Promise<string | null> {
  const slug = CLUSTER_SLUGS[id];
  if (!slug) return null;
  const file = path.join(process.cwd(), `content/clusters/${slug}.md`);
  try {
    return await fs.readFile(file, "utf-8");
  } catch {
    return null;
  }
}

export default async function ClusterPage({ params }: Params) {
  const { id: idParam } = await params;
  const id = parseInt(idParam);
  if (isNaN(id)) notFound();

  const clusters = await loadClusters();
  const info = clusters[String(id)];
  if (!info) notFound();

  const note = await loadClusterNote(id);
  const name = CLUSTER_NAMES[id] ?? `Cluster ${id + 1}`;

  // Compute color via rank
  const sorted = Object.entries(clusters).sort((a, b) => b[1].size - a[1].size);
  const rank = sorted.findIndex(([cid]) => parseInt(cid) === id);
  const color = clusterColor(rank);

  return (
    <div className="min-h-screen bg-background">
      <Header />
      <div className="pt-20 px-6 pb-16 max-w-4xl mx-auto">
        <div className="mb-2">
          <Link href="/" className="text-xs text-muted-foreground hover:text-foreground">
            ← Back to graph
          </Link>
        </div>
        <div className="flex items-center gap-3 mb-2">
          <span
            className="h-3 w-3 rounded-full flex-shrink-0"
            style={{ backgroundColor: color }}
          />
          <span className="text-xs text-muted-foreground uppercase tracking-wide">
            Cluster {id + 1}
          </span>
        </div>
        <h1 className="text-3xl font-bold mb-3">{name}</h1>
        <div className="flex flex-wrap gap-2 mb-6">
          <Badge variant="secondary">{info.size} roots</Badge>
          <Link href={`/?focus=${id}`} className={buttonVariants({ size: "sm", variant: "outline" })}>
            View on graph →
          </Link>
        </div>

        <div className="mb-8 rounded-lg border bg-muted/30 p-4">
          <div className="text-xs font-semibold uppercase tracking-wide text-muted-foreground mb-3">
            Top roots in this cluster
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2">
            {info.members.slice(0, 24).map((m) => (
              <Link
                key={m.root}
                href={`/root/${encodeURIComponent(m.root)}`}
                className="flex items-center justify-between rounded-md border bg-background px-2.5 py-1.5 text-sm transition hover:border-foreground/30"
              >
                <span className="font-arabic text-lg" dir="rtl">{m.arabic}</span>
                <span className="text-xs text-muted-foreground tabular-nums">
                  {m.count}
                </span>
              </Link>
            ))}
          </div>
          {info.members.length > 24 && (
            <div className="text-xs text-muted-foreground mt-3">
              + {info.members.length - 24} more roots
            </div>
          )}
        </div>

        {note && (
          <article className="prose prose-invert prose-sm max-w-none prose-headings:font-bold prose-h1:text-2xl prose-h2:text-xl prose-h2:mt-8 prose-h2:mb-3 prose-h3:text-lg prose-p:leading-relaxed prose-table:text-xs prose-table:my-4 prose-th:p-2 prose-td:p-2 prose-th:border prose-td:border prose-table:border-collapse prose-th:bg-muted/50">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{note}</ReactMarkdown>
          </article>
        )}
        {!note && (
          <div className="text-sm text-muted-foreground">
            No deep analysis available for this cluster yet.
          </div>
        )}
      </div>
    </div>
  );
}
