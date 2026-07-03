#!/usr/bin/env python3
import argparse
import csv
import hashlib
import json
import random
import re
import sys
import time
from pathlib import Path

import numpy as np
import torch


REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
FIPER_ROOT = REDA_WS / "fiper_ws"
SIMVLA_SRC = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_PRO_SRC = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
ASYNCHVLA_SRC = REDA_WS / "asynchvla_ws/src"

SUITE_NAME = "libero_goal_object_official_byte_identical"
BDDL_DIR = LIBERO_PRO_SRC / "libero/libero/bddl_files/libero_goal_object_official"
INIT_DIR = LIBERO_PRO_SRC / "libero/libero/init_files/libero_goal_object_official"
OUT_ROOT = FIPER_ROOT / "datasets/simvla_official_libero_goal_object_h10_basic_500ep_20260626"

CHECKPOINT_PATH = FIPER_ROOT / "checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO"
NORM_STATS_PATH = SIMVLA_SRC / "norm_stats/libero_norm.json"
SMOLVLM_CACHE = FIPER_ROOT / "realtime_deployment/smolvlm_cache"
EXPECTED_CKPT_HASH = "9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be"
GLOBAL_ACTION_SEED_BASE = "2026062601_official_goal_object_h10_basic"

TASKS = [
    (0, "open_the_middle_drawer_of_the_cabinet", "open the middle drawer of the cabinet"),
    (1, "put_the_bowl_on_the_stove", "put the bowl on the stove"),
    (2, "put_the_wine_bottle_on_top_of_the_cabinet", "put the wine bottle on top of the cabinet"),
    (3, "open_the_top_drawer_and_put_the_bowl_inside", "open the top drawer and put the bowl inside"),
    (4, "put_the_bowl_on_top_of_the_cabinet", "put the bowl on top of the cabinet"),
    (5, "push_the_plate_to_the_front_of_the_stove", "push the plate to the front of the stove"),
    (6, "put_the_cream_cheese_in_the_bowl", "put the cream cheese in the bowl"),
    (7, "turn_on_the_stove", "turn on the stove"),
    (8, "put_the_bowl_on_the_plate", "put the bowl on the plate"),
    (9, "put_the_wine_bottle_on_the_rack", "put the wine bottle on the rack"),
]


for p in [SIMVLA_SRC, LIBERO_PRO_SRC, ASYNCHVLA_SRC]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

_orig_torch_load = torch.load
torch.load = lambda *args, **kwargs: _orig_torch_load(*args, **{**kwargs, "weights_only": False})

from data_collection_stage9.libero_pro_env_utils import obs_images, obs_to_proprio
from data_collection_stage9.simvla_candidate_sampler import load_simvla, sample_candidate

try:
    from libero.envs import OffScreenRenderEnv
except ImportError:
    from libero.libero.envs import OffScreenRenderEnv


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def parse_bddl_instruction(path: Path) -> str:
    text = path.read_text()
    match = re.search(r"\(:language\s+(.*?)\)", text, re.DOTALL)
    if not match:
        return ""
    raw = match.group(1).strip()
    if raw.startswith('"') and raw.endswith('"'):
        return raw[1:-1].strip()
    return raw


def deterministic_action_seed(uid: str, policy_timestep: int, chunk_index: int) -> int:
    raw = f"{GLOBAL_ACTION_SEED_BASE}|{uid}|{policy_timestep}|{chunk_index}".encode()
    return int(hashlib.sha256(raw).hexdigest()[:8], 16) % (2**31)


def append_jsonl(path: Path, row: dict) -> None:
    with path.open("a") as f:
        f.write(json.dumps(row) + "\n")


def build_manifest(episodes_per_task: int, seed_base: int) -> list[dict]:
    rng = random.Random(seed_base)
    rows = []
    seen_seeds = set()
    order = 0
    for init_idx in range(episodes_per_task):
        for task_id, stem, desc in TASKS:
            eval_seed = rng.randrange(1_000_000, 2_147_000_000)
            while eval_seed in seen_seeds:
                eval_seed = rng.randrange(1_000_000, 2_147_000_000)
            seen_seeds.add(eval_seed)
            bddl = BDDL_DIR / f"{stem}.bddl"
            init = INIT_DIR / f"{stem}.pruned_init"
            rows.append(
                {
                    "episode_uid": f"{SUITE_NAME}::task{task_id:02d}::init{init_idx:03d}::seed{eval_seed}",
                    "execution_order": order,
                    "suite_name": SUITE_NAME,
                    "task_id": task_id,
                    "task_stem": stem,
                    "task_description": desc,
                    "initial_state_index": init_idx,
                    "eval_seed": eval_seed,
                    "bddl_path": str(bddl),
                    "bddl_sha256": sha256_file(bddl),
                    "init_state_path": str(init),
                    "init_state_sha256": sha256_file(init),
                }
            )
            order += 1
    return rows


def write_manifest(out_dir: Path, rows: list[dict], max_steps: int, episodes_per_task: int, seed_base: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "episode_manifest.csv"
    with manifest_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / "run_manifest.json").write_text(
        json.dumps(
            {
                "suite_name": SUITE_NAME,
                "bddl_dir": str(BDDL_DIR),
                "init_dir": str(INIT_DIR),
                "episodes_per_task": episodes_per_task,
                "total_episodes": len(rows),
                "task_count": len(TASKS),
                "init_state_coverage": "0..49 exactly once per task" if episodes_per_task == 50 else f"0..{episodes_per_task - 1}",
                "task_order": TASKS,
                "execution_order": "round_robin_by_init_state_then_task",
                "policy": "official SimVLA checkpoint, fixed receding H10",
                "checkpoint_path": str(CHECKPOINT_PATH),
                "checkpoint_sha256": sha256_file(CHECKPOINT_PATH / "model.safetensors"),
                "expected_checkpoint_sha256": EXPECTED_CKPT_HASH,
                "norm_stats_path": str(NORM_STATS_PATH),
                "max_steps": max_steps,
                "num_steps_wait": 10,
                "eval_seed_base": seed_base,
                "action_seed_base": GLOBAL_ACTION_SEED_BASE,
                "created_unix_time": time.time(),
            },
            indent=2,
        )
    )


def load_completed(path: Path) -> set[str]:
    done = set()
    if not path.exists():
        return done
    with path.open() as f:
        for line in f:
            if not line.strip():
                continue
            try:
                done.add(json.loads(line)["episode_uid"])
            except Exception:
                continue
    return done


def make_env(bddl_path: Path, eval_seed: int):
    env = OffScreenRenderEnv(
        bddl_file_name=str(bddl_path),
        camera_heights=128,
        camera_widths=128,
    )
    env.seed(int(eval_seed))
    return env


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes-per-task", type=int, default=50)
    parser.add_argument("--max-steps", type=int, default=800)
    parser.add_argument("--seed-base", type=int, default=2026062601)
    parser.add_argument("--output-root", type=Path, default=OUT_ROOT)
    parser.add_argument("--limit", type=int, default=0, help="Optional early stop after N manifest rows for smoke testing.")
    args = parser.parse_args()

    out_dir = args.output_root
    summaries_path = out_dir / "episode_summaries.jsonl"
    events_path = out_dir / "chunk_events.jsonl"
    live_status_path = out_dir / "live_status.json"
    out_dir.mkdir(parents=True, exist_ok=True)

    for task_id, stem, _ in TASKS:
        bddl = BDDL_DIR / f"{stem}.bddl"
        init = INIT_DIR / f"{stem}.pruned_init"
        if not bddl.exists() or not init.exists():
            raise FileNotFoundError(f"Missing official suite file for task {task_id}: {bddl} / {init}")
        states = torch.load(init, map_location="cpu", weights_only=False)
        if len(states) < args.episodes_per_task:
            raise RuntimeError(f"Task {task_id} only has {len(states)} init states, need {args.episodes_per_task}")

    ckpt_hash = sha256_file(CHECKPOINT_PATH / "model.safetensors")
    print(f"Checkpoint: {CHECKPOINT_PATH}")
    print(f"Checkpoint SHA256: {ckpt_hash}")
    if ckpt_hash != EXPECTED_CKPT_HASH:
        raise RuntimeError(f"Checkpoint hash mismatch: expected {EXPECTED_CKPT_HASH}, got {ckpt_hash}")

    rows = build_manifest(args.episodes_per_task, args.seed_base)
    write_manifest(out_dir, rows, args.max_steps, args.episodes_per_task, args.seed_base)
    if args.limit:
        rows = rows[: args.limit]

    completed = load_completed(summaries_path)
    print(f"Loaded {len(completed)} completed episodes from {summaries_path}")
    print("Loading official SimVLA checkpoint...")
    model, proc, device = load_simvla(
        ckpt=str(CHECKPOINT_PATH),
        norm_stats=str(NORM_STATS_PATH),
        smolvlm=str(SMOLVLM_CACHE),
    )
    print(f"Loaded model on {device}; action_horizon={getattr(model, 'action_horizon', 'N/A')}")

    total = len(rows)
    for i, row in enumerate(rows, start=1):
        uid = row["episode_uid"]
        if uid in completed:
            print(f"[skip] {i}/{total} {uid}")
            continue

        task_id = int(row["task_id"])
        init_idx = int(row["initial_state_index"])
        eval_seed = int(row["eval_seed"])
        bddl_path = Path(row["bddl_path"])
        init_path = Path(row["init_state_path"])
        bddl_hash = sha256_file(bddl_path)
        init_hash = sha256_file(init_path)
        if bddl_hash != row["bddl_sha256"] or init_hash != row["init_state_sha256"]:
            raise RuntimeError(f"Hash drift detected for {uid}")

        instruction = parse_bddl_instruction(bddl_path)
        print(f"\n[{i}/{total}] task={task_id} init={init_idx} seed={eval_seed} instruction={instruction}", flush=True)

        random.seed(eval_seed)
        np.random.seed(eval_seed)
        torch.manual_seed(eval_seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(eval_seed)

        env = None
        success = False
        terminal_done = False
        error_msg = ""
        policy_step = 0
        chunk_idx = 0
        start = time.time()
        try:
            env = make_env(bddl_path, eval_seed)
            init_states = torch.load(init_path, map_location="cpu", weights_only=False)
            obs = env.reset()
            maybe_obs = env.set_init_state(init_states[init_idx])
            if maybe_obs is not None:
                obs = maybe_obs
            for _ in range(10):
                obs, _, _, _ = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float32))

            while policy_step < args.max_steps and not success and not terminal_done:
                action_seed = deterministic_action_seed(uid, policy_step, chunk_idx)
                img, wrist = obs_images(obs)
                prop = obs_to_proprio(obs)
                cand = sample_candidate(
                    model,
                    proc,
                    instruction,
                    img,
                    wrist,
                    prop,
                    seed=int(action_seed),
                    device=device,
                    steps=10,
                    flowtrace=False,
                )
                chunk_env = cand["candidate_action_env"].detach().cpu().numpy()
                chunk_norm = cand["candidate_action_normalized"].detach().cpu().numpy()
                if chunk_env.shape != (10, 7):
                    raise RuntimeError(f"Expected H10 action chunk shape (10, 7), got {chunk_env.shape}")

                rewards = []
                dones = []
                successes = []
                before = policy_step
                executed = 0
                for h in range(10):
                    obs, rew, terminal_done, _info = env.step(chunk_env[h].astype(np.float32))
                    policy_step += 1
                    executed += 1
                    step_success = bool(rew > 0)
                    if hasattr(env, "_check_success"):
                        step_success = bool(step_success or env._check_success())
                    rewards.append(float(rew))
                    dones.append(bool(terminal_done))
                    successes.append(bool(step_success))
                    if step_success or terminal_done or policy_step >= args.max_steps:
                        success = bool(step_success)
                        break

                append_jsonl(
                    events_path,
                    {
                        "episode_uid": uid,
                        "suite_name": SUITE_NAME,
                        "task_id": task_id,
                        "task_description": row["task_description"],
                        "initial_state_index": init_idx,
                        "eval_seed": eval_seed,
                        "chunk_index": chunk_idx,
                        "policy_timestep_before": before,
                        "policy_timestep_after": policy_step,
                        "action_seed": int(action_seed),
                        "horizon": 10,
                        "actions_executed": executed,
                        "full_denormalized_chunk": chunk_env.tolist(),
                        "full_normalized_chunk": chunk_norm.tolist(),
                        "rewards": rewards,
                        "dones": dones,
                        "successes": successes,
                    },
                )
                chunk_idx += 1
        except Exception as exc:
            import traceback

            error_msg = repr(exc)
            traceback.print_exc()
        finally:
            if env is not None:
                env.close()

        wall = time.time() - start
        summary = {
            "episode_uid": uid,
            "suite_name": SUITE_NAME,
            "policy": "simvla_official_basic_h10",
            "task_id": task_id,
            "task_stem": row["task_stem"],
            "task_description": row["task_description"],
            "initial_state_index": init_idx,
            "eval_seed": eval_seed,
            "success": bool(success),
            "outcome": "success" if success else "failure",
            "terminal_done": bool(terminal_done),
            "timeout": bool(policy_step >= args.max_steps and not success),
            "policy_environment_steps": int(policy_step),
            "max_steps": int(args.max_steps),
            "num_chunk_queries": int(chunk_idx),
            "bddl_path": str(bddl_path),
            "bddl_sha256": bddl_hash,
            "init_state_path": str(init_path),
            "init_state_sha256": init_hash,
            "instruction": instruction,
            "checkpoint_path": str(CHECKPOINT_PATH),
            "checkpoint_sha256": ckpt_hash,
            "wall_time_seconds": float(wall),
            "error_message": error_msg,
        }
        append_jsonl(summaries_path, summary)
        completed.add(uid)

        live_status_path.write_text(
            json.dumps(
                {
                    "completed": len(completed),
                    "target": total,
                    "last_episode": summary,
                    "updated_unix_time": time.time(),
                },
                indent=2,
            )
        )
        print(
            f"[done] {uid} success={success} steps={policy_step} chunks={chunk_idx} wall={wall:.1f}s error={error_msg}",
            flush=True,
        )


if __name__ == "__main__":
    main()
