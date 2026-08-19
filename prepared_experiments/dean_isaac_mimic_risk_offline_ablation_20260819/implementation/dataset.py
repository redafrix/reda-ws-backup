"""Dataset, normalization, and window builder for Isaac Mimic H10 monitor."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset

from .constants import (
    HISTORY_WINDOW_LENGTH,
    HORIZON_CHANNELS,
    HORIZON_STEPS,
    SCALAR_DIM,
)


def fit_normalization(
    train_scalars: np.ndarray,
    train_horizon: np.ndarray,
    std_floor: float = 1e-6,
) -> Dict[str, Any]:
    """Fit mean and std on train split only."""
    s_arr = np.asarray(train_scalars, dtype=np.float32)
    h_arr = np.asarray(train_horizon, dtype=np.float32)

    if s_arr.shape[-1] != SCALAR_DIM:
        raise ValueError(f"Expected scalar dim {SCALAR_DIM}, got {s_arr.shape[-1]}")
    if h_arr.shape[1:] != (HORIZON_STEPS, HORIZON_CHANNELS):
        raise ValueError(f"Expected horizon shape (*, {HORIZON_STEPS}, {HORIZON_CHANNELS}), got {h_arr.shape}")

    # Scalar normalization (per-coordinate)
    scalar_mean = np.mean(s_arr, axis=0)
    scalar_std = np.std(s_arr, axis=0)
    scalar_std = np.where(scalar_std < std_floor, std_floor, scalar_std)

    # Horizon normalization (per-channel across all train rows and 10 horizon positions)
    flat_h = h_arr.reshape(-1, HORIZON_CHANNELS)
    horizon_mean = np.mean(flat_h, axis=0)
    horizon_std = np.std(flat_h, axis=0)
    horizon_std = np.where(horizon_std < std_floor, std_floor, horizon_std)

    return {
        "scalar_mean": scalar_mean.tolist(),
        "scalar_std": scalar_std.tolist(),
        "horizon_mean": horizon_mean.tolist(),
        "horizon_std": horizon_std.tolist(),
        "std_floor": std_floor,
    }


def apply_normalization(
    scalars: np.ndarray,
    horizon: np.ndarray,
    norm_params: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray]:
    """Apply fitted normalization to scalar and horizon arrays."""
    s_mean = np.array(norm_params["scalar_mean"], dtype=np.float32)
    s_std = np.array(norm_params["scalar_std"], dtype=np.float32)
    h_mean = np.array(norm_params["horizon_mean"], dtype=np.float32)
    h_std = np.array(norm_params["horizon_std"], dtype=np.float32)

    norm_s = ((scalars - s_mean) / s_std).astype(np.float32)
    norm_h = ((horizon - h_mean) / h_std).astype(np.float32)
    return norm_s, norm_h


class IsaacMimicWindowDataset(Dataset):
    """Query-centered 8-record window dataset with left zero-padding."""

    def __init__(
        self,
        raw_scalars: np.ndarray,
        raw_horizon: np.ndarray,
        labels: np.ndarray,
        episode_indices: np.ndarray,
        decision_indices: np.ndarray,
        norm_params: Dict[str, Any],
        row_indices: np.ndarray | None = None,
    ) -> None:
        self.norm_scalars, self.norm_horizon = apply_normalization(
            raw_scalars, raw_horizon, norm_params
        )
        self.labels = np.asarray(labels, dtype=np.float32)
        self.episode_indices = np.asarray(episode_indices, dtype=np.int64)
        self.decision_indices = np.asarray(decision_indices, dtype=np.int64)

        if row_indices is None:
            self.active_indices = np.arange(len(self.labels), dtype=np.int64)
        else:
            self.active_indices = np.asarray(row_indices, dtype=np.int64)

        # Build episode row lookup for fast window assembly
        self._build_episode_lookup()

    def _build_episode_lookup(self) -> None:
        self.ep_row_ranges: Dict[int, Tuple[int, int]] = {}
        n_rows = len(self.labels)
        if n_rows == 0:
            return
        
        cur_ep = self.episode_indices[0]
        start_idx = 0
        for i in range(1, n_rows):
            if self.episode_indices[i] != cur_ep:
                self.ep_row_ranges[cur_ep] = (start_idx, i)
                cur_ep = self.episode_indices[i]
                start_idx = i
        self.ep_row_ranges[cur_ep] = (start_idx, n_rows)

    def __len__(self) -> int:
        return len(self.active_indices)

    def __getitem__(self, item_idx: int) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        row_idx = int(self.active_indices[item_idx])
        ep_id = int(self.episode_indices[row_idx])
        dec_idx = int(self.decision_indices[row_idx])
        label = float(self.labels[row_idx])

        ep_start, ep_end = self.ep_row_ranges[ep_id]
        # Slice queries up to current row
        start_q = max(ep_start, row_idx - HISTORY_WINDOW_LENGTH + 1)
        end_q = row_idx + 1

        s_slice = self.norm_scalars[start_q:end_q]      # [L, 37]
        h_slice = self.norm_horizon[start_q:end_q]      # [L, 10, 6]
        L = s_slice.shape[0]

        if L < HISTORY_WINDOW_LENGTH:
            pad_len = HISTORY_WINDOW_LENGTH - L
            s_pad = np.zeros((pad_len, SCALAR_DIM), dtype=np.float32)
            h_pad = np.zeros((pad_len, HORIZON_STEPS, HORIZON_CHANNELS), dtype=np.float32)
            window_s = np.concatenate([s_pad, s_slice], axis=0)
            window_h = np.concatenate([h_pad, h_slice], axis=0)
        else:
            window_s = s_slice
            window_h = h_slice

        return (
            torch.from_numpy(window_s),
            torch.from_numpy(window_h),
            torch.tensor(label, dtype=torch.float32),
        )
