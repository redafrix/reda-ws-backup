from __future__ import annotations

import argparse
import json
import os
import time
from collections import Counter
from pathlib import Path
from typing import Any

from .collect_outcome_advantage_dataset import (
    PHASES_OF_INTEREST,
    generate_chunk,
    git_hash,
    run_parent_rollout,
    save_png,
    select_states,
)
from .libero_pro_env_utils import make_env, obs_images, obs_to_proprio, reset_to_init, suite_perturbation_type
from .local_chunk_quality import score_state_group, summarize_state_group_risks
from .outcome_metrics import execute_action_chunk, object_body_positions
from .sim_state_utils import save_state_npz, set_state
from .simvla_candidate_sampler import load_simvla
from .task_parser import parse_task_context


DEFAULT_REDA_WS = Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))


def collect(args: argparse.Namespace) -> None:
    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "states").mkdir(exist_ok=True)
    (outdir / "images").mkdir(exist_ok=True)
    if args.save_trace_frames:
        (outdir / "trace_frames").mkdir(exist_ok=True)

    model, proc, device = load_simvla()
    selected_state_count = 0
    risk_bins = Counter()
    legacy_suggestions = Counter()
    old_raw_counts = Counter()
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
            task_samples: list[dict[str, Any]] = []
            print(f"Continuous-risk V2 sampling {suite}_t{task_id}", flush=True)

            for rollout_idx in range(min(args.max_parent_episodes, len(init_states))):
                if selected_state_count >= args.max_total_states:
                    break
                obs0 = reset_to_init(env, init_states[rollout_idx % len(init_states)], warmup=args.warmup)
                task_context = parse_task_context(lang, obs0, all_bodies=all_bodies)
                parent_states = run_parent_rollout(
                    env,
                    model,
                    proc,
                    lang,
                    device,
                    init_states[rollout_idx % len(init_states)],
                    task_context,
                    args,
                    rollout_idx,
                )

                for entry in select_states(parent_states, args):
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
                    before_obj = object_body_positions(env)
                    prop = obs_to_proprio(obs)
                    before_agent_path = save_png(outdir / "images" / f"{state_id}_before_agent.png", before_img) if args.save_images else None
                    before_wrist_path = save_png(outdir / "images" / f"{state_id}_before_wrist.png", before_wrist) if args.save_images and before_wrist is not None else None

                    state_samples: list[dict[str, Any]] = []
                    for seed in args.simvla_seeds:
                        set_state(env, state)
                        initial_chunk, norm, flow = generate_chunk(
                            model,
                            proc,
                            lang,
                            obs,
                            seed=seed,
                            device=device,
                            steps=args.initial_chunk_steps,
                            flowtrace=True,
                        )
                        sid = f"{state_id}_seed{seed}"
                        frame_dir = outdir / "trace_frames" / sid if args.save_trace_frames else None
                        local_horizon = min(args.initial_chunk_steps, len(initial_chunk))
                        outcome, after_obs = execute_action_chunk(
                            env,
                            initial_chunk,
                            local_horizon,
                            obs,
                            task_context=task_context,
                            return_after_obs=True,
                            save_full_trace=True,
                            trace_frame_dir=frame_dir,
                            trace_frame_stride=args.trace_frame_stride,
                        )
                        after_img, after_wrist = obs_images(after_obs)
                        after_agent_path = save_png(outdir / "images" / f"{sid}_after_agent.png", after_img) if args.save_images else None
                        after_wrist_path = save_png(outdir / "images" / f"{sid}_after_wrist.png", after_wrist) if args.save_images and after_wrist is not None else None

                        sample = {
                            "schema_version": "stage9_continuous_risk_dataset_v2",
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
                                "before_image_path": before_agent_path,
                                "before_wrist_image_path": before_wrist_path,
                                "task_context": task_context,
                            },
                            "candidate_action": {
                                "candidate_action_normalized": norm.tolist(),
                                "candidate_action_env": initial_chunk.tolist(),
                                "simvla_seed": int(seed),
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
                                "chunk_steps": int(local_horizon),
                                "terminal_continuation_used_for_label": False,
                                "terminal_outcome_policy": "not_collected_in_v2_local_chunk_collector",
                                "continuous_risk_primary": True,
                            },
                        }
                        state_samples.append(sample)

                    risks = score_state_group(state_samples)
                    group_summary = summarize_state_group_risks(risks)
                    for risk in risks:
                        risk["same_state_group_summary_v2"] = group_summary
                    for sample, risk in zip(state_samples, risks):
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
                            "same_state_comparison_v2": risk["same_state_comparison_v2"],
                            "same_state_group_summary_v2": risk["same_state_group_summary_v2"],
                        }
                        risk_bins[risk["risk_bin"]] += 1
                        legacy_suggestions[risk["legacy_label_suggestion"]] += 1
                        old_raw_counts["continuous_only_no_old_raw"] += 1
                        task_samples.append(sample)

                    print(
                        "states",
                        selected_state_count,
                        "samples",
                        sum(risk_bins.values()),
                        "risk_bins",
                        dict(risk_bins),
                        flush=True,
                    )

            env.close()
            with (outdir / "counterfactual_samples.jsonl").open("a") as f:
                for sample in task_samples:
                    f.write(json.dumps(sample, default=str) + "\n")
            print(f"Finished {suite}_t{task_id}, saved {len(task_samples)} samples.", flush=True)

    summary = {
        "schema_version": "stage9_continuous_risk_dataset_v2_summary",
        "num_samples": sum(risk_bins.values()),
        "selected_states": selected_state_count,
        "risk_bin_counts": dict(risk_bins),
        "legacy_label_suggestion_counts": dict(legacy_suggestions),
        "raw_counts": dict(old_raw_counts),
        "out_dir": str(outdir),
        "suites": args.suites,
        "task_ids": args.task_ids,
        "simvla_seeds": args.simvla_seeds,
        "initial_chunk_steps": args.initial_chunk_steps,
        "history_k": args.history_k,
        "terminal_continuation_used_for_label": False,
    }
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suites", nargs="+", default=["libero_spatial_with_mug", "libero_object_with_mug"])
    parser.add_argument("--task-ids", nargs="+", type=int, default=[0, 1, 2, 3, 4, 5])
    parser.add_argument("--simvla-seeds", nargs="+", type=int, default=list(range(64)))
    parser.add_argument("--max-total-states", type=int, default=24)
    parser.add_argument("--max-parent-episodes", type=int, default=8)
    parser.add_argument("--max-states-per-parent", type=int, default=2)
    parser.add_argument("--parent-roll-steps", type=int, default=120)
    parser.add_argument("--risk-window", type=int, default=12)
    parser.add_argument("--pre-failure-distances", nargs="+", type=int, default=[40, 24, 12, 1])
    parser.add_argument("--preferred-phases", nargs="+", default=PHASES_OF_INTEREST)
    parser.add_argument("--initial-chunk-steps", type=int, default=10)
    parser.add_argument("--history-k", type=int, default=8)
    parser.add_argument("--resolution", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--env-seed", type=int, default=7)
    parser.add_argument("--save-images", action="store_true")
    parser.add_argument("--save-trace-frames", action="store_true")
    parser.add_argument("--trace-frame-stride", type=int, default=5)
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_REDA_WS / "asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/continuous_risk_v2"),
    )
    args = parser.parse_args()
    collect(args)


if __name__ == "__main__":
    main()
