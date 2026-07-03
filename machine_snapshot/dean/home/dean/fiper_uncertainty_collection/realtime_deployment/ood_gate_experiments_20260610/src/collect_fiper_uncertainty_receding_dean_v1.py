#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import subprocess
import sys
import time
import traceback
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image


DEAN_SIMVLA_ROOT = Path("/home/redafrix/SimVLA_modified")
DEAN_LIBERO_PRO_ROOT = Path("/home/redafrix/LIBERO-PRO")
DEAN_CKPT_60K = Path("/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000")
DEAN_NORM_STATS = DEAN_SIMVLA_ROOT / "norm_stats/libero_norm.json"
DEAN_SMOLVLM_CACHE = (
    "/home/redafrix/.cache/huggingface/hub/"
    "models--HuggingFaceTB--SmolVLM-500M-Instruct/"
    "snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47"
)

DEFAULT_SUITES = [
    "libero_spatial_object",
    "libero_object_object",
    "libero_goal_object",
    "libero_10_object",
    "libero_90",
]

UNCERTAINTY_49D_KEYS = [
    "path_step_mean",
    "last_step_mean",
    "mean_path_var",
    "mean_last_var",
    "max_path_var",
    "max_last_var",
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
    "state_mahalanobis",
    "state_mahalanobis_eef",
    "state_mahalanobis_rotation",
    "state_mahalanobis_gripper",
    "state_eef_norm",
    "state_rotation_norm",
    "state_gripper_norm",
    "state_gripper_width",
    "state_delta_prev_norm",
]
UNCERTAINTY_DELTA_49D_KEYS = [f"{key}_delta" for key in UNCERTAINTY_49D_KEYS]


def setup_runtime(simvla_root: Path, libero_pro_root: Path) -> None:
    os.environ.setdefault("MUJOCO_GL", "egl")
    os.environ.setdefault("PYOPENGL_PLATFORM", "egl")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("USE_TF", "0")
    os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
    os.environ.setdefault("USE_FLAX", "0")
    for path in [Path(__file__).parent, simvla_root, libero_pro_root]:
        text = str(path)
        if text not in sys.path:
            sys.path.insert(0, text)


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


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(json_sanitize(payload), indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(json_sanitize(row), sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def git_hash() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=Path(__file__).resolve().parents[2],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "unknown"


def sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def set_all_seeds(seed: int) -> None:
    seed = int(seed) % (2**31 - 1)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def draw_unique_seeds(rng: np.random.Generator, n: int) -> tuple[list[int], int]:
    seeds: list[int] = []
    seen: set[int] = set()
    collisions = 0
    while len(seeds) < n:
        candidate = int(rng.integers(0, 2**31 - 1, dtype=np.int64))
        if candidate in seen:
            collisions += 1
            continue
        seen.add(candidate)
        seeds.append(candidate)
    return seeds, collisions


def quat2axisangle(quat: np.ndarray) -> np.ndarray:
    quat = np.asarray(quat, dtype=np.float64).copy()
    if quat.size < 4:
        return np.zeros(3, dtype=np.float64)
    quat[3] = np.clip(quat[3], -1.0, 1.0)
    den = np.sqrt(max(0.0, 1.0 - quat[3] * quat[3]))
    if math.isclose(den, 0.0):
        return np.zeros(3, dtype=np.float64)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den


def obs_to_proprio(obs: dict[str, Any]) -> np.ndarray:
    ee_pos = np.asarray(obs.get("robot0_eef_pos", np.zeros(3)), dtype=np.float32)
    ee_quat = np.asarray(obs.get("robot0_eef_quat", np.array([0, 0, 0, 1.0])), dtype=np.float32)
    grip = np.asarray(obs.get("robot0_gripper_qpos", np.zeros(2)), dtype=np.float32)
    state = np.concatenate([ee_pos, quat2axisangle(ee_quat).astype(np.float32), grip])[:8]
    if state.size < 8:
        state = np.pad(state, (0, 8 - state.size))
    return state.astype(np.float32)


def obs_images(obs: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    img = obs.get("agentview_image")
    wrist = obs.get("robot0_eye_in_hand_image")
    if img is None:
        img = np.zeros((128, 128, 3), dtype=np.uint8)
    if wrist is None:
        wrist = np.zeros_like(img)
    return np.ascontiguousarray(img[::-1, ::-1]), np.ascontiguousarray(wrist[::-1, ::-1])


def get_sim(env: Any) -> Any:
    return getattr(env, "sim", None) or getattr(getattr(env, "env", None), "sim", None)


def object_body_positions(env: Any) -> dict[str, list[float]]:
    sim = get_sim(env)
    if sim is None:
        return {}
    try:
        names = list(sim.model.body_names)
    except Exception:
        names = []
    ignore = ("world", "robot", "gripper", "eef", "mount", "base", "link", "wrist", "camera", "table", "floor")
    out: dict[str, list[float]] = {}
    for name in names:
        low = str(name).lower()
        if any(tok in low for tok in ignore):
            continue
        try:
            bid = sim.model.body_name2id(name)
            out[str(name)] = np.asarray(sim.data.body_xpos[bid], dtype=float).tolist()
        except Exception:
            pass
    return out


def check_success(env: Any) -> bool | None:
    for obj in [env, getattr(env, "env", None), getattr(env, "base_env", None)]:
        if obj is None:
            continue
        fn = getattr(obj, "_check_success", None) or getattr(obj, "check_success", None)
        if callable(fn):
            try:
                return bool(fn())
            except Exception:
                pass
    return None


class HistoryBuffer:
    def __init__(self, maxlen: int):
        self.items: deque[dict[str, Any]] = deque(maxlen=max(0, int(maxlen)))

    def append(self, item: dict[str, Any]) -> None:
        if self.items.maxlen != 0:
            self.items.append(json_sanitize(item))

    def to_list(self) -> list[dict[str, Any]]:
        return list(self.items)


class ImagePreprocessor:
    def __init__(self, image_size: int = 384):
        self.image_size = int(image_size)
        self.mean = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float32).view(3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float32).view(3, 1, 1)

    def _to_tensor(self, image: np.ndarray) -> torch.Tensor:
        pil = Image.fromarray(image.astype(np.uint8)).resize((self.image_size, self.image_size), Image.BILINEAR)
        arr = np.asarray(pil, dtype=np.float32) / 255.0
        if arr.ndim == 2:
            arr = np.repeat(arr[..., None], 3, axis=-1)
        if arr.shape[-1] > 3:
            arr = arr[..., :3]
        tensor = torch.from_numpy(np.ascontiguousarray(arr)).permute(2, 0, 1)
        return (tensor - self.mean) / self.std

    def __call__(self, image0: np.ndarray, image1: np.ndarray, device: torch.device) -> tuple[torch.Tensor, torch.Tensor]:
        img0 = self._to_tensor(image0)
        img1 = self._to_tensor(image1)
        pad = torch.zeros_like(img0)
        images = torch.stack([img0, img1, pad], dim=0).unsqueeze(0).to(device)
        image_mask = torch.tensor([[True, True, False]], device=device)
        return images, image_mask


@dataclass
class BatchResult:
    chunks_env: np.ndarray
    chunks_norm: np.ndarray
    main_uncertainty: dict[str, Any]
    features_49d: list[float]
    feature_map: dict[str, float]


def tensor_scalar(value: torch.Tensor | float | int) -> float:
    if torch.is_tensor(value):
        return float(value.detach().cpu().reshape(-1)[0].item())
    return float(value)


def generate_seeded_chunks_with_main_uncertainty(
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
) -> BatchResult:
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

        path_np = path_variance[0].detach().cpu().numpy()
        last_np = last_step_variance[0].detach().cpu().numpy()
        path_step_mean = path_np.mean(axis=-1)
        last_step_mean = last_np.mean(axis=-1)

        main_uncertainty: dict[str, Any] = {
            "path_variance": path_np.tolist(),
            "last_step_variance": last_np.tolist(),
            "path_step_mean": path_step_mean.tolist(),
            "last_step_mean": last_step_mean.tolist(),
            "mean_path_var": float(path_np.mean()),
            "mean_last_var": float(last_np.mean()),
            "max_path_var": float(path_np.max()),
            "max_last_var": float(last_np.max()),
        }

        main_idx = 0
        if velocity_norms:
            velocity_trace = torch.stack(velocity_norms, dim=1)
            update_trace = torch.stack(update_norms, dim=1)
            main_uncertainty.update(
                {
                    "denoise_velocity_norm_mean": tensor_scalar(velocity_trace[main_idx].mean()),
                    "denoise_velocity_norm_max": tensor_scalar(velocity_trace[main_idx].amax()),
                    "denoise_update_norm_mean": tensor_scalar(update_trace[main_idx].mean()),
                    "denoise_update_norm_max": tensor_scalar(update_trace[main_idx].amax()),
                    "denoise_update_norm_final": tensor_scalar(update_trace[main_idx, -1]),
                    "denoise_update_spike": tensor_scalar(
                        (update_trace[main_idx, 1:] - update_trace[main_idx, :-1]).clamp_min(0.0).amax()
                    )
                    if update_trace.shape[1] > 1
                    else 0.0,
                    "denoise_final_initial_action_l2": tensor_scalar((x_t[main_idx] - noise[main_idx]).flatten().norm()),
                }
            )
            if len(update_vectors) > 1:
                update_vec_trace = torch.stack(update_vectors, dim=1)
                step_delta = update_vec_trace[main_idx, 1:] - update_vec_trace[main_idx, :-1]
                cos = F.cosine_similarity(
                    update_vec_trace[main_idx, 1:],
                    update_vec_trace[main_idx, :-1],
                    dim=-1,
                )
                main_uncertainty["denoise_update_oscillation_mean"] = tensor_scalar(step_delta.norm(dim=-1).mean())
                main_uncertainty["denoise_update_direction_flip_mean"] = tensor_scalar((1.0 - cos).mean())
            else:
                main_uncertainty["denoise_update_oscillation_mean"] = 0.0
                main_uncertainty["denoise_update_direction_flip_mean"] = 0.0

        if denoise_means:
            denoise_mean_trace = torch.stack(denoise_means, dim=1)
            trace = denoise_mean_trace[main_idx]
            initial_mean = trace[0]
            final_mean = trace[-1]
            if trace.shape[0] > 1:
                x = torch.arange(trace.shape[0], device=device, dtype=dtype)
                x = x - x.mean()
                y = trace - trace.mean()
                slope = (y * x).sum() / x.square().sum().clamp_min(1e-12)
                spike = (trace[1:] - trace[:-1]).clamp_min(0.0).max()
            else:
                slope = torch.zeros((), device=device, dtype=dtype)
                spike = torch.zeros((), device=device, dtype=dtype)
            rotation_end = min(6, last_step_variance.shape[-1])
            final_rotation_mean = (
                last_step_variance[main_idx, :, 3:rotation_end].mean()
                if rotation_end > 3
                else torch.zeros((), device=device, dtype=dtype)
            )
            main_uncertainty.update(
                {
                    "denoise_initial_mean": tensor_scalar(initial_mean),
                    "denoise_final_mean": tensor_scalar(final_mean),
                    "denoise_delta": tensor_scalar(initial_mean - final_mean),
                    "denoise_slope": tensor_scalar(slope),
                    "denoise_final_max": tensor_scalar(last_step_variance[main_idx].amax()),
                    "denoise_spike": tensor_scalar(spike),
                    "denoise_final_gripper": tensor_scalar(last_step_variance[main_idx, :, -1].mean()),
                    "denoise_final_rotation_mean": tensor_scalar(final_rotation_mean),
                }
            )

        chunks_env = chunks_env_t.detach().cpu().numpy().astype(np.float32)
        chunks_norm = chunks_norm_t.detach().cpu().numpy().astype(np.float32)

    sample_var = chunks_env.var(axis=0)
    sample_mean = chunks_env.mean(axis=0, keepdims=True)
    sample_l2 = np.linalg.norm(chunks_env - sample_mean, axis=-1)
    rotation_end_np = min(6, chunks_env.shape[-1])

    action = chunks_env[0, 0].astype(np.float32)
    plan_delta = np.diff(chunks_env[0], axis=0)
    plan_delta_norms = np.linalg.norm(plan_delta, axis=-1) if plan_delta.size else np.array([0.0], dtype=np.float32)
    if previous_action is None:
        action_delta_prev = np.zeros_like(action)
    else:
        action_delta_prev = action - previous_action

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

    feature_map = {
        "path_step_mean": float(path_step_mean[0]),
        "last_step_mean": float(last_step_mean[0]),
        "mean_path_var": float(main_uncertainty["mean_path_var"]),
        "mean_last_var": float(main_uncertainty["mean_last_var"]),
        "max_path_var": float(main_uncertainty["max_path_var"]),
        "max_last_var": float(main_uncertainty["max_last_var"]),
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
        "plan_drift_l2": float(np.linalg.norm(chunks_env[0, -1] - chunks_env[0, 0])),
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
    for key in UNCERTAINTY_49D_KEYS:
        if key.startswith("denoise_"):
            feature_map[key] = float(main_uncertainty.get(key, 0.0))
    features_49d = [float(feature_map[key]) for key in UNCERTAINTY_49D_KEYS]

    return BatchResult(
        chunks_env=chunks_env,
        chunks_norm=chunks_norm,
        main_uncertainty=main_uncertainty,
        features_49d=features_49d,
        feature_map=feature_map,
    )


def load_state_stats(model: Any, norm_stats_path: Path) -> tuple[np.ndarray | None, np.ndarray | None]:
    stats_obj = getattr(getattr(model, "action_space", None), "state_norm_stats", None)
    if stats_obj is not None:
        try:
            mean = stats_obj.mean.detach().cpu().numpy().astype(np.float32)
            std = stats_obj.std.detach().cpu().numpy().astype(np.float32)
            return mean, std
        except Exception:
            pass
    try:
        raw = json.loads(norm_stats_path.read_text())
        state = raw.get("norm_stats", {}).get("state", {})
        return np.asarray(state["mean"], dtype=np.float32), np.asarray(state["std"], dtype=np.float32)
    except Exception:
        return None, None


def save_png(path: Path, img: np.ndarray) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(img.astype(np.uint8)).save(path)
    return str(path)


def task_count(bench: Any) -> int:
    n_tasks = getattr(bench, "n_tasks", None)
    if callable(n_tasks):
        return int(n_tasks())
    if n_tasks is not None:
        return int(n_tasks)
    return len(getattr(bench, "tasks", []))


def build_task_plan(benchmark_dict: dict[str, Any], suites: list[str], task_ids: list[int] | None) -> list[tuple[str, int]]:
    tasks: list[tuple[str, int]] = []
    missing = [suite for suite in suites if suite not in benchmark_dict]
    if missing:
        raise KeyError(f"suites unavailable in LIBERO registry: {missing}")
    for suite in suites:
        bench = benchmark_dict[suite]()
        available = set(range(task_count(bench)))
        ids = sorted(available if task_ids is None else [tid for tid in task_ids if tid in available])
        for task_id in ids:
            tasks.append((suite, int(task_id)))
    return tasks


def make_env(benchmark_dict: dict[str, Any], get_libero_path_fn: Any, offscreen_cls: Any, suite: str, task_id: int, resolution: int, env_seed: int):
    bench = benchmark_dict[suite]()
    task = bench.get_task(task_id)
    bddl_root = Path(get_libero_path_fn("bddl_files"))
    init_root = Path(get_libero_path_fn("init_states"))
    folder_candidates = [task.problem_folder]
    if task.problem_folder == "libero_goal_object_ood":
        folder_candidates.append("libero_goal_object_ood_temp")
    if task.problem_folder == "libero_spatial_object":
        # LIBERO-PRO registers this suite but the checked-out data tree only has
        # base spatial BDDL/init files. The task names match, so resolve it as an
        # explicit documented alias instead of modifying /home/redafrix in place.
        folder_candidates.append("libero_spatial")
    


    resolved_folder = task.problem_folder
    bddl_path = None
    init_states_path = None
    for folder in folder_candidates:
        candidate_bddl = bddl_root / folder / task.bddl_file
        if candidate_bddl.exists():
            bddl_path = candidate_bddl
            resolved_folder = folder # Track which folder worked for BDDL primarily
            break
    if bddl_path is None and task.problem_folder == "libero_goal_object_ood":
        ood_bddl_root = Path(os.environ.get("LIBERO_GOAL_OBJECT_OOD_BDDL_ROOT", "/home/dean/LIBERO-PRO/libero/libero/bddl_files"))
        for folder in folder_candidates:
            candidate_bddl = ood_bddl_root / folder / task.bddl_file
            if candidate_bddl.exists():
                bddl_path = candidate_bddl
                resolved_folder = folder
                break
    
    for folder in folder_candidates:
        candidate_init = init_root / folder / task.init_states_file
        if candidate_init.exists():
            init_states_path = candidate_init
            break
    if init_states_path is None and task.problem_folder == "libero_goal_object_ood":
        ood_init_root = Path(os.environ.get("LIBERO_GOAL_OBJECT_OOD_INIT_ROOT", "/home/dean/LIBERO-PRO/libero/libero/init_files"))
        for folder in folder_candidates:
            candidate_init = ood_init_root / folder / task.init_states_file
            if candidate_init.exists():
                init_states_path = candidate_init
                break

    if bddl_path is None or init_states_path is None:
        missing_details = [
            {
                "folder": folder,
                "bddl_exists": (bddl_root / folder / task.bddl_file).exists(),
                "init_exists": (init_root / folder / task.init_states_file).exists(),
            }
            for folder in folder_candidates
        ]
        raise FileNotFoundError(f"could not resolve BDDL/init files for {suite} task {task_id}: {missing_details}")

    try:
        init_states = torch.load(init_states_path, map_location="cpu", weights_only=False)
    except TypeError:
        init_states = torch.load(init_states_path, map_location="cpu")
    env_args = {
        "bddl_file_name": str(bddl_path),
        "camera_heights": int(resolution),
        "camera_widths": int(resolution),
    }
    env = offscreen_cls(**env_args)
    if hasattr(env, "seed"):
        env.seed(int(env_seed))
    return env, {
        "benchmark": bench,
        "task": task,
        "init_states": init_states,
        "bddl_path": str(bddl_path),
        "init_states_path": str(init_states_path),
        "declared_problem_folder": task.problem_folder,
        "resolved_problem_folder": resolved_folder,
        "suite": suite,
        "task_id": task_id,
    }


def reset_to_init(env: Any, init_state: Any, warmup: int) -> dict[str, Any]:
    obs = env.reset()
    if init_state is not None:
        obs = env.set_init_state(init_state)
    zero = np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32)
    for _ in range(max(0, int(warmup))):
        obs, _reward, _done, _info = env.step(zero)
    return obs


def load_completed_counts(summary_path: Path) -> dict[tuple[str, int], int]:
    counts: dict[tuple[str, int], int] = defaultdict(int)
    if not summary_path.exists():
        return counts
    with summary_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                key = (str(row["suite"]), int(row["task_id"]))
                counts[key] += 1
            except Exception:
                continue
    return counts


def collect(args: argparse.Namespace) -> None:
    setup_runtime(Path(args.simvla_root), Path(args.libero_pro_root))

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv
    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor
    from sim_state_utils import get_state, save_state_npz
    from task_parser import parse_task_context

    torch.set_float32_matmul_precision("high")
    device = torch.device(args.device or ("cuda" if torch.cuda.is_available() else "cpu"))
    checkpoint = Path(args.checkpoint)
    model_file = checkpoint / "model.safetensors"
    if not model_file.exists():
        raise FileNotFoundError(f"checkpoint model file missing: {model_file}")
    if args.expected_checkpoint_sha256:
        actual_sha = sha256_file(model_file)
        if actual_sha != args.expected_checkpoint_sha256:
            raise RuntimeError(
                f"checkpoint sha256 mismatch for {model_file}: expected={args.expected_checkpoint_sha256}, actual={actual_sha}"
            )

    print(f"[startup] loading model from {checkpoint}", flush=True)
    set_all_seeds(args.model_load_seed)
    model = SmolVLMVLA.from_pretrained(str(checkpoint)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(str(args.smolvlm_path))
    if args.norm_stats and Path(args.norm_stats).exists():
        model.action_space.load_norm_stats(str(args.norm_stats))
    if not getattr(model.config, "predict_uncertainty", False):
        raise RuntimeError("selected checkpoint does not have predict_uncertainty=True")

    state_mean, state_std = load_state_stats(model, Path(args.norm_stats))
    image_preprocessor = ImagePreprocessor(args.image_size)

    benchmark_dict = benchmark.get_benchmark_dict()
    task_ids = args.task_ids if args.task_ids else None
    global_tasks = build_task_plan(benchmark_dict, args.suites, task_ids)
    shard_tasks = [task for i, task in enumerate(global_tasks) if i % args.worker_shard_count == args.worker_shard_index]
    if not shard_tasks:
        raise RuntimeError("worker shard has no tasks; check shard index/count")

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    if args.save_states:
        (outdir / "states").mkdir(exist_ok=True)
    if args.save_images:
        (outdir / "images").mkdir(exist_ok=True)
    logs_dir = outdir / "logs"
    logs_dir.mkdir(exist_ok=True)

    rows_path = outdir / "fiper_receding_samples.jsonl"
    summaries_path = outdir / "episode_summaries.jsonl"
    status_path = outdir / "live_status.json"
    manifest_path = outdir / "run_manifest.json"

    episodes_per_task = load_completed_counts(summaries_path) if args.resume else defaultdict(int)
    rng = np.random.default_rng(int(args.global_action_seed) + 1000003 * int(args.worker_shard_index))
    code_version = git_hash()
    checkpoint_sha = sha256_file(model_file)

    manifest = {
        "schema_version": "dean_fiper_uncertainty_receding_v1_manifest",
        "created_at": now_iso(),
        "worker_id": args.worker_id,
        "worker_shard_index": args.worker_shard_index,
        "worker_shard_count": args.worker_shard_count,
        "global_task_count": len(global_tasks),
        "worker_task_count": len(shard_tasks),
        "global_task_plan": global_tasks,
        "worker_task_plan": shard_tasks,
        "suites": args.suites,
        "excluded_suites": ["libero_100"],
        "perturbation_plan": "generic_object_for_object_suites_plus_base_libero_90_control",
        "checkpoint": str(checkpoint),
        "checkpoint_sha256": checkpoint_sha,
        "smolvlm_path": str(args.smolvlm_path),
        "norm_stats": str(args.norm_stats),
        "uncertainty_49d_keys": UNCERTAINTY_49D_KEYS,
        "uncertainty_delta_49d_keys": UNCERTAINTY_DELTA_49D_KEYS,
        "ace_candidates": args.ace_candidates,
        "action_horizon": args.action_horizon,
        "model_denoise_steps": args.model_denoise_steps,
        "history_k": args.history_k,
        "max_timesteps": args.max_timesteps,
        "save_states": args.save_states,
        "save_images": args.save_images,
        "code_version": code_version,
    }
    write_json_atomic(manifest_path, manifest)

    total_episodes = sum(episodes_per_task.values())
    total_rows = 0
    outcome_counts: Counter[str] = Counter()
    consecutive_errors = 0
    seed_collisions_total = 0
    main_ace_collisions_total = 0
    start_time = time.time()

    print(
        f"[startup] worker={args.worker_id} shard={args.worker_shard_index}/{args.worker_shard_count} "
        f"tasks={len(shard_tasks)} checkpoint_sha={checkpoint_sha}",
        flush=True,
    )

    def write_status(extra: dict[str, Any] | None = None) -> None:
        elapsed = time.time() - start_time
        payload = {
            "schema_version": "dean_fiper_uncertainty_receding_v1_status",
            "updated_at": now_iso(),
            "worker_id": args.worker_id,
            "pid": os.getpid(),
            "elapsed_seconds": elapsed,
            "total_episodes_completed": total_episodes,
            "total_rows_written": total_rows,
            "outcome_counts": dict(outcome_counts),
            "episodes_per_task": {f"{k[0]}/task_{k[1]}": v for k, v in sorted(episodes_per_task.items())},
            "seed_collisions_total": seed_collisions_total,
            "main_ace_collisions_total": main_ace_collisions_total,
            "consecutive_errors": consecutive_errors,
        }
        if extra:
            payload.update(extra)
        write_json_atomic(status_path, payload)

    write_status({"state": "started"})

    for sweep_idx in range(int(args.num_sweeps)):
        for task_offset, (suite, task_id) in enumerate(shard_tasks):
            if args.max_episodes is not None and total_episodes >= args.max_episodes:
                write_status({"state": "max_episodes_reached"})
                return

            episode_start = time.time()
            rollout_idx = int(episodes_per_task[(suite, task_id)])
            episode_id = f"{args.worker_id}_{suite}_t{task_id}_r{rollout_idx}"
            episode_rows: list[dict[str, Any]] = []
            error_message = ""
            success = False
            terminal_done = False
            env = None
            previous_action: np.ndarray | None = None
            previous_proprio: np.ndarray | None = None
            previous_features: np.ndarray | None = None
            timesteps_seed_checked = 0
            episode_seed_collisions = 0
            episode_main_ace_collisions = 0

            try:
                write_status({"state": "running_episode", "suite": suite, "task_id": task_id, "episode_id": episode_id})
                env_seed = int(args.env_seed_base) + int(task_id) + 1009 * int(args.worker_shard_index)
                env, bundle = make_env(benchmark_dict, get_libero_path, OffScreenRenderEnv, suite, task_id, args.resolution, env_seed)
                init_states = bundle["init_states"]
                lang = bundle["task"].language
                init_state_idx = rollout_idx % len(init_states)
                obs = reset_to_init(env, init_states[init_state_idx], args.warmup)
                all_bodies = list(object_body_positions(env).keys())
                try:
                    task_context = parse_task_context(lang, obs, all_bodies=all_bodies)
                except Exception as exc:
                    task_context = {"parse_error": str(exc), "confidence": "ERROR"}
                hist = HistoryBuffer(args.history_k)

                for timestep in range(int(args.max_timesteps)):
                    state = get_state(env)
                    proprio_np = obs_to_proprio(obs)
                    before_obj = object_body_positions(env)
                    before_img, before_wrist = obs_images(obs)

                    state_path = None
                    state_id = f"{episode_id}_s{timestep:04d}"
                    if args.save_states:
                        state_path = save_state_npz(outdir / "states" / f"{state_id}.npz", state)
                    before_agent_path = (
                        save_png(outdir / "images" / f"{state_id}_before_agent.png", before_img) if args.save_images else None
                    )
                    before_wrist_path = (
                        save_png(outdir / "images" / f"{state_id}_before_wrist.png", before_wrist) if args.save_images else None
                    )

                    seeds, collisions = draw_unique_seeds(rng, 1 + int(args.ace_candidates))
                    episode_seed_collisions += collisions
                    seed_collisions_total += collisions
                    main_seed = seeds[0]
                    ace_seeds = seeds[1:]
                    if main_seed in set(ace_seeds):
                        episode_main_ace_collisions += 1
                        main_ace_collisions_total += 1
                        raise RuntimeError(f"main seed collided with ACE seeds at {episode_id} timestep {timestep}")
                    timesteps_seed_checked += 1

                    images_t, mask_t = image_preprocessor(before_img, before_wrist, device)
                    lang_t = processor.encode_language([lang])
                    lang_t = {key: value.to(device) for key, value in lang_t.items()}
                    proprio_t = torch.as_tensor(proprio_np, dtype=torch.float32, device=device).unsqueeze(0)

                    batch = generate_seeded_chunks_with_main_uncertainty(
                        model=model,
                        input_ids=lang_t["input_ids"],
                        image_input=images_t,
                        image_mask=mask_t,
                        proprio=proprio_t,
                        seeds=seeds,
                        steps=args.model_denoise_steps,
                        previous_action=previous_action,
                        previous_proprio=previous_proprio,
                        state_mean=state_mean,
                        state_std=state_std,
                    )

                    features = np.asarray(batch.features_49d, dtype=np.float32)
                    if previous_features is None:
                        deltas = np.zeros_like(features)
                    else:
                        deltas = features - previous_features

                    main_chunk_env = batch.chunks_env[0]
                    main_chunk_norm = batch.chunks_norm[0]
                    ace_chunks_env = batch.chunks_env[1:]
                    ace_chunks_norm = batch.chunks_norm[1:]
                    act = main_chunk_env[0].astype(np.float32)

                    row = {
                        "schema_version": "stage9_fiper_uncertainty_receding_dean_v1",
                        "episode_id": episode_id,
                        "episode_index_for_task": rollout_idx,
                        "sweep_idx": sweep_idx,
                        "task_offset_in_worker_plan": task_offset,
                        "timestep": timestep,
                        "suite": suite,
                        "task_id": int(task_id),
                        "task_instruction": lang,
                        "current": {
                            "proprio": proprio_np.tolist(),
                            "object_positions_before": before_obj,
                            "sim_state_path": state_path,
                            "before_image_path": before_agent_path,
                            "before_wrist_image_path": before_wrist_path,
                            "task_context": task_context,
                        },
                        "history": hist.to_list(),
                        "main_seed": int(main_seed),
                        "main_candidate_action_chunk_normalized": main_chunk_norm.tolist(),
                        "main_candidate_action_chunk_env": main_chunk_env.tolist(),
                        "executed_action": act.tolist(),
                        "ace_candidate_seeds": [int(seed) for seed in ace_seeds],
                        "ace_candidate_chunks_normalized": ace_chunks_norm.tolist(),
                        "ace_candidate_chunks_env": ace_chunks_env.tolist(),
                        "simvla_uncertainty_49d_keys": UNCERTAINTY_49D_KEYS,
                        "simvla_uncertainty_49d": features.tolist(),
                        "simvla_uncertainty_delta_49d_keys": UNCERTAINTY_DELTA_49D_KEYS,
                        "simvla_uncertainty_delta_49d": deltas.tolist(),
                        "simvla_uncertainty_scalar_map": batch.feature_map,
                        "simvla_uncertainty_raw": batch.main_uncertainty,
                        "metadata": {
                            "collection_time": now_iso(),
                            "code_version": code_version,
                            "source": "dean_fiper_uncertainty_receding_v1",
                            "checkpoint": str(checkpoint),
                            "checkpoint_sha256": checkpoint_sha,
                            "model_predict_uncertainty": True,
                            "ace_replay_used": False,
                            "uncertainty_features_used": True,
                            "object_perturbation_collection": True,
                            "init_state_idx": int(init_state_idx),
                            "declared_problem_folder": bundle.get("declared_problem_folder"),
                            "resolved_problem_folder": bundle.get("resolved_problem_folder"),
                            "bddl_path": bundle.get("bddl_path"),
                            "init_states_path": bundle.get("init_states_path"),
                            "env_seed": int(env_seed),
                            "worker_id": args.worker_id,
                            "worker_shard_index": args.worker_shard_index,
                            "worker_shard_count": args.worker_shard_count,
                        },
                        "deployability_flags": {
                            "proprio_deployable": True,
                            "history_deployable": True,
                            "candidate_action_deployable": True,
                            "uncertainty_features_deployable": True,
                            "object_positions_deployable": True,
                            "sim_state_deployable": False,
                            "before_image_deployable": True,
                            "reward_or_success_used_for_action": False,
                            "future_timestep_used": False,
                        },
                    }
                    episode_rows.append(row)

                    obs, rew, done, info = env.step(act)
                    reward_success = bool(float(rew) > 0.0)
                    checked_success = check_success(env)
                    success = success or reward_success or bool(checked_success)
                    terminal_done = terminal_done or bool(done)
                    next_proprio = obs_to_proprio(obs)
                    hist.append(
                        {
                            "reward": float(rew),
                            "success": bool(success),
                            "proprio": next_proprio.tolist(),
                            "executed_action": act.tolist(),
                        }
                    )
                    previous_action = act
                    previous_proprio = proprio_np
                    previous_features = features

                    if args.status_every_steps and timestep % int(args.status_every_steps) == 0:
                        write_status(
                            {
                                "state": "running_episode",
                                "suite": suite,
                                "task_id": task_id,
                                "episode_id": episode_id,
                                "timestep": timestep,
                            }
                        )
                    if done or success:
                        break

                consecutive_errors = 0

            except Exception as exc:
                error_message = "".join(traceback.format_exception_only(type(exc), exc)).strip()
                consecutive_errors += 1
                print(f"[episode-error] {episode_id}: {error_message}", flush=True)
                traceback.print_exc()
            finally:
                if env is not None:
                    try:
                        env.close()
                    except Exception:
                        pass

            outcome_str = "success" if success else "failure_or_timeout"
            if error_message:
                outcome_str = "error"
            outcome_counts[outcome_str] += 1
            for row in episode_rows:
                row["episode_outcome"] = outcome_str
                row["parent_episode_success"] = bool(success)
                row["parent_failed_or_timeout"] = not bool(success)
                row["parent_error"] = bool(error_message)
                row["terminal_done"] = bool(terminal_done)
                row["allowed_use"] = "train_calib_eval_success" if success else "eval_only_failure"
            if episode_rows:
                append_jsonl(rows_path, episode_rows)
                total_rows += len(episode_rows)

            episode_seconds = time.time() - episode_start
            summary = {
                "schema_version": "dean_fiper_uncertainty_receding_v1_episode_summary",
                "episode_id": episode_id,
                "suite": suite,
                "task_id": int(task_id),
                "sweep_idx": int(sweep_idx),
                "episode_index_for_task": int(rollout_idx),
                "outcome": outcome_str,
                "success": bool(success),
                "terminal_done": bool(terminal_done),
                "num_steps": len(episode_rows),
                "wall_time_seconds": episode_seconds,
                "error_message": error_message,
                "timesteps_seed_checked": timesteps_seed_checked,
                "seed_collisions": episode_seed_collisions,
                "main_seed_collisions_with_ace": episode_main_ace_collisions,
                "worker_id": args.worker_id,
                "updated_at": now_iso(),
            }
            append_jsonl(summaries_path, [summary])
            episodes_per_task[(suite, task_id)] += 1
            total_episodes += 1

            print(
                f"[episode] {episode_id} outcome={outcome_str} steps={len(episode_rows)} "
                f"time={episode_seconds:.1f}s total={total_episodes}",
                flush=True,
            )
            write_status({"state": "episode_completed", "last_episode": summary})

            if consecutive_errors >= int(args.max_consecutive_errors):
                write_status({"state": "failed", "reason": "max_consecutive_errors"})
                raise RuntimeError(f"stopping after {consecutive_errors} consecutive errors")

    write_status({"state": "num_sweeps_completed"})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Dean FIPER uncertainty receding collector v1")
    parser.add_argument("--simvla-root", default=str(DEAN_SIMVLA_ROOT))
    parser.add_argument("--libero-pro-root", default=str(DEAN_LIBERO_PRO_ROOT))
    parser.add_argument("--checkpoint", default=str(DEAN_CKPT_60K))
    parser.add_argument("--expected-checkpoint-sha256", default="")
    parser.add_argument("--smolvlm-path", default=DEAN_SMOLVLM_CACHE)
    parser.add_argument("--norm-stats", default=str(DEAN_NORM_STATS))
    parser.add_argument("--device", default="")
    parser.add_argument("--suites", nargs="+", default=DEFAULT_SUITES)
    parser.add_argument("--task-ids", nargs="+", type=int, default=[])
    parser.add_argument("--num-sweeps", type=int, default=1_000_000)
    parser.add_argument("--max-episodes", type=int, default=None)
    parser.add_argument("--max-timesteps", type=int, default=300)
    parser.add_argument("--ace-candidates", type=int, default=8)
    parser.add_argument("--action-horizon", type=int, default=10)
    parser.add_argument("--model-denoise-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--image-size", type=int, default=384)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed-base", type=int, default=7)
    parser.add_argument("--global-action-seed", type=int, default=2026052900)
    parser.add_argument("--model-load-seed", type=int, default=7)
    parser.add_argument("--worker-id", default="worker_0")
    parser.add_argument("--worker-shard-index", type=int, default=0)
    parser.add_argument("--worker-shard-count", type=int, default=1)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-states", dest="save_states", action="store_true", default=True)
    parser.add_argument("--no-save-states", dest="save_states", action="store_false")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--status-every-steps", type=int, default=10)
    parser.add_argument("--max-consecutive-errors", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    collect(parse_args())


if __name__ == "__main__":
    main()
