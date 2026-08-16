"""Corrected new-training ACE and deployable action statistics."""

from __future__ import annotations

import numpy as np

from .constants import ACE_CANDIDATES, ACE_DIM, ACTION_DIM, ACTION_HORIZON


def compute_ace_new_training(chunks_normalized: np.ndarray) -> np.ndarray:
    """Return the trusted L2-log ACE vector from eight alternatives only."""
    arr = np.asarray(chunks_normalized, dtype=np.float32)
    expected = (ACE_CANDIDATES, ACTION_HORIZON, ACTION_DIM)
    if arr.shape != expected:
        raise ValueError(f"expected ACE chunks {expected}, got {arr.shape}")
    if not np.isfinite(arr).all():
        raise ValueError("ACE chunks contain nonfinite values")

    flat = arr.reshape(ACE_CANDIDATES, -1)
    centered = flat - flat.mean(axis=0, keepdims=True)
    per_candidate_l2 = np.linalg.norm(centered, axis=1)
    diffs = flat[:, None, :] - flat[None, :, :]
    pairwise = np.linalg.norm(diffs, axis=-1)
    upper = pairwise[np.triu_indices(ACE_CANDIDATES, 1)]

    translation = arr[:, :, :3].reshape(ACE_CANDIDATES, -1)
    rotation = arr[:, :, 3:6].reshape(ACE_CANDIDATES, -1)
    gripper = arr[:, :, 6:7].reshape(ACE_CANDIDATES, -1)
    result = np.asarray(
        [
            np.log(np.mean(per_candidate_l2) + 1e-6),
            upper.mean(),
            arr.std(axis=0).mean(),
            translation.std(axis=0).mean(),
            rotation.std(axis=0).mean(),
            gripper.std(axis=0).mean(),
            flat.std(axis=0).mean(),
        ],
        dtype=np.float32,
    )
    if result.shape != (ACE_DIM,) or not np.isfinite(result).all():
        raise RuntimeError("ACE computation produced invalid output")
    return result


def action_statistics(chunk_normalized: np.ndarray) -> np.ndarray:
    chunk = np.asarray(chunk_normalized, dtype=np.float32)
    if chunk.shape != (ACTION_HORIZON, ACTION_DIM):
        raise ValueError(f"invalid action chunk shape: {chunk.shape}")
    if not np.isfinite(chunk).all():
        raise ValueError("action chunk contains nonfinite values")
    return np.concatenate(
        [
            chunk[0],
            chunk.mean(axis=0),
            chunk.std(axis=0),
            chunk[-1] - chunk[0],
        ]
    ).astype(np.float32)
