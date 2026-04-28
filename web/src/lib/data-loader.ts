import type { ClustersData, GraphData } from "./types";

let graphDataCache: GraphData | null = null;
let clustersDataCache: ClustersData | null = null;

export async function loadGraphData(): Promise<GraphData> {
  if (graphDataCache) return graphDataCache;
  const res = await fetch("/data/data.json");
  if (!res.ok) throw new Error("Failed to load graph data");
  graphDataCache = (await res.json()) as GraphData;
  return graphDataCache;
}

export async function loadClustersData(): Promise<ClustersData> {
  if (clustersDataCache) return clustersDataCache;
  const res = await fetch("/data/clusters.json");
  if (!res.ok) throw new Error("Failed to load clusters data");
  clustersDataCache = (await res.json()) as ClustersData;
  return clustersDataCache;
}
