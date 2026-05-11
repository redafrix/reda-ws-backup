"""
Build v7 22D dataset: 11D features + 11D temporal deltas.

Feature vector (22D per plan-prediction step):
  [0-10]  Raw 11D features from v7
  [11-21] Temporal deltas: df_t = f_t - f_{t-1}, with df_0 = 0

Input:  train/val/test/ood .jsonl or .jsonl.gz files
Output: .pt files with 22D tensors

Usage:
    python3 build_dataset_v7_22d.py \
        --train  path/to/train_clean.jsonl.gz \
        --val    path/to/val_clean.jsonl.gz \
        --test   path/to/test_clean.jsonl.gz \
        --ood    path/to/ood.jsonl \
        --outdir path/to/output/
"""

import gzip
import json
import math
import argparse
import torch
from pathlib import Path
from tqdm import tqdm

GRIPPER_DIM = 6


def _std(vals: list) -> float:
    n = len(vals)
    if n < 2:
        return 0.0
    m = sum(vals) / n
    return math.sqrt(sum((v - m) ** 2 for v in vals) / n)


def _signed_log1p(x: float) -> float:
    return math.copysign(math.log1p(abs(x)), x)


def _feat(step: dict) -> list:
    pv = step["path_variance"]       # list[7]
    lv = step["last_step_variance"]  # list[7]
    di = step["denoise_initial_mean"]
    dd = step["denoise_delta"]       # = initial - final, usually negative
    dr = step["denoise_final_rotation_mean"]

    return [
        math.log1p(sum(pv) / len(pv)),      # [0] mean path
        math.log1p(sum(lv) / len(lv)),      # [1] mean last-step
        math.log1p(_std(pv)),               # [2] std path
        math.log1p(_std(lv)),               # [3] std last-step
        math.log1p(max(pv)),                # [4] max path
        math.log1p(max(lv)),                # [5] max last-step
        math.log1p(pv[GRIPPER_DIM]),        # [6] gripper path
        math.log1p(lv[GRIPPER_DIM]),        # [7] gripper last-step
        math.log1p(di),                     # [8] denoise initial mean
        _signed_log1p(dd),                  # [9] denoise delta (signed log)
        math.log1p(dr),                     # [10] denoise rotation mean
    ]


def convert_split(jsonl_path: str, split_name: str) -> list:
    episodes = []
    skipped  = 0
    print(f"\n[{split_name}] Reading {jsonl_path} ...")

    is_gz = str(jsonl_path).endswith(".gz")
    opener = gzip.open if is_gz else open
    mode = "rt" if is_gz else "r"

    with opener(jsonl_path, mode) as f:
        for raw in tqdm(f, desc=split_name):
            data  = json.loads(raw)
            trace = data.get("uncertainty_trace", [])

            steps_data = []
            for step in trace:
                pv = step.get("path_variance", [])
                lv = step.get("last_step_variance", [])
                di = step.get("denoise_initial_mean")
                dd = step.get("denoise_delta")
                dr = step.get("denoise_final_rotation_mean")

                if not pv or not lv or di is None or dd is None or dr is None:
                    skipped += 1
                    continue

                steps_data.append(_feat(step))

            if not steps_data:
                continue

            # Compute 22D: [raw_11d, delta_11d]
            raw_feats = torch.tensor(steps_data, dtype=torch.float32)
            # delta_f_t = f_t - f_{t-1}, delta_f_0 = 0
            deltas = torch.zeros_like(raw_feats)
            if raw_feats.shape[0] > 1:
                deltas[1:] = raw_feats[1:] - raw_feats[:-1]
            
            combined_feats = torch.cat([raw_feats, deltas], dim=-1)

            episodes.append({
                "features":    combined_feats,
                "success":     bool(data.get("success", False)),
                "task_id":     int(data.get("task_id", -1)),
                "episode_idx": int(data.get("episode", -1)),
                "task_suite":  str(data.get("task_suite", "")),
                "instruction": str(data.get("task_description", "")),
            })

    print(f"  Episodes loaded: {len(episodes)}  Steps skipped (missing fields): {skipped}")
    return episodes


def print_stats(episodes: list, split_name: str):
    if not episodes:
        print(f"[{split_name}] No episodes found.")
        return
    all_feats = torch.cat([ep["features"] for ep in episodes], dim=0)
    n_success = sum(1 for ep in episodes if ep["success"])
    n_fail    = len(episodes) - n_success
    total_steps = all_feats.shape[0]

    names_11 = [
        "mean_p", "mean_h", "std_p", "std_h", "max_p", "max_h",
        "grip_p", "grip_h", "dn_init", "dn_delta", "dn_rot",
    ]
    names = names_11 + [f"d_{n}" for n in names_11]

    print(f"\n{'─'*75}")
    print(f"[{split_name}]  episodes={len(episodes)}  "
          f"success={n_success} ({n_success/len(episodes)*100:.1f}%)  "
          f"failure={n_fail} ({n_fail/len(episodes)*100:.1f}%)  "
          f"steps={total_steps:,}")
    print(f"{'─'*75}")
    print(f"{'idx':<5} {'name':<12} {'mean':>9} {'std':>9} {'min':>10} {'max':>10}  zeros")
    for i, name in enumerate(names):
        col = all_feats[:, i]
        nz  = (col == 0.0).sum().item()
        print(f"[{i:02d}]  {name:<12} {col.mean():>9.5f} {col.std():>9.5f} "
              f"{col.min():>10.5f} {col.max():>10.5f}  {nz}")

    # Sanity: no NaN or Inf
    assert not torch.isnan(all_feats).any(),  "NaN found in features!"
    assert not torch.isinf(all_feats).any(),  "Inf found in features!"
    print("  ✓ No NaN or Inf")

    # Sanity: check slot [9] (dn_delta) is signed correctly — most should be negative
    col9 = all_feats[:, 9]
    frac_neg = (col9 < 0).float().mean().item()
    print(f"  ✓ Slot [9] dn_delta: {frac_neg*100:.1f}% negative (expected ~99%)")

    print(f"{'─'*75}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train",  help="Path to train jsonl.gz")
    parser.add_argument("--val",    help="Path to val jsonl.gz")
    parser.add_argument("--test",   help="Path to test jsonl.gz")
    parser.add_argument("--ood",    help="Path to ood jsonl")
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    splits = []
    if args.train: splits.append(("train", args.train, "v7_22d_train.pt"))
    if args.val:   splits.append(("val",   args.val,   "v7_22d_val.pt"))
    if args.test:  splits.append(("test",  args.test,  "v7_22d_test.pt"))
    if args.ood:   splits.append(("ood",   args.ood,   "v7_22d_ood.pt"))

    for split_name, path_arg, out_name in splits:
        episodes = convert_split(path_arg, split_name)
        print_stats(episodes, split_name)
        out_path = outdir / out_name
        torch.save({"episodes": episodes}, str(out_path))
        print(f"  Saved → {out_path}")

    print("\n✓ All requested splits built successfully.")


if __name__ == "__main__":
    main()
