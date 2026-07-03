#!/usr/bin/env python3
import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize a FIPER split from a row-reference manifest.")
    parser.add_argument("--ref-rows", type=str, required=True, help="Path to split row refs file (*.rows.jsonl)")
    parser.add_argument("--output-jsonl", type=str, required=True, help="Path to write materialized JSONL split")
    args = parser.parse_args()

    ref_path = Path(args.ref_rows)
    out_path = Path(args.output_jsonl)

    if not ref_path.exists():
        print(f"Error: Reference rows file not found at {ref_path}")
        sys.exit(1)

    print(f"Loading row references from {ref_path}...")
    # Read references
    refs = []
    with ref_path.open("r") as f:
        for idx, line in enumerate(f):
            ref = json.loads(line)
            refs.append({
                "index": idx,
                "source_jsonl": ref["source_jsonl"],
                "line_no": int(ref["line_no"])
            })

    print(f"Loaded {len(refs)} row references. Grouping by source file...")
    # Group by source file to minimize I/O
    by_source = defaultdict(list)
    for ref in refs:
        by_source[ref["source_jsonl"]].append(ref)

    # Workspace root is parent of scripts directory (where this script resides is fiper_ws/scripts/)
    workspace_root = Path(__file__).resolve().parent.parent

    # To hold the materialized rows mapped by their original order index
    materialized_rows = [None] * len(refs)

    start_time = time.time()
    for source_rel, src_refs in by_source.items():
        source_path = workspace_root / source_rel
        if not source_path.exists():
            print(f"Error: Source file {source_path} not found.")
            sys.exit(1)

        # Sort references by line number to read sequentially in one pass
        src_refs.sort(key=lambda x: x["line_no"])
        
        # Build line mapping: line_no -> list of indices where this line is needed
        line_map = defaultdict(list)
        for r in src_refs:
            line_map[r["line_no"]].append(r["index"])

        needed_lines = sorted(list(line_map.keys()))
        needed_idx = 0
        max_needed_idx = len(needed_lines)

        print(f"Streaming {len(src_refs)} rows from {source_rel}...")
        with source_path.open("r") as f:
            for line_idx, line in enumerate(f):
                line_no = line_idx + 1
                if needed_idx >= max_needed_idx:
                    break
                if line_no == needed_lines[needed_idx]:
                    # Retrieve the line
                    raw_content = line.strip()
                    for idx in line_map[line_no]:
                        materialized_rows[idx] = raw_content
                    needed_idx += 1

    # Write materialized split
    print(f"Writing materialized split to {out_path}...")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        for idx, row in enumerate(materialized_rows):
            if row is None:
                print(f"Warning: Reference index {idx} was not successfully read from source files.")
                continue
            f.write(row + "\n")

    duration = time.time() - start_time
    print(f"Success! Materialized {len(refs)} rows in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
