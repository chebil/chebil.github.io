# Archive — completed markdown-to-notebook migration

These documents record a one-time migration, finished in December 2025, that
converted every chapter section from Markdown to Jupyter notebooks. All 48
sections across `part1/`, `part2/` and `part3/` are notebooks now; no `.md`
source files remain.

They are kept for the record only. Nothing here describes current process.

The GitHub Actions workflow they refer to, `convert-to-notebooks.yml`, has been
removed: it converted files and **committed the result to `main` automatically**,
which is a standing risk for a migration that is already over. It remains in git
history if it is ever needed again.
