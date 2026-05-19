from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

from .history_buffer import HistoryBuffer
from .label_rules import LABEL_AMBIGUOUS, LABEL_GOOD_STRONG, LABEL_GOOD_WEAK, label_outcome
from .libero_pro_env_utils import make_env, obs_images, obs_to_proprio, reset_to_init, suite_perturbation_type
from .outcome_metrics import detect_phase, eef_pos, execute_action_chunk, object_body_positions
from .sim_state_utils import get_state, save_state_npz, set_state
from .simvla_candidate_sampler import load_simvla, sample_candidate
from .strict_label_utils import LABEL_VALIDATED_BAD, same_state_summary
from .task_parser import parse_task_context


PHASES_OF_INTEREST = [
    "NEAR_GRASP",
    "GRASP_OR_LIFT",
    "TRANSPORT",
    "PLACE_OR_GOAL",
    "STUCK_OR_NO_PROGRESS",
]

BAD_SUBTYPE_ACTION_SPECIFIC = "action_specific"
BAD_SUBTYPE_STATE_CONTEXT = "state_context"
BAD_SUBTYPE_UNKNOWN = "unknown"
ALLOWED_BAD_SUBTYPES = {
    BAD_SUBTYPE_ACTION_SPECIFIC,
    BAD_SUBTYPE_STATE_CONTEXT,
    BAD_SUBTYPE_UNKNOWN,
}


def git_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def save_png(path: Path, img) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(img.astype(np.uint8)).save(path)
    return str(path)


def terminal_success(outcome: dict[str, Any]) -> bool:
    return bool(outcome.get("terminal_success") or outcome.get("success_within_H") or outcome.get("success_after"))


def terminal_failure(outcome: dict[str, Any]) -> bool:
    return bool(outcome.get("terminal_failure") or outcome.get("terminal_timeout"))


def rollout_quality(sample: dict[str, Any]) -> float:
    outcome = sample["outcome"]
    label = sample.get("raw_local_label", {})
    evidence = label.get("numeric_evidence", {})
    score = 0.0
    if terminal_success(outcome):
        score += 1000.0
    if terminal_failure(outcome):
        score -= 300.0
    score += 20.0 * float(outcome.get("reward_sum_H", 0.0))
    goal_delta = evidence.get("target_to_goal_delta")
    if goal_delta is not None:
        score += max(-80.0, min(80.0, -500.0 * float(goal_delta)))
    height_delta = evidence.get("target_height_delta")
    if height_delta is not None:
        score += max(-60.0, min(60.0, 400.0 * float(height_delta)))
    return score


def has_strong_progress(sample: dict[str, Any]) -> bool:
    raw = sample.get("raw_local_label") or {}
    outcome = sample.get("outcome") or {}
    if terminal_success(outcome):
        return True
    if raw.get("strong_good_evidence"):
        return True
    evidence = raw.get("numeric_evidence") or {}
    goal_delta = evidence.get("target_to_goal_delta")
    height_delta = evidence.get("target_height_delta")
    target_motion = evidence.get("target_motion")
    try:
        if goal_delta is not None and float(goal_delta) < -0.025:
            return True
        if height_delta is not None and target_motion is not None and float(height_delta) > 0.025 and float(target_motion) > 0.012:
            return True
    except (TypeError, ValueError):
        pass
    return False


def infer_bad_subtype(sample: dict[str, Any], siblings: list[dict[str, Any]]) -> tuple[str, dict[str, Any]]:
    if not terminal_failure(sample.get("outcome") or {}):
        return BAD_SUBTYPE_UNKNOWN, {"candidate_terminal_failure": False}
    other_samples = [s for s in siblings if s.get("sample_id") != sample.get("sample_id")]
    success_or_progress_alt = [s for s in other_samples if terminal_success(s.get("outcome") or {}) or has_strong_progress(s)]
    terminal_failures = [s for s in siblings if terminal_failure(s.get("outcome") or {})]
    no_progress_failures = [
        s for s in siblings
        if terminal_failure(s.get("outcome") or {}) and not has_strong_progress(s)
    ]
    majority_threshold = max(3, (len(siblings) + 1) // 2)
    evidence = {
        "candidate_terminal_failure": True,
        "num_siblings": len(siblings),
        "success_or_strong_progress_alternative_count": len(success_or_progress_alt),
        "terminal_failure_count": len(terminal_failures),
        "no_progress_failure_count": len(no_progress_failures),
        "majority_threshold": majority_threshold,
    }
    if success_or_progress_alt:
        return BAD_SUBTYPE_ACTION_SPECIFIC, evidence
    if len(no_progress_failures) >= majority_threshold:
        return BAD_SUBTYPE_STATE_CONTEXT, evidence
    return BAD_SUBTYPE_UNKNOWN, evidence


def generate_chunk(model, proc, lang, obs, seed: int, device, steps: int, flowtrace: bool):
    img, wrist = obs_images(obs)
    prop = obs_to_proprio(obs)
    cand = sample_candidate(model, proc, lang, img, wrist, prop, seed=seed, device=device, steps=steps, flowtrace=flowtrace)
    chunk = cand["candidate_action_env"].numpy().astype(np.float32)
    norm = cand["candidate_action_normalized"].numpy().astype(np.float32)
    flow = {k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in cand.get("flow_trace_summary", {}).items()}
    return chunk, norm, flow


def execute_policy_continuation(
    env,
    model,
    proc,
    lang: str,
    device,
    initial_chunk: np.ndarray,
    before_obs: dict,
    task_context: dict,
    eval_horizon: int,
    terminal_horizon: int,
    continuation_seed: int,
    trace_frame_dir: Path | None,
    trace_frame_stride: int,
) -> tuple[dict[str, Any], dict, list[list[float]]]:
    all_rewards = []
    continuation_actions = []
    obs = before_obs
    steps_done = 0
    terminal_success_seen = False
    done_seen = False
    chunks = [initial_chunk]
    chunk_index = 0
    aggregate_trace = {
        "schema_version": "stage9_horizon_trace_v2_chunked_policy",
        "requested_horizon": int(eval_horizon),
        "saved_action_steps": 0,
        "rewards": [],
        "success_flags": [],
        "done_flags": [],
        "eef_positions": [],
        "target_object_positions": [],
        "target_object_heights": [],
        "object_goal_distances": [],
        "eef_target_distances": [],
        "gripper_states": [],
        "contact_summaries": [],
        "frame_paths": [],
    }

    first_outcome = None
    while steps_done < terminal_horizon:
        if chunk_index >= len(chunks):
            chunk, _norm, _flow = generate_chunk(
                model,
                proc,
                lang,
                obs,
                seed=continuation_seed + chunk_index,
                device=device,
                steps=min(10, terminal_horizon - steps_done),
                flowtrace=False,
            )
            chunks.append(chunk)
            continuation_actions.extend(chunk.tolist())

        chunk = chunks[chunk_index]
        remaining = terminal_horizon - steps_done
        horizon_now = min(len(chunk), remaining)
        should_record_trace = steps_done < eval_horizon
        frame_dir = None
        if trace_frame_dir is not None and should_record_trace:
            frame_dir = trace_frame_dir / f"chunk_{chunk_index:02d}"
        outcome, obs = execute_action_chunk(
            env,
            chunk[:horizon_now],
            horizon_now,
            obs,
            task_context=task_context,
            return_after_obs=True,
            save_full_trace=should_record_trace,
            trace_frame_dir=frame_dir,
            trace_frame_stride=trace_frame_stride,
        )
        htrace = outcome.get("horizon_trace") or {}
        if steps_done < eval_horizon:
            keep = max(0, min(eval_horizon - steps_done, len(htrace.get("rewards") or [])))
            for key in [
                "rewards",
                "success_flags",
                "done_flags",
                "eef_positions",
                "target_object_positions",
                "target_object_heights",
                "object_goal_distances",
                "eef_target_distances",
                "gripper_states",
                "contact_summaries",
            ]:
                aggregate_trace[key].extend((htrace.get(key) or [])[:keep])
            aggregate_trace["saved_action_steps"] += keep
            if htrace.get("initial") and "initial" not in aggregate_trace:
                aggregate_trace["initial"] = htrace["initial"]
            for frame in htrace.get("frame_paths") or []:
                try:
                    aggregate_trace["frame_paths"].append({
                        **frame,
                        "step": int(frame.get("step", 0)) + int(steps_done),
                        "chunk_index": int(chunk_index),
                    })
                except Exception:
                    aggregate_trace["frame_paths"].append(frame)
        if first_outcome is None:
            first_outcome = outcome
        all_rewards.extend(outcome.get("rewards", []))
        steps_done += outcome.get("steps_executed", 0)
        terminal_success_seen = terminal_success_seen or bool(outcome.get("success_after") or outcome.get("success_within_H"))
        done_seen = done_seen or bool(outcome.get("done_within_H"))
        if terminal_success_seen or done_seen or outcome.get("steps_executed", 0) == 0:
            break
        chunk_index += 1

    if first_outcome is None:
        first_outcome = execute_action_chunk(
            env,
            initial_chunk[:0],
            0,
            before_obs,
            task_context=task_context,
            return_after_obs=False,
            save_full_trace=True,
            trace_frame_dir=trace_frame_dir,
            trace_frame_stride=trace_frame_stride,
        )
    first_outcome["terminal_steps"] = int(steps_done)
    first_outcome["terminal_reward_sum"] = float(sum(all_rewards))
    first_outcome["terminal_success"] = bool(terminal_success_seen)
    first_outcome["terminal_done"] = bool(done_seen)
    first_outcome["terminal_timeout"] = bool((not terminal_success_seen) and (not done_seen) and steps_done >= terminal_horizon)
    first_outcome["terminal_failure"] = bool((not terminal_success_seen) and (done_seen or steps_done >= terminal_horizon))
    first_outcome["terminal_rewards"] = all_rewards
    aggregate_trace["steps_executed"] = len(aggregate_trace["rewards"])
    aggregate_trace["terminal_steps"] = int(steps_done)
    aggregate_trace["terminal_success"] = bool(terminal_success_seen)
    aggregate_trace["terminal_failure"] = first_outcome["terminal_failure"]
    aggregate_trace["terminal_timeout"] = first_outcome["terminal_timeout"]
    first_outcome["H_used"] = int(len(aggregate_trace["rewards"]))
    first_outcome["rewards"] = aggregate_trace["rewards"]
    first_outcome["reward_sum_H"] = float(sum(aggregate_trace["rewards"]))
    first_outcome["nonzero_reward_count_H"] = int(sum(abs(r) > 1e-8 for r in aggregate_trace["rewards"]))
    first_outcome["horizon_trace"] = aggregate_trace
    return first_outcome, obs, continuation_actions


def run_parent_rollout(env, model, proc, lang, device, init_state, task_context, args, rollout_idx: int):
    obs = reset_to_init(env, init_state, warmup=args.warmup)
    hist = HistoryBuffer(args.history_k)
    last_eef = None
    recent_motion = []
    states = []
    rewards = []
    success = False
    done_seen = False
    for step in range(args.parent_roll_steps):
        curr_eef = eef_pos(obs)
        if last_eef is not None and curr_eef is not None:
            recent_motion.append(float(np.linalg.norm(curr_eef - last_eef)))
            recent_motion = recent_motion[-15:]
        stats = {"recent_motion": float(np.mean(recent_motion)) if len(recent_motion) >= 15 else 1.0}
        phase = detect_phase(obs, env, task_context, history_stats=stats)
        states.append({
            "state": get_state(env),
            "obs": obs,
            "history": hist.to_list(),
            "phase": phase,
            "step": step,
            "rollout": rollout_idx,
        })
        chunk, _norm, _flow = generate_chunk(model, proc, lang, obs, seed=0, device=device, steps=1, flowtrace=False)
        act = chunk[0].astype(np.float32)
        last_eef = curr_eef
        obs, rew, done, _info = env.step(act)
        rewards.append(float(rew))
        success = success or float(rew) > 0.0
        done_seen = done_seen or bool(done)
        hist.append({"reward": float(rew), "success": bool(rew > 0), "proprio": obs_to_proprio(obs).tolist(), "executed_action": act.tolist()})
        if done or success:
            break
    parent_failed_or_timeout = not success
    for s in states:
        s["parent_episode_success"] = success
        s["parent_failed_or_timeout"] = parent_failed_or_timeout
        s["parent_timeout"] = bool(parent_failed_or_timeout and not done_seen)
        s["parent_episode_steps"] = len(states)
        s["distance_to_failure_or_timeout"] = max(0, len(states) - s["step"])
        lo, hi = max(0, s["step"] - 4), min(len(rewards), s["step"] + 5)
        s["parent_rewards_around_state"] = rewards[lo:hi]
    return states


def select_states(rollout_states: list[dict[str, Any]], args) -> list[dict[str, Any]]:
    if not rollout_states:
        return []
    selected = []
    used_steps = set()

    def add(entry):
        if entry is None:
            return
        step = int(entry["step"])
        if step in used_steps:
            return
        used_steps.add(step)
        selected.append(entry)

    failed_parent = bool(rollout_states[-1].get("parent_failed_or_timeout"))
    useful_all = [s for s in rollout_states if s["phase"] in args.preferred_phases]
    if failed_parent:
        source = useful_all or rollout_states
        for distance in args.pre_failure_distances:
            target_step = max(0, len(rollout_states) - int(distance))
            eligible = [s for s in source if s["step"] <= len(rollout_states) - 1]
            if not eligible:
                eligible = rollout_states
            add(min(eligible, key=lambda s: abs(int(s["step"]) - target_step)))
            if len(selected) >= args.max_states_per_parent:
                return selected
        risk_start = max(0, len(rollout_states) - args.risk_window)
        risk = [s for s in source if s["step"] >= risk_start] or rollout_states[risk_start:]
        if risk:
            add(risk[len(risk) // 2])
            add(risk[-1])
    else:
        for phase in args.preferred_phases:
            phase_states = [s for s in useful_all if s["phase"] == phase]
            if phase_states:
                add(phase_states[len(phase_states) // 2])
                if len(selected) >= args.max_states_per_parent:
                    return selected
        risk_start = max(0, len(rollout_states) - args.risk_window)
        risk = rollout_states[risk_start:]
        if risk:
            add(risk[len(risk) // 2])
            add(risk[-1])
    return selected[: args.max_states_per_parent]


def final_labels_for_state(samples: list[dict[str, Any]]) -> None:
    success_alternatives = [s for s in samples if terminal_success(s["outcome"])]
    failed_alternatives = [s for s in samples if terminal_failure(s["outcome"])]
    failure_majority = len(failed_alternatives) >= max(3, (len(samples) + 1) // 2)
    for sample in samples:
        raw = sample["raw_local_label"]
        same = same_state_summary(sample, samples)
        same["terminal_success_count"] = len(success_alternatives)
        same["terminal_failure_count"] = len(failed_alternatives)
        same["terminal_failure_majority"] = bool(failure_majority)
        sample["label"] = {
            "label": LABEL_AMBIGUOUS,
            "final_label": LABEL_AMBIGUOUS,
            "initial_label": raw.get("label"),
            "bad_subtype": BAD_SUBTYPE_UNKNOWN,
            "label_reasons": ["terminal_outcome_ambiguous"],
            "raw_local_label": raw,
            "same_state_comparison": same,
            "terminal_success": terminal_success(sample["outcome"]),
            "terminal_failure": terminal_failure(sample["outcome"]),
            "label_evidence": {
                "terminal_success": terminal_success(sample["outcome"]),
                "terminal_failure": terminal_failure(sample["outcome"]),
                "raw_bad_evidence": raw.get("bad_evidence") or [],
                "raw_strong_good_evidence": raw.get("strong_good_evidence") or [],
                "raw_weak_good_evidence": raw.get("weak_good_evidence") or [],
                "parent_failed_or_timeout": bool(sample["metadata"].get("parent_failed_or_timeout")),
                "distance_to_failure_or_timeout": sample["metadata"].get("distance_to_failure_or_timeout"),
            },
        }

    scores = {s["sample_id"]: rollout_quality(s) for s in samples}
    best_score = max(scores.values()) if scores else 0.0
    for sample in samples:
        raw = sample["raw_local_label"]
        parent_failed = bool(sample["metadata"].get("parent_failed_or_timeout"))
        distance = sample["metadata"].get("distance_to_failure_or_timeout")
        reasons = []
        if terminal_success(sample["outcome"]):
            sample["label"].update({
                "label": LABEL_GOOD_STRONG,
                "final_label": LABEL_GOOD_STRONG,
                "label_confidence": "HIGH",
                "label_reasons": ["terminal_success_under_policy_continuation"],
            })
        elif raw.get("strong_good_evidence"):
            sample["label"].update({
                "label": LABEL_GOOD_WEAK,
                "final_label": LABEL_GOOD_WEAK,
                "label_confidence": "MEDIUM",
                "label_reasons": ["local_strong_progress_but_no_terminal_success"],
            })
        elif raw.get("weak_good_evidence"):
            sample["label"].update({
                "label": LABEL_GOOD_WEAK,
                "final_label": LABEL_GOOD_WEAK,
                "label_confidence": "MEDIUM",
                "label_reasons": raw.get("weak_good_evidence"),
            })

        raw_bad = raw.get("bad_evidence") or []
        has_success_alt = bool(success_alternatives)
        has_local_progress = bool(raw.get("strong_good_evidence") or raw.get("weak_good_evidence"))
        bad_by_advantage = terminal_failure(sample["outcome"]) and has_success_alt and (best_score - scores[sample["sample_id"]] >= 200.0)
        bad_by_failure_tail = (
            terminal_failure(sample["outcome"])
            and parent_failed
            and distance is not None
            and int(distance) <= 12
            and failure_majority
            and not has_local_progress
            and ("no_progress_strong" in raw_bad or sample["outcome"].get("terminal_timeout"))
        )
        if bad_by_advantage:
            reasons.append("terminal_failure_with_successful_same_state_alternative")
        if bad_by_failure_tail:
            reasons.append("repeated_same_state_failure_tail_no_progress")
        if raw_bad and (bad_by_advantage or bad_by_failure_tail):
            reasons.extend(raw_bad)
        if reasons:
            bad_subtype, bad_subtype_evidence = infer_bad_subtype(sample, samples)
            if bad_subtype == BAD_SUBTYPE_UNKNOWN:
                sample["label"].update({
                    "label": LABEL_AMBIGUOUS,
                    "final_label": LABEL_AMBIGUOUS,
                    "label_confidence": "LOW",
                    "bad_subtype": BAD_SUBTYPE_UNKNOWN,
                    "label_reasons": ["validated_bad_subtype_unknown"],
                    "validated_bad_reasons": [],
                    "bad_subtype_evidence": bad_subtype_evidence,
                })
                continue
            sample["label"].update({
                "label": LABEL_VALIDATED_BAD,
                "final_label": LABEL_VALIDATED_BAD,
                "label_confidence": "HIGH",
                "bad_subtype": bad_subtype,
                "label_reasons": sorted(set(reasons)),
                "validated_bad_reasons": sorted(set(reasons)),
                "bad_subtype_evidence": bad_subtype_evidence,
            })
    for sample in samples:
        same = same_state_summary(sample, samples)
        same["terminal_success_count"] = len(success_alternatives)
        same["terminal_failure_count"] = len(failed_alternatives)
        same["terminal_failure_majority"] = bool(failure_majority)
        sample["label"]["same_state_comparison"] = same


def collect(args):
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "states").mkdir(exist_ok=True)
    (outdir / "images").mkdir(exist_ok=True)
    if args.save_trace_frames:
        (outdir / "trace_frames").mkdir(exist_ok=True)
    model, proc, device = load_simvla()
    final_counts = Counter()
    raw_counts = Counter()
    selected_state_count = 0
    code_version = git_hash()
    for suite in args.suites:
        for task_id in args.task_ids:
            if selected_state_count >= args.max_total_states:
                break
            try:
                env, bundle = make_env(suite, task_id, args.resolution, seed=args.env_seed)
            except Exception as exc:
                print(f"Skipping unavailable {suite}_t{task_id}: {exc}", flush=True)
                continue
            init_states = bundle["init_states"]
            lang = bundle["task"].language
            all_bodies = list(object_body_positions(env).keys())
            task_context = None
            task_samples = []
            print(f"Outcome-advantage sampling {suite}_t{task_id}", flush=True)
            for rollout_idx in range(min(args.max_parent_episodes, len(init_states))):
                if selected_state_count >= args.max_total_states:
                    break
                obs0 = reset_to_init(env, init_states[rollout_idx % len(init_states)], warmup=args.warmup)
                task_context = parse_task_context(lang, obs0, all_bodies=all_bodies)
                states = run_parent_rollout(env, model, proc, lang, device, init_states[rollout_idx % len(init_states)], task_context, args, rollout_idx)
                for entry in select_states(states, args):
                    if selected_state_count >= args.max_total_states:
                        break
                    selected_state_count += 1
                    state = entry["state"]
                    obs = entry["obs"]
                    phase = entry["phase"]
                    parent_step = entry["step"]
                    state_id = f"{suite}_t{task_id}_r{entry['rollout']}_p{phase}_s{parent_step}_state"
                    state_path = save_state_npz(outdir / "states" / f"{state_id}.npz", state)
                    before_img, before_wrist = obs_images(obs)
                    prop = obs_to_proprio(obs)
                    before_obj = object_body_positions(env)
                    state_samples = []
                    for seed in args.simvla_seeds:
                        set_state(env, state)
                        initial_chunk, norm, flow = generate_chunk(model, proc, lang, obs, seed=seed, device=device, steps=args.initial_chunk_steps, flowtrace=True)
                        sid = f"{state_id}_seed{seed}"
                        frame_dir = outdir / "trace_frames" / sid if args.save_trace_frames else None
                        outcome, _after_obs, continuation_actions = execute_policy_continuation(
                            env,
                            model,
                            proc,
                            lang,
                            device,
                            initial_chunk,
                            obs,
                            task_context,
                            eval_horizon=args.eval_horizon,
                            terminal_horizon=args.terminal_horizon,
                            continuation_seed=args.continuation_seed,
                            trace_frame_dir=frame_dir,
                            trace_frame_stride=args.trace_frame_stride,
                        )
                        raw = label_outcome(outcome, task_context=task_context)
                        raw_counts[raw["label"]] += 1
                        before_path = save_png(outdir / "images" / f"{sid}_before.png", before_img) if args.save_images else None
                        after_img, _ = obs_images(_after_obs)
                        after_path = save_png(outdir / "images" / f"{sid}_after.png", after_img) if args.save_images else None
                        sample = {
                            "schema_version": "stage9_outcome_advantage_v2",
                            "_dataset_name": outdir.name,
                            "sample_id": sid,
                            "metadata": {
                                "task_name": f"{suite}_task{task_id}",
                                "task_language": lang,
                                "libero_pro_suite_or_task": suite,
                                "perturbation_type": suite_perturbation_type(suite),
                                "parent_phase": phase,
                                "simvla_generation_seed": int(seed),
                                "state_id": state_id,
                                "parent_step_index": parent_step,
                                "parent_episode_success": entry["parent_episode_success"],
                                "parent_failed_or_timeout": entry["parent_failed_or_timeout"],
                                "parent_timeout": entry["parent_timeout"],
                                "parent_episode_steps": entry["parent_episode_steps"],
                                "distance_to_failure_or_timeout": entry["distance_to_failure_or_timeout"],
                                "parent_rewards_around_state": entry["parent_rewards_around_state"],
                                "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                "code_version": code_version,
                            },
                            "history": entry["history"],
                            "current": {
                                "proprio": prop.tolist(),
                                "object_positions_before": before_obj,
                                "sim_state_path": state_path,
                                "before_image_path": before_path,
                                "after_image_path": after_path,
                                "task_context": task_context,
                            },
                            "candidate_action": {
                                "candidate_action_normalized": norm.tolist(),
                                "candidate_action_env": initial_chunk.tolist(),
                                "continuation_policy": "SimVLA",
                                "continuation_seed": args.continuation_seed,
                                "continuation_actions_env": continuation_actions,
                                "simvla_seed": int(seed),
                                "flowtrace_features": flow,
                            },
                            "outcome": outcome,
                            "raw_local_label": raw,
                        }
                        state_samples.append(sample)
                    final_labels_for_state(state_samples)
                    for sample in state_samples:
                        final_counts[sample["label"]["label"]] += 1
                        task_samples.append(sample)
                    print("states", selected_state_count, "samples", sum(final_counts.values()), "labels", dict(final_counts), flush=True)
            env.close()
            with (outdir / "counterfactual_samples.jsonl").open("a") as f:
                for sample in task_samples:
                    f.write(json.dumps(sample, default=str) + "\n")
            print(f"Finished {suite}_t{task_id}, saved {len(task_samples)} samples.", flush=True)
    summary = {
        "num_samples": sum(final_counts.values()),
        "selected_states": selected_state_count,
        "label_counts": dict(final_counts),
        "raw_label_counts": dict(raw_counts),
        "out_dir": str(outdir),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "eval_horizon": args.eval_horizon,
        "terminal_horizon": args.terminal_horizon,
        "simvla_seeds": args.simvla_seeds,
    }
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug", "libero_object_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5])
    parser.add_argument("--simvla-seeds", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5, 6, 7])
    parser.add_argument("--max-total-states", type=int, default=24)
    parser.add_argument("--max-parent-episodes", type=int, default=8)
    parser.add_argument("--max-states-per-parent", type=int, default=2)
    parser.add_argument("--parent-roll-steps", type=int, default=120)
    parser.add_argument("--risk-window", type=int, default=12)
    parser.add_argument("--pre-failure-distances", nargs="+", type=int, default=[40, 24, 12, 1])
    parser.add_argument("--preferred-phases", nargs="+", default=PHASES_OF_INTEREST)
    parser.add_argument("--initial-chunk-steps", type=int, default=10)
    parser.add_argument("--eval-horizon", type=int, default=40)
    parser.add_argument("--terminal-horizon", type=int, default=80)
    parser.add_argument("--continuation-seed", type=int, default=0)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed", type=int, default=7)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-trace-frames", action="store_true")
    parser.add_argument("--trace-frame-stride", type=int, default=20)
    parser.add_argument("--out-dir", default=str(Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws")) / "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/outcome_advantage_v1"))
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
