# Quran Semantic Graph — Web app

Interactive Next.js app for the Quran research project. Renders the full 1,642-root co-occurrence graph via Sigma.js (WebGL), with per-cluster and per-root pages that pull in the markdown research notes.

## Run locally

```bash
cd web
npm install   # only first time
npm run dev
```

Open <http://localhost:3000>.

## What's where

```
web/
├── public/data/
│   ├── data.json              ← graph nodes + edges
│   ├── clusters.json          ← cluster catalog (15 named + 651 detected)
│   └── macro-data.json        ← cluster super-node graph
├── content/
│   ├── clusters/              ← 15 named-cluster analyses (markdown)
│   ├── cognition/             ← 14 cognition-root analyses
│   └── mercy/                 ← rḥm analysis
└── src/
    ├── app/
    │   ├── page.tsx                    ← main graph page (client)
    │   ├── cluster/[id]/page.tsx       ← per-cluster page (server)
    │   ├── root/[id]/page.tsx          ← per-root page (server)
    │   └── clusters/page.tsx           ← cluster index
    ├── components/
    │   ├── graph/sigma-graph.tsx       ← Sigma.js WebGL graph
    │   ├── cluster-legend.tsx          ← collapsible left sidebar
    │   ├── node-detail-sheet.tsx       ← right-side node details
    │   ├── search-command.tsx          ← Cmd+K search palette
    │   ├── header.tsx                  ← top header (client)
    │   ├── header-static.tsx           ← top header (server pages)
    │   ├── graph-controls.tsx          ← filters (sheet)
    │   └── ui/                         ← shadcn primitives
    └── lib/
        ├── types.ts
        ├── cluster-names.ts            ← cluster ID → name mapping
        ├── cluster-colors.ts           ← color palette
        ├── data-loader.ts              ← client-side fetching
        └── utils.ts                    ← cn helper
```

## Refreshing data after Python pipeline updates

If the Python pipeline regenerates `notes/full-quran-graph/`, copy the updates back into `web/`:

```bash
# from project root
cp notes/full-quran-graph/data.json web/public/data/
cp notes/full-quran-graph/clusters.json web/public/data/
cp notes/full-quran-graph/macro-data.json web/public/data/
cp notes/full-quran-graph/clusters/*.md web/content/clusters/
cp notes/cognition/*.md web/content/cognition/
cp notes/mercy/*.md web/content/mercy/
```

## Routes

- `/` — interactive graph
- `/clusters` — cluster catalog (cards)
- `/cluster/[id]` — per-cluster page (members + markdown analysis)
- `/root/[id]` — per-root page (top co-occurrences + concept analysis if exists)

## Keyboard shortcuts

- `⌘K` / `Ctrl+K` — open search palette
