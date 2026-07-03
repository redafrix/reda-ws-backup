#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import time
import traceback
from collections import Counter, deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch

from collect_fiper_uncertainty_receding_dean_v1 import (
    DEAN_CKPT_60K,
    DEAN_LIBERO_PRO_ROOT,
    DEAN_NORM_STATS,
    DEAN_SIMVLA_ROOT,
    DEAN_SMOLVLM_CACHE,
    UNCERTAINTY_49D_KEYS,
    UNCERTAINTY_DELTA_49D_KEYS,
    HistoryBuffer,
    ImagePreprocessor,
    append_jsonl,
    check_success,
    generate_seeded_chunks_with_main_uncertainty,
    json_sanitize,
    load_state_stats,
    now_iso,
    object_body_positions,
    obs_images,
    obs_to_proprio,
    save_png,
    set_all_seeds,
    setup_runtime,
    sha256_file,
    write_json_atomic,
)


EXPECTED_CHECKPOINT_SHA256 = "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71"
TOPK8_INDICES = [6, 21, 25, 27, 23, 2, 26, 24]
TOPK8_KEYS = [UNCERTAINTY_49D_KEYS[index] for index in TOPK8_INDICES]


@dataclass(frozen=True)
class EpisodeSpec:
    episode_uid: str
    global_episode_index: int
    run_id: str
    task_suite_name: str
    task_id: int
    initial_state_index: int
    eval_seed: int
    episode_seed: int
    bddl_relative_path: str
    bddl_sha256: str
    init_state_file_relative_path: str
    init_state_file_sha256: str


def parse_bddl_language(path: Path) -> str:
    match = re.search(r"\(:language\s*(.*?)\)", path.read_text(encoding="utf-8"), flags=re.S | re.I)
    if not match:
        raise ValueError(f"missing (:language ...) in {path}")
    return " ".join(match.group(1).split()).lower()


def stable_seeds(base_seed: int, episode_uid: str, timestep: int, count: int) -> list[int]:
    seeds: list[int] = []
    seen: set[int] = set()
    nonce = 0
    while len(seeds) < count:
        payload = f"{base_seed}|{episode_uid}|{timestep}|{nonce}".encode()
        candidate = int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**31 - 1)
        nonce += 1
        if candidate == 0 or candidate in seen:
            continue
        seen.add(candidate)
        seeds.append(candidate)
    return seeds


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")


def load_specs(path: Path, phase: str) -> list[EpisodeSpec]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    specs: list[EpisodeSpec] = []
    for index, row in enumerate(rows):
        run_id = row.get("run_id") or phase
        global_index = int(row.get("global_episode_index") or index)
        specs.append(
            EpisodeSpec(
                episode_uid=row["episode_uid"],
                global_episode_index=global_index,
                run_id=run_id,
                task_suite_name=row["task_suite_name"],
                task_id=int(row["task_id"]),
                initial_state_index=int(row["initial_state_index"]),
                eval_seed=int(row["eval_seed"]),
                episode_seed=int(row["episode_seed"]),
                bddl_relative_path=row["bddl_relative_path"],
                bddl_sha256=row["bddl_sha256"],
                init_state_file_relative_path=row["init_state_file_relative_path"],
                init_state_file_sha256=row["init_state_file_sha256"],
            )
        )
    if len({spec.episode_uid for spec in specs}) != len(specs):
        raise ValueError(f"duplicate episode_uid in {path}")
    return specs


def load_completed(path: Path) -> set[str]:
    completed: set[str] = set()
    if not path.exists():
        return completed
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                row = json.loads(line)
                if row.get("episode_complete"):
                    completed.add(str(row["episode_uid"]))
            except Exception:
                continue
    return completed


def verify_asset(path: Path, expected_sha256: str, cache: dict[Path, str]) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    actual = cache.get(path)
    if actual is None:
        actual = str(sha256_file(path))
        cache[path] = actual
    if actual != expected_sha256:
        raise RuntimeError(f"asset SHA-256 mismatch: {path}: expected={expected_sha256}, actual={actual}")


def make_env(offscreen_cls: Any, bddl_path: Path, init_path: Path, resolution: int, env_seed: int):
    init_states = torch.load(init_path, map_location="cpu", weights_only=False)
    env = offscreen_cls(
        bddl_file_name=str(bddl_path),
        camera_heights=int(resolution),
        camera_widths=int(resolution),
    )
    if hasattr(env, "seed"):
        env.seed(int(env_seed))
    return env, init_states


def reset_to_exact_init(env: Any, init_state: Any, warmup: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    env.reset()
    obs = env.set_init_state(init_state)
    warmup_rows: list[dict[str, Any]] = []
    zero = np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32)
    for index in range(max(0, int(warmup))):
        pre = obs_to_proprio(obs)
        obs, reward, done, _info = env.step(zero)
        warmup_rows.append(
            {
                "warmup_index": index,
                "action": zero.tolist(),
                "reward": float(reward),
                "done": bool(done),
                "pre_proprio": pre.tolist(),
                "post_proprio": obs_to_proprio(obs).tolist(),
            }
        )
        if done:
            raise RuntimeError(f"environment terminated during warmup at step {index}")
    return obs, warmup_rows


def disk_wait(outdir: Path, minimum_free_gb: float, sleep_seconds: int, status_path: Path) -> None:
    while shutil.disk_usage(outdir).free < minimum_free_gb * 1024**3:
        free_gb = shutil.disk_usage(outdir).free / 1024**3
        write_json_atomic(
            status_path,
            {
                "schema_version": "goal_object_dual_mode_status_v1",
                "state": "paused_low_disk",
                "free_gb": free_gb,
                "minimum_free_gb": minimum_free_gb,
                "updated_at": now_iso(),
                "pid": os.getpid(),
            },
        )
        print(f"[disk] paused: {free_gb:.2f} GiB free, need {minimum_free_gb:.2f} GiB", flush=True)
        time.sleep(max(10, sleep_seconds))


def array_or_empty(values: list[Any], shape: tuple[int, ...], dtype: Any) -> np.ndarray:
    if values:
        return np.asarray(values, dtype=dtype)
    return np.empty((0, *shape), dtype=dtype)


def save_episode_npz(
    path: Path,
    query_data: dict[str, list[Any]],
    transition_data: dict[str, list[Any]],
) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        path,
        query_timesteps=np.asarray(query_data["timesteps"], dtype=np.int32),
        query_proprio=array_or_empty(query_data["proprio"], (8,), np.float32),
        main_seeds=np.asarray(query_data["main_seeds"], dtype=np.int64),
        ace_seeds=array_or_empty(query_data["ace_seeds"], (8,), np.int64),
        main_chunks_env=array_or_empty(query_data["main_chunks_env"], (10, 7), np.float32),
        main_chunks_normalized=array_or_empty(query_data["main_chunks_norm"], (10, 7), np.float32),
        ace_chunks_env=array_or_empty(query_data["ace_chunks_env"], (8, 10, 7), np.float32),
        ace_chunks_normalized=array_or_empty(query_data["ace_chunks_norm"], (8, 10, 7), np.float32),
        uncertainty_49d=array_or_empty(query_data["features"], (49,), np.float32),
        uncertainty_delta_49d=array_or_empty(query_data["deltas"], (49,), np.float32),
        uncertainty_topk8=array_or_empty(query_data["topk8"], (8,), np.float32),
        uncertainty_delta_topk8=array_or_empty(query_data["delta_topk8"], (8,), np.float32),
        transition_timesteps=np.asarray(transition_data["timesteps"], dtype=np.int32),
        transition_query_indices=np.asarray(transition_data["query_indices"], dtype=np.int32),
        transition_action_indices=np.asarray(transition_data["action_indices"], dtype=np.int16),
        executed_actions=array_or_empty(transition_data["actions"], (7,), np.float32),
        rewards=np.asarray(transition_data["rewards"], dtype=np.float32),
        dones=np.asarray(transition_data["dones"], dtype=np.bool_),
        successes=np.asarray(transition_data["successes"], dtype=np.bool_),
        pre_proprio=array_or_empty(transition_data["pre_proprio"], (8,), np.float32),
        post_proprio=array_or_empty(transition_data["post_proprio"], (8,), np.float32),
    )
    return str(path)


def collect(args: argparse.Namespace) -> None:
    setup_runtime(Path(args.simvla_root), Path(args.libero_pro_root))
    from libero.libero.envs import OffScreenRenderEnv
    from models.modeling_smolvlm_vla import SmolVLMVLA
    from models.processing_smolvlm_vla import SmolVLMVLAProcessor
    from sim_state_utils import get_state, save_state_npz
    from task_parser import parse_task_context

    if args.ace_candidates != 8 or args.action_horizon != 10:
        raise ValueError("this collection contract requires exactly 8 ACE candidates and a 10-action horizon")
    if args.execution_mode not in {"receding", "chunk10"}:
        raise ValueError(args.execution_mode)

    bundle_root = Path(args.bundle_root).resolve()
    episode_plan = Path(args.episode_plan).resolve()
    outdir = Path(args.out_dir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    status_path = outdir / "live_status.json"
    summary_path = outdir / "episode_summaries.jsonl"
    query_rows_path = outdir / "query_samples.jsonl"
    transition_rows_path = outdir / "transitions.jsonl"
    compact_dir = outdir / "episodes_npz"
    metadata_dir = outdir / "episode_metadata"
    image_dir = outdir / "images"
    state_dir = outdir / "states"
    for directory in [compact_dir, metadata_dir]:
        directory.mkdir(exist_ok=True)
    if args.save_images:
        image_dir.mkdir(exist_ok=True)
    if args.save_states:
        state_dir.mkdir(exist_ok=True)

    specs = load_specs(episode_plan, args.phase)
    specs = [spec for spec in specs if spec.global_episode_index % args.worker_count == args.worker_index]
    completed = load_completed(summary_path) if args.resume else set()
    pending = [spec for spec in specs if spec.episode_uid not in completed]
    if args.stop_after_episodes is not None:
        pending = pending[: args.stop_after_episodes]
    if not pending:
        write_json_atomic(
            status_path,
            {
                "schema_version": "goal_object_dual_mode_status_v1",
                "state": "completed",
                "phase": args.phase,
                "execution_mode": args.execution_mode,
                "worker_index": args.worker_index,
                "worker_count": args.worker_count,
                "completed_before_start": len(completed),
                "completed_this_process": 0,
                "updated_at": now_iso(),
                "pid": os.getpid(),
                "reason": "no_pending_episodes",
            },
        )
        print("[startup] no pending episodes; exiting without loading the model", flush=True)
        return

    checkpoint = Path(args.checkpoint)
    checkpoint_file = checkpoint / "model.safetensors"
    checkpoint_sha = sha256_file(checkpoint_file)
    if checkpoint_sha != args.expected_checkpoint_sha256:
        raise RuntimeError(
            f"checkpoint SHA-256 mismatch: expected={args.expected_checkpoint_sha256}, actual={checkpoint_sha}"
        )

    torch.set_float32_matmul_precision("high")
    device = torch.device(args.device or ("cuda" if torch.cuda.is_available() else "cpu"))
    print(f"[startup] loading {checkpoint} on {device}", flush=True)
    set_all_seeds(args.model_load_seed)
    model = SmolVLMVLA.from_pretrained(str(checkpoint)).to(device).eval()
    processor = SmolVLMVLAProcessor.from_pretrained(str(args.smolvlm_path))
    model.action_space.load_norm_stats(str(args.norm_stats))
    if not getattr(model.config, "predict_uncertainty", False):
        raise RuntimeError("checkpoint does not expose the uncertainty head")
    state_mean, state_std = load_state_stats(model, Path(args.norm_stats))
    preprocessor = ImagePreprocessor(args.image_size)

    manifest = {
        "schema_version": "goal_object_dual_mode_manifest_v1",
        "created_at": now_iso(),
        "phase": args.phase,
        "execution_mode": args.execution_mode,
        "bundle_root": str(bundle_root),
        "bundle_manifest_sha256": sha256_file(bundle_root / "MANIFEST.json"),
        "episode_plan": str(episode_plan),
        "episode_plan_sha256": sha256_file(episode_plan),
        "episodes_in_worker_plan": len(specs),
        "worker_index": args.worker_index,
        "worker_count": args.worker_count,
        "checkpoint": str(checkpoint),
        "checkpoint_sha256": checkpoint_sha,
        "uncertainty_49d_keys": UNCERTAINTY_49D_KEYS,
        "uncertainty_delta_49d_keys": UNCERTAINTY_DELTA_49D_KEYS,
        "topk8_indices": TOPK8_INDICES,
        "topk8_keys": TOPK8_KEYS,
        "ace_candidates": args.ace_candidates,
        "action_horizon": args.action_horizon,
        "model_denoise_steps": args.model_denoise_steps,
        "history_k": args.history_k,
        "max_timesteps": args.max_timesteps,
        "warmup": args.warmup,
        "save_images": args.save_images,
        "save_states": args.save_states,
        "full_json_queries": args.full_json_queries,
        "minimum_free_gb": args.minimum_free_gb,
        "action_seed_base": args.action_seed_base,
    }
    write_json_atomic(outdir / "run_manifest.json", manifest)

    counters: Counter[str] = Counter()
    consecutive_errors = 0
    started = time.time()
    asset_hash_cache: dict[Path, str] = {}
    current_run_id: str | None = None

    def write_status(state: str, **extra: Any) -> None:
        payload = {
            "schema_version": "goal_object_dual_mode_status_v1",
            "state": state,
            "phase": args.phase,
            "execution_mode": args.execution_mode,
            "worker_index": args.worker_index,
            "worker_count": args.worker_count,
            "pid": os.getpid(),
            "completed_before_start": len(completed),
            "completed_this_process": sum(counters.values()),
            "outcome_counts": dict(counters),
            "elapsed_seconds": time.time() - started,
            "updated_at": now_iso(),
        }
        payload.update(extra)
        write_json_atomic(status_path, payload)

    write_status("started", pending_episodes=len(pending))
    for spec in pending:
        disk_wait(outdir, args.minimum_free_gb, args.low_disk_sleep_seconds, status_path)
        episode_start = time.time()
        episode_name = safe_name(spec.episode_uid)
        env = None
        error_message = ""
        success = False
        terminal_done = False
        env_steps = 0
        query_count = 0
        full_query_rows: list[dict[str, Any]] = []
        full_transition_rows: list[dict[str, Any]] = []
        query_data: dict[str, list[Any]] = {
            key: []
            for key in [
                "timesteps",
                "proprio",
                "main_seeds",
                "ace_seeds",
                "main_chunks_env",
                "main_chunks_norm",
                "ace_chunks_env",
                "ace_chunks_norm",
                "features",
                "deltas",
                "topk8",
                "delta_topk8",
            ]
        }
        transition_data: dict[str, list[Any]] = {
            key: []
            for key in [
                "timesteps",
                "query_indices",
                "action_indices",
                "actions",
                "rewards",
                "dones",
                "successes",
                "pre_proprio",
                "post_proprio",
            ]
        }
        warmup_rows: list[dict[str, Any]] = []
        language = ""
        task_context: dict[str, Any] = {}
        bddl_path = bundle_root / spec.bddl_relative_path
        init_path = bundle_root / spec.init_state_file_relative_path
        previous_action: np.ndarray | None = None
        previous_proprio: np.ndarray | None = None
        previous_features: np.ndarray | None = None
        history = HistoryBuffer(args.history_k)

        try:
            verify_asset(bddl_path, spec.bddl_sha256, asset_hash_cache)
            verify_asset(init_path, spec.init_state_file_sha256, asset_hash_cache)
            language = parse_bddl_language(bddl_path)

            if args.phase == "exact":
                if spec.run_id != current_run_id:
                    set_all_seeds(spec.eval_seed)
                    current_run_id = spec.run_id
            else:
                set_all_seeds(spec.episode_seed)

            env, init_states = make_env(
                OffScreenRenderEnv,
                bddl_path,
                init_path,
                args.resolution,
                spec.eval_seed,
            )
            if spec.initial_state_index >= len(init_states):
                raise IndexError(
                    f"init state {spec.initial_state_index} unavailable; file has {len(init_states)} states"
                )
            obs, warmup_rows = reset_to_exact_init(env, init_states[spec.initial_state_index], args.warmup)
            all_bodies = list(object_body_positions(env).keys())
            try:
                task_context = parse_task_context(language, obs, all_bodies=all_bodies)
            except Exception as exc:
                task_context = {"parse_error": f"{type(exc).__name__}: {exc}"}

            while env_steps < args.max_timesteps and not success and not terminal_done:
                query_index = query_count
                query_timestep = env_steps
                before_img, before_wrist = obs_images(obs)
                proprio_np = obs_to_proprio(obs)
                before_obj = object_body_positions(env)
                query_state_path = None
                before_agent_path = None
                before_wrist_path = None
                if args.save_states:
                    query_state_path = save_state_npz(
                        state_dir / episode_name / f"query_{query_index:04d}_pre.npz", get_state(env)
                    )
                if args.save_images:
                    before_agent_path = save_png(
                        image_dir / episode_name / f"query_{query_index:04d}_agent.png", before_img
                    )
                    before_wrist_path = save_png(
                        image_dir / episode_name / f"query_{query_index:04d}_wrist.png", before_wrist
                    )

                seeds = stable_seeds(
                    args.action_seed_base,
                    spec.episode_uid,
                    query_timestep,
                    1 + args.ace_candidates,
                )
                images_t, mask_t = preprocessor(before_img, before_wrist, device)
                language_t = processor.encode_language([language])
                language_t = {key: value.to(device) for key, value in language_t.items()}
                proprio_t = torch.as_tensor(proprio_np, dtype=torch.float32, device=device).unsqueeze(0)
                batch = generate_seeded_chunks_with_main_uncertainty(
                    model=model,
                    input_ids=language_t["input_ids"],
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
                deltas = np.zeros_like(features) if previous_features is None else features - previous_features
                topk8 = features[TOPK8_INDICES]
                delta_topk8 = deltas[TOPK8_INDICES]
                main_chunk_env = np.asarray(batch.chunks_env[0], dtype=np.float32)
                main_chunk_norm = np.asarray(batch.chunks_norm[0], dtype=np.float32)
                ace_chunks_env = np.asarray(batch.chunks_env[1:], dtype=np.float32)
                ace_chunks_norm = np.asarray(batch.chunks_norm[1:], dtype=np.float32)

                query_data["timesteps"].append(query_timestep)
                query_data["proprio"].append(proprio_np)
                query_data["main_seeds"].append(seeds[0])
                query_data["ace_seeds"].append(seeds[1:])
                query_data["main_chunks_env"].append(main_chunk_env)
                query_data["main_chunks_norm"].append(main_chunk_norm)
                query_data["ace_chunks_env"].append(ace_chunks_env)
                query_data["ace_chunks_norm"].append(ace_chunks_norm)
                query_data["features"].append(features)
                query_data["deltas"].append(deltas)
                query_data["topk8"].append(topk8)
                query_data["delta_topk8"].append(delta_topk8)

                query_row = {
                    "schema_version": "goal_object_dual_mode_query_v1",
                    "episode_uid": spec.episode_uid,
                    "global_episode_index": spec.global_episode_index,
                    "phase": args.phase,
                    "execution_mode": args.execution_mode,
                    "query_index": query_index,
                    "timestep": query_timestep,
                    "suite": spec.task_suite_name,
                    "task_id": spec.task_id,
                    "task_instruction": language,
                    "initial_state_index": spec.initial_state_index,
                    "eval_seed": spec.eval_seed,
                    "episode_seed": spec.episode_seed,
                    "current": {
                        "proprio": proprio_np.tolist(),
                        "object_positions_before": before_obj,
                        "sim_state_path": query_state_path,
                        "before_image_path": before_agent_path,
                        "before_wrist_image_path": before_wrist_path,
                        "task_context": task_context,
                    },
                    "history": history.to_list(),
                    "main_seed": seeds[0],
                    "main_candidate_action_chunk_normalized": main_chunk_norm.tolist(),
                    "main_candidate_action_chunk_env": main_chunk_env.tolist(),
                    "ace_candidate_seeds": seeds[1:],
                    "ace_candidate_chunks_normalized": ace_chunks_norm.tolist(),
                    "ace_candidate_chunks_env": ace_chunks_env.tolist(),
                    "simvla_uncertainty_49d_keys": UNCERTAINTY_49D_KEYS,
                    "simvla_uncertainty_49d": features.tolist(),
                    "simvla_uncertainty_delta_49d_keys": UNCERTAINTY_DELTA_49D_KEYS,
                    "simvla_uncertainty_delta_49d": deltas.tolist(),
                    "simvla_uncertainty_topk8_keys": TOPK8_KEYS,
                    "simvla_uncertainty_topk8": topk8.tolist(),
                    "simvla_uncertainty_delta_topk8": delta_topk8.tolist(),
                    "simvla_uncertainty_scalar_map": batch.feature_map,
                    "simvla_uncertainty_raw": batch.main_uncertainty,
                    "metadata": {
                        "checkpoint_sha256": checkpoint_sha,
                        "bddl_path": str(bddl_path),
                        "bddl_sha256": spec.bddl_sha256,
                        "init_states_path": str(init_path),
                        "init_states_sha256": spec.init_state_file_sha256,
                        "collection_time": now_iso(),
                    },
                }
                if args.full_json_queries:
                    full_query_rows.append(query_row)

                actions_to_execute = 1 if args.execution_mode == "receding" else args.action_horizon
                for action_index, action in enumerate(main_chunk_env[:actions_to_execute]):
                    if env_steps >= args.max_timesteps or success or terminal_done:
                        break
                    transition_timestep = env_steps
                    pre_proprio = obs_to_proprio(obs)
                    obs, reward, done, _info = env.step(action.astype(np.float32))
                    env_steps += 1
                    checked_success = check_success(env)
                    success = bool(success or float(reward) > 0.0 or bool(checked_success) or bool(done))
                    terminal_done = bool(terminal_done or done)
                    post_proprio = obs_to_proprio(obs)
                    post_agent_path = None
                    post_wrist_path = None
                    post_state_path = None
                    if args.save_images:
                        post_img, post_wrist = obs_images(obs)
                        post_agent_path = save_png(
                            image_dir / episode_name / f"transition_{transition_timestep:04d}_post_agent.png", post_img
                        )
                        post_wrist_path = save_png(
                            image_dir / episode_name / f"transition_{transition_timestep:04d}_post_wrist.png", post_wrist
                        )
                    if args.save_states:
                        post_state_path = save_state_npz(
                            state_dir / episode_name / f"transition_{transition_timestep:04d}_post.npz", get_state(env)
                        )

                    transition_data["timesteps"].append(transition_timestep)
                    transition_data["query_indices"].append(query_index)
                    transition_data["action_indices"].append(action_index)
                    transition_data["actions"].append(action)
                    transition_data["rewards"].append(float(reward))
                    transition_data["dones"].append(bool(done))
                    transition_data["successes"].append(bool(success))
                    transition_data["pre_proprio"].append(pre_proprio)
                    transition_data["post_proprio"].append(post_proprio)
                    transition_row = {
                        "schema_version": "goal_object_dual_mode_transition_v1",
                        "episode_uid": spec.episode_uid,
                        "execution_mode": args.execution_mode,
                        "timestep": transition_timestep,
                        "query_index": query_index,
                        "action_index_in_chunk": action_index,
                        "executed_action": np.asarray(action, dtype=np.float32).tolist(),
                        "reward": float(reward),
                        "done": bool(done),
                        "success_after_transition": bool(success),
                        "pre_proprio": pre_proprio.tolist(),
                        "post_proprio": post_proprio.tolist(),
                        "post_image_path": post_agent_path,
                        "post_wrist_image_path": post_wrist_path,
                        "post_state_path": post_state_path,
                    }
                    if args.full_json_queries:
                        full_transition_rows.append(transition_row)
                    history.append(
                        {
                            "timestep": transition_timestep,
                            "query_index": query_index,
                            "action_index_in_chunk": action_index,
                            "reward": float(reward),
                            "success": bool(success),
                            "proprio": post_proprio.tolist(),
                            "executed_action": np.asarray(action, dtype=np.float32).tolist(),
                        }
                    )
                    previous_action = np.asarray(action, dtype=np.float32)
                    previous_proprio = pre_proprio

                previous_features = features
                query_count += 1
                write_status(
                    "running_episode",
                    episode_uid=spec.episode_uid,
                    task_id=spec.task_id,
                    initial_state_index=spec.initial_state_index,
                    timestep=env_steps,
                    query_count=query_count,
                )

        except Exception as exc:
            error_message = "".join(traceback.format_exception_only(type(exc), exc)).strip()
            traceback.print_exc()
        finally:
            if env is not None:
                try:
                    env.close()
                except Exception:
                    pass

        outcome = "error" if error_message else ("success" if success else "failure_or_timeout")
        npz_path = save_episode_npz(compact_dir / f"{episode_name}.npz", query_data, transition_data)
        metadata = {
            "schema_version": "goal_object_dual_mode_episode_metadata_v1",
            "episode": asdict(spec),
            "phase": args.phase,
            "execution_mode": args.execution_mode,
            "task_instruction": language,
            "task_context": task_context,
            "warmup_transitions": warmup_rows,
            "outcome": outcome,
            "success": success,
            "terminal_done": terminal_done,
            "env_steps": env_steps,
            "query_count": query_count,
            "npz_path": npz_path,
            "uncertainty_49d_keys": UNCERTAINTY_49D_KEYS,
            "uncertainty_delta_49d_keys": UNCERTAINTY_DELTA_49D_KEYS,
            "topk8_indices": TOPK8_INDICES,
            "topk8_keys": TOPK8_KEYS,
            "error_message": error_message,
        }
        metadata_path = metadata_dir / f"{episode_name}.json"
        write_json_atomic(metadata_path, metadata)
        if args.full_json_queries:
            for row in full_query_rows:
                row["episode_outcome"] = outcome
                row["parent_episode_success"] = success
                row["allowed_use"] = "train_calib_eval_all_outcomes"
            append_jsonl(query_rows_path, full_query_rows)
            append_jsonl(transition_rows_path, full_transition_rows)

        summary = {
            "schema_version": "goal_object_dual_mode_episode_summary_v1",
            "episode_uid": spec.episode_uid,
            "global_episode_index": spec.global_episode_index,
            "run_id": spec.run_id,
            "phase": args.phase,
            "execution_mode": args.execution_mode,
            "task_id": spec.task_id,
            "initial_state_index": spec.initial_state_index,
            "eval_seed": spec.eval_seed,
            "episode_seed": spec.episode_seed,
            "outcome": outcome,
            "success": success,
            "terminal_done": terminal_done,
            "num_env_steps": env_steps,
            "num_queries": query_count,
            "num_transitions": len(transition_data["timesteps"]),
            "wall_time_seconds": time.time() - episode_start,
            "error_message": error_message,
            "npz_path": npz_path,
            "metadata_path": str(metadata_path),
            "episode_complete": True,
            "updated_at": now_iso(),
        }
        append_jsonl(summary_path, [summary])
        counters[outcome] += 1
        consecutive_errors = consecutive_errors + 1 if error_message else 0
        print(
            f"[episode] {spec.episode_uid} outcome={outcome} steps={env_steps} "
            f"queries={query_count} seconds={summary['wall_time_seconds']:.1f}",
            flush=True,
        )
        write_status("episode_completed", last_episode=summary)

        if consecutive_errors >= args.max_errors:
            write_status("failed", reason="max_errors_reached")
            raise RuntimeError(f"stopping after {consecutive_errors} consecutive errors")

    write_status("completed", total_worker_specs=len(specs))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Exact/continuous LIBERO goal-object dual-mode collector")
    parser.add_argument("--phase", choices=["exact", "continuous"], required=True)
    parser.add_argument("--execution-mode", choices=["receding", "chunk10"], required=True)
    parser.add_argument("--bundle-root", required=True)
    parser.add_argument("--episode-plan", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--simvla-root", default=str(DEAN_SIMVLA_ROOT))
    parser.add_argument("--libero-pro-root", default=str(DEAN_LIBERO_PRO_ROOT))
    parser.add_argument("--checkpoint", default=str(DEAN_CKPT_60K))
    parser.add_argument("--expected-checkpoint-sha256", default=EXPECTED_CHECKPOINT_SHA256)
    parser.add_argument("--smolvlm-path", default=DEAN_SMOLVLM_CACHE)
    parser.add_argument("--norm-stats", default=str(DEAN_NORM_STATS))
    parser.add_argument("--device", default="")
    parser.add_argument("--worker-index", type=int, default=0)
    parser.add_argument("--worker-count", type=int, default=1)
    parser.add_argument("--stop-after-episodes", type=int)
    parser.add_argument("--max-timesteps", type=int, default=250)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--ace-candidates", type=int, default=8)
    parser.add_argument("--action-horizon", type=int, default=10)
    parser.add_argument("--model-denoise-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--image-size", type=int, default=384)
    parser.add_argument("--model-load-seed", type=int, default=7)
    parser.add_argument("--action-seed-base", type=int, default=2026060502)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-states", action="store_true")
    parser.add_argument("--full-json-queries", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--minimum-free-gb", type=float, default=12.0)
    parser.add_argument("--low-disk-sleep-seconds", type=int, default=300)
    parser.add_argument("--max-errors", type=int, default=5)
    return parser.parse_args()


if __name__ == "__main__":
    collect(parse_args())
