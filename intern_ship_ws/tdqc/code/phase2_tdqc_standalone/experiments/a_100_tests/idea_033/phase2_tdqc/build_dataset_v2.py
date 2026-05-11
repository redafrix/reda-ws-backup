"""
Build a correctly structured TDQC dataset from raw collection JSONL.

8D feature vector per plan-prediction step:
  [0] mean_path   -- log1p(mean(path_variance))       mean uncertainty across all 7 action dims
  [1] mean_last   -- log1p(mean(last_step_variance))  mean uncertainty at last predicted action
  [2] std_path    -- log1p(std(path_variance))        spread of uncertainty across the 7 joints
  [3] std_last    -- log1p(std(last_step_variance))   spread at last predicted action
  [4] max_path    -- log1p(max(path_variance))        peak uncertainty anywhere in path
  [5] max_last    -- log1p(max(last_step_variance))   peak uncertainty at last predicted action
  [6] gripper_path-- log1p(path_variance[6])          gripper-dim path uncertainty (dim 6)
  [7] gripper_last-- log1p(last_step_variance[6])     gripper-dim last-step uncertainty (dim 6)

Notes:
- Slots 2/3 use population std across the 7 action dims. Captures whether uncertainty is
  spread uniformly across joints (low std) or concentrated in specific joints (high std).
  First-horizon-step variances (the ideal values) were lost: the JSONL stores only per-dim
  aggregates collapsed over the H-step action prediction horizon.
- Gripper confirmed as dim 6 by consistently near-zero variance (~1e-5 vs arm dims ~1e-2).
- log1p applied to all values, consistent with aggregate_uncertainty_features runtime.
"""

import json
import math
import argparse
import torch
from tqdm import tqdm

GRIPPER_DIM = 6  # last action dim; confirmed gripper by near-zero variance


def _std(vals: list) -> float:
    n = len(vals)
    if n < 2:
        return 0.0
    m = sum(vals) / n
    return math.sqrt(sum((v - m) ** 2 for v in vals) / n)  # population std


def _feat(pv: list, lv: list) -> list:
    return [
        math.log1p(sum(pv) / len(pv)),       # [0] mean path
        math.log1p(sum(lv) / len(lv)),       # [1] mean last-step
        math.log1p(_std(pv)),                # [2] std path
        math.log1p(_std(lv)),                # [3] std last-step
        math.log1p(max(pv)),                 # [4] max path
        math.log1p(max(lv)),                 # [5] max last-step
        math.log1p(pv[GRIPPER_DIM]),         # [6] gripper path
        math.log1p(lv[GRIPPER_DIM]),         # [7] gripper last-step
    ]


def convert(jsonl_path: str, output_path: str) -> None:
    episodes = []
    print(f"Reading {jsonl_path} ...")

    with open(jsonl_path, "r") as f:
        for raw in tqdm(f):
            data = json.loads(raw)
            trace = data.get("uncertainty_trace", [])

            steps_data = []
            for step in trace:
                pv = step.get("path_variance", [])
                lv = step.get("last_step_variance", [])
                if not pv or not lv:
                    continue
                steps_data.append(_feat(pv, lv))

            if not steps_data:
                continue

            episodes.append({
                "features": torch.tensor(steps_data, dtype=torch.float32),
                "success": data.get("success", False),
                "task_id": data.get("task_id", -1),
                "episode_idx": data.get("episode", -1),
                "task_suite": data.get("task_suite", ""),
                "instruction": data.get("task_description", ""),
            })

    torch.save({"episodes": episodes}, output_path)
    print(f"Saved {len(episodes)} episodes -> {output_path}")

    # Sanity checks
    all_feats = torch.cat([ep["features"] for ep in episodes], dim=0)
    names = ["mean_p", "mean_h", "first_p", "first_h", "max_p", "max_h", "grip_p", "grip_h"]
    print(f"\n{'idx':<4} {'name':<10} {'mean':>9} {'std':>9} {'min':>9} {'max':>9}  zeros")
    for i, name in enumerate(names):
        col = all_feats[:, i]
        nz = (col == 0.0).sum().item()
        print(f"[{i}]  {name:<10} {col.mean():>9.5f} {col.std():>9.5f} "
              f"{col.min():>9.6f} {col.max():>9.5f}  {nz}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    convert(args.input, args.output)
