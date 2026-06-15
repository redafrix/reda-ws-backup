from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from pathlib import Path
from typing import Any

import numpy as np

from .collect_outcome_advantage_dataset import generate_chunk, git_hash, save_png
from .history_buffer import HistoryBuffer
from .libero_pro_env_utils import check_success, make_env, obs_images, obs_to_proprio, reset_to_init, suite_perturbation_type
from .outcome_metrics import contact_summary, detect_phase, object_body_positions
from .sim_state_utils import get_sim, get_state, save_state_npz
from .simvla_candidate_sampler import load_simvla
from .task_parser import parse_task_context


DEFAULT_REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def safe_info(info: dict[str, Any] | None) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in (info or {}).items():
        if isinstance(value, (bool, int, float, str)) or value is None:
            out[str(key)] = value
        elif isinstance(value, np.generic):
            out[str(key)] = value.item()
        elif hasattr(value, "tolist"):
            try:
                out[str(key)] = value.tolist()
            except Exception:
                out[str(key)] = str(value)[:500]
        else:
            out[str(key)] = str(value)[:500]
    return out


def save_obs_npz(path: Path, obs: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {}
    skipped: dict[str, str] = {}
    for key, value in obs.items():
        try:
            arr = np.asarray(value)
            if arr.dtype.kind in {"O", "U", "S"}:
                skipped[str(key)] = str(value)[:500]
            else:
                payload[str(key)] = arr
        except Exception as exc:
            skipped[str(key)] = f"{type(exc).__name__}: {exc}"
    payload["_obs_keys_json"] = np.array(json.dumps(sorted(obs.keys())))
    payload["_skipped_json"] = np.array(json.dumps(skipped, sort_keys=True))
    np.savez_compressed(path, **payload)
    return str(path)


def sim_model_summary(env) -> dict[str, Any]:
    sim = get_sim(env)
    if sim is None:
        return {"sim_available": False}
    model = getattr(sim, "model", None)
    data = getattr(sim, "data", None)
    out: dict[str, Any] = {"sim_available": True}
    for attr in ["body_names", "geom_names", "joint_names", "camera_names", "site_names", "actuator_names"]:
        try:
            out[attr] = [str(x) for x in getattr(model, attr)]
        except Exception:
            out[attr] = []
    for attr in ["nq", "nv", "nu", "nbody", "ngeom", "njnt", "ncam", "nsite"]:
        try:
            out[attr] = int(getattr(model, attr))
        except Exception:
            pass
    if data is not None:
        for attr in ["qpos", "qvel", "ctrl"]:
            try:
                out[f"initial_{attr}_shape"] = list(np.asarray(getattr(data, attr)).shape)
            except Exception:
                pass
    return out


def run_episode(
    *,
    env,
    model,
    proc,
    lang: str,
    device,
    init_state,
    task_context: dict[str, Any],
    suite: str,
    task_id: int,
    rollout_idx: int,
    policy_seed: int,
    args: argparse.Namespace,
    record_dir: Path | None,
) -> dict[str, Any]:
    obs = reset_to_init(env, init_state, warmup=args.warmup)
    hist = HistoryBuffer(args.history_k)
    success = False
    done_seen = False
    reward_sum = 0.0
    step_rows: list[dict[str, Any]] = []
    parent_chunk = None
    parent_norm = None
    parent_chunk_index = -1
    parent_chunk_pos = 0
    code_version = git_hash()
    episode_id = f"{suite}_t{task_id}_r{rollout_idx}_pseed{policy_seed}"

    if record_dir is not None:
        if record_dir.exists():
            shutil.rmtree(record_dir)
        for sub in ["obs_npz", "states", "images"]:
            (record_dir / sub).mkdir(parents=True, exist_ok=True)
        write_json(record_dir / "episode_metadata.json", {
            "schema_version": "stage9_raw_failure_episode_metadata_v1",
            "episode_id": episode_id,
            "suite": suite,
            "task_id": int(task_id),
            "task_language": lang,
            "perturbation_type": suite_perturbation_type(suite),
            "rollout_idx": int(rollout_idx),
            "policy_seed": int(policy_seed),
            "parent_max_steps": int(args.parent_max_steps),
            "parent_policy_chunk_steps": int(args.parent_policy_chunk_steps),
            "history_k": int(args.history_k),
            "task_context": task_context,
            "sim_model_summary": sim_model_summary(env),
            "code_version": code_version,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "label_policy": "raw_parent_episode_only_no_action_labels",
            "failure_definition": "episode_success_false_after_parent_max_steps_or_done_without_success",
        })

    for env_step in range(args.parent_max_steps):
        if parent_chunk is None or parent_chunk_pos >= len(parent_chunk):
            parent_chunk_index += 1
            parent_chunk_pos = 0
            chunk_seed = policy_seed + parent_chunk_index
            parent_chunk, parent_norm, _flow = generate_chunk(
                model,
                proc,
                lang,
                obs,
                seed=chunk_seed,
                device=device,
                steps=args.parent_policy_chunk_steps,
                flowtrace=False,
            )
        else:
            chunk_seed = policy_seed + parent_chunk_index

        action = np.asarray(parent_chunk[parent_chunk_pos], dtype=np.float32)
        action_norm = None
        if parent_norm is not None and parent_chunk_pos < len(parent_norm):
            action_norm = np.asarray(parent_norm[parent_chunk_pos], dtype=np.float32)

        before_obs = obs
        before_state = get_state(env)
        before_objects = object_body_positions(env)
        before_contact = contact_summary(env)
        phase = detect_phase(before_obs, env, task_context)
        before_success = bool(check_success(env))

        before_obs_path = before_state_path = before_agent_path = before_wrist_path = None
        if record_dir is not None:
            before_obs_path = save_obs_npz(record_dir / "obs_npz" / f"step_{env_step:04d}_before_obs.npz", before_obs)
            before_state_path = save_state_npz(record_dir / "states" / f"step_{env_step:04d}_before_state.npz", before_state)
            img, wrist = obs_images(before_obs)
            before_agent_path = save_png(record_dir / "images" / f"step_{env_step:04d}_before_agent.png", img)
            before_wrist_path = save_png(record_dir / "images" / f"step_{env_step:04d}_before_wrist.png", wrist)

        obs, reward, done, info = env.step(action)
        after_objects = object_body_positions(env)
        after_contact = contact_summary(env)
        after_success = bool(check_success(env))
        reward = float(reward)
        reward_sum += reward
        success = bool(success or after_success or reward > 0.0)
        done_seen = bool(done_seen or done)

        after_obs_path = after_state_path = after_agent_path = after_wrist_path = None
        if record_dir is not None:
            after_obs_path = save_obs_npz(record_dir / "obs_npz" / f"step_{env_step:04d}_after_obs.npz", obs)
            after_state_path = save_state_npz(record_dir / "states" / f"step_{env_step:04d}_after_state.npz", get_state(env))
            img, wrist = obs_images(obs)
            after_agent_path = save_png(record_dir / "images" / f"step_{env_step:04d}_after_agent.png", img)
            after_wrist_path = save_png(record_dir / "images" / f"step_{env_step:04d}_after_wrist.png", wrist)

        row = {
            "schema_version": "stage9_raw_failure_episode_step_v1",
            "episode_id": episode_id,
            "env_step": int(env_step),
            "phase_before": phase,
            "parent_chunk_index": int(parent_chunk_index),
            "parent_chunk_position": int(parent_chunk_pos),
            "parent_chunk_seed": int(chunk_seed),
            "action_env": action.tolist(),
            "action_normalized": action_norm.tolist() if action_norm is not None else None,
            "reward": reward,
            "done": bool(done),
            "success_before": before_success,
            "success_after": after_success,
            "cumulative_success": bool(success),
            "cumulative_reward_sum": float(reward_sum),
            "info": safe_info(info),
            "before_proprio": obs_to_proprio(before_obs).tolist(),
            "after_proprio": obs_to_proprio(obs).tolist(),
            "before_object_positions": before_objects,
            "after_object_positions": after_objects,
            "before_contact": before_contact,
            "after_contact": after_contact,
            "history_before": hist.to_list(),
            "paths": {
                "before_obs_npz": before_obs_path,
                "after_obs_npz": after_obs_path,
                "before_state_npz": before_state_path,
                "after_state_npz": after_state_path,
                "before_agent_image": before_agent_path,
                "before_wrist_image": before_wrist_path,
                "after_agent_image": after_agent_path,
                "after_wrist_image": after_wrist_path,
            },
        }
        step_rows.append(row)
        if record_dir is not None:
            append_jsonl(record_dir / "steps.jsonl", [row])

        hist.append({
            "env_step": int(env_step),
            "reward": reward,
            "success": bool(success),
            "phase": phase,
            "proprio": obs_to_proprio(obs).tolist(),
            "executed_action": action.tolist(),
        })
        parent_chunk_pos += 1
        if done or success:
            break

    summary = {
        "schema_version": "stage9_raw_failure_episode_summary_v1",
        "episode_id": episode_id,
        "suite": suite,
        "task_id": int(task_id),
        "task_language": lang,
        "perturbation_type": suite_perturbation_type(suite),
        "rollout_idx": int(rollout_idx),
        "policy_seed": int(policy_seed),
        "episode_steps": len(step_rows),
        "episode_success": bool(success),
        "episode_done": bool(done_seen),
        "episode_timeout": bool((not success) and (not done_seen) and len(step_rows) >= args.parent_max_steps),
        "episode_failure": bool(not success),
        "episode_reward_sum": float(reward_sum),
        "recorded": bool(record_dir is not None),
        "record_dir": str(record_dir) if record_dir is not None else None,
        "task_context": task_context,
        "phase_counts": {},
        "code_version": code_version,
        "completed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    phases: dict[str, int] = {}
    for row in step_rows:
        phases[row["phase_before"]] = phases.get(row["phase_before"], 0) + 1
    summary["phase_counts"] = phases
    if record_dir is not None:
        write_json(record_dir / "summary.json", summary)
    return summary


def collect(args: argparse.Namespace) -> None:
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "episodes").mkdir(exist_ok=True)
    (outdir / "scout").mkdir(exist_ok=True)

    model, proc, device = load_simvla()
    accepted_failures = 0
    episodes_total = 0
    summaries: list[dict[str, Any]] = []
    failure_summaries: list[dict[str, Any]] = []

    for suite in args.suites:
        for task_id in args.task_ids:
            if accepted_failures >= args.max_failure_episodes:
                break
            try:
                env, bundle = make_env(suite, task_id, args.resolution, seed=args.env_seed)
            except Exception as exc:
                append_jsonl(outdir / "errors.jsonl", [{"suite": suite, "task_id": int(task_id), "error": str(exc)}])
                continue
            init_states = bundle["init_states"]
            lang = bundle["task"].language
            obs0 = reset_to_init(env, init_states[0], warmup=args.warmup)
            task_context = parse_task_context(lang, obs0, all_bodies=list(object_body_positions(env).keys()))
            for rollout_idx in range(min(args.rollouts_per_task, len(init_states))):
                if accepted_failures >= args.max_failure_episodes or episodes_total >= args.max_parent_episodes:
                    break
                policy_seed = args.policy_seed_base + episodes_total
                init_state = init_states[rollout_idx % len(init_states)]
                scout = run_episode(
                    env=env,
                    model=model,
                    proc=proc,
                    lang=lang,
                    device=device,
                    init_state=init_state,
                    task_context=task_context,
                    suite=suite,
                    task_id=task_id,
                    rollout_idx=rollout_idx,
                    policy_seed=policy_seed,
                    args=args,
                    record_dir=None,
                )
                episodes_total += 1
                summaries.append(scout)
                append_jsonl(outdir / "scout" / "episode_scout_summaries.jsonl", [scout])
                print(
                    f"scout {scout['episode_id']} success={scout['episode_success']} steps={scout['episode_steps']} failures={accepted_failures}/{args.max_failure_episodes}",
                    flush=True,
                )
                if scout["episode_success"]:
                    continue

                episode_dir = outdir / "episodes" / scout["episode_id"]
                recorded = run_episode(
                    env=env,
                    model=model,
                    proc=proc,
                    lang=lang,
                    device=device,
                    init_state=init_state,
                    task_context=task_context,
                    suite=suite,
                    task_id=task_id,
                    rollout_idx=rollout_idx,
                    policy_seed=policy_seed,
                    args=args,
                    record_dir=episode_dir,
                )
                append_jsonl(outdir / "raw_failure_episode_summaries.jsonl", [recorded])
                if recorded["episode_success"]:
                    append_jsonl(outdir / "errors.jsonl", [{
                        "episode_id": recorded["episode_id"],
                        "error": "scout_failed_but_recorded_success",
                        "summary": recorded,
                    }])
                    continue
                accepted_failures += 1
                failure_summaries.append(recorded)
                print(
                    f"recorded_failure {recorded['episode_id']} steps={recorded['episode_steps']} failures={accepted_failures}/{args.max_failure_episodes}",
                    flush=True,
                )

    final = {
        "schema_version": "stage9_raw_failure_collection_v1",
        "out_dir": str(outdir),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "max_failure_episodes": int(args.max_failure_episodes),
        "parent_max_steps": int(args.parent_max_steps),
        "parent_policy_chunk_steps": int(args.parent_policy_chunk_steps),
        "history_k": int(args.history_k),
        "episodes_scouted": int(episodes_total),
        "failures_recorded": int(accepted_failures),
        "failure_episode_ids": [row["episode_id"] for row in failure_summaries],
        "failure_summaries": failure_summaries,
        "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    write_json(outdir / "summary.json", final)
    print(json.dumps(final, indent=2, sort_keys=True), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug", "libero_object_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5])
    parser.add_argument("--max-failure-episodes", type=int, default=5)
    parser.add_argument("--max-parent-episodes", type=int, default=80)
    parser.add_argument("--rollouts-per-task", type=int, default=20)
    parser.add_argument("--parent-max-steps", type=int, default=400)
    parser.add_argument("--parent-policy-chunk-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--policy-seed-base", type=int, default=2026052100)
    parser.add_argument("--env-seed", type=int, default=20260521)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes/raw_failure_episodes_v1"),
    )
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
