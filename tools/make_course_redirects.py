#!/usr/bin/env python3
"""Write redirect stubs for course URLs whose shape MyST changed.

These pages were Jekyll pages with explicit permalinks, e.g.

    /DataStructure/Labs/Lab1

MyST derives the URL from the file path and lowercases every segment, so
`Labs/Lab1.md` publishes as:

    /DataStructure/labs/lab1/

GitHub Pages is case sensitive, so the old link 404s. For the plain
chapter pages there is nothing to do -- Pages 301s `/DataStructure/chap1`
to `/DataStructure/chap1/` on its own -- so a stub is written only where
the old and new paths genuinely differ.

Run after `myst build --html`, from the repository root:

    python tools/make_course_redirects.py
"""
from __future__ import annotations

import os
import sys
import yaml

# course directory -> published base path
COURSES = {
    "courses/cs2311": "/DataStructure",
    "courses/cs3401": "/AlgDesign",
}

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
    for e in entries:
        if "file" in e:
            yield e["file"]
        for child in e.get("children") or []:
            yield from walk([child])


def main() -> int:
    total = 0
    for course, base in COURSES.items():
        build = os.path.join(course, "_build", "html")
        if not os.path.isdir(build):
            sys.exit(f"{build} not found -- run `myst build --html` in {course} first")

        toc = yaml.safe_load(open(os.path.join(course, "myst.yml")))["project"]["toc"]
        for rel in walk(toc):
            stem, _ = os.path.splitext(rel)
            if stem == "index":
                continue
            new = "/".join(p.lower() for p in stem.split("/"))
            if new == stem:
                continue  # Pages resolves this one by itself

            # Stub sits at the old path with a .html suffix, so Pages serves
            # it directly rather than redirecting into it first.
            dest = os.path.join(build, stem + ".html")
            depth = stem.count("/")
            target = "../" * depth + new + "/"

            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "w") as fh:
                fh.write(STUB.format(target=target))
            print(f"  {base}/{stem} -> {base}/{new}/")
            total += 1

    print(f"wrote {total} course redirect stubs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
