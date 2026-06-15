#!/usr/bin/env python3
"""Run target-object OOD monitor experiments.

This script is intentionally separate from run_receding_only_fiper_train_eval.py.
It explores alternative monitors while keeping the existing baseline reproducible.

Training rules:
- OOD target-object success/failure rows are never used for training,
  early stopping, or threshold calibration.
- Success-only anomaly models train on success_train_seen only.
- Supervised risk models train on success_train_seen plus failure_eval_seen
  only; they are therefore not pure success-only RND/FIPER, and are reported
  as supervised risk candidates.
- Thresholds are calibrated from success_calib_seen only.
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
    "success_calib_seen",
    "success_test_seen",
    "success_test_ood",
    "failure_eval_seen",
    "failure_eval_ood",
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


def make_history_seq(history: Any, steps: int) -> np.ndarray:
    out = np.zeros((steps, 17), dtype=np.float32)
    hist = history if isinstance(history, list) else []
    tail = hist[-steps:]
    start = steps - len(tail)
    for offset, item in enumerate(tail):
        if not isinstance(item, dict):
            continue
        row = np.concatenate(
            [
                pad_flat(item.get("proprio"), 8),
                pad_flat(item.get("executed_action"), 7),
                np.asarray([float(item.get("reward") or 0.0), float(bool(item.get("success")))], dtype=np.float32),
            ]
        )
        out[start + offset, :] = row[:17]
    return out


def object_set_by_distance(current: dict[str, Any], max_objects: int = 10) -> np.ndarray:
    proprio = pad_flat(current.get("proprio"), 8)
    eef_xyz = proprio[:3]
    positions = current.get("object_positions_before") or {}
    rows: list[np.ndarray] = []
    if isinstance(positions, dict):
        for value in positions.values():
            xyz = pad_flat(value, 3)
            diff = xyz - eef_xyz
            dist = np.asarray([float(np.linalg.norm(diff))], dtype=np.float32)
            rows.append(np.concatenate([xyz, diff, dist]).astype(np.float32))
    rows.sort(key=lambda x: float(x[-1]))
    out = np.zeros((max_objects, 7), dtype=np.float32)
    for i, row in enumerate(rows[:max_objects]):
        out[i, :] = row
    return out


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


def load_rows_from_refs(
    refs_dir: Path,
    base_dir: Path,
    max_rows_by_split: dict[str, int | None],
    history_steps_needed: list[int],
) -> dict[str, list[CompactRow]]:
    out: dict[str, list[CompactRow]] = {}
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
                    histories = {k: make_history_seq(row.get("history"), k) for k in history_steps_needed}
                    split_rows.append(
                        CompactRow(
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
                            objects=object_set_by_distance(current, 10),
                            history_by_k=histories,
                        )
                    )
        out[split] = split_rows
        print(f"Loaded {split}: {len(split_rows)} rows, {len({r.episode_key for r in split_rows})} episodes", flush=True)
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
    histories = np.stack([r.history_by_k[history_steps] for r in rows], axis=0).astype(np.float32)
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
    def __init__(self, hist: np.ndarray, action: np.ndarray, static: np.ndarray, y: np.ndarray | None = None) -> None:
        self.hist = torch.tensor(hist, dtype=torch.float32)
        self.action = torch.tensor(action, dtype=torch.float32)
        self.static = torch.tensor(static, dtype=torch.float32)
        self.y = None if y is None else torch.tensor(y, dtype=torch.float32)

    def __len__(self) -> int:
        return int(self.hist.shape[0])

    def __getitem__(self, idx: int) -> Any:
        item = {"history": self.hist[idx], "action": self.action[idx], "static": self.static[idx]}
        if self.y is None:
            return item
        return item, self.y[idx]


class MLP(nn.Module):
    def __init__(self, dim: int, hidden: list[int], dropout: float = 0.1, out_dim: int = 1) -> None:
        super().__init__()
        layers: list[nn.Module] = []
        cur = dim
        for width in hidden:
            layers.extend([nn.Linear(cur, width), nn.GELU(), nn.Dropout(dropout)])
            cur = width
        layers.append(nn.Linear(cur, out_dim))
        self.net = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


class ResidualBlock(nn.Module):
    def __init__(self, dim: int, dropout: float) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.LayerNorm(dim), nn.Linear(dim, dim * 2), nn.GELU(), nn.Dropout(dropout), nn.Linear(dim * 2, dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.net(x)


class ResidualMLP(nn.Module):
    def __init__(self, dim: int, width: int = 512, blocks: int = 4, dropout: float = 0.12, out_dim: int = 1) -> None:
        super().__init__()
        self.inp = nn.Linear(dim, width)
        self.blocks = nn.Sequential(*[ResidualBlock(width, dropout) for _ in range(blocks)])
        self.head = nn.Linear(width, out_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.head(self.blocks(self.inp(x))).squeeze(-1)


class SeqRiskModel(nn.Module):
    def __init__(
        self,
        kind: str,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 2,
        heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.kind = kind
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
        elif kind == "transformer":
            enc_layer = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=dropout, batch_first=True, activation="gelu")
            self.cls = nn.Parameter(torch.zeros(1, 1, width))
            self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
            self.seq = nn.TransformerEncoder(enc_layer, layers)
        else:
            raise ValueError(f"unknown sequence model {kind}")
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(nn.LayerNorm(width * 2), nn.Linear(width * 2, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1))

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        if self.kind == "tcn":
            seq = self.seq(tokens.transpose(1, 2)).squeeze(-1)
        elif self.kind in {"gru", "lstm"}:
            _out, state = self.seq(tokens)
            if isinstance(state, tuple):
                state = state[0]
            seq = state[-1]
        else:
            bsz = tokens.shape[0]
            tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
            seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(batch["static"])
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


class RNDPair(nn.Module):
    def __init__(self, dim: int, hidden: list[int], embed_dim: int = 128, dropout: float = 0.0) -> None:
        super().__init__()
        self.predictor = MLP(dim, hidden, dropout, embed_dim)
        self.target = MLP(dim, hidden, 0.0, embed_dim)
        for p in self.target.parameters():
            p.requires_grad = False

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.predictor(x), self.target(x)

    def score(self, x: torch.Tensor) -> torch.Tensor:
        pred, targ = self.forward(x)
        return torch.mean((pred - targ) ** 2, dim=-1)


class AutoEncoder(nn.Module):
    def __init__(self, dim: int, hidden: list[int], latent: int = 64, dropout: float = 0.1) -> None:
        super().__init__()
        enc: list[nn.Module] = []
        cur = dim
        for width in hidden:
            enc.extend([nn.Linear(cur, width), nn.GELU(), nn.Dropout(dropout)])
            cur = width
        enc.append(nn.Linear(cur, latent))
        dec: list[nn.Module] = []
        cur = latent
        for width in reversed(hidden):
            dec.extend([nn.Linear(cur, width), nn.GELU(), nn.Dropout(dropout)])
            cur = width
        dec.append(nn.Linear(cur, dim))
        self.encoder = nn.Sequential(*enc)
        self.decoder = nn.Sequential(*dec)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.decoder(self.encoder(x))

    def score(self, x: torch.Tensor) -> torch.Tensor:
        recon = self.forward(x)
        return torch.mean((recon - x) ** 2, dim=-1)


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


def split_by_episode(rows: list[CompactRow], val_fraction: float, seed: int) -> tuple[list[int], list[int]]:
    by_ep: dict[str, list[int]] = defaultdict(list)
    for idx, row in enumerate(rows):
        by_ep[row.episode_key].append(idx)
    eps = sorted(by_ep)
    rng = random.Random(seed)
    rng.shuffle(eps)
    n_val = max(1, int(round(len(eps) * val_fraction))) if eps else 0
    val_eps = set(eps[:n_val])
    train_idx: list[int] = []
    val_idx: list[int] = []
    for ep, indices in by_ep.items():
        if ep in val_eps:
            val_idx.extend(indices)
        else:
            train_idx.extend(indices)
    return train_idx, val_idx


def make_vector_inputs(rows_by_split: dict[str, list[CompactRow]], cfg: dict[str, Any], mode: str) -> dict[str, Any]:
    seed = int(cfg.get("seed", 42))
    if mode == "supervised":
        success_rows = rows_by_split["success_train_seen"]
        fail_rows = rows_by_split["failure_eval_seen"]
        s_train, s_val = split_by_episode(success_rows, float(cfg.get("val_fraction", 0.15)), seed)
        f_train, f_val = split_by_episode(fail_rows, float(cfg.get("val_fraction", 0.15)), seed + 17)
        train_rows = [success_rows[i] for i in s_train] + [fail_rows[i] for i in f_train]
        val_rows = [success_rows[i] for i in s_val] + [fail_rows[i] for i in f_val]
        y_train = np.asarray([0.0] * len(s_train) + [1.0] * len(f_train), dtype=np.float32)
        y_val = np.asarray([0.0] * len(s_val) + [1.0] * len(f_val), dtype=np.float32)
    else:
        success_rows = rows_by_split["success_train_seen"]
        s_train, s_val = split_by_episode(success_rows, float(cfg.get("val_fraction", 0.15)), seed)
        train_rows = [success_rows[i] for i in s_train]
        val_rows = [success_rows[i] for i in s_val]
        y_train = None
        y_val = None
    x_train_raw = vector_features(train_rows, cfg)
    stats = fit_standardizer(x_train_raw)
    return {
        "train_rows": train_rows,
        "val_rows": val_rows,
        "x_train": apply_standardizer(x_train_raw, stats),
        "x_val": apply_standardizer(vector_features(val_rows, cfg), stats),
        "y_train": y_train,
        "y_val": y_val,
        "stats": stats,
    }


def make_seq_inputs(rows_by_split: dict[str, list[CompactRow]], cfg: dict[str, Any]) -> dict[str, Any]:
    seed = int(cfg.get("seed", 42))
    success_rows = rows_by_split["success_train_seen"]
    fail_rows = rows_by_split["failure_eval_seen"]
    s_train, s_val = split_by_episode(success_rows, float(cfg.get("val_fraction", 0.15)), seed)
    f_train, f_val = split_by_episode(fail_rows, float(cfg.get("val_fraction", 0.15)), seed + 17)
    train_rows = [success_rows[i] for i in s_train] + [fail_rows[i] for i in f_train]
    val_rows = [success_rows[i] for i in s_val] + [fail_rows[i] for i in f_val]
    y_train = np.asarray([0.0] * len(s_train) + [1.0] * len(f_train), dtype=np.float32)
    y_val = np.asarray([0.0] * len(s_val) + [1.0] * len(f_val), dtype=np.float32)
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
        "stats": {"history": h_stats, "action": a_stats, "static": st_stats},
    }


def move_batch(batch: Any, device: torch.device) -> Any:
    if torch.is_tensor(batch):
        return batch.to(device)
    if isinstance(batch, dict):
        return {k: v.to(device) if torch.is_tensor(v) else v for k, v in batch.items()}
    return batch


def train_supervised_vector(x: np.ndarray, y: np.ndarray, xv: np.ndarray, yv: np.ndarray, cfg: dict[str, Any], device: torch.device) -> tuple[nn.Module, list[dict[str, Any]], int]:
    hidden = list(cfg.get("hidden", [256, 128]))
    dropout = float(cfg.get("dropout", 0.1))
    model_name = str(cfg.get("model", "mlp"))
    model: nn.Module
    if model_name == "residual_mlp":
        model = ResidualMLP(x.shape[1], int(cfg.get("width", 512)), int(cfg.get("blocks", 4)), dropout)
    else:
        model = MLP(x.shape[1], hidden, dropout)
    return train_supervised_model(model, VectorDataset(x, y), VectorDataset(xv, yv), cfg, device)


def train_supervised_sequence(inputs: dict[str, Any], cfg: dict[str, Any], device: torch.device) -> tuple[nn.Module, list[dict[str, Any]], int]:
    model = SeqRiskModel(
        str(cfg.get("model", "tcn")).replace("seq_", ""),
        hist_dim=inputs["h_train"].shape[-1],
        action_dim=inputs["a_train"].shape[-1],
        static_dim=inputs["st_train"].shape[-1],
        width=int(cfg.get("width", 128)),
        layers=int(cfg.get("layers", 2)),
        heads=int(cfg.get("heads", 4)),
        dropout=float(cfg.get("dropout", 0.1)),
    )
    train_ds = SeqDataset(inputs["h_train"], inputs["a_train"], inputs["st_train"], inputs["y_train"])
    val_ds = SeqDataset(inputs["h_val"], inputs["a_val"], inputs["st_val"], inputs["y_val"])
    return train_supervised_model(model, train_ds, val_ds, cfg, device)


def train_supervised_model(model: nn.Module, train_ds: Dataset, val_ds: Dataset, cfg: dict[str, Any], device: torch.device) -> tuple[nn.Module, list[dict[str, Any]], int]:
    model = model.to(device)
    batch_size = int(cfg.get("batch_size", 256))
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, drop_last=False)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, drop_last=False)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(cfg.get("lr", 2e-4)), weight_decay=float(cfg.get("weight_decay", 1e-4)))
    pos_weight_value = float(cfg.get("pos_weight", 1.0))
    pos_weight = torch.tensor([pos_weight_value], dtype=torch.float32, device=device)
    loss_name = str(cfg.get("loss", "bce"))
    max_epochs = int(cfg.get("max_epochs", 120))
    patience = int(cfg.get("patience", 15))
    best_state: dict[str, torch.Tensor] | None = None
    best_score = -1e9
    best_epoch = 0
    no_improve = 0
    history: list[dict[str, Any]] = []
    for epoch in range(1, max_epochs + 1):
        model.train()
        losses: list[float] = []
        for batch in train_loader:
            xb, yb = batch
            xb = move_batch(xb, device)
            yb = yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(xb)
            bce = nn.functional.binary_cross_entropy_with_logits(logits, yb, pos_weight=pos_weight, reduction="none")
            if loss_name == "focal":
                prob = torch.sigmoid(logits.detach())
                pt = torch.where(yb > 0.5, prob, 1.0 - prob)
                loss = (((1.0 - pt) ** float(cfg.get("focal_gamma", 2.0))) * bce).mean()
            else:
                loss = bce.mean()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            losses.append(float(loss.detach().cpu()))
        val_scores, val_y = predict_supervised(model, val_loader, device)
        auc = auroc_binary(val_y, val_scores)
        brier = float(np.mean((val_scores - val_y) ** 2))
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
        for batch in loader:
            xb, yb = batch
            xb = move_batch(xb, device)
            logits = model(xb)
            scores.append(torch.sigmoid(logits).detach().cpu().numpy())
            labels.append(yb.detach().cpu().numpy())
    return np.concatenate(scores), np.concatenate(labels)


def train_rnd(x: np.ndarray, xv: np.ndarray, cfg: dict[str, Any], device: torch.device) -> tuple[RNDPair, list[dict[str, Any]], int]:
    model = RNDPair(x.shape[1], list(cfg.get("hidden", [256, 256])), int(cfg.get("embed_dim", 128)), float(cfg.get("dropout", 0.0))).to(device)
    optimizer = torch.optim.AdamW(model.predictor.parameters(), lr=float(cfg.get("lr", 2e-4)), weight_decay=float(cfg.get("weight_decay", 1e-5)))
    return train_success_only_score_model(model, x, xv, cfg, device, optimizer, "rnd")


def train_ae(x: np.ndarray, xv: np.ndarray, cfg: dict[str, Any], device: torch.device) -> tuple[AutoEncoder, list[dict[str, Any]], int]:
    model = AutoEncoder(x.shape[1], list(cfg.get("hidden", [256, 128])), int(cfg.get("latent", 64)), float(cfg.get("dropout", 0.1))).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(cfg.get("lr", 2e-4)), weight_decay=float(cfg.get("weight_decay", 1e-5)))
    return train_success_only_score_model(model, x, xv, cfg, device, optimizer, "ae")


def train_success_only_score_model(model: Any, x: np.ndarray, xv: np.ndarray, cfg: dict[str, Any], device: torch.device, optimizer: torch.optim.Optimizer, kind: str) -> tuple[Any, list[dict[str, Any]], int]:
    train_loader = DataLoader(VectorDataset(x), batch_size=int(cfg.get("batch_size", 256)), shuffle=True)
    val_tensor = torch.tensor(xv, dtype=torch.float32, device=device)
    max_epochs = int(cfg.get("max_epochs", 120))
    patience = int(cfg.get("patience", 15))
    best_state: dict[str, torch.Tensor] | None = None
    best_loss = float("inf")
    best_epoch = 0
    no_improve = 0
    history: list[dict[str, Any]] = []
    for epoch in range(1, max_epochs + 1):
        model.train()
        losses: list[float] = []
        for xb in train_loader:
            xb = xb.to(device)
            optimizer.zero_grad(set_to_none=True)
            if kind == "rnd":
                loss = model.score(xb).mean()
            else:
                recon = model(xb)
                if cfg.get("denoise", False):
                    noisy = torch.clamp(xb + torch.randn_like(xb) * float(cfg.get("noise_std", 0.05)), -10.0, 10.0)
                    recon = model(noisy)
                loss = torch.mean((recon - xb) ** 2)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            losses.append(float(loss.detach().cpu()))
        model.eval()
        with torch.no_grad():
            val_loss = float(model.score(val_tensor).mean().detach().cpu())
        row = {"epoch": epoch, "train_loss": float(np.mean(losses)), "val_success_score": val_loss}
        history.append(row)
        print(json.dumps({"job": cfg["name"], **row}, sort_keys=True), flush=True)
        if val_loss < best_loss - 1e-8:
            best_loss = val_loss
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


def score_vector_model(model: Any, x: np.ndarray, cfg: dict[str, Any], device: torch.device) -> np.ndarray:
    loader = DataLoader(VectorDataset(x), batch_size=int(cfg.get("batch_size", 512)), shuffle=False)
    model.eval()
    scores: list[np.ndarray] = []
    with torch.no_grad():
        for xb in loader:
            xb = xb.to(device)
            mode = str(cfg.get("mode"))
            if mode == "supervised":
                score = torch.sigmoid(model(xb))
            else:
                score = model.score(xb)
            scores.append(score.detach().cpu().numpy())
    return np.concatenate(scores)


def score_seq_model(model: nn.Module, hist: np.ndarray, action: np.ndarray, static: np.ndarray, cfg: dict[str, Any], device: torch.device) -> np.ndarray:
    loader = DataLoader(SeqDataset(hist, action, static), batch_size=int(cfg.get("batch_size", 512)), shuffle=False)
    model.eval()
    scores: list[np.ndarray] = []
    with torch.no_grad():
        for xb in loader:
            xb = move_batch(xb, device)
            scores.append(torch.sigmoid(model(xb)).detach().cpu().numpy())
    return np.concatenate(scores)


def consecutive_first_idx(bools: list[bool], k: int) -> int | None:
    for i in range(0, len(bools) - k + 1):
        if all(bools[i : i + k]):
            return i
    return None


def summarize_policy(rows: list[CompactRow], score_alarm: np.ndarray, ace_alarm: np.ndarray, k: int, mode: str) -> dict[str, Any]:
    by_ep: dict[str, list[tuple[int, bool, bool]]] = defaultdict(list)
    for row, s_alarm, a_alarm in zip(rows, score_alarm, ace_alarm):
        by_ep[row.episode_key].append((row.timestep, bool(s_alarm), bool(a_alarm)))
    detected = 0
    d10 = d25 = d50 = 0
    first_times: list[float] = []
    alarm_steps_per_ep: list[int] = []
    for ep_rows in by_ep.values():
        ep_rows.sort(key=lambda x: x[0])
        if mode == "score":
            raw = [x[1] for x in ep_rows]
        elif mode == "ace":
            raw = [x[2] for x in ep_rows]
        elif mode == "and":
            raw = [x[1] and x[2] for x in ep_rows]
        else:
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
            d10 += norm <= 0.10
            d25 += norm <= 0.25
            d50 += norm <= 0.50
    n = max(1, len(by_ep))
    return {
        "episodes": len(by_ep),
        "episode_alarm_rate": detected / n,
        "never_rate": 1.0 - detected / n,
        "det_at_10": d10 / n,
        "det_at_25": d25 / n,
        "det_at_50": d50 / n,
        "mean_first_norm_detected": float(np.mean(first_times)) if first_times else None,
        "median_first_norm_detected": float(np.median(first_times)) if first_times else None,
        "mean_alarm_steps": float(np.mean(alarm_steps_per_ep)) if alarm_steps_per_ep else 0.0,
        "median_alarm_steps": float(np.median(alarm_steps_per_ep)) if alarm_steps_per_ep else 0.0,
    }


def evaluate_job(
    rows_by_split: dict[str, list[CompactRow]],
    scores_by_split: dict[str, np.ndarray],
    thresholds: dict[str, dict[str, float]],
) -> dict[str, Any]:
    ace_thresholds = thresholds["ace"]
    score_thresholds = thresholds["score"]
    out: dict[str, Any] = {"row_metrics": {}, "episode_metrics": {}}
    for split, rows in rows_by_split.items():
        if split not in scores_by_split or split == "success_train_seen":
            continue
        scores = scores_by_split[split]
        ace_entropy = np.asarray([r.ace[0] for r in rows], dtype=np.float32)
        row_metrics: dict[str, Any] = {"rows": len(rows), "episodes": len({r.episode_key for r in rows})}
        for q in ["q90", "q95", "q99"]:
            s_alarm = scores > score_thresholds[q]
            a_alarm = ace_entropy > ace_thresholds[q]
            row_metrics[f"score_alarm_{q}"] = float(np.mean(s_alarm))
            row_metrics[f"ace_alarm_{q}"] = float(np.mean(a_alarm))
            row_metrics[f"or_alarm_{q}"] = float(np.mean(s_alarm | a_alarm))
            row_metrics[f"and_alarm_{q}"] = float(np.mean(s_alarm & a_alarm))
        out["row_metrics"][split] = row_metrics
        out["episode_metrics"][split] = {}
        for q in ["q95", "q99"]:
            s_alarm = scores > score_thresholds[q]
            a_alarm = ace_entropy > ace_thresholds[q]
            for k in [1, 2, 3, 5, 10]:
                for mode in ["score", "ace", "or", "and"]:
                    out["episode_metrics"][split][f"{mode}_{q}_K{k}"] = summarize_policy(rows, s_alarm, a_alarm, k, mode)
    return out


def campaign_objective(metrics: dict[str, Any]) -> float:
    ep = metrics["episode_metrics"]
    ood_fail = ep["failure_eval_ood"]["or_q95_K3"]
    ood_succ = ep["success_test_ood"]["or_q95_K3"]
    seen_succ = ep["success_test_seen"]["or_q95_K3"]
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
    job_dir = out_dir / "jobs" / cfg["name"]
    if (job_dir / "summary.json").exists() and not global_args.force:
        return json.loads((job_dir / "summary.json").read_text())
    job_dir.mkdir(parents=True, exist_ok=True)
    (job_dir / "config.json").write_text(json.dumps(cfg, indent=2, sort_keys=True) + "\n")
    mode = str(cfg["mode"])
    use_sequence = str(cfg.get("model", "")).startswith("seq_")
    start = time.time()
    if use_sequence:
        inputs = make_seq_inputs(rows_by_split, cfg)
        model, history, best_epoch = train_supervised_sequence(inputs, cfg, device)
        scores_by_split: dict[str, np.ndarray] = {}
        for split, rows in rows_by_split.items():
            h_raw, a_raw, st_raw = sequence_features(rows, cfg)
            h = apply_seq_standardizer(h_raw, inputs["stats"]["history"])
            a = apply_seq_standardizer(a_raw, inputs["stats"]["action"])
            st = apply_standardizer(st_raw, inputs["stats"]["static"])
            scores_by_split[split] = score_seq_model(model, h, a, st, cfg, device)
    else:
        inputs = make_vector_inputs(rows_by_split, cfg, mode)
        if mode == "supervised":
            model, history, best_epoch = train_supervised_vector(inputs["x_train"], inputs["y_train"], inputs["x_val"], inputs["y_val"], cfg, device)
        elif mode == "rnd":
            model, history, best_epoch = train_rnd(inputs["x_train"], inputs["x_val"], cfg, device)
        elif mode == "ae":
            model, history, best_epoch = train_ae(inputs["x_train"], inputs["x_val"], cfg, device)
        else:
            raise ValueError(f"unsupported mode {mode}")
        scores_by_split = {}
        for split, rows in rows_by_split.items():
            x = apply_standardizer(vector_features(rows, cfg), inputs["stats"])
            scores_by_split[split] = score_vector_model(model, x, cfg, device)
    calib_scores = scores_by_split["success_calib_seen"]
    calib_ace = np.asarray([r.ace[0] for r in rows_by_split["success_calib_seen"]], dtype=np.float32)
    thresholds = {
        "score": {q: float(np.quantile(calib_scores, val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()},
        "ace": {q: float(np.quantile(calib_ace, val)) for q, val in {"q90": 0.90, "q95": 0.95, "q99": 0.99}.items()},
    }
    metrics = evaluate_job(rows_by_split, scores_by_split, thresholds)
    metrics["objective"] = campaign_objective(metrics)
    summary = {
        "name": cfg["name"],
        "mode": mode,
        "model": cfg.get("model"),
        "feature_notes": cfg.get("notes", ""),
        "best_epoch": best_epoch,
        "runtime_seconds": time.time() - start,
        "thresholds": thresholds,
        "objective": metrics["objective"],
        "key_metrics": {
            "success_test_seen_or_q95_K3_fa": metrics["episode_metrics"]["success_test_seen"]["or_q95_K3"]["episode_alarm_rate"],
            "success_test_ood_or_q95_K3_fa": metrics["episode_metrics"]["success_test_ood"]["or_q95_K3"]["episode_alarm_rate"],
            "failure_eval_ood_or_q95_K3_det": metrics["episode_metrics"]["failure_eval_ood"]["or_q95_K3"]["episode_alarm_rate"],
            "failure_eval_ood_or_q95_K3_det25": metrics["episode_metrics"]["failure_eval_ood"]["or_q95_K3"]["det_at_25"],
            "failure_eval_ood_or_q95_K3_mean_time": metrics["episode_metrics"]["failure_eval_ood"]["or_q95_K3"]["mean_first_norm_detected"],
            "success_test_ood_score_q95_K3_fa": metrics["episode_metrics"]["success_test_ood"]["score_q95_K3"]["episode_alarm_rate"],
            "failure_eval_ood_score_q95_K3_det25": metrics["episode_metrics"]["failure_eval_ood"]["score_q95_K3"]["det_at_25"],
        },
    }
    torch.save(model.state_dict(), job_dir / "model.pt")
    (job_dir / "training_history.json").write_text(json.dumps(history, indent=2, sort_keys=True) + "\n")
    (job_dir / "thresholds.json").write_text(json.dumps(thresholds, indent=2, sort_keys=True) + "\n")
    (job_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n")
    (job_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    score_rows = []
    for split, rows in rows_by_split.items():
        if split == "success_train_seen":
            continue
        for row, score in zip(rows, scores_by_split[split]):
            score_rows.append(
                {
                    "split": split,
                    "episode_key": row.episode_key,
                    "timestep": row.timestep,
                    "score": float(score),
                    "ace_entropy": float(row.ace[0]),
                    "outcome": row.outcome,
                }
            )
    write_jsonl(job_dir / "scores.jsonl", score_rows)
    return summary


def write_campaign_reports(out_dir: Path, summaries: list[dict[str, Any]]) -> None:
    rows = sorted(summaries, key=lambda r: r["objective"], reverse=True)
    csv_path = out_dir / "campaign_summary.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "rank",
                "name",
                "mode",
                "model",
                "objective",
                "best_epoch",
                "success_test_seen_or_q95_K3_fa",
                "success_test_ood_or_q95_K3_fa",
                "failure_eval_ood_or_q95_K3_det",
                "failure_eval_ood_or_q95_K3_det25",
                "failure_eval_ood_or_q95_K3_mean_time",
                "success_test_ood_score_q95_K3_fa",
                "failure_eval_ood_score_q95_K3_det25",
            ],
        )
        writer.writeheader()
        for rank, row in enumerate(rows, start=1):
            flat = {k: row.get(k) for k in ["name", "mode", "model", "objective", "best_epoch"]}
            flat.update(row["key_metrics"])
            flat["rank"] = rank
            writer.writerow(flat)
    (out_dir / "campaign_summary.json").write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    md_lines = [
        "# Target-Object OOD 50-Experiment Campaign Report",
        "",
        "This is an automatically generated intermediate report. A human audit is still required before trusting any final deployment rule.",
        "",
        "| Rank | Job | Mode | Model | Objective | OOD Success FA OR q95 K3 | OOD Failure Det OR q95 K3 | OOD Failure Det@25 OR q95 K3 |",
        "|---:|---|---|---|---:|---:|---:|---:|",
    ]
    for rank, row in enumerate(rows[:20], start=1):
        km = row["key_metrics"]
        md_lines.append(
            f"| {rank} | `{row['name']}` | {row['mode']} | {row.get('model')} | {row['objective']:.4f} | "
            f"{km['success_test_ood_or_q95_K3_fa']:.2%} | {km['failure_eval_ood_or_q95_K3_det']:.2%} | {km['failure_eval_ood_or_q95_K3_det25']:.2%} |"
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
        "success_calib_seen": args.max_calib_rows,
        "success_test_seen": args.max_eval_rows,
        "success_test_ood": args.max_eval_rows,
        "failure_eval_seen": args.max_eval_rows,
        "failure_eval_ood": args.max_eval_rows,
    }
    rows_by_split = load_rows_from_refs(Path(args.refs_dir), Path(args.base_dir), max_rows_by_split, history_steps_needed)
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
        except Exception as exc:  # noqa: BLE001
            err = {"name": job.get("name"), "error": repr(exc)}
            (out_dir / "failed_jobs.jsonl").open("a").write(json.dumps(err, sort_keys=True) + "\n")
            print(json.dumps(err, sort_keys=True), flush=True)
            if bool(config.get("stop_on_error", False)):
                raise
    write_campaign_reports(out_dir, summaries)
    print(json.dumps({"done": True, "jobs_completed": len(summaries), "output_dir": str(out_dir)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
