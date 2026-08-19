#!/usr/bin/env python3
"""Prepare OOD400 TopK Active Controller Configuration, Shadow Intervention Forecast & Run Lock.

Freezes A, C=0.90, M=0.0, generates diagnostic shadow intervention forecast,
and writes RUN_LOCK.json into the active output directory.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from typing import Any

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import sha256_file


def prepare_topk_controller(
    *,
    selection_json_path: Path,
    baseline_decisions_path: Path,
    output_dir: Path,
    model_path: Path,
    norm_path: Path,
    manifest_path: Path,
    runner_path: Path,
    runtime_path: Path,
    active_output_dir: Path | None = None,
) -> dict[str, Any]:
    selection_json_path = Path(selection_json_path).resolve()
    baseline_decisions_path = Path(baseline_decisions_path).resolve()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    selection = json.loads(selection_json_path.read_text(encoding="utf-8"))
    a_val = float(selection["selected_threshold_a"])
    a_rule = str(selection["selected_rule_name"])
    c_val = 0.90
    m_val = 0.0

    # 1. Freeze Controller Spec
    controller_spec = {
        "schema_version": "ood400_frozen_controller_v1",
        "controller_type": "argmin_on_alarm_cap_pass",
        "main_threshold_name": a_rule,
        "main_threshold_value": a_val,
        "alternative_cap_name": "engineering_cap_0.90",
        "alternative_cap_value": c_val,
        "min_delta": m_val,
        "candidate_count": 9,
        "provenance": {
            "A_source": "Selected among a predeclared set of Seen-validation-derived operating points after evaluating their transfer on the OOD400 baseline.",
            "C_source": "Historical fixed engineering alternative-acceptance cap from OOD150",
            "M_source": "Zero min-delta invariant",
        },
        "locked_hashes": {
            "model_sha256": sha256_file(model_path),
            "normalization_sha256": sha256_file(norm_path),
            "manifest_sha256": sha256_file(manifest_path),
            "runner_sha256": sha256_file(runner_path),
            "runtime_sha256": sha256_file(runtime_path),
        },
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "FROZEN_CONTROLLER.json").write_text(json.dumps(controller_spec, indent=2) + "\n")

    # 2. Shadow Intervention Forecast
    decisions = [json.loads(line) for line in baseline_decisions_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    total_queries = len(decisions)
    alarm_queries = 0
    alt_lower_main = 0
    alt_pass_cap = 0
    full_pass_queries = 0
    episodes_with_hypothetical_interventions = set()

    for d in decisions:
        scores = [float(s) for s in d["online_risk"]["candidate_scores"]]
        main_score = scores[0]
        alt_scores = scores[1:]
        best_alt = min(alt_scores)

        if main_score >= a_val:
            alarm_queries += 1
            if best_alt < main_score:
                alt_lower_main += 1
                if best_alt <= c_val:
                    alt_pass_cap += 1
                    full_pass_queries += 1
                    episodes_with_hypothetical_interventions.add(d["episode_id"])

    forecast = {
        "schema_version": "ood400_shadow_intervention_forecast_v1",
        "total_baseline_queries": total_queries,
        "main_alarm_queries": alarm_queries,
        "main_alarm_rate": alarm_queries / total_queries if total_queries > 0 else 0.0,
        "best_alt_lower_main_queries": alt_lower_main,
        "best_alt_pass_cap_queries": alt_pass_cap,
        "full_pass_hypothetical_replacements": full_pass_queries,
        "hypothetical_replacement_rate": full_pass_queries / total_queries if total_queries > 0 else 0.0,
        "episodes_with_hypothetical_replacements": len(episodes_with_hypothetical_interventions),
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }
    (output_dir / "BASELINE_SHADOW_INTERVENTION_FORECAST.json").write_text(json.dumps(forecast, indent=2) + "\n")

    # 3. Create RUN_LOCK in active output directory if specified
    if active_output_dir:
        active_output_dir = Path(active_output_dir).resolve()
        active_output_dir.mkdir(parents=True, exist_ok=True)
        run_lock_p = active_output_dir / "RUN_LOCK.json"
        
        run_lock_doc = {
            "schema_version": "ood400_active_run_lock_v1",
            "mode": "online",
            "protocol": "3cm350_no_dwell",
            "threshold_a": a_val,
            "threshold_a_rule": a_rule,
            "threshold_c": c_val,
            "threshold_m": m_val,
            "locked_hashes": controller_spec["locked_hashes"],
            "created_timestamp": datetime.now(timezone.utc).isoformat(),
        }
        
        if run_lock_p.exists():
            existing_lock = json.loads(run_lock_p.read_text(encoding="utf-8"))
            if existing_lock["locked_hashes"] != run_lock_doc["locked_hashes"] or existing_lock["threshold_a"] != a_val:
                raise RuntimeError(f"RUN_LOCK.json mismatch in active dir {active_output_dir}! Refusing to mix controller data.")
        else:
            run_lock_p.write_text(json.dumps(run_lock_doc, indent=2) + "\n")

    print(f"=== Controller Frozen: A = {a_val:.6f} ({a_rule}), C = {c_val:.2f}, Forecast Replacements = {full_pass_queries}/{total_queries} queries ===")
    return controller_spec


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selection-json", type=Path, required=True)
    parser.add_argument("--baseline-decisions", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--norm", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--runner", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--active-output-dir", type=Path, default=None)
    args = parser.parse_args()

    prepare_topk_controller(
        selection_json_path=args.selection_json,
        baseline_decisions_path=args.baseline_decisions,
        output_dir=args.output_dir,
        model_path=args.model,
        norm_path=args.norm,
        manifest_path=args.manifest,
        runner_path=args.runner,
        runtime_path=args.runtime,
        active_output_dir=args.active_output_dir,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
