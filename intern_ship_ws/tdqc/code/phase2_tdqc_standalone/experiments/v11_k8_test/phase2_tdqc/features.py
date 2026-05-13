from __future__ import annotations

import math
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence

import numpy as np

try:
    import torch
except ImportError:  # pragma: no cover - torch is required for training, not for JSON parsing
    torch = None


DEFAULT_TRACE_FEATURE_KEYS: tuple[str, ...] = (
    "path_step_mean",
    "last_step_mean",
    "mean_path_var",
    "mean_last_var",
    "max_path_var",
    "max_last_var",
)

DENOISE_TRACE_FEATURE_KEYS: tuple[str, ...] = (
    "denoise_initial_mean",
    "denoise_final_mean",
    "denoise_delta",
    "denoise_slope",
    "denoise_final_max",
    "denoise_spike",
    "denoise_final_gripper",
    "denoise_final_rotation_mean",
    "denoise_velocity_norm_mean",
    "denoise_velocity_norm_max",
    "denoise_update_norm_mean",
    "denoise_update_norm_max",
    "denoise_update_norm_final",
    "denoise_update_spike",
    "denoise_update_oscillation_mean",
    "denoise_update_direction_flip_mean",
    "denoise_final_initial_action_l2",
)

ACTION_TRACE_FEATURE_KEYS: tuple[str, ...] = (
    "sample_action_var_mean",
    "sample_action_var_max",
    "sample_action_l2_mean",
    "sample_action_l2_max",
    "sample_action_translation_var",
    "sample_action_rotation_var",
    "sample_action_gripper_var",
    "action_norm",
    "action_max_abs",
    "action_translation_norm",
    "action_rotation_norm",
    "action_gripper_abs",
    "action_delta_prev_norm",
    "action_delta_prev_max_abs",
    "plan_drift_l2",
    "plan_drift_mean_l2",
    "plan_drift_max_l2",
)

STATE_TRACE_FEATURE_KEYS: tuple[str, ...] = (
    "state_mahalanobis",
    "state_mahalanobis_eef",
    "state_mahalanobis_rotation",
    "state_mahalanobis_gripper",
    "state_eef_norm",
    "state_rotation_norm",
    "state_gripper_norm",
    "state_gripper_width",
    "state_delta_prev_norm",
)

SUMMARY_DENOISE_TRACE_FEATURE_KEYS: tuple[str, ...] = (
    *DEFAULT_TRACE_FEATURE_KEYS,
    *DENOISE_TRACE_FEATURE_KEYS,
    *ACTION_TRACE_FEATURE_KEYS,
    *STATE_TRACE_FEATURE_KEYS,
)


def raw_trace_feature_keys(action_dim: int = 7, *, include_summaries: bool = False) -> list[str]:
    keys: list[str] = []
    if include_summaries:
        keys.extend(DEFAULT_TRACE_FEATURE_KEYS)
    keys.extend([f"path_var_{i}" for i in range(action_dim)])
    keys.extend([f"last_var_{i}" for i in range(action_dim)])
    return keys


def compact8_trace_feature_keys() -> list[str]:
    return [
        "weighted_path_mean",
        "weighted_last_mean",
        "first_path_mean",
        "first_last_mean",
        "max_path",
        "max_last",
        "gripper_path",
        "gripper_last",
    ]


def _safe_float(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    try:
        out = float(value)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(out):
        return default
    return out


def trace_step_to_features(
    step: Mapping[str, Any],
    feature_keys: Sequence[str] = DEFAULT_TRACE_FEATURE_KEYS,
    *,
    log1p: bool = True,
) -> np.ndarray:
    """Convert one uncertainty_trace item into a small TDQC feature vector.

    The current LIBERO evaluator already logs these scalar summaries per executed
    environment step. They are in normalized action/variance units, which is fine
    because the calibrator is trained and evaluated on the same convention.
    """
    values: List[float] = []
    for key in feature_keys:
        v = _safe_float(step.get(key), default=0.0)
        # Variance summaries should be non-negative. Clamp tiny numeric negatives.
        if v < 0.0:
            v = 0.0
        if log1p:
            v = math.log1p(v)
        values.append(v)
    return np.asarray(values, dtype=np.float32)


def trace_step_to_summary_denoise_features(
    step: Mapping[str, Any],
    *,
    log1p: bool = True,
) -> np.ndarray:
    return trace_step_to_features(step, SUMMARY_DENOISE_TRACE_FEATURE_KEYS, log1p=log1p)


def _raw_variance_vector(step: Mapping[str, Any], key: str, action_dim: int) -> np.ndarray:
    value = step.get(key)
    if value is None:
        return np.zeros(action_dim, dtype=np.float32)
    arr = np.asarray(value, dtype=np.float32)
    if arr.ndim == 0:
        return np.full(action_dim, float(arr), dtype=np.float32)
    if arr.ndim >= 2:
        plan_idx = int(step.get("plan_step_idx", 0) or 0)
        plan_idx = max(0, min(plan_idx, arr.shape[0] - 1))
        arr = arr[plan_idx]
    arr = np.ravel(arr).astype(np.float32)
    if arr.shape[0] >= action_dim:
        return arr[:action_dim]
    out = np.zeros(action_dim, dtype=np.float32)
    out[: arr.shape[0]] = arr
    return out


def trace_step_to_raw_features(
    step: Mapping[str, Any],
    *,
    action_dim: int = 7,
    include_summaries: bool = False,
    log1p: bool = True,
) -> np.ndarray:
    """Convert one uncertainty step into raw per-action variance features.

    Expected raw keys are `path_variance` and `last_step_variance`. Each may be
    either a per-action vector `[D]` or a full plan tensor `[H, D]`; in the latter
    case `plan_step_idx` selects the executed action row.
    """
    values: List[np.ndarray] = []
    if include_summaries:
        values.append(trace_step_to_features(step, DEFAULT_TRACE_FEATURE_KEYS, log1p=log1p))
    path = np.clip(_raw_variance_vector(step, "path_variance", action_dim), 0.0, None)
    last = np.clip(_raw_variance_vector(step, "last_step_variance", action_dim), 0.0, None)
    raw = np.concatenate([path, last], axis=0).astype(np.float32)
    if log1p:
        raw = np.log1p(raw).astype(np.float32)
    values.append(raw)
    return np.concatenate(values, axis=0).astype(np.float32)


def trace_step_to_compact8_features(
    step: Mapping[str, Any],
    *,
    log1p: bool = True,
) -> np.ndarray:
    """Compact 8D feature vector matching the standalone TDQC recipe.

    Our JSONL stores per-executed-step variance vectors, not the full replanning
    horizon tensor used by the standalone collector. The closest compatible
    mapping uses the logged horizon summaries plus the gripper dimension.
    """
    path = _raw_variance_vector(step, "path_variance", action_dim=7)
    last = _raw_variance_vector(step, "last_step_variance", action_dim=7)
    values = np.asarray(
        [
            _safe_float(step.get("mean_path_var")),
            _safe_float(step.get("mean_last_var")),
            _safe_float(step.get("path_step_mean")),
            _safe_float(step.get("last_step_mean")),
            _safe_float(step.get("max_path_var")),
            _safe_float(step.get("max_last_var")),
            float(max(path[-1], 0.0)) if path.size else 0.0,
            float(max(last[-1], 0.0)) if last.size else 0.0,
        ],
        dtype=np.float32,
    )
    values = np.clip(values, 0.0, None)
    return np.log1p(values).astype(np.float32) if log1p else values


def record_to_episode(
    record: Mapping[str, Any],
    feature_keys: Sequence[str] = DEFAULT_TRACE_FEATURE_KEYS,
    *,
    log1p: bool = True,
    min_steps: int = 2,
    feature_mode: str = "summary",
    raw_action_dim: int = 7,
) -> Optional[Dict[str, Any]]:
    """Convert one JSONL rollout record into a TDQC episode dictionary.

    Expected source format is the JSONL produced by evaluation/libero/libero_client.py:
    each record contains `success: bool` and `uncertainty_trace: list[dict]`.
    """
    trace = record.get("uncertainty_trace") or []
    rows: List[np.ndarray] = []
    for item in trace:
        if not isinstance(item, Mapping):
            continue
        if feature_mode == "summary":
            rows.append(trace_step_to_features(item, feature_keys, log1p=log1p))
        elif feature_mode == "summary_denoise":
            rows.append(trace_step_to_summary_denoise_features(item, log1p=log1p))
        elif feature_mode == "raw":
            rows.append(
                trace_step_to_raw_features(
                    item,
                    action_dim=raw_action_dim,
                    include_summaries=False,
                    log1p=log1p,
                )
            )
        elif feature_mode == "raw_plus_summary":
            rows.append(
                trace_step_to_raw_features(
                    item,
                    action_dim=raw_action_dim,
                    include_summaries=True,
                    log1p=log1p,
                )
            )
        elif feature_mode == "compact8":
            rows.append(trace_step_to_compact8_features(item, log1p=log1p))
        else:
            raise ValueError(f"Unknown feature_mode: {feature_mode}")

    if len(rows) < min_steps:
        return None

    features = np.stack(rows, axis=0).astype(np.float32)
    success = int(bool(record.get("success", False)))
    if feature_mode == "summary":
        episode_feature_keys = list(feature_keys)
    elif feature_mode == "summary_denoise":
        episode_feature_keys = list(SUMMARY_DENOISE_TRACE_FEATURE_KEYS)
    elif feature_mode == "compact8":
        episode_feature_keys = compact8_trace_feature_keys()
    else:
        episode_feature_keys = raw_trace_feature_keys(raw_action_dim, include_summaries=feature_mode == "raw_plus_summary")
    episode = {
        "features": features,
        "success": success,
        "failure": 1 - success,
        "task_suite": record.get("task_suite"),
        "task_id": record.get("task_id"),
        "episode": record.get("episode"),
        "task_description": record.get("task_description"),
        "steps": record.get("steps"),
        "feature_keys": episode_feature_keys,
        "feature_mode": feature_mode,
        "raw_action_dim": raw_action_dim if feature_mode in ("raw", "raw_plus_summary") else None,
    }
    return episode


def aggregate_variance_tensors(
    path_variance: "torch.Tensor",
    last_step_variance: "torch.Tensor",
    *,
    lambda_decay: float = 0.8,
    log1p: bool = True,
) -> "torch.Tensor":
    """Aggregate raw [H, D] variance tensors into the Phase-2 feature vector.

    This is for future online/direct collection if you call
    `generate_actions_with_uncertainty(...)` inside Python rather than reading the
    evaluator JSONL. The JSONL path already contains equivalent summaries.
    """
    if torch is None:
        raise ImportError("aggregate_variance_tensors requires torch")
    if path_variance.ndim != 2 or last_step_variance.ndim != 2:
        raise ValueError(
            f"Expected [H, D] tensors, got {tuple(path_variance.shape)} and {tuple(last_step_variance.shape)}"
        )
    if path_variance.shape != last_step_variance.shape:
        raise ValueError("path_variance and last_step_variance must have the same shape")
    if not (0.0 < lambda_decay <= 1.0):
        raise ValueError("lambda_decay must be in (0, 1]")

    H, D = path_variance.shape
    weights = lambda_decay ** torch.arange(H, device=path_variance.device, dtype=path_variance.dtype)
    weights = weights.view(H, 1)
    z = weights.sum() * D

    path_step_mean = path_variance.mean(dim=-1)[0]
    last_step_mean = last_step_variance.mean(dim=-1)[0]
    weighted_path = (weights * path_variance).sum() / z
    weighted_last = (weights * last_step_variance).sum() / z
    max_path = path_variance.max()
    max_last = last_step_variance.max()

    phi = torch.stack([
        path_step_mean,
        last_step_mean,
        weighted_path,
        weighted_last,
        max_path,
        max_last,
    ])
    phi = torch.clamp(phi, min=0.0)
    return torch.log1p(phi) if log1p else phi
