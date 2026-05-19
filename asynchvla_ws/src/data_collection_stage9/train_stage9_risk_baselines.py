from __future__ import annotations

import argparse
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


LABEL_GOOD = "GOOD_STRONG"
LABEL_BAD = "VALIDATED_BAD"


def load_rows(paths: list[str]) -> list[dict[str, Any]]:
    files = []
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob("counterfactual_samples.jsonl")))
    rows = []
    seen = set()
    for file in files:
        with file.open() as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                key = (str(file), row.get("sample_id"))
                if key in seen:
                    continue
                seen.add(key)
                rows.append(row)
    return rows


def final_label(row: dict[str, Any]) -> str | None:
    label = row.get("label")
    if isinstance(label, dict):
        return label.get("label") or label.get("final_label")
    return label


def pad_flat(values, size: int) -> np.ndarray:
    arr = np.asarray(values if values is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(size, dtype=np.float32)
    n = min(size, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def action_feature(row: dict[str, Any], size: int = 70) -> np.ndarray:
    cand = row.get("candidate_action") or {}
    return pad_flat(cand.get("candidate_action_normalized") or cand.get("candidate_action_env"), size)


def proprio_feature(row: dict[str, Any], size: int = 8) -> np.ndarray:
    return pad_flat((row.get("current") or {}).get("proprio"), size)


def history_feature(row: dict[str, Any], k: int = 8, dim: int = 15) -> np.ndarray:
    hist = row.get("history") or []
    out = np.zeros((k, dim), dtype=np.float32)
    tail = hist[-k:]
    for i, item in enumerate(tail, start=k - len(tail)):
        if not isinstance(item, dict):
            continue
        step = np.concatenate([
            pad_flat(item.get("proprio"), 8),
            pad_flat(item.get("executed_action"), 7),
        ])
        out[i, : min(dim, step.size)] = step[:dim]
    return out


def metadata_group(row: dict[str, Any], key: str) -> str:
    meta = row.get("metadata") or {}
    return str(meta.get(key) or "unknown")


def build_arrays(rows: list[dict[str, Any]], baseline: str, subtype_filter: str = "all"):
    xs = []
    hs = []
    ys = []
    kept = []
    for row in rows:
        label = final_label(row)
        if label not in {LABEL_GOOD, LABEL_BAD}:
            continue
        subtype = (row.get("label") or {}).get("bad_subtype") or "unknown"
        if subtype_filter != "all":
            if label == LABEL_BAD and subtype != subtype_filter:
                continue
            if label == LABEL_GOOD and subtype_filter in {"action_specific", "state_context"}:
                pass
        action = action_feature(row)
        proprio = proprio_feature(row)
        hist = history_feature(row)
        if baseline == "action_only_mlp":
            x = action
        elif baseline == "context_action_mlp":
            x = np.concatenate([proprio, action])
        else:
            x = np.concatenate([proprio, action])
        xs.append(x.astype(np.float32))
        hs.append(hist.astype(np.float32))
        ys.append(1 if label == LABEL_BAD else 0)
        kept.append(row)
    if not xs:
        return None
    return np.stack(xs), np.stack(hs), np.asarray(ys, dtype=np.float32), kept


class MLP(nn.Module):
    def __init__(self, input_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.10),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
        )

    def forward(self, x, h=None):
        return self.net(x).squeeze(-1)


class HistoryGRU(nn.Module):
    def __init__(self, input_dim: int, hist_dim: int):
        super().__init__()
        self.gru = nn.GRU(hist_dim, 64, batch_first=True)
        self.head = nn.Sequential(nn.Linear(input_dim + 64, 160), nn.ReLU(), nn.Linear(160, 1))

    def forward(self, x, h):
        _, state = self.gru(h)
        return self.head(torch.cat([x, state[-1]], dim=-1)).squeeze(-1)


class SmallHistoryTransformer(nn.Module):
    def __init__(self, input_dim: int, hist_dim: int):
        super().__init__()
        self.proj = nn.Linear(hist_dim, 64)
        layer = nn.TransformerEncoderLayer(d_model=64, nhead=4, dim_feedforward=128, dropout=0.05, batch_first=True)
        self.enc = nn.TransformerEncoder(layer, num_layers=2)
        self.head = nn.Sequential(nn.Linear(input_dim + 64, 160), nn.ReLU(), nn.Linear(160, 1))

    def forward(self, x, h):
        encoded = self.enc(self.proj(h)).mean(dim=1)
        return self.head(torch.cat([x, encoded], dim=-1)).squeeze(-1)


def split_indices(rows: list[dict[str, Any]], y: np.ndarray, seed: int):
    rng = random.Random(seed)
    by_task = defaultdict(list)
    for idx, row in enumerate(rows):
        by_task[metadata_group(row, "task_name")].append(idx)
    tasks = list(by_task)
    rng.shuffle(tasks)
    test_tasks = set(tasks[: max(1, len(tasks) // 5)])
    train, val, test = [], [], []
    for task, idxs in by_task.items():
        rng.shuffle(idxs)
        if task in test_tasks:
            test.extend(idxs)
        else:
            n_val = max(1, int(0.15 * len(idxs)))
            val.extend(idxs[:n_val])
            train.extend(idxs[n_val:])
    if not train or not val or not test:
        idxs = list(range(len(rows)))
        rng.shuffle(idxs)
        a = int(0.70 * len(idxs))
        b = int(0.85 * len(idxs))
        train, val, test = idxs[:a], idxs[a:b], idxs[b:]
    return train, val, test


def auc_roc(y, p):
    y = np.asarray(y)
    p = np.asarray(p)
    pos = y == 1
    neg = y == 0
    if pos.sum() == 0 or neg.sum() == 0:
        return None
    order = np.argsort(p)
    ranks = np.empty_like(order, dtype=np.float64)
    ranks[order] = np.arange(1, len(p) + 1)
    return float((ranks[pos].sum() - pos.sum() * (pos.sum() + 1) / 2) / (pos.sum() * neg.sum()))


def auc_pr(y, p):
    y = np.asarray(y)
    p = np.asarray(p)
    if y.sum() == 0:
        return None
    order = np.argsort(-p)
    yy = y[order]
    tp = np.cumsum(yy)
    precision = tp / (np.arange(len(yy)) + 1)
    return float((precision * yy).sum() / max(1, yy.sum()))


def ece_score(y, p, bins: int = 10):
    y = np.asarray(y)
    p = np.asarray(p)
    ece = 0.0
    for i in range(bins):
        lo, hi = i / bins, (i + 1) / bins
        mask = (p >= lo) & (p < hi if i < bins - 1 else p <= hi)
        if mask.any():
            ece += float(mask.mean() * abs(p[mask].mean() - y[mask].mean()))
    return ece


def metrics(y, p):
    out = {
        "n": int(len(y)),
        "bad_rate": float(np.mean(y)) if len(y) else None,
        "auroc_bad": auc_roc(y, p),
        "auprc_bad": auc_pr(y, p),
        "brier": float(np.mean((p - y) ** 2)) if len(y) else None,
        "ece_10": ece_score(y, p) if len(y) else None,
        "thresholds": {},
    }
    for thr in [0.3, 0.5, 0.7, 0.8, 0.9]:
        pred = p >= thr
        tp = int(((pred == 1) & (y == 1)).sum())
        fp = int(((pred == 1) & (y == 0)).sum())
        fn = int(((pred == 0) & (y == 1)).sum())
        out["thresholds"][str(thr)] = {
            "precision_bad": float(tp / (tp + fp)) if tp + fp else None,
            "recall_bad": float(tp / (tp + fn)) if tp + fn else None,
            "accepted_safe_fraction": float((~pred).mean()) if len(y) else None,
        }
    return out


def train_one(name: str, x: np.ndarray, h: np.ndarray, y: np.ndarray, rows: list[dict[str, Any]], outdir: Path, epochs: int, seed: int):
    train_idx, val_idx, test_idx = split_indices(rows, y, seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if name in {"action_only_mlp", "context_action_mlp"}:
        model = MLP(x.shape[1]).to(device)
    elif name == "history_gru_k8":
        model = HistoryGRU(x.shape[1], h.shape[2]).to(device)
    else:
        model = SmallHistoryTransformer(x.shape[1], h.shape[2]).to(device)
    pos = float(y[train_idx].sum())
    neg = float(len(train_idx) - pos)
    pos_weight = torch.tensor([neg / max(pos, 1.0)], device=device)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    ds = TensorDataset(torch.tensor(x[train_idx]), torch.tensor(h[train_idx]), torch.tensor(y[train_idx]))
    loader = DataLoader(ds, batch_size=256, shuffle=True)
    best = {"val_auprc_bad": -1.0, "epoch": -1}
    outdir.mkdir(parents=True, exist_ok=True)
    ckpt = outdir / f"{name}.pt"
    for epoch in range(epochs):
        model.train()
        for xb, hb, yb in loader:
            xb, hb, yb = xb.to(device), hb.to(device), yb.to(device)
            opt.zero_grad(set_to_none=True)
            loss = loss_fn(model(xb, hb), yb)
            loss.backward()
            opt.step()
        val = predict(model, x[val_idx], h[val_idx], device)
        score = auc_pr(y[val_idx], val) or -1.0
        if score >= best["val_auprc_bad"]:
            best = {"val_auprc_bad": score, "epoch": epoch}
            torch.save({"model": model.state_dict(), "baseline": name, "input_dim": x.shape[1], "hist_dim": h.shape[2]}, ckpt)
    model.eval()
    if ckpt.exists():
        state = torch.load(ckpt, map_location=device)
        model.load_state_dict(state["model"])
    result = {
        "baseline": name,
        "best_epoch": best["epoch"],
        "checkpoint": str(ckpt),
        "train": metrics(y[train_idx], predict(model, x[train_idx], h[train_idx], device)),
        "calib": metrics(y[val_idx], predict(model, x[val_idx], h[val_idx], device)),
        "test_unseen_task": metrics(y[test_idx], predict(model, x[test_idx], h[test_idx], device)),
        "split_counts": {"train": len(train_idx), "calib": len(val_idx), "test_unseen_task": len(test_idx)},
    }
    return result


@torch.no_grad()
def predict(model, x, h, device):
    model.eval()
    outs = []
    for start in range(0, len(x), 512):
        xb = torch.tensor(x[start:start + 512], dtype=torch.float32, device=device)
        hb = torch.tensor(h[start:start + 512], dtype=torch.float32, device=device)
        outs.append(torch.sigmoid(model(xb, hb)).cpu().numpy())
    return np.concatenate(outs) if outs else np.asarray([], dtype=np.float32)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", nargs="+", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--epochs", type=int, default=12)
    parser.add_argument("--seed", type=int, default=9)
    parser.add_argument("--min-samples", type=int, default=5000)
    parser.add_argument("--subtype-filter", default="all", choices=["all", "action_specific", "state_context"])
    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    rows = load_rows(args.data)
    labels = Counter(final_label(r) for r in rows)
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    eligible = sum(1 for r in rows if final_label(r) in {LABEL_GOOD, LABEL_BAD})
    if eligible < args.min_samples:
        summary = {"status": "not_enough_samples", "eligible_samples": eligible, "min_samples": args.min_samples, "label_counts": dict(labels)}
        (outdir / "training_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
        print(json.dumps(summary, indent=2, sort_keys=True), flush=True)
        return
    results = {"status": "ok", "label_counts": dict(labels), "eligible_samples": eligible, "subtype_filter": args.subtype_filter, "baselines": {}}
    for baseline in ["action_only_mlp", "context_action_mlp", "history_gru_k8", "small_history_transformer_k8"]:
        arrays = build_arrays(rows, baseline, subtype_filter=args.subtype_filter)
        if arrays is None:
            results["baselines"][baseline] = {"status": "no_data"}
            continue
        x, h, y, kept = arrays
        if len(np.unique(y)) < 2:
            results["baselines"][baseline] = {"status": "one_class_only", "n": int(len(y))}
            continue
        results["baselines"][baseline] = train_one(baseline, x, h, y, kept, outdir / baseline, args.epochs, args.seed)
        print(json.dumps({"finished": baseline, "metrics": results["baselines"][baseline]["test_unseen_task"]}, sort_keys=True), flush=True)
    (outdir / "training_summary.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
