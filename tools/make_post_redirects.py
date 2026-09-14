#!/usr/bin/env python3
"""Keep the URLs of blog posts that became book and course pages.

These were Jekyll posts published at the site root, e.g. /ConvexHull/.
They were never really blog posts -- each one expands on a specific
chapter -- so they now live inside the project they belong to. The old
URLs are public, so each keeps a stub pointing at its new home.

Run after the site and the MyST projects are assembled into out/:

    python tools/make_post_redirects.py
"""
from __future__ import annotations

import os
import sys

OUT = "out"

MOVED = {
    # old post URL          new home
    "ConvexHull":         "/AlgDesign/convex-hull/",
    "subsets":            "/AlgDesign/subsets/",
    "permutations":       "/AlgDesign/permutations/",
    "exponentiation":     "/AlgDesign/exponentiation/",
    "MaximumSubSequence": "/AlgDesign/maximum-subsequence/",
    "Searching":          "/AI-course-book/ch02-search-libraries/",
    "DiagnosisFOL":       "/AI-course-book/ch05-firstorder-diagnosis/",
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


def main() -> int:
    if not os.path.isdir(OUT):
        sys.exit(f"{OUT} not found -- build the site first")

    written = 0
    for slug, target in MOVED.items():
        if not os.path.isdir(os.path.join(OUT, target.strip("/"))):
            print(f"  ::warning::{target} does not exist in the build")
        # Jekyll published these as a directory with an index.
        dest = os.path.join(OUT, slug, "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as fh:
            fh.write(STUB.format(target=target))
        print(f"  /{slug}/ -> {target}")
        written += 1

    print(f"wrote {written} post redirect stubs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
