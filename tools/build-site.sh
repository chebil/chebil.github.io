#!/usr/bin/env bash
#
# Build the whole site the way .github/workflows/deploy.yml does, into out/.
# Keep this script and that workflow in step.
#
#   tools/build-site.sh           build into out/
#   tools/build-site.sh --serve   build, then serve out/ at http://localhost:8000
#
# Serving at the root is the point: production serves from the domain root,
# so this is the only local arrangement where the sub-paths resolve exactly
# as they will live.

set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
ROOT="$PWD"
OUT="$ROOT/out"

echo "==> Static pages and assets -> out/"
rm -rf "$OUT"
mkdir -p "$OUT"
cp -r static/. "$OUT/"

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
cp -r books/ai/_build/html/.       "$OUT/AI-course-book/"
cp -r books/stat/_build/html/.     "$OUT/stat/"
cp -r courses/cs2311/_build/html/. "$OUT/DataStructure/"
cp -r courses/cs3401/_build/html/. "$OUT/AlgDesign/"
cp -r courses/cs602/_build/html/.  "$OUT/ProbSolvers/"

python3 tools/make_post_redirects.py

echo "==> Checking the assembled tree"
missing=0
for p in \
  index.html \
  images/bio.jpg \
  assets/downloads/diagnostic_chatbot.py \
  ai/index.html \
  DataStructure/index.html \
  DataStructure/chap1/index.html \
  DataStructure/Labs/Lab1.html \
  DataStructure/labs/lab1/index.html \
  AlgDesign/chap7/index.html \
  AlgDesign/convex-hull/index.html \
  ProbSolvers/chap1/index.html \
  AI-course-book/index.html \
  AI-course-book/ch13-integration/index.html \
  AI-course-book/ch05-firstorder-diagnosis/index.html \
  stat/index.html \
  stat/part1/ch01-datasets/index.html \
  stat/part1/ch01_datasets.html \
  ConvexHull/index.html \
  DiagnosisFOL/index.html
do
  if [ ! -f "$OUT/$p" ]; then echo "  MISSING $p"; missing=1; fi
done
[ "$missing" -eq 0 ] || { echo "assembly incomplete"; exit 1; }

echo "==> Built $(find "$OUT" -type f | wc -l) files into out/"

if [ "${1:-}" = "--serve" ]; then
  echo
  echo "Serving http://localhost:8000/ -- use trailing slashes on project"
  echo "pages (/DataStructure/chap1/). GitHub Pages redirects the bare form;"
  echo "python's http.server does not."
  echo
  cd "$OUT" && exec python3 -m http.server 8000
fi
