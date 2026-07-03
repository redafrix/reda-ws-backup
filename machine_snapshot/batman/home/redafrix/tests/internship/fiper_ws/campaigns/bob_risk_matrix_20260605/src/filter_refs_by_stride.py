#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--stride", type=int, default=10)
    args = parser.parse_args()

    source = Path(args.source)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    report = {}
    for src in sorted(source.glob("*.jsonl")):
        kept = 0
        total = 0
        out = dest / src.name
        with src.open() as reader, out.open("w") as writer:
            for line in reader:
                if not line.strip():
                    continue
                total += 1
                row = json.loads(line)
                if int(row.get("timestep") or 0) % args.stride != 0:
                    continue
                writer.write(json.dumps(row, sort_keys=True) + "\n")
                kept += 1
        report[src.name] = {"total": total, "kept": kept}
    (dest / "STRIDE_FILTER_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
