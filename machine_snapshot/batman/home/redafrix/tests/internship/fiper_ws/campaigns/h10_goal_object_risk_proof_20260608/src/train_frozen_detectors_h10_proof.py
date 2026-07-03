#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset


FIXED_TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]
FEATURE_VARIANTS = ["base", "unc_topk8"]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def read_jsonl(path: Path):
    with path.open() as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n")


def pad_flat(values: Any, size: int) -> np.ndarray:
    arr = np.asarray(values if values is not None else [], dtype=np.float32).reshape(-1)
    out = np.zeros(size, dtype=np.float32)
    n = min(size, arr.size)
    if n:
        out[:n] = arr[:n]
    return out


def pad_seq(values: Any, rows: int, cols: int) -> np.ndarray:
    arr = np.asarray(values if values is not None else [], dtype=np.float32)
    if arr.size == 0:
        return np.zeros((rows, cols), dtype=np.float32)
    if arr.ndim == 1:
        arr = arr.reshape(-1, cols) if arr.size % cols == 0 else arr.reshape(1, -1)
    out = np.zeros((rows, cols), dtype=np.float32)
    rr = min(rows, arr.shape[0])
    cc = min(cols, arr.shape[1])
    out[:rr, :cc] = arr[:rr, :cc]
    return out


def compute_ace_metrics(ace_chunks_normalized: Any) -> np.ndarray:
    chunks = np.asarray(ace_chunks_normalized, dtype=np.float32)
    if chunks.ndim != 3 or chunks.shape[0] < 2:
        return np.zeros(7, dtype=np.float32)
    n_seeds = chunks.shape[0]
    flat = chunks.reshape(n_seeds, -1)
    cov = np.cov(flat, rowvar=False)
    eps = 1e-6
    _sign, logdet = np.linalg.slogdet(cov + eps * np.eye(flat.shape[1]))
    entropy = 0.5 * (flat.shape[1] * (1.0 + np.log(2 * np.pi)) + logdet)
    diffs = flat[:, None, :] - flat[None, :, :]
    dists = np.sqrt(np.sum(diffs * diffs, axis=-1))
    mean_pairwise = np.sum(dists) / (n_seeds * (n_seeds - 1))
    per_step_std = float(np.mean(np.std(chunks, axis=0)))
    trans_std = float(np.mean(np.std(chunks[:, :, :3], axis=0)))
    rot_std = float(np.mean(np.std(chunks[:, :, 3:6], axis=0)))
    grip_std = float(np.mean(np.std(chunks[:, :, 6:], axis=0)))
    flat_std = float(np.mean(np.std(flat, axis=0)))
    return np.asarray([entropy, mean_pairwise, per_step_std, trans_std, rot_std, grip_std, flat_std], dtype=np.float32)


def uncertainty_summary_features(uncertainty: np.ndarray) -> np.ndarray:
    def summarize(vec: np.ndarray) -> list[float]:
        vec = np.asarray(vec, dtype=np.float32).reshape(-1)
        if vec.size == 0:
            return [0.0] * 10
        return [
            float(np.mean(vec)),
            float(np.std(vec)),
            float(np.min(vec)),
            float(np.max(vec)),
            float(np.median(vec)),
            float(np.quantile(vec, 0.90)),
            float(np.mean(np.abs(vec))),
            float(np.max(np.abs(vec))),
            float(np.linalg.norm(vec) / math.sqrt(max(1, vec.size))),
            float(np.mean(vec > 0.0)),
        ]

    unc = uncertainty[:49]
    delta = uncertainty[49:98]
    return np.asarray(summarize(unc) + summarize(delta), dtype=np.float32)


def auroc_binary(y_true: np.ndarray, scores: np.ndarray) -> float:
    y = y_true.astype(np.int32)
    pos = scores[y == 1]
    neg = scores[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return 0.5
    order = np.argsort(scores)
    ranks = np.empty_like(order, dtype=np.float64)
    ranks[order] = np.arange(1, len(scores) + 1)
    pos_ranks = ranks[y == 1].sum()
    return float((pos_ranks - len(pos) * (len(pos) + 1) / 2.0) / (len(pos) * len(neg)))


@dataclass(frozen=True)
class EpisodeMeta:
    episode_id: str
    worker: str
    suite: str
    task_id: int
    success: bool
    outcome: str
    num_steps: int
    sweep_idx: int


@dataclass
class RowEx:
    episode_id: str
    timestep: int
    y: float
    history: np.ndarray
    action: np.ndarray
    static_base: np.ndarray
    uncertainty: np.ndarray


def discover_worker_dirs(run_root: Path) -> list[str]:
    workers = sorted(
        path.name
        for path in run_root.iterdir()
        if path.is_dir() and (path / "episode_summaries.jsonl").exists()
    )
    if not workers:
        raise RuntimeError(f"no worker directories with episode_summaries.jsonl under {run_root}")
    return workers


def load_episode_meta(run_root: Path, default_suite: str) -> dict[str, EpisodeMeta]:
    episodes: dict[str, EpisodeMeta] = {}
    duplicates = 0
    for worker_dir in discover_worker_dirs(run_root):
        path = run_root / worker_dir / "episode_summaries.jsonl"
        if not path.exists():
            continue
        for row in read_jsonl(path):
            eid = str(row.get("episode_id") or row.get("episode_uid") or "")
            if not eid:
                continue
            if eid in episodes:
                duplicates += 1
                continue
            suite = str(row.get("suite") or default_suite)
            task_id = int(row.get("task_id"))
            if row.get("outcome") == "error" or row.get("error_message"):
                continue
            episodes[eid] = EpisodeMeta(
                episode_id=eid,
                worker=worker_dir,
                suite=suite,
                task_id=task_id,
                success=bool(row.get("success")),
                outcome=str(row.get("outcome")),
                num_steps=int(row.get("num_steps") or row.get("num_env_steps") or 0),
                sweep_idx=int(row.get("sweep_idx") or row.get("global_episode_index") or 0),
            )
    print(f"Loaded valid episode metadata: {len(episodes)} episodes; duplicate summaries ignored={duplicates}", flush=True)
    return episodes


def split_bool_ood(name: str, ep: EpisodeMeta) -> bool:
    if name in {"random_mixed", "all_tasks_random"}:
        return False
    if name == "ood_suite_libero90":
        return ep.suite == "libero_90"
    if name == "ood_task_holdout":
        if ep.suite == "libero_90":
            return ep.task_id >= 80
        return ep.task_id in {8, 9}
    if name == "ood_last2_taskids":
        return ep.task_id in {8, 9}
    if name == "ood_hard_goal_tasks":
        return ep.task_id in {3, 4, 6, 9}
    raise ValueError(f"unknown split {name}")


def take(items: list[EpisodeMeta], n: int | None) -> list[EpisodeMeta]:
    if n is None:
        return items
    if n <= 0:
        return []
    if len(items) <= n:
        return items
    idx = np.linspace(0, len(items) - 1, num=n, dtype=np.int64)
    return [items[int(i)] for i in idx]


def stratified_seen_buckets(
    seen: list[EpisodeMeta],
    rng: random.Random,
    limits: dict[str, int],
) -> dict[str, set[str]]:
    succ = [e for e in seen if e.success]
    fail = [e for e in seen if not e.success]
    rng.shuffle(succ)
    rng.shuffle(fail)

    def split_class(items: list[EpisodeMeta], train_frac: float, val_frac: float, calib_frac: float):
        n = len(items)
        n_train = int(n * train_frac)
        n_val = int(n * val_frac)
        n_calib = int(n * calib_frac)
        train = items[:n_train]
        val = items[n_train : n_train + n_val]
        calib = items[n_train + n_val : n_train + n_val + n_calib]
        test = items[n_train + n_val + n_calib :]
        return train, val, calib, test

    # H10 proof split policy:
    # - the exact_200 chunk10 run is the only final test set;
    # - continuous chunk10 data is only for train/validation/calibration.
    # Keep success calibration separate because conformal thresholds are defined
    # on successful episodes. Failures are split between train and validation.
    s_train, s_val, s_calib, s_test = split_class(succ, 0.80, 0.10, 0.10)
    f_train, f_val, _f_unused_calib, f_test = split_class(fail, 0.80, 0.20, 0.0)
    s_train = s_train + s_test
    f_train = f_train + f_test
    s_test = []
    f_test = []

    buckets = {
        "success_train_seen": {e.episode_id for e in take(s_train, limits["train_success"])},
        "failure_train_seen": {e.episode_id for e in take(f_train, limits["train_failure"])},
        "success_val_seen": {e.episode_id for e in take(s_val, limits["val_success"])},
        "failure_val_seen": {e.episode_id for e in take(f_val, limits["val_failure"])},
        "success_calib_seen": {e.episode_id for e in take(s_calib, limits["calib_success"])},
        "success_test_seen": {e.episode_id for e in take(s_test, limits["test_success"])},
        "failure_test_seen": {e.episode_id for e in take(f_test, limits["test_failure"])},
    }
    return buckets


def make_split_assignments(
    episodes: dict[str, EpisodeMeta],
    split_name: str,
    seed: int,
    limits: dict[str, int],
) -> dict[str, set[str]]:
    split_offset = int(hashlib.sha256(split_name.encode()).hexdigest()[:8], 16) % 100000
    rng = random.Random(seed + split_offset)
    eps = list(episodes.values())
    rng.shuffle(eps)
    if split_name == "random_mixed":
        seen = eps
        buckets = stratified_seen_buckets(seen, rng, limits)
        buckets["success_test_ood"] = set()
        buckets["failure_eval_ood"] = set()
        return buckets
    if split_name == "all_tasks_random":
        seen = eps
        buckets = stratified_seen_buckets(seen, rng, limits)
        buckets["success_test_ood"] = set()
        buckets["failure_eval_ood"] = set()
        return buckets

    seen = [e for e in eps if not split_bool_ood(split_name, e)]
    ood = [e for e in eps if split_bool_ood(split_name, e)]
    buckets = stratified_seen_buckets(seen, rng, limits)
    ood_success = [e for e in ood if e.success]
    ood_failure = [e for e in ood if not e.success]
    rng.shuffle(ood_success)
    rng.shuffle(ood_failure)
    buckets["success_test_ood"] = {e.episode_id for e in take(ood_success, limits["ood_success"])}
    buckets["failure_eval_ood"] = {e.episode_id for e in take(ood_failure, limits["ood_failure"])}
    return buckets


def fit_seq_standardizer(x: np.ndarray) -> dict[str, np.ndarray]:
    mean = x.reshape(-1, x.shape[-1]).mean(axis=0)
    std = x.reshape(-1, x.shape[-1]).std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}


def fit_standardizer(x: np.ndarray) -> dict[str, np.ndarray]:
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}


def apply_seq_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


def apply_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


def build_rows_for_split(
    run_root: Path,
    episodes: dict[str, EpisodeMeta],
    buckets: dict[str, set[str]],
    history_steps: int,
    cadence: str,
    stride: int,
) -> dict[str, list[RowEx]]:
    episode_to_bucket: dict[str, str] = {}
    for bucket, ids in buckets.items():
        for eid in ids:
            episode_to_bucket[eid] = bucket

    rows_by_bucket: dict[str, list[RowEx]] = {k: [] for k in buckets}
    wanted = set(episode_to_bucket)
    parsed_rows = 0
    used_rows = 0

    for worker_dir in discover_worker_dirs(run_root):
        worker_root = run_root / worker_dir
        path = worker_root / "fiper_receding_samples.jsonl"
        if not path.exists():
            path = worker_root / "query_samples.jsonl"
        if not path.exists():
            continue
        executed_by_query: dict[tuple[str, int], np.ndarray] = {}
        transitions_path = worker_root / "transitions.jsonl"
        if transitions_path.exists():
            for transition in read_jsonl(transitions_path):
                if int(transition.get("action_index_in_chunk") or 0) != 0:
                    continue
                transition_eid = str(transition.get("episode_id") or transition.get("episode_uid") or "")
                transition_query = int(transition.get("query_index") or 0)
                executed_by_query[(transition_eid, transition_query)] = pad_flat(transition.get("executed_action"), 7)
        current_eid = None
        history_buffer: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []
        for raw in read_jsonl(path):
            parsed_rows += 1
            eid = str(raw.get("episode_id") or raw.get("episode_uid") or "")
            if eid != current_eid:
                current_eid = eid
                history_buffer = []
            if eid not in wanted:
                continue
            timestep = int(raw.get("timestep") or 0)
            if cadence == "stride" and timestep % stride != 0:
                continue
            meta = episodes[eid]
            bucket = episode_to_bucket[eid]
            action = pad_seq(raw.get("main_candidate_action_chunk_normalized"), 10, 7)
            ace = compute_ace_metrics(raw.get("ace_candidate_chunks_normalized"))
            current = raw.get("current") or {}
            proprio = pad_flat(current.get("proprio"), 8)
            query_index = int(raw.get("query_index") or 0)
            raw_executed = raw.get("executed_action")
            executed = pad_flat(raw_executed, 7)
            if raw_executed is None and (eid, query_index) in executed_by_query:
                executed = executed_by_query[(eid, query_index)]
            if raw_executed is None and (eid, query_index) not in executed_by_query:
                executed = action[0].copy()
            action_stats = np.concatenate([action[0], action.mean(axis=0), action.std(axis=0), action[-1] - action[0]]).astype(np.float32)
            static_base = np.concatenate([action_stats, ace, proprio]).astype(np.float32)
            unc = pad_flat(raw.get("simvla_uncertainty_49d"), 49)
            delta = pad_flat(raw.get("simvla_uncertainty_delta_49d"), 49)
            uncertainty = np.concatenate([unc, delta]).astype(np.float32)

            hist = np.zeros((history_steps, 21), dtype=np.float32)
            hist_src = history_buffer[-history_steps:]
            offset = history_steps - len(hist_src)
            for i, (h_prop, h_act, h_ace) in enumerate(hist_src):
                hist[offset + i, :] = np.concatenate([h_prop, h_act, h_ace[:6]])

            rows_by_bucket[bucket].append(
                RowEx(
                    episode_id=eid,
                    timestep=timestep,
                    y=0.0 if meta.success else 1.0,
                    history=hist,
                    action=action,
                    static_base=static_base,
                    uncertainty=uncertainty,
                )
            )
            history_buffer.append((proprio, executed, ace))
            used_rows += 1
    print(f"Built rows: parsed={parsed_rows}, used={used_rows}, cadence={cadence}, stride={stride}", flush=True)
    return rows_by_bucket


class SeqDataset(Dataset):
    def __init__(self, h: np.ndarray, a: np.ndarray, st: np.ndarray, y: np.ndarray | None = None) -> None:
        self.h = torch.tensor(h, dtype=torch.float32)
        self.a = torch.tensor(a, dtype=torch.float32)
        self.st = torch.tensor(st, dtype=torch.float32)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float32)

    def __len__(self) -> int:
        return int(self.h.shape[0])

    def __getitem__(self, idx: int):
        batch = {"history": self.h[idx], "action": self.a[idx], "static": self.st[idx]}
        if self.y is None:
            return batch
        return batch, self.y[idx]


class SeqRiskModel(nn.Module):
    def __init__(
        self,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 3,
        heads: int = 4,
        dropout: float = 0.1,
        static_input_dropout: float = 0.0,
    ) -> None:
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(
            width,
            heads,
            width * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(static_input_dropout)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


def make_arrays(rows: list[RowEx], variant: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, list[str], np.ndarray]:
    h = np.stack([r.history for r in rows], axis=0).astype(np.float32)
    a = np.stack([r.action for r in rows], axis=0).astype(np.float32)
    if variant == "unc_topk8":
        dims = np.asarray(FIXED_TOPK8_DIMS, dtype=np.int64)
        st = np.stack([np.concatenate([r.static_base, r.uncertainty[dims]]).astype(np.float32) for r in rows], axis=0)
    elif variant in {"uncertainty", "unc_raw", "unc_raw_dropout"}:
        st = np.stack([np.concatenate([r.static_base, r.uncertainty]).astype(np.float32) for r in rows], axis=0)
    elif variant == "unc_summary":
        st = np.stack([np.concatenate([r.static_base, uncertainty_summary_features(r.uncertainty)]).astype(np.float32) for r in rows], axis=0)
    elif variant == "unc_summary_only":
        st = np.stack([uncertainty_summary_features(r.uncertainty) for r in rows], axis=0).astype(np.float32)
    elif variant == "unc_raw_only":
        st = np.stack([r.uncertainty for r in rows], axis=0).astype(np.float32)
    else:
        st = np.stack([r.static_base for r in rows], axis=0).astype(np.float32)
    y = np.asarray([r.y for r in rows], dtype=np.float32)
    episode_ids = [r.episode_id for r in rows]
    timesteps = np.asarray([r.timestep for r in rows], dtype=np.int32)
    return h, a, st, y, episode_ids, timesteps


def move_batch(batch: dict[str, torch.Tensor], device: torch.device) -> dict[str, torch.Tensor]:
    return {k: v.to(device) for k, v in batch.items()}


def train_model(
    train_rows: list[RowEx],
    val_rows: list[RowEx],
    variant: str,
    args: argparse.Namespace,
    device: torch.device,
) -> tuple[SeqRiskModel, dict[str, dict[str, np.ndarray]], list[dict[str, Any]], int]:
    h_train_raw, a_train_raw, st_train_raw, y_train, _, _ = make_arrays(train_rows, variant)
    h_val_raw, a_val_raw, st_val_raw, y_val, _, _ = make_arrays(val_rows, variant)
    stats = {
        "history": fit_seq_standardizer(h_train_raw),
        "action": fit_seq_standardizer(a_train_raw),
        "static": fit_standardizer(st_train_raw),
    }
    h_train = apply_seq_standardizer(h_train_raw, stats["history"])
    a_train = apply_seq_standardizer(a_train_raw, stats["action"])
    st_train = apply_standardizer(st_train_raw, stats["static"])
    h_val = apply_seq_standardizer(h_val_raw, stats["history"])
    a_val = apply_seq_standardizer(a_val_raw, stats["action"])
    st_val = apply_standardizer(st_val_raw, stats["static"])

    model = SeqRiskModel(
        hist_dim=h_train.shape[-1],
        action_dim=a_train.shape[-1],
        static_dim=st_train.shape[-1],
        width=args.width,
        layers=args.layers,
        heads=args.heads,
        dropout=args.dropout,
        static_input_dropout=args.unc_raw_static_dropout if variant == "unc_raw_dropout" else 0.0,
    ).to(device)
    neg = float(np.sum(y_train == 0))
    pos = float(np.sum(y_train == 1))
    pos_weight = torch.tensor([max(1.0, neg / max(1.0, pos))], dtype=torch.float32, device=device)
    loss_fn = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    train_loader = DataLoader(SeqDataset(h_train, a_train, st_train, y_train), batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(SeqDataset(h_val, a_val, st_val, y_val), batch_size=args.batch_size, shuffle=False)

    best_state = None
    best_auc = -1.0
    best_epoch = 0
    no_improve = 0
    history: list[dict[str, Any]] = []
    for epoch in range(1, args.max_epochs + 1):
        model.train()
        train_losses = []
        for batch, yb in train_loader:
            batch = move_batch(batch, device)
            yb = yb.to(device)
            opt.zero_grad(set_to_none=True)
            logits = model(batch)
            loss = loss_fn(logits, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            opt.step()
            train_losses.append(float(loss.detach().cpu().item()))
        scores, labels = predict_scores_from_loader(model, val_loader, device, want_labels=True)
        auc = auroc_binary(labels, scores)
        val_loss = float(loss_fn(torch.logit(torch.tensor(np.clip(scores, 1e-6, 1 - 1e-6), device=device)), torch.tensor(labels, device=device)).detach().cpu().item())
        rec = {"epoch": epoch, "train_loss": float(np.mean(train_losses)), "val_auc": auc, "val_loss": val_loss}
        history.append(rec)
        print(f"epoch={epoch} variant={variant} train_loss={rec['train_loss']:.4f} val_auc={auc:.4f}", flush=True)
        if auc > best_auc + 1e-4:
            best_auc = auc
            best_epoch = epoch
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= args.patience:
                break
    if best_state is not None:
        model.load_state_dict(best_state)
    return model, stats, history, best_epoch


def predict_scores_from_loader(model: nn.Module, loader: DataLoader, device: torch.device, want_labels: bool = False):
    model.eval()
    scores = []
    labels = []
    with torch.no_grad():
        for item in loader:
            if want_labels:
                batch, yb = item
                labels.append(yb.numpy())
            else:
                batch = item
            batch = move_batch(batch, device)
            s = torch.sigmoid(model(batch)).detach().cpu().numpy()
            scores.append(s)
    scores_np = np.concatenate(scores, axis=0) if scores else np.zeros((0,), dtype=np.float32)
    if want_labels:
        return scores_np, np.concatenate(labels, axis=0) if labels else np.zeros((0,), dtype=np.float32)
    return scores_np


def score_rows(
    model: nn.Module,
    stats: dict[str, dict[str, np.ndarray]],
    rows: list[RowEx],
    variant: str,
    batch_size: int,
    device: torch.device,
) -> tuple[np.ndarray, np.ndarray, list[str], np.ndarray]:
    if not rows:
        return np.zeros((0,), dtype=np.float32), np.zeros((0,), dtype=np.float32), [], np.zeros((0,), dtype=np.int32)
    h_raw, a_raw, st_raw, y, episode_ids, timesteps = make_arrays(rows, variant)
    h = apply_seq_standardizer(h_raw, stats["history"])
    a = apply_seq_standardizer(a_raw, stats["action"])
    st = apply_standardizer(st_raw, stats["static"])
    loader = DataLoader(SeqDataset(h, a, st, None), batch_size=batch_size, shuffle=False)
    return predict_scores_from_loader(model, loader, device), y, episode_ids, timesteps


def episode_masses(scores: np.ndarray, episode_ids: list[str], q: float) -> dict[str, float]:
    masses: dict[str, float] = defaultdict(float)
    for eid, score in zip(episode_ids, scores):
        masses[eid] += max(0.0, float(score) - q)
    return dict(masses)


def calibrate_thresholds(
    scores_by_bucket: dict[str, np.ndarray],
    ids_by_bucket: dict[str, list[str]],
    alpha: float,
    min_conformal_mass: float,
) -> dict[str, float]:
    calib_scores = scores_by_bucket.get("success_calib_seen", np.zeros((0,), dtype=np.float32))
    if calib_scores.size:
        q95 = float(np.quantile(calib_scores, 0.95))
        q99 = float(np.quantile(calib_scores, 0.99))
    else:
        q95 = 0.95
        q99 = 0.99
    val_masses = episode_masses(scores_by_bucket.get("success_val_seen", np.zeros((0,), dtype=np.float32)), ids_by_bucket.get("success_val_seen", []), q95)
    vals = np.asarray(list(val_masses.values()), dtype=np.float32)
    if vals.size:
        conformal = float(np.quantile(vals, 1.0 - alpha))
    else:
        conformal = 0.15
    conformal = max(float(min_conformal_mass), conformal)
    return {"q95": q95, "q99": q99, "conformal_mass": conformal}


def evaluate_bucket(
    bucket: str,
    rows: list[RowEx],
    scores: np.ndarray,
    episode_ids: list[str],
    timesteps: np.ndarray,
    episodes: dict[str, EpisodeMeta],
    thresholds: dict[str, float],
) -> dict[str, Any]:
    by_episode: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for eid, t, s in zip(episode_ids, timesteps, scores):
        by_episode[eid].append((int(t), float(s)))
    triggered = 0
    det25 = 0
    det50 = 0
    first_ratios = []
    final_masses = []
    for eid, vals in by_episode.items():
        vals.sort()
        mass = 0.0
        first_alarm = None
        for t, score in vals:
            mass += max(0.0, score - thresholds["q95"])
            if first_alarm is None and mass >= thresholds["conformal_mass"]:
                first_alarm = t
        final_masses.append(mass)
        if first_alarm is not None:
            triggered += 1
            denom = max(1, episodes[eid].num_steps)
            ratio = first_alarm / denom
            first_ratios.append(ratio)
            if ratio <= 0.25:
                det25 += 1
            if ratio <= 0.50:
                det50 += 1
    n = len(by_episode)
    is_success_bucket = bucket.startswith("success")
    return {
        "episodes": n,
        "rows": len(rows),
        "triggered": triggered,
        "episode_alarm_rate": triggered / n if n else 0.0,
        "success_false_alarm_rate": triggered / n if is_success_bucket and n else None,
        "failure_detection_rate": triggered / n if (not is_success_bucket) and n else None,
        "det_at_25": det25 / n if (not is_success_bucket) and n else None,
        "det_at_50": det50 / n if (not is_success_bucket) and n else None,
        "mean_detection_time": float(np.mean(first_ratios)) if first_ratios else None,
        "mean_final_mass": float(np.mean(final_masses)) if final_masses else None,
    }


def summarize_available(episodes: dict[str, EpisodeMeta]) -> dict[str, Any]:
    by_suite = Counter(e.suite for e in episodes.values())
    by_suite_success = Counter(e.suite for e in episodes.values() if e.success)
    by_suite_fail = Counter(e.suite for e in episodes.values() if not e.success)
    return {
        "valid_episodes": len(episodes),
        "successes": sum(e.success for e in episodes.values()),
        "failures": sum(not e.success for e in episodes.values()),
        "by_suite_total": dict(sorted(by_suite.items())),
        "by_suite_success": dict(sorted(by_suite_success.items())),
        "by_suite_failure": dict(sorted(by_suite_fail.items())),
        "excluded_bad_tasks": [],
    }


def run_job(
    split_name: str,
    variant: str,
    rows_by_bucket: dict[str, list[RowEx]],
    episodes: dict[str, EpisodeMeta],
    args: argparse.Namespace,
    device: torch.device,
    out_dir: Path,
) -> dict[str, Any]:
    print(f"Training split={split_name} variant={variant}", flush=True)
    train_rows = rows_by_bucket["success_train_seen"] + rows_by_bucket["failure_train_seen"]
    val_rows = rows_by_bucket["success_val_seen"] + rows_by_bucket["failure_val_seen"]
    if variant not in args.variants:
        raise ValueError(f"variant {variant} not enabled")
    model, stats, history, best_epoch = train_model(train_rows, val_rows, variant, args, device)

    scores_by_bucket = {}
    labels_by_bucket = {}
    ids_by_bucket = {}
    ts_by_bucket = {}
    for bucket, rows in rows_by_bucket.items():
        scores, labels, ids, timesteps = score_rows(model, stats, rows, variant, args.batch_size, device)
        scores_by_bucket[bucket] = scores
        labels_by_bucket[bucket] = labels
        ids_by_bucket[bucket] = ids
        ts_by_bucket[bucket] = timesteps

    thresholds = calibrate_thresholds(scores_by_bucket, ids_by_bucket, args.alpha, args.min_conformal_mass)
    metrics_by_bucket = {}
    for bucket, rows in rows_by_bucket.items():
        metrics_by_bucket[bucket] = evaluate_bucket(bucket, rows, scores_by_bucket[bucket], ids_by_bucket[bucket], ts_by_bucket[bucket], episodes, thresholds)

    eval_pairs = {
        "seen_success_fa": metrics_by_bucket["success_test_seen"].get("success_false_alarm_rate"),
        "seen_failure_detection": metrics_by_bucket["failure_test_seen"].get("failure_detection_rate"),
        "seen_failure_det_at_25": metrics_by_bucket["failure_test_seen"].get("det_at_25"),
        "seen_failure_det_at_50": metrics_by_bucket["failure_test_seen"].get("det_at_50"),
        "ood_success_fa": metrics_by_bucket["success_test_ood"].get("success_false_alarm_rate"),
        "ood_failure_detection": metrics_by_bucket["failure_eval_ood"].get("failure_detection_rate"),
        "ood_failure_det_at_25": metrics_by_bucket["failure_eval_ood"].get("det_at_25"),
        "ood_failure_det_at_50": metrics_by_bucket["failure_eval_ood"].get("det_at_50"),
    }

    job_dir = out_dir / split_name / variant
    job_dir.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), job_dir / "model.pt")
    serial_stats = {k: {kk: vv.tolist() for kk, vv in v.items()} for k, v in stats.items()}
    write_json(job_dir / "normalization.json", serial_stats)
    write_json(job_dir / "thresholds.json", thresholds)
    write_json(job_dir / "history.json", history)
    result = {
        "split": split_name,
        "variant": variant,
        "best_epoch": best_epoch,
        "thresholds": thresholds,
        "bucket_counts": {k: {"episodes": len(set(r.episode_id for r in v)), "rows": len(v)} for k, v in rows_by_bucket.items()},
        "metrics_by_bucket": metrics_by_bucket,
        "summary_metrics": eval_pairs,
        "feature_audit": {
            "uses_reward": False,
            "uses_success": False,
            "uses_future_timestep": False,
            "uses_object_positions_before": False,
            "uses_task_metadata_as_input": False,
            "uses_ood_rows_for_train": False,
            "input_fields": [
                "history.previous_proprio",
                "history.previous_executed_action",
                "history.previous_ace_metrics",
                "main_candidate_action_chunk_normalized.sequence_tokens",
                "main_candidate_action_chunk_normalized.stats",
                "ace_candidate_chunks_normalized.metrics",
                "current.proprio",
            ] + (
                ["fixed_topk8(simvla_uncertainty_49d)"]
                if variant == "unc_topk8"
                else
                ["simvla_uncertainty_49d", "simvla_uncertainty_delta_49d"]
                if variant in {"uncertainty", "unc_raw", "unc_raw_dropout", "unc_raw_only"}
                else ["summary(simvla_uncertainty_49d)", "summary(simvla_uncertainty_delta_49d)"]
                if variant in {"unc_summary", "unc_summary_only"}
                else []
            ),
            "static_dim": {
                "base": 43,
                "unc_topk8": 51,
                "uncertainty": 141,
                "unc_raw": 141,
                "unc_raw_dropout": 141,
                "unc_summary": 63,
                "unc_summary_only": 20,
                "unc_raw_only": 98,
            }.get(variant, 43),
            "selected_uncertainty_dims": FIXED_TOPK8_DIMS if variant == "unc_topk8" else [],
            "unc_raw_static_dropout": args.unc_raw_static_dropout if variant == "unc_raw_dropout" else 0.0,
            "history_dim": 21,
            "history_steps": args.history_steps,
        },
    }
    write_json(job_dir / "metrics.json", result)
    return result


def write_reports(out_dir: Path, available: dict[str, Any], results: list[dict[str, Any]]) -> None:
    csv_path = out_dir / "dean_uncertainty_comparison_results.csv"
    fields = [
        "split",
        "variant",
        "best_epoch",
        "seen_success_fa",
        "seen_failure_detection",
        "seen_failure_det_at_25",
        "seen_failure_det_at_50",
        "ood_success_fa",
        "ood_failure_detection",
        "ood_failure_det_at_25",
        "ood_failure_det_at_50",
        "q95",
        "q99",
        "conformal_mass",
    ]
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            row = {k: r["summary_metrics"].get(k) for k in fields}
            row["split"] = r["split"]
            row["variant"] = r["variant"]
            row["best_epoch"] = r["best_epoch"]
            row["q95"] = r["thresholds"]["q95"]
            row["q99"] = r["thresholds"]["q99"]
            row["conformal_mass"] = r["thresholds"]["conformal_mass"]
            writer.writerow(row)

    lines = [
        "# Dean Uncertainty Transformer Exploration v2",
        "",
        "## Dataset",
        "",
        f"- Valid episodes used/indexed: `{available['valid_episodes']}`",
        f"- Successes: `{available['successes']}`",
        f"- Failures/timeouts: `{available['failures']}`",
        f"- Excluded bad reset tasks: `{', '.join(available['excluded_bad_tasks'])}`",
        "",
        "## Results",
        "",
        "| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    def pct(v):
        return "" if v is None else f"{100.0 * float(v):.1f}%"
    for r in results:
        s = r["summary_metrics"]
        lines.append(
            "| {split} | {variant} | {seen_fa} | {seen_det} | {seen25} | {seen50} | {ood_fa} | {ood_det} | {ood25} | {ood50} | {epoch} |".format(
                split=r["split"],
                variant=r["variant"],
                seen_fa=pct(s.get("seen_success_fa")),
                seen_det=pct(s.get("seen_failure_detection")),
                seen25=pct(s.get("seen_failure_det_at_25")),
                seen50=pct(s.get("seen_failure_det_at_50")),
                ood_fa=pct(s.get("ood_success_fa")),
                ood_det=pct(s.get("ood_failure_detection")),
                ood25=pct(s.get("ood_failure_det_at_25")),
                ood50=pct(s.get("ood_failure_det_at_50")),
                epoch=r["best_epoch"],
            )
        )
    report_path = out_dir / "DEAN_UNCERTAINTY_TRANSFORMER_COMPARISON_REPORT.md"
    report_path.write_text("\n".join(lines) + "\n")
    write_json(out_dir / "available_dataset_summary.json", available)
    print(f"Wrote {report_path}", flush=True)
    print(f"Wrote {csv_path}", flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--run-root", default="/home/dean/fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529")
    p.add_argument("--output-dir", default="/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_transformer_exploration_v2_20260601")
    p.add_argument("--splits", nargs="+", default=["all_tasks_random", "ood_last2_taskids"])
    p.add_argument("--variants", nargs="+", default=FEATURE_VARIANTS)
    p.add_argument("--default-suite", default="libero_goal_object")
    p.add_argument("--cadence", choices=["native", "stride"], default="native")
    p.add_argument("--stride", type=int, default=10)
    p.add_argument("--history-steps", type=int, default=16)
    p.add_argument("--width", type=int, default=128)
    p.add_argument("--layers", type=int, default=3)
    p.add_argument("--heads", type=int, default=4)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--unc-raw-static-dropout", type=float, default=0.25)
    p.add_argument("--batch-size", type=int, default=512)
    p.add_argument("--max-epochs", type=int, default=35)
    p.add_argument("--patience", type=int, default=8)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--weight-decay", type=float, default=1e-4)
    p.add_argument("--alpha", type=float, default=0.15)
    p.add_argument("--min-conformal-mass", type=float, default=0.15)
    p.add_argument("--seed", type=int, default=20260601)
    p.add_argument("--train-success-limit", type=int, default=1000000)
    p.add_argument("--train-failure-limit", type=int, default=1000000)
    p.add_argument("--val-success-limit", type=int, default=1000000)
    p.add_argument("--val-failure-limit", type=int, default=1000000)
    p.add_argument("--calib-success-limit", type=int, default=1000000)
    p.add_argument("--test-success-limit", type=int, default=1000000)
    p.add_argument("--test-failure-limit", type=int, default=1000000)
    p.add_argument("--ood-success-limit", type=int, default=1000000)
    p.add_argument("--ood-failure-limit", type=int, default=1000000)
    p.add_argument("--smoke", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.smoke:
        args.max_epochs = 1
        args.patience = 1
        args.batch_size = min(args.batch_size, 128)
    seed_everything(args.seed)
    run_root = Path(args.run_root)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device={device}", flush=True)

    episodes = load_episode_meta(run_root, args.default_suite)
    available = summarize_available(episodes)
    print(json.dumps(available, indent=2, sort_keys=True), flush=True)
    limits = {
        "train_success": args.train_success_limit,
        "train_failure": args.train_failure_limit,
        "val_success": args.val_success_limit,
        "val_failure": args.val_failure_limit,
        "calib_success": args.calib_success_limit,
        "test_success": args.test_success_limit,
        "test_failure": args.test_failure_limit,
        "ood_success": args.ood_success_limit,
        "ood_failure": args.ood_failure_limit,
    }
    all_results: list[dict[str, Any]] = []
    started = time.time()
    for split_name in args.splits:
        print(f"=== SPLIT {split_name} ===", flush=True)
        buckets = make_split_assignments(episodes, split_name, args.seed, limits)
        split_dir = out_dir / split_name
        write_json(split_dir / "episode_buckets.json", {k: sorted(v) for k, v in buckets.items()})
        rows_by_bucket = build_rows_for_split(run_root, episodes, buckets, args.history_steps, args.cadence, args.stride)
        write_json(split_dir / "bucket_counts.json", {k: {"episodes": len(set(r.episode_id for r in rows)), "rows": len(rows)} for k, rows in rows_by_bucket.items()})
        for variant in args.variants:
            result = run_job(split_name, variant, rows_by_bucket, episodes, args, device, out_dir)
            all_results.append(result)
            write_reports(out_dir, available, all_results)
        del rows_by_bucket
    write_reports(out_dir, available, all_results)
    write_json(out_dir / "run_config.json", vars(args) | {"elapsed_seconds": time.time() - started, "device": str(device)})


if __name__ == "__main__":
    main()
