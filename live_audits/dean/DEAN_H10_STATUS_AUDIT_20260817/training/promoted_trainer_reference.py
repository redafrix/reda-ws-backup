#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import random
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, average_precision_score, f1_score, precision_recall_curve, roc_auc_score
from torch.utils.data import DataLoader, Dataset


TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]
K_HISTORY = 16


def read_jsonl(path: Path):
    with path.open() as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                yield line_no, json.loads(line)


def pad_flat(value: Any, dim: int) -> np.ndarray:
    arr = np.asarray(value if value is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(dim, dtype=np.float32)
    n = min(dim, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def pad_seq(value: Any, steps: int = 10, dim: int = 7) -> np.ndarray:
    arr = np.asarray(value if value is not None else [], dtype=np.float32)
    out = np.zeros((steps, dim), dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, dim) if arr.size % dim == 0 else arr.reshape(1, -1)
    if arr.ndim == 2:
        s = min(steps, arr.shape[0])
        d = min(dim, arr.shape[1])
        out[:s, :d] = arr[:s, :d]
    return out


def compute_ace_metrics(candidates: Any) -> np.ndarray:
    arr = np.asarray(candidates if candidates is not None else [], dtype=np.float32)
    out = np.zeros(7, dtype=np.float32)
    if arr.ndim != 3 or arr.shape[0] < 2:
        return out
    flat = arr.reshape(arr.shape[0], -1)
    centered = flat - flat.mean(axis=0, keepdims=True)
    per_candidate_l2 = np.linalg.norm(centered, axis=1)
    diffs = flat[:, None, :] - flat[None, :, :]
    pairwise = np.linalg.norm(diffs, axis=-1)
    tr = arr[:, :, :3].reshape(arr.shape[0], -1)
    rot = arr[:, :, 3:6].reshape(arr.shape[0], -1)
    grip = arr[:, :, 6:7].reshape(arr.shape[0], -1)
    std_all = arr.std(axis=0)
    out[0] = float(np.log(np.mean(per_candidate_l2) + 1e-6))
    out[1] = float(pairwise[np.triu_indices(arr.shape[0], 1)].mean())
    out[2] = float(std_all.mean())
    out[3] = float(tr.std(axis=0).mean())
    out[4] = float(rot.std(axis=0).mean())
    out[5] = float(grip.std(axis=0).mean())
    out[6] = float(flat.std(axis=0).mean())
    return np.nan_to_num(out, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32)


def action_stats(action: np.ndarray) -> np.ndarray:
    return np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)


def selected_unc(row: dict[str, Any]) -> np.ndarray:
    vals = pad_flat(row.get("simvla_uncertainty_49d"), 49)
    return vals[TOPK8_DIMS].astype(np.float32)


def current_proprio(row: dict[str, Any]) -> np.ndarray:
    current = row.get("current") or {}
    return pad_flat(current.get("proprio"), 8)


@dataclass
class FeatRow:
    episode_id: str
    suite: str
    task_id: int
    timestep: int
    y: float
    history: np.ndarray
    action: np.ndarray
    static: np.ndarray


def source_label(row: dict[str, Any]) -> float:
    if "parent_failed_or_timeout" in row:
        return 1.0 if bool(row["parent_failed_or_timeout"]) else 0.0
    outcome = str(row.get("episode_outcome") or row.get("outcome") or "").lower()
    return 1.0 if ("fail" in outcome or "timeout" in outcome) else 0.0


def load_goal_source(path: Path, max_rows: int | None = None) -> list[FeatRow]:
    rows: list[FeatRow] = []
    hist_by_ep: dict[str, deque[tuple[np.ndarray, np.ndarray, np.ndarray]]] = defaultdict(lambda: deque(maxlen=K_HISTORY))
    for line_no, row in read_jsonl(path):
        if max_rows is not None and len(rows) >= max_rows:
            break
        eid = str(row["episode_id"])
        proprio = current_proprio(row)
        executed = pad_flat(row.get("executed_action"), 7)
        ace = compute_ace_metrics(row.get("ace_candidate_chunks_normalized"))
        action = pad_seq(row.get("main_candidate_action_chunk_normalized"), 10, 7)
        static = np.concatenate([action_stats(action), ace, proprio, selected_unc(row)]).astype(np.float32)
        hist = np.zeros((K_HISTORY, 21), dtype=np.float32)
        past = list(hist_by_ep[eid])
        offset = K_HISTORY - len(past)
        for i, (hp, ha, hace) in enumerate(past):
            hist[offset + i] = np.concatenate([hp, ha, hace[:6]]).astype(np.float32)
        rows.append(
            FeatRow(
                episode_id=eid,
                suite=str(row.get("suite", "libero_goal")),
                task_id=int(row.get("task_id", -1)),
                timestep=int(row.get("timestep", 0)),
                y=source_label(row),
                history=hist,
                action=action,
                static=static,
            )
        )
        hist_by_ep[eid].append((proprio, executed, ace))
        if line_no % 100000 == 0:
            print(f"[load source] line={line_no} rows={len(rows)}", flush=True)
    return rows


def load_target_episode_labels(summary_path: Path) -> dict[str, float]:
    labels: dict[str, float] = {}
    for _, row in read_jsonl(summary_path):
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        labels[eid] = 0.0 if bool(row.get("success")) else 1.0
    return labels


def find_dataset_files(dataset_root: Path) -> tuple[Path, Path]:
    candidates = [
        (dataset_root / "fiper_receding_samples.jsonl", dataset_root / "episode_summaries.jsonl"),
        (dataset_root / "worker_0" / "fiper_receding_samples.jsonl", dataset_root / "worker_0" / "episode_summaries.jsonl"),
        (dataset_root / "query_samples.jsonl", dataset_root / "episode_summaries.jsonl"),
        (dataset_root / "worker_0" / "query_samples.jsonl", dataset_root / "worker_0" / "episode_summaries.jsonl"),
    ]
    for rows_path, summary_path in candidates:
        if rows_path.exists() and summary_path.exists():
            return rows_path, summary_path
    raise FileNotFoundError(f"could not find rows+summary JSONL files under {dataset_root}")


def load_goal_object_target(query_path: Path, summary_path: Path, max_rows: int | None = None) -> list[FeatRow]:
    labels = load_target_episode_labels(summary_path)
    rows: list[FeatRow] = []
    hist_by_ep: dict[str, deque[tuple[np.ndarray, np.ndarray, np.ndarray]]] = defaultdict(lambda: deque(maxlen=K_HISTORY))
    for line_no, row in read_jsonl(query_path):
        if max_rows is not None and len(rows) >= max_rows:
            break
        eid = str(row.get("episode_id") or row.get("episode_uid"))
        if eid not in labels:
            continue
        proprio = current_proprio(row)
        executed = pad_flat(row.get("executed_action"), 7)
        ace = compute_ace_metrics(row.get("ace_candidate_chunks_normalized"))
        action = pad_seq(row.get("main_candidate_action_chunk_normalized"), 10, 7)
        static = np.concatenate([action_stats(action), ace, proprio, selected_unc(row)]).astype(np.float32)
        hist = np.zeros((K_HISTORY, 21), dtype=np.float32)
        past = list(hist_by_ep[eid])
        offset = K_HISTORY - len(past)
        for i, (hp, ha, hace) in enumerate(past):
            hist[offset + i] = np.concatenate([hp, ha, hace[:6]]).astype(np.float32)
        rows.append(
            FeatRow(
                episode_id=eid,
                suite=str(row.get("suite", "libero_goal_object")),
                task_id=int(row.get("task_id", -1)),
                timestep=int(row.get("timestep", 0)),
                y=labels[eid],
                history=hist,
                action=action,
                static=static,
            )
        )
        hist_by_ep[eid].append((proprio, executed, ace))
        if line_no % 100000 == 0:
            print(f"[load target] line={line_no} rows={len(rows)}", flush=True)
    return rows


def split_source_by_episode(rows: list[FeatRow], seed: int = 20260622):
    by_ep: dict[str, list[FeatRow]] = defaultdict(list)
    ep_label: dict[str, float] = {}
    for r in rows:
        by_ep[r.episode_id].append(r)
        ep_label[r.episode_id] = max(ep_label.get(r.episode_id, 0.0), r.y)
    success = [e for e, y in ep_label.items() if y < 0.5]
    failure = [e for e, y in ep_label.items() if y >= 0.5]
    rng = random.Random(seed)
    rng.shuffle(success)
    rng.shuffle(failure)

    def cut(eps: list[str]):
        n = len(eps)
        n_train = int(round(n * 0.70))
        n_val = int(round(n * 0.15))
        return eps[:n_train], eps[n_train:n_train + n_val], eps[n_train + n_val:]

    s_train, s_val, s_test = cut(success)
    f_train, f_val, f_test = cut(failure)
    splits = {
        "train": set(s_train + f_train),
        "val": set(s_val + f_val),
        "test": set(s_test + f_test),
    }
    return {name: [r for ep in eps for r in by_ep[ep]] for name, eps in splits.items()}, {k: sorted(v) for k, v in splits.items()}


def arrays(rows: list[FeatRow]):
    h = np.stack([r.history for r in rows]).astype(np.float32)
    a = np.stack([r.action for r in rows]).astype(np.float32)
    st = np.stack([r.static for r in rows]).astype(np.float32)
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    return h, a, st, y


def fit_std(x: np.ndarray, axes) -> dict[str, np.ndarray]:
    mean = x.mean(axis=axes, keepdims=True).astype(np.float32)
    std = x.std(axis=axes, keepdims=True).astype(np.float32)
    std = np.maximum(std, 1e-6)
    return {"mean": mean, "std": std}


def apply_std(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return ((x - stats["mean"]) / stats["std"]).astype(np.float32)


class SeqDataset(Dataset):
    def __init__(self, h, a, st, y=None):
        self.h = torch.as_tensor(h, dtype=torch.float32)
        self.a = torch.as_tensor(a, dtype=torch.float32)
        self.st = torch.as_tensor(st, dtype=torch.float32)
        self.y = None if y is None else torch.as_tensor(y, dtype=torch.float32)

    def __len__(self):
        return int(self.h.shape[0])

    def __getitem__(self, idx):
        batch = {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}
        if self.y is None:
            return batch
        return batch, self.y[idx]


class SeqRiskModel(nn.Module):
    def __init__(self, hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, dropout=0.1):
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu")
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(layer, layers)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch):
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        b = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(b, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def move(batch, device):
    return {k: v.to(device, non_blocking=True) for k, v in batch.items()}


def predict(model, h, a, st, device, batch_size=2048):
    ds = SeqDataset(h, a, st)
    loader = DataLoader(ds, batch_size=batch_size, shuffle=False)
    out = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            logits = model(move(batch, device))
            out.append(torch.sigmoid(logits).detach().cpu().numpy())
    return np.concatenate(out).astype(np.float32)


def threshold_table(y_val: np.ndarray, s_val: np.ndarray) -> dict[str, float]:
    precision, recall, thresholds = precision_recall_curve(y_val, s_val)
    f1 = 2 * precision * recall / np.maximum(precision + recall, 1e-9)
    if len(thresholds):
        idx = int(np.nanargmax(f1[:-1] if len(f1) > len(thresholds) else f1[: len(thresholds)]))
        best = float(thresholds[idx])
    else:
        best = 0.5
    success_scores = s_val[y_val < 0.5]
    return {
        "best_val_f1": best,
        "q90_success": float(np.quantile(success_scores, 0.90)) if len(success_scores) else 0.5,
        "q95_success": float(np.quantile(success_scores, 0.95)) if len(success_scores) else 0.5,
        "q99_success": float(np.quantile(success_scores, 0.99)) if len(success_scores) else 0.5,
        "fixed_0.5": 0.5,
    }


def step_metrics(y: np.ndarray, scores: np.ndarray, threshold: float) -> dict[str, float]:
    pred = (scores >= threshold).astype(np.int32)
    yb = y.astype(np.int32)
    tp = int(((pred == 1) & (yb == 1)).sum())
    tn = int(((pred == 0) & (yb == 0)).sum())
    fp = int(((pred == 1) & (yb == 0)).sum())
    fn = int(((pred == 0) & (yb == 1)).sum())
    return {
        "auroc": float(roc_auc_score(yb, scores)) if len(set(yb.tolist())) == 2 else 0.5,
        "auprc": float(average_precision_score(yb, scores)) if len(set(yb.tolist())) == 2 else float(yb.mean()),
        "f1": float(f1_score(yb, pred, zero_division=0)),
        "accuracy": float(accuracy_score(yb, pred)),
        "fpr": float(fp / max(1, fp + tn)),
        "fnr": float(fn / max(1, fn + tp)),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
    }


def episode_metrics(rows: list[FeatRow], scores: np.ndarray, threshold: float) -> dict[str, Any]:
    by_ep: dict[str, list[tuple[FeatRow, float]]] = defaultdict(list)
    for r, s in zip(rows, scores):
        by_ep[r.episode_id].append((r, float(s)))
    succ_eps = fail_eps = false_alarm = detected = det25 = det50 = 0
    det_fracs: list[float] = []
    for eid, vals in by_ep.items():
        vals.sort(key=lambda x: x[0].timestep)
        y = max(v[0].y for v in vals)
        hit_positions = [i for i, (_, s) in enumerate(vals) if s >= threshold]
        n = len(vals)
        if y >= 0.5:
            fail_eps += 1
            if hit_positions:
                detected += 1
                first = hit_positions[0]
                frac = (first + 1) / max(1, n)
                det_fracs.append(frac)
                if frac <= 0.25:
                    det25 += 1
                if frac <= 0.50:
                    det50 += 1
        else:
            succ_eps += 1
            if hit_positions:
                false_alarm += 1
    return {
        "episodes": len(by_ep),
        "success_episodes": succ_eps,
        "failure_episodes": fail_eps,
        "episode_false_alarm_rate": false_alarm / max(1, succ_eps),
        "failure_detection_rate": detected / max(1, fail_eps),
        "det_at_25": det25 / max(1, fail_eps),
        "det_at_50": det50 / max(1, fail_eps),
        "mean_detection_fraction": float(np.mean(det_fracs)) if det_fracs else None,
        "false_alarm_count": false_alarm,
        "detected_failure_count": detected,
    }


def summarize_rows(rows: list[FeatRow]) -> dict[str, Any]:
    eps: dict[str, float] = {}
    tasks = Counter()
    for r in rows:
        eps[r.episode_id] = max(eps.get(r.episode_id, 0.0), r.y)
        tasks[r.task_id] += 1
    failures = sum(1 for y in eps.values() if y >= 0.5)
    return {
        "rows": len(rows),
        "episodes": len(eps),
        "failure_episodes": failures,
        "success_episodes": len(eps) - failures,
        "row_task_counts": dict(sorted(tasks.items())),
    }


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-jsonl", required=True)
    ap.add_argument("--target-root", required=True)
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--epochs", type=int, default=10)
    ap.add_argument("--batch-size", type=int, default=512)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--weight-decay", type=float, default=1e-4)
    ap.add_argument("--max-source-rows", type=int, default=0)
    ap.add_argument("--max-target-rows", type=int, default=0)
    args = ap.parse_args()

    started = time.time()
    out = Path(args.output_root)
    out.mkdir(parents=True, exist_ok=True)
    source_path = Path(args.source_jsonl)
    target_root = Path(args.target_root)
    target_query, target_summary = find_dataset_files(target_root)

    print("[1/6] loading source plain-goal dataset", flush=True)
    source_rows = load_goal_source(source_path, args.max_source_rows or None)
    print("[2/6] splitting source by episode", flush=True)
    source_splits, split_eps = split_source_by_episode(source_rows)
    del source_rows
    print("[3/6] loading target goal-object dataset", flush=True)
    target_rows = load_goal_object_target(target_query, target_summary, args.max_target_rows or None)

    h_train_raw, a_train_raw, st_train_raw, y_train = arrays(source_splits["train"])
    h_val_raw, a_val_raw, st_val_raw, y_val = arrays(source_splits["val"])
    h_test_raw, a_test_raw, st_test_raw, y_test = arrays(source_splits["test"])
    h_ood_raw, a_ood_raw, st_ood_raw, y_ood = arrays(target_rows)

    stats = {
        "history": fit_std(h_train_raw, axes=(0, 1)),
        "action": fit_std(a_train_raw, axes=(0, 1)),
        "static": fit_std(st_train_raw, axes=0),
    }
    h_train, a_train, st_train = apply_std(h_train_raw, stats["history"]), apply_std(a_train_raw, stats["action"]), apply_std(st_train_raw, stats["static"])
    h_val, a_val, st_val = apply_std(h_val_raw, stats["history"]), apply_std(a_val_raw, stats["action"]), apply_std(st_val_raw, stats["static"])
    h_test, a_test, st_test = apply_std(h_test_raw, stats["history"]), apply_std(a_test_raw, stats["action"]), apply_std(st_test_raw, stats["static"])
    h_ood, a_ood, st_ood = apply_std(h_ood_raw, stats["history"]), apply_std(a_ood_raw, stats["action"]), apply_std(st_ood_raw, stats["static"])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SeqRiskModel(static_dim=st_train.shape[-1]).to(device)
    neg = float((y_train < 0.5).sum())
    pos = float((y_train >= 0.5).sum())
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([max(1.0, neg / max(1.0, pos))], device=device))
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    train_loader = DataLoader(SeqDataset(h_train, a_train, st_train, y_train), batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(SeqDataset(h_val, a_val, st_val, y_val), batch_size=args.batch_size, shuffle=False)

    print("[4/6] training", flush=True)
    history = []
    best_state = None
    best_auprc = -1.0
    best_epoch = 0
    for epoch in range(1, args.epochs + 1):
        model.train()
        losses = []
        for batch, yb in train_loader:
            batch = move(batch, device)
            yb = yb.to(device)
            opt.zero_grad(set_to_none=True)
            loss = loss_fn(model(batch), yb)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            losses.append(float(loss.detach().cpu()))
        val_scores = predict(model, h_val, a_val, st_val, device, args.batch_size * 2)
        val_auprc = float(average_precision_score(y_val.astype(int), val_scores)) if len(set(y_val.astype(int).tolist())) == 2 else 0.0
        val_auroc = float(roc_auc_score(y_val.astype(int), val_scores)) if len(set(y_val.astype(int).tolist())) == 2 else 0.5
        rec = {"epoch": epoch, "train_loss": float(np.mean(losses)), "val_auprc": val_auprc, "val_auroc": val_auroc}
        history.append(rec)
        print(rec, flush=True)
        if val_auprc > best_auprc:
            best_auprc = val_auprc
            best_epoch = epoch
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
    if best_state is not None:
        model.load_state_dict(best_state)

    print("[5/6] scoring", flush=True)
    val_scores = predict(model, h_val, a_val, st_val, device, args.batch_size * 2)
    test_scores = predict(model, h_test, a_test, st_test, device, args.batch_size * 2)
    ood_scores = predict(model, h_ood, a_ood, st_ood, device, args.batch_size * 2)
    thresholds = threshold_table(y_val, val_scores)

    results = {
        "experiment": "simvla_goal_train_to_goal_object_ood_topk8_20260622",
        "source": str(source_path),
        "target_root": str(target_root),
        "feature_schema": {
            "history_dim": 21,
            "history_steps": 16,
            "action_shape": [10, 7],
            "static_dim": int(st_train.shape[-1]),
            "static_layout": "action_stats_28 + ace_7 + proprio_8 + selected_uncertainty_topk8_8",
            "selected_uncertainty_dims": TOPK8_DIMS,
            "explicit_task_id_input": False,
            "explicit_timestep_input": False,
        },
        "dataset_summary": {
            "source_train": summarize_rows(source_splits["train"]),
            "source_val": summarize_rows(source_splits["val"]),
            "source_test": summarize_rows(source_splits["test"]),
            "target_goal_object_full": summarize_rows(target_rows),
        },
        "best_epoch": best_epoch,
        "train_history": history,
        "thresholds": thresholds,
        "metrics": {},
        "runtime_seconds": time.time() - started,
    }
    for name, th in thresholds.items():
        results["metrics"][name] = {
            "source_test_step": step_metrics(y_test, test_scores, th),
            "source_test_episode": episode_metrics(source_splits["test"], test_scores, th),
            "goal_object_ood_step": step_metrics(y_ood, ood_scores, th),
            "goal_object_ood_episode": episode_metrics(target_rows, ood_scores, th),
        }

    print("[6/6] writing artifacts", flush=True)
    write_json(out / "results.json", results)
    write_json(out / "split_episode_ids.json", split_eps)
    np.savez_compressed(out / "scores.npz", y_val=y_val, val_scores=val_scores, y_test=y_test, test_scores=test_scores, y_ood=y_ood, ood_scores=ood_scores)
    torch.save(model.state_dict(), out / "model.pt")
    serial_stats = {k: {kk: vv.tolist() for kk, vv in v.items()} for k, v in stats.items()}
    write_json(out / "normalization.json", serial_stats)
    report_lines = [
        "# SimVLA Goal to Goal-Object OOD Risk Evaluation",
        "",
        f"- Source train dataset: `{source_path}`",
        f"- Target OOD dataset: `{target_root}`",
        f"- Best epoch: `{best_epoch}`",
        f"- Runtime seconds: `{results['runtime_seconds']:.1f}`",
        "",
        "## Dataset Summary",
        "",
        "| Split | Rows | Episodes | Success eps | Failure eps |",
        "|---|---:|---:|---:|---:|",
    ]
    for key, val in results["dataset_summary"].items():
        report_lines.append(f"| {key} | {val['rows']} | {val['episodes']} | {val['success_episodes']} | {val['failure_episodes']} |")
    report_lines += ["", "## Threshold Metrics", "", "| Threshold | Value | Source AUROC | Source AUPRC | Source false alarm | OOD AUROC | OOD AUPRC | OOD false alarm | OOD failure det | OOD Det@25 | OOD Det@50 |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for name, th in thresholds.items():
        m = results["metrics"][name]
        st = m["source_test_step"]
        se = m["source_test_episode"]
        ot = m["goal_object_ood_step"]
        oe = m["goal_object_ood_episode"]
        report_lines.append(
            f"| {name} | {th:.4f} | {st['auroc']:.4f} | {st['auprc']:.4f} | {100*se['episode_false_alarm_rate']:.2f}% | "
            f"{ot['auroc']:.4f} | {ot['auprc']:.4f} | {100*oe['episode_false_alarm_rate']:.2f}% | "
            f"{100*oe['failure_detection_rate']:.2f}% | {100*oe['det_at_25']:.2f}% | {100*oe['det_at_50']:.2f}% |"
        )
    report_lines += [
        "",
        "## Legitimacy Notes",
        "",
        "- Train split uses only plain `libero_goal` episodes.",
        "- Full OOD test uses transferred `libero_goal_object` episodes and is never used for training or threshold calibration.",
        "- Inputs exclude explicit task id and explicit timestep.",
        "- Feature schema mirrors the H10 TopK8 SimVLA detector shape: `history=16x21`, `action=10x7`, `static=51`.",
    ]
    (out / "SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md").write_text("\n".join(report_lines) + "\n")
    print(f"DONE report={out / 'SIMVLA_GOAL_TO_GOAL_OBJECT_OOD_REPORT_20260622.md'}", flush=True)


if __name__ == "__main__":
    main()
