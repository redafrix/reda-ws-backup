#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import torch
import torch.nn as nn

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))

from features_stage6.build_features import build_seed_stats, feature_vector  # noqa: E402
from rater_stage6.common_metrics import all_candidate_metrics, simvla_only_metrics  # noqa: E402
from rater_stage6.models import MLPRegressor, ContextGatedActionFixed  # noqa: E402

DATA_ROOT = REDA_WS / "asynchvla_ws/data/processed_stage5"
RROOT = REDA_WS / "asynchvla_ws/stage8_ultimate/reports"
CKROOT = REDA_WS / "asynchvla_ws/outputs/checkpoints/stage8_quantile"


VARIANTS = {
    "quantile_action_q80": ("A0_action_flat", "mlp", 0.80),
    "quantile_action_q90": ("A0_action_flat", "mlp", 0.90),
    "quantile_action_q95": ("A0_action_flat", "mlp", 0.95),
    "quantile_context_gated_q80": ("M3_gated_base", "gated", 0.80),
    "quantile_context_gated_q90": ("M3_gated_base", "gated", 0.90),
    "quantile_context_gated_q95": ("M3_gated_base", "gated", 0.95),
    "quantile_seed_relative_q90": ("M4_seed_relative", "mlp_big", 0.90),
}


def load_part(split: str, part: str):
    p = DATA_ROOT / split / f"multiseed_candidate_{part}.pt"
    return torch.load(p, map_location="cpu", weights_only=False)["candidates"] if p.exists() else []


def build_matrix(rows, mode, seed_stats):
    x = torch.stack([feature_vector(r, mode, seed_stats) for r in rows])
    y = torch.tensor([float(r["true_chunk_l2_error"]) for r in rows], dtype=torch.float32)
    return x, y


def standardize(xtr, *xs):
    mu = xtr.mean(0, keepdim=True)
    sd = xtr.std(0, keepdim=True).clamp_min(1e-6)
    return [(x - mu) / sd for x in (xtr, *xs)], mu, sd


def model_for(kind, in_dim, context_dim=968):
    if kind == "mlp":
        return MLPRegressor(in_dim, hidden=256, depth=2)
    if kind == "mlp_big":
        return MLPRegressor(in_dim, hidden=384, depth=3)
    if kind == "gated":
        return ContextGatedActionFixed(context_dim, in_dim - context_dim, hidden=384)
    raise KeyError(kind)


def pinball(pred, target, q):
    err = target - pred
    return torch.maximum(q * err, (q - 1.0) * err).mean()


def train_one(split, variant, epochs):
    mode, kind, q = VARIANTS[variant]
    parts = {p: load_part(split, p) for p in ["train", "calib", "test_id", "test_ood"]}
    if not parts["train"] or not parts["calib"]:
        return {"variant": variant, "error": "missing train/calib"}
    seed_stats = build_seed_stats(sum((v for v in parts.values()), []))
    xtr, ytr = build_matrix(parts["train"], mode, seed_stats)
    xcal, ycal = build_matrix(parts["calib"], mode, seed_stats)
    (xtr, xcal), mu, sd = standardize(xtr, xcal)
    model = model_for(kind, xtr.shape[1])
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
    best = (1e9, None, 0)
    t0 = time.time()
    for ep in range(1, epochs + 1):
        perm = torch.randperm(len(xtr))
        for st in range(0, len(perm), 512):
            ix = perm[st:st + 512]
            pred = model(xtr[ix])
            pred = pred.squeeze(-1) if pred.ndim > 1 else pred
            loss = pinball(pred, ytr[ix], q)
            opt.zero_grad()
            loss.backward()
            opt.step()
        with torch.no_grad():
            pred = model(xcal)
            pred = pred.squeeze(-1) if pred.ndim > 1 else pred
            val = float(pinball(pred, ycal, q))
        if val < best[0]:
            best = (val, {k: v.detach().clone() for k, v in model.state_dict().items()}, ep)
    model.load_state_dict(best[1])
    metrics = {}
    for part, rows in parts.items():
        if not rows:
            continue
        x, _ = build_matrix(rows, mode, seed_stats)
        x = (x - mu) / sd
        with torch.no_grad():
            pred = model(x)
            pred = pred.squeeze(-1) if pred.ndim > 1 else pred
        pp = pred.detach().cpu().numpy().tolist()
        metrics[part] = {
            "all_candidate": all_candidate_metrics(rows, pp),
            "simvla_only": simvla_only_metrics(rows, pp),
        }
    ck = CKROOT / split / variant
    ck.mkdir(parents=True, exist_ok=True)
    torch.save({"state_dict": model.state_dict(), "feature_mode": mode, "kind": kind, "q": q, "input_mean": mu, "input_std": sd}, ck / "model.pt")
    return {"variant": variant, "feature_mode": mode, "kind": kind, "q": q, "best_epoch": best[2], "best_calib_pinball": best[0], "train_time_sec": time.time() - t0, "metrics": metrics, "checkpoint": str(ck / "model.pt")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--splits", nargs="+", default=["holdout_libero_object"])
    ap.add_argument("--variants", nargs="+", default=list(VARIANTS))
    ap.add_argument("--epochs", type=int, default=80)
    args = ap.parse_args()
    RROOT.mkdir(parents=True, exist_ok=True)
    out = {"splits": {}, "variants": args.variants}
    for split in args.splits:
        out["splits"][split] = []
        for variant in args.variants:
            print("TRAIN", split, variant, flush=True)
            out["splits"][split].append(train_one(split, variant, args.epochs))
    (RROOT / "stage8_quantile_head_results.json").write_text(json.dumps(out, indent=2, default=str))
    (RROOT / "stage8_quantile_head_results.md").write_text("# Stage 8 Quantile Head Results\n\n```json\n" + json.dumps(out, indent=2, default=str) + "\n```\n")
    print(RROOT / "stage8_quantile_head_results.md")


if __name__ == "__main__":
    main()
