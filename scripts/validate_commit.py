#!/usr/bin/env python3
"""Validate Conventional Commit header and profanity intensity; read-only."""
import argparse
import re
import sys
from pathlib import Path
from generate_commit import catalogs

HEADER = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([\w.-]+\))?(!)?: .+")


def validate(message, catalog_dir, intensity):
    errors = []
    first = message.strip().splitlines()[0] if message.strip() else ""
    if not HEADER.match(first):
        errors.append("header does not match Conventional Commits format")
    terms = {term["term"].casefold() for catalog in catalogs(catalog_dir) for term in catalog["terms"]}
    count = sum(1 for term in terms if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", message.casefold()))
    required = {"low": 1, "medium": 2, "high": 2}[intensity]
    if count < required:
        errors.append("{} intensity requires at least {} catalog profanity term(s); found {}".format(intensity, required, count))
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message")
    parser.add_argument("--catalog-dir", type=Path, default=Path(__file__).resolve().parents[1] / "catalogs")
    parser.add_argument("--intensity", choices=("low", "medium", "high"), default="high")
    args = parser.parse_args()
    errors = validate(args.message, args.catalog_dir, args.intensity)
    print("\n".join(errors) if errors else "Commit message is valid")
    sys.exit(bool(errors))
