#!/usr/bin/env python3
"""Check raw episode language prompts for asset suffix leaks and label mismatch."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from franka_wrist_camera_scene.simvla.language_audit import audit_episode_prompts, audit_verified_episode_prompts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit saved raw episode language prompts.")
    parser.add_argument("collection_roots", nargs="*", type=Path)
    parser.add_argument(
        "--raw-exact-report",
        type=Path,
        help="Audit only source episodes referenced by a raw_exact_verification_report.json file.",
    )
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.raw_exact_report is not None:
        findings = audit_verified_episode_prompts(args.raw_exact_report)
    else:
        if not args.collection_roots:
            raise SystemExit("Provide at least one collection root or --raw-exact-report.")
        findings = audit_episode_prompts(args.collection_roots)
    payload = [finding.to_dict() for finding in findings]
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        if not findings:
            print("Language prompt audit passed.")
        for finding in findings:
            print(f"{finding.episode_dir}: {finding.reason}: {finding.instruction}")
    if findings:
        sys.exit(1)


if __name__ == "__main__":
    main()
