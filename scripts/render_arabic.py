#!/usr/bin/env python3
"""Render a Markdown file (with mixed Arabic + English) to a properly
typeset HTML page and open it in the browser.

Terminals cannot stack Arabic diacritics, shape letters cursively, or
reorder bidirectional (RTL/LTR) runs. A browser does all three correctly.
This script wraps your Markdown in an HTML template with a Quranic-grade
Arabic font and automatically isolates every Arabic run with <bdi> so that
Arabic embedded inside an English sentence stays correctly ordered.

Usage:
    python3 scripts/render_arabic.py notes/some-answer.md
    python3 scripts/render_arabic.py notes/some-answer.md -o /tmp/out.html
    python3 scripts/render_arabic.py notes/some-answer.md --no-open

Supported Markdown subset (enough for analysis write-ups):
    # / ## / ###   headings
    **bold**       strong
    _italic_       emphasis
    `code`         inline code
    - item         unordered list
    ---            horizontal rule
    blank line     paragraph break
"""
import argparse
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Unicode ranges covering Arabic letters, diacritics, presentation forms,
# and Arabic punctuation. A "run" is any maximal stretch containing at least
# one of these that we isolate for correct bidi rendering.
ARABIC_CHAR = (
    r"؀-ۿ"   # Arabic
    r"ݐ-ݿ"   # Arabic Supplement
    r"ࢠ-ࣿ"   # Arabic Extended-A
    r"ﭐ-﷿"   # Arabic Presentation Forms-A
    r"ﹰ-﻿"   # Arabic Presentation Forms-B
)
# A run may include internal spaces and the tatweel/punctuation, but must
# start and end on an actual Arabic codepoint.
ARABIC_RUN = re.compile(
    rf"[{ARABIC_CHAR}](?:[{ARABIC_CHAR}\s،؛؟ـ]*[{ARABIC_CHAR}])?"
)


def wrap_arabic(text: str) -> str:
    """Isolate each Arabic run in a <bdi> so mixed RTL/LTR lines stay sane."""
    return ARABIC_RUN.sub(lambda m: f'<bdi class="ar">{m.group(0)}</bdi>', text)


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"_([^_]+)_", r"<em>\1</em>", text)
    # Arabic-wrap last so it never touches the ASCII tags we just inserted.
    return wrap_arabic(text)


def render_body(md: str) -> str:
    out: list[str] = []
    para: list[str] = []
    list_items: list[str] = []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_list():
        if list_items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in list_items) + "</ul>")
            list_items.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        if line.strip() == "---":
            flush_para(); flush_list(); out.append("<hr>"); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            flush_para(); flush_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            flush_para()
            list_items.append(m.group(1))
            continue
        flush_list()
        para.append(line.strip())

    flush_para(); flush_list()
    return "\n".join(out)


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Scheherazade+New:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #1a1816; --fg: #e8e2d8; --muted: #9a9286;
    --accent: #d98b4a; --rule: #34302b; --code: #2a2622;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    background: var(--bg); color: var(--fg);
    font: 16px/1.7 ui-sans-serif, -apple-system, "Segoe UI", system-ui, sans-serif;
    max-width: 820px; margin: 0 auto; padding: 3rem 1.5rem 6rem;
    text-rendering: optimizeLegibility;
  }}
  h1, h2, h3 {{ color: var(--accent); line-height: 1.3; margin: 2.2rem 0 .6rem; font-weight: 700; }}
  h1 {{ font-size: 1.7rem; }} h2 {{ font-size: 1.3rem; }} h3 {{ font-size: 1.08rem; }}
  p {{ margin: .7rem 0; }}
  ul {{ margin: .6rem 0; padding-inline-start: 1.3rem; }}
  li {{ margin: .35rem 0; }}
  hr {{ border: none; border-top: 1px solid var(--rule); margin: 2rem 0; }}
  em {{ color: var(--muted); font-style: italic; }}
  code {{ background: var(--code); padding: .1em .4em; border-radius: 4px; font-size: .9em; }}
  strong {{ color: #f2ede4; }}
  /* The crucial part: real Arabic typesetting. */
  .ar {{
    font-family: "Amiri", "Scheherazade New", "Noto Naskh Arabic",
                 "Geeza Pro", "SF Arabic", serif;
    direction: rtl; unicode-bidi: isolate;
    font-size: 1.55em; line-height: 2.1;
    /* Let the font place diacritics and join letters; no monospace grid. */
    font-feature-settings: "calt" 1, "liga" 1, "mark" 1, "mkmk" 1, "ccmp" 1;
  }}
  /* Standalone Arabic (a whole heading or paragraph that is only Arabic) */
  h1 .ar, h2 .ar, h3 .ar {{ font-size: 1.25em; }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Render mixed Arabic/English Markdown to HTML and open it.")
    ap.add_argument("input", help="Markdown file to render")
    ap.add_argument("-o", "--output", help="Output HTML path (default: temp file)")
    ap.add_argument("--no-open", action="store_true", help="Write HTML but do not open the browser")
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        sys.exit(f"error: no such file: {src}")
    md = src.read_text(encoding="utf-8")
    title = src.stem.replace("-", " ").replace("_", " ").title()
    htmlpage = TEMPLATE.format(title=html.escape(title), body=render_body(md))

    if args.output:
        out = Path(args.output)
    else:
        out = Path(tempfile.gettempdir()) / f"{src.stem}.render.html"
    out.write_text(htmlpage, encoding="utf-8")
    print(f"rendered -> {out}")

    if not args.no_open:
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
