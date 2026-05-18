#!/usr/bin/env python3
"""Stage 7 — train rater variants with optional flow-trace features.

Variants:
  context_gated_action_no_flow   = Stage 6 baseline (M3_gated_base features only)
  context_gated_action_plus_flow = M3_gated_base + flow_trace_vector(12)
  action_only_plus_flow          = A0_action_flat + flow_trace_vector(12)
  flow_only                      = flow_trace_vector(12) features only (sanity)
  seed_relative_plus_flow        = M4_seed_relative + flow_trace_vector(12)

Loads the flow-trace candidate dataset built by
`build_flowtrace_candidate_dataset.py`. Source path:
asynchvla_ws/data/processed_stage7_flow/<split>/flowtrace_multiseed_candidate_*.pt
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))
sys.path.insert(0, str(REDA_WS / "asynchvla_ws/src"))

from features_stage6.build_features import (  # noqa: E402
    build_seed_stats, feature_vector, is_simvla_type,
)
from features_stage7.flow_trace_features import flow_trace_vector  # noqa: E402
from rater_stage6.common_metrics import (  # noqa: E402
    all_candidate_metrics, simvla_only_metrics,
)
from rater_stage6.models import MLPRegressor, ContextGatedActionFixed  # noqa: E402

DATA_ROOT = REDA_WS / "asynchvla_ws/data/processed_stage7_flow"
ROUT = REDA_WS / "asynchvla_ws/outputs/reports/stage7"


VARIANTS = {
    # name: (base_mode, with_flow, model_kind)
    "context_gated_action_no_flow":   ("M3_gated_base", False, "gated"),
    "context_gated_action_plus_flow": ("M3_gated_base", True,  "gated"),
    "action_only_baseline":           ("A0_action_flat", False, "mlp"),
    "action_only_plus_flow":          ("A0_action_flat", True,  "mlp"),
    "flow_only":                      (None,             True,  "mlp"),
    "seed_relative_plus_flow":        ("M4_seed_relative", True, "mlp_big"),
}


def load_part(split, part):
    p = DATA_ROOT / split / f"flowtrace_multiseed_candidate_{part}.pt"
    if not p.exists():
        return []
    return torch.load(p, map_location="cpu", weights_only=False)["candidates"]


def build_matrix(rows, base_mode, with_flow, seed_stats):
    xs = []
    for r in rows:
        if base_mode is None:
            x = flow_trace_vector(r)
        else:
            base = feature_vector(r, base_mode, seed_stats)
            if with_flow:
                x = torch.cat([base, flow_trace_vector(r)])
            else:
                x = base
        xs.append(x)
    y = torch.tensor([float(r["true_chunk_l2_error"]) for r in rows], dtype=torch.float32)
    ystep = torch.stack([r["true_per_step_l2_error"].float() for r in rows])
    return torch.stack(xs), y, ystep


def standardize(xtr, *xs):
    mu = xtr.mean(0, keepdim=True)
    sd = xtr.std(0, keepdim=True).clamp_min(1e-6)
    return [(x - mu) / sd for x in (xtr, *xs)], mu, sd


def model_for(kind, in_dim, context_dim_no_flow=968, with_flow=False):
    if kind == "gated":
        # context_dim is the prefix length used for gating.
        ctx_dim = context_dim_no_flow + (12 if with_flow else 0)
        return ContextGatedActionFixed(ctx_dim, in_dim - ctx_dim, hidden=384).train()
    if kind == "mlp":
        return MLPRegressor(in_dim, hidden=256, depth=2).train()
    if kind == "mlp_big":
        return MLPRegressor(in_dim, hidden=384, depth=3).train()
    raise KeyError(kind)


def train_variant(split, variant, *, epochs=80, batch=512):
    base_mode, with_flow, kind = VARIANTS[variant]
    parts = {p: load_part(split, p) for p in ("train", "calib", "test_id", "test_ood")}
    if not parts["train"] or not parts["calib"]:
        return {"variant": variant, "error": "missing train or calib candidates"}
    seed_stats = build_seed_stats(parts["train"] + parts["calib"] + parts["test_id"] + parts["test_ood"])
    xtr, ytr, ystep_tr = build_matrix(parts["train"], base_mode, with_flow, seed_stats)
    xcal, ycal, ystep_cal = build_matrix(parts["calib"], base_mode, with_flow, seed_stats)
    (xtrn, xcaln), mu, sd = standardize(xtr, xcal)
    m = model_for(kind, xtr.shape[1], context_dim_no_flow=968, with_flow=with_flow)
    opt = torch.optim.AdamW(m.parameters(), lr=2e-3, weight_decay=1e-4)
    hub = nn.HuberLoss(delta=0.25)
    best = (1e9, None, 0)
    t0 = time.time()
    for ep in range(1, epochs + 1):
        perm = torch.randperm(len(xtrn))
        m.train()
        for st in range(0, len(perm), batch):
            ix = perm[st:st + batch]
            out = m(xtrn[ix])
            pred = out.squeeze(-1) if out.ndim > 1 else out
            loss = hub(pred, ytr[ix])
            opt.zero_grad()
            loss.backward()
            opt.step()
        m.eval()
        with torch.no_grad():
            pred = m(xcaln)
            pred = pred.squeeze(-1) if pred.ndim > 1 else pred
            vl = float(hub(pred, ycal))
        if vl < best[0]:
            best = (vl, {k: v.detach().clone() for k, v in m.state_dict().items()}, ep)
    m.load_state_dict(best[1])
    m.eval()
    metrics = {}
    for part, rows in parts.items():
        if not rows:
            continue
        x, y, _ = build_matrix(rows, base_mode, with_flow, seed_stats)
        xn = (x - mu) / sd
        with torch.no_grad():
            pred = m(xn)
            pred = pred.squeeze(-1) if pred.ndim > 1 else pred
        pp = pred.detach().cpu().numpy().tolist()
        metrics[part] = {
            "all_candidate": all_candidate_metrics(rows, pp),
            "simvla_only": simvla_only_metrics(rows, pp),
        }
    return {
        "variant": variant,
        "feature_mode": base_mode or "flow_only",
        "with_flow": with_flow,
        "model_kind": kind,
        "input_dim": int(xtr.shape[1]),
        "best_epoch": best[2],
        "best_calib_loss": best[0],
        "train_time_sec": time.time() - t0,
        "metrics": metrics,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="holdout_libero_object")
    ap.add_argument("--variants", nargs="+", default=list(VARIANTS))
    ap.add_argument("--epochs", type=int, default=80)
    args = ap.parse_args()

    ROUT.mkdir(parents=True, exist_ok=True)
    results = []
    for v in args.variants:
        print("[stage7-flow]", args.split, v, flush=True)
        res = train_variant(args.split, v, epochs=args.epochs)
        results.append(res)
    out = {"split": args.split, "variants": results}
    out_p = ROUT / f"stage7_flowtrace_{args.split}.json"
    out_p.write_text(json.dumps(out, indent=2, default=str))
    md = ["# Stage 7 Flow-trace Experiments: " + args.split, "", "```json",
          json.dumps(out, indent=2, default=str), "```"]
    (ROUT / f"stage7_flowtrace_{args.split}.md").write_text("\n".join(md) + "\n")
    print("wrote", out_p)


if __name__ == "__main__":
    main()
