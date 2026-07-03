#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any


BOB_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608")
SIMVLA_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified")
LIBERO_PRO_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
NORM_STATS = SIMVLA_ROOT / "norm_stats/libero_norm.json"
SMOLVLM = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/smolvlm_cache")
ORIGINAL_CKPT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO")
MODIFIED_CKPT = Path("/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000")
ORIGINAL_SHA = "9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be"
MODIFIED_SHA = "3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71"
TOPK8_DIMS = [6, 21, 25, 27, 23, 2, 26, 24]


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def unique_seeds(seed: int, count: int) -> list[int]:
    rng = random.Random(seed)
    out: list[int] = []
    seen: set[int] = set()
    while len(out) < count:
        value = rng.randrange(1, 2**31 - 1)
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def base_config(task_id: int, reset_seeds: list[int], out_dir: Path, experiment_id: str, checkpoint: Path, checkpoint_sha: str) -> dict[str, Any]:
    return {
        "ace_candidate_count": 8,
        "checkpoint": str(checkpoint),
        "execution_horizon": 10,
        "expected_checkpoint_sha256": checkpoint_sha,
        "expected_topk8_dims": TOPK8_DIMS,
        "experiment_id": experiment_id,
        "global_action_seed": 206080917 + int(task_id),
        "history_steps": 16,
        "image_size": 384,
        "libero_pro_root": str(LIBERO_PRO_ROOT),
        "max_steps": 300,
        "model_denoise_steps": 10,
        "model_load_seed": 206080911,
        "norm_stats": str(NORM_STATS),
        "output_dir": str(out_dir),
        "reset_seeds": reset_seeds,
        "resolution": 128,
        "risk_model_base_dir": str(BOB_ROOT / "models/h10_continuous/all_tasks_random/base"),
        "risk_model_unc_topk8_dir": str(BOB_ROOT / "models/h10_continuous/all_tasks_random/unc_topk8"),
        "selection_cooldown_steps": 0,
        "selection_main_threshold": "q95",
        "selection_max_modifications_per_episode": 0,
        "selection_min_high_risk_streak": 1,
        "selection_min_margin": 0.1,
        "selection_min_timestep": 0,
        "selection_require_candidate_below_q95": False,
        "selection_streak_threshold": "q95",
        "selection_strong_margin": 0.15,
        "simvla_root": str(SIMVLA_ROOT),
        "smolvlm_path": str(SMOLVLM),
        "suite": "libero_goal_object",
        "task_id": int(task_id),
        "warmup": 10,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=str(BOB_ROOT))
    p.add_argument("--seed", type=int, default=2026060801)
    p.add_argument("--tasks", nargs="+", type=int, default=[3, 6, 8])
    p.add_argument("--episodes", type=int, default=100)
    p.add_argument("--shards", type=int, default=2)
    args = p.parse_args()

    root = Path(args.root)
    cfg_dir = root / "configs/online"
    seed_plan: dict[str, Any] = {"seed": args.seed, "tasks": {}}
    jobs = []
    policies = [
        ("original_simvla", "simvla_only", ORIGINAL_CKPT, ORIGINAL_SHA),
        ("original_h10_risk_base", "risk_base", ORIGINAL_CKPT, ORIGINAL_SHA),
        ("modified_simvla", "simvla_only", MODIFIED_CKPT, MODIFIED_SHA),
        ("modified_h10_risk_topk8", "risk_topk8", MODIFIED_CKPT, MODIFIED_SHA),
    ]
    for task_id in args.tasks:
        task_seeds = unique_seeds(args.seed + task_id * 1009, args.episodes)
        seed_plan["tasks"][str(task_id)] = task_seeds
        shard_size = args.episodes // args.shards
        for label, policy, checkpoint, sha in policies:
            for shard in range(args.shards):
                start = shard * shard_size
                end = args.episodes if shard == args.shards - 1 else (shard + 1) * shard_size
                shard_seeds = task_seeds[start:end]
                exp_id = f"task{task_id}_{label}_h10_s{shard}"
                out_dir = root / "runs/online" / f"task{task_id}" / label / f"shard_{shard}"
                cfg = base_config(task_id, shard_seeds, out_dir, exp_id, checkpoint, sha)
                cfg_path = cfg_dir / f"{exp_id}.json"
                write_json(cfg_path, cfg)
                jobs.append(
                    {
                        "task_id": task_id,
                        "label": label,
                        "policy": policy,
                        "shard": shard,
                        "config": str(cfg_path),
                        "output_dir": str(out_dir),
                        "episodes": len(shard_seeds),
                    }
                )
    write_json(root / "configs/online_seed_plan.json", seed_plan)
    write_json(root / "configs/online_jobs.json", {"jobs": jobs})
    print(json.dumps({"configs": len(jobs), "seed_plan": str(root / "configs/online_seed_plan.json")}, indent=2), flush=True)


if __name__ == "__main__":
    main()
