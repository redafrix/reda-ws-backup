"""
Build v6_delta: 16D per-step feature dataset for TDQC delta-features experiment (idea 2).

Feature layout (16D):
  [0-7]   Same as v6 (mean_path, mean_last, std_path, std_last, max_path, max_last, gripper_path, gripper_last)
  [8-15]  Per-step deltas: Δf_t = f_t - f_{t-1}  (Δf_0 = 0 for all dims)

Rationale: delta features capture rate-of-change of uncertainty, giving the LSTM a direct
signal for whether uncertainty is rising or falling — a stronger failure predictor than
level features alone.
"""

import json
import math
import argparse
import torch
from tqdm import tqdm

GRIPPER_DIM = 6


def _std(vals: list) -> float:
    n = len(vals)
    if n < 2:
        return 0.0
    m = sum(vals) / n
    return math.sqrt(sum((v - m) ** 2 for v in vals) / n)


def _feat8(pv: list, lv: list) -> list:
    return [
        math.log1p(sum(pv) / len(pv)),   # [0] mean path
        math.log1p(sum(lv) / len(lv)),   # [1] mean last-step
        math.log1p(_std(pv)),             # [2] std path
        math.log1p(_std(lv)),             # [3] std last-step
        math.log1p(max(pv)),              # [4] max path
        math.log1p(max(lv)),              # [5] max last-step
        math.log1p(pv[GRIPPER_DIM]),      # [6] gripper path
        math.log1p(lv[GRIPPER_DIM]),      # [7] gripper last-step
    ]


def convert(jsonl_path: str, output_path: str) -> None:
    episodes = []
    print(f"Reading {jsonl_path} ...")

    with open(jsonl_path, "r") as f:
        for raw in tqdm(f):
            data = json.loads(raw)
            trace = data.get("uncertainty_trace", [])

            base_steps = []
            for step in trace:
                pv = step.get("path_variance", [])
                lv = step.get("last_step_variance", [])
                if not pv or not lv:
                    continue
                base_steps.append(_feat8(pv, lv))

            if not base_steps:
                continue

            # Build 16D: [f_t | delta_t]
            n = len(base_steps)
            feats_16 = []
            for t in range(n):
                f = base_steps[t]
                if t == 0:
                    delta = [0.0] * 8
                else:
                    delta = [f[i] - base_steps[t - 1][i] for i in range(8)]
                feats_16.append(f + delta)

            episodes.append({
                "features": torch.tensor(feats_16, dtype=torch.float32),
                "success": data.get("success", False),
                "task_id": data.get("task_id", -1),
                "episode_idx": data.get("episode", -1),
                "task_suite": data.get("task_suite", ""),
                "instruction": data.get("task_description", ""),
            })

    torch.save({"episodes": episodes}, output_path)
    print(f"Saved {len(episodes)} episodes -> {output_path}")

    all_feats = torch.cat([ep["features"] for ep in episodes], dim=0)
    names = [
        "mean_p", "mean_h", "std_p", "std_h", "max_p", "max_h", "grip_p", "grip_h",
        "Δmean_p", "Δmean_h", "Δstd_p", "Δstd_h", "Δmax_p", "Δmax_h", "Δgrip_p", "Δgrip_h",
    ]
    print(f"\n{'idx':<5} {'name':<10} {'mean':>9} {'std':>9} {'min':>9} {'max':>9}  zeros")
    for i, name in enumerate(names):
        col = all_feats[:, i]
        nz = (col == 0.0).sum().item()
        print(f"[{i:02d}]  {name:<10} {col.mean():>9.5f} {col.std():>9.5f} "
              f"{col.min():>9.5f} {col.max():>9.5f}  {nz}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    convert(args.input, args.output)
