"""CLI: python -m src.main [--sources arxiv,eprint] [--dry-run]."""
import argparse
import json
import logging
from datetime import date
from pathlib import Path

from .runner import load_config, run


def main():
    parser = argparse.ArgumentParser(description="Track MPC and TEE papers across DBLP, arXiv and IACR ePrint")
    root = Path(__file__).resolve().parent.parent
    parser.add_argument("--config", type=Path, default=root / "config.yaml")
    parser.add_argument("--output-dir", type=Path, default=root, help="Root for data/, reports/ and PAPERS.md")
    parser.add_argument("--sources", default="", help="Comma-separated source names: dblp,arxiv,eprint")
    parser.add_argument("--since", type=date.fromisoformat, help="Quiet historical backfill from this date (YYYY-MM-DD); no new-paper alerts")
    parser.add_argument("--refresh", action="store_true", help="Recheck sources now even if already scanned today; retain normal request pacing")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and summarize without writing cache or files")
    parser.add_argument("--no-enrich", action="store_true", help="Skip optional Crossref/translation calls")
    args = parser.parse_args()
    selected = [item.strip() for item in args.sources.split(",") if item.strip()]
    if set(selected) - {"dblp", "arxiv", "eprint"}:
        parser.error("Unknown source in --sources")
    if args.since and args.since > date.today():
        parser.error("--since must not be in the future")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    config = load_config(args.config)
    report = run(args.output_dir.resolve(), config, selected or None, args.since, args.dry_run, no_enrich=args.no_enrich, refresh=args.refresh)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report["failed_sources"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
