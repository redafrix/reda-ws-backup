from __future__ import annotations

import argparse
import json
import os
import random
import time
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

from .collect_outcome_advantage_dataset import execute_policy_continuation, generate_chunk, git_hash, save_png
from .collect_failed_episode_mining_v2 import add_continuous_label, strip_private
from .history_buffer import HistoryBuffer
from .libero_pro_env_utils import check_success, make_env, obs_images, obs_to_proprio, reset_to_init, suite_perturbation_type
from .local_chunk_quality import score_state_group, summarize_state_group_risks
from .outcome_metrics import contact_summary, compute_delta, detect_phase, execute_action_chunk, object_body_positions
from .sim_state_utils import get_state, save_state_npz, set_state
from .simvla_candidate_sampler import load_simvla
from .task_parser import parse_task_context


DEFAULT_REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        for row in rows:
            f.write(json.dumps(row, default=str) + "\n")


def episode_key(suite: str, task_id: int, rollout_idx: int, policy_seed: int) -> str:
    return f"{suite}_t{task_id}_r{rollout_idx}_pseed{policy_seed}"


def make_replay_seeds(args: argparse.Namespace) -> list[int]:
    if args.replay_seeds:
        return [int(s) for s in args.replay_seeds]
    rng = random.Random(args.replay_seed_base)
    seeds: list[int] = []
    seen: set[int] = set()
    while len(seeds) < args.num_replay_seeds:
        value = rng.randrange(1, 2_147_483_000)
        if value not in seen:
            seen.add(value)
            seeds.append(value)
    return seeds


def add_parent_record(
    *,
    dense_states: list[dict[str, Any]],
    outdir: Path,
    suite: str,
    task_id: int,
    lang: str,
    task_context: dict[str, Any],
    episode_id: str,
    rollout_idx: int,
    policy_seed: int,
    env_step: int,
    parent_chunk_index: int,
    parent_chunk_pos: int,
    parent_chunk_seed: int,
    phase: str,
    before_state: dict[str, Any],
    before_obs: dict[str, Any],
    before_obj: dict[str, Any],
    history: list[dict[str, Any]],
    parent_action: np.ndarray,
    parent_action_norm: np.ndarray | None,
    code_version: str,
) -> None:
    state_id = f"{episode_id}_envstep{env_step:04d}_state"
    dense_states.append({
        "schema_version": "stage9_dense_parent_timestep_v2",
        "sample_id": f"{episode_id}_envstep{env_step:04d}_parent",
        "metadata": {
            "task_name": f"{suite}_task{task_id}",
            "task_language": lang,
            "libero_pro_suite_or_task": suite,
            "perturbation_type": suite_perturbation_type(suite),
            "episode_id": episode_id,
            "rollout_index": int(rollout_idx),
            "policy_seed": int(policy_seed),
            "env_step": int(env_step),
            "parent_chunk_index": int(parent_chunk_index),
            "parent_chunk_position": int(parent_chunk_pos),
            "parent_chunk_seed": int(parent_chunk_seed),
            "parent_phase": phase,
            "state_id": state_id,
            "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "code_version": code_version,
        },
        "history": history,
        "current": {
            "proprio": obs_to_proprio(before_obs).tolist(),
            "object_positions_before": before_obj,
            "task_context": task_context,
        },
        "parent_policy_action": {
            "action_env": parent_action.tolist() if hasattr(parent_action, "tolist") else parent_action,
            "action_normalized": parent_action_norm.tolist() if hasattr(parent_action_norm, "tolist") else parent_action_norm,
        },
        "_runtime_before_state": before_state,
        "_runtime_before_obs": before_obs,
    })


def run_parent_episode_dense(
    env,
    model,
    proc,
    lang: str,
    device,
    outdir: Path,
    suite: str,
    task_id: int,
    task_context: dict[str, Any],
    init_state,
    rollout_idx: int,
    policy_seed: int,
    args: argparse.Namespace,
    code_version: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    episode_id = episode_key(suite, task_id, rollout_idx, policy_seed)
    obs = reset_to_init(env, init_state, warmup=args.warmup)
    hist = HistoryBuffer(args.history_k)
    dense_states: list[dict[str, Any]] = []
    reward_sum = 0.0
    success = False
    done = False
    parent_chunk: np.ndarray | None = None
    parent_norm: np.ndarray | None = None
    parent_chunk_index = -1
    parent_chunk_pos = 0
    parent_chunk_seed = policy_seed

    for env_step in range(args.parent_max_steps):
        if parent_chunk is None or parent_chunk_pos >= len(parent_chunk):
            parent_chunk_index += 1
            parent_chunk_pos = 0
            parent_chunk_seed = policy_seed + parent_chunk_index
            parent_chunk, parent_norm, _flow = generate_chunk(
                model,
                proc,
                lang,
                obs,
                seed=parent_chunk_seed,
                device=device,
                steps=args.parent_policy_chunk_steps,
                flowtrace=False,
            )

        action = np.asarray(parent_chunk[parent_chunk_pos], dtype=np.float32)
        action_norm = parent_norm[parent_chunk_pos] if parent_norm is not None and parent_chunk_pos < len(parent_norm) else None
        phase = detect_phase(obs, env, task_context)
        before_state = get_state(env)
        before_obs = obs
        before_obj = object_body_positions(env)

        stop_step = args.stop_step if args.stop_step >= 0 else args.parent_max_steps - args.eval_horizon
        if env_step >= args.start_step and env_step <= stop_step and ((env_step - args.start_step) % args.state_stride == 0):
            add_parent_record(
                dense_states=dense_states,
                outdir=outdir,
                suite=suite,
                task_id=task_id,
                lang=lang,
                task_context=task_context,
                episode_id=episode_id,
                rollout_idx=rollout_idx,
                policy_seed=policy_seed,
                env_step=env_step,
                parent_chunk_index=parent_chunk_index,
                parent_chunk_pos=parent_chunk_pos,
                parent_chunk_seed=parent_chunk_seed,
                phase=phase,
                before_state=before_state,
                before_obs=before_obs,
                before_obj=before_obj,
                history=hist.to_list(),
                parent_action=action,
                parent_action_norm=action_norm,
                code_version=code_version,
            )

        outcome, obs = execute_action_chunk(
            env,
            np.asarray([action], dtype=np.float32),
            1,
            before_obs,
            task_context=task_context,
            return_after_obs=True,
            save_full_trace=False,
        )
        reward = float(outcome.get("reward_sum_H") or 0.0)
        reward_sum += reward
        success = bool(success or outcome.get("success_after") or outcome.get("success_within_H") or check_success(env) or reward > 0)
        done = bool(outcome.get("done_within_H"))
        hist.append({
            "env_step": int(env_step),
            "reward_sum": reward,
            "success": bool(success),
            "phase": phase,
            "proprio": obs_to_proprio(obs).tolist(),
            "executed_action": action.tolist(),
        })
        parent_chunk_pos += 1
        if success or done:
            break

    summary = {
        "episode_id": episode_id,
        "suite": suite,
        "task_id": int(task_id),
        "rollout_index": int(rollout_idx),
        "policy_seed": int(policy_seed),
        "episode_success": bool(success),
        "episode_done": bool(done),
        "episode_timeout": bool((not success) and (not done)),
        "episode_reward_sum": float(reward_sum),
        "parent_steps": int(env_step + 1),
        "dense_state_count": len(dense_states),
        "start_step": int(args.start_step),
        "stop_step": int(args.stop_step if args.stop_step >= 0 else args.parent_max_steps - args.eval_horizon),
        "state_stride": int(args.state_stride),
        "parent_max_steps": int(args.parent_max_steps),
        "parent_policy_chunk_steps": int(args.parent_policy_chunk_steps),
    }
    for record in dense_states:
        env_step_i = int((record.get("metadata") or {}).get("env_step") or 0)
        distance_to_failure = max(0, int(summary["parent_steps"]) - env_step_i)
        record.setdefault("metadata", {})["parent_episode_failed_or_timeout"] = bool(not summary["episode_success"])
        record.setdefault("metadata", {})["distance_to_failure_or_timeout"] = int(distance_to_failure)
        record["episode_outcome"] = dict(summary)
        record["labeling_policy"] = {
            "label_target": "candidate_action_chunk_from_dense_timestep",
            "terminal_continuation_used_for_label": False,
            "episode_failure_used_for_label": False,
            "episode_failure_used_for_mining_only": True,
            "dense_every_timestep_failure_scan": args.state_stride == 1,
        }
    return summary, dense_states


def replay_dense_state(
    env,
    model,
    proc,
    lang: str,
    device,
    outdir: Path,
    task_context: dict[str, Any],
    parent_state: dict[str, Any],
    replay_seeds: list[int],
    args: argparse.Namespace,
    code_version: str,
) -> list[dict[str, Any]]:
    before_state = parent_state["_runtime_before_state"]
    before_obs = parent_state["_runtime_before_obs"]
    meta = parent_state["metadata"]
    state_id = str(meta["state_id"])

    set_state(env, before_state)
    state_path = save_state_npz(outdir / "states" / f"{state_id}.npz", before_state)
    before_agent, before_wrist = obs_images(before_obs)
    before_agent_path = save_png(outdir / "images" / f"{state_id}_before_agent.png", before_agent) if args.save_images else None
    before_wrist_path = save_png(outdir / "images" / f"{state_id}_before_wrist.png", before_wrist) if args.save_images and before_wrist is not None else None
    before_obj = parent_state.get("current", {}).get("object_positions_before") or object_body_positions(env)
    prop = obs_to_proprio(before_obs)

    samples: list[dict[str, Any]] = []
    for seed_value in replay_seeds:
        set_state(env, before_state)
        initial_chunk, norm, flow = generate_chunk(
            model,
            proc,
            lang,
            before_obs,
            seed=int(seed_value),
            device=device,
            steps=args.candidate_chunk_steps,
            flowtrace=True,
        )
        sid = f"{state_id}_seed{seed_value}"
        frame_dir = outdir / "trace_frames" / sid if args.save_trace_frames else None
        candidate_steps = min(args.candidate_chunk_steps, len(initial_chunk))
        eval_horizon = max(candidate_steps, int(args.eval_horizon))
        if eval_horizon > candidate_steps:
            outcome, after_obs, continuation_actions = execute_policy_continuation(
                env,
                model,
                proc,
                lang,
                device,
                initial_chunk[:candidate_steps],
                before_obs,
                task_context,
                eval_horizon=eval_horizon,
                terminal_horizon=eval_horizon,
                continuation_seed=int(seed_value) + 1_000_003,
                trace_frame_dir=frame_dir,
                trace_frame_stride=args.trace_frame_stride,
            )
            after_obj = object_body_positions(env)
            after_contact = contact_summary(env)
            htrace = outcome.get("horizon_trace") or {}
            rewards = htrace.get("rewards") or outcome.get("rewards") or []
            success_flags = htrace.get("success_flags") or []
            done_flags = htrace.get("done_flags") or []
            outcome.update({
                "H_used": int(len(rewards)),
                "steps_executed": int(len(rewards)),
                "rewards": rewards,
                "reward_sum_H": float(sum(rewards)),
                "nonzero_reward_count_H": int(sum(abs(float(r)) > 1e-8 for r in rewards)),
                "success_before": bool(outcome.get("success_before")),
                "success_after": bool(check_success(env)),
                "success_within_H": bool(any(success_flags) and not outcome.get("success_before")),
                "done_within_H": bool(any(done_flags)),
                "after_proprio": obs_to_proprio(after_obs).tolist(),
                "object_positions_after": after_obj,
                "contact_after": after_contact,
                "delta": compute_delta(before_obs, after_obs, before_obj, after_obj, task_context),
                "candidate_chunk_steps": int(candidate_steps),
                "eval_horizon_requested": int(eval_horizon),
                "policy_continuation_steps_after_candidate": int(max(0, len(rewards) - candidate_steps)),
                "policy_continuation_actions_audit": continuation_actions,
            })
        else:
            outcome, after_obs = execute_action_chunk(
                env,
                initial_chunk[:candidate_steps],
                candidate_steps,
                before_obs,
                task_context=task_context,
                return_after_obs=True,
                save_full_trace=True,
                trace_frame_dir=frame_dir,
                trace_frame_stride=args.trace_frame_stride,
            )
            outcome["candidate_chunk_steps"] = int(candidate_steps)
            outcome["eval_horizon_requested"] = int(eval_horizon)
            outcome["policy_continuation_steps_after_candidate"] = 0
            outcome["policy_continuation_actions_audit"] = []
        after_agent, after_wrist = obs_images(after_obs)
        after_agent_path = save_png(outdir / "images" / f"{sid}_after_agent.png", after_agent) if args.save_images else None
        after_wrist_path = save_png(outdir / "images" / f"{sid}_after_wrist.png", after_wrist) if args.save_images and after_wrist is not None else None
        sample = {
            "schema_version": "stage9_dense_failure_timestep_replay_candidate_v2",
            "_dataset_name": outdir.name,
            "sample_id": sid,
            "metadata": {
                "task_name": meta.get("task_name"),
                "task_language": lang,
                "libero_pro_suite_or_task": meta.get("libero_pro_suite_or_task"),
                "perturbation_type": meta.get("perturbation_type"),
                "episode_id": meta.get("episode_id"),
                "source_parent_timestep_sample_id": parent_state.get("sample_id"),
                "source_env_step": int(meta.get("env_step")),
                "distance_to_failure_or_timeout": int(meta.get("distance_to_failure_or_timeout", -1)),
                "parent_episode_failed_or_timeout": bool(meta.get("parent_episode_failed_or_timeout")),
                "source_parent_chunk_index": int(meta.get("parent_chunk_index")),
                "source_parent_chunk_position": int(meta.get("parent_chunk_position")),
                "window_selection_reason": "dense_failure_every_timestep",
                "parent_phase": meta.get("parent_phase"),
                "simvla_generation_seed": int(seed_value),
                "state_id": state_id,
                "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "code_version": code_version,
            },
            "history": parent_state.get("history") or [],
            "current": {
                "proprio": prop.tolist() if hasattr(prop, "tolist") else prop,
                "object_positions_before": before_obj,
                "sim_state_path": state_path,
                "before_image_path": before_agent_path,
                "before_wrist_image_path": before_wrist_path,
                "task_context": task_context,
            },
            "candidate_action": {
                "candidate_action_normalized": norm.tolist() if hasattr(norm, "tolist") else norm,
                "candidate_action_env": initial_chunk.tolist() if hasattr(initial_chunk, "tolist") else initial_chunk,
                "simvla_seed": int(seed_value),
                "target_action_chunk_steps": int(candidate_steps),
                "eval_horizon_steps": int(eval_horizon),
                "flowtrace_features": flow,
            },
            "outcome": outcome,
            "visual_evidence": {
                "after_image_path": after_agent_path,
                "after_wrist_image_path": after_wrist_path,
                "trace_frame_paths": (outcome.get("horizon_trace") or {}).get("frame_paths") or [],
            },
            "episode_outcome": parent_state.get("episode_outcome") or {},
            "labeling_policy": {
                "label_target": "initial_10_action_simvla_chunk",
                "terminal_continuation_used_for_label": False,
                "episode_failure_used_for_label": False,
                "episode_failure_used_for_mining_only": True,
                "same_state_replay_for_dense_timestep": True,
                "continuous_risk_primary": True,
                "policy_continuation_used_for_eval_horizon": bool(eval_horizon > candidate_steps),
                "terminal_success_failure_used_for_label": False,
                "eval_horizon_steps": int(eval_horizon),
            },
        }
        samples.append(sample)

    risks = score_state_group(samples)
    group_summary = summarize_state_group_risks(risks)
    for risk in risks:
        risk["same_state_group_summary_v2"] = group_summary
    for sample, risk in zip(samples, risks):
        add_continuous_label(sample, risk)
    return samples


def collect(args: argparse.Namespace) -> None:
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    for sub in ["states", "images", "trace_frames"]:
        (outdir / sub).mkdir(exist_ok=True)

    replay_seeds = make_replay_seeds(args)
    model, proc, device = load_simvla()
    code_version = git_hash()
    summary = Counter()
    replay_bins = Counter()
    group_types = Counter()
    subtype_counts = Counter()
    score_ranges: list[float] = []

    parent_path = outdir / "dense_parent_timesteps.jsonl"
    replay_path = outdir / "dense_replay_counterfactual_samples.jsonl"
    group_path = outdir / "dense_same_state_group_summaries.jsonl"
    episode_path = outdir / "dense_parent_episode_summaries.jsonl"

    for suite in args.suites:
        for task_id in args.task_ids:
            if summary["failure_episodes_mined"] >= args.max_failure_episodes:
                break
            try:
                env, bundle = make_env(suite, task_id, args.resolution, seed=args.env_seed)
            except Exception as exc:
                print(f"Skipping unavailable {suite}_t{task_id}: {exc}", flush=True)
                continue
            init_states = bundle["init_states"]
            lang = bundle["task"].language
            obs0 = reset_to_init(env, init_states[0], warmup=args.warmup)
            task_context = parse_task_context(lang, obs0, all_bodies=list(object_body_positions(env).keys()))
            print(f"Dense failure timestep mining {suite}_t{task_id}", flush=True)

            for rollout_idx in range(min(args.rollouts_per_task, len(init_states))):
                if summary["episodes_total"] >= args.max_parent_episodes:
                    break
                if summary["failure_episodes_mined"] >= args.max_failure_episodes:
                    break
                policy_seed = args.policy_seed_base + rollout_idx
                ep_summary, dense_states = run_parent_episode_dense(
                    env,
                    model,
                    proc,
                    lang,
                    device,
                    outdir,
                    suite,
                    task_id,
                    task_context,
                    init_states[rollout_idx % len(init_states)],
                    rollout_idx,
                    policy_seed,
                    args,
                    code_version,
                )
                append_jsonl(episode_path, [ep_summary])
                summary["episodes_total"] += 1
                if ep_summary["episode_success"]:
                    summary["episodes_success"] += 1
                    print(f"episode {ep_summary['episode_id']} success steps={ep_summary['parent_steps']}", flush=True)
                    continue

                summary["episodes_failed_or_timeout"] += 1
                summary["failure_episodes_mined"] += 1
                if args.max_replay_states and args.max_replay_states > 0:
                    dense_states = dense_states[: args.max_replay_states]
                append_jsonl(parent_path, [strip_private(s) for s in dense_states])
                summary["dense_states_replayed"] += len(dense_states)
                print(
                    f"failure {ep_summary['episode_id']} steps={ep_summary['parent_steps']} dense_states={len(dense_states)} seeds={len(replay_seeds)}",
                    flush=True,
                )
                for idx, parent_state in enumerate(dense_states):
                    samples = replay_dense_state(
                        env,
                        model,
                        proc,
                        lang,
                        device,
                        outdir,
                        task_context,
                        parent_state,
                        replay_seeds,
                        args,
                        code_version,
                    )
                    clean = [strip_private(s) for s in samples]
                    append_jsonl(replay_path, clean)
                    summary["replay_samples"] += len(clean)
                    group_summary = ((clean[0].get("label") or {}).get("same_state_group_summary_v2") or {}) if clean else {}
                    if group_summary:
                        row = {
                            "state_id": (parent_state.get("metadata") or {}).get("state_id"),
                            "episode_id": ep_summary["episode_id"],
                            "source_env_step": (parent_state.get("metadata") or {}).get("env_step"),
                            "parent_phase": (parent_state.get("metadata") or {}).get("parent_phase"),
                            **group_summary,
                        }
                        append_jsonl(group_path, [row])
                        group_types[str(group_summary.get("group_type"))] += 1
                        if group_summary.get("risk_score_range") is not None:
                            score_ranges.append(float(group_summary["risk_score_range"]))
                    for sample in clean:
                        label = sample.get("label") or {}
                        replay_bins[str(label.get("risk_bin"))] += 1
                        subtype_counts[str(label.get("bad_subtype"))] += 1
                    if (idx + 1) % args.progress_every_states == 0:
                        print(
                            f"replayed_states={idx + 1}/{len(dense_states)} samples={summary['replay_samples']} bins={dict(replay_bins)} groups={dict(group_types)}",
                            flush=True,
                        )
                        write_json(outdir / "summary_live.json", {
                            "summary_counts": dict(summary),
                            "replay_risk_bin_counts": dict(replay_bins),
                            "bad_subtype_counts": dict(subtype_counts),
                            "group_type_counts": dict(group_types),
                            "risk_score_range_max": max(score_ranges) if score_ranges else None,
                            "risk_score_range_mean": (sum(score_ranges) / len(score_ranges)) if score_ranges else None,
                        })

    final = {
        "schema_version": "stage9_dense_failure_timestep_mining_v2_summary",
        "out_dir": str(outdir),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "history_k": args.history_k,
        "parent_max_steps": args.parent_max_steps,
        "start_step": args.start_step,
        "stop_step": args.stop_step if args.stop_step >= 0 else args.parent_max_steps - args.eval_horizon,
        "state_stride": args.state_stride,
        "parent_policy_chunk_steps": args.parent_policy_chunk_steps,
        "candidate_chunk_steps": args.candidate_chunk_steps,
        "eval_horizon": args.eval_horizon,
        "num_replay_seeds": len(replay_seeds),
        "replay_seeds": replay_seeds,
        "terminal_continuation_used_for_label": False,
        "episode_failure_used_for_label": False,
        "summary_counts": dict(summary),
        "replay_risk_bin_counts": dict(replay_bins),
        "bad_subtype_counts": dict(subtype_counts),
        "group_type_counts": dict(group_types),
        "risk_score_range_max": max(score_ranges) if score_ranges else None,
        "risk_score_range_mean": (sum(score_ranges) / len(score_ranges)) if score_ranges else None,
    }
    write_json(outdir / "summary.json", final)
    print(json.dumps(final, indent=2, sort_keys=True), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug", "libero_object_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5])
    parser.add_argument("--rollouts-per-task", type=int, default=8)
    parser.add_argument("--max-parent-episodes", type=int, default=32)
    parser.add_argument("--max-failure-episodes", type=int, default=1)
    parser.add_argument("--parent-max-steps", type=int, default=400)
    parser.add_argument("--start-step", type=int, default=10)
    parser.add_argument("--stop-step", type=int, default=-1, help="Last parent env step to replay; default parent_max_steps - eval_horizon")
    parser.add_argument("--state-stride", type=int, default=1)
    parser.add_argument("--max-replay-states", type=int, default=0, help="0 means every dense state from failed episodes")
    parser.add_argument("--parent-policy-chunk-steps", type=int, default=10)
    parser.add_argument("--candidate-chunk-steps", type=int, default=10)
    parser.add_argument("--eval-horizon", type=int, default=10, help="Trace/scoring horizon. The target action remains the initial candidate chunk.")
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--policy-seed-base", type=int, default=0)
    parser.add_argument("--num-replay-seeds", type=int, default=20)
    parser.add_argument("--replay-seed-base", type=int, default=20260520)
    parser.add_argument("--replay-seeds", nargs="+", type=int, default=None)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed", type=int, default=7)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-trace-frames", action="store_true")
    parser.add_argument("--trace-frame-stride", type=int, default=5)
    parser.add_argument("--progress-every-states", type=int, default=5)
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data/data/probe/dense_failure_timestep_v2"),
    )
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
