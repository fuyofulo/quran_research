import { notFound } from "next/navigation";
import Link from "next/link";
import fs from "fs/promises";
import path from "path";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Header } from "@/components/header-static";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { CLUSTER_NAMES, CLUSTER_SLUGS } from "@/lib/cluster-names";
import { clusterColor } from "@/lib/cluster-colors";
import type { ClustersData, GraphData } from "@/lib/types";

interface Params { params: Promise<{ id: string }> }

async function loadGraph(): Promise<GraphData> {
  const file = path.join(process.cwd(), "public/data/data.json");
  return JSON.parse(await fs.readFile(file, "utf-8"));
}

async function loadClusters(): Promise<ClustersData> {
  const file = path.join(process.cwd(), "public/data/clusters.json");
  return JSON.parse(await fs.readFile(file, "utf-8"));
}

// Map root buckwalter to a probable concept-md filename
const COGNITION_ROOTS: Record<string, string> = {
  "Elm": "concept-Elm",
  "*kr": "concept-dhikr",
  "Hkm": "concept-Hkm",
  "bSr": "concept-bSr",
  "nZr": "concept-nZr",
  "sAl": "concept-sAl",
  "wjd": "concept-wjd",
  "bgy": "concept-bgy",
  "qrA": "concept-qrA",
  "Eql": "concept-Eql",
  "dbr": "concept-dbr",
  "fqh": "concept-fqh",
  "fkr": "concept-fkr",
  "lbb": "concept-lbb",
  "bHv": "concept-bHv",
};

async function loadRootNote(rootId: string): Promise<string | null> {
  // Try cognition first
  const cogSlug = COGNITION_ROOTS[rootId];
  if (cogSlug) {
    try {
      return await fs.readFile(path.join(process.cwd(), `content/cognition/${cogSlug}.md`), "utf-8");
    } catch {}
  }
  // Try mercy
  if (rootId === "rHm") {
    try {
      return await fs.readFile(path.join(process.cwd(), "content/mercy/concept-rhm.md"), "utf-8");
    } catch {}
  }
  return null;
}

export default async function RootPage({ params }: Params) {
  const { id: rootIdRaw } = await params;
  const rootId = decodeURIComponent(rootIdRaw);

  const [graph, clusters] = await Promise.all([loadGraph(), loadClusters()]);
  const node = graph.nodes.find((n) => n.id === rootId);
  if (!node) notFound();

  // Compute neighbors
  const neighborMap = new Map<string, number>();
  for (const e of graph.edges) {
    const sId = typeof e.source === "string" ? e.source : (e.source as { id: string }).id;
    const tId = typeof e.target === "string" ? e.target : (e.target as { id: string }).id;
    if (sId === rootId) neighborMap.set(tId, e.weight);
    else if (tId === rootId) neighborMap.set(sId, e.weight);
  }
  const nodeMap = new Map(graph.nodes.map((n) => [n.id, n]));
  const neighbors = [...neighborMap.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 25)
    .map(([id, w]) => ({ node: nodeMap.get(id)!, weight: w }));

  // Cluster info
  const clusterInfo = clusters[String(node.cluster)];
  const clusterName = CLUSTER_NAMES[node.cluster] ?? `Cluster ${node.cluster + 1}`;
  const clusterSlug = CLUSTER_SLUGS[node.cluster];

  // Color via rank
  const sorted = Object.entries(clusters).sort((a, b) => b[1].size - a[1].size);
  const rank = sorted.findIndex(([cid]) => parseInt(cid) === node.cluster);
  const color = clusterColor(rank);

  const note = await loadRootNote(rootId);

  return (
    <div className="min-h-screen bg-background">
      <Header />
      <div className="pt-20 px-6 pb-16 max-w-4xl mx-auto">
        <div className="mb-2">
          <Link href="/" className="text-xs text-muted-foreground hover:text-foreground">
            ← Back to graph
          </Link>
        </div>
        <div className="flex items-center gap-2 text-xs text-muted-foreground mb-2">
          <Link
            href={`/cluster/${node.cluster}`}
            className="flex items-center gap-1.5 hover:text-foreground transition"
          >
            <span
              className="h-2 w-2 rounded-full"
              style={{ backgroundColor: color }}
            />
            <span>{clusterName}</span>
          </Link>
        </div>
        <h1 className="font-arabic text-6xl font-bold mb-2" dir="rtl">{node.arabic}</h1>
        <div className="flex flex-wrap items-center gap-3 mb-6">
          <code className="rounded bg-muted px-2 py-1 font-mono text-sm">{node.id}</code>
          {node.english && <span className="text-muted-foreground">{node.english}</span>}
          <Badge variant="secondary">{node.count} occurrences</Badge>
        </div>

        <div className="mb-8 rounded-lg border bg-muted/30 p-4">
          <div className="text-xs font-semibold uppercase tracking-wide text-muted-foreground mb-3">
            Top co-occurring roots
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2">
            {neighbors.map(({ node: nb, weight }) => {
              const nbRank = sorted.findIndex(([cid]) => parseInt(cid) === nb.cluster);
              const nbColor = clusterColor(nbRank);
              return (
                <Link
                  key={nb.id}
                  href={`/root/${encodeURIComponent(nb.id)}`}
                  className="flex items-center justify-between rounded-md border bg-background px-2.5 py-1.5 text-sm transition hover:border-foreground/30"
                >
                  <div className="flex items-center gap-1.5 min-w-0">
                    <span
                      className="h-2 w-2 flex-shrink-0 rounded-full"
                      style={{ backgroundColor: nbColor }}
                    />
                    <span className="font-arabic text-base" dir="rtl">{nb.arabic}</span>
                  </div>
                  <span className="text-xs text-muted-foreground tabular-nums">{weight}</span>
                </Link>
              );
            })}
          </div>
        </div>

        {note && (
          <article className="prose prose-invert prose-sm max-w-none prose-headings:font-bold prose-h1:text-2xl prose-h2:text-xl prose-h2:mt-8 prose-h2:mb-3 prose-h3:text-lg prose-p:leading-relaxed prose-table:text-xs prose-table:my-4 prose-th:p-2 prose-td:p-2 prose-th:border prose-td:border prose-table:border-collapse prose-th:bg-muted/50">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{note}</ReactMarkdown>
          </article>
        )}
        {!note && clusterSlug && (
          <div className="text-sm text-muted-foreground">
            No deep root analysis yet — but this root belongs to{" "}
            <Link href={`/cluster/${node.cluster}`} className="underline hover:text-foreground">
              {clusterName}
            </Link>
            , which has its own analysis.
          </div>
        )}
      </div>
    </div>
  );
}
