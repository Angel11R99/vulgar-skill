#!/usr/bin/env python3
"""Validate catalog JSON files and report term counts. Read-only, stdlib only."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"es/dominican.json", "es/mexican.json", "es/spanish.json", "es/argentinian.json", "es/colombian.json", "es/venezuelan.json", "es/other-regions.json", "en/american.json", "en/british.json", "en/australian.json"}


def validate(directory):
    root = Path(directory)
    errors, files, total = [], [], 0
    found = {p.relative_to(root).as_posix() for p in root.glob("*/*.json")}
    for missing in sorted(REQUIRED - found):
        errors.append("missing required catalog: " + missing)
    for path in sorted(root.glob("*/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            assert data.get("language") in ("en", "es") and data.get("region") and isinstance(data.get("terms"), list)
            terms = data["terms"]
            words = [item["term"].strip().casefold() for item in terms]
            assert all(words) and len(words) == len(set(words)), "empty or duplicate terms"
            assert all(item.get("intensity") in ("mild", "moderate", "strong") for item in terms), "invalid intensity"
            assert len(terms) >= 5, "catalog needs at least five terms"
            files.append((path, len(terms)))
            total += len(terms)
        except (ValueError, AssertionError, KeyError, TypeError) as error:
            errors.append("{}: {}".format(path, error))
    return errors, files, total


if __name__ == "__main__":
    errors, files, total = validate(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "catalogs")
    for path, count in files:
        print("{}: {} terms".format(path, count))
    print("Total: {} terms across {} catalogs".format(total, len(files)))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
