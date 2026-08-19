"""Production Goal-Object H10 Mimic-Head Data Collector for SimVLA."""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
import os
from pathlib import Path
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch

from simvla_mimic_action_adapter import action_7d_to_10d
from simvla_mimic_features import (
    compute_denoising_metrics,
    extract_query_features,
)


def sha256_file(path: Path | str) -> str:
    """Compute sha256 hash of a file."""
    p = Path(path)
    if not p.exists() or not p.is_file():
        return "N/A"
    hasher = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024 * 4), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def deterministic_action_seed(
    global_action_seed: int,
    reset_seed: int,
    episode_index: int,
    timestep: int,
    sample_index: int,
) -> int:
    """Produce a deterministic 32-bit seed for candidate generation."""
    state = (
        int(global_action_seed) * 1000000007
        + int(reset_seed) * 1000003
        + int(episode_index) * 10007
        + int(timestep) * 101
        + int(sample_index)
    )
    return int(state & 0x7FFFFFFF)


def action_seeds_for_step(
    global_action_seed: int,
    reset_seed: int,
    episode_index: int,
    timestep: int,
    num_seeds: int = 8,
) -> List[int]:
    """Generate unique deterministic seeds for a query step."""
    seeds: List[int] = []
    seen = set()
    offset = 0
    while len(seeds) < num_seeds:
        candidate_seed = deterministic_action_seed(
            global_action_seed, reset_seed, episode_index, timestep, offset
        )
        if candidate_seed not in seen:
            seen.add(candidate_seed)
            seeds.append(candidate_seed)
        offset += 1
    return seeds


def build_collection_plan() -> List[Dict[str, Any]]:
    """Build the deterministic 1000-episode plan across tasks 0..9 and init states 0..49."""
    plan: List[Dict[str, Any]] = []
    for task_id in range(10):
        for init_state_idx in range(50):
            if init_state_idx < 25:
                assignment = "train"
            elif init_state_idx < 35:
                assignment = "id_development"
            elif init_state_idx < 45:
                assignment = "seen_test"
            else:
                assignment = "successful_calibration_pool"

            for seed_idx in range(2):
                rollout_seed = int(task_id * 10000 + init_state_idx * 100 + seed_idx)
                episode_key = (
                    f"libero_goal_object::task{task_id:02d}::init{init_state_idx:02d}::seed{seed_idx}"
                )
                plan.append(
                    {
                        "episode_key": episode_key,
                        "task_id": task_id,
                        "init_state_idx": init_state_idx,
                        "seed_idx": seed_idx,
                        "rollout_seed": rollout_seed,
                        "assignment": assignment,
                    }
                )
    return plan


def run_episode_collection(
    episode_spec: Dict[str, Any],
    simvla_model: Any,
    processor: Any,
    image_preprocessor: Any,
    offscreen_cls: Any,
    benchmark_dict: Any,
    get_libero_path_fn: Any,
    device: torch.device,
    data_root: Path,
    cfg: Dict[str, Any],
) -> Dict[str, Any]:
    """Execute a single complete episode with H10 chunk collection."""
    from simvla.env.libero_env import make_env, reset_to_init, check_success, obs_to_proprio

    task_id = int(episode_spec["task_id"])
    init_state_idx = int(episode_spec["init_state_idx"])
    rollout_seed = int(episode_spec["rollout_seed"])
    episode_key = str(episode_spec["episode_key"])
    assignment = str(episode_spec["assignment"])

    env, bundle = make_env(
        benchmark_dict,
        get_libero_path_fn,
        offscreen_cls,
        "libero_goal_object",
        task_id,
        int(cfg.get("resolution", 128)),
        rollout_seed,
    )

    init_states = bundle["init_states"]
    lang = bundle["task"].language
    obs = reset_to_init(env, init_states[init_state_idx % len(init_states)], int(cfg.get("warmup", 10)))

    lang_t = processor.encode_language([lang])
    lang_t = {k: v.to(device) for k, v in lang_t.items()}

    max_steps = int(cfg.get("max_steps", 300))
    execution_horizon = int(cfg.get("execution_horizon", 10))
    denoise_steps = int(cfg.get("denoise_steps", 10))
    global_action_seed = int(cfg.get("global_action_seed", 42))

    num_steps = 0
    query_index = 0
    success = False
    episode_queries: List[Dict[str, Any]] = []
    episode_arrays: List[Tuple[str, np.ndarray, np.ndarray]] = []
    previous_query_state: Optional[Dict[str, float]] = None

    try:
        while num_steps < max_steps and not success:
            timestep = num_steps
            proprio_np = obs_to_proprio(obs)
            proprio_t = torch.from_numpy(proprio_np).unsqueeze(0).to(device)
            image_t, mask_t = image_preprocessor(obs["agentview_rgb"], obs["eye_in_hand_rgb"], device)

            query_seeds = action_seeds_for_step(
                global_action_seed=global_action_seed,
                reset_seed=rollout_seed,
                episode_index=init_state_idx,
                timestep=timestep,
                num_seeds=8,
            )

            # Generate candidate 0 ALONE
            seed_main = [query_seeds[0]]
            res_main = simvla_model.generate_candidates_with_trajectory(
                input_ids=lang_t["input_ids"],
                image_input=image_t,
                image_mask=mask_t,
                proprio=proprio_t,
                seeds=seed_main,
                steps=denoise_steps,
            )

            # Generate candidates 1..7 in batch
            seeds_alt = query_seeds[1:8]
            res_alt = simvla_model.generate_candidates_with_trajectory(
                input_ids=lang_t["input_ids"],
                image_input=image_t,
                image_mask=mask_t,
                proprio=proprio_t,
                seeds=seeds_alt,
                steps=denoise_steps,
            )

            # Combine trajectories and calculate denoising metrics per step
            step_metrics: List[Dict[str, float]] = []
            for d in range(denoise_steps):
                x_d_main = res_main["trajectory_x"][d]  # [1, 10, 7]
                x_d_alt = res_alt["trajectory_x"][d]    # [7, 10, 7]
                x_d = np.concatenate([x_d_main, x_d_alt], axis=0)  # [8, 10, 7]

                v_d_main = res_main["trajectory_v"][d]  # [1, 10, 7]
                v_d_alt = res_alt["trajectory_v"][d]    # [7, 10, 7]
                v_d = np.concatenate([v_d_main, v_d_alt], axis=0)  # [8, 10, 7]

                m_d = compute_denoising_metrics(x_d, v_d)
                m_d["denoising_step"] = d
                step_metrics.append(m_d)

            # Combine final normalized chunks
            chunks_norm_7d = np.concatenate(
                [res_main["chunks_normalized"], res_alt["chunks_normalized"]], axis=0
            ).astype(np.float32)  # [8, 10, 7]

            # Postprocess to environment action space
            chunks_env_7d = simvla_model.action_space.postprocess(
                torch.from_numpy(chunks_norm_7d).to(device)
            ).detach().cpu().numpy().astype(np.float32)  # [8, 10, 7]

            # Convert to monitor 10D representation
            chunks_monitor_10d = action_7d_to_10d(chunks_env_7d)  # [8, 10, 10]

            scalars_37, horizon_10x6, previous_query_state = extract_query_features(
                chunks_monitor_10d, step_metrics, previous_query_state
            )

            array_rel_path = f"arrays/{episode_key}_q{query_index:03d}.npz"
            episode_arrays.append((array_rel_path, chunks_env_7d, chunks_monitor_10d))

            query_record = {
                "episode_key": episode_key,
                "task_id": task_id,
                "init_state_idx": init_state_idx,
                "rollout_seed": rollout_seed,
                "query_index": query_index,
                "action_timestep_start": timestep,
                "assignment": assignment,
                "candidate_seeds": query_seeds,
                "arrays_path": array_rel_path,
                "w2a_denoising_step_metrics": step_metrics,
                "instruction": lang,
                "checkpoint_sha": cfg.get("checkpoint_sha", ""),
                "normalization_sha": cfg.get("normalization_sha", ""),
            }

            # Execute candidate 0 actions across full execution horizon
            actions_executed = 0
            for action_idx in range(execution_horizon):
                if num_steps >= max_steps or success:
                    break
                act_7d = chunks_env_7d[0, action_idx]
                obs, _, done, _ = env.step(act_7d)
                num_steps += 1
                actions_executed += 1
                if check_success(env):
                    success = True

            query_record["actions_executed_from_chunk"] = actions_executed
            query_record["success_after_chunk"] = success
            episode_queries.append(query_record)
            query_index += 1

    finally:
        if env is not None:
            env.close()

    eventual_failure_target = 0 if success else 1
    for q in episode_queries:
        q["eventual_failure_target"] = eventual_failure_target
        q["parent_episode_success"] = success

    return {
        "episode_key": episode_key,
        "task_id": task_id,
        "init_state_idx": init_state_idx,
        "rollout_seed": rollout_seed,
        "assignment": assignment,
        "success": success,
        "total_steps": num_steps,
        "total_queries": len(episode_queries),
        "queries": episode_queries,
        "arrays": episode_arrays,
    }


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Goal-Object H10 Mimic-Head Data Collector"
    )
    parser.add_argument(
        "--data_root",
        type=str,
        default="/home/rootalkhatib/test/reda_ws_current_20260818/datasets/mimic_head_h10_goal_object_1000ep",
        help="Root path for saving collected dataset",
    )
    parser.add_argument(
        "--simvla_root",
        type=str,
        default="/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified",
        help="SimVLA modified code root",
    )
    parser.add_argument(
        "--libero_pro_root",
        type=str,
        default="/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO",
        help="LIBERO-PRO repository root",
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="/home/rootalkhatib/test/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000",
        help="SimVLA uncertainty checkpoint path",
    )
    parser.add_argument(
        "--norm_stats",
        type=str,
        default="/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json",
        help="Normalization statistics JSON path",
    )
    parser.add_argument(
        "--smolvlm_path",
        type=str,
        default="/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/models/huggingface/.hf_cache/transformers/models--HuggingFaceTB--SmolVLM-500M-Instruct/snapshots/a7da5b986cb59b408707209984f360a5f4ad7e47",
        help="SmolVLM cached processor path",
    )
    parser.add_argument(
        "--assignment",
        type=str,
        default="all",
        choices=["all", "train", "id_development", "seen_test", "successful_calibration_pool"],
        help="Filter collection to a specific split assignment",
    )
    parser.add_argument(
        "--task_ids",
        type=int,
        nargs="+",
        default=list(range(10)),
        help="Task IDs to collect (0..9)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume collection skipping completed episodes",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda" if torch.cuda.is_available() else "cpu",
        help="Device for policy inference",
    )
    parser.add_argument(
        "--denoise_steps",
        type=int,
        default=10,
        help="Number of flow-matching denoising steps",
    )
    parser.add_argument(
        "--execution_horizon",
        type=int,
        default=10,
        help="Actions to execute per policy chunk",
    )
    parser.add_argument(
        "--max_steps",
        type=int,
        default=300,
        help="Maximum action steps per episode",
    )
    return parser.parse_args()


def main() -> None:
    """Main entry point for collection execution."""
    args = parse_args()
    data_root = Path(args.data_root)
    data_root.mkdir(parents=True, exist_ok=True)
    arrays_dir = data_root / "arrays"
    arrays_dir.mkdir(parents=True, exist_ok=True)

    plan = build_collection_plan()
    if args.assignment != "all":
        plan = [p for p in plan if p["assignment"] == args.assignment]
    if args.task_ids:
        allowed_tasks = set(args.task_ids)
        plan = [p for p in plan if p["task_id"] in allowed_tasks]

    completed_keys = set()
    summaries_file = data_root / "episode_summaries.jsonl"
    if args.resume and summaries_file.exists():
        with open(summaries_file, "r") as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    completed_keys.add(rec["episode_key"])

    print(
        f"[collector] starting plan with {len(plan)} episodes, already completed {len(completed_keys)}"
    )


if __name__ == "__main__":
    main()
