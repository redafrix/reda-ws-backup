#!/usr/bin/env python3
"""Recompute reaching success metrics for one saved episode."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from franka_wrist_camera_scene.simvla.reaching_diagnostics import diagnose_reaching_episode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Diagnose reaching success scoring for a saved episode.")
    parser.add_argument("episode_dir", type=Path)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    diagnostic = diagnose_reaching_episode(args.episode_dir)
    payload = diagnostic.to_dict()
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for key, value in payload.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
