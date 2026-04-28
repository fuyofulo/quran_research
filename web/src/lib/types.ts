export interface GraphNode {
  id: string;
  arabic: string;
  english: string;
  count: number;
  cluster: number;
}

export interface GraphEdge {
  source: string | { id: string };
  target: string | { id: string };
  weight: number;
}

export interface GraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
  n_clusters: number;
}

export interface ClusterMember {
  root: string;
  arabic: string;
  count: number;
}

export interface ClusterInfo {
  size: number;
  name: string | null;
  members: ClusterMember[];
}

export type ClustersData = Record<string, ClusterInfo>;
