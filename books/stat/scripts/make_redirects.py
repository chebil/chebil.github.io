#!/usr/bin/env python3
"""Write redirect stubs for the URLs the Jupyter Book site used to publish.

Jupyter Book 0.15 published one file per page, keeping the source name:

    /stat/part1/ch01_datasets.html

MyST publishes a directory per page, with a slugified name:

    /stat/part1/ch01-datasets/

Every deep link into the old site would break. This drops a small HTML
stub at each old path pointing at the new one, so existing links -- in
syllabi, LMS entries, bookmarks -- keep resolving.

Targets are RELATIVE, so the stubs work under any base path: locally at
`/`, in production at `/stat/`.

Run after `myst build --html`:

    python scripts/make_redirects.py
"""
from __future__ import annotations

import os
import sys
import yaml

BUILD = "_build/html"

STUB = """<!doctype html>
<meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex">
<script>location.replace("{target}");</script>
<p>This page has moved to <a href="{target}">{target}</a>.</p>
"""


def walk(entries):
    """Yield every `file:` path in a MyST toc, depth first."""
    for e in entries:
        if "file" in e:
            yield e["file"]
        for child in e.get("children", []) or []:
            yield from walk([child])


def slug(name: str) -> str:
    return name.replace("_", "-").lower()


def main() -> int:
    if not os.path.isdir(BUILD):
        sys.exit(f"{BUILD} not found -- run `myst build --html` first")

    toc = yaml.safe_load(open("myst.yml"))["project"]["toc"]
    files = list(walk(toc))
    root = files[0]

    written = 0
    for path in files:
        stem, _ = os.path.splitext(path)
        old = f"{stem}.html"
        target = "./" if path == root else f"{slug(os.path.basename(stem))}/"

        dest = os.path.join(BUILD, old)
        if os.path.exists(dest):
            print(f"  skip (real page): {old}")
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as fh:
            fh.write(STUB.format(target=target))
        written += 1

    print(f"wrote {written} redirect stubs into {BUILD}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
