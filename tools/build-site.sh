#!/usr/bin/env bash
#
# Build the whole site the way .github/workflows/deploy.yml does, into out/.
# Keep this script and that workflow in step -- the cutover procedure relies
# on the local build matching what CI publishes.
#
#   tools/build-site.sh           build into out/
#   tools/build-site.sh --serve   build, then serve out/ at http://localhost:8000
#
# Serving at the root is the point: production serves the site from the
# domain root, so this is the only local arrangement where the books'
# /stat/ and /AI-course-book/ paths resolve exactly as they will live.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
ROOT="$PWD"
OUT="$ROOT/out"

# Jekyll 3.9 pulls Liquid 4.0.3, which calls Object#tainted?. Ruby 3.2
# removed it. CI pins 3.1; locally you need the same or the build dies
# part way through rendering the posts.
ruby_major_minor=$(ruby -e 'print RUBY_VERSION[/\d+\.\d+/]' 2>/dev/null || echo "none")
if [ "$ruby_major_minor" != "3.1" ]; then
  echo "warning: Ruby $ruby_major_minor found, CI uses 3.1."
  echo "         3.2+ fails on Object#tainted? while rendering posts."
fi

echo "==> Jekyll site -> out/"
rm -rf "$OUT"
( cd site && JEKYLL_ENV=production bundle exec jekyll build --destination "$OUT" --baseurl "" )

echo "==> AI book -> out/AI-course-book/"
( cd books/ai && BASE_URL=/AI-course-book myst build --html )

echo "==> Statistics book -> out/stat/"
( cd books/stat && BASE_URL=/stat myst build --html && python3 scripts/make_redirects.py )

echo "==> Courses -> out/DataStructure|AlgDesign|ProbSolvers/"
( cd courses/cs2311 && BASE_URL=/DataStructure myst build --html )
( cd courses/cs3401 && BASE_URL=/AlgDesign     myst build --html )
( cd courses/cs602  && BASE_URL=/ProbSolvers   myst build --html )
python3 tools/make_course_redirects.py

mkdir -p "$OUT/AI-course-book" "$OUT/stat" \
         "$OUT/DataStructure" "$OUT/AlgDesign" "$OUT/ProbSolvers"
cp -r books/ai/_build/html/.      "$OUT/AI-course-book/"
cp -r books/stat/_build/html/.    "$OUT/stat/"
# Courses are copied over the Jekyll output, not instead of it: the two
# reveal.js decks still come from Jekyll and live inside these paths.
cp -r courses/cs2311/_build/html/. "$OUT/DataStructure/"
cp -r courses/cs3401/_build/html/. "$OUT/AlgDesign/"
cp -r courses/cs602/_build/html/.  "$OUT/ProbSolvers/"

python3 tools/make_post_redirects.py

echo "==> Checking the assembled tree"
missing=0
for p in \
  index.html \
  feed.xml \
  DataStructure/index.html \
  DataStructure/chap1/index.html \
  DataStructure/Labs/Lab1.html \
  DataStructure/labs/lab1/index.html \
  AlgDesign/chap7/index.html \
  ProbSolvers/chap1/index.html \
  ProbSolvers/slideschap2.html \
  AlgDesign/convex-hull/index.html \
  AI-course-book/ch05-firstorder-diagnosis/index.html \
  ConvexHull/index.html \
  DiagnosisFOL/index.html \
  AI-course-book/index.html \
  AI-course-book/ch13-integration/index.html \
  stat/index.html \
  stat/part1/ch01-datasets/index.html \
  stat/part1/ch01_datasets.html
do
  if [ ! -f "$OUT/$p" ]; then echo "  MISSING $p"; missing=1; fi
done
[ "$missing" -eq 0 ] || { echo "assembly incomplete"; exit 1; }

echo "==> Built $(find "$OUT" -type f | wc -l) files into out/"

if [ "${1:-}" = "--serve" ]; then
  echo
  echo "Serving http://localhost:8000/ -- note that python's http.server does"
  echo "not redirect /DataStructure/chap1 to /DataStructure/chap1/ the way"
  echo "GitHub Pages does. Use the trailing slash locally."
  echo
  cd "$OUT" && exec python3 -m http.server 8000
fi
