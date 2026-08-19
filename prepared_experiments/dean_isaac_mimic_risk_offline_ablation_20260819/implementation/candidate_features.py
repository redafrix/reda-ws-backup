"""Candidate disagreement scalars, 10x6 horizon features, and temporal changes."""

from __future__ import annotations

from typing import Tuple
import numpy as np

from .constants import HORIZON_STEPS, HORIZON_CHANNELS, PRIMARY_CANDIDATES


def compute_disagreement_and_horizon_features(
    candidates_10d: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute 9 disagreement scalars and [10, 6] horizon tensor from 8 candidates in 10D.
    
    Args:
        candidates_10d: [8, 10, 10] float32 array of 8 candidates in 10D monitor representation
        
    Returns:
        scalars_9: [9] float32 array
        horizon_10x6: [10, 6] float32 array
    """
    C = np.asarray(candidates_10d, dtype=np.float32)
    if C.shape != (PRIMARY_CANDIDATES, HORIZON_STEPS, 10):
        raise ValueError(f"Expected shape ({PRIMARY_CANDIDATES}, {HORIZON_STEPS}, 10), got {C.shape}")

    # Population variance across candidates (ddof=0)
    var_cand = np.var(C, axis=0, ddof=0)  # [10, 10]

    # 1. w2a_action_variance_mean
    s1_var_mean = float(np.mean(var_cand))

    # 2. w2a_action_variance_max
    s2_var_max = float(np.max(var_cand))

    # 3. w2a_pairwise_mse_mean over 28 unordered candidate pairs
    pairwise_mses = []
    for i in range(PRIMARY_CANDIDATES):
        for j in range(i + 1, PRIMARY_CANDIDATES):
            diff = C[i] - C[j]
            pairwise_mses.append(float(np.mean(diff ** 2)))
    s3_pairwise_mse_mean = float(np.mean(pairwise_mses))

    # 4. w2a_first_candidate_vs_mean_mse
    mean_candidate = np.mean(C, axis=0)  # [10, 10]
    s4_cand0_vs_mean_mse = float(np.mean((C[0] - mean_candidate) ** 2))

    # Cumulative positions: P[c, h] = sum_{k=0..h} C[c, k, 0:3]
    P = np.cumsum(C[:, :, :3], axis=1)  # [8, 10, 3]

    # Endpoint position spread (at h=9) over 28 pairs
    endpoint_dists = []
    for i in range(PRIMARY_CANDIDATES):
        for j in range(i + 1, PRIMARY_CANDIDATES):
            d = np.linalg.norm(P[i, 9] - P[j, 9])
            endpoint_dists.append(float(d))

    # 5. w2a_endpoint_position_spread_mean_m
    s5_endpoint_spread_mean = float(np.mean(endpoint_dists))

    # 6. w2a_endpoint_position_spread_max_m
    s6_endpoint_spread_max = float(np.max(endpoint_dists))

    # 7. w2a_position_variance_mean
    s7_pos_var_mean = float(np.mean(var_cand[:, :3]))

    # 8. w2a_rotation_variance_mean
    s8_rot_var_mean = float(np.mean(var_cand[:, 3:9]))

    # 9. w2a_gripper_variance_mean
    s9_grip_var_mean = float(np.mean(var_cand[:, 9]))

    scalars_9 = np.asarray(
        [
            s1_var_mean,
            s2_var_max,
            s3_pairwise_mse_mean,
            s4_cand0_vs_mean_mse,
            s5_endpoint_spread_mean,
            s6_endpoint_spread_max,
            s7_pos_var_mean,
            s8_rot_var_mean,
            s9_grip_var_mean,
        ],
        dtype=np.float32,
    )

    # Compute Horizon Features [10, 6]
    horizon_10x6 = np.zeros((HORIZON_STEPS, HORIZON_CHANNELS), dtype=np.float32)

    for h in range(HORIZON_STEPS):
        # 1. position_variance_mean[h]
        horizon_10x6[h, 0] = float(np.mean(var_cand[h, :3]))

        # 2. position_variance_max[h]
        horizon_10x6[h, 1] = float(np.max(var_cand[h, :3]))

        # 3. rotation_variance_mean[h]
        horizon_10x6[h, 2] = float(np.mean(var_cand[h, 3:9]))

        # 4. gripper_variance[h]
        horizon_10x6[h, 3] = float(var_cand[h, 9])

        # Cumulative position pairwise spread at horizon h
        h_dists = []
        for i in range(PRIMARY_CANDIDATES):
            for j in range(i + 1, PRIMARY_CANDIDATES):
                d = np.linalg.norm(P[i, h] - P[j, h])
                h_dists.append(float(d))

        # 5. cumulative_position_spread_mean[h]
        horizon_10x6[h, 4] = float(np.mean(h_dists))

        # 6. cumulative_position_spread_max[h]
        horizon_10x6[h, 5] = float(np.max(h_dists))

    return scalars_9, horizon_10x6


def compute_temporal_scalars(
    decision_index: int,
    current_action_var_mean: float,
    current_endpoint_spread_mean: float,
    prev_action_var_mean: float | None,
    prev_endpoint_spread_mean: float | None,
) -> np.ndarray:
    """
    Compute 3 temporal change scalars:
    1. history_available: 0 if q=0 else 1
    2. abs_delta_action_variance_mean: 0 if q=0 else abs(curr - prev)
    3. abs_delta_endpoint_spread_mean: 0 if q=0 else abs(curr - prev)
    """
    if decision_index == 0 or prev_action_var_mean is None or prev_endpoint_spread_mean is None:
        return np.array([0.0, 0.0, 0.0], dtype=np.float32)

    hist_avail = 1.0
    d_var = float(abs(current_action_var_mean - prev_action_var_mean))
    d_spread = float(abs(current_endpoint_spread_mean - prev_endpoint_spread_mean))

    return np.array([hist_avail, d_var, d_spread], dtype=np.float32)


def assemble_scalar37(
    disagreement_9: np.ndarray,
    c0_dynamics_25: np.ndarray,
    temporal_3: np.ndarray,
) -> np.ndarray:
    """Assemble exactly 37 current-query scalars: 9 disagreement + 25 c0 dynamics + 3 temporal."""
    vec = np.concatenate([disagreement_9, c0_dynamics_25, temporal_3], axis=0).astype(np.float32)
    if vec.shape != (37,):
        raise RuntimeError(f"Expected scalar37 shape (37,), got {vec.shape}")
    return vec
