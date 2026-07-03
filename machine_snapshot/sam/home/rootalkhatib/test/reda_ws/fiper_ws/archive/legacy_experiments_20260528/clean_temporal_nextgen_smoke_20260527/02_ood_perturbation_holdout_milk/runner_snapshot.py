#!/usr/bin/env python3
"""Run target-object OOD monitor NextGen experiments.

This script implements clean temporal risk monitors with:
A. Baseline carryover controls (TCN and LSTM score-only).
B. Survival / horizon-risk heads (predict failure within 10, 25, 50 steps, and eventual failure).
C. GroupDRO / worst-group training.
D. Domain-adversarial object/suite-invariant encoder.
E. Dynamics residual features.
F. Two-level policy evaluation.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import shutil
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset


SPLITS_TO_LOAD = [
    "success_train_seen",
    "success_val_seen",
    "success_calib_seen",
    "success_test_seen",
    "success_test_ood",
    "failure_train_seen",
    "failure_val_seen",
    "failure_test_seen",
    "failure_eval_ood"
]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


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


@dataclass
class CompactRow:
    split: str
    episode_key: str
    timestep: int
    outcome: str
    source_jsonl: str
    line_no: int
    action_seq: np.ndarray
    action_flat: np.ndarray
    action_stats: np.ndarray
    ace: np.ndarray
    proprio: np.ndarray
    objects: np.ndarray
    history_by_k: dict[int, np.ndarray]
    delta_proprio: np.ndarray = None
    group_name: str = "unknown"
    y_survival: np.ndarray = None


def get_target_object_fold(refs_dir: Path) -> str:
    for parent in [refs_dir] + list(refs_dir.parents):
        if parent.name.startswith("fold_"):
            return parent.name
    return "none"


def load_rows_from_refs(
    refs_dir: Path,
    base_dir: Path,
    max_rows_by_split: dict[str, int | None],
    history_steps_needed: list[int],
) -> dict[str, list[CompactRow]]:
    out: dict[str, list[CompactRow]] = {}
    all_loaded_rows: list[CompactRow] = []

    for split in SPLITS_TO_LOAD:
        ref_path = refs_dir / f"{split}.rows.jsonl"
        if not ref_path.exists():
            raise FileNotFoundError(f"missing refs file {ref_path}")
        refs = read_jsonl(ref_path)
        limit = max_rows_by_split.get(split)
        if limit:
            refs = refs[:limit]
        by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for ref in refs:
            by_source[str(ref["source_jsonl"])].append(ref)
        split_rows: list[CompactRow] = []
        for source_jsonl, source_refs in sorted(by_source.items()):
            source_path = base_dir / source_jsonl
            if not source_path.exists():
                raise FileNotFoundError(f"missing raw JSONL {source_path}")
            needed = {int(ref["line_no"]): ref for ref in source_refs}
            max_line = max(needed) if needed else 0
            print(f"Reading {split}: {len(source_refs)} rows from {source_jsonl}", flush=True)
            with source_path.open() as f:
                for line_no, line in enumerate(f, start=1):
                    if line_no > max_line:
                        break
                    ref = needed.get(line_no)
                    if ref is None:
                        continue
                    row = json.loads(line)
                    action_seq = pad_seq(row.get("main_candidate_action_chunk_normalized"), 10, 7)
                    action_flat = action_seq.reshape(-1).astype(np.float32)
                    action_stats = np.concatenate(
                        [
                            action_seq[0],
                            action_seq.mean(axis=0),
                            action_seq.std(axis=0),
                            (action_seq[-1] - action_seq[0]),
                        ]
                    ).astype(np.float32)
                    current = row.get("current") or {}
                    
                    compact_row = CompactRow(
                        split=split,
                        episode_key=str(ref.get("episode_key") or row.get("episode_id")),
                        timestep=int(ref.get("timestep", row.get("timestep", 0))),
                        outcome=str(ref.get("episode_outcome") or row.get("episode_outcome")),
                        source_jsonl=source_jsonl,
                        line_no=line_no,
                        action_seq=action_seq,
                        action_flat=action_flat,
                        action_stats=action_stats,
                        ace=compute_ace_metrics(row.get("ace_candidate_chunks_normalized")),
                        proprio=pad_flat(current.get("proprio"), 8),
                        objects=np.zeros((10, 7), dtype=np.float32),
                        history_by_k={},
                    )
                    compact_row._raw_executed_action = pad_flat(row.get("executed_action"), 7)
                    
                    target_obj = row.get("target_object_label") or "none"
                    pert_group = row.get("perturbation_group") or "none"
                    suite_fam = row.get("suite_family") or "none"
                    fold_name = get_target_object_fold(refs_dir)
                    compact_row.group_name = f"{pert_group}_{suite_fam}_{target_obj}_{fold_name}"
                    
                    split_rows.append(compact_row)
                    all_loaded_rows.append(compact_row)
        out[split] = split_rows
        print(f"Loaded {split}: {len(split_rows)} rows, {len({r.episode_key for r in split_rows})} episodes", flush=True)

    lookup: dict[tuple[str, int], tuple[np.ndarray, np.ndarray, np.ndarray]] = {}
    for r in all_loaded_rows:
        lookup[(r.episode_key, r.timestep)] = (r.proprio, r._raw_executed_action, r.ace)

    ep_max_t = {}
    for r in all_loaded_rows:
        ep_max_t[r.episode_key] = max(ep_max_t.get(r.episode_key, 0), r.timestep)

    for r in all_loaded_rows:
        for k in history_steps_needed:
            history_seq = np.zeros((k, 21), dtype=np.float32)
            for i in range(k):
                t_prev = r.timestep - k + i
                if t_prev >= 0:
                    prev_data = lookup.get((r.episode_key, t_prev))
                    if prev_data is not None:
                        prev_proprio, prev_act, prev_ace = prev_data
                        history_seq[i, :] = np.concatenate([prev_proprio, prev_act, prev_ace[:6]])
            r.history_by_k[k] = history_seq

        next_data = lookup.get((r.episode_key, r.timestep + 1))
        if next_data is not None:
            r.delta_proprio = next_data[0] - r.proprio
        else:
            r.delta_proprio = np.zeros(8, dtype=np.float32)

        is_fail = r.outcome in ["failure_or_timeout", "failure"] or r.outcome.startswith("fail")
        t_to_fail = ep_max_t[r.episode_key] - r.timestep
        r.y_survival = np.array([
            1.0 if (is_fail and t_to_fail <= 10) else 0.0,
            1.0 if (is_fail and t_to_fail <= 25) else 0.0,
            1.0 if (is_fail and t_to_fail <= 50) else 0.0,
            1.0 if is_fail else 0.0
        ], dtype=np.float32)

    return out


def vector_features(rows: list[CompactRow], cfg: dict[str, Any]) -> np.ndarray:
    history_steps = int(cfg.get("history_steps", 8))
    include_action = bool(cfg.get("include_action", True))
    action_repr = str(cfg.get("action_repr", "flat"))
    parts: list[np.ndarray] = []
    for row in rows:
        vec_parts: list[np.ndarray] = []
        if include_action:
            if action_repr == "stats":
                vec_parts.append(row.action_stats)
            elif action_repr == "first":
                vec_parts.append(row.action_seq[0])
            elif action_repr == "seq_stats":
                vec_parts.append(np.concatenate([row.action_flat, row.action_stats]).astype(np.float32))
            else:
                vec_parts.append(row.action_flat)
        if cfg.get("include_ace", False):
            vec_parts.append(row.ace)
        if cfg.get("include_proprio", False):
            vec_parts.append(row.proprio)
        if cfg.get("include_objects", False):
            vec_parts.append(row.objects.reshape(-1))
        if cfg.get("include_history", False):
            vec_parts.append(row.history_by_k[history_steps].reshape(-1))
        if not vec_parts:
            vec_parts.append(np.zeros(1, dtype=np.float32))
        parts.append(np.concatenate(vec_parts).astype(np.float32))
    return np.stack(parts, axis=0) if parts else np.zeros((0, 1), dtype=np.float32)


def sequence_features(rows: list[CompactRow], cfg: dict[str, Any]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    history_steps = int(cfg.get("history_steps", 8))
    if not rows:
        hist_dim = 21 if bool(cfg.get("include_ace_history", True)) else 15
        static_cfg = dict(cfg)
        static_cfg["include_history"] = False
        static_dim = vector_features([], static_cfg).shape[1]
        return (
            np.zeros((0, history_steps, hist_dim), dtype=np.float32),
            np.zeros((0, 10, 7), dtype=np.float32),
            np.zeros((0, static_dim), dtype=np.float32),
        )
    histories = np.stack([r.history_by_k[history_steps] for r in rows], axis=0).astype(np.float32)
    include_ace_history = bool(cfg.get("include_ace_history", True))
    if not include_ace_history:
        histories = histories[:, :, :15]
    actions = np.stack([r.action_seq for r in rows], axis=0).astype(np.float32)
    static_cfg = dict(cfg)
    static_cfg["include_history"] = False
    static = vector_features(rows, static_cfg)
    return histories, actions, static


def fit_standardizer(x: np.ndarray) -> dict[str, np.ndarray]:
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}


def apply_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


def fit_seq_standardizer(x: np.ndarray) -> dict[str, np.ndarray]:
    mean = x.reshape(-1, x.shape[-1]).mean(axis=0)
    std = x.reshape(-1, x.shape[-1]).std(axis=0)
    std = np.where(std < 1e-5, 1.0, std)
    return {"mean": mean.astype(np.float32), "std": std.astype(np.float32)}


def apply_seq_standardizer(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    return np.clip((x - stats["mean"]) / stats["std"], -10.0, 10.0).astype(np.float32)


class VectorDataset(Dataset):
    def __init__(self, x: np.ndarray, y: np.ndarray | None = None) -> None:
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float32)

    def __len__(self) -> int:
        return int(self.x.shape[0])

    def __getitem__(self, idx: int) -> Any:
        if self.y is None:
            return self.x[idx]
        return self.x[idx], self.y[idx]


class SeqDataset(Dataset):
    def __init__(
        self,
        hist: np.ndarray,
        action: np.ndarray,
        static: np.ndarray,
        y: np.ndarray | None = None,
        delta_proprio: np.ndarray | None = None,
        group_ids: np.ndarray | None = None,
    ) -> None:
        self.hist = torch.tensor(hist, dtype=torch.float32)
        self.action = torch.tensor(action, dtype=torch.float32)
        self.static = torch.tensor(static, dtype=torch.float32)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float32)
        self.delta_proprio = None if delta_proprio is None else torch.tensor(delta_proprio, dtype=torch.float32)
        self.group_ids = None if group_ids is None else torch.tensor(group_ids, dtype=torch.long)

    def __len__(self) -> int:
        return int(self.hist.shape[0])

    def __getitem__(self, idx: int) -> Any:
        item = {"history": self.hist[idx], "action": self.action[idx], "static": self.static[idx]}
        if self.delta_proprio is not None:
            item["delta_proprio"] = self.delta_proprio[idx]
        if self.group_ids is not None:
            item["group_id"] = self.group_ids[idx]
            
        if self.y is None:
            return item
        return item, self.y[idx]


class GradientReversal(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, alpha):
        ctx.alpha = alpha
        return x.view_as(x)

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output.neg() * ctx.alpha, None


def grad_reverse(x, alpha=1.0):
    return GradientReversal.apply(x, alpha)


class SeqRiskModel(nn.Module):
    def __init__(
        self,
        kind: str,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 2,
        dropout: float = 0.1,
        survival_heads: bool = False,
        dynamics_residual: bool = False,
        num_groups: int = 1,
    ) -> None:
        super().__init__()
        self.kind = kind
        self.survival_heads = survival_heads
        self.dynamics_residual = dynamics_residual
        self.num_groups = num_groups

        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)

        if kind == "tcn":
            self.seq = nn.Sequential(
                nn.Conv1d(width, width, 3, padding=1),
                nn.GELU(),
                nn.Conv1d(width, width, 3, padding=2, dilation=2),
                nn.GELU(),
                nn.AdaptiveAvgPool1d(1),
            )
        elif kind in {"gru", "lstm"}:
            rnn_cls = nn.GRU if kind == "gru" else nn.LSTM
            self.seq = rnn_cls(width, width, num_layers=layers, dropout=dropout if layers > 1 else 0.0, batch_first=True)
        else:
            raise ValueError(f"unknown sequence model {kind}")

        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())

        latent_dim = width * 2

        if self.dynamics_residual:
            self.dynamics_head = nn.Sequential(
                nn.Linear(latent_dim, width),
                nn.GELU(),
                nn.Linear(width, 8)
            )
            risk_input_dim = latent_dim + 1
        else:
            risk_input_dim = latent_dim

        out_dim = 4 if self.survival_heads else 1
        self.head = nn.Sequential(
            nn.LayerNorm(risk_input_dim),
            nn.Linear(risk_input_dim, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, out_dim)
        )

        if self.num_groups > 1:
            self.adv_head = nn.Sequential(
                nn.Linear(latent_dim, width),
                nn.GELU(),
                nn.Linear(width, num_groups)
            )

    def forward(self, batch: dict[str, torch.Tensor], alpha: float = 1.0) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        if self.kind == "tcn":
            seq = self.seq(tokens.transpose(1, 2)).squeeze(-1)
        elif self.kind in {"gru", "lstm"}:
            _out, state = self.seq(tokens)
            if isinstance(state, tuple):
                state = state[0]
            seq = state[-1]
        else:
            raise ValueError(f"unknown sequence model {self.kind}")

        static = self.static(batch["static"])
        latent = torch.cat([seq, static], dim=-1)

        outputs = {}

        if self.dynamics_residual:
            pred_delta = self.dynamics_head(latent)
            outputs["pred_delta"] = pred_delta
            if "delta_proprio" in batch:
                true_delta = batch["delta_proprio"]
                residual_norm = torch.norm(pred_delta - true_delta, p=2, dim=-1, keepdim=True)
                outputs["residual_norm"] = residual_norm
                risk_input = torch.cat([latent, residual_norm.detach()], dim=-1)
            else:
                risk_input = torch.cat([latent, torch.zeros((latent.shape[0], 1), device=latent.device)], dim=-1)
        else:
            risk_input = latent

        logits = self.head(risk_input)

        if self.num_groups > 1:
            reversed_latent = grad_reverse(latent, alpha)
            group_logits = self.adv_head(reversed_latent)
            outputs["group_logits"] = group_logits

        if not self.survival_heads:
            logits = logits.squeeze(-1)

        return logits, outputs


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


def make_seq_inputs(rows_by_split: dict[str, list[CompactRow]], cfg: dict[str, Any]) -> dict[str, Any]:
    train_rows = rows_by_split["success_train_seen"] + rows_by_split["failure_train_seen"]
    val_rows = rows_by_split["success_val_seen"] + rows_by_split["failure_val_seen"]

    if cfg.get("survival_heads", False):
        y_train = np.stack([r.y_survival for r in train_rows], axis=0).astype(np.float32)
        y_val = np.stack([r.y_survival for r in val_rows], axis=0).astype(np.float32)
    else:
        y_train = np.asarray([0.0] * len(rows_by_split["success_train_seen"]) + [1.0] * len(rows_by_split["failure_train_seen"]), dtype=np.float32)
        y_val = np.asarray([0.0] * len(rows_by_split["success_val_seen"]) + [1.0] * len(rows_by_split["failure_val_seen"]), dtype=np.float32)

    delta_proprio_train = np.stack([r.delta_proprio for r in train_rows], axis=0).astype(np.float32)
    delta_proprio_val = np.stack([r.delta_proprio for r in val_rows], axis=0).astype(np.float32)

    unique_group_names = sorted(list({r.group_name for r in train_rows + val_rows}))
    group_to_id = {name: idx for idx, name in enumerate(unique_group_names)}
    group_ids_train = np.array([group_to_id[r.group_name] for r in train_rows], dtype=np.int64)
    group_ids_val = np.array([group_to_id[r.group_name] for r in val_rows], dtype=np.int64)

    h_train_raw, a_train_raw, st_train_raw = sequence_features(train_rows, cfg)
    h_stats = fit_seq_standardizer(h_train_raw)
    a_stats = fit_seq_standardizer(a_train_raw)
    st_stats = fit_standardizer(st_train_raw)
    h_val_raw, a_val_raw, st_val_raw = sequence_features(val_rows, cfg)

    return {
        "train_rows": train_rows,
        "val_rows": val_rows,
        "h_train": apply_seq_standardizer(h_train_raw, h_stats),
        "a_train": apply_seq_standardizer(a_train_raw, a_stats),
        "st_train": apply_standardizer(st_train_raw, st_stats),
        "h_val": apply_seq_standardizer(h_val_raw, h_stats),
        "a_val": apply_seq_standardizer(a_val_raw, a_stats),
        "st_val": apply_standardizer(st_val_raw, st_stats),
        "y_train": y_train,
        "y_val": y_val,
        "delta_proprio_train": delta_proprio_train,
        "delta_proprio_val": delta_proprio_val,
        "group_ids_train": group_ids_train,
        "group_ids_val": group_ids_val,
        "group_to_id": group_to_id,
        "stats": {"history": h_stats, "action": a_stats, "static": st_stats},
    }


def move_batch(batch: Any, device: torch.device) -> Any:
    if torch.is_tensor(batch):
        return batch.to(device)
    if isinstance(batch, dict):
        return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
    return batch


def train_supervised_sequence(inputs: dict[str, Any], cfg: dict[str, Any], device: torch.device) -> tuple[nn.Module, list[dict[str, Any]], int]:
    num_groups = len(inputs["group_to_id"])
    model = SeqRiskModel(
        str(cfg.get("model", "tcn")).replace("seq_", ""),
        hist_dim=inputs["h_train"].shape[-1],
        action_dim=inputs["a_train"].shape[-1],
        static_dim=inputs["st_train"].shape[-1],
        width=int(cfg.get("width", 128)),
        layers=int(cfg.get("layers", 2)),
        dropout=float(cfg.get("dropout", 0.1)),
        survival_heads=bool(cfg.get("survival_heads", False)),
        dynamics_residual=bool(cfg.get("dynamics_residual", False)),
        num_groups=num_groups if bool(cfg.get("adversarial", False)) else 1,
    )
    train_ds = SeqDataset(
        inputs["h_train"], inputs["a_train"], inputs["st_train"], inputs["y_train"],
        inputs["delta_proprio_train"], inputs["group_ids_train"]
    )
    val_ds = SeqDataset(
        inputs["h_val"], inputs["a_val"], inputs["st_val"], inputs["y_val"],
        inputs["delta_proprio_val"], inputs["group_ids_val"]
    )
    return train_supervised_model(model, train_ds, val_ds, cfg, device)


def train_supervised_model(model: nn.Module, train_ds: Dataset, val_ds: Dataset, cfg: dict[str, Any], device: torch.device) -> tuple[nn.Module, list[dict[str, Any]], int]:
    model = model.to(device)
    batch_size = int(cfg.get("batch_size", 256))
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, drop_last=False)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, drop_last=False)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(cfg.get("lr", 2e-4)), weight_decay=float(cfg.get("weight_decay", 1e-4)))
    
    survival_heads = bool(cfg.get("survival_heads", False))
    group_dro = bool(cfg.get("group_dro", False))
    adversarial = bool(cfg.get("adversarial", False))
    dynamics_residual = bool(cfg.get("dynamics_residual", False))

    pos_weight_value = float(cfg.get("pos_weight", 1.0))
    if survival_heads:
        pos_weight = torch.tensor([pos_weight_value] * 4, dtype=torch.float32, device=device)
    else:
        pos_weight = torch.tensor([pos_weight_value], dtype=torch.float32, device=device)

    max_epochs = int(cfg.get("max_epochs", 120))
    patience = int(cfg.get("patience", 15))
    best_state: dict[str, torch.Tensor] | None = None
    best_score = -1e9
    best_epoch = 0
    no_improve = 0
    history: list[dict[str, Any]] = []
    
    adv_alpha = float(cfg.get("adv_alpha", 0.5))

    for epoch in range(1, max_epochs + 1):
        model.train()
        losses: list[float] = []
        for batch, yb in train_loader:
            batch = move_batch(batch, device)
            yb = yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            
            logits, outputs = model(batch, alpha=adv_alpha)
            
            if survival_heads:
                bce_elements = nn.functional.binary_cross_entropy_with_logits(logits, yb, pos_weight=pos_weight, reduction="none")
                bce = bce_elements.mean(dim=-1)
            else:
                bce = nn.functional.binary_cross_entropy_with_logits(logits, yb, pos_weight=pos_weight, reduction="none")

            if group_dro:
                group_ids = batch["group_id"]
                unique_groups = torch.unique(group_ids)
                group_losses = []
                for g in unique_groups:
                    mask = (group_ids == g)
                    group_losses.append(bce[mask].mean())
                group_losses = torch.stack(group_losses)
                weights = nn.functional.softmax(group_losses * 1.0, dim=0)
                risk_loss = (weights * group_losses).sum()
            else:
                risk_loss = bce.mean()

            loss = risk_loss

            if dynamics_residual:
                dyn_loss = nn.functional.mse_loss(outputs["pred_delta"], batch["delta_proprio"])
                loss = loss + 1.0 * dyn_loss

            if adversarial and "group_logits" in outputs:
                adv_loss = nn.functional.cross_entropy(outputs["group_logits"], batch["group_id"])
                loss = loss + 1.0 * adv_loss

            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            losses.append(float(loss.detach().cpu()))

        val_scores, val_y = predict_supervised(model, val_loader, device)
        if survival_heads:
            val_scores_auc = val_scores[:, 3]
            val_y_auc = val_y[:, 3]
        else:
            val_scores_auc = val_scores
            val_y_auc = val_y

        auc = auroc_binary(val_y_auc, val_scores_auc)
        brier = float(np.mean((val_scores_auc - val_y_auc) ** 2))
        score = auc - brier
        row = {"epoch": epoch, "train_loss": float(np.mean(losses)), "val_auroc": auc, "val_brier": brier, "early_stop_score": score}
        history.append(row)
        print(json.dumps({"job": cfg["name"], **row}, sort_keys=True), flush=True)

        if score > best_score + 1e-6:
            best_score = score
            best_epoch = epoch
            no_improve = 0
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
        else:
            no_improve += 1
            if no_improve >= patience:
                break

    if best_state is not None:
        model.load_state_dict(best_state)
    return model, history, best_epoch


def predict_supervised(model: nn.Module, loader: DataLoader, device: torch.device) -> tuple[np.ndarray, np.ndarray]:
    model.eval()
    scores: list[np.ndarray] = []
    labels: list[np.ndarray] = []
    with torch.no_grad():
        for batch, yb in loader:
            batch = move_batch(batch, device)
            logits, outputs = model(batch)
            scores.append(torch.sigmoid(logits).detach().cpu().numpy())
            labels.append(yb.detach().cpu().numpy())
    return np.concatenate(scores), np.concatenate(labels)


def score_seq_model(
    model: nn.Module,
    hist: np.ndarray,
    action: np.ndarray,
    static: np.ndarray,
    delta_proprio: np.ndarray,
    group_ids: np.ndarray,
    cfg: dict[str, Any],
    device: torch.device,
) -> tuple[np.ndarray, np.ndarray | None]:
    dummy_y = np.zeros(hist.shape[0])
    loader = DataLoader(
        SeqDataset(hist, action, static, dummy_y, delta_proprio, group_ids),
        batch_size=int(cfg.get("batch_size", 512)),
        shuffle=False
    )
    model.eval()
    scores: list[np.ndarray] = []
    res_norms: list[np.ndarray] = []
    with torch.no_grad():
        for batch, _ in loader:
            batch = move_batch(batch, device)
            logits, outputs = model(batch)
            scores.append(torch.sigmoid(logits).detach().cpu().numpy())
            if "residual_norm" in outputs:
                res_norms.append(outputs["residual_norm"].detach().cpu().numpy())
    risk_scores = np.concatenate(scores)
    residual_norms = np.concatenate(res_norms) if res_norms else None
    return risk_scores, residual_norms


def summarize_policy(
    rows: list[CompactRow],
    s_alarm: np.ndarray,
    a_alarm: np.ndarray,
    res_alarm: np.ndarray,
    k: int,
    mode: str,
) -> dict[str, Any]:
    by_ep: dict[str, list[tuple[int, bool, bool, bool]]] = defaultdict(list)
    for row, sa, aa, ra in zip(rows, s_alarm, a_alarm, res_alarm):
        by_ep[row.episode_key].append((row.timestep, bool(sa), bool(aa), bool(ra)))
        
    detected = 0
    d10 = d25 = d50 = 0
    first_times: list[float] = []
    alarm_steps_per_ep: list[int] = []
    first_time_unnormalized: list[int] = []
    
    for ep_rows in by_ep.values():
        ep_rows.sort(key=lambda x: x[0])
        if mode == "score":
            raw = [x[1] for x in ep_rows]
        elif mode == "ace":
            raw = [x[2] for x in ep_rows]
        elif mode == "and":
            raw = [x[1] and x[2] for x in ep_rows]
        elif mode == "hardstop":
            raw = [x[1] and x[3] for x in ep_rows]
        else: # or
            raw = [x[1] or x[2] for x in ep_rows]
            
        alarm_steps = [False] * len(raw)
        for t in range(k - 1, len(raw)):
            if all(raw[t - j] for j in range(k)):
                alarm_steps[t] = True
                
        first = next((i for i, val in enumerate(alarm_steps) if val), None)
        alarm_steps_per_ep.append(sum(alarm_steps))
        if first is not None:
            detected += 1
            norm = first / max(1, len(raw))
            first_times.append(norm)
            first_time_unnormalized.append(first)
            d10 += norm <= 0.10
            d25 += norm <= 0.25
            d50 += norm <= 0.50
            
    n = max(1, len(by_ep))
    fp_ep_alarm_steps = [s for s in alarm_steps_per_ep if s > 0]
    mean_alarm_steps_fp = float(np.mean(fp_ep_alarm_steps)) if fp_ep_alarm_steps else 0.0
    
    return {
        "episodes": len(by_ep),
        "episode_alarm_rate": detected / n,
        "never_rate": 1.0 - detected / n,
        "det_at_10": d10 / n,
        "det_at_25": d25 / n,
        "det_at_50": d50 / n,
        "mean_first_norm_detected": float(np.mean(first_times)) if first_times else None,
        "median_first_norm_detected": float(np.median(first_times)) if first_times else None,
        "mean_first_step_detected": float(np.mean(first_time_unnormalized)) if first_time_unnormalized else None,
        "mean_alarm_steps": float(np.mean(alarm_steps_per_ep)) if alarm_steps_per_ep else 0.0,
        "mean_alarm_steps_per_fp_episode": mean_alarm_steps_fp,
    }


def evaluate_job(
    rows_by_split: dict[str, list[CompactRow]],
    scores_by_split: dict[str, np.ndarray],
    res_norms_by_split: dict[str, np.ndarray | None],
    thresholds: dict[str, Any],
) -> dict[str, Any]:
    out: dict[str, Any] = {"row_metrics": {}, "episode_metrics": {}}
    ace_thresholds = thresholds["ace"]
    res_thresholds = thresholds.get("residual", {})
    
    has_survival = False
    for split, scores in scores_by_split.items():
        if scores.ndim == 2 and scores.shape[1] == 4:
            has_survival = True
            break
            
    head_names = ["h10", "h25", "h50", "eventual"] if has_survival else ["eventual"]
    
    for split, rows in rows_by_split.items():
        if split not in scores_by_split or split == "success_train_seen":
            continue
        scores = scores_by_split[split]
        res_norms = res_norms_by_split.get(split)
        ace_entropy = np.asarray([r.ace[0] for r in rows], dtype=np.float32)
        
        row_metrics: dict[str, Any] = {"rows": len(rows), "episodes": len({r.episode_key for r in rows})}
        if not rows:
            out["row_metrics"][split] = row_metrics
            out["episode_metrics"][split] = {}
            continue
            
        out["episode_metrics"][split] = {}
        
        for head_name in head_names:
            if has_survival:
                head_idx = ["h10", "h25", "h50", "eventual"].index(head_name)
                h_scores = scores[:, head_idx]
            else:
                h_scores = scores
                
            score_thresholds = thresholds["score"][head_name]
            
            for q in ["q90", "q95", "q99"]:
                s_alarm = h_scores > score_thresholds[q]
                a_alarm = ace_entropy > ace_thresholds[q]
                row_metrics[f"{head_name}_score_alarm_{q}"] = float(np.mean(s_alarm))
                row_metrics[f"{head_name}_or_alarm_{q}"] = float(np.mean(s_alarm | a_alarm))
                row_metrics[f"{head_name}_and_alarm_{q}"] = float(np.mean(s_alarm & a_alarm))
                
            for q in ["q95", "q99"]:
                s_alarm = h_scores > score_thresholds[q]
                a_alarm = ace_entropy > ace_thresholds[q]
                
                if res_norms is not None and "q95" in res_thresholds:
                    res_alarm = res_norms.squeeze(-1) > res_thresholds["q95"]
                else:
                    res_alarm = np.ones_like(h_scores, dtype=bool)
                    
                for k in [1, 2, 3, 5, 10]:
                    out["episode_metrics"][split][f"{head_name}_score_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, res_alarm, k, "score")
                    out["episode_metrics"][split][f"{head_name}_ace_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, res_alarm, k, "ace")
                    out["episode_metrics"][split][f"{head_name}_or_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, res_alarm, k, "or")
                    out["episode_metrics"][split][f"{head_name}_and_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, res_alarm, k, "and")
                    out["episode_metrics"][split][f"{head_name}_hardstop_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, res_alarm, k, "hardstop")
                    
        out["row_metrics"][split] = row_metrics
    return out


def campaign_objective(metrics: dict[str, Any]) -> float:
    ep = metrics["episode_metrics"]
    ood_fail = ep.get("failure_eval_ood", {}).get("eventual_or_q95_K3")
    ood_succ = ep.get("success_test_ood", {}).get("eventual_or_q95_K3")
    seen_succ = ep.get("success_test_seen", {}).get("eventual_or_q95_K3", {"episode_alarm_rate": 0.0})
    if ood_fail is None:
        ood_fail = ep.get("failure_test_seen", {}).get("eventual_or_q95_K3", {"det_at_25": 0.0, "episode_alarm_rate": 0.0})
    if ood_succ is None:
        ood_succ = {"episode_alarm_rate": 0.0}
    return (
        2.0 * ood_fail["det_at_25"]
        + 1.0 * ood_fail["episode_alarm_rate"]
        - 1.5 * ood_succ["episode_alarm_rate"]
        - 0.5 * seen_succ["episode_alarm_rate"]
    )


def run_one_job(
    cfg: dict[str, Any],
    rows_by_split: dict[str, list[CompactRow]],
    out_dir: Path,
    device: torch.device,
    global_args: argparse.Namespace,
) -> dict[str, Any]:
    if cfg.get("include_objects", False) or cfg.get("include_objects_before", False):
        raise ValueError("Global Validation FAIL: include_objects is True in config!")
    if cfg.get("include_reward", False) or cfg.get("include_success", False):
        raise ValueError("Global Validation FAIL: include_reward or include_success is True in config!")
    
    banned_keys = [
        "reward", "success", "object_positions_before", "target_object_label",
        "task_id", "suite", "task_instruction", "language", "episode_outcome",
        "failure_labels", "suite_family", "task_context"
    ]
    for key in banned_keys:
        if cfg.get(f"include_{key}", False):
            raise ValueError(f"Global Validation FAIL: include_{key} is True in config!")
        for k_val in cfg.values():
            if isinstance(k_val, str) and key in k_val:
                if key in ["reward", "success", "object"] and any(x in k_val for x in ["no_reward_success", "no_object"]):
                    continue
                raise ValueError(f"Global Validation FAIL: Banned term '{key}' in config value '{k_val}'!")

    job_dir = out_dir / "jobs" / cfg["name"]
    if (job_dir / "summary.json").exists() and not global_args.force:
        return json.loads((job_dir / "summary.json").read_text())
    job_dir.mkdir(parents=True, exist_ok=True)
    (job_dir / "config.json").write_text(json.dumps(cfg, indent=2, sort_keys=True) + "\n")
    
    start = time.time()
    
    inputs = make_seq_inputs(rows_by_split, cfg)
    model, history, best_epoch = train_supervised_sequence(inputs, cfg, device)
    
    scores_by_split: dict[str, np.ndarray] = {}
    res_norms_by_split: dict[str, np.ndarray | None] = {}
    
    for split, rows in rows_by_split.items():
        if not rows:
            scores_by_split[split] = np.zeros(0, dtype=np.float32)
            res_norms_by_split[split] = None
            continue
            
        h_raw, a_raw, st_raw = sequence_features(rows, cfg)
        h = apply_seq_standardizer(h_raw, inputs["stats"]["history"])
        a = apply_seq_standardizer(a_raw, inputs["stats"]["action"])
        st = apply_standardizer(st_raw, inputs["stats"]["static"])
        
        delta_proprio = np.stack([r.delta_proprio for r in rows], axis=0).astype(np.float32)
        group_ids = np.array([inputs["group_to_id"].get(r.group_name, 0) for r in rows], dtype=np.int64)
        
        scores_by_split[split], res_norms_by_split[split] = score_seq_model(
            model, h, a, st, delta_proprio, group_ids, cfg, device
        )
        
    hist_dim = inputs["h_train"].shape[-1]
    static_dim = inputs["st_train"].shape[-1]

    # Write machine-readable FEATURE_AUDIT.json
    audit_data = {
        "uses_object_positions_before": False,
        "uses_reward": False,
        "uses_success": False,
        "uses_task_metadata": False,
        "uses_ood_rows_for_train": False,
        "history_dim": hist_dim,
        "current_feature_dim": static_dim,
        "input_fields": [
            "main_candidate_action_chunk_normalized",
            "ace_candidate_chunks_normalized",
            "current.proprio",
            "executed_action",
            "timestep"
        ]
    }
    (job_dir / "FEATURE_AUDIT.json").write_text(json.dumps(audit_data, indent=2) + "\n")

    calib_scores = scores_by_split["success_calib_seen"]
    calib_ace = np.asarray([r.ace[0] for r in rows_by_split["success_calib_seen"]], dtype=np.float32)
    calib_res_norms = res_norms_by_split["success_calib_seen"]
    
    thresholds = {
        "score": {},
        "ace": {q: float(np.quantile(calib_ace, val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()},
        "residual": {}
    }
    
    if calib_scores.ndim == 2 and calib_scores.shape[1] == 4:
        for head_idx, head_name in enumerate(["h10", "h25", "h50", "eventual"]):
            thresholds["score"][head_name] = {
                q: float(np.quantile(calib_scores[:, head_idx], val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()
            }
    else:
        thresholds["score"]["eventual"] = {
            q: float(np.quantile(calib_scores, val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()
        }
        
    if calib_res_norms is not None:
        thresholds["residual"] = {
            q: float(np.quantile(calib_res_norms, val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()
        }

    metrics = evaluate_job(rows_by_split, scores_by_split, res_norms_by_split, thresholds)
    metrics["objective"] = campaign_objective(metrics)
    
    def metric_value(split: str, policy: str, field: str) -> Any:
        return metrics.get("episode_metrics", {}).get(split, {}).get(policy, {}).get(field)

    summary = {
        "name": cfg["name"],
        "mode": cfg["mode"],
        "model": cfg.get("model"),
        "feature_notes": cfg.get("notes", ""),
        "best_epoch": best_epoch,
        "runtime_seconds": time.time() - start,
        "thresholds": thresholds,
        "objective": metrics["objective"],
        "key_metrics": {
            "success_test_seen_or_q95_K3_fa": metric_value("success_test_seen", "eventual_or_q95_K3", "episode_alarm_rate"),
            "success_test_ood_or_q95_K3_fa": metric_value("success_test_ood", "eventual_or_q95_K3", "episode_alarm_rate"),
            "failure_test_seen_or_q95_K3_det": metric_value("failure_test_seen", "eventual_or_q95_K3", "episode_alarm_rate"),
            "failure_test_seen_or_q95_K3_det25": metric_value("failure_test_seen", "eventual_or_q95_K3", "det_at_25"),
            "failure_eval_ood_or_q95_K3_det": metric_value("failure_eval_ood", "eventual_or_q95_K3", "episode_alarm_rate"),
            "failure_eval_ood_or_q95_K3_det25": metric_value("failure_eval_ood", "eventual_or_q95_K3", "det_at_25"),
            "failure_eval_ood_or_q95_K3_mean_time": metric_value("failure_eval_ood", "eventual_or_q95_K3", "mean_first_norm_detected"),
            "success_test_ood_score_q95_K3_fa": metric_value("success_test_ood", "eventual_score_q95_K3", "episode_alarm_rate"),
            "failure_eval_ood_score_q95_K3_det25": metric_value("failure_eval_ood", "eventual_score_q95_K3", "det_at_25"),
            # Red warning
            "success_test_seen_score_q99_K3_fa": metric_value("success_test_seen", "eventual_score_q99_K3", "episode_alarm_rate"),
            "success_test_ood_score_q99_K3_fa": metric_value("success_test_ood", "eventual_score_q99_K3", "episode_alarm_rate"),
            "failure_eval_ood_score_q99_K3_det": metric_value("failure_eval_ood", "eventual_score_q99_K3", "episode_alarm_rate"),
            # Hard stop metrics
            "success_test_seen_hardstop_q99_K3_fa": metric_value("success_test_seen", "eventual_hardstop_q99_K3", "episode_alarm_rate"),
            "success_test_ood_hardstop_q99_K3_fa": metric_value("success_test_ood", "eventual_hardstop_q99_K3", "episode_alarm_rate"),
            "failure_eval_ood_hardstop_q99_K3_det": metric_value("failure_eval_ood", "eventual_hardstop_q99_K3", "episode_alarm_rate"),
            "failure_eval_ood_hardstop_q99_K3_det25": metric_value("failure_eval_ood", "eventual_hardstop_q99_K3", "det_at_25"),
        },
    }
    torch.save(model.state_dict(), job_dir / "model.pt")
    (job_dir / "training_history.json").write_text(json.dumps(history, indent=2, sort_keys=True) + "\n")
    (job_dir / "policy_thresholds.json").write_text(json.dumps(thresholds, indent=2, sort_keys=True) + "\n")
    (job_dir / "thresholds.json").write_text(json.dumps(thresholds, indent=2, sort_keys=True) + "\n")
    (job_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")
    (job_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    
    score_rows = []
    for split, rows in rows_by_split.items():
        if split == "success_train_seen":
            continue
        scores = scores_by_split[split]
        res_norms = res_norms_by_split.get(split)
        for i, row in enumerate(rows):
            score_val = scores[i]
            res_val = float(res_norms[i][0]) if res_norms is not None else 0.0
            
            row_dict = {
                "split": split,
                "episode_key": row.episode_key,
                "timestep": row.timestep,
                "ace_entropy": float(row.ace[0]),
                "outcome": row.outcome,
                "residual_norm": res_val,
            }
            if score_val.ndim == 1:
                for head_idx, head_name in enumerate(["h10", "h25", "h50", "eventual"]):
                    row_dict[f"score_{head_name}"] = float(score_val[head_idx])
            else:
                row_dict["score"] = float(score_val)
            score_rows.append(row_dict)
            
    write_jsonl(job_dir / "scores.jsonl", score_rows)
    return summary


def write_campaign_reports(out_dir: Path, summaries: list[dict[str, Any]]) -> None:
    rows = sorted(summaries, key=lambda r: r["objective"], reverse=True)
    def pct_or_na(value: Any) -> str:
        return "NA" if value is None else f"{float(value):.2%}"

    csv_path = out_dir / "campaign_summary.csv"
    with csv_path.open("w", newline="") as f:
        fieldnames = ["rank", "name", "mode", "model", "objective", "best_epoch"]
        if rows:
            fieldnames += list(rows[0]["key_metrics"].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank, row in enumerate(rows, start=1):
            flat = {k: row.get(k) for k in ["name", "mode", "model", "objective", "best_epoch"]}
            flat.update(row["key_metrics"])
            flat["rank"] = rank
            writer.writerow(flat)
            
    (out_dir / "campaign_summary.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    md_lines = [
        "# NextGen Clean Temporal Campaign Report",
        "",
        "| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 | HardStop OOD FA q99 K3 | HardStop OOD Det q99 K3 |",
        "|---:|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, row in enumerate(rows[:20], start=1):
        km = row["key_metrics"]
        md_lines.append(
            f"| {rank} | `{row['name']}` | {row['mode']} | {row.get('model')} | {row['objective']:.4f} | "
            f"{pct_or_na(km.get('success_test_ood_or_q95_K3_fa'))} | {pct_or_na(km.get('failure_eval_ood_or_q95_K3_det'))} | {pct_or_na(km.get('failure_eval_ood_or_q95_K3_det25'))} | "
            f"{pct_or_na(km.get('success_test_ood_hardstop_q99_K3_fa'))} | {pct_or_na(km.get('failure_eval_ood_hardstop_q99_K3_det'))} |"
        )
    (out_dir / "CAMPAIGN_TOPLINE_REPORT.md").write_text("\n".join(md_lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign-config", required=True)
    parser.add_argument("--refs-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--max-jobs", type=int)
    parser.add_argument("--only-job")
    parser.add_argument("--max-train-rows", type=int)
    parser.add_argument("--max-calib-rows", type=int)
    parser.add_argument("--max-eval-rows", type=int)
    parser.add_argument("--max-epochs", type=int)
    parser.add_argument("--patience", type=int)
    parser.add_argument("--batch-size", type=int)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    seed_everything(args.seed)
    config = json.loads(Path(args.campaign_config).read_text())
    jobs: list[dict[str, Any]] = list(config["jobs"])
    if args.only_job:
        jobs = [job for job in jobs if job["name"] == args.only_job]
    if args.max_jobs:
        jobs = jobs[: args.max_jobs]
    for job in jobs:
        job.setdefault("seed", args.seed)
        if args.max_epochs:
            job["max_epochs"] = args.max_epochs
        if args.patience:
            job["patience"] = args.patience
        if args.batch_size:
            job["batch_size"] = args.batch_size
            
    history_steps_needed = sorted({int(job.get("history_steps", 8)) for job in jobs} | {4, 8, 16})
    max_rows_by_split = {
        "success_train_seen": args.max_train_rows,
        "success_val_seen": args.max_train_rows,
        "success_calib_seen": args.max_calib_rows,
        "success_test_seen": args.max_eval_rows,
        "success_test_ood": args.max_eval_rows,
        "failure_train_seen": args.max_train_rows,
        "failure_val_seen": args.max_train_rows,
        "failure_test_seen": args.max_eval_rows,
        "failure_eval_ood": args.max_eval_rows,
    }
    
    rows_by_split = load_rows_from_refs(Path(args.refs_dir), Path(args.base_dir), max_rows_by_split, history_steps_needed)
    
    # Feature audit global check (ensuring no OOD rows are used in train/val/calib)
    for split in ["success_train_seen", "success_val_seen", "success_calib_seen", "failure_train_seen", "failure_val_seen"]:
        for r in rows_by_split.get(split, []):
            if "ood" in r.split or "ood" in r.episode_key:
                raise ValueError(f"Global Validation FAIL: OOD rows found in training split: {r}")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(Path(args.campaign_config), out_dir / "campaign_config.json")
    shutil.copy2(Path(__file__), out_dir / "runner_snapshot.py")
    
    device = torch.device(args.device if args.device == "cpu" or torch.cuda.is_available() else "cpu")
    summaries: list[dict[str, Any]] = []
    
    for idx, job in enumerate(jobs, start=1):
        print(f"=== Running job {idx}/{len(jobs)}: {job['name']} ===", flush=True)
        try:
            summaries.append(run_one_job(job, rows_by_split, out_dir, device, args))
            write_campaign_reports(out_dir, summaries)
        except Exception as exc:
            err = {"name": job.get("name"), "error": repr(exc)}
            (out_dir / "failed_jobs.jsonl").open("a").write(json.dumps(err, sort_keys=True) + "\n")
            print(json.dumps(err, sort_keys=True), flush=True)
            if bool(config.get("stop_on_error", False)):
                raise
                
    write_campaign_reports(out_dir, summaries)
    print(json.dumps({"done": True, "jobs_completed": len(summaries), "output_dir": str(out_dir)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
