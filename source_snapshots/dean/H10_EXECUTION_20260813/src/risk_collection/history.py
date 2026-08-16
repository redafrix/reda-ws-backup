"""Episode-local 16x21 deployable history."""

from __future__ import annotations

from collections import deque

import numpy as np

from .constants import ACE_DIM, ACTION_DIM, HISTORY_DIM, HISTORY_STEPS, PROPRIO_DIM


class DeployableHistory:
    def __init__(self) -> None:
        self._rows: deque[np.ndarray] = deque(maxlen=HISTORY_STEPS)

    def reset(self) -> None:
        self._rows.clear()

    def snapshot(self) -> np.ndarray:
        out = np.zeros((HISTORY_STEPS, HISTORY_DIM), dtype=np.float32)
        rows = list(self._rows)
        if rows:
            out[-len(rows) :] = np.stack(rows)
        return out

    def append(
        self,
        proprio: np.ndarray,
        executed_action: np.ndarray,
        ace: np.ndarray,
    ) -> None:
        proprio = np.asarray(proprio, dtype=np.float32)
        action = np.asarray(executed_action, dtype=np.float32)
        ace = np.asarray(ace, dtype=np.float32)
        if proprio.shape != (PROPRIO_DIM,):
            raise ValueError(f"invalid proprio shape: {proprio.shape}")
        if action.shape != (ACTION_DIM,):
            raise ValueError(f"invalid executed action shape: {action.shape}")
        if ace.shape != (ACE_DIM,):
            raise ValueError(f"invalid ACE shape: {ace.shape}")
        row = np.concatenate([proprio, action, ace[:6]]).astype(np.float32)
        if row.shape != (HISTORY_DIM,) or not np.isfinite(row).all():
            raise ValueError("invalid history row")
        self._rows.append(row)
