"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Search } from "lucide-react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";

interface Props {
  onSearchClick: () => void;
}

export function Header({ onSearchClick }: Props) {
  const pathname = usePathname();

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
          <NavLink href="/" active={pathname === "/"}>Graph</NavLink>
          <NavLink href="/clusters" active={pathname.startsWith("/clusters") || pathname.startsWith("/cluster")}>Clusters</NavLink>
        </nav>
      </div>
      <div className="flex items-center gap-2">
        <Button
          variant="outline"
          size="sm"
          className="h-8 gap-2 text-muted-foreground"
          onClick={onSearchClick}
        >
          <Search className="h-3.5 w-3.5" />
          <span className="hidden sm:inline">Search root...</span>
          <kbd className="hidden sm:inline ml-1 rounded border bg-muted px-1.5 py-0.5 text-[10px] font-mono">
            ⌘K
          </kbd>
        </Button>
      </div>
    </header>
  );
}

function NavLink({ href, active, children }: { href: string; active: boolean; children: React.ReactNode }) {
  return (
    <Link
      href={href}
      className={cn(
        "rounded-md px-2 py-1 transition hover:text-foreground",
        active && "text-foreground bg-muted"
      )}
    >
      {children}
    </Link>
  );
}
