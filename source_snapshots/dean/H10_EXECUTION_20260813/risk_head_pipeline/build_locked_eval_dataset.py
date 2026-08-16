#!/usr/bin/env python3
"""Build read-only feature arrays for a fully audited locked collection."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys

import numpy as np
from numpy.lib.format import open_memmap

PIPELINE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE))
from common import ACTION_SHAPE, HISTORY_SHAPE, STATIC_DIM, feature_tensors, sha256_file, write_json_atomic  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection-root", type=Path, required=True)
    parser.add_argument("--audit-json", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    audit = json.loads(args.audit_json.read_text())
    if not audit.get("pass"):
        raise RuntimeError("locked collection did not pass exhaustive audit")
    destination = args.output_root.resolve()
    if (destination / "EVAL_DATASET_COMPLETE").is_file():
        print((destination / "manifest.json").read_text())
        return 0
    episodes = []
    for episode_dir in sorted((args.collection_root / "episodes").iterdir()):
        if not (episode_dir / "COMMITTED").is_file():
            continue
        summary = json.loads((episode_dir / "summary.json").read_text())
        episodes.append((episode_dir, summary))
    row_count = sum(int(summary["decision_rows"]) for _, summary in episodes)
    staging = destination.parent / f".{destination.name}.staging-{os.getpid()}"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    history = open_memmap(staging / "history.npy", mode="w+", dtype="float32", shape=(row_count, *HISTORY_SHAPE))
    action = open_memmap(staging / "action.npy", mode="w+", dtype="float32", shape=(row_count, *ACTION_SHAPE))
    static = open_memmap(staging / "static.npy", mode="w+", dtype="float32", shape=(row_count, STATIC_DIM))
    label = open_memmap(staging / "label.npy", mode="w+", dtype="float32", shape=(row_count,))
    episode_index = open_memmap(staging / "episode_index.npy", mode="w+", dtype="int32", shape=(row_count,))
    decision_index = open_memmap(staging / "decision_index.npy", mode="w+", dtype="int32", shape=(row_count,))
    episode_metadata = []
    cursor = 0
    for output_index, (episode_dir, summary) in enumerate(episodes):
        start = cursor
        for expected, line in enumerate((episode_dir / "risk_rows.jsonl").open()):
            row = json.loads(line)
            h, a, s = feature_tensors(row)
            history[cursor], action[cursor], static[cursor] = h, a, s
            label[cursor] = int(summary["risk_label"])
            episode_index[cursor] = output_index
            decision_index[cursor] = expected
            cursor += 1
        episode_metadata.append({
            "episode_index": output_index,
            "episode_id": summary["episode_id"],
            "label": summary["risk_label"],
            "rows": summary["decision_rows"],
            "row_start": start,
            "row_end_exclusive": cursor,
            "instruction": summary["instruction"],
            "scene_fingerprint_sha256": summary["scene_fingerprint_sha256"],
        })
    if cursor != row_count:
        raise RuntimeError("locked evaluation row count changed during build")
    for array in (history, action, static, label, episode_index, decision_index):
        array.flush()
    write_json_atomic(staging / "episodes.json", episode_metadata)
    manifest = {
        "schema_version": "simvla_locked_evaluation_arrays_v1",
        "source_collection": str(args.collection_root.resolve()),
        "source_audit": str(args.audit_json.resolve()),
        "source_audit_sha256": sha256_file(args.audit_json),
        "episodes": len(episodes),
        "rows": row_count,
        "training_eligible": False,
        "normalization_fit_allowed": False,
    }
    write_json_atomic(staging / "manifest.json", manifest)
    (staging / "EVAL_DATASET_COMPLETE").write_text("complete\n")
    if destination.exists():
        raise RuntimeError(f"refusing to overwrite locked evaluation arrays: {destination}")
    staging.replace(destination)
    print((destination / "manifest.json").read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
