#!/usr/bin/env python3
"""Failure-aware policy selection for v2_018_transformer_k16.

This is a held-out policy-selection experiment:
  - Tune/select operating points on dev object folds.
  - Report once on a held-out target-object fold.

It does not retrain the model and does not tune on the held-out fold.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
from pathlib import Path

from analyze_transformer_k16_online_policy_v1 import (
    build_policies,
    evaluate_policy,
    load_traces,
    objective,
)


ALL_OBJECT_FOLDS = [
    "fold_00_holdout_alphabet_soup_bbq_sauce",
    "fold_01_holdout_butter_chocolate_pudding",
    "fold_02_holdout_cream_cheese_ketchup",
    "fold_03_holdout_milk_orange_juice",
    "fold_04_holdout_salad_dressing_tomato_sauce",
]


def row_from_metrics(policy_name: str, family: str, metrics: dict) -> dict:
    success_seen = metrics["success_test_seen"]
    success_ood = metrics["success_test_ood"]
    failure = metrics["failure_eval_ood"]
    row = {
        "policy": policy_name,
        "family": family,
        "success_seen_episodes": success_seen["episodes"],
        "success_ood_episodes": success_ood["episodes"],
        "failure_ood_episodes": failure["episodes"],
        "success_seen_fa": success_seen["alarm_rate"],
        "success_ood_fa": success_ood["alarm_rate"],
        "failure_detection": failure["alarm_rate"],
        "failure_det_at_10": failure["det_at_10"],
        "failure_det_at_25": failure["det_at_25"],
        "failure_det_at_50": failure["det_at_50"],
        "failure_mean_time": failure["mean_time_detected"],
        "failure_never": failure["never_rate"],
    }
    row["objective"] = objective(row)
    return row


def score_for_selection(row: dict, fa_budget: float) -> float:
    """Select for high failure utility subject to a soft FA budget."""

    fa_penalty = max(0.0, row["success_ood_fa"] - fa_budget)
    return (
        2.5 * row["failure_detection"]
        + 1.75 * row["failure_det_at_50"]
        + 1.50 * row["failure_det_at_25"]
        - 0.30
        * (row["failure_mean_time"] if row["failure_mean_time"] is not None else 1.0)
        - 6.0 * fa_penalty
        - 1.0 * row["success_ood_fa"]
    )


def pct(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{100 * value:.1f}%"


def num(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.3f}"


def evaluate_folds(root: Path, job: str, folds: list[str]) -> tuple[list[dict], dict]:
    traces = load_traces(root, folds, job)
    policies, calibration = build_policies(traces)
    rows = []
    for policy in policies:
        metrics = evaluate_policy(traces, policy["trigger"])
        rows.append(row_from_metrics(policy["name"], policy["family"], metrics))
    return rows, calibration


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="experiments/clean_temporal_nextgen_v2_full_all_20260527",
    )
    parser.add_argument("--job", default="v2_018_transformer_k16")
    parser.add_argument(
        "--heldout-fold",
        default="fold_00_holdout_alphabet_soup_bbq_sauce",
    )
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    root = Path(args.root)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    dev_folds = [fold for fold in ALL_OBJECT_FOLDS if fold != args.heldout_fold]
    dev_rows, dev_calibration = evaluate_folds(root, args.job, dev_folds)
    test_rows, test_calibration = evaluate_folds(root, args.job, [args.heldout_fold])
    test_by_policy = {row["policy"]: row for row in test_rows}

    selected = []
    for fa_budget in [0.20, 0.30, 0.35, 0.40, 0.45, 0.50]:
        eligible = [row for row in dev_rows if row["success_ood_fa"] <= fa_budget]
        if not eligible:
            eligible = dev_rows
        best = max(eligible, key=lambda row: score_for_selection(row, fa_budget))
        selected.append(
            {
                "fa_budget": fa_budget,
                "selected_policy": best["policy"],
                "selected_family": best["family"],
                "dev": best,
                "heldout": test_by_policy[best["policy"]],
            }
        )

    for name, rows in [("dev_policy_rows.csv", dev_rows), ("heldout_policy_rows.csv", test_rows)]:
        with (out_dir / name).open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    (out_dir / "dev_calibration.json").write_text(
        json.dumps(dev_calibration, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "heldout_calibration.json").write_text(
        json.dumps(test_calibration, indent=2, sort_keys=True) + "\n"
    )
    (out_dir / "selected_policies.json").write_text(
        json.dumps(selected, indent=2, sort_keys=True) + "\n"
    )

    lines = [
        "# Failure-Aware Policy Tuning Report",
        "",
        f"Model: `{args.job}`",
        f"Held-out final fold: `{args.heldout_fold}`",
        f"Dev folds: `{', '.join(dev_folds)}`",
        "",
        "The policy is selected using success+failure metrics on dev folds, then evaluated on the held-out fold.",
        "No held-out fold metrics are used for selection.",
        "",
        "| FA Budget | Selected Policy | Family | Dev OOD FA | Dev Det | Dev Det@25 | Dev Det@50 | Heldout OOD FA | Heldout Det | Heldout Det@25 | Heldout Det@50 | Heldout Mean Time |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in selected:
        dev = item["dev"]
        held = item["heldout"]
        lines.append(
            "| "
            + " | ".join(
                [
                    pct(item["fa_budget"]),
                    f"`{item['selected_policy']}`",
                    item["selected_family"],
                    pct(dev["success_ood_fa"]),
                    pct(dev["failure_detection"]),
                    pct(dev["failure_det_at_25"]),
                    pct(dev["failure_det_at_50"]),
                    pct(held["success_ood_fa"]),
                    pct(held["failure_detection"]),
                    pct(held["failure_det_at_25"]),
                    pct(held["failure_det_at_50"]),
                    num(held["failure_mean_time"]),
                ]
            )
            + " |"
        )

    baseline_names = [
        "q95_consec_K3",
        "q95_mass_conformal_alpha0p15",
        "q95_mass_1",
        "q95_mass_3",
    ]
    lines.extend(
        [
            "",
            "## Held-Out Baselines",
            "",
            "| Policy | Family | OOD FA | Seen FA | Det | Det@25 | Det@50 | Mean Time | Never |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for name in baseline_names:
        row = test_by_policy[name]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['policy']}`",
                    row["family"],
                    pct(row["success_ood_fa"]),
                    pct(row["success_seen_fa"]),
                    pct(row["failure_detection"]),
                    pct(row["failure_det_at_25"]),
                    pct(row["failure_det_at_50"]),
                    num(row["failure_mean_time"]),
                    pct(row["failure_never"]),
                ]
            )
            + " |"
        )

    (out_dir / "FAILURE_AWARE_POLICY_TUNING_REPORT.md").write_text(
        "\n".join(lines) + "\n"
    )

    print(f"Wrote failure-aware tuning report to {out_dir}")


if __name__ == "__main__":
    main()
