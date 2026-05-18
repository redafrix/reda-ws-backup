#!/usr/bin/env python3
"""Stage 7 — Train/evaluate raters with the multi-expert min-distance target.

Reuses Stage 6 model architectures and feature builders. For each requested
target column (e.g., target_chunk_min_l2_K10), creates a temporary copy of
the candidate rows where `true_chunk_l2_error` is replaced by the chosen
column, then runs the Stage 6 training+evaluation pipeline.

Compares against the single-expert baseline (target_chunk_l2_single_expert,
which equals the original true_chunk_l2_error).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))

from rater_stage6.run_stage6_experiments import (  # noqa: E402
    train_variant,
    VARIANTS,
    DATA_ROOT,
    CKROOT,
    RROOT,
)

MULTIEXP_TARGETS = [
    "target_chunk_l2_single_expert",
    "target_chunk_min_l2_K5",
    "target_chunk_min_l2_K10",
    "target_chunk_min_l2_K20",
    "target_chunk_softmin_l2_K10",
    "target_chunk_mean_top3_l2_K10",
]


def stage_temp_candidates(split: str, target_col: str, suffix: str):
    """Write per-part `multiseed_candidate_<part>.pt` files into a temp dir,
    with `true_chunk_l2_error` and `true_per_step_l2_error` overridden by the
    chosen target column. Returns the staged directory (a sibling of the
    original split dir under processed_stage5).
    """
    src_dir = DATA_ROOT / split
    staged_split = f"{split}__{suffix}"
    dst_dir = DATA_ROOT / staged_split
    dst_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for part in ("train", "calib", "test_id", "test_ood"):
        p = src_dir / f"multiseed_candidate_{part}_multiexp.pt"
        if not p.exists():
            continue
        data = torch.load(p, map_location="cpu", weights_only=False)
        new_rows = []
        for row in data["candidates"]:
            new = dict(row)
            if target_col not in new:
                raise KeyError(f"row missing target {target_col}: {list(new)[:6]}...")
            new_target = float(new[target_col])
            new["true_chunk_l2_error"] = new_target
            # Scale per-step proportionally so per-step head still has signal.
            old_target = float(row["true_chunk_l2_error"])
            scale = (new_target + 1e-8) / (old_target + 1e-8)
            new["true_per_step_l2_error"] = row["true_per_step_l2_error"].float() * scale
            new_rows.append(new)
        out_p = dst_dir / f"multiseed_candidate_{part}.pt"
        torch.save(
            {
                "schema_version": data["schema_version"],
                "source_candidate": str(p),
                "num_contexts": data["num_contexts"],
                "num_candidates": data["num_candidates"],
                "candidates": new_rows,
                "target_column": target_col,
            },
            out_p,
        )
        written.append(part)
    return staged_split, written


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="holdout_libero_object")
    ap.add_argument(
        "--targets",
        nargs="+",
        default=[
            "target_chunk_l2_single_expert",
            "target_chunk_min_l2_K10",
            "target_chunk_softmin_l2_K10",
        ],
    )
    ap.add_argument(
        "--variants",
        nargs="+",
        default=["action_only_baseline", "context_gated_action"],
    )
    ap.add_argument("--epochs", type=int, default=80)
    args = ap.parse_args()

    RROOT.mkdir(parents=True, exist_ok=True)
    full = {"split": args.split, "by_target": {}}

    for target_col in args.targets:
        suffix = "MET_" + target_col.replace("target_chunk_", "")
        staged_split, parts = stage_temp_candidates(args.split, target_col, suffix)
        print(f"[stage] target={target_col} staged_split={staged_split} parts={parts}",
              flush=True)
        per_variant = []
        for v in args.variants:
            res = train_variant(staged_split, v, epochs=args.epochs, quick=False)
            res["variant"] = v
            res["target_column"] = target_col
            per_variant.append(res)
            print(f"  done {v}", flush=True)
        full["by_target"][target_col] = per_variant

    out_path = RROOT / f"stage7_multi_expert_target_{args.split}.json"
    out_path.write_text(json.dumps(full, indent=2))
    md = ["# Stage 7 Multi-Expert Target Experiments: " + args.split, "", "```json",
          json.dumps(full, indent=2), "```"]
    (RROOT / f"stage7_multi_expert_target_{args.split}.md").write_text("\n".join(md) + "\n")
    print("wrote", out_path)


if __name__ == "__main__":
    main()
