"""Mimic/W2A Single-Head K1-without-ACE feature extraction for SimVLA H10."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple
import numpy as np


def compute_denoising_metrics(
    x_candidates_7d: np.ndarray,
    v_candidates_7d: np.ndarray,
) -> Dict[str, float]:
    """Compute the five required genuine denoising metrics at step d.

    Args:
        x_candidates_7d: Pre-update normalized flow state tensor [8, 10, 7].
        v_candidates_7d: Evaluated velocity/vector-field tensor [8, 10, 7].

    Returns:
        Dictionary with exactly the five frozen metric keys.
    """
    x = np.asarray(x_candidates_7d, dtype=np.float64)
    v = np.asarray(v_candidates_7d, dtype=np.float64)

    if x.shape != (8, 10, 7) or v.shape != (8, 10, 7):
        raise ValueError(
            f"Expected shape (8, 10, 7) for x and v, got x={x.shape}, v={v.shape}"
        )

    # 1 & 2: Variance across candidate axis (ddof=0)
    var_x = np.var(x, axis=0, ddof=0)  # [10, 7]
    sample_variance_mean = float(np.mean(var_x))
    sample_variance_max = float(np.max(var_x))

    # Pairwise unordered pairs strictly excluding diagonal self-pairs (i < j -> 28 pairs)
    num_candidates = x.shape[0]
    x_pairs_mse: List[float] = []
    v_pairs_mse: List[float] = []

    for i in range(num_candidates):
        for j in range(i + 1, num_candidates):
            x_pairs_mse.append(float(np.mean((x[i] - x[j]) ** 2)))
            v_pairs_mse.append(float(np.mean((v[i] - v[j]) ** 2)))

    sample_pairwise_mse_mean = float(np.mean(x_pairs_mse))
    sample_velocity_mse_mean = float(np.mean(v_pairs_mse))

    # Vector field L2 mean: average across candidates (8) and horizon (10) of L2 norm over 7 dims
    v_l2 = np.linalg.norm(v, axis=-1)  # [8, 10]
    vector_field_l2_mean = float(np.mean(v_l2))

    return {
        "sample_pairwise_mse_mean": sample_pairwise_mse_mean,
        "sample_variance_max": sample_variance_max,
        "sample_variance_mean": sample_variance_mean,
        "sample_velocity_mse_mean": sample_velocity_mse_mean,
        "vector_field_l2_mean": vector_field_l2_mean,
    }


def reduce_denoising_traces(
    step_metrics: List[Dict[str, float]],
    expected_steps: int = 10,
) -> np.ndarray:
    """Reduce D denoising step metric dicts into a 25-dimensional feature vector.

    For each of the 5 traces in frozen order, compute:
    [first, last, mean, max, last - first].
    """
    if len(step_metrics) != expected_steps:
        raise ValueError(
            f"Expected {expected_steps} denoising records, got {len(step_metrics)}"
        )

    trace_keys = [
        "sample_pairwise_mse_mean",
        "sample_variance_max",
        "sample_variance_mean",
        "sample_velocity_mse_mean",
        "vector_field_l2_mean",
    ]

    reduced: List[float] = []
    for key in trace_keys:
        trace = np.array([float(m[key]) for m in step_metrics], dtype=np.float64)
        first_val = float(trace[0])
        last_val = float(trace[-1])
        mean_val = float(np.mean(trace))
        max_val = float(np.max(trace))
        diff_val = last_val - first_val
        reduced.extend([first_val, last_val, mean_val, max_val, diff_val])

    return np.array(reduced, dtype=np.float32)


def compute_candidate_disagreement_scalars(
    action_candidates_10d: np.ndarray,
) -> np.ndarray:
    """Compute the 9 candidate disagreement scalars from action_candidates [8, 10, 10]."""
    c10 = np.asarray(action_candidates_10d, dtype=np.float64)
    if c10.shape != (8, 10, 10):
        raise ValueError(f"Expected shape (8, 10, 10), got {c10.shape}")

    num_candidates = c10.shape[0]

    # 1. w2a_action_variance_mean
    act_var = np.var(c10, axis=0, ddof=0)  # [10, 10]
    w2a_action_variance_mean = float(np.mean(act_var))

    # 2. w2a_action_variance_max
    w2a_action_variance_max = float(np.max(act_var))

    # 3. w2a_pairwise_mse_mean
    pair_mses: List[float] = []
    for i in range(num_candidates):
        for j in range(i + 1, num_candidates):
            pair_mses.append(float(np.mean((c10[i] - c10[j]) ** 2)))
    w2a_pairwise_mse_mean = float(np.mean(pair_mses))

    # 4. w2a_first_candidate_vs_mean_mse
    mean_cand = np.mean(c10, axis=0)  # [10, 10]
    w2a_first_candidate_vs_mean_mse = float(np.mean((c10[0] - mean_cand) ** 2))

    # Endpoint position spread
    cum_pos = np.cumsum(c10[:, :, :3], axis=1)  # [8, 10, 3]
    endpoint_pos = cum_pos[:, -1, :]  # [8, 3]
    endpoint_dists: List[float] = []
    for i in range(num_candidates):
        for j in range(i + 1, num_candidates):
            endpoint_dists.append(float(np.linalg.norm(endpoint_pos[i] - endpoint_pos[j])))

    # 5. w2a_endpoint_position_spread_mean_m
    w2a_endpoint_position_spread_mean_m = float(np.mean(endpoint_dists))

    # 6. w2a_endpoint_position_spread_max_m
    w2a_endpoint_position_spread_max_m = float(np.max(endpoint_dists))

    # 7. w2a_position_variance_mean
    w2a_position_variance_mean = float(np.mean(np.var(c10[:, :, :3], axis=0, ddof=0)))

    # 8. w2a_rotation_variance_mean
    w2a_rotation_variance_mean = float(np.mean(np.var(c10[:, :, 3:9], axis=0, ddof=0)))

    # 9. w2a_gripper_variance_mean
    w2a_gripper_variance_mean = float(np.mean(np.var(c10[:, :, 9:10], axis=0, ddof=0)))

    return np.array(
        [
            w2a_action_variance_mean,
            w2a_action_variance_max,
            w2a_pairwise_mse_mean,
            w2a_first_candidate_vs_mean_mse,
            w2a_endpoint_position_spread_mean_m,
            w2a_endpoint_position_spread_max_m,
            w2a_position_variance_mean,
            w2a_rotation_variance_mean,
            w2a_gripper_variance_mean,
        ],
        dtype=np.float32,
    )


def compute_temporal_change_scalars(
    curr_disagreement_9: np.ndarray,
    previous_state: Optional[Dict[str, float]] = None,
) -> Tuple[np.ndarray, Dict[str, float]]:
    """Compute 3 temporal-change scalars: history_available, d_action_var, d_endpoint_spread."""
    curr_var_mean = float(curr_disagreement_9[0])
    curr_spread_mean = float(curr_disagreement_9[4])

    new_state = {
        "w2a_action_variance_mean": curr_var_mean,
        "w2a_endpoint_position_spread_mean_m": curr_spread_mean,
    }

    if previous_state is None:
        temporal_3 = np.array([0.0, 0.0, 0.0], dtype=np.float32)
    else:
        d_var = abs(curr_var_mean - float(previous_state["w2a_action_variance_mean"]))
        d_spread = abs(curr_spread_mean - float(previous_state["w2a_endpoint_position_spread_mean_m"]))
        temporal_3 = np.array([1.0, d_var, d_spread], dtype=np.float32)

    return temporal_3, new_state


def compute_horizon_features(
    action_candidates_10d: np.ndarray,
) -> np.ndarray:
    """Compute the [10, 6] horizon feature tensor from action_candidates [8, 10, 10]."""
    c10 = np.asarray(action_candidates_10d, dtype=np.float64)
    if c10.shape != (8, 10, 10):
        raise ValueError(f"Expected shape (8, 10, 10), got {c10.shape}")

    num_candidates, horizon, _ = c10.shape
    horizon_features = np.zeros((horizon, 6), dtype=np.float32)

    for t in range(horizon):
        trans_t = c10[:, t, :3]  # [8, 3]
        rot_t = c10[:, t, 3:9]  # [8, 6]
        grip_t = c10[:, t, 9]  # [8]

        pos_var_t = np.var(trans_t, axis=0, ddof=0)  # [3]
        rot_var_t = np.var(rot_t, axis=0, ddof=0)  # [6]
        grip_var_t = float(np.var(grip_t, ddof=0))  # scalar

        cum_pos_t = np.sum(c10[:, : t + 1, :3], axis=1)  # [8, 3]
        pair_dists_t: List[float] = []
        for i in range(num_candidates):
            for j in range(i + 1, num_candidates):
                pair_dists_t.append(float(np.linalg.norm(cum_pos_t[i] - cum_pos_t[j])))

        horizon_features[t, 0] = float(np.mean(pos_var_t))
        horizon_features[t, 1] = float(np.max(pos_var_t))
        horizon_features[t, 2] = float(np.mean(rot_var_t))
        horizon_features[t, 3] = grip_var_t
        horizon_features[t, 4] = float(np.mean(pair_dists_t))
        horizon_features[t, 5] = float(np.max(pair_dists_t))

    return horizon_features


def extract_query_features(
    action_candidates_10d: np.ndarray,
    denoising_step_metrics: List[Dict[str, float]],
    previous_query_state: Optional[Dict[str, float]] = None,
) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
    """Extract exactly 37 scalar features and [10, 6] horizon features for one query."""
    scalars_9 = compute_candidate_disagreement_scalars(action_candidates_10d)
    scalars_25 = reduce_denoising_traces(denoising_step_metrics, expected_steps=10)
    scalars_3, new_state = compute_temporal_change_scalars(scalars_9, previous_query_state)

    scalars_37 = np.concatenate([scalars_9, scalars_25, scalars_3], axis=0).astype(np.float32)
    horizon_10x6 = compute_horizon_features(action_candidates_10d).astype(np.float32)

    return scalars_37, horizon_10x6, new_state
