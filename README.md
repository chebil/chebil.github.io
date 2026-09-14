# chebil.github.io

Everything published at <https://chebil.github.io> — the personal site, the
blog, the course notes, and two interactive textbooks — built from this one
repository by a single workflow.

## What lives where

| Path | Tool | Publishes to |
|---|---|---|
| `site/` | Jekyll (minimal-mistakes) | `/` — bio, blog, course pages, slide decks |
| `books/ai/` | MyST MD | `/AI-course-book/` — *Artificial Intelligence: A Textbook* |
| `books/stat/` | MyST MD | `/stat/` — *Probability and Statistics for Computer Science* |
| `tools/` | — | `build-site.sh`, which builds all three |
| `.github/workflows/deploy.yml` | GitHub Actions | builds and publishes the whole thing |

Two sites are **not** here and keep their own repositories:
[AI-slides](https://github.com/chebil/AI-slides) (Slidev, embedded in `/ai/`)
and [BigData](https://github.com/chebil/BigData). They publish to
`/AI-slides/` and `/BigData/` as project pages.

## Building

Everything, the way CI does it, into `out/`:

    tools/build-site.sh
    tools/build-site.sh --serve      # then open http://localhost:8000

Serving at the root matters: production serves from the domain root, so this
is the only local arrangement where `/stat/` and `/AI-course-book/` resolve
exactly as they will live.

One caveat when clicking around locally — course pages need the `.html`
suffix (`/DataStructure/chap1.html`). GitHub Pages adds it for you; Python's
`http.server` does not.

### One piece at a time

    cd site       && bundle exec jekyll serve --livereload
    cd books/ai   && myst start
    cd books/stat && myst start

`myst start` gives a live-reloading preview. Install it once with
`npm install -g mystmd`.

### Use Ruby 3.1

Not 3.2 or later. Jekyll 3.9 pulls in Liquid 4.0.3, which calls
`Object#tainted?` — removed in Ruby 3.2. On a newer Ruby the build dies part
way through rendering the posts. CI pins 3.1 for the same reason.

Python dependencies are per book (`books/*/requirements.txt`) and are only
needed to *run* the notebooks. CI never executes them; it renders the outputs
already stored in each `.ipynb`.

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
