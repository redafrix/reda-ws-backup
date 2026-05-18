#!/usr/bin/env python3
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import roc_auc_score

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
DATA = REDA_WS / "asynchvla_ws/data/debug/candidate_debug.pt"
CKPT_DIR = REDA_WS / "asynchvla_ws/outputs/checkpoints/debug_rater"
LOG = REDA_WS / "asynchvla_ws/outputs/logs/debug_rater_train.log"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/debug_rater_metrics.md"


class MLP(nn.Module):
    def __init__(self, in_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 256), nn.ReLU(), nn.Dropout(0.05),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 1), nn.Softplus(),
        )
    def forward(self, x):
        return self.net(x).squeeze(-1)


def make_features(rows, mode: str):
    xs, ys, ctxs, types = [], [], [], []
    for r in rows:
        parts = []
        if mode in ("full", "context"):
            parts += [r["pooled_vlm_features"].float().flatten(), r["proprio"].float().flatten()]
        if mode in ("full", "action"):
            parts += [r["candidate_action_normalized"].float().flatten()]
        xs.append(torch.cat(parts))
        ys.append(float(r["true_chunk_l2_error"]))
        ctxs.append(r["context_id"])
        types.append(r["candidate_type"])
    return torch.stack(xs), torch.tensor(ys, dtype=torch.float32), ctxs, types


def split_rows(rows, seed=7):
    ctxs = sorted({r["context_id"] for r in rows})
    random.Random(seed).shuffle(ctxs)
    n_train = int(0.8 * len(ctxs))
    train_ctx = set(ctxs[:n_train])
    val_ctx = set(ctxs[n_train:])
    train = [r for r in rows if r["context_id"] in train_ctx]
    val = [r for r in rows if r["context_id"] in val_ctx]
    return train, val, sorted(train_ctx), sorted(val_ctx)


def standardize(x_train, x_val):
    mean = x_train.mean(0, keepdim=True)
    std = x_train.std(0, keepdim=True).clamp_min(1e-6)
    return (x_train - mean) / std, (x_val - mean) / std, mean, std


def risk_coverage(y, p):
    order = np.argsort(p)
    out = []
    for cov in [0.10, 0.25, 0.50, 0.75, 1.00]:
        n = max(1, int(round(len(y) * cov)))
        keep = order[:n]
        out.append((cov, float(np.mean(y[keep]))))
    return out


def same_context_metrics(rows, preds):
    by_ctx = defaultdict(dict)
    for r, pred in zip(rows, preds):
        by_ctx[r["context_id"]][r["candidate_type"]] = (float(pred), float(r["true_chunk_l2_error"]))
    def acc_pair(a, b):
        ok = total = 0
        for d in by_ctx.values():
            if a in d and b in d:
                total += 1
                ok += int(d[a][0] < d[b][0])
        return ok / total if total else float("nan")
    simvla_order_ok = 0
    simvla_order_total = 0
    for d in by_ctx.values():
        if "simvla_seed0" not in d:
            continue
        for b in ("perturb_small", "perturb_large", "same_task_far", "other_demo_or_other_task"):
            if b in d:
                sim_true_less = d["simvla_seed0"][1] < d[b][1]
                sim_pred_less = d["simvla_seed0"][0] < d[b][0]
                simvla_order_ok += int(sim_true_less == sim_pred_less)
                simvla_order_total += 1
    pred_stds = []
    for d in by_ctx.values():
        vals = [v[0] for v in d.values()]
        if len(vals) > 1:
            pred_stds.append(float(np.std(vals)))
    return {
        "expert_lt_perturb_large": acc_pair("expert_action", "perturb_large"),
        "expert_lt_other_task": acc_pair("expert_action", "other_demo_or_other_task"),
        "expert_lt_same_task_far": acc_pair("expert_action", "same_task_far"),
        "expert_lt_simvla": acc_pair("expert_action", "simvla_seed0"),
        "simvla_pairwise_true_order_accuracy": simvla_order_ok / simvla_order_total if simvla_order_total else float("nan"),
        "action_sensitivity_avg_pred_std_same_context": float(np.mean(pred_stds)) if pred_stds else float("nan"),
    }


def evaluate(rows, y, pred):
    y_np = y.detach().cpu().numpy()
    p_np = pred.detach().cpu().numpy()
    pear = pearsonr(p_np, y_np).statistic if np.std(p_np) > 1e-8 else float("nan")
    spear = spearmanr(p_np, y_np).statistic if np.std(p_np) > 1e-8 else float("nan")
    thresh = np.quantile(y_np, 0.70)
    labels = (y_np >= thresh).astype(int)
    auroc = roc_auc_score(labels, p_np) if len(set(labels.tolist())) == 2 and np.std(p_np) > 1e-8 else float("nan")
    return {
        "pearson": float(pear),
        "spearman": float(spear),
        "auroc_top30_bad": float(auroc),
        "mse": float(np.mean((p_np - y_np) ** 2)),
        "mae": float(np.mean(np.abs(p_np - y_np))),
        "risk_coverage": risk_coverage(y_np, p_np),
        **same_context_metrics(rows, p_np),
    }


def train_one(train_rows, val_rows, mode: str):
    x_tr, y_tr, _, _ = make_features(train_rows, mode)
    x_va, y_va, _, _ = make_features(val_rows, mode)
    x_tr, x_va, mean, std = standardize(x_tr, x_va)
    model = MLP(x_tr.shape[1])
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
    loss_fn = nn.HuberLoss(delta=0.25)
    best = {"loss": float("inf"), "state": None, "epoch": 0}
    log_lines = []
    for epoch in range(1, 301):
        model.train()
        perm = torch.randperm(len(x_tr))
        total = 0.0
        for start in range(0, len(perm), 128):
            idx = perm[start:start+128]
            pred = model(x_tr[idx])
            loss = loss_fn(pred, y_tr[idx])
            opt.zero_grad()
            loss.backward()
            opt.step()
            total += float(loss.detach()) * len(idx)
        model.eval()
        with torch.no_grad():
            val_pred = model(x_va)
            val_loss = float(loss_fn(val_pred, y_va))
        train_loss = total / len(x_tr)
        if val_loss < best["loss"]:
            best = {"loss": val_loss, "state": {k: v.detach().clone() for k, v in model.state_dict().items()}, "epoch": epoch}
        if epoch % 25 == 0 or epoch == 1:
            log_lines.append(f"{mode} epoch={epoch} train_loss={train_loss:.6f} val_loss={val_loss:.6f}")
    model.load_state_dict(best["state"])
    model.eval()
    with torch.no_grad():
        val_pred = model(x_va)
    metrics = evaluate(val_rows, y_va, val_pred)
    return model, mean, std, metrics, log_lines, best


def main() -> int:
    torch.manual_seed(7)
    np.random.seed(7)
    payload = torch.load(DATA, map_location="cpu")
    rows = payload["candidates"]
    train_rows, val_rows, train_ctx, val_ctx = split_rows(rows, seed=7)
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    results = {}
    ckpt = {"split": {"train_contexts": train_ctx, "val_contexts": val_ctx}, "models": {}}
    all_logs = []
    for mode in ("full", "context", "action"):
        model, mean, std, metrics, logs, best = train_one(train_rows, val_rows, mode)
        results[mode] = metrics
        all_logs.extend(logs)
        ckpt["models"][mode] = {
            "state_dict": model.state_dict(),
            "input_mean": mean,
            "input_std": std,
            "input_dim": int(mean.shape[1]),
            "best_epoch": best["epoch"],
            "best_val_loss": best["loss"],
        }
    torch.save(ckpt, CKPT_DIR / "debug_rater.pt")
    LOG.write_text("\n".join(all_logs) + "\n")
    success = results["full"]["expert_lt_perturb_large"] > results["context"]["expert_lt_perturb_large"] + 0.25 and results["full"]["action_sensitivity_avg_pred_std_same_context"] > results["context"]["action_sensitivity_avg_pred_std_same_context"] + 0.02
    lines = [
        "# Debug Rater Metrics",
        "",
        f"- Dataset: `{DATA}`",
        f"- Checkpoint: `{CKPT_DIR / 'debug_rater.pt'}`",
        f"- Train contexts: `{len(train_ctx)}`",
        f"- Validation contexts: `{len(val_ctx)}`",
        f"- Train rows: `{len(train_rows)}`",
        f"- Validation rows: `{len(val_rows)}`",
        "- Split rule: by `context_id`; no context appears in both train and validation.",
        "- Target: chunk-level normalized action L2 error.",
        "- Full input: pooled VLM features + proprio + candidate action.",
        "- Context baseline input: pooled VLM features + proprio only.",
        "- Action baseline input: candidate action only.",
        f"- Critical success condition met: `{success}`",
        "",
        "## Metrics JSON",
        "",
        "```json",
        json.dumps(results, indent=2),
        "```",
    ]
    REPORT.write_text("\n".join(lines) + "\n")
    print("debug_rater_training: OK")
    print(json.dumps(results, indent=2))
    print("success", success)
    print("checkpoint", CKPT_DIR / "debug_rater.pt")
    print("report", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
