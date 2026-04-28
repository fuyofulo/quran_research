// Vibrant palette tuned for dark backgrounds — distinguishable colors
const PALETTE = [
  "#5b8def", "#ff5e5b", "#22c55e", "#fbbf24", "#a855f7",
  "#ec4899", "#06b6d4", "#84cc16", "#f97316", "#818cf8",
  "#14b8a6", "#facc15", "#c084fc", "#34d399", "#0ea5e9",
  "#f87171", "#7c3aed", "#a3e635", "#fb923c", "#22d3ee",
  "#f472b6", "#10b981", "#d946ef", "#eab308", "#3b82f6",
];

/**
 * Color for cluster by its rank (largest cluster gets palette[0]).
 * Pass the cluster's rank (0-based, sorted by member count desc).
 */
export function clusterColor(rank: number): string {
  return PALETTE[rank % PALETTE.length];
}

/** Convert hex to rgba string with given alpha. */
export function hexAlpha(hex: string, alpha: number): string {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r},${g},${b},${alpha})`;
}
