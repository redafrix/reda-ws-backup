#!/usr/bin/env python3
"""Audit Active TopK OOD400 Run and Compute Paired Comparison with Baseline.

Verifies:
1. Exact directory membership (000000..000399), 0 missing, 0 extra.
2. Contiguous decision indices 0..N-1 (0 gaps, 0 duplicates).
3. Active controller logic consistency for every decision:
   - expected_selected = controller_rule(candidate_scores, A, C)
   - executed_candidate_index == expected_selected (0 mismatches)
   - executed_action_sequence == selected candidate prefix (0 mismatches, 0.0 max diff)
4. Protocol compliance on all 400 episodes (3cm immediate termination, 350 exact failure horizon).
5. 400 matched pairs: Persisted Success, Rescues, Regressions, Persisted Failure.
6. Exact arithmetic: active_success == baseline_success + rescues - regressions.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

import numpy as np

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import sha256_file


def canonical_json_sha256(payload: object) -> str:
    serialized = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def audit_active_run(
    *,
    active_output_dir: Path,
    baseline_output_dir: Path,
    manifest_path: Path,
    controller_json_path: Path,
    evidence_dir: Path,
) -> dict[str, Any]:
    active_output_dir = Path(active_output_dir).resolve()
    baseline_output_dir = Path(baseline_output_dir).resolve()
    manifest_path = Path(manifest_path).resolve()
    controller_json_path = Path(controller_json_path).resolve()
    evidence_dir = Path(evidence_dir).resolve()
    evidence_dir.mkdir(parents=True, exist_ok=True)

    controller_cfg = json.loads(controller_json_path.read_text(encoding="utf-8"))
    a_val = float(controller_cfg["main_threshold_value"])
    c_val = float(controller_cfg["alternative_cap_value"])
    a_rule = str(controller_cfg["main_threshold_name"])

    raw_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest_episodes = {int(e["benchmark_episode_id"]): e for e in raw_manifest["episodes"]}
    total_expected = len(manifest_episodes)

    # Load baseline summaries
    base_summaries_p = baseline_output_dir / "canonical_episode_summaries.jsonl"
    if not base_summaries_p.exists():
        base_summaries_p = baseline_output_dir / "episode_summaries.jsonl"
    base_summaries = {s["episode_id"]: s for s in [json.loads(l) for l in base_summaries_p.read_text(encoding="utf-8").splitlines() if l.strip()]}

    active_episodes_dir = active_output_dir / "episodes"
    active_videos_dir = active_output_dir / "videos"

    if not active_episodes_dir.exists():
        raise FileNotFoundError(f"Active episodes directory not found: {active_episodes_dir}")

    # Check directory membership
    actual_dirs = sorted([p.name for p in active_episodes_dir.iterdir() if p.is_dir()])
    expected_dirs = [f"{i:06d}" for i in range(total_expected)]
    missing_dirs = sorted(list(set(expected_dirs) - set(actual_dirs)))
    extra_dirs = sorted(list(set(actual_dirs) - set(expected_dirs)))

    if missing_dirs or extra_dirs:
        raise RuntimeError(f"Active episode directory membership failure: missing={missing_dirs}, extra={extra_dirs}")

    active_summaries: list[dict[str, Any]] = []
    active_decisions: list[dict[str, Any]] = []

    selection_mismatches = 0
    execution_mismatches = 0
    max_action_diff = 0.0

    total_queries = 0
    main_alarms = 0
    best_alt_lower_main_cnt = 0
    full_cap_passes = 0
    accepted_replacements = 0
    candidate_histogram: Counter[int] = Counter()
    episodes_with_replacements = set()

    protocol_audit: list[dict[str, Any]] = []
    scene_audit: list[dict[str, Any]] = []
    video_paths: list[dict[str, Any]] = []

    print(f"=== Auditing 400 Active TopK episodes in {active_output_dir} ===")

    for bench_id in range(total_expected):
        ep_id = f"{bench_id:06d}"
        ep_dir = active_episodes_dir / ep_id
        summary_p = ep_dir / "summary.json"
        decisions_p = ep_dir / "decisions.jsonl"
        vid_p = active_videos_dir / f"{ep_id}.mp4"

        if not summary_p.exists() or not decisions_p.exists():
            raise FileNotFoundError(f"Active episode {ep_id} missing summary or decisions file")

        summary = json.loads(summary_p.read_text(encoding="utf-8"))
        ep_decisions = [json.loads(l) for l in decisions_p.read_text(encoding="utf-8").splitlines() if l.strip()]

        if summary["episode_id"] != ep_id or int(summary["benchmark_episode_id"]) != bench_id:
            raise ValueError(f"Episode ID mismatch in active summary for {ep_id}")

        if len(ep_decisions) != int(summary["decision_rows"]):
            raise ValueError(f"Decision row count mismatch for active ep {ep_id}")

        # Contiguous decision indices check
        dec_indices = [int(d["decision_index"]) for d in ep_decisions]
        expected_indices = list(range(len(ep_decisions)))
        if dec_indices != expected_indices:
            raise ValueError(f"Non-contiguous decision indices in active ep {ep_id}: {dec_indices}")

        active_summaries.append(summary)
        active_decisions.extend(ep_decisions)

        m_ep = manifest_episodes[bench_id]
        m_scene = m_ep["scene"]
        m_fp = str(m_ep["scene_fingerprint_sha256"])

        # 1. Scene Parity
        if summary["scene_fingerprint_sha256"] != m_fp:
            raise RuntimeError(f"Scene fingerprint mismatch on active ep {ep_id}")

        scene_audit.append({
            "episode_id": ep_id,
            "benchmark_episode_id": bench_id,
            "manifest_fingerprint": m_fp,
            "runtime_contract_enforced": True,
            "status": "PASS",
        })

        # 2. Protocol
        succ = bool(summary["success"])
        ticks = int(summary["control_ticks"])
        steps = int(summary["simulation_steps"])
        min_dist = float(summary["minimum_tcp_distance_m"])
        rows_cnt = int(summary["decision_rows"])

        if ticks > 350 or rows_cnt > 35:
            raise RuntimeError(f"Active ep {ep_id} exceeded max horizon: ticks={ticks}, rows={rows_cnt}")

        if succ:
            if min_dist > 0.030:
                raise RuntimeError(f"Success active ep {ep_id} min_dist {min_dist} > 0.030m")
            if summary["first_3cm_crossing_physics_step"] is None or summary["first_3cm_crossing_control_tick"] is None:
                raise RuntimeError(f"Success active ep {ep_id} missing crossing step/tick")
            if summary["completed_physics_step"] != summary["first_3cm_crossing_physics_step"]:
                raise RuntimeError(f"Success active ep {ep_id} physics step mismatch")
            if summary["completed_control_tick"] != summary["first_3cm_crossing_control_tick"]:
                raise RuntimeError(f"Success active ep {ep_id} control tick mismatch")
        else:
            if ticks != 350 or steps != 1400 or rows_cnt != 35:
                raise RuntimeError(f"Failure active ep {ep_id} did not execute exact 350 ticks: ticks={ticks}, steps={steps}, rows={rows_cnt}")
            if min_dist <= 0.030:
                raise RuntimeError(f"Failure active ep {ep_id} reached <= 0.030m distance")
            if summary["first_3cm_crossing_physics_step"] is not None:
                raise RuntimeError(f"Failure active ep {ep_id} has non-null crossing step")

        protocol_audit.append({
            "episode_id": ep_id,
            "outcome": summary["outcome"],
            "success": succ,
            "control_ticks": ticks,
            "decision_rows": rows_cnt,
            "minimum_tcp_distance_m": min_dist,
            "status": "PASS",
        })

        # 3. Controller Logic & Action Equality
        ep_had_replacement = False
        for d in ep_decisions:
            total_queries += 1
            scores = [float(s) for s in d["online_risk"]["candidate_scores"]]
            main_s = scores[0]
            alt_scores = scores[1:]
            best_alt_idx = 1 + int(np.argmin(alt_scores))
            best_alt_s = scores[best_alt_idx]

            # Recompute expected decision
            if main_s < a_val:
                exp_idx = 0
                exp_mod = False
            elif best_alt_s >= main_s:
                exp_idx = 0
                exp_mod = False
            elif best_alt_s > c_val:
                exp_idx = 0
                exp_mod = False
            else:
                exp_idx = best_alt_idx
                exp_mod = True

            if main_s >= a_val:
                main_alarms += 1
                if best_alt_s < main_s:
                    best_alt_lower_main_cnt += 1
                    if best_alt_s <= c_val:
                        full_cap_passes += 1

            act_exec_idx = int(d.get("executed_candidate_index", d["online_risk"]["selected_candidate_index"]))
            if act_exec_idx != exp_idx:
                selection_mismatches += 1

            if exp_mod:
                accepted_replacements += 1
                candidate_histogram[exp_idx] += 1
                ep_had_replacement = True

            # Action equality check
            seq = np.asarray(d["executed_action_sequence"], dtype=np.float32)
            if act_exec_idx == 0:
                expected_chunk = np.asarray(d["main_candidate_action_chunk_env"], dtype=np.float32)
            else:
                expected_chunk = np.asarray(d["ace_candidate_chunks_env"][act_exec_idx - 1], dtype=np.float32)

            diff = float(np.max(np.abs(seq - expected_chunk[:len(seq)])))
            max_action_diff = max(max_action_diff, diff)
            if diff > 1e-6:
                execution_mismatches += 1

        if ep_had_replacement:
            episodes_with_replacements.add(ep_id)

        # 4. Video Check
        if not vid_p.exists() or vid_p.stat().st_size < 1000:
            raise FileNotFoundError(f"Active video missing or empty for ep {ep_id}")
        video_paths.append({
            "episode_id": ep_id,
            "video_path": str(vid_p),
            "size_bytes": vid_p.stat().st_size,
        })

    if selection_mismatches > 0 or execution_mismatches > 0 or max_action_diff > 1e-6:
        raise RuntimeError(f"Controller audit failure: selection_mismatches={selection_mismatches}, execution_mismatches={execution_mismatches}, max_diff={max_action_diff}")

    # Canonicalize active aggregate JSONLs
    canonical_active_summaries_p = active_output_dir / "canonical_episode_summaries.jsonl"
    canonical_active_decisions_p = active_output_dir / "canonical_decisions.jsonl"

    with canonical_active_summaries_p.open("w", encoding="utf-8") as f:
        for s in active_summaries:
            f.write(json.dumps(s) + "\n")

    with canonical_active_decisions_p.open("w", encoding="utf-8") as f:
        for d in active_decisions:
            f.write(json.dumps(d) + "\n")

    # 5. Paired Comparison Matrix
    persisted_success = 0
    rescues = 0
    regressions = 0
    persisted_failure = 0

    pair_details = []

    for s_act in active_summaries:
        ep_id = s_act["episode_id"]
        s_base = base_summaries[ep_id]

        b_succ = bool(s_base["success"])
        a_succ = bool(s_act["success"])

        if b_succ and a_succ:
            cat = "persisted_success"
            persisted_success += 1
        elif not b_succ and a_succ:
            cat = "rescue"
            rescues += 1
        elif b_succ and not a_succ:
            cat = "regression"
            regressions += 1
        else:
            cat = "persisted_failure"
            persisted_failure += 1

        pair_details.append({
            "episode_id": ep_id,
            "baseline_success": b_succ,
            "active_success": a_succ,
            "category": cat,
            "baseline_min_dist": float(s_base["minimum_tcp_distance_m"]),
            "active_min_dist": float(s_act["minimum_tcp_distance_m"]),
            "baseline_ticks": int(s_base["control_ticks"]),
            "active_ticks": int(s_act["control_ticks"]),
        })

    total_pairs = len(pair_details)
    if total_pairs != 400:
        raise ValueError(f"Expected 400 pairs, got {total_pairs}")

    base_succ_count = sum(1 for s in base_summaries.values() if s["success"])
    act_succ_count = sum(1 for s in active_summaries if s["success"])

    # Strict Arithmetic Invariant
    if act_succ_count != base_succ_count + rescues - regressions:
        raise RuntimeError(f"Arithmetic violation: active ({act_succ_count}) != base ({base_succ_count}) + rescues ({rescues}) - regressions ({regressions})")

    delta_episodes = act_succ_count - base_succ_count
    delta_pp = (act_succ_count / 400.0 - base_succ_count / 400.0) * 100.0

    paired_summary = {
        "schema_version": "ood400_paired_comparison_v1",
        "provenance_statement": "paired OOD400 engineering evaluation using an operating point selected from a predeclared Seen-derived threshold set.",
        "benchmark_name": "reaching_mimic_risk_ood400",
        "total_pairs": total_pairs,
        "baseline_successes": base_succ_count,
        "baseline_success_rate": base_succ_count / 400.0,
        "active_successes": act_succ_count,
        "active_success_rate": act_succ_count / 400.0,
        "delta_episodes": delta_episodes,
        "delta_percentage_points": delta_pp,
        "matrix": {
            "persisted_success": persisted_success,
            "rescues": rescues,
            "regressions": regressions,
            "persisted_failure": persisted_failure,
        },
        "arithmetic_verification": {
            "base_plus_rescue_minus_regress": base_succ_count + rescues - regressions,
            "matches_active": (act_succ_count == base_succ_count + rescues - regressions),
        },
        "pair_details": pair_details,
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    controller_audit_data = {
        "schema_version": "ood400_controller_audit_v1",
        "controller_rule": "argmin_on_alarm_cap_pass",
        "threshold_a_rule": a_rule,
        "threshold_a_value": a_val,
        "threshold_c_value": c_val,
        "total_decision_queries": total_queries,
        "main_alarm_queries": main_alarms,
        "best_alt_lower_main_queries": best_alt_lower_main_cnt,
        "full_cap_pass_queries": full_cap_passes,
        "accepted_replacements": accepted_replacements,
        "replacement_rate_per_query": accepted_replacements / total_queries if total_queries > 0 else 0.0,
        "episodes_with_replacements": len(episodes_with_replacements),
        "episodes_with_replacements_rate": len(episodes_with_replacements) / 400.0,
        "candidate_histogram": dict(candidate_histogram),
        "selection_mismatches": selection_mismatches,
        "execution_mismatches": execution_mismatches,
        "max_action_diff": max_action_diff,
        "status": "PASS",
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    active_result = {
        "schema_version": "ood400_active_result_v1",
        "benchmark_name": "reaching_mimic_risk_ood400",
        "total_episodes": total_expected,
        "success_count": act_succ_count,
        "failure_count": total_expected - act_succ_count,
        "success_rate": act_succ_count / total_expected,
        "failure_rate": 1.0 - (act_succ_count / total_expected),
        "delta_vs_baseline_pp": delta_pp,
        "rescues": rescues,
        "regressions": regressions,
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    (evidence_dir / "ACTIVE_RESULT.json").write_text(json.dumps(active_result, indent=2) + "\n")
    (evidence_dir / "PAIRED_COMPARISON.json").write_text(json.dumps(paired_summary, indent=2) + "\n")
    (evidence_dir / "CONTROLLER_AUDIT.json").write_text(json.dumps(controller_audit_data, indent=2) + "\n")
    (evidence_dir / "MEMBERSHIP_AUDIT.json").write_text(json.dumps({
        "total_episodes": total_expected,
        "missing_ids": 0,
        "extra_ids": 0,
        "status": "PASS",
    }, indent=2) + "\n")
    (evidence_dir / "ACTIVE_PROTOCOL.json").write_text(json.dumps(protocol_audit, indent=2) + "\n")
    (evidence_dir / "ACTIVE_VIDEO_PATHS.json").write_text(json.dumps(video_paths, indent=2) + "\n")

    # SHA256 sums
    sha_lines = []
    for f in sorted(evidence_dir.iterdir()):
        if f.is_file() and f.name != "ACTIVE_SHA256SUMS.txt":
            sha_lines.append(f"{sha256_file(f)}  {f.name}")
    (evidence_dir / "ACTIVE_SHA256SUMS.txt").write_text("\n".join(sha_lines) + "\n")

    print(f"=== Active Audit COMPLETE: Active Success={act_succ_count}/400 ({act_succ_count/4.0:.2f}%), Delta={delta_pp:+.2f} pp, Rescues={rescues}, Regressions={regressions} ===")
    return paired_summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--active-output-dir", type=Path, required=True)
    parser.add_argument("--baseline-output-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--controller-json", type=Path, required=True)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    args = parser.parse_args()

    audit_active_run(
        active_output_dir=args.active_output_dir,
        baseline_output_dir=args.baseline_output_dir,
        manifest_path=args.manifest,
        controller_json_path=args.controller_json,
        evidence_dir=args.evidence_dir,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
