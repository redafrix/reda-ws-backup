"""Trusted 49D uncertainty feature construction."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .constants import (
    ACTION_DIM,
    ACTION_HORIZON,
    PROPRIO_DIM,
    TOTAL_CANDIDATES,
    UNCERTAINTY_49D_KEYS,
)


@dataclass(frozen=True)
class DenoisingTrace:
    path_variance: np.ndarray
    last_step_variance: np.ndarray
    denoise_mean_trace: np.ndarray
    velocity_norm_trace: np.ndarray
    update_norm_trace: np.ndarray
    update_vector_trace: np.ndarray
    initial_noise: np.ndarray
    final_action_normalized: np.ndarray

    def validate(self) -> None:
        for name in (
            "path_variance",
            "last_step_variance",
            "initial_noise",
            "final_action_normalized",
        ):
            value = np.asarray(getattr(self, name))
            if value.shape != (ACTION_HORIZON, ACTION_DIM):
                raise ValueError(f"{name}: expected (10, 7), got {value.shape}")
            if not np.isfinite(value).all():
                raise ValueError(f"{name} contains nonfinite values")
        for name in (
            "denoise_mean_trace",
            "velocity_norm_trace",
            "update_norm_trace",
        ):
            value = np.asarray(getattr(self, name))
            if value.ndim != 1 or value.size == 0 or not np.isfinite(value).all():
                raise ValueError(f"invalid {name}")
        update_vectors = np.asarray(self.update_vector_trace)
        if (
            update_vectors.ndim != 2
            or update_vectors.shape[0] != self.update_norm_trace.size
            or not np.isfinite(update_vectors).all()
        ):
            raise ValueError("invalid update_vector_trace")

    def raw_payload(self) -> dict[str, Any]:
        self.validate()
        return {
            "path_variance": np.asarray(self.path_variance).tolist(),
            "last_step_variance": np.asarray(self.last_step_variance).tolist(),
            "denoise_mean_trace": np.asarray(self.denoise_mean_trace).tolist(),
            "velocity_norm_trace": np.asarray(self.velocity_norm_trace).tolist(),
            "update_norm_trace": np.asarray(self.update_norm_trace).tolist(),
            "update_vector_trace": np.asarray(self.update_vector_trace).tolist(),
            "initial_noise": np.asarray(self.initial_noise).tolist(),
            "final_action_normalized": np.asarray(
                self.final_action_normalized
            ).tolist(),
        }


def _slope(values: np.ndarray) -> float:
    if values.size <= 1:
        return 0.0
    x = np.arange(values.size, dtype=np.float64)
    x -= x.mean()
    y = values.astype(np.float64) - float(values.mean())
    return float(np.dot(x, y) / max(float(np.dot(x, x)), 1e-12))


def build_uncertainty_49d(
    *,
    main_trace: DenoisingTrace,
    all_candidate_chunks_env: np.ndarray,
    proprio: np.ndarray,
    state_mean: np.ndarray,
    state_std: np.ndarray,
    previous_executed_action: np.ndarray | None,
    previous_proprio: np.ndarray | None,
) -> tuple[np.ndarray, dict[str, float]]:
    """Build the trusted vector for candidate zero using all nine for spread."""
    main_trace.validate()
    chunks = np.asarray(all_candidate_chunks_env, dtype=np.float32)
    if chunks.shape != (TOTAL_CANDIDATES, ACTION_HORIZON, ACTION_DIM):
        raise ValueError(f"invalid candidate chunk shape: {chunks.shape}")
    if not np.isfinite(chunks).all():
        raise ValueError("candidate chunks contain nonfinite values")

    state = np.asarray(proprio, dtype=np.float32)
    mean = np.asarray(state_mean, dtype=np.float64)
    std = np.asarray(state_std, dtype=np.float64)
    if state.shape != (PROPRIO_DIM,) or mean.shape != (PROPRIO_DIM,) or std.shape != (
        PROPRIO_DIM,
    ):
        raise ValueError("state and normalization must have shape (8,)")
    z = (state.astype(np.float64) - mean) / np.maximum(std, 1e-6)

    path = np.asarray(main_trace.path_variance, dtype=np.float64)
    last = np.asarray(main_trace.last_step_variance, dtype=np.float64)
    denoise = np.asarray(main_trace.denoise_mean_trace, dtype=np.float64)
    velocity = np.asarray(main_trace.velocity_norm_trace, dtype=np.float64)
    update = np.asarray(main_trace.update_norm_trace, dtype=np.float64)
    update_vectors = np.asarray(main_trace.update_vector_trace, dtype=np.float64)
    final_norm = np.asarray(main_trace.final_action_normalized, dtype=np.float64)
    initial_noise = np.asarray(main_trace.initial_noise, dtype=np.float64)

    sample_var = chunks.var(axis=0)
    sample_mean = chunks.mean(axis=0, keepdims=True)
    sample_l2 = np.linalg.norm(chunks - sample_mean, axis=-1)
    action = chunks[0, 0]
    plan_delta = np.diff(chunks[0], axis=0)
    plan_delta_norms = np.linalg.norm(plan_delta, axis=-1)

    if previous_executed_action is None:
        action_delta = np.zeros(ACTION_DIM, dtype=np.float32)
    else:
        action_delta = action - np.asarray(
            previous_executed_action, dtype=np.float32
        )
    if previous_proprio is None:
        state_delta = np.zeros(PROPRIO_DIM, dtype=np.float32)
    else:
        state_delta = state - np.asarray(previous_proprio, dtype=np.float32)

    update_diff = np.diff(update)
    vector_diff = np.diff(update_vectors, axis=0)
    if update_vectors.shape[0] > 1:
        a = update_vectors[1:]
        b = update_vectors[:-1]
        denom = np.maximum(np.linalg.norm(a, axis=1) * np.linalg.norm(b, axis=1), 1e-12)
        direction_flip = 1.0 - np.sum(a * b, axis=1) / denom
    else:
        direction_flip = np.zeros(1, dtype=np.float64)

    rotation = last[:, 3:6]
    feature_map = {
        "path_step_mean": float(path.mean(axis=-1)[0]),
        "last_step_mean": float(last.mean(axis=-1)[0]),
        "mean_path_var": float(path.mean()),
        "mean_last_var": float(last.mean()),
        "max_path_var": float(path.max()),
        "max_last_var": float(last.max()),
        "denoise_initial_mean": float(denoise[0]),
        "denoise_final_mean": float(denoise[-1]),
        "denoise_delta": float(denoise[0] - denoise[-1]),
        "denoise_slope": _slope(denoise),
        "denoise_final_max": float(last.max()),
        "denoise_spike": float(np.maximum(np.diff(denoise), 0.0).max())
        if denoise.size > 1
        else 0.0,
        "denoise_final_gripper": float(last[:, -1].mean()),
        "denoise_final_rotation_mean": float(rotation.mean()),
        "denoise_velocity_norm_mean": float(velocity.mean()),
        "denoise_velocity_norm_max": float(velocity.max()),
        "denoise_update_norm_mean": float(update.mean()),
        "denoise_update_norm_max": float(update.max()),
        "denoise_update_norm_final": float(update[-1]),
        "denoise_update_spike": float(np.maximum(update_diff, 0.0).max())
        if update_diff.size
        else 0.0,
        "denoise_update_oscillation_mean": float(
            np.linalg.norm(vector_diff, axis=1).mean()
        )
        if vector_diff.size
        else 0.0,
        "denoise_update_direction_flip_mean": float(direction_flip.mean()),
        "denoise_final_initial_action_l2": float(
            np.linalg.norm(final_norm - initial_noise)
        ),
        "sample_action_var_mean": float(sample_var.mean()),
        "sample_action_var_max": float(sample_var.max()),
        "sample_action_l2_mean": float(sample_l2.mean()),
        "sample_action_l2_max": float(sample_l2.max()),
        "sample_action_translation_var": float(sample_var[..., :3].mean()),
        "sample_action_rotation_var": float(sample_var[..., 3:6].mean()),
        "sample_action_gripper_var": float(sample_var[..., -1].mean()),
        "action_norm": float(np.linalg.norm(action)),
        "action_max_abs": float(np.abs(action).max()),
        "action_translation_norm": float(np.linalg.norm(action[:3])),
        "action_rotation_norm": float(np.linalg.norm(action[3:6])),
        "action_gripper_abs": float(abs(action[-1])),
        "action_delta_prev_norm": float(np.linalg.norm(action_delta)),
        "action_delta_prev_max_abs": float(np.abs(action_delta).max()),
        "plan_drift_l2": float(np.linalg.norm(chunks[0, -1] - chunks[0, 0])),
        "plan_drift_mean_l2": float(plan_delta_norms.mean()),
        "plan_drift_max_l2": float(plan_delta_norms.max()),
        "state_mahalanobis": float(np.linalg.norm(z)),
        "state_mahalanobis_eef": float(np.linalg.norm(z[:3])),
        "state_mahalanobis_rotation": float(np.linalg.norm(z[3:6])),
        "state_mahalanobis_gripper": float(np.linalg.norm(z[6:8])),
        "state_eef_norm": float(np.linalg.norm(state[:3])),
        "state_rotation_norm": float(np.linalg.norm(state[3:6])),
        "state_gripper_norm": float(np.linalg.norm(state[6:8])),
        "state_gripper_width": float(abs(state[7] - state[6])),
        "state_delta_prev_norm": float(np.linalg.norm(state_delta)),
    }
    missing = set(UNCERTAINTY_49D_KEYS) - feature_map.keys()
    if missing:
        raise RuntimeError(f"missing uncertainty features: {sorted(missing)}")
    vector = np.asarray(
        [feature_map[key] for key in UNCERTAINTY_49D_KEYS], dtype=np.float32
    )
    if vector.shape != (49,) or not np.isfinite(vector).all():
        raise RuntimeError("49D uncertainty vector is invalid")
    return vector, feature_map
