# chebil.github.io

Everything published at <https://chebil.github.io> — the homepage, two course
sites, and two interactive textbooks — built from this one repository by a
single workflow.

## What lives where

| Path | Tool | Publishes to |
|---|---|---|
| `static/` | plain HTML | `/` — the homepage, `/images/`, `/assets/` |
| `books/ai/` | MyST MD | `/AI-course-book/` — *Artificial Intelligence: A Textbook* |
| `books/stat/` | MyST MD | `/stat/` — *Probability and Statistics for Computer Science* |
| `courses/cs2311/` | MyST MD | `/DataStructure/` — Data Structures |
| `courses/cs3401/` | MyST MD | `/AlgDesign/` — Algorithm Design |
| `tools/` | — | `build-site.sh`, which builds everything |
| `.github/workflows/deploy.yml` | GitHub Actions | builds and publishes the whole thing |

[AI-slides](https://github.com/chebil/AI-slides) is not here -- it keeps its
own repository and publishes to `/AI-slides/` as a project page, linked from
the homepage.

[BigData](https://github.com/chebil/BigData) also still publishes to
`/BigData/`, but nothing links to it any more. To take it offline, disable
Pages on that repository.

### This repository is the source of truth

The two textbooks were separate repositories until 2026 and were brought in
with `git subtree`, so their full history is here. **Do not edit
[AI-course-book](https://github.com/chebil/AI-course-book) or
[stat](https://github.com/chebil/stat) any more.** Pages is already disabled
on both, so nothing published there reaches the site; a commit made in
either one is simply lost work.

That has happened once. The AI book was first imported from a stale local
`main`, and 21 commits were left behind -- the per-chapter presentation
slides among them. It was only noticed because the slides were visibly
missing from the site. Recovering it meant a `git subtree pull` and a
hand-resolved toc conflict.

Archiving both repositories closes that door for good. They were kept live
as a rollback path during the merge; that window has passed. Until they are
archived, fetch before assuming a local clone is current:

    git -C ../AI-course-book fetch origin && git -C ../AI-course-book log --oneline -1 origin/main

## Building

Everything, the way CI does it, into `out/`:

    tools/build-site.sh
    tools/build-site.sh --serve      # then open http://localhost:8000

Serving at the root matters: production serves from the domain root, so this
is the only local arrangement where `/stat/` and `/AI-course-book/` resolve
exactly as they will live.

One caveat when clicking around locally — use trailing slashes
(`/DataStructure/chap1/`). GitHub Pages 301s the bare form to it; Python's
`http.server` does not.

### One piece at a time

    cd books/ai       && myst start
    cd books/stat     && myst start
    cd courses/cs2311 && myst start

`myst start` gives a live-reloading preview. Install it once with
`npm install -g mystmd`.


## How publishing works

One repository means one GitHub Pages deployment, so every run builds all
three projects and assembles them into a single artifact. Before uploading,
the workflow asserts that eight representative pages exist — a partial tree
fails the build instead of going live.

The deploy job runs only from the default branch and never from a pull
request. That is deliberate: `workflow_dispatch` on a feature branch builds
and uploads an artifact you can download and inspect, without touching the
live site.

### Why there are no path filters

It is tempting to skip the book builds when only a blog post changed. Don't.
A Pages deployment replaces the entire site, so an artifact built without the
books would publish a site without them. The whole build is about 80 seconds,
of which the two books are 24 — not worth the risk.

### The statistics book's old URLs

It was a Jupyter Book until 2026, published as `/stat/part1/ch01_datasets.html`.
MyST publishes `/stat/part1/ch01-datasets/` instead. `books/stat/scripts/make_redirects.py`
writes a stub at each of the 46 old paths so existing links keep resolving,
and the workflow runs it after every build.

Two settings keep the rest stable, and they differ between the books on
purpose:

- `books/stat/myst.yml` sets `site.options.folders: true`, preserving the
  `part1/part2/part3` structure its old URLs used.
- `books/ai/myst.yml` must **not** set it. That book has always been MyST and
  its live URLs are already flat — adding it would break every one of them.

### Course pages and case

The three courses were Jekyll pages with explicit permalinks until 2026.
MyST derives each URL from the file path and **lowercases every segment**, so
`Labs/Lab1.md` publishes at `/DataStructure/labs/lab1/`, not
`/DataStructure/Labs/Lab1`. Renaming the source directory does not change
this — the lowercasing is unconditional.

Chapter pages are unaffected, because Pages 301s `/DataStructure/chap1` to
`/DataStructure/chap1/` by itself. Only the seven lab pages change, and
`tools/make_course_redirects.py` writes a stub for each. It derives them from
the toc, so adding a lab with a capitalised name is handled automatically.

Two more things to know when editing course markdown:

- **Never use absolute links.** MyST prefixes `BASE_URL` to anything starting
  with `/`, including inside raw HTML, so `](/AlgDesign/chap1)` becomes
  `/AlgDesign/AlgDesign/chap1`. Link within a course by source file
  (`](chap1.md)`), and to the Jekyll side by full URL
  (`](https://chebil.github.io/ConvexHull)`).
- **Keep images inside the course.** A course cannot reach `site/assets/`;
  put images in its own `images/` directory and reference them relatively.

### There is no site generator any more

`static/` is plain HTML, copied verbatim into the build. The homepage is a
single self-contained file; there is no theme, no Ruby, and no Gemfile.

That removes the last of the minimal-mistakes fork, and with it the blog:
no `feed.xml`, no `sitemap.xml`, no post layouts. Every post turned out to
be chapter material and now lives in the relevant project, with
`tools/make_post_redirects.py` keeping the old URLs working.

If a real blog is ever wanted again, it needs a generator adding back --
this is a one-way door, taken deliberately.
