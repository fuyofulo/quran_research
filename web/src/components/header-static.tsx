import Link from "next/link";

/** Static (server-rendered) header for content pages — no client interactivity. */
export function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 z-30 flex h-14 items-center justify-between border-b border-border/40 bg-background/80 px-4 backdrop-blur-md">
      <div className="flex items-center gap-6">
        <Link href="/" className="flex items-center gap-2">
          <div className="font-semibold text-sm">Quran semantic graph</div>
          <div className="text-xs text-muted-foreground hidden sm:block">
            1,642 roots · 666 clusters
          </div>
        </Link>
        <nav className="flex items-center gap-3 text-xs text-muted-foreground">
          <Link href="/" className="rounded-md px-2 py-1 transition hover:text-foreground">
            Graph
          </Link>
        </nav>
      </div>
    </header>
  );
}
