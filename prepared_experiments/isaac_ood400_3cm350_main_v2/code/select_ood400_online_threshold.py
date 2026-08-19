#!/usr/bin/env python3
"""Deterministic Online Alarm Threshold A Selection for OOD400 TopK Active Run.

Selects strictly among the 5 predeclared Seen-derived operating points using
the frozen 6-step decision procedure.
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

PRIMARY_CANDIDATES = [
    "Best F1",
    "Fixed 0.5",
    "q90 success",
    "q95 success",
    "q99 success",
]


def select_online_threshold(
    sweep_json_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    sweep_json_path = Path(sweep_json_path).resolve()
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sweep_data = json.loads(sweep_json_path.read_text(encoding="utf-8"))
    candidates = [row for row in sweep_data if row["rule_name"] in PRIMARY_CANDIDATES]

    if len(candidates) != 5:
        raise ValueError(f"Expected 5 candidates in sweep, found {len(candidates)}")

    audit_steps: list[str] = []

    # Step 1: Find maximum failure-detection rate among the five
    max_fail_det = max(c["fail_detection_rate"] for c in candidates)
    audit_steps.append(f"Step 1: Maximum fail detection rate among 5 candidates is {max_fail_det*100:.2f}%")

    # Step 2: Retain all operating points achieving that maximum
    retained_step2 = [c for c in candidates if c["fail_detection_rate"] == max_fail_det]
    audit_steps.append(f"Step 2: Retained {len(retained_step2)} points achieving max fail detection: {[c['rule_name'] for c in retained_step2]}")

    # Step 3: If at least one retained point has Det@50 >= 80%: discard retained points below 80% Det@50
    has_ge80 = any(c["det_at_50_pct"] >= 80.0 for c in retained_step2)
    if has_ge80:
        retained_step3 = [c for c in retained_step2 if c["det_at_50_pct"] >= 80.0]
        audit_steps.append(f"Step 3: Filtered for Det@50 >= 80%, retained {len(retained_step3)} points: {[c['rule_name'] for c in retained_step3]}")
    else:
        retained_step3 = retained_step2
        audit_steps.append("Step 3: No retained point achieved Det@50 >= 80%, retaining all Step 2 candidates")

    # Step 4: Among remaining, choose minimum success false-alarm rate
    min_succ_fa = min(c["succ_false_alarm_rate"] for c in retained_step3)
    retained_step4 = [c for c in retained_step3 if c["succ_false_alarm_rate"] == min_succ_fa]
    audit_steps.append(f"Step 4: Minimum success FA rate is {min_succ_fa*100:.2f}%, retained {len(retained_step4)} points: {[c['rule_name'] for c in retained_step4]}")

    # Step 5: Tie breaker: choose maximum Det@25
    if len(retained_step4) > 1:
        max_det25 = max(c["det_at_25_pct"] for c in retained_step4)
        retained_step5 = [c for c in retained_step4 if c["det_at_25_pct"] == max_det25]
        audit_steps.append(f"Step 5: Tie-break max Det@25 ({max_det25:.2f}%), retained {len(retained_step5)} points: {[c['rule_name'] for c in retained_step5]}")
    else:
        retained_step5 = retained_step4

    # Step 6: Final tie: choose higher threshold value
    if len(retained_step5) > 1:
        selected = max(retained_step5, key=lambda c: float(c["threshold"]))
        audit_steps.append(f"Step 6: Final tie-break chose higher threshold: {selected['rule_name']} ({selected['threshold']:.4f})")
    else:
        selected = retained_step5[0]
        audit_steps.append(f"Step 6: Uniquely selected {selected['rule_name']} ({selected['threshold']:.4f})")

    result = {
        "schema_version": "ood400_online_a_selection_v1",
        "provenance_statement": "Selected among a predeclared set of Seen-validation-derived operating points after evaluating their transfer on the OOD400 baseline.",
        "new_ood_numerical_threshold_fit": False,
        "selected_rule_name": selected["rule_name"],
        "selected_threshold_a": float(selected["threshold"]),
        "selected_metrics": selected,
        "candidate_pool": candidates,
        "selection_audit_steps": audit_steps,
        "created_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    output_path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"=== Online A Selection COMPLETE: {selected['rule_name']} (A = {selected['threshold']:.6f}) ===")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sweep-json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    select_online_threshold(
        sweep_json_path=args.sweep_json,
        output_path=args.output,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
