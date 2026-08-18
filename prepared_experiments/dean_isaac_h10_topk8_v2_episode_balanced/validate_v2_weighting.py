#!/usr/bin/env python3
"""CPU-only audit of the frozen Seen train split and V2 episode-balanced weights."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np

EXPECTED = {"rows": 52825, "episodes": 2800, "failures": 64, "successes": 2736}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--train-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    labels = np.asarray(np.load(args.train_root / "label.npy", mmap_mode="r"), dtype=np.float64)
    epi = np.asarray(np.load(args.train_root / "episode_index.npy", mmap_mode="r"), dtype=np.int64)
    episodes = json.loads((args.train_root / "episodes.json").read_text())
    n_ep = len(episodes)
    counts = np.bincount(epi, minlength=n_ep)
    if np.any(counts <= 0):
        raise RuntimeError("empty episode")
    ep_label = np.empty(n_ep, dtype=np.float64)
    for i in range(n_ep):
        vals = np.unique(labels[epi == i])
        if len(vals) != 1:
            raise RuntimeError(f"mixed labels episode {i}: {vals}")
        ep_label[i] = vals[0]
    positive = labels >= 0.5
    n_fail = int((ep_label >= 0.5).sum())
    n_success = int((ep_label < 0.5).sum())
    actual = {"rows": int(len(labels)), "episodes": n_ep, "failures": n_fail, "successes": n_success}
    if actual != EXPECTED:
        raise RuntimeError(f"frozen split changed: {actual}")
    Ti = counts[epi].astype(np.float64)
    raw = np.empty(len(labels), dtype=np.float64)
    raw[~positive] = 0.5 / (n_success * Ti[~positive])
    raw[positive] = 0.5 / (n_fail * Ti[positive])
    per_ep = np.bincount(epi, weights=raw, minlength=n_ep)
    success_ep = per_ep[ep_label < 0.5]
    failure_ep = per_ep[ep_label >= 0.5]
    success_counts = counts[ep_label < 0.5]
    failure_counts = counts[ep_label >= 0.5]
    checks = {
        "success_mass_half": bool(np.isclose(raw[~positive].sum(), 0.5, atol=1e-10, rtol=0)),
        "failure_mass_half": bool(np.isclose(raw[positive].sum(), 0.5, atol=1e-10, rtol=0)),
        "success_episode_equal": bool(np.allclose(success_ep, 0.5/n_success, atol=1e-10, rtol=0)),
        "failure_episode_equal": bool(np.allclose(failure_ep, 0.5/n_fail, atol=1e-10, rtol=0)),
        "mean_multiplier_one": bool(np.isclose((len(labels)*raw).mean(), 1.0, atol=1e-10, rtol=0)),
    }
    payload = {
        "schema_version": "isaac_h10_topk8_v2_weighting_cpu_preflight_v1",
        **actual,
        "success_rows": int((~positive).sum()),
        "failure_rows": int(positive.sum()),
        "success_rows_per_episode": {"min": int(success_counts.min()), "mean": float(success_counts.mean()), "max": int(success_counts.max())},
        "failure_rows_per_episode": {"min": int(failure_counts.min()), "mean": float(failure_counts.mean()), "max": int(failure_counts.max())},
        "success_raw_weight_sum": float(raw[~positive].sum()),
        "failure_raw_weight_sum": float(raw[positive].sum()),
        "per_success_episode_weight": {"min": float(success_ep.min()), "mean": float(success_ep.mean()), "max": float(success_ep.max())},
        "per_failure_episode_weight": {"min": float(failure_ep.min()), "mean": float(failure_ep.mean()), "max": float(failure_ep.max())},
        "row_multiplier": {"min": float((len(labels)*raw).min()), "mean": float((len(labels)*raw).mean()), "max": float((len(labels)*raw).max())},
        "checks": checks,
        "pass": bool(all(checks.values())),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    if not payload["pass"]:
        raise SystemExit(2)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
