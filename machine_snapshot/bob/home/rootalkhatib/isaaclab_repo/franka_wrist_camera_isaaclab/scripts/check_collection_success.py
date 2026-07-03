#!/usr/bin/env python3
"""Strict success checker for data collection episodes."""

import argparse
import json
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Check collection success.")
    parser.add_argument(
        "collection_dir", type=str, help="Directory containing collection episodes."
    )
    parser.add_argument(
        "--allow-failures",
        action="store_true",
        help="Do not exit nonzero if failures exist.",
    )
    args = parser.parse_args()

    collection_path = Path(args.collection_dir)
    if not collection_path.exists() or not collection_path.is_dir():
        print(
            f"Error: Collection directory does not exist: {collection_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Find all episode meta.json files
    meta_paths = sorted(collection_path.glob("*/meta.json"))
    if not meta_paths:
        print(
            f"No episode meta.json files found in {collection_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    has_failures = False
    missing_failure_json = False
    malformed_meta = False

    print(f"Checking collection success in: {collection_path}")
    print("Episodes and status:")
    for meta_path in meta_paths:
        episode_dir = meta_path.parent
        episode_id = episode_dir.name
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            success = bool(meta.get("success", False))
            status_str = "SUCCESS" if success else "FAILED"
            print(f"  Episode {episode_id}: {status_str}")

            if not success:
                has_failures = True
                # Check for failure.json
                failure_json_path = episode_dir / "failure.json"
                if not failure_json_path.exists():
                    print(
                        f"    Error: Failed episode {episode_id} is missing failure.json at {failure_json_path}",
                        file=sys.stderr,
                    )
                    missing_failure_json = True
                else:
                    print(f"    failure.json: {failure_json_path}")
        except (json.JSONDecodeError, OSError) as e:
            print(
                f"  Episode {episode_id}: ERROR parsing meta.json ({e})",
                file=sys.stderr,
            )
            malformed_meta = True

    if malformed_meta:
        print("Validation FAILED: One or more episodes had malformed meta.json.", file=sys.stderr)
        sys.exit(1)

    if missing_failure_json:
        print(
            "Error: Missing failure.json for one or more failed episodes.",
            file=sys.stderr,
        )
        sys.exit(1)

    if has_failures and not args.allow_failures:
        print("Validation FAILED: One or more episodes failed.", file=sys.stderr)
        sys.exit(1)

    print("Validation PASSED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
