from __future__ import annotations

import argparse
import json
import os
import time
from collections import Counter
from pathlib import Path
from typing import Any

from .collect_outcome_advantage_dataset import PHASES_OF_INTEREST, generate_chunk, git_hash, save_png
from .history_buffer import HistoryBuffer
from .libero_pro_env_utils import make_env, obs_images, obs_to_proprio, reset_to_init, suite_perturbation_type
from .local_chunk_quality import score_sample_local, score_state_group, summarize_state_group_risks
from .outcome_metrics import detect_phase, execute_action_chunk, object_body_positions
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


def strip_private(sample: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in sample.items() if not k.startswith("_runtime_")}


def add_continuous_label(sample: dict[str, Any], risk: dict[str, Any]) -> None:
    sample["continuous_risk"] = risk
    sample["label"] = {
        "label_schema": "continuous_risk_v2",
        "risk_score": risk["risk_score"],
        "risk_confidence": risk["risk_confidence"],
        "chunk_quality": risk["chunk_quality"],
        "risk_bin": risk["risk_bin"],
        "legacy_label_suggestion": risk["legacy_label_suggestion"],
        "bad_subtype": risk["bad_subtype"],
        "positive_evidence": risk["positive_evidence"],
        "negative_evidence": risk["negative_evidence"],
        "weak_negative_evidence": risk["weak_negative_evidence"],
        "ambiguous_evidence": risk["ambiguous_evidence"],
        "risk_components": risk["risk_components"],
        "same_state_comparison_v2": risk.get("same_state_comparison_v2") or {},
        "same_state_group_summary_v2": risk.get("same_state_group_summary_v2") or {},
    }


def episode_key(suite: str, task_id: int, rollout_idx: int, policy_seed: int) -> str:
    return f"{suite}_t{task_id}_r{rollout_idx}_pseed{policy_seed}"


def make_episode_chunk_sample(
    outdir: Path,
    suite: str,
    task_id: int,
    lang: str,
    task_context: dict[str, Any],
    episode_id: str,
    rollout_idx: int,
    policy_seed: int,
    chunk_idx: int,
    chunk_seed: int,
    phase: str,
    before_state: dict[str, Any],
    before_obs: dict[str, Any],
    before_obj: dict[str, Any],
    before_agent_path: str | None,
    before_wrist_path: str | None,
    state_path: str,
    history: list[dict[str, Any]],
    prop: Any,
    initial_chunk,
    norm,
    flow: dict[str, Any],
    outcome: dict[str, Any],
    after_agent_path: str | None,
    after_wrist_path: str | None,
    code_version: str,
) -> dict[str, Any]:
    sid = f"{episode_id}_chunk{chunk_idx:03d}_seed{chunk_seed}"
    return {
        "schema_version": "stage9_failed_episode_chunk_v2",
        "_dataset_name": outdir.name,
        "sample_id": sid,
        "metadata": {
            "task_name": f"{suite}_task{task_id}",
            "task_language": lang,
            "libero_pro_suite_or_task": suite,
            "perturbation_type": suite_perturbation_type(suite),
            "episode_id": episode_id,
            "rollout_index": rollout_idx,
            "policy_seed": int(policy_seed),
            "chunk_index": int(chunk_idx),
            "chunk_seed": int(chunk_seed),
            "parent_phase": phase,
            "simvla_generation_seed": int(chunk_seed),
            "state_id": f"{episode_id}_chunk{chunk_idx:03d}_state",
            "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "code_version": code_version,
        },
        "history": history,
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
            "simvla_seed": int(chunk_seed),
            "flowtrace_features": flow,
        },
        "outcome": outcome,
        "visual_evidence": {
            "after_image_path": after_agent_path,
            "after_wrist_image_path": after_wrist_path,
            "trace_frame_paths": (outcome.get("horizon_trace") or {}).get("frame_paths") or [],
        },
        "labeling_policy": {
            "label_target": "candidate_action_chunk",
            "terminal_continuation_used_for_label": False,
            "episode_failure_used_for_label": False,
            "episode_failure_used_for_mining_only": True,
            "continuous_risk_primary": True,
        },
        "_runtime_before_state": before_state,
        "_runtime_before_obs": before_obs,
    }


def select_failure_windows(chunks: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    scored: list[tuple[int, dict[str, Any], dict[str, Any]]] = []
    for idx, sample in enumerate(chunks):
        local = score_sample_local(sample)
        scored.append((idx, sample, local))

    selected: dict[int, str] = {}
    for idx, _sample, risk in scored:
        if float(risk["risk_score_local"]) >= args.window_risk_threshold and (
            risk.get("negative_evidence") or risk.get("weak_negative_evidence")
        ):
            selected[idx] = "high_local_risk"
        elif risk.get("negative_evidence"):
            selected[idx] = "negative_evidence"

    tail_start = max(0, len(chunks) - args.tail_windows)
    for idx in range(tail_start, len(chunks)):
        selected.setdefault(idx, "failure_tail")

    top = sorted(scored, key=lambda x: float(x[2]["risk_score_local"]), reverse=True)[: args.top_risk_windows]
    for idx, _sample, _risk in top:
        selected.setdefault(idx, "top_local_risk")

    if args.scan_all_failed_windows:
        for idx in range(len(chunks)):
            selected.setdefault(idx, "branchpoint_scan")

    for offset in args.pre_failure_offsets:
        idx = len(chunks) - 1 - int(offset)
        if 0 <= idx < len(chunks):
            selected.setdefault(idx, "pre_failure_offset")

    rows = []
    for idx in sorted(selected):
        risk = scored[idx][2]
        rows.append({
            "chunk_index": idx,
            "selection_reason": selected[idx],
            "local_risk_score": risk["risk_score_local"],
            "local_risk_confidence": risk["risk_confidence_local"],
            "positive_evidence": risk.get("positive_evidence") or [],
            "negative_evidence": risk.get("negative_evidence") or [],
            "weak_negative_evidence": risk.get("weak_negative_evidence") or [],
        })
    def priority(row: dict[str, Any]) -> tuple[int, int]:
        reason = row["selection_reason"]
        order = {
            "high_local_risk": 0,
            "negative_evidence": 1,
            "pre_failure_offset": 2,
            "top_local_risk": 3,
            "branchpoint_scan": 4,
            "failure_tail": 5,
        }
        return (order.get(reason, 99), int(row["chunk_index"]))

    rows.sort(key=priority)
    return rows[: args.max_windows_per_failed_episode]


def _spread_indices(n: int, limit: int) -> list[int]:
    if n <= 0 or limit <= 0:
        return []
    if n <= limit:
        return list(range(n))
    if limit == 1:
        return [n // 2]
    return sorted(set(round(i * (n - 1) / (limit - 1)) for i in range(limit)))


def select_success_branchpoints(chunks: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """Pick solvable same-state branchpoints from successful episodes.

    The first 64-seed pilot showed that selecting only the highest-progress
    success chunks mostly chooses easy terminal chunks, where all SimVLA seeds
    look safe.  For action-specific BAD mining we need earlier states from a
    successful trajectory: they are known recoverable because the parent
    trajectory solved the task, but alternative real SimVLA seeds may still make
    locally bad choices.
    """
    scored: list[tuple[int, dict[str, Any], dict[str, Any]]] = []
    for idx, sample in enumerate(chunks):
        local = score_sample_local(sample)
        scored.append((idx, sample, local))

    phase_priority = {
        "GRASP_OR_LIFT": 0,
        "TRANSPORT": 1,
        "PLACE_OR_GOAL": 2,
        "NEAR_GRASP": 3,
        "STUCK_OR_NO_PROGRESS": 4,
        "APPROACH": 5,
        "UNKNOWN": 6,
    }
    preferred_phases = set(args.success_branchpoint_phases)
    nonterminal_rows = []
    for idx, _sample, risk in scored:
        positives = risk.get("positive_evidence") or []
        phase = str((_sample.get("metadata") or {}).get("parent_phase") or "UNKNOWN")
        has_sparse_success = "local_success" in positives or "local_reward" in positives
        if args.success_branchpoints_preterminal_only and has_sparse_success:
            continue
        if preferred_phases and phase not in preferred_phases:
            continue
        nonterminal_rows.append((idx, phase, float(risk["chunk_quality_local"]), risk))

    # If phase/preterminal filtering is too strict, fall back to nonterminal
    # chunks first, then to all chunks except the last one.  This still avoids
    # using parent episode success as a label; it only selects recoverable states.
    if not nonterminal_rows:
        for idx, _sample, risk in scored:
            positives = risk.get("positive_evidence") or []
            has_sparse_success = "local_success" in positives or "local_reward" in positives
            if args.success_branchpoints_preterminal_only and has_sparse_success:
                continue
            phase = str((_sample.get("metadata") or {}).get("parent_phase") or "UNKNOWN")
            nonterminal_rows.append((idx, phase, float(risk["chunk_quality_local"]), risk))
    if not nonterminal_rows:
        for idx, _sample, risk in scored[:-1] or scored:
            phase = str((_sample.get("metadata") or {}).get("parent_phase") or "UNKNOWN")
            nonterminal_rows.append((idx, phase, float(risk["chunk_quality_local"]), risk))

    rows = []
    if args.success_branchpoint_strategy == "diverse_preterminal":
        # First take phase-diverse representative chunks, then fill by evenly
        # spaced chunk indices. This is deliberately not just "top quality".
        selected: dict[int, tuple[int, str, float, dict[str, Any]]] = {}
        by_phase: dict[str, list[tuple[int, str, float, dict[str, Any]]]] = {}
        for row in nonterminal_rows:
            by_phase.setdefault(row[1], []).append(row)
        for phase in sorted(by_phase, key=lambda p: phase_priority.get(p, 99)):
            phase_rows = sorted(by_phase[phase], key=lambda x: (abs(x[0] - len(chunks) // 2), x[0]))
            if phase_rows:
                selected.setdefault(phase_rows[0][0], phase_rows[0])
            if len(selected) >= args.success_windows_per_episode:
                break

        ordered = sorted(nonterminal_rows, key=lambda x: x[0])
        spread = _spread_indices(len(ordered), args.success_windows_per_episode)
        for pos in spread:
            row = ordered[pos]
            selected.setdefault(row[0], row)
            if len(selected) >= args.success_windows_per_episode:
                break
        chosen = [selected[k] for k in sorted(selected)]
    else:
        progress_rows = []
        for idx, _sample, risk in scored:
            positives = risk.get("positive_evidence") or []
            quality = float(risk["chunk_quality_local"])
            if positives:
                progress_rows.append((idx, str((_sample.get("metadata") or {}).get("parent_phase") or "UNKNOWN"), quality, risk))
        if not progress_rows:
            progress_rows = [
                (idx, str((_sample.get("metadata") or {}).get("parent_phase") or "UNKNOWN"), float(risk["chunk_quality_local"]), risk)
                for idx, _sample, risk in scored
                if idx >= max(0, len(scored) // 3)
            ]
        progress_rows.sort(key=lambda x: (-x[2], x[0]))
        chosen = progress_rows[: args.success_windows_per_episode]

    for idx, phase, _quality, risk in chosen[: args.success_windows_per_episode]:
        selection_reason = "success_branchpoint_preterminal" if args.success_branchpoint_strategy == "diverse_preterminal" else "success_branchpoint"
        quality = float(risk["chunk_quality_local"])
        rows.append({
            "chunk_index": idx,
            "selection_reason": selection_reason,
            "source_phase": phase,
            "source_chunk_quality": quality,
            "local_risk_score": risk["risk_score_local"],
            "local_risk_confidence": risk["risk_confidence_local"],
            "positive_evidence": risk.get("positive_evidence") or [],
            "negative_evidence": risk.get("negative_evidence") or [],
            "weak_negative_evidence": risk.get("weak_negative_evidence") or [],
        })
    return rows


def replay_window_candidates(
    env,
    model,
    proc,
    lang: str,
    device,
    outdir: Path,
    task_context: dict[str, Any],
    window_sample: dict[str, Any],
    window: dict[str, Any],
    args: argparse.Namespace,
    code_version: str,
) -> list[dict[str, Any]]:
    before_state = window_sample["_runtime_before_state"]
    before_obs = window_sample["_runtime_before_obs"]
    meta = window_sample["metadata"]
    replay_state_id = f"{meta['episode_id']}_window{int(window['chunk_index']):03d}_state"
    state_path = save_state_npz(outdir / "states" / f"{replay_state_id}.npz", before_state)
    before_agent, before_wrist = obs_images(before_obs)
    before_agent_path = save_png(outdir / "images" / f"{replay_state_id}_before_agent.png", before_agent) if args.save_images else None
    before_wrist_path = save_png(outdir / "images" / f"{replay_state_id}_before_wrist.png", before_wrist) if args.save_images and before_wrist is not None else None
    prop = obs_to_proprio(before_obs)
    before_obj = object_body_positions(env)
    source_outcome = window_sample.get("episode_outcome") or {}
    source_failed = not bool(source_outcome.get("episode_success"))

    samples: list[dict[str, Any]] = []
    for seed_value in args.replay_seeds:
        set_state(env, before_state)
        initial_chunk, norm, flow = generate_chunk(
            model,
            proc,
            lang,
            before_obs,
            seed=int(seed_value),
            device=device,
            steps=args.initial_chunk_steps,
            flowtrace=True,
        )
        sid = f"{replay_state_id}_seed{seed_value}"
        frame_dir = outdir / "trace_frames" / sid if args.save_trace_frames else None
        outcome, after_obs = execute_action_chunk(
            env,
            initial_chunk,
            min(args.initial_chunk_steps, len(initial_chunk)),
            before_obs,
            task_context=task_context,
            return_after_obs=True,
            save_full_trace=True,
            trace_frame_dir=frame_dir,
            trace_frame_stride=args.trace_frame_stride,
        )
        after_agent, after_wrist = obs_images(after_obs)
        after_agent_path = save_png(outdir / "images" / f"{sid}_after_agent.png", after_agent) if args.save_images else None
        after_wrist_path = save_png(outdir / "images" / f"{sid}_after_wrist.png", after_wrist) if args.save_images and after_wrist is not None else None
        sample = {
            "schema_version": "stage9_failed_episode_replay_candidate_v2",
            "_dataset_name": outdir.name,
            "sample_id": sid,
            "metadata": {
                "task_name": meta.get("task_name"),
                "task_language": lang,
                "libero_pro_suite_or_task": meta.get("libero_pro_suite_or_task"),
                "perturbation_type": meta.get("perturbation_type"),
                "episode_id": meta.get("episode_id"),
                "source_episode_chunk_sample_id": window_sample.get("sample_id"),
                "source_episode_chunk_index": int(window["chunk_index"]),
                "window_selection_reason": window["selection_reason"],
                "parent_phase": meta.get("parent_phase"),
                "simvla_generation_seed": int(seed_value),
                "state_id": replay_state_id,
                "collection_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "code_version": code_version,
            },
            "history": window_sample.get("history") or [],
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
                "flowtrace_features": flow,
            },
            "outcome": outcome,
            "visual_evidence": {
                "after_image_path": after_agent_path,
                "after_wrist_image_path": after_wrist_path,
                "trace_frame_paths": (outcome.get("horizon_trace") or {}).get("frame_paths") or [],
            },
            "labeling_policy": {
                "label_target": "candidate_action_chunk",
                "terminal_continuation_used_for_label": False,
                "episode_failure_used_for_label": False,
                "episode_failure_used_for_mining_only": bool(source_failed),
                "success_episode_used_for_branchpoint_mining": bool(not source_failed),
                "same_state_replay_for_failure_window": True,
                "continuous_risk_primary": True,
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

    model, proc, device = load_simvla()
    code_version = git_hash()
    summary = Counter()
    risk_bins = Counter()
    replay_risk_bins = Counter()
    failure_window_rows: list[dict[str, Any]] = []

    episode_chunks_path = outdir / "episode_chunks.jsonl"
    replay_path = outdir / "replay_counterfactual_samples.jsonl"

    for suite in args.suites:
        for task_id in args.task_ids:
            if summary["episodes_total"] >= args.max_episodes_total:
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
            print(f"Failed-episode mining {suite}_t{task_id}", flush=True)

            for rollout_idx in range(min(args.rollouts_per_task, len(init_states))):
                if summary["episodes_total"] >= args.max_episodes_total:
                    break
                policy_seed = args.policy_seed_base + rollout_idx
                ep_id = episode_key(suite, task_id, rollout_idx, policy_seed)
                obs = reset_to_init(env, init_states[rollout_idx % len(init_states)], warmup=args.warmup)
                hist = HistoryBuffer(args.history_k)
                episode_chunks: list[dict[str, Any]] = []
                success = False
                done = False
                reward_sum = 0.0

                for chunk_idx in range(args.max_episode_chunks):
                    phase = detect_phase(obs, env, task_context)
                    before_state = get_state(env)
                    state_path = save_state_npz(outdir / "states" / f"{ep_id}_chunk{chunk_idx:03d}_state.npz", before_state)
                    before_agent, before_wrist = obs_images(obs)
                    before_agent_path = save_png(outdir / "images" / f"{ep_id}_chunk{chunk_idx:03d}_before_agent.png", before_agent) if args.save_images else None
                    before_wrist_path = save_png(outdir / "images" / f"{ep_id}_chunk{chunk_idx:03d}_before_wrist.png", before_wrist) if args.save_images and before_wrist is not None else None
                    before_obj = object_body_positions(env)
                    prop = obs_to_proprio(obs)
                    chunk_seed = policy_seed + chunk_idx
                    initial_chunk, norm, flow = generate_chunk(
                        model,
                        proc,
                        lang,
                        obs,
                        seed=chunk_seed,
                        device=device,
                        steps=args.initial_chunk_steps,
                        flowtrace=True,
                    )
                    frame_dir = outdir / "trace_frames" / f"{ep_id}_chunk{chunk_idx:03d}" if args.save_trace_frames else None
                    outcome, after_obs = execute_action_chunk(
                        env,
                        initial_chunk,
                        min(args.initial_chunk_steps, len(initial_chunk)),
                        obs,
                        task_context=task_context,
                        return_after_obs=True,
                        save_full_trace=True,
                        trace_frame_dir=frame_dir,
                        trace_frame_stride=args.trace_frame_stride,
                    )
                    after_agent, after_wrist = obs_images(after_obs)
                    after_agent_path = save_png(outdir / "images" / f"{ep_id}_chunk{chunk_idx:03d}_after_agent.png", after_agent) if args.save_images else None
                    after_wrist_path = save_png(outdir / "images" / f"{ep_id}_chunk{chunk_idx:03d}_after_wrist.png", after_wrist) if args.save_images and after_wrist is not None else None
                    sample = make_episode_chunk_sample(
                        outdir,
                        suite,
                        task_id,
                        lang,
                        task_context,
                        ep_id,
                        rollout_idx,
                        policy_seed,
                        chunk_idx,
                        chunk_seed,
                        phase,
                        before_state,
                        obs,
                        before_obj,
                        before_agent_path,
                        before_wrist_path,
                        state_path,
                        hist.to_list(),
                        prop,
                        initial_chunk,
                        norm,
                        flow,
                        outcome,
                        after_agent_path,
                        after_wrist_path,
                        code_version,
                    )
                    local_risk = score_state_group([sample])[0]
                    add_continuous_label(sample, local_risk)
                    episode_chunks.append(sample)
                    risk_bins[local_risk["risk_bin"]] += 1

                    reward_sum += float(outcome.get("reward_sum_H") or 0.0)
                    success = success or bool(outcome.get("success_after") or outcome.get("success_within_H") or reward_sum > 0)
                    done = bool(outcome.get("done_within_H"))
                    hist.append({
                        "reward_sum": float(outcome.get("reward_sum_H") or 0.0),
                        "success": bool(outcome.get("success_after") or outcome.get("success_within_H")),
                        "proprio": obs_to_proprio(after_obs).tolist(),
                        "executed_action_chunk_first": initial_chunk[0].tolist() if hasattr(initial_chunk[0], "tolist") else initial_chunk[0],
                    })
                    obs = after_obs
                    if success or done:
                        break

                summary["episodes_total"] += 1
                if success:
                    summary["episodes_success"] += 1
                else:
                    summary["episodes_failed_or_timeout"] += 1
                summary["episode_chunks"] += len(episode_chunks)

                clean_episode_chunks = []
                for sample in episode_chunks:
                    sample["episode_outcome"] = {
                        "episode_success": bool(success),
                        "episode_done": bool(done),
                        "episode_timeout": bool((not success) and (not done)),
                        "episode_reward_sum": float(reward_sum),
                        "episode_chunks": len(episode_chunks),
                    }
                    sample.setdefault("labeling_policy", {})["episode_failure_used_for_mining_only"] = bool(not success)
                    clean_episode_chunks.append(strip_private(sample))
                append_jsonl(episode_chunks_path, clean_episode_chunks)

                if not success:
                    windows = select_failure_windows(episode_chunks, args)
                    summary["failure_windows"] += len(windows)
                    for window in windows:
                        src = episode_chunks[int(window["chunk_index"])]
                        row = {
                            "episode_id": ep_id,
                            "task_name": f"{suite}_task{task_id}",
                            "task_language": lang,
                            "source_sample_id": src["sample_id"],
                            **window,
                        }
                        failure_window_rows.append(row)
                        replay_samples = replay_window_candidates(
                            env,
                            model,
                            proc,
                            lang,
                            device,
                            outdir,
                            task_context,
                            src,
                            window,
                            args,
                            code_version,
                        )
                        for sample in replay_samples:
                            replay_risk_bins[sample["label"]["risk_bin"]] += 1
                        append_jsonl(replay_path, [strip_private(s) for s in replay_samples])
                        summary["replay_samples"] += len(replay_samples)
                elif args.mine_success_branchpoints:
                    windows = select_success_branchpoints(episode_chunks, args)
                    summary["success_branchpoint_windows"] += len(windows)
                    for window in windows:
                        src = episode_chunks[int(window["chunk_index"])]
                        row = {
                            "episode_id": ep_id,
                            "task_name": f"{suite}_task{task_id}",
                            "task_language": lang,
                            "source_sample_id": src["sample_id"],
                            **window,
                        }
                        failure_window_rows.append(row)
                        replay_samples = replay_window_candidates(
                            env,
                            model,
                            proc,
                            lang,
                            device,
                            outdir,
                            task_context,
                            src,
                            window,
                            args,
                            code_version,
                        )
                        for sample in replay_samples:
                            replay_risk_bins[sample["label"]["risk_bin"]] += 1
                        append_jsonl(replay_path, [strip_private(s) for s in replay_samples])
                        summary["replay_samples"] += len(replay_samples)

                print(
                    "episodes",
                    summary["episodes_total"],
                    "success",
                    summary["episodes_success"],
                    "failed",
                    summary["episodes_failed_or_timeout"],
                    "chunks",
                    summary["episode_chunks"],
                    "windows",
                    summary["failure_windows"],
                    "risk_bins",
                    dict(risk_bins),
                    "replay_bins",
                    dict(replay_risk_bins),
                    flush=True,
                )
            env.close()

    append_jsonl(outdir / "failure_windows.jsonl", failure_window_rows)
    final_summary = {
        "schema_version": "stage9_failed_episode_mining_v2_summary",
        "out_dir": str(outdir),
        "summary_counts": dict(summary),
        "episode_chunk_risk_bin_counts": dict(risk_bins),
        "replay_risk_bin_counts": dict(replay_risk_bins),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "replay_seeds": args.replay_seeds,
        "initial_chunk_steps": args.initial_chunk_steps,
        "history_k": args.history_k,
        "terminal_continuation_used_for_label": False,
        "episode_failure_used_for_label": False,
    }
    write_json(outdir / "summary.json", final_summary)
    print(json.dumps(final_summary, indent=2, sort_keys=True), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug", "libero_object_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5])
    parser.add_argument("--rollouts-per-task", type=int, default=4)
    parser.add_argument("--max-episodes-total", type=int, default=16)
    parser.add_argument("--max-episode-chunks", type=int, default=16)
    parser.add_argument("--initial-chunk-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--policy-seed-base", type=int, default=0)
    parser.add_argument("--replay-seeds", nargs="+", type=int, default=list(range(64)))
    parser.add_argument("--max-windows-per-failed-episode", type=int, default=8)
    parser.add_argument("--mine-success-branchpoints", action="store_true")
    parser.add_argument("--success-windows-per-episode", type=int, default=3)
    parser.add_argument("--success-branchpoint-strategy", choices=["diverse_preterminal", "top_progress"], default="diverse_preterminal")
    parser.add_argument("--success-branchpoints-preterminal-only", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--success-branchpoint-phases",
        nargs="+",
        default=["NEAR_GRASP", "GRASP_OR_LIFT", "TRANSPORT", "PLACE_OR_GOAL"],
    )
    parser.add_argument("--tail-windows", type=int, default=2)
    parser.add_argument("--top-risk-windows", type=int, default=2)
    parser.add_argument("--pre-failure-offsets", nargs="+", type=int, default=[1, 2, 3, 4, 6, 8])
    parser.add_argument("--scan-all-failed-windows", action="store_true")
    parser.add_argument("--window-risk-threshold", type=float, default=0.65)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed", type=int, default=7)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-trace-frames", action="store_true")
    parser.add_argument("--trace-frame-stride", type=int, default=5)
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/failed_episode_mining_v2"),
    )
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
