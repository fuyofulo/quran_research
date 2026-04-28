// Human-readable names for the 15 thematically-analyzed clusters.
// Source: notes/full-quran-graph/clusters/cluster-NN-name.md
export const CLUSTER_NAMES: Record<number, string> = {
  4: "Revelation, Speech & Disbelief",
  8: "Allegiance & the Object of Worship",
  0: "The Believers' Reward",
  5: "The Commanded Self",
  19: "Household Law & Lineage",
  17: "Bodily Purity & Prayer",
  7: "Sea-Rescue / Bounty / Gratitude",
  90: "Sin–Mercy Economy",
  96: "Dunya vs. Ākhirah",
  11: "Vegetative Signs / Reflective Gaze",
  66: "Jihād fī Sabīl Allāh",
  62: "The Prepared Fire",
  43: "Divine Will & Dominion",
  77: "Creation & the Appointed Term",
  75: "Witnessing the Visible Sign",
};

// URL slugs matching the markdown filenames in content/clusters/
export const CLUSTER_SLUGS: Record<number, string> = {
  4: "cluster-04-revelation-and-disbelief",
  8: "cluster-08-allegiance-and-worship",
  0: "cluster-00-believers-reward",
  5: "cluster-05-commanded-self",
  19: "cluster-19-household-law",
  17: "cluster-17-bodily-purity",
  7: "cluster-07-sea-rescue",
  90: "cluster-90-sin-mercy-economy",
  96: "cluster-96-dunya-akhirah",
  11: "cluster-11-vegetative-signs",
  66: "cluster-66-jihad-fi-sabil-allah",
  62: "cluster-62-prepared-fire",
  43: "cluster-43-divine-will-dominion",
  77: "cluster-77-creation-and-term",
  75: "cluster-75-visible-sign",
};

export function clusterName(id: number, fallback?: string): string {
  return CLUSTER_NAMES[id] ?? fallback ?? `Cluster ${id + 1}`;
}

export function isNamed(id: number): boolean {
  return id in CLUSTER_NAMES;
}
