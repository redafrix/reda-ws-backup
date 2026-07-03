#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import sys
import time
import traceback
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


DEAN_ROOT = Path("/home/dean/fiper_uncertainty_collection")
COLLECTOR_DIR = DEAN_ROOT / "src/data_collection_stage9"
_SCRIPT_DIR = str(Path(__file__).resolve().parent)
if _SCRIPT_DIR not in sys.path:
    sys.path.insert(0, _SCRIPT_DIR)
if str(DEAN_ROOT) not in sys.path:
    sys.path.insert(0, str(DEAN_ROOT))
if str(COLLECTOR_DIR) not in sys.path:
    sys.path.insert(0, str(COLLECTOR_DIR))

from collect_fiper_uncertainty_receding_dean_v1 import (  # noqa: E402
    DEAN_CKPT_60K,
    DEAN_LIBERO_PRO_ROOT,
    DEAN_NORM_STATS,
    DEAN_SIMVLA_ROOT,
    DEAN_SMOLVLM_CACHE,
    UNCERTAINTY_49D_KEYS,
    ImagePreprocessor,
    check_success,
    load_state_stats,
    make_env,
    obs_images,
    obs_to_proprio,
    quat2axisangle,
    reset_to_init,
    setup_runtime,
    sha256_file,
)


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def json_sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): json_sanitize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_sanitize(v) for v in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if torch.is_tensor(value):
        return value.detach().cpu().tolist()
    if isinstance(value, Path):
        return str(value)
    return value


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(json_sanitize(payload), indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(json_sanitize(row), sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def set_all_seeds(seed: int) -> None:
    seed = int(seed) % (2**31 - 1)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def deterministic_action_seed(global_action_seed: int, reset_seed: int, episode_index: int, timestep: int, sample_index: int) -> int:
    key = f"{global_action_seed}|{reset_seed}|{episode_index}|{timestep}|{sample_index}".encode("utf-8")
    return int(hashlib.sha256(key).hexdigest()[:16], 16) % (2**31 - 1)


def action_seeds_for_step(global_action_seed: int, reset_seed: int, episode_index: int, timestep: int, n: int) -> list[int]:
    seeds = [deterministic_action_seed(global_action_seed, reset_seed, episode_index, timestep, i) for i in range(n)]
    if len(set(seeds)) != len(seeds):
        raise RuntimeError(f"duplicate action seeds at episode={episode_index} timestep={timestep}: {seeds}")
    return seeds


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


def standardize_last_dim(x: np.ndarray, stats: dict[str, np.ndarray]) -> np.ndarray:
    mean = np.asarray(stats["mean"], dtype=np.float32)
    std = np.maximum(np.asarray(stats["std"], dtype=np.float32), 1e-6)
    return ((x.astype(np.float32) - mean) / std).astype(np.float32)


class SeqRiskModel(nn.Module):
    def __init__(
        self,
        hist_dim: int,
        action_dim: int,
        static_dim: int,
        width: int = 128,
        layers: int = 3,
        heads: int = 4,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.hist_proj = nn.Linear(hist_dim, width)
        self.action_proj = nn.Linear(action_dim, width)
        enc_layer = nn.TransformerEncoderLayer(
            width,
            heads,
            width * 4,
            dropout=dropout,
            batch_first=True,
            activation="gelu",
        )
        self.cls = nn.Parameter(torch.zeros(1, 1, width))
        self.pos = nn.Parameter(torch.randn(1, 64, width) * 0.02)
        self.seq = nn.TransformerEncoder(enc_layer, layers)
        self.static_in_dropout = nn.Dropout(0.0)
        self.static = nn.Sequential(nn.Linear(static_dim, width), nn.GELU())
        self.head = nn.Sequential(
            nn.LayerNorm(width * 2),
            nn.Linear(width * 2, width),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(width, 1),
        )

    def forward(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        tokens = torch.cat([self.hist_proj(batch["history"]), self.action_proj(batch["action"])], dim=1)
        bsz = tokens.shape[0]
        tokens = torch.cat([self.cls.expand(bsz, -1, -1), tokens], dim=1)
        seq = self.seq(tokens + self.pos[:, : tokens.shape[1]])[:, 0]
        static = self.static(self.static_in_dropout(batch["static"]))
        return self.head(torch.cat([seq, static], dim=-1)).squeeze(-1)


@dataclass
class RiskDetector:
    name: str
    model_dir: Path
    model: SeqRiskModel
    stats: dict[str, dict[str, np.ndarray]]
    thresholds: dict[str, float]
    selected_uncertainty_dims: list[int]
    static_dim: int


def load_detector(name: str, model_dir: Path, device: torch.device) -> RiskDetector:
    metrics = json.loads((model_dir / "metrics.json").read_text())
    thresholds = json.loads((model_dir / "thresholds.json").read_text())
    raw_stats = json.loads((model_dir / "normalization.json").read_text())
    stats = {
        key: {
            "mean": np.asarray(raw_stats[key]["mean"], dtype=np.float32),
            "std": np.asarray(raw_stats[key]["std"], dtype=np.float32),
        }
        for key in ["history", "action", "static"]
    }
    feature_audit = metrics.get("feature_audit", {})
    selected_dims = [int(x) for x in feature_audit.get("selected_uncertainty_dims", [])]
    hist_dim = int(stats["history"]["mean"].shape[-1])
    action_dim = int(stats["action"]["mean"].shape[-1])
    static_dim = int(stats["static"]["mean"].shape[-1])
    model = SeqRiskModel(hist_dim=hist_dim, action_dim=action_dim, static_dim=static_dim).to(device)
    state = torch.load(model_dir / "model.pt", map_location=device)
    model.load_state_dict(state)
    model.eval()
    return RiskDetector(
        name=name,
        model_dir=model_dir,
        model=model,
        stats=stats,
        thresholds={k: float(v) for k, v in thresholds.items()},
        selected_uncertainty_dims=selected_dims,
        static_dim=static_dim,
    )


@dataclass
class CandidateBatch:
    chunks_env: np.ndarray
    chunks_norm: np.ndarray
    features_49d: np.ndarray
    feature_maps: list[dict[str, float]]


def rebuild_features_from_maps(feature_maps: list[dict[str, float]]) -> np.ndarray:
    return np.asarray([[float(fmap.get(key, 0.0)) for key in UNCERTAINTY_49D_KEYS] for fmap in feature_maps], dtype=np.float32)


def combine_main_and_ace_batches(main: CandidateBatch, ace: CandidateBatch) -> CandidateBatch:
    """Keep the main action identical to SimVLA-only, then add ACE candidates.

    The SimVLA transformer is not guaranteed to produce bit-identical output
    for sample 0 when it is generated in a batch of 9 instead of alone. For a
    fair baseline-vs-risk comparison, the main chunk must be generated alone
    exactly as the baseline does. We then recompute group-level sample-spread
    uncertainty features over [main + ACE] so the risk feature schema remains
    compatible with training.
    """
    chunks_env = np.concatenate([main.chunks_env, ace.chunks_env], axis=0)
    chunks_norm = np.concatenate([main.chunks_norm, ace.chunks_norm], axis=0)
    feature_maps = [dict(x) for x in (main.feature_maps + ace.feature_maps)]

    sample_var = chunks_env.var(axis=0)
    sample_mean = chunks_env.mean(axis=0, keepdims=True)
    sample_l2 = np.linalg.norm(chunks_env - sample_mean, axis=-1)
    rotation_end_np = min(6, chunks_env.shape[-1])
    shared_updates = {
        "sample_action_var_mean": float(sample_var.mean()),
        "sample_action_var_max": float(sample_var.max()),
        "sample_action_l2_mean": float(sample_l2.mean()),
        "sample_action_l2_max": float(sample_l2.max()),
        "sample_action_translation_var": float(sample_var[..., :3].mean()),
        "sample_action_rotation_var": float(sample_var[..., 3:rotation_end_np].mean()) if rotation_end_np > 3 else 0.0,
        "sample_action_gripper_var": float(sample_var[..., -1].mean()),
    }
    for fmap in feature_maps:
        fmap.update(shared_updates)
    return CandidateBatch(
        chunks_env=chunks_env,
        chunks_norm=chunks_norm,
        features_49d=rebuild_features_from_maps(feature_maps),
        feature_maps=feature_maps,
    )


def tensor_scalar(value: torch.Tensor | float | int) -> float:
    if torch.is_tensor(value):
        return float(value.detach().cpu().reshape(-1)[0].item())
    return float(value)


def generate_candidates_with_uncertainty(
    model: Any,
    input_ids: torch.Tensor,
    image_input: torch.Tensor,
    image_mask: torch.Tensor,
    proprio: torch.Tensor,
    seeds: list[int],
    steps: int,
    previous_action: np.ndarray | None,
    previous_proprio: np.ndarray | None,
    state_mean: np.ndarray | None,
    state_std: np.ndarray | None,
) -> CandidateBatch:
    if not seeds:
        raise ValueError("at least one seed is required")
    if len(set(seeds)) != len(seeds):
        raise ValueError(f"duplicate action seeds in one timestep: {seeds}")

    with torch.inference_mode():
        enc = model.forward_vlm_efficient(image_input, image_mask, input_ids)
        device = proprio.device
        dtype = proprio.dtype
        dim_action = int(model.action_space.dim_action)
        num_actions = int(model.num_actions)
        num_samples = len(seeds)

        if hasattr(model.action_space, "normalize_state"):
            proprio_norm = model.action_space.normalize_state(proprio)
        elif hasattr(model.action_space, "normalize"):
            proprio_norm = model.action_space.normalize(proprio)
        else:
            proprio_norm = proprio

        noise = []
        for seed in seeds:
            generator = torch.Generator(device=device)
            generator.manual_seed(int(seed) % (2**31 - 1))
            noise.append(torch.randn((num_actions, dim_action), device=device, dtype=dtype, generator=generator))
        x_t = torch.stack(noise, dim=0)
        initial_noise = x_t.detach().clone()

        vlm_features = enc["vlm_features"].repeat_interleave(num_samples, dim=0)
        proprio_batch = proprio_norm.repeat_interleave(num_samples, dim=0)

        path_variance = torch.zeros_like(x_t)
        last_step_variance = torch.zeros_like(x_t)
        denoise_means = []
        velocity_norms = []
        update_norms = []
        update_vectors = []

        denoise_steps = max(1, int(steps))
        dt = -1.0 / denoise_steps
        t = 1.0
        while t > -dt / 2:
            t_tensor = torch.full((num_samples,), t, device=device, dtype=dtype)
            pred = model.transformer(
                vlm_features=vlm_features,
                action_with_noise=x_t,
                proprio=proprio_batch,
                t=t_tensor,
            )
            if getattr(model.config, "predict_uncertainty", False):
                v_t, logvar_t = pred
                var_t = F.softplus(logvar_t) + model.config.uncertainty_eps
                denoise_means.append(var_t.mean(dim=(1, 2)))
                last_step_variance = var_t
                path_variance = path_variance + (dt * dt) * var_t
            else:
                v_t = pred
            update = dt * v_t
            velocity_norms.append(v_t.norm(dim=-1).mean(dim=1))
            update_norms.append(update.norm(dim=-1).mean(dim=1))
            update_vectors.append(update.flatten(1))
            x_t = x_t + update
            t = t + dt

        chunks_norm_t = x_t.detach()
        chunks_env_t = model.action_space.postprocess(chunks_norm_t).detach()
        chunks_env = chunks_env_t.detach().cpu().numpy().astype(np.float32)
        chunks_norm = chunks_norm_t.detach().cpu().numpy().astype(np.float32)
        path_np = path_variance.detach().cpu().numpy()
        last_np = last_step_variance.detach().cpu().numpy()

        velocity_trace = torch.stack(velocity_norms, dim=1) if velocity_norms else None
        update_trace = torch.stack(update_norms, dim=1) if update_norms else None
        update_vec_trace = torch.stack(update_vectors, dim=1) if update_vectors else None
        denoise_mean_trace = torch.stack(denoise_means, dim=1) if denoise_means else None

    sample_var = chunks_env.var(axis=0)
    sample_mean = chunks_env.mean(axis=0, keepdims=True)
    sample_l2 = np.linalg.norm(chunks_env - sample_mean, axis=-1)
    rotation_end_np = min(6, chunks_env.shape[-1])

    state = proprio.detach().cpu().numpy().reshape(-1).astype(np.float32)
    if state_mean is not None and state_std is not None:
        std = np.maximum(state_std[: state.size].astype(np.float64), 1e-6)
        z = (state.astype(np.float64) - state_mean[: state.size].astype(np.float64)) / std
    else:
        z = state.astype(np.float64)
    if previous_proprio is None:
        state_delta_prev = np.zeros_like(state)
    else:
        state_delta_prev = state - previous_proprio

    feature_maps: list[dict[str, float]] = []
    features = []
    for idx in range(len(seeds)):
        path_i = path_np[idx]
        last_i = last_np[idx]
        path_step_mean = path_i.mean(axis=-1)
        last_step_mean = last_i.mean(axis=-1)
        action = chunks_env[idx, 0].astype(np.float32)
        plan_delta = np.diff(chunks_env[idx], axis=0)
        plan_delta_norms = np.linalg.norm(plan_delta, axis=-1) if plan_delta.size else np.array([0.0], dtype=np.float32)
        if previous_action is None:
            action_delta_prev = np.zeros_like(action)
        else:
            action_delta_prev = action - previous_action

        fmap: dict[str, float] = {
            "path_step_mean": float(path_step_mean[0]),
            "last_step_mean": float(last_step_mean[0]),
            "mean_path_var": float(path_i.mean()),
            "mean_last_var": float(last_i.mean()),
            "max_path_var": float(path_i.max()),
            "max_last_var": float(last_i.max()),
            "sample_action_var_mean": float(sample_var.mean()),
            "sample_action_var_max": float(sample_var.max()),
            "sample_action_l2_mean": float(sample_l2.mean()),
            "sample_action_l2_max": float(sample_l2.max()),
            "sample_action_translation_var": float(sample_var[..., :3].mean()),
            "sample_action_rotation_var": float(sample_var[..., 3:rotation_end_np].mean()) if rotation_end_np > 3 else 0.0,
            "sample_action_gripper_var": float(sample_var[..., -1].mean()),
            "action_norm": float(np.linalg.norm(action)),
            "action_max_abs": float(np.max(np.abs(action))),
            "action_translation_norm": float(np.linalg.norm(action[:3])),
            "action_rotation_norm": float(np.linalg.norm(action[3:rotation_end_np])) if rotation_end_np > 3 else 0.0,
            "action_gripper_abs": float(abs(action[-1])),
            "action_delta_prev_norm": float(np.linalg.norm(action_delta_prev)),
            "action_delta_prev_max_abs": float(np.max(np.abs(action_delta_prev))),
            "plan_drift_l2": float(np.linalg.norm(chunks_env[idx, -1] - chunks_env[idx, 0])),
            "plan_drift_mean_l2": float(plan_delta_norms.mean()),
            "plan_drift_max_l2": float(plan_delta_norms.max()),
            "state_mahalanobis": float(np.linalg.norm(z)),
            "state_mahalanobis_eef": float(np.linalg.norm(z[:3])),
            "state_mahalanobis_rotation": float(np.linalg.norm(z[3:6])),
            "state_mahalanobis_gripper": float(np.linalg.norm(z[6:8])),
            "state_eef_norm": float(np.linalg.norm(state[:3])),
            "state_rotation_norm": float(np.linalg.norm(state[3:6])),
            "state_gripper_norm": float(np.linalg.norm(state[6:8])),
            "state_gripper_width": float(abs(state[7] - state[6])) if state.size >= 8 else 0.0,
            "state_delta_prev_norm": float(np.linalg.norm(state_delta_prev)),
        }
        if velocity_trace is not None and update_trace is not None:
            fmap.update(
                {
                    "denoise_velocity_norm_mean": tensor_scalar(velocity_trace[idx].mean()),
                    "denoise_velocity_norm_max": tensor_scalar(velocity_trace[idx].amax()),
                    "denoise_update_norm_mean": tensor_scalar(update_trace[idx].mean()),
                    "denoise_update_norm_max": tensor_scalar(update_trace[idx].amax()),
                    "denoise_update_norm_final": tensor_scalar(update_trace[idx, -1]),
                    "denoise_update_spike": tensor_scalar((update_trace[idx, 1:] - update_trace[idx, :-1]).clamp_min(0.0).amax())
                    if update_trace.shape[1] > 1
                    else 0.0,
                    "denoise_final_initial_action_l2": tensor_scalar((chunks_norm_t[idx] - initial_noise[idx]).flatten().norm()),
                }
            )
            if update_vec_trace is not None and update_vec_trace.shape[1] > 1:
                step_delta = update_vec_trace[idx, 1:] - update_vec_trace[idx, :-1]
                cos = F.cosine_similarity(update_vec_trace[idx, 1:], update_vec_trace[idx, :-1], dim=-1)
                fmap["denoise_update_oscillation_mean"] = tensor_scalar(step_delta.norm(dim=-1).mean())
                fmap["denoise_update_direction_flip_mean"] = tensor_scalar((1.0 - cos).mean())
            else:
                fmap["denoise_update_oscillation_mean"] = 0.0
                fmap["denoise_update_direction_flip_mean"] = 0.0
        if denoise_mean_trace is not None:
            trace = denoise_mean_trace[idx]
            initial_mean = trace[0]
            final_mean = trace[-1]
            if trace.shape[0] > 1:
                x = torch.arange(trace.shape[0], device=trace.device, dtype=trace.dtype)
                x = x - x.mean()
                y = trace - trace.mean()
                slope = (y * x).sum() / x.square().sum().clamp_min(1e-12)
                spike = (trace[1:] - trace[:-1]).clamp_min(0.0).max()
            else:
                slope = torch.zeros((), device=trace.device, dtype=trace.dtype)
                spike = torch.zeros((), device=trace.device, dtype=trace.dtype)
            rotation_end = min(6, last_step_variance.shape[-1])
            final_rotation_mean = (
                last_step_variance[idx, :, 3:rotation_end].mean()
                if rotation_end > 3
                else torch.zeros((), device=trace.device, dtype=trace.dtype)
            )
            fmap.update(
                {
                    "denoise_initial_mean": tensor_scalar(initial_mean),
                    "denoise_final_mean": tensor_scalar(final_mean),
                    "denoise_delta": tensor_scalar(initial_mean - final_mean),
                    "denoise_slope": tensor_scalar(slope),
                    "denoise_final_max": tensor_scalar(last_step_variance[idx].amax()),
                    "denoise_spike": tensor_scalar(spike),
                    "denoise_final_gripper": tensor_scalar(last_step_variance[idx, :, -1].mean()),
                    "denoise_final_rotation_mean": tensor_scalar(final_rotation_mean),
                }
            )
        for key in UNCERTAINTY_49D_KEYS:
            fmap.setdefault(key, 0.0)
        feature_maps.append(fmap)
        features.append([float(fmap[key]) for key in UNCERTAINTY_49D_KEYS])

    return CandidateBatch(
        chunks_env=chunks_env,
        chunks_norm=chunks_norm,
        features_49d=np.asarray(features, dtype=np.float32),
        feature_maps=feature_maps,
    )


def history_array(history: deque[tuple[np.ndarray, np.ndarray, np.ndarray]], history_steps: int) -> np.ndarray:
    out = np.zeros((history_steps, 21), dtype=np.float32)
    src = list(history)[-history_steps:]
    offset = history_steps - len(src)
    for i, (prop, act, ace) in enumerate(src):
        out[offset + i, :] = np.concatenate([prop, act, ace[:6]]).astype(np.float32)
    return out


def action_stats(chunk_norm: np.ndarray) -> np.ndarray:
    chunk = np.asarray(chunk_norm, dtype=np.float32)
    return np.concatenate([chunk[0], chunk.mean(axis=0), chunk.std(axis=0), chunk[-1] - chunk[0]]).astype(np.float32)


def build_static(chunk_norm: np.ndarray, ace: np.ndarray, proprio: np.ndarray, features_49d: np.ndarray, detector: RiskDetector) -> np.ndarray:
    base = np.concatenate([action_stats(chunk_norm), ace, proprio]).astype(np.float32)
    if detector.static_dim == 43:
        return base
    if not detector.selected_uncertainty_dims:
        raise RuntimeError(f"detector {detector.name} expects static_dim={detector.static_dim} but has no selected uncertainty dims")
    unc = np.asarray(features_49d, dtype=np.float32)[detector.selected_uncertainty_dims]
    return np.concatenate([base, unc]).astype(np.float32)


def score_candidates(detector: RiskDetector, hist: np.ndarray, chunks_norm: np.ndarray, ace: np.ndarray, proprio: np.ndarray, features_49d: np.ndarray, device: torch.device) -> np.ndarray:
    h = np.repeat(hist[None, :, :], chunks_norm.shape[0], axis=0)
    a = chunks_norm.astype(np.float32)
    st = np.stack([build_static(a[i], ace, proprio, features_49d[i], detector) for i in range(a.shape[0])], axis=0)
    h = standardize_last_dim(h, detector.stats["history"])
    a = standardize_last_dim(a, detector.stats["action"])
    st = standardize_last_dim(st, detector.stats["static"])
    with torch.inference_mode():
        batch = {
            "history": torch.as_tensor(h, dtype=torch.float32, device=device),
            "action": torch.as_tensor(a, dtype=torch.float32, device=device),
            "static": torch.as_tensor(st, dtype=torch.float32, device=device),
        }
        return torch.sigmoid(detector.model(batch)).detach().cpu().numpy().astype(np.float32)


def select_action(scores: np.ndarray, detector: RiskDetector, min_margin: float, strong_margin: float) -> tuple[int, str]:
    main = float(scores[0])
    best_idx = int(np.argmin(scores))
    best = float(scores[best_idx])
    if best_idx == 0:
        return 0, "main_is_lowest"
    diff = main - best
    q95 = detector.thresholds["q95"]
    q99 = detector.thresholds["q99"]
    if main < q95:
        return 0, "main_below_q95"
    if diff < min_margin:
        return 0, "insufficient_margin"
    if best < q95:
        return best_idx, "best_below_q95"
    if main >= q99 and diff >= strong_margin:
        return best_idx, "main_q99_strong_margin"
    return 0, "strict_margin_reject"


def run_episode(
    args: argparse.Namespace,
    cfg: dict[str, Any],
    policy: str,
    detector: RiskDetector | None,
    episode_index: int,
    reset_seed: int,
    simvla_model: Any,
    processor: Any,
    image_preprocessor: ImagePreprocessor,
    benchmark_dict: dict[str, Any],
    get_libero_path_fn: Any,
    offscreen_cls: Any,
    device: torch.device,
    state_mean: np.ndarray | None,
    state_std: np.ndarray | None,
    out_dir: Path,
) -> dict[str, Any]:
    suite = str(cfg["suite"])
    task_id = int(cfg["task_id"])
    start = time.time()
    env = None
    rows_path = out_dir / f"step_scores_{policy}.jsonl"
    history: deque[tuple[np.ndarray, np.ndarray, np.ndarray]] = deque(maxlen=int(cfg.get("history_steps", 16)))
    scores_seen = []
    selected_scores = []
    modification_count = 0
    first_mod_timestep = None
    seed_collision_count = 0
    main_ace_collision_count = 0
    success = False
    terminal_done = False
    error_message = ""
    num_steps = 0
    last_selection_reason = ""
    try:
        env, bundle = make_env(
            benchmark_dict,
            get_libero_path_fn,
            offscreen_cls,
            suite,
            task_id,
            int(cfg.get("resolution", 128)),
            int(reset_seed),
        )
        init_states = bundle["init_states"]
        lang = bundle["task"].language
        init_state_idx = int(reset_seed) % len(init_states)
        obs = reset_to_init(env, init_states[init_state_idx], int(cfg.get("warmup", 10)))
        lang_t = processor.encode_language([lang])
        lang_t = {key: value.to(device) for key, value in lang_t.items()}
        previous_action = None
        previous_proprio = None

        for timestep in range(int(cfg.get("max_steps", 300))):
            proprio_np = obs_to_proprio(obs)
            before_img, before_wrist = obs_images(obs)
            images_t, mask_t = image_preprocessor(before_img, before_wrist, device)
            proprio_t = torch.as_tensor(proprio_np, dtype=torch.float32, device=device).unsqueeze(0)
            n_samples = 1 if policy == "simvla_only" else 1 + int(cfg.get("ace_candidate_count", 8))
            seeds = action_seeds_for_step(int(cfg["global_action_seed"]), int(reset_seed), int(episode_index), timestep, n_samples)
            if len(set(seeds)) != len(seeds):
                seed_collision_count += 1
                raise RuntimeError(f"duplicate seeds after deterministic generation: {seeds}")
            if len(seeds) > 1 and seeds[0] in set(seeds[1:]):
                main_ace_collision_count += 1
                raise RuntimeError(f"main seed collision with ACE seeds: {seeds}")

            main_candidates = generate_candidates_with_uncertainty(
                model=simvla_model,
                input_ids=lang_t["input_ids"],
                image_input=images_t,
                image_mask=mask_t,
                proprio=proprio_t,
                seeds=[seeds[0]],
                steps=int(cfg.get("model_denoise_steps", 10)),
                previous_action=previous_action,
                previous_proprio=previous_proprio,
                state_mean=state_mean,
                state_std=state_std,
            )
            if policy == "simvla_only":
                candidates = main_candidates
            else:
                ace_candidates = generate_candidates_with_uncertainty(
                    model=simvla_model,
                    input_ids=lang_t["input_ids"],
                    image_input=images_t,
                    image_mask=mask_t,
                    proprio=proprio_t,
                    seeds=seeds[1:],
                    steps=int(cfg.get("model_denoise_steps", 10)),
                    previous_action=previous_action,
                    previous_proprio=previous_proprio,
                    state_mean=state_mean,
                    state_std=state_std,
                )
                candidates = combine_main_and_ace_batches(main_candidates, ace_candidates)
            ace = compute_ace_metrics(candidates.chunks_norm[1:])
            hist = history_array(history, int(cfg.get("history_steps", 16)))
            selected_idx = 0
            score_list = None
            selected_score = None
            main_score = None
            if policy != "simvla_only":
                assert detector is not None
                score_arr = score_candidates(detector, hist, candidates.chunks_norm, ace, proprio_np, candidates.features_49d, device)
                selected_idx, last_selection_reason = select_action(
                    score_arr,
                    detector,
                    float(cfg.get("selection_min_margin", 0.10)),
                    float(cfg.get("selection_strong_margin", 0.15)),
                )
                score_list = [float(x) for x in score_arr.tolist()]
                main_score = float(score_arr[0])
                selected_score = float(score_arr[selected_idx])
                scores_seen.append(main_score)
                selected_scores.append(selected_score)
                if selected_idx != 0:
                    modification_count += 1
                    if first_mod_timestep is None:
                        first_mod_timestep = timestep
            else:
                last_selection_reason = "simvla_only"

            action = candidates.chunks_env[selected_idx, 0].astype(np.float32)
            obs, rew, done, info = env.step(action)
            reward_success = bool(float(rew) > 0.0)
            checked_success = check_success(env)
            success = success or reward_success or bool(checked_success)
            terminal_done = terminal_done or bool(done)
            history.append((proprio_np, action, ace))
            previous_action = action
            previous_proprio = proprio_np
            num_steps += 1

            append_jsonl(
                rows_path,
                {
                    "schema_version": "dean_uncertainty_realtime_step_v1",
                    "policy": policy,
                    "suite": suite,
                    "task_id": task_id,
                    "episode_index": episode_index,
                    "reset_seed": int(reset_seed),
                    "timestep": timestep,
                    "main_seed": int(seeds[0]),
                    "ace_candidate_seeds": [int(s) for s in seeds[1:]],
                    "selected_candidate_index": int(selected_idx),
                    "selection_reason": last_selection_reason,
                    "main_score": main_score,
                    "selected_score": selected_score,
                    "candidate_scores": score_list,
                    "success_after_step": bool(success),
                    "reward": float(rew),
                    "done": bool(done),
                },
            )
            if done or success:
                break
    except Exception as exc:
        error_message = "".join(traceback.format_exception_only(type(exc), exc)).strip()
        traceback.print_exc()
    finally:
        if env is not None:
            try:
                env.close()
            except Exception:
                pass

    wall = time.time() - start
    return {
        "schema_version": "dean_uncertainty_realtime_episode_v1",
        "policy": policy,
        "risk_model_dir": str(detector.model_dir) if detector else "",
        "risk_static_dim": detector.static_dim if detector else 0,
        "selected_uncertainty_dims": detector.selected_uncertainty_dims if detector else [],
        "suite": suite,
        "task_id": task_id,
        "episode_index": int(episode_index),
        "reset_seed": int(reset_seed),
        "success": bool(success) and not bool(error_message),
        "outcome": "error" if error_message else ("success" if success else "failure_or_timeout"),
        "terminal_done": bool(terminal_done),
        "num_steps": int(num_steps),
        "wall_time_seconds": float(wall),
        "error_message": error_message,
        "action_modifications_count": int(modification_count),
        "first_modification_timestep": first_mod_timestep,
        "risk_score_min": float(np.min(scores_seen)) if scores_seen else None,
        "risk_score_mean": float(np.mean(scores_seen)) if scores_seen else None,
        "risk_score_max": float(np.max(scores_seen)) if scores_seen else None,
        "selected_risk_min": float(np.min(selected_scores)) if selected_scores else None,
        "selected_risk_mean": float(np.mean(selected_scores)) if selected_scores else None,
        "selected_risk_max": float(np.max(selected_scores)) if selected_scores else None,
        "seed_collisions": int(seed_collision_count),
        "main_seed_collisions_with_ace": int(main_ace_collision_count),
        "updated_at": now_iso(),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser("Dean realtime SimVLA uncertainty policy v1")
    p.add_argument("--config", required=True)
    p.add_argument("--policy", choices=["simvla_only", "risk_base", "risk_unc_topk8"], required=True)
    p.add_argument("--num-episodes", type=int, default=None)
    p.add_argument("--episode-start", type=int, default=0)
    p.add_argument("--episode-end", type=int, default=None)
    p.add_argument("--smoke", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg_path = Path(args.config)
    cfg = json.loads(cfg_path.read_text())
    setup_runtime(Path(cfg.get("simvla_root", DEAN_SIMVLA_ROOT)), Path(cfg.get("libero_pro_root", DEAN_LIBERO_PRO_ROOT)))

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv
    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor

    torch.set_float32_matmul_precision("high")
    device = torch.device(cfg.get("device") or ("cuda" if torch.cuda.is_available() else "cpu"))
    set_all_seeds(int(cfg.get("model_load_seed", 7)))
    checkpoint = Path(cfg.get("checkpoint", str(DEAN_CKPT_60K)))
    expected_sha = str(cfg.get("expected_checkpoint_sha256", ""))
    if expected_sha:
        actual_sha = sha256_file(checkpoint / "model.safetensors")
        if actual_sha != expected_sha:
            raise RuntimeError(f"checkpoint sha mismatch expected={expected_sha} actual={actual_sha}")

    print(f"[startup] policy={args.policy} config={cfg_path} checkpoint={checkpoint}", flush=True)
    simvla_model = SmolVLMVLA.from_pretrained(str(checkpoint)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(str(cfg.get("smolvlm_path", DEAN_SMOLVLM_CACHE)))
    norm_stats = Path(cfg.get("norm_stats", str(DEAN_NORM_STATS)))
    if norm_stats.exists():
        simvla_model.action_space.load_norm_stats(str(norm_stats))
    if not getattr(simvla_model.config, "predict_uncertainty", False):
        raise RuntimeError("checkpoint does not expose predict_uncertainty=True")
    state_mean, state_std = load_state_stats(simvla_model, norm_stats)
    image_preprocessor = ImagePreprocessor(int(cfg.get("image_size", 384)))
    benchmark_dict = benchmark.get_benchmark_dict()

    detector = None
    if args.policy == "risk_base":
        detector = load_detector("base", Path(cfg["risk_model_base_dir"]), device)
    elif args.policy == "risk_unc_topk8":
        detector = load_detector("unc_topk8", Path(cfg["risk_model_unc_topk8_dir"]), device)

    out_dir = Path(cfg["output_dir"]) / args.policy
    out_dir.mkdir(parents=True, exist_ok=True)
    seeds = [int(x) for x in cfg["reset_seeds"]]
    if len(set(seeds)) != len(seeds):
        raise RuntimeError("reset_seeds must be unique")
    start = int(args.episode_start)
    end = args.episode_end if args.episode_end is not None else len(seeds)
    if args.num_episodes is not None:
        end = min(start + int(args.num_episodes), end)
    if args.smoke:
        end = min(start + 1, end)
    selected = list(range(start, min(end, len(seeds))))

    write_json(
        out_dir / "run_manifest.json",
        {
            "schema_version": "dean_uncertainty_realtime_manifest_v1",
            "created_at": now_iso(),
            "policy": args.policy,
            "config": str(cfg_path),
            "suite": cfg["suite"],
            "task_id": int(cfg["task_id"]),
            "episode_indices": selected,
            "reset_seeds_sha256": hashlib.sha256(json.dumps(seeds).encode("utf-8")).hexdigest(),
            "checkpoint": str(checkpoint),
            "checkpoint_sha256": sha256_file(checkpoint / "model.safetensors"),
            "risk_model_dir": str(detector.model_dir) if detector else "",
            "risk_thresholds": detector.thresholds if detector else {},
            "selected_uncertainty_dims": detector.selected_uncertainty_dims if detector else [],
            "execute_policy": "receding_horizon_execute_first_action_only",
        },
    )

    counts: Counter[str] = Counter()
    total_steps = 0
    campaign_start = time.time()
    for ep_idx in selected:
        summary = run_episode(
            args,
            cfg,
            args.policy,
            detector,
            ep_idx,
            seeds[ep_idx],
            simvla_model,
            processor,
            image_preprocessor,
            benchmark_dict,
            get_libero_path,
            OffScreenRenderEnv,
            device,
            state_mean,
            state_std,
            out_dir,
        )
        append_jsonl(out_dir / "episode_summaries.jsonl", summary)
        counts[summary["outcome"]] += 1
        total_steps += int(summary["num_steps"])
        write_json(
            out_dir / "live_status.json",
            {
                "schema_version": "dean_uncertainty_realtime_status_v1",
                "updated_at": now_iso(),
                "policy": args.policy,
                "suite": cfg["suite"],
                "task_id": int(cfg["task_id"]),
                "completed": sum(counts.values()),
                "target": len(selected),
                "counts": dict(counts),
                "total_steps": total_steps,
                "elapsed_seconds": time.time() - campaign_start,
                "last_episode": summary,
            },
        )
        print(
            f"[episode] policy={args.policy} ep={ep_idx} seed={seeds[ep_idx]} "
            f"outcome={summary['outcome']} steps={summary['num_steps']} mods={summary['action_modifications_count']} "
            f"time={summary['wall_time_seconds']:.1f}s",
            flush=True,
        )


if __name__ == "__main__":
    main()
