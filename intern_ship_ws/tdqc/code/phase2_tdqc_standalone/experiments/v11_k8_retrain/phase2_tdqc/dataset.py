from __future__ import annotations

import gzip
import json
import random
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset

from .features import DEFAULT_TRACE_FEATURE_KEYS, record_to_episode


def load_jsonl_records(path: str | Path) -> List[Dict[str, Any]]:
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    records: List[Dict[str, Any]] = []
    with opener(path, "rt", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_no}: {exc}") from exc
    return records


def build_dataset_from_jsonl(
    input_jsonl: str | Path,
    *,
    feature_keys: Sequence[str] = DEFAULT_TRACE_FEATURE_KEYS,
    log1p: bool = True,
    min_steps: int = 2,
    feature_mode: str = "summary",
    raw_action_dim: int = 7,
) -> Dict[str, Any]:
    records = load_jsonl_records(input_jsonl)
    episodes: List[Dict[str, Any]] = []
    skipped = 0
    for rec in records:
        ep = record_to_episode(
            rec,
            feature_keys=feature_keys,
            log1p=log1p,
            min_steps=min_steps,
            feature_mode=feature_mode,
            raw_action_dim=raw_action_dim,
        )
        if ep is None:
            skipped += 1
            continue
        episodes.append(ep)
    if not episodes:
        raise ValueError(f"No usable episodes found in {input_jsonl}")
    output_feature_keys = episodes[0].get("feature_keys", list(feature_keys))
    return {
        "episodes": episodes,
        "feature_keys": list(output_feature_keys),
        "log1p": log1p,
        "feature_mode": feature_mode,
        "raw_action_dim": raw_action_dim if feature_mode != "summary" else None,
        "source_jsonl": str(input_jsonl),
        "skipped_episodes": skipped,
    }


def save_tdqc_dataset(dataset: Mapping[str, Any], output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(dict(dataset), output_path)


def load_tdqc_dataset(path: str | Path) -> Dict[str, Any]:
    try:
        obj = torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        obj = torch.load(path, map_location="cpu")
    if "episodes" not in obj:
        raise ValueError(f"{path} does not look like a TDQC dataset: missing 'episodes'")
    return obj


def split_episodes(
    episodes: Sequence[Mapping[str, Any]],
    *,
    val_ratio: float = 0.2,
    seed: int = 7,
    split_by_task: bool = False,
) -> tuple[List[Mapping[str, Any]], List[Mapping[str, Any]]]:
    if not (0.0 < val_ratio < 1.0):
        raise ValueError("val_ratio must be in (0, 1)")
    rng = random.Random(seed)

    if split_by_task:
        task_ids = sorted({ep.get("task_id") for ep in episodes})
        rng.shuffle(task_ids)
        n_val_tasks = max(1, int(round(len(task_ids) * val_ratio)))
        val_tasks = set(task_ids[:n_val_tasks])
        train = [ep for ep in episodes if ep.get("task_id") not in val_tasks]
        val = [ep for ep in episodes if ep.get("task_id") in val_tasks]
    else:
        idx = list(range(len(episodes)))
        rng.shuffle(idx)
        n_val = max(1, int(round(len(idx) * val_ratio)))
        val_idx = set(idx[:n_val])
        train = [episodes[i] for i in idx if i not in val_idx]
        val = [episodes[i] for i in idx if i in val_idx]

    if not train or not val:
        raise ValueError("Empty train or validation split; collect more rollouts or reduce val_ratio")
    return list(train), list(val)


def _rolling_mean(values: np.ndarray, window: int) -> np.ndarray:
    out = np.zeros_like(values, dtype=np.float32)
    for i in range(len(values)):
        start = max(0, i - window + 1)
        out[i] = float(values[start : i + 1].mean())
    return out


def _rolling_std(values: np.ndarray, window: int) -> np.ndarray:
    out = np.zeros_like(values, dtype=np.float32)
    for i in range(len(values)):
        start = max(0, i - window + 1)
        out[i] = float(values[start : i + 1].std())
    return out


def _rolling_slope(values: np.ndarray, window: int) -> np.ndarray:
    out = np.zeros_like(values, dtype=np.float32)
    for i in range(len(values)):
        start = max(0, i - window + 1)
        y = values[start : i + 1].astype(np.float32)
        if len(y) < 2:
            continue
        x = np.arange(len(y), dtype=np.float32)
        x = x - x.mean()
        denom = float((x * x).sum())
        if denom > 0.0:
            out[i] = float((x * (y - y.mean())).sum() / denom)
    return out


def _rolling_max_spike(values: np.ndarray, window: int) -> np.ndarray:
    diffs = np.diff(values, prepend=values[:1]).astype(np.float32)
    out = np.zeros_like(values, dtype=np.float32)
    for i in range(len(values)):
        start = max(0, i - window + 1)
        out[i] = float(np.maximum(diffs[start : i + 1], 0.0).max(initial=0.0))
    return out


def clip_episode_steps(
    episodes: Sequence[Mapping[str, Any]],
    max_steps: int | None,
) -> List[Dict[str, Any]]:
    """Keep only the first max_steps observations while preserving episode labels."""
    if max_steps is None or int(max_steps) <= 0:
        return [dict(ep) for ep in episodes]
    clipped: List[Dict[str, Any]] = []
    limit = int(max_steps)
    for ep in episodes:
        features = np.asarray(ep["features"], dtype=np.float32)
        if features.shape[0] <= 0:
            continue
        new_ep = dict(ep)
        new_ep["features"] = features[:limit].astype(np.float32)
        new_ep["source_num_steps"] = int(features.shape[0])
        new_ep["max_clipped_steps"] = limit
        clipped.append(new_ep)
    return clipped


def add_all_deltas(
    episodes: Sequence[Mapping[str, Any]],
    feature_keys: Sequence[str] | None = None,
) -> tuple[List[Dict[str, Any]], List[str]]:
    """Add per-step deltas for ALL base features.

    Matching the v8 experiment '11 uncertainty + 11 delta' protocol.
    """
    keys = list(feature_keys or [])
    extra_keys = [f"{k}_delta" for k in keys]
    augmented: List[Dict[str, Any]] = []
    for ep in episodes:
        features = np.asarray(ep["features"], dtype=np.float32)
        # diff along time axis (0), prepend first row to keep same length
        deltas = np.diff(features, axis=0, prepend=features[:1, :]).astype(np.float32)
        new_ep = dict(ep)
        new_ep["features"] = np.concatenate([features, deltas], axis=-1).astype(np.float32)
        new_ep["base_feature_dim"] = int(features.shape[-1])
        augmented.append(new_ep)
    return augmented, keys + extra_keys


def add_temporal_features(
    episodes: Sequence[Mapping[str, Any]],
    feature_keys: Sequence[str] | None = None,
    *,
    source_key: str = "mean_last_var",
) -> tuple[List[Dict[str, Any]], List[str]]:
    keys = list(feature_keys or [])
    if source_key not in keys:
        raise ValueError(f"Cannot add temporal features: '{source_key}' not found in feature_keys={keys}")
    idx = keys.index(source_key)
    extra_keys = [
        f"{source_key}_delta",
        f"{source_key}_roll5_mean",
        f"{source_key}_roll5_std",
        f"{source_key}_roll10_mean",
        f"{source_key}_roll10_std",
        f"{source_key}_slope10",
        f"{source_key}_max_spike10",
    ]
    augmented: List[Dict[str, Any]] = []
    for ep in episodes:
        features = np.asarray(ep["features"], dtype=np.float32)
        values = features[:, idx]
        delta = np.diff(values, prepend=values[:1]).astype(np.float32)
        extras = np.stack(
            [
                delta,
                _rolling_mean(values, 5),
                _rolling_std(values, 5),
                _rolling_mean(values, 10),
                _rolling_std(values, 10),
                _rolling_slope(values, 10),
                _rolling_max_spike(values, 10),
            ],
            axis=-1,
        ).astype(np.float32)
        new_ep = dict(ep)
        new_ep["features"] = np.concatenate([features, extras], axis=-1).astype(np.float32)
        new_ep["base_feature_dim"] = int(features.shape[-1])
        new_ep["temporal_feature_source"] = source_key
        augmented.append(new_ep)
    return augmented, keys + extra_keys


class TDQCEpisodeDataset(Dataset):
    def __init__(self, episodes: Sequence[Mapping[str, Any]]):
        self.episodes = list(episodes)

    def __len__(self) -> int:
        return len(self.episodes)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        ep = self.episodes[idx]
        features = torch.as_tensor(ep["features"], dtype=torch.float32)
        success = int(ep["success"])
        return {
            "features": features,
            "success": torch.tensor(success, dtype=torch.float32),
            "failure": torch.tensor(1 - success, dtype=torch.float32),
            "length": torch.tensor(features.shape[0], dtype=torch.long),
            "task_id": ep.get("task_id"),
            "task_suite": ep.get("task_suite"),
            "episode": ep.get("episode"),
        }


class TDQCFixedHorizonWindowDataset(Dataset):
    def __init__(
        self,
        episodes: Sequence[Mapping[str, Any]],
        horizons: Sequence[int],
        *,
        window_size: int,
    ) -> None:
        if window_size <= 0:
            raise ValueError("window_size must be > 0 for fixed-horizon training")
        self.episodes = list(episodes)
        self.horizons = [int(h) for h in horizons]
        self.window_size = int(window_size)
        self.samples: List[tuple[int, int]] = []
        for ep_idx, ep in enumerate(self.episodes):
            L = len(ep["features"])
            for horizon in self.horizons:
                if horizon <= 0:
                    raise ValueError("fixed horizons must be positive")
                if L >= horizon:
                    self.samples.append((ep_idx, horizon))
        if not self.samples:
            raise ValueError("No fixed-horizon samples; check horizons and episode lengths")

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        ep_idx, horizon = self.samples[idx]
        ep = self.episodes[ep_idx]
        features = torch.as_tensor(ep["features"], dtype=torch.float32)
        start = max(0, horizon - self.window_size)
        window = features[start:horizon]
        valid_len = int(window.shape[0])
        if valid_len < self.window_size:
            pad = torch.zeros(self.window_size - valid_len, features.shape[-1], dtype=torch.float32)
            window = torch.cat([pad, window], dim=0)
        mask = torch.zeros(self.window_size, dtype=torch.float32)
        mask[-valid_len:] = 1.0
        success = int(ep["success"])
        return {
            "features": window,
            "valid_masks": mask,
            "success": torch.tensor(success, dtype=torch.float32),
            "failure": torch.tensor(1 - success, dtype=torch.float32),
            "length": torch.tensor(valid_len, dtype=torch.long),
            "horizon": torch.tensor(horizon, dtype=torch.long),
            "task_id": ep.get("task_id"),
            "task_suite": ep.get("task_suite"),
            "episode": ep.get("episode"),
        }

    def balanced_weights(self) -> torch.Tensor:
        counts: Dict[tuple[int, int], int] = {}
        keys: List[tuple[int, int]] = []
        for ep_idx, horizon in self.samples:
            failure = 1 - int(self.episodes[ep_idx]["success"])
            key = (horizon, failure)
            keys.append(key)
            counts[key] = counts.get(key, 0) + 1
        return torch.as_tensor([1.0 / counts[key] for key in keys], dtype=torch.double)


def collate_tdqc_fixed_windows(batch: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    return {
        "features": torch.stack([item["features"] for item in batch]).float(),
        "valid_masks": torch.stack([item["valid_masks"] for item in batch]).float(),
        "lengths": torch.stack([item["length"] for item in batch]).long(),
        "success": torch.stack([item["success"] for item in batch]).float(),
        "failure": torch.stack([item["failure"] for item in batch]).float(),
        "horizon": torch.stack([item["horizon"] for item in batch]).long(),
        "task_id": [item.get("task_id") for item in batch],
        "task_suite": [item.get("task_suite") for item in batch],
        "episode": [item.get("episode") for item in batch],
    }


def collate_tdqc_episodes(batch: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    lengths = torch.stack([item["length"] for item in batch]).long()
    B = len(batch)
    T = int(lengths.max().item())
    F = int(batch[0]["features"].shape[-1])

    features = torch.zeros(B, T, F, dtype=torch.float32)
    valid_masks = torch.zeros(B, T, dtype=torch.float32)
    for i, item in enumerate(batch):
        L = int(item["length"].item())
        features[i, :L] = item["features"]
        valid_masks[i, :L] = 1.0

    success = torch.stack([item["success"] for item in batch]).float()
    failure = torch.stack([item["failure"] for item in batch]).float()
    return {
        "features": features,
        "valid_masks": valid_masks,
        "lengths": lengths,
        "success": success,
        "failure": failure,
        "task_id": [item.get("task_id") for item in batch],
        "task_suite": [item.get("task_suite") for item in batch],
        "episode": [item.get("episode") for item in batch],
    }


def compute_feature_stats(episodes: Sequence[Mapping[str, Any]], eps: float = 1e-6) -> tuple[torch.Tensor, torch.Tensor]:
    arrays = [torch.as_tensor(ep["features"], dtype=torch.float32) for ep in episodes]
    all_features = torch.cat(arrays, dim=0)
    mean = all_features.mean(dim=0)
    std = all_features.std(dim=0).clamp_min(eps)
    return mean, std


def apply_feature_stats(episodes: Sequence[Mapping[str, Any]], mean: torch.Tensor, std: torch.Tensor) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    mean_np = mean.cpu().numpy().astype(np.float32)
    std_np = std.cpu().numpy().astype(np.float32)
    for ep in episodes:
        new_ep = dict(ep)
        new_ep["features"] = (np.asarray(ep["features"], dtype=np.float32) - mean_np) / std_np
        normalized.append(new_ep)
    return normalized
