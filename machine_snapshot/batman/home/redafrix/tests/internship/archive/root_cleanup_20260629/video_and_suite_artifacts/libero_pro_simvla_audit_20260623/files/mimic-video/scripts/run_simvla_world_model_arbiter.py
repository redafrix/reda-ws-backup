#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
from collections import Counter, deque
from pathlib import Path
from typing import Any

import numpy as np
import torch
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
WORLD_ROOT = ROOT.parent
SIMVLA_MAIN_POLICY = "simvla_main"
SIMVLA_TOPK8_POLICY = "simvla_topk8"
WM_LOW_RISK_FALLBACK_POLICY = "wm_low_risk_fallback"
DUAL_THRESHOLD_HORIZON_POLICY = "dual_threshold_horizon"
DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY = "dual_main_risk_simvla_medoid"
WM_PREFIX_LOW_RISK_SIMVLA_POLICY = "wm_prefix_low_risk_simvla"
ARBITER_POLICIES = {
    SIMVLA_MAIN_POLICY,
    SIMVLA_TOPK8_POLICY,
    WM_LOW_RISK_FALLBACK_POLICY,
    DUAL_THRESHOLD_HORIZON_POLICY,
    DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY,
    WM_PREFIX_LOW_RISK_SIMVLA_POLICY,
}
SIMVLA_RISK_POLICIES = {
    SIMVLA_TOPK8_POLICY,
    WM_LOW_RISK_FALLBACK_POLICY,
    DUAL_THRESHOLD_HORIZON_POLICY,
    DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY,
    WM_PREFIX_LOW_RISK_SIMVLA_POLICY,
}
WORLD_MODEL_POLICIES = {
    WM_LOW_RISK_FALLBACK_POLICY,
    DUAL_THRESHOLD_HORIZON_POLICY,
    DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY,
    WM_PREFIX_LOW_RISK_SIMVLA_POLICY,
}
WORLD_MODEL_ACTION_BRANCHES = {
    "world_model",
    "both_high_short_world_model",
}


def _require(mapping: dict[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise RuntimeError(f"{context} missing required key: {key}")
    return mapping[key]


def _append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(_jsonable(row), sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(_jsonable(payload), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def _jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if torch.is_tensor(value):
        return value.detach().cpu().tolist()
    if isinstance(value, Path):
        return str(value)
    return value


def _sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolve_path(raw: str | Path, *, base: Path) -> Path:
    path = Path(os.path.expandvars(str(raw))).expanduser()
    if path.is_absolute():
        return path
    return (base / path).resolve()


def _resolve_path_or_model_id(raw: str | Path, *, base: Path) -> str:
    expanded = os.path.expandvars(str(raw)).strip()
    if expanded == "HuggingFaceTB/SmolVLM-500M-Instruct":
        return expanded
    path = _resolve_path(expanded, base=base)
    if not path.exists():
        raise FileNotFoundError(path)
    return str(path)


def _load_simvla_api(bundle_root: Path) -> dict[str, Any]:
    scripts_dir = bundle_root / "scripts"
    if not (scripts_dir / "run_policy_matrix.py").exists():
        raise FileNotFoundError(scripts_dir / "run_policy_matrix.py")
    for path in [str(scripts_dir), str(bundle_root), str(ROOT), str(ROOT / "model")]:
        if path not in sys.path:
            sys.path.insert(0, path)

    from run_policy_matrix import (  # type: ignore
        action_seeds_for_step,
        candidate_first_action_l2,
        check_success,
        combine_main_and_ace_batches,
        compute_ace_metrics,
        generate_candidates_with_uncertainty,
        history_array,
        load_detector,
        load_episode_specs,
        load_state_stats,
        make_env,
        obs_images,
        obs_to_proprio,
        reset_to_init,
        resolve_score_threshold,
        score_candidates,
        select_action,
        set_all_seeds,
        setup_runtime,
        sha256_array,
    )
    from collect_fiper_uncertainty_receding_dean_v1 import ImagePreprocessor  # type: ignore

    return {
        "action_seeds_for_step": action_seeds_for_step,
        "candidate_first_action_l2": candidate_first_action_l2,
        "check_success": check_success,
        "combine_main_and_ace_batches": combine_main_and_ace_batches,
        "compute_ace_metrics": compute_ace_metrics,
        "generate_candidates_with_uncertainty": generate_candidates_with_uncertainty,
        "history_array": history_array,
        "load_detector": load_detector,
        "load_episode_specs": load_episode_specs,
        "load_state_stats": load_state_stats,
        "make_env": make_env,
        "obs_images": obs_images,
        "obs_to_proprio": obs_to_proprio,
        "reset_to_init": reset_to_init,
        "resolve_score_threshold": resolve_score_threshold,
        "score_candidates": score_candidates,
        "select_action": select_action,
        "set_all_seeds": set_all_seeds,
        "setup_runtime": setup_runtime,
        "sha256_array": sha256_array,
        "ImagePreprocessor": ImagePreprocessor,
    }


class LazyWorldModelFallback:
    def __init__(self, cfg: dict[str, Any], out_dir: Path) -> None:
        self.cfg = cfg
        self.out_dir = out_dir
        self.policy: Any | None = None
        self.loaded_at: float | None = None

    def reset_episode(self, task_description: str, task_id: int, episode_index: int, global_episode_index: int) -> None:
        if self.policy is not None:
            self.policy.reset(task_description)
            self.policy.set_episode_context(task_id, episode_index, global_episode_index)

    def load(self) -> Any:
        if self.policy is not None:
            return self.policy

        sys.path.insert(0, str(ROOT))
        sys.path.insert(0, str(ROOT / "model"))
        from eval.libero.run import VAMInference  # pylint: disable=import-outside-toplevel

        cfg = self.cfg
        model_dir = ROOT / "model"
        rollout_dir = self.out_dir / "world_model_fallback"
        rollout_dir.mkdir(parents=True, exist_ok=True)

        def p(name: str) -> Path:
            return _resolve_path(cfg[name], base=ROOT)

        started = time.perf_counter()
        self.policy = VAMInference(
            str(cfg["experiment"]),
            str(p("video_model")),
            str(p("action_model")),
            p("dataset_statistics"),
            int(cfg["img_horizon"]),
            int(cfg["lowdim_horizon"]),
            int(cfg["stop_video_denoising_step"]),
            int(cfg["num_execute_actions"]),
            int(cfg["num_sampling_steps"]),
            rollout_dir,
            use_text_encoder=bool(cfg["use_text_encoder"]),
            uq_num_action_candidates=int(cfg["uq_num_action_candidates"]),
            uq_action_candidate_batch_size=int(cfg["uq_action_candidate_batch_size"]),
            uq_num_world_candidates=int(cfg["uq_num_world_candidates"]),
            uq_log_action_candidates=True,
            uq_save_candidate_arrays=bool(cfg["uq_save_candidate_arrays"]),
            v2w_uncertainty_head_path=p("v2w_uncertainty_head"),
            v2w_uncertainty_calibration_path=p("v2w_calibration"),
            v2w_uncertainty_variant=str(cfg["v2w_uncertainty_variant"]),
            v2w_uncertainty_save_variance_arrays=bool(cfg["v2w_uncertainty_save_variance_arrays"]),
            uq_control_policy=str(cfg["uq_control_policy"]),
            uq_risk_model_dir=p("uq_risk_model_dir"),
            uq_risk_threshold=float(cfg["uq_risk_threshold"]),
            uq_risk_medium_threshold=float(cfg["uq_risk_medium_threshold"]),
            uq_risk_persistence=int(cfg["uq_risk_persistence"]),
            uq_risk_medium_execute_actions=int(cfg["uq_risk_medium_execute_actions"]),
            uq_risk_high_execute_actions=int(cfg["uq_risk_high_execute_actions"]),
        )
        self.loaded_at = time.perf_counter() - started
        print(f"[arbiter] loaded world-model fallback in {self.loaded_at:.1f}s", flush=True)
        return self.policy

    @staticmethod
    def _agentview_image(obs: dict[str, np.ndarray]) -> np.ndarray:
        image = obs["agentview_image"][::-1, ::-1]
        if image.dtype != np.uint8:
            raise ValueError(f"Expected uint8 agentview image, got {image.dtype}.")
        return image

    def first_action_and_decision(
        self,
        obs: dict[str, np.ndarray],
        task_description: str,
        task_id: int,
        episode_index: int,
        global_episode_index: int,
    ) -> tuple[np.ndarray, dict[str, Any]]:
        policy = self.load()
        if task_description != policy.task_description:
            policy.reset(task_description)
        policy.set_episode_context(task_id, episode_index, global_episode_index)
        action = policy.step(self._agentview_image(obs), task_description, obs).astype(np.float32)
        decision = dict(policy._last_control_decision)
        return action, decision

    def observe_only(
        self,
        obs: dict[str, np.ndarray],
        task_description: str,
        task_id: int,
        episode_index: int,
        global_episode_index: int,
    ) -> None:
        """Update the world-model temporal context without querying or executing it."""
        policy = self.load()
        if task_description != policy.task_description:
            policy.reset(task_description)
        policy.set_episode_context(task_id, episode_index, global_episode_index)
        policy._add_image_to_history(policy._process_image(self._agentview_image(obs)))
        policy._add_lowdim_to_history(policy._state_from_observation(obs))

    def first_action_from_current_history(self, task_description: str) -> tuple[np.ndarray, dict[str, Any]]:
        """Query/consume the first WM action using the already-shadowed current observation."""
        policy = self.load()
        if task_description != policy.task_description:
            raise RuntimeError("World-model shadow history was not initialized for the requested task.")
        if policy.action_buffer is None:
            policy._query_policy(task_description)
        current_action = policy.action_buffer[policy.action_buffer_idx]
        policy.action_buffer_idx += 1
        if policy.action_buffer_idx >= policy._execute_horizon:
            policy._previous_action_chunk = policy.action_buffer.copy()
            policy._previous_execute_horizon = policy._execute_horizon
            policy.action_buffer = None
        decision = dict(policy._last_control_decision)
        return policy._convert_action(current_action).astype(np.float32), decision


def _validate_config(cfg: dict[str, Any]) -> None:
    required_top = {"simvla_bundle_root", "simvla", "world_model", "arbiter", "output_dir"}
    missing = sorted(required_top - set(cfg))
    if missing:
        raise RuntimeError(f"Arbiter config missing top-level keys: {missing}")

    simvla_required = {
        "checkpoint",
        "risk_model_unc_topk8_dir",
        "simvla_root",
        "libero_pro_root",
        "norm_stats",
        "smolvlm_path",
        "suite",
        "task_id",
        "global_action_seed",
        "model_load_seed",
        "device",
        "execution_horizon",
        "ace_candidate_count",
        "history_steps",
        "image_size",
        "resolution",
        "env_camera_height",
        "env_camera_width",
        "simvla_input_height",
        "simvla_input_width",
        "model_denoise_steps",
        "max_steps",
        "warmup",
        "selection_min_margin",
        "selection_strong_margin",
        "selection_max_first_action_l2",
        "selection_main_threshold",
        "selection_require_candidate_below_q95",
        "expected_topk8_dims",
        "episode_manifest_csv",
        "language_prompt_source",
        "reset_seeds",
    }
    missing = sorted(simvla_required - set(cfg["simvla"]))
    if missing:
        raise RuntimeError(f"simvla config missing keys: {missing}")

    wm_required = {
        "experiment",
        "video_model",
        "action_model",
        "dataset_statistics",
        "v2w_uncertainty_head",
        "v2w_calibration",
        "uq_risk_model_dir",
        "uq_risk_threshold",
        "img_horizon",
        "lowdim_horizon",
        "stop_video_denoising_step",
        "num_execute_actions",
        "num_sampling_steps",
        "use_text_encoder",
        "uq_num_action_candidates",
        "uq_action_candidate_batch_size",
        "uq_num_world_candidates",
        "uq_save_candidate_arrays",
        "v2w_uncertainty_variant",
        "v2w_uncertainty_save_variance_arrays",
        "uq_control_policy",
        "uq_risk_medium_threshold",
        "uq_risk_persistence",
        "uq_risk_medium_execute_actions",
        "uq_risk_high_execute_actions",
        "uq_risk_score_semantics",
    }
    missing = sorted(wm_required - set(cfg["world_model"]))
    if missing:
        raise RuntimeError(f"world_model config missing keys: {missing}")

    arbiter_required = {
        "policy",
        "simvla_trigger_threshold",
        "simvla_high_risk_streak",
        "simvla_risk_score_source",
        "world_model_low_risk_execute_actions",
        "both_high_execute_actions",
        "max_fallback_calls_per_episode",
        "shadow_world_model",
    }
    missing = sorted(arbiter_required - set(cfg["arbiter"]))
    if missing:
        raise RuntimeError(f"arbiter config missing keys: {missing}")

    sim = cfg["simvla"]
    if int(sim["execution_horizon"]) != 10:
        raise RuntimeError("This arbiter expects normal SimVLA execution_horizon=10.")
    if int(sim["ace_candidate_count"]) != 8:
        raise RuntimeError("This arbiter expects SimVLA ace_candidate_count=8.")
    if int(sim["model_denoise_steps"]) != 10:
        raise RuntimeError("This arbiter expects SimVLA model_denoise_steps=10.")

    wm = cfg["world_model"]
    wm_control_policy = str(wm["uq_control_policy"])
    if wm_control_policy not in {
        "calibrator_adaptive_horizon",
        "action_medoid",
        "action_medoid_calibrator_adaptive_horizon",
    }:
        raise RuntimeError(
            "world_model.uq_control_policy must be calibrator_adaptive_horizon, "
            "action_medoid, or action_medoid_calibrator_adaptive_horizon."
        )
    risk_policy_names = {
        "calibrator_adaptive_horizon",
        "action_medoid_calibrator_adaptive_horizon",
    }
    if wm_control_policy not in risk_policy_names and bool(cfg["arbiter"].get("world_model_risk_gate", True)):
        raise RuntimeError(
            "Non-calibrator world-model control requires arbiter.world_model_risk_gate=false. "
            "This avoids silently treating a missing world-model risk score as low risk."
        )
    if int(wm["uq_num_action_candidates"]) != 8:
        raise RuntimeError("world_model.uq_num_action_candidates must be 8 for the trained full-UQ calibrator.")
    if int(wm["uq_num_world_candidates"]) != 3:
        raise RuntimeError("world_model.uq_num_world_candidates must be 3 for the trained full-UQ calibrator.")

    policy = str(cfg["arbiter"]["policy"])
    if policy not in ARBITER_POLICIES:
        raise RuntimeError(f"Unknown arbiter.policy={policy!r}; expected one of {sorted(ARBITER_POLICIES)}.")
    risk_score_source = str(cfg["arbiter"]["simvla_risk_score_source"])
    if risk_score_source not in {"main", "selected"}:
        raise RuntimeError("arbiter.simvla_risk_score_source must be either 'main' or 'selected'.")
    if policy == DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY:
        if risk_score_source != "main":
            raise RuntimeError(f"{DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY} requires arbiter.simvla_risk_score_source='main'.")
        if cfg["arbiter"]["simvla_trigger_threshold"] != "q95":
            raise RuntimeError(f"{DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY} requires the calibrated q95 SimVLA threshold.")
    prompt_source = str(cfg["simvla"]["language_prompt_source"])
    if prompt_source != "registered":
        raise RuntimeError("simvla.language_prompt_source must be 'registered'.")
    if policy == WM_PREFIX_LOW_RISK_SIMVLA_POLICY:
        prefix_keys = {"min_simvla_query_index"}
        missing = sorted(prefix_keys - set(cfg["arbiter"]))
        if missing:
            raise RuntimeError(f"{WM_PREFIX_LOW_RISK_SIMVLA_POLICY} config missing keys: {missing}")
        if int(cfg["arbiter"]["min_simvla_query_index"]) < 0:
            raise RuntimeError("arbiter.min_simvla_query_index must be non-negative.")
    _validate_world_model_risk_label(cfg)


def _validate_world_model_risk_label(cfg: dict[str, Any]) -> None:
    if not _uses_world_model(_arbiter_policy(cfg)):
        return
    metadata_path = _resolve_path(cfg["world_model"]["uq_risk_model_dir"], base=ROOT) / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(metadata_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    label_column = str(metadata.get("label_column", ""))
    if label_column != "failure_label":
        raise RuntimeError(
            "World-model risk control only accepts models trained on episode-level failure_label. "
            f"Got label_column={label_column!r} from {metadata_path}."
        )


def _arbiter_policy(cfg: dict[str, Any]) -> str:
    return str(cfg["arbiter"]["policy"])


def _uses_simvla_risk(policy_name: str) -> bool:
    return policy_name in SIMVLA_RISK_POLICIES


def _uses_world_model(policy_name: str) -> bool:
    return policy_name in WORLD_MODEL_POLICIES


def _uses_main_risk_simvla_medoid(policy_name: str) -> bool:
    return policy_name == DUAL_MAIN_RISK_SIMVLA_MEDOID_POLICY


def _forces_world_model_prefix(policy_name: str, cfg: dict[str, Any], query_index: int) -> bool:
    if policy_name != WM_PREFIX_LOW_RISK_SIMVLA_POLICY:
        return False
    return query_index < int(cfg["arbiter"]["min_simvla_query_index"])


def _executes_world_model_actions(branch: str) -> bool:
    return branch in WORLD_MODEL_ACTION_BRANCHES


def _simvla_trigger_score(cfg: dict[str, Any], main_score: float, selected_score: float) -> float:
    source = str(cfg["arbiter"]["simvla_risk_score_source"])
    return main_score if source == "main" else selected_score


def _world_model_risk_probability(decision: dict[str, Any]) -> float:
    if "risk_probability" not in decision:
        raise RuntimeError(
            "World-model calibrator did not return risk_probability. "
            "Refusing to arbitrate from a missing thresholded risk score."
        )
    return float(decision["risk_probability"])


def _world_model_low_risk(decision: dict[str, Any], threshold: float) -> bool:
    return _world_model_risk_probability(decision) <= float(threshold)


def _action_medoid_index(chunks_normalized: np.ndarray) -> int:
    chunks = np.asarray(chunks_normalized, dtype=np.float32)
    if chunks.ndim != 3 or chunks.shape[0] < 2:
        raise RuntimeError(f"Expected at least two action chunks shaped [N,T,A], got {chunks.shape}.")
    flat = chunks.reshape(chunks.shape[0], -1)
    distances = np.linalg.norm(flat[:, None, :] - flat[None, :, :], axis=-1)
    return int(np.argmin(distances.mean(axis=1)))


def _resize_uint8_image(image: np.ndarray, height: int, width: int) -> np.ndarray:
    if image.dtype != np.uint8:
        raise ValueError(f"Expected uint8 image before SimVLA resize, got {image.dtype}.")
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError(f"Expected HWC RGB image before SimVLA resize, got shape {image.shape}.")
    if image.shape[0] == height and image.shape[1] == width:
        return image
    return np.asarray(Image.fromarray(image).resize((width, height), Image.Resampling.BICUBIC), dtype=np.uint8)


def _simvla_obs_images(api: dict[str, Any], obs: dict[str, Any], height: int, width: int) -> tuple[np.ndarray, np.ndarray]:
    _validate_simvla_observation(obs)
    agentview, wrist = api["obs_images"](obs)
    return _resize_uint8_image(agentview, height, width), _resize_uint8_image(wrist, height, width)


def _validate_simvla_observation(obs: dict[str, Any]) -> None:
    image_keys = ("agentview_image", "robot0_eye_in_hand_image")
    vector_keys = ("robot0_eef_pos", "robot0_eef_quat", "robot0_gripper_qpos")
    missing = [key for key in (*image_keys, *vector_keys) if key not in obs]
    if missing:
        raise RuntimeError(f"LIBERO observation is missing required SimVLA keys: {missing}")
    for key in image_keys:
        value = np.asarray(obs[key])
        if value.dtype != np.uint8 or value.ndim != 3 or value.shape[2] != 3:
            raise RuntimeError(f"Observation {key} must be uint8 HWC RGB, got dtype={value.dtype}, shape={value.shape}")
    expected_widths = {"robot0_eef_pos": 3, "robot0_eef_quat": 4, "robot0_gripper_qpos": 2}
    for key, width in expected_widths.items():
        value = np.asarray(obs[key])
        if value.shape[-1] != width:
            raise RuntimeError(f"Observation {key} must have trailing dimension {width}, got shape={value.shape}")


def _load_arbiter_episode_specs(api: dict[str, Any], sim: dict[str, Any]) -> list[dict[str, Any]] | None:
    manifest = sim["episode_manifest_csv"]
    path = _resolve_path(manifest, base=ROOT)
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise RuntimeError(f"episode manifest is empty: {path}")

    if {"bddl_relative_path", "init_state_file_relative_path", "bddl_sha256", "init_state_file_sha256"} <= set(rows[0]):
        return api["load_episode_specs"](sim)

    required = {"episode_uid", "task_suite_name", "task_id", "initial_state_index", "eval_seed", "task_description"}
    missing = required - set(rows[0])
    if missing:
        raise RuntimeError(f"{path} is missing required columns for lightweight episode specs: {sorted(missing)}")
    order_key = "selected_manifest_order" if "selected_manifest_order" in rows[0] else "execution_order_in_run"
    rows.sort(key=lambda row: int(row[order_key]))
    specs = []
    seen: set[tuple[str, int, int, int]] = set()
    seen_uids: set[str] = set()
    for idx, row in enumerate(rows):
        suite = str(row["task_suite_name"])
        task_id = int(row["task_id"])
        init_idx = int(row["initial_state_index"])
        eval_seed = int(row["eval_seed"])
        episode_uid = str(row["episode_uid"])
        if episode_uid in seen_uids:
            raise RuntimeError(f"duplicate episode_uid in {path}: {episode_uid}")
        seen_uids.add(episode_uid)
        key = (suite, task_id, init_idx, eval_seed)
        if key in seen:
            raise RuntimeError(f"duplicate episode identity in {path}: {key}")
        seen.add(key)
        specs.append(
            {
                "manifest_row_index": idx,
                "episode_uid": episode_uid,
                "suite": suite,
                "task_id": task_id,
                "initial_state_index": init_idx,
                "eval_seed": eval_seed,
                "instruction": str(row["task_description"]),
                "source_manifest": str(path),
            }
        )
    return specs


def _make_env_for_episode(
    api: dict[str, Any],
    cfg: dict[str, Any],
    benchmark_dict: dict[str, Any],
    get_libero_path_fn: Any,
    offscreen_cls: Any,
    episode_index: int,
    reset_seed: int,
    episode_spec: dict[str, Any] | None,
) -> tuple[Any, dict[str, Any], str, int, str]:
    sim = cfg["simvla"]
    camera_height = int(sim["env_camera_height"])
    camera_width = int(sim["env_camera_width"])
    suite = str(episode_spec["suite"] if episode_spec else sim["suite"])
    task_id = int(episode_spec["task_id"] if episode_spec else sim["task_id"])
    episode_uid = str(
        episode_spec["episode_uid"] if episode_spec else f"{suite}::task{task_id:02d}::episode{episode_index:05d}"
    )
    if episode_spec and "bddl_path" in episode_spec:
        bench = benchmark_dict[suite]()
        task = bench.get_task(task_id)
        env = offscreen_cls(
            bddl_file_name=str(episode_spec["bddl_path"]),
            camera_heights=camera_height,
            camera_widths=camera_width,
        )
        if not hasattr(env, "seed"):
            raise RuntimeError("LIBERO environment does not expose seed().")
        env.seed(int(episode_spec["eval_seed"]))
        init_states = torch.load(episode_spec["init_state_path"], map_location="cpu", weights_only=False)
        init_state_idx = int(episode_spec["initial_state_index"])
        if init_state_idx < 0 or init_state_idx >= len(init_states):
            raise RuntimeError(
                f"initial_state_index={init_state_idx} out of range for {suite} task {task_id}; "
                f"available={len(init_states)}"
            )
        obs = env.reset()
        obs = env.set_init_state(init_states[init_state_idx])
        for _ in range(int(sim["warmup"])):
            obs, _, _, _ = env.step(np.asarray([0, 0, 0, 0, 0, 0, -1], dtype=np.float32))
        lang = str(task.language)
        return env, obs, lang, task_id, episode_uid

    if episode_spec:
        bench = benchmark_dict[suite]()
        task = bench.get_task(task_id)
        bddl_root = Path(get_libero_path_fn("bddl_files"))
        init_root = Path(get_libero_path_fn("init_states"))
        folder_candidates = [task.problem_folder]
        if task.problem_folder == "libero_spatial_object":
            folder_candidates.append("libero_spatial")
        bddl_path = None
        init_states_path = None
        for folder in folder_candidates:
            candidate_bddl = bddl_root / folder / task.bddl_file
            candidate_init = init_root / folder / task.init_states_file
            if candidate_bddl.exists() and candidate_init.exists():
                bddl_path = candidate_bddl
                init_states_path = candidate_init
                break
        if bddl_path is None or init_states_path is None:
            raise FileNotFoundError(
                f"could not resolve BDDL/init files for {suite} task {task_id}: "
                f"bddl={task.bddl_file}, init={task.init_states_file}, folders={folder_candidates}"
            )
        env = offscreen_cls(
            bddl_file_name=str(bddl_path),
            camera_heights=camera_height,
            camera_widths=camera_width,
        )
        if not hasattr(env, "seed"):
            raise RuntimeError("LIBERO environment does not expose seed().")
        env.seed(int(episode_spec["eval_seed"]))
        init_states = torch.load(init_states_path, map_location="cpu", weights_only=False)
        init_state_idx = int(episode_spec["initial_state_index"])
        if init_state_idx < 0 or init_state_idx >= len(init_states):
            raise RuntimeError(
                f"initial_state_index={init_state_idx} out of range for {suite} task {task_id}; "
                f"available={len(init_states)}"
            )
        obs = api["reset_to_init"](env, init_states[init_state_idx], int(sim["warmup"]))
        registered_lang = str(task.language)
        lang = registered_lang
        return env, obs, lang, task_id, episode_uid

    env, bundle = api["make_env"](
        benchmark_dict,
        get_libero_path_fn,
        offscreen_cls,
        suite,
        task_id,
        camera_height,
        int(reset_seed),
    )
    init_states = bundle["init_states"]
    init_state_idx = int(reset_seed) % len(init_states)
    obs = api["reset_to_init"](env, init_states[init_state_idx], int(sim["warmup"]))
    return env, obs, str(bundle["task"].language), task_id, episode_uid


def run_episode(
    *,
    api: dict[str, Any],
    cfg: dict[str, Any],
    detector: Any,
    episode_index: int,
    reset_seed: int,
    simvla_model: Any,
    processor: Any,
    image_preprocessor: Any,
    benchmark_dict: dict[str, Any],
    get_libero_path_fn: Any,
    offscreen_cls: Any,
    device: torch.device,
    state_mean: np.ndarray | None,
    state_std: np.ndarray | None,
    out_dir: Path,
    wm_fallback: LazyWorldModelFallback,
    episode_spec: dict[str, Any] | None = None,
) -> dict[str, Any]:
    sim = cfg["simvla"]
    suite_name = str(episode_spec["suite"] if episode_spec else sim["suite"])
    env = None
    start = time.perf_counter()
    rows_path = out_dir / "arbiter_step_scores.jsonl"
    history: deque[tuple[np.ndarray, np.ndarray, np.ndarray]] = deque(maxlen=int(sim["history_steps"]))
    selected_scores: list[float] = []
    simvla_trigger_scores: list[float] = []
    world_model_risk_scores: list[float] = []
    fallback_calls = 0
    wm_accepted = 0
    wm_rejected = 0
    success = False
    done = False
    num_steps = 0
    query_index = 0
    high_risk_streak = 0
    previous_action = None
    previous_proprio = None
    try:
        env, obs, lang, task_id, episode_uid = _make_env_for_episode(
            api,
            cfg,
            benchmark_dict,
            get_libero_path_fn,
            offscreen_cls,
            episode_index,
            reset_seed,
            episode_spec,
        )
        wm_fallback.reset_episode(lang, task_id, episode_index, episode_index)
        lang_t = processor.encode_language([lang])
        lang_t = {key: value.to(device) for key, value in lang_t.items()}
        max_steps = int(sim["max_steps"])
        simvla_horizon = int(sim["execution_horizon"])
        simvla_input_height = int(sim["simvla_input_height"])
        simvla_input_width = int(sim["simvla_input_width"])
        policy_name = _arbiter_policy(cfg)
        wm_low_horizon = int(cfg["arbiter"]["world_model_low_risk_execute_actions"])
        both_high_horizon = int(cfg["arbiter"]["both_high_execute_actions"])
        max_fallback_calls = int(cfg["arbiter"]["max_fallback_calls_per_episode"])
        use_simvla_risk = _uses_simvla_risk(policy_name)
        trigger_name = cfg["arbiter"]["simvla_trigger_threshold"]
        trigger_threshold = api["resolve_score_threshold"](trigger_name, detector) if use_simvla_risk else None
        shadow_world_model = _uses_world_model(policy_name) and bool(cfg["arbiter"]["shadow_world_model"])
        if shadow_world_model:
            wm_fallback.load()
            wm_fallback.reset_episode(lang, task_id, episode_index, episode_index)

        while num_steps < max_steps and not success:
            query_started = time.perf_counter()
            timestep = num_steps
            current_obs_shadowed = False
            if shadow_world_model:
                wm_fallback.observe_only(obs, lang, task_id, episode_index, episode_index)
                current_obs_shadowed = True
            proprio_np = api["obs_to_proprio"](obs)
            before_img, before_wrist = _simvla_obs_images(api, obs, simvla_input_height, simvla_input_width)
            images_t, mask_t = image_preprocessor(before_img, before_wrist, device)
            proprio_t = torch.as_tensor(proprio_np, dtype=torch.float32, device=device).unsqueeze(0)
            n_samples = 1 + int(sim["ace_candidate_count"]) if use_simvla_risk else 1
            seeds = api["action_seeds_for_step"](
                int(sim["global_action_seed"]),
                int(reset_seed),
                int(episode_index),
                query_index,
                n_samples,
            )
            main_candidates = api["generate_candidates_with_uncertainty"](
                model=simvla_model,
                input_ids=lang_t["input_ids"],
                image_input=images_t,
                image_mask=mask_t,
                proprio=proprio_t,
                seeds=[seeds[0]],
                steps=int(sim["model_denoise_steps"]),
                previous_action=previous_action,
                previous_proprio=previous_proprio,
                state_mean=state_mean,
                state_std=state_std,
            )
            if use_simvla_risk:
                ace_candidates = api["generate_candidates_with_uncertainty"](
                    model=simvla_model,
                    input_ids=lang_t["input_ids"],
                    image_input=images_t,
                    image_mask=mask_t,
                    proprio=proprio_t,
                    seeds=seeds[1:],
                    steps=int(sim["model_denoise_steps"]),
                    previous_action=previous_action,
                    previous_proprio=previous_proprio,
                    state_mean=state_mean,
                    state_std=state_std,
                )
                candidates = api["combine_main_and_ace_batches"](main_candidates, ace_candidates)
            else:
                candidates = main_candidates
            ace = api["compute_ace_metrics"](candidates.chunks_norm[1:])
            hist = api["history_array"](history, int(sim["history_steps"]))
            if use_simvla_risk:
                if _uses_main_risk_simvla_medoid(policy_name):
                    score_arr = api["score_candidates"](
                        detector,
                        hist,
                        candidates.chunks_norm[:1],
                        ace,
                        proprio_np,
                        candidates.features_49d[:1],
                        device,
                    )
                    proposed_idx = _action_medoid_index(candidates.chunks_norm)
                    selection_reason = "simvla_action_medoid_with_main_only_risk"
                else:
                    score_arr = api["score_candidates"](
                        detector,
                        hist,
                        candidates.chunks_norm,
                        ace,
                        proprio_np,
                        candidates.features_49d,
                        device,
                    )
                    action_l2 = api["candidate_first_action_l2"](candidates.chunks_norm)
                    proposed_idx, selection_reason = api["select_action"](
                        score_arr,
                        detector,
                        float(sim["selection_min_margin"]),
                        float(sim["selection_strong_margin"]),
                        action_l2=action_l2,
                        max_action_l2=(
                            None
                            if sim["selection_max_first_action_l2"] is None
                            else float(sim["selection_max_first_action_l2"])
                        ),
                        main_threshold=sim["selection_main_threshold"],
                        require_candidate_below_q95=bool(sim["selection_require_candidate_below_q95"]),
                    )
            else:
                score_arr = None
                proposed_idx = 0
                selected_idx = 0
                selection_reason = "arbiter_policy_simvla_main"
            if use_simvla_risk:
                selected_idx = int(proposed_idx)
                main_score = float(score_arr[0])
                selected_score = main_score if _uses_main_risk_simvla_medoid(policy_name) else float(score_arr[selected_idx])
                selected_scores.append(selected_score)
                trigger_score = _simvla_trigger_score(cfg, main_score, selected_score)
                simvla_trigger_scores.append(trigger_score)
                if trigger_threshold is None:
                    raise RuntimeError("SimVLA risk policy has no resolved trigger threshold.")
                high_risk_streak = high_risk_streak + 1 if trigger_score >= trigger_threshold else 0
            else:
                selected_score = None
                main_score = None
                trigger_score = None
                high_risk_streak = 0
            force_world_model_prefix = _forces_world_model_prefix(policy_name, cfg, query_index)
            risk_triggered = high_risk_streak >= int(cfg["arbiter"]["simvla_high_risk_streak"])
            fallback_triggered = (
                _uses_world_model(policy_name)
                and (force_world_model_prefix or risk_triggered)
                and fallback_calls < max_fallback_calls
            )
            branch = "simvla"
            wm_decision: dict[str, Any] = {}
            selected_chunk = candidates.chunks_env[selected_idx]
            execute_horizon = simvla_horizon
            wm_first_action: np.ndarray | None = None

            if fallback_triggered:
                fallback_calls += 1
                if shadow_world_model:
                    wm_first_action, wm_decision = wm_fallback.first_action_from_current_history(lang)
                else:
                    wm_first_action, wm_decision = wm_fallback.first_action_and_decision(
                        obs,
                        lang,
                        task_id,
                        episode_index,
                        episode_index,
                    )
                use_world_model_risk_gate = bool(cfg["arbiter"].get("world_model_risk_gate", True))
                if use_world_model_risk_gate:
                    wm_threshold = float(cfg["world_model"]["uq_risk_threshold"])
                    wm_risk = _world_model_risk_probability(wm_decision)
                    world_model_risk_scores.append(wm_risk)
                else:
                    if "risk_probability" in wm_decision:
                        raise RuntimeError(
                            "arbiter.world_model_risk_gate=false but world-model decision still contains "
                            "risk_probability. Use the calibrator-gated config for that experiment."
                        )
                    wm_threshold = None
                    wm_risk = None

                if not use_world_model_risk_gate or _world_model_low_risk(wm_decision, wm_threshold):
                    branch = "world_model"
                    selected_chunk = np.empty((0,), dtype=np.float32)
                    execute_horizon = min(
                        wm_low_horizon,
                        int(wm_decision["selected_execute_horizon"]),
                    )
                    wm_accepted += 1
                else:
                    branch = "both_high_short_world_model"
                    selected_chunk = np.empty((0,), dtype=np.float32)
                    execute_horizon = min(both_high_horizon, int(wm_decision["selected_execute_horizon"]))
                    wm_rejected += 1

            first_executed_action = None
            last_action = None
            last_pre_proprio = proprio_np
            actions_executed = 0
            reward = 0.0
            uses_world_model_actions = _executes_world_model_actions(branch)
            max_branch_actions = (
                execute_horizon
                if uses_world_model_actions
                else min(execute_horizon, len(selected_chunk))
            )
            planning_seconds = time.perf_counter() - query_started
            execution_started = time.perf_counter()
            for action_index in range(max_branch_actions):
                pre_proprio = api["obs_to_proprio"](obs)
                if uses_world_model_actions:
                    if action_index == 0:
                        if wm_first_action is None:
                            raise RuntimeError("world_model branch selected without a first WM action")
                        action = wm_first_action.astype(np.float32)
                    else:
                        wm_policy = wm_fallback.policy
                        if wm_policy is None:
                            raise RuntimeError("world_model branch lost its loaded policy")
                        action = wm_policy.step(
                            LazyWorldModelFallback._agentview_image(obs),
                            lang,
                            obs,
                        ).astype(np.float32)
                else:
                    if shadow_world_model and not (action_index == 0 and current_obs_shadowed):
                        wm_fallback.observe_only(obs, lang, task_id, episode_index, episode_index)
                    action = selected_chunk[action_index].astype(np.float32)
                if first_executed_action is None:
                    first_executed_action = action.copy()
                obs, reward, done, _info = env.step(action)
                success = success or bool(float(reward) > 0.0) or bool(api["check_success"](env))
                last_action = action
                last_pre_proprio = pre_proprio
                actions_executed += 1
                num_steps += 1
                if done or success or num_steps >= max_steps:
                    break
            execution_seconds = time.perf_counter() - execution_started
            if first_executed_action is None or last_action is None:
                raise RuntimeError("arbiter executed zero actions")
            history.append((proprio_np, first_executed_action, ace))
            previous_action = last_action
            previous_proprio = last_pre_proprio

            _append_jsonl(
                rows_path,
                {
                    "schema_version": "simvla_wm_arbiter_step_v1",
                    "arbiter_policy": policy_name,
                    "episode_index": int(episode_index),
                    "episode_uid": episode_uid,
                    "task_suite_name": suite_name,
                    "task_id": int(task_id),
                    "query_index": int(query_index),
                    "timestep": int(timestep),
                    "branch": branch,
                    "simvla_trigger_threshold_name": trigger_name,
                    "simvla_trigger_threshold": None if trigger_threshold is None else float(trigger_threshold),
                    "simvla_trigger_score_source": str(cfg["arbiter"]["simvla_risk_score_source"]),
                    "simvla_trigger_score": None if trigger_score is None else float(trigger_score),
                    "simvla_main_score": main_score,
                    "simvla_selected_score": selected_score,
                    "simvla_candidate_scores": None if score_arr is None else [float(x) for x in score_arr.tolist()],
                    "simvla_selected_candidate_index": int(selected_idx),
                    "simvla_proposed_candidate_index": int(proposed_idx),
                    "simvla_selection_reason": selection_reason,
                    "fallback_triggered": bool(fallback_triggered),
                    "force_world_model_prefix": bool(force_world_model_prefix),
                    "wm_decision": wm_decision,
                    "wm_risk_score_semantics": str(
                        cfg["world_model"]["uq_risk_score_semantics"]
                    ),
                    "wm_risk_threshold": (
                        float(cfg["world_model"]["uq_risk_threshold"])
                        if bool(cfg["arbiter"].get("world_model_risk_gate", True))
                        else None
                    ),
                    "selected_execute_horizon": int(execute_horizon),
                    "actions_executed_from_chunk": int(actions_executed),
                    "planning_wall_time_seconds": float(planning_seconds),
                    "execution_wall_time_seconds": float(execution_seconds),
                    "query_wall_time_seconds": float(planning_seconds + execution_seconds),
                    "success_after_step": bool(success),
                    "reward": float(reward),
                    "done": bool(done),
                    "main_chunk_sha256": api["sha256_array"](candidates.chunks_env[0]),
                    "selected_simvla_chunk_sha256": api["sha256_array"](candidates.chunks_env[selected_idx]),
                },
            )
            query_index += 1
            if done or success:
                break
    finally:
        if env is not None:
            env.close()

    outcome = "success" if success else "failure"
    return {
        "schema_version": "simvla_wm_arbiter_episode_v1",
        "episode_index": int(episode_index),
        "episode_uid": episode_uid,
        "task_suite_name": suite_name,
        "task_id": int(task_id),
        "arbiter_policy": _arbiter_policy(cfg),
        "outcome": outcome,
        "success": bool(success),
        "num_steps": int(num_steps),
        "num_queries": int(query_index),
        "fallback_calls": int(fallback_calls),
        "wm_accepted": int(wm_accepted),
        "wm_rejected": int(wm_rejected),
        "selected_risk_min": float(np.min(selected_scores)) if selected_scores else None,
        "selected_risk_mean": float(np.mean(selected_scores)) if selected_scores else None,
        "selected_risk_max": float(np.max(selected_scores)) if selected_scores else None,
        "simvla_trigger_risk_min": float(np.min(simvla_trigger_scores)) if simvla_trigger_scores else None,
        "simvla_trigger_risk_mean": float(np.mean(simvla_trigger_scores)) if simvla_trigger_scores else None,
        "simvla_trigger_risk_max": float(np.max(simvla_trigger_scores)) if simvla_trigger_scores else None,
        "world_model_risk_min": float(np.min(world_model_risk_scores)) if world_model_risk_scores else None,
        "world_model_risk_mean": float(np.mean(world_model_risk_scores)) if world_model_risk_scores else None,
        "world_model_risk_max": float(np.max(world_model_risk_scores)) if world_model_risk_scores else None,
        "wall_time_seconds": float(time.perf_counter() - start),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("SimVLA default executor with lazy world-model fallback")
    parser.add_argument("--config", required=True)
    parser.add_argument("--num-episodes", type=int, default=None)
    parser.add_argument("--episode-start", type=int, default=0)
    parser.add_argument("--episode-end", type=int, default=None)
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    process_started_at = time.perf_counter()
    args = parse_args()
    cfg_path = Path(args.config).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    _validate_config(cfg)
    bundle_root = _resolve_path(cfg["simvla_bundle_root"], base=ROOT)
    api = _load_simvla_api(bundle_root)
    sim = cfg["simvla"]
    out_dir = _resolve_path(cfg["output_dir"], base=ROOT)
    policy_name = _arbiter_policy(cfg)
    use_simvla_risk = _uses_simvla_risk(policy_name)
    use_world_model = _uses_world_model(policy_name)
    if args.validate_only:
        required_paths = [
            _resolve_path(sim["checkpoint"], base=bundle_root) / "model.safetensors",
            _resolve_path(sim["norm_stats"], base=bundle_root),
        ]
        if use_simvla_risk:
            required_paths.append(_resolve_path(sim["risk_model_unc_topk8_dir"], base=bundle_root) / "model.pt")
        if use_world_model:
            required_paths.extend(
                [
                    _resolve_path(cfg["world_model"]["video_model"], base=ROOT),
                    _resolve_path(cfg["world_model"]["action_model"], base=ROOT),
                    _resolve_path(cfg["world_model"]["dataset_statistics"], base=ROOT),
                    _resolve_path(cfg["world_model"]["v2w_uncertainty_head"], base=ROOT),
                    _resolve_path(cfg["world_model"]["v2w_calibration"], base=ROOT),
                    _resolve_path(cfg["world_model"]["uq_risk_model_dir"], base=ROOT) / "model.pt",
                ]
            )
        missing = [str(path) for path in required_paths if not path.exists()]
        if missing:
            raise FileNotFoundError("Missing required arbiter artifacts: " + json.dumps(missing, indent=2))
        print(f"VALIDATE_ONLY passed: config={cfg_path} out_dir={out_dir}")
        return

    if bool(cfg.get("require_empty_output_dir", False)) and out_dir.exists() and any(out_dir.iterdir()):
        raise RuntimeError(f"Campaign output directory must be empty: {out_dir}")

    api["setup_runtime"](_resolve_path(sim["simvla_root"], base=bundle_root), _resolve_path(sim["libero_pro_root"], base=bundle_root))
    from libero.libero import benchmark, get_libero_path  # pylint: disable=import-outside-toplevel
    from libero.libero.envs import OffScreenRenderEnv  # pylint: disable=import-outside-toplevel
    from models.modeling_smolvlm_vla import SmolVLMVLA  # pylint: disable=import-outside-toplevel
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor  # pylint: disable=import-outside-toplevel

    torch.set_float32_matmul_precision("highest")
    if torch.cuda.is_available():
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
    torch.use_deterministic_algorithms(True)
    device = torch.device(sim["device"])
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("SimVLA configuration requires CUDA, but no CUDA device is available.")
    api["set_all_seeds"](int(sim["model_load_seed"]))

    checkpoint = _resolve_path(sim["checkpoint"], base=bundle_root)
    risk_dir = _resolve_path(sim["risk_model_unc_topk8_dir"], base=bundle_root)
    norm_stats = _resolve_path(sim["norm_stats"], base=bundle_root)
    smolvlm_path = _resolve_path_or_model_id(sim["smolvlm_path"], base=bundle_root)
    required_paths = [checkpoint / "model.safetensors", norm_stats]
    if use_simvla_risk:
        required_paths.append(risk_dir / "model.pt")
    for path in required_paths:
        if not path.exists():
            raise FileNotFoundError(path)

    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[startup] loading SimVLA checkpoint={checkpoint}", flush=True)
    simvla_model = SmolVLMVLA.from_pretrained(str(checkpoint)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(smolvlm_path)
    simvla_model.action_space.load_norm_stats(str(norm_stats))
    if use_simvla_risk and not bool(simvla_model.config.predict_uncertainty):
        raise RuntimeError("SimVLA fallback arbiter requires a predict_uncertainty=True checkpoint.")
    state_mean, state_std = api["load_state_stats"](simvla_model, norm_stats)
    image_preprocessor = api["ImagePreprocessor"](int(sim["image_size"]))
    detector = None
    if use_simvla_risk:
        detector = api["load_detector"]("unc_topk8", risk_dir, device)
        expected_dims = [int(x) for x in sim["expected_topk8_dims"]]
        if detector.static_dim != 51 or detector.selected_uncertainty_dims != expected_dims:
            raise RuntimeError(
                f"Top-8 detector identity mismatch: static_dim={detector.static_dim}, "
                f"dims={detector.selected_uncertainty_dims}, expected={expected_dims}"
            )

    benchmark_dict = benchmark.get_benchmark_dict()
    episode_specs = _load_arbiter_episode_specs(api, sim)
    expected_episode_count = cfg.get("expected_episode_count")
    if expected_episode_count is not None and len(episode_specs) != int(expected_episode_count):
        raise RuntimeError(
            f"Expected {int(expected_episode_count)} manifest episodes, got {len(episode_specs)}."
        )
    seeds = [int(x["eval_seed"]) for x in episode_specs]
    start = int(args.episode_start)
    end = args.episode_end if args.episode_end is not None else len(seeds)
    if args.num_episodes is not None:
        end = min(end, start + int(args.num_episodes))
    if args.smoke:
        end = min(end, start + 1)
    selected = list(range(start, min(end, len(seeds))))
    if expected_episode_count is not None and (start != 0 or len(selected) != int(expected_episode_count)):
        raise RuntimeError(
            "Campaign configs must execute the complete manifest in one invocation: "
            f"start={start}, selected={len(selected)}, expected={int(expected_episode_count)}."
        )
    wm_fallback = LazyWorldModelFallback(cfg["world_model"], out_dir)

    setup_wall_seconds = time.perf_counter() - process_started_at
    rollout_started_at = time.perf_counter()

    _write_json(
        out_dir / "run_manifest.json",
        {
            "schema_version": "simvla_wm_arbiter_manifest_v1",
            "config": str(cfg_path),
            "bundle_root": str(bundle_root),
            "simvla_checkpoint": str(checkpoint),
            "simvla_checkpoint_sha256": _sha256_file(checkpoint / "model.safetensors"),
            "simvla_risk_model": str(risk_dir) if use_simvla_risk else None,
            "uses_world_model": use_world_model,
            "world_model": cfg["world_model"],
            "episode_indices": selected,
            "runner_sha256": _sha256_file(Path(__file__)),
            "episode_manifest_sha256": _sha256_file(
                _resolve_path(sim["episode_manifest_csv"], base=ROOT)
            ),
            "setup_wall_seconds": setup_wall_seconds,
        },
    )

    summaries_path = out_dir / "episode_summaries.jsonl"
    counts: Counter[str] = Counter()
    for ep_idx in selected:
        summary = run_episode(
            api=api,
            cfg=cfg,
            detector=detector,
            episode_index=ep_idx,
            reset_seed=seeds[ep_idx],
            simvla_model=simvla_model,
            processor=processor,
            image_preprocessor=image_preprocessor,
            benchmark_dict=benchmark_dict,
            get_libero_path_fn=get_libero_path,
            offscreen_cls=OffScreenRenderEnv,
            device=device,
            state_mean=state_mean,
            state_std=state_std,
            out_dir=out_dir,
            wm_fallback=wm_fallback,
            episode_spec=episode_specs[ep_idx],
        )
        _append_jsonl(summaries_path, summary)
        counts[str(summary["outcome"])] += 1
        _write_json(
            out_dir / "live_status.json",
            {
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "completed": sum(counts.values()),
                "target": len(selected),
                "counts": dict(counts),
                "last_episode": summary,
            },
        )
        print(
            f"[episode] ep={ep_idx} outcome={summary['outcome']} steps={summary['num_steps']} "
            f"fallback={summary['fallback_calls']} wm_accept={summary['wm_accepted']} "
            f"time={summary['wall_time_seconds']:.1f}s",
            flush=True,
        )

    rollout_wall_seconds = time.perf_counter() - rollout_started_at
    total_wall_seconds = time.perf_counter() - process_started_at
    completed = sum(counts.values())
    episodes_per_hour = 3600.0 * completed / rollout_wall_seconds
    _write_json(
        out_dir / "runtime_summary.json",
        {
            "completed_episodes": completed,
            "successes": counts["success"],
            "failures": counts["failure"],
            "setup_wall_seconds": setup_wall_seconds,
            "rollout_wall_seconds": rollout_wall_seconds,
            "total_wall_seconds": total_wall_seconds,
            "episodes_per_hour": episodes_per_hour,
            "projected_rollout_hours_200_episodes": 200.0 / episodes_per_hour,
            "projected_rollout_hours_600_episodes": 600.0 / episodes_per_hour,
            "projected_rollout_hours_1000_episodes": 1000.0 / episodes_per_hour,
            "cuda_peak_memory_gb": torch.cuda.max_memory_allocated(device) / (1024**3),
        },
    )


if __name__ == "__main__":
    main()
