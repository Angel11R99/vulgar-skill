#!/usr/bin/env python3
"""Generate a Conventional Commit message; reads catalogs and prints one message."""
import argparse
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def catalogs(directory):
    result = []
    for path in sorted(Path(directory).glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_path"] = path.stem
        result.append(data)
    return result


def generate(description, language=None, region=None, intensity="high", previous="", catalog_dir=ROOT / "catalogs", rng=None, commit_type="chore", scope=None):
    rng = rng or random.SystemRandom()
    available = catalogs(catalog_dir)
    if language:
        available = [c for c in available if c["language"] == language]
    if region:
        available = [c for c in available if region.lower() in c["region"].lower() or region.lower() in c["_path"].lower()]
    if not available:
        raise ValueError("No catalog matches the requested language and region")
    cat = rng.choice(available)
    terms = [t for t in cat["terms"] if t["intensity"] == "mild"] if intensity == "low" else [t for t in cat["terms"] if t["intensity"] in (("mild", "moderate") if intensity == "medium" else ("strong", "moderate"))]
    count = 1 if intensity == "low" else 2
    previous_lower = previous.casefold()
    terms = [t for t in terms if t["term"].casefold() not in previous_lower] or terms
    if len(terms) < count:
        terms = [t for t in cat["terms"] if t["intensity"] in (("mild", "moderate") if intensity == "medium" else ("strong", "moderate"))]
    picked = rng.sample(terms, min(count, len(terms)))
    words = " ".join(t["term"] for t in picked)
    # Profanity is deliberately in a compact clause after the factual subject.
    header = commit_type + ("({})".format(scope) if scope else "")
    return header + ": " + description.strip().rstrip(".") + " — " + words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--description", required=True, help="Accurate technical change summary")
    parser.add_argument("--language", choices=("en", "es"))
    parser.add_argument("--region", help="Catalog region or filename fragment")
    parser.add_argument("--intensity", choices=("low", "medium", "high"), default="high")
    parser.add_argument("--previous", default="", help="Recent message to avoid repeating its profanity")
    parser.add_argument("--type", dest="commit_type", choices=("feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"), default="chore")
    parser.add_argument("--scope")
    parser.add_argument("--catalog-dir", type=Path, default=ROOT / "catalogs")
    args = parser.parse_args()
    print(generate(args.description, args.language, args.region, args.intensity, args.previous, args.catalog_dir, commit_type=args.commit_type, scope=args.scope))


if __name__ == "__main__":
    main()
