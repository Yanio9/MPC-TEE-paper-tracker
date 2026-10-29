# Agent guidance: MPC-TEE-paper-tracker

This is Yanio9's independent personal MPC / TEE tracker. Modify only this repository. Do not open upstream PRs, push to upstream, import the original FL cache, or restore generic federated-learning queries.

The LICENSE file is MIT (copyright 2026 Yuwen Yang). Preserve that notice and the README provenance. The old upstream AGENTS.md incorrectly said Apache; the license file is authoritative.

## Architecture

Python 3.11+, requests, PyYAML; standard-library XML parsing and unittest. Entry point: `python -m src.main`. All paths resolve against the repository or the explicit output directory, not the shell working directory.

- `src/sources.py`: independent DBLP, arXiv Atom, ePrint OAI-PMH collectors. DBLP defaults to its official SPARQL API, with a selectable legacy search backend. Paginate distinct publication IDs before joining authors; never count author rows as papers. Fully paginate or report failure. Never silently truncate results or treat errors as empty responses.
- `src/core.py`: topic rules, acronym disambiguation, identity merge. DOI, normalized title, stable source IDs and aliases prevent cross-source and version duplicates. Retain both topic labels and all source links.
- `src/runner.py`: one transaction per source; update last-success only after the source completes. Preserve a failed source's checkpoint and continue other sources. First success per source creates a quiet baseline.
- `src/catalog.py`: direct title/venue/year/material tables, a complete single-page HTML catalog, and marker-based README updates. The user explicitly prefers the original Awesome-FL direct-list layout; do not replace it with a page-count index or numbered pagination. Keep every matching paper visible in the complete list.
- `src/output.py`: update the README paper block, `PAPERS.md`, `docs/index.html` and `reports/`. Preserve README content outside the generated markers. Only remove obsolete generated archive filenames inside `papers/`, never personal notes.
- `src/enrichment.py`: optional Crossref abstracts and optional Qwen translations; missing credentials must not break tracking. Never log credentials.
- `scripts/publish_digest.py`: own-repository Issue notifications with recoverable paper-ID markers.

## Behavior

Both MPC and TEE always scan independently. No primary-keyword gating. Generic FL is excluded; a paper that also matches MPC/TEE is included unless the explicit FL exclusion is enabled. Avoid standalone MPC/TEE/SEV/TDX matches without appropriate context.

The publication-year floor is fixed at `tracking.start_year: 2020`, with upper bound `current_year + years_ahead` (default +1). It must not roll forward with the current year. Preprints initially backfill from January 1 of that year, then use the previous successful update date minus a 3-day overlap. Exclude preprints originally submitted before the start year even when recently revised. Historical arXiv queries are partitioned by submission year. Explicit `--since` backfills are quiet and must not queue historical notifications. Revisions update metadata, not new-paper notifications.

Keep DBLP request pacing at least 6 seconds plus 0.5–2.5 seconds jitter, and arXiv/ePrint at least 3 seconds. Respect Retry-After. Do not solve or bypass anti-bot challenges. Automatic runs refresh the daily window at most once per day; explicitly requested historical backfills may query an older disjoint date interval on the same day. An explicit user-requested immediate refresh uses --refresh (workflow input refresh: true), retaining normal pacing and existing checkpoints while rechecking the incremental window. Retain completed coverage_start checkpoints and skip repeated same-day backfills that are already covered unless refresh was explicitly requested.

The daily action runs at 01:17 UTC / 09:17 Asia/Shanghai, with contents and issues write permissions only. Use ordinary pushes, never force pushes. Persist the notification queue before posting Issues; detect already-posted markers on retry. Do not interpolate paper metadata into shell code.

`pages.yml` publishes only this repository's generated `docs/` to GitHub Pages. It uses contents:read, pages:write and id-token:write. The workflow_run trigger is necessary because data commits made with GITHUB_TOKEN do not trigger a new push workflow. Always checkout main for deployment. GitHub truncates README rendering beyond 500 KiB; retain the full README tables and provide the complete single-page site rather than silently omitting papers. Keep full usage and source provenance in GUIDE.md.

## Validation

Run `python -m unittest discover -s tests -v` after behavioral changes. Add meaningful regression cases for classification, independent source execution, pagination, checkpoint failure, deduplication or notification recovery. Use a separate `--output-dir` for live probes. Network failure is not a successful zero-result test. `--dry-run` must not write any cache, output or notification files.

Keep README.md and TECHNICAL.md synchronized with actual behavior. No subagents are required for this project.
