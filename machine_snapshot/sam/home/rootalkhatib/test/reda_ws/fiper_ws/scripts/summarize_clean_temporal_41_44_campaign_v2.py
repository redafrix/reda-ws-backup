#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


WORKSPACE = Path(__file__).resolve().parent.parent
EXPERIMENTS = WORKSPACE / "experiments"
REPORT = WORKSPACE / "reports/FIPER_CLEAN_TEMPORAL_41_44_FULL_AUDIT_REPORT_20260527.md"
CSV_OUT = WORKSPACE / "reports/FIPER_CLEAN_TEMPORAL_41_44_FULL_AUDIT_RESULTS_20260527.csv"

POLICIES = [
    "score_q95_K3",
    "score_q99_K3",
    "score_q95_K5",
    "or_q95_K3",
    "or_q99_K3",
    "and_q95_K3",
]


def pct(x: float | None) -> str:
    if x is None:
        return "NA"
    return f"{100.0 * x:.2f}%"


def num(x: float | None) -> str:
    if x is None:
        return "NA"
    return f"{x:.4f}"


def get_metric(metrics: dict[str, Any], split: str, policy: str, field: str) -> float | None:
    return metrics.get("episode_metrics", {}).get(split, {}).get(policy, {}).get(field)


def balanced_score(row: dict[str, Any]) -> float:
    return (
        2.0 * float(row.get("ood_fail_det25") or 0.0)
        + 1.0 * float(row.get("ood_fail_det") or 0.0)
        - 1.5 * float(row.get("ood_success_fa") or 0.0)
        - 0.5 * float(row.get("seen_success_fa") or 0.0)
        - 1.0 * float(row.get("ood_fail_never") or 0.0)
    )


def load_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for campaign_dir in sorted(EXPERIMENTS.glob("clean_temporal_41_44_*_20260527")):
        if "smoke" in campaign_dir.name or "invalid" in campaign_dir.name:
            continue
        for summary_path in sorted(campaign_dir.glob("jobs/*/summary.json")):
            job_dir = summary_path.parent
            metrics_path = job_dir / "metrics.json"
            audit_path = job_dir / "FEATURE_AUDIT.json"
            history_path = job_dir / "training_history.json"
            if not metrics_path.exists():
                continue
            summary = json.loads(summary_path.read_text())
            metrics = json.loads(metrics_path.read_text())
            audit = json.loads(audit_path.read_text()) if audit_path.exists() else {}
            history = json.loads(history_path.read_text()) if history_path.exists() else []
            for policy in POLICIES:
                row = {
                    "campaign": campaign_dir.name.replace("clean_temporal_41_44_", "").replace("_20260527", ""),
                    "job": job_dir.name,
                    "policy": policy,
                    "model": summary.get("model"),
                    "best_epoch": summary.get("best_epoch"),
                    "epochs_run": len(history),
                    "uses_object_positions_before": audit.get("uses_object_positions_before"),
                    "uses_reward": audit.get("uses_reward"),
                    "uses_success": audit.get("uses_success"),
                    "uses_task_metadata": audit.get("uses_task_metadata"),
                    "uses_ood_rows_for_train": audit.get("uses_ood_rows_for_train"),
                    "seen_success_fa": get_metric(metrics, "success_test_seen", policy, "episode_alarm_rate"),
                    "ood_success_fa": get_metric(metrics, "success_test_ood", policy, "episode_alarm_rate"),
                    "seen_fail_det": get_metric(metrics, "failure_test_seen", policy, "episode_alarm_rate"),
                    "seen_fail_det25": get_metric(metrics, "failure_test_seen", policy, "det_at_25"),
                    "seen_fail_mean_time": get_metric(metrics, "failure_test_seen", policy, "mean_first_norm_detected"),
                    "ood_fail_det": get_metric(metrics, "failure_eval_ood", policy, "episode_alarm_rate"),
                    "ood_fail_det10": get_metric(metrics, "failure_eval_ood", policy, "det_at_10"),
                    "ood_fail_det25": get_metric(metrics, "failure_eval_ood", policy, "det_at_25"),
                    "ood_fail_det50": get_metric(metrics, "failure_eval_ood", policy, "det_at_50"),
                    "ood_fail_mean_time": get_metric(metrics, "failure_eval_ood", policy, "mean_first_norm_detected"),
                    "ood_fail_never": get_metric(metrics, "failure_eval_ood", policy, "never_rate"),
                }
                row["balanced_score"] = balanced_score(row)
                rows.append(row)
    return rows


def main() -> None:
    rows = load_rows()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        with CSV_OUT.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    completed_campaigns = sorted({r["campaign"] for r in rows})
    completed_jobs = sorted({(r["campaign"], r["job"]) for r in rows})
    audit_failures = [
        r for r in rows
        if r["uses_object_positions_before"] or r["uses_reward"] or r["uses_success"] or r["uses_task_metadata"] or r["uses_ood_rows_for_train"]
    ]
    top_balanced = sorted(rows, key=lambda r: r["balanced_score"], reverse=True)[:25]

    low_fa_candidates = [
        r for r in rows
        if (r["ood_success_fa"] is not None and r["ood_success_fa"] <= 0.30)
        and (r["ood_fail_det"] is not None and r["ood_fail_det"] >= 0.75)
    ]
    low_fa_candidates = sorted(low_fa_candidates, key=lambda r: (r["ood_fail_det25"] or 0, -(r["ood_success_fa"] or 1)), reverse=True)[:25]

    lines: list[str] = []
    lines.append("# FIPER Clean Temporal 41/44 Full Audit Report")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- Completed campaigns found: `{len(completed_campaigns)}`")
    lines.append(f"- Completed job directories found: `{len(completed_jobs)}`")
    lines.append(f"- Policy rows summarized: `{len(rows)}`")
    lines.append(f"- Feature audit failures: `{len(audit_failures)}`")
    lines.append("")
    lines.append("This report is generated strictly from completed `summary.json`, `metrics.json`, `training_history.json`, and `FEATURE_AUDIT.json` artifacts. It excludes smoke and invalid row-leakage runs.")
    lines.append("")
    lines.append("## Completed Campaigns")
    lines.append("")
    for campaign in completed_campaigns:
        n_jobs = len({r["job"] for r in rows if r["campaign"] == campaign})
        lines.append(f"- `{campaign}`: {n_jobs} jobs")
    lines.append("")
    lines.append("## Feature Audit")
    lines.append("")
    if audit_failures:
        lines.append("Feature audit failed for these rows:")
        for r in audit_failures[:20]:
            lines.append(f"- `{r['campaign']}` / `{r['job']}` / `{r['policy']}`")
    else:
        lines.append("All completed jobs report no object-position oracle, no reward, no success flag, no task metadata, and no OOD rows for training.")
    lines.append("")
    lines.append("## Top Balanced Policies")
    lines.append("")
    lines.append("| Rank | Campaign | Job | Policy | Score | Seen Succ FA | OOD Succ FA | OOD Fail Det | OOD Det@25 | OOD Mean Time | OOD Never |")
    lines.append("|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for i, r in enumerate(top_balanced, start=1):
        lines.append(
            f"| {i} | `{r['campaign']}` | `{r['job']}` | `{r['policy']}` | {r['balanced_score']:.4f} | "
            f"{pct(r['seen_success_fa'])} | {pct(r['ood_success_fa'])} | {pct(r['ood_fail_det'])} | "
            f"{pct(r['ood_fail_det25'])} | {num(r['ood_fail_mean_time'])} | {pct(r['ood_fail_never'])} |"
        )
    lines.append("")
    lines.append("## Low False-Alarm Candidates")
    lines.append("")
    if low_fa_candidates:
        lines.append("| Rank | Campaign | Job | Policy | Seen Succ FA | OOD Succ FA | OOD Fail Det | OOD Det@25 | OOD Mean Time |")
        lines.append("|---:|---|---|---|---:|---:|---:|---:|---:|")
        for i, r in enumerate(low_fa_candidates, start=1):
            lines.append(
                f"| {i} | `{r['campaign']}` | `{r['job']}` | `{r['policy']}` | {pct(r['seen_success_fa'])} | "
                f"{pct(r['ood_success_fa'])} | {pct(r['ood_fail_det'])} | {pct(r['ood_fail_det25'])} | {num(r['ood_fail_mean_time'])} |"
            )
    else:
        lines.append("No completed policy simultaneously reached OOD success FA <= 30% and OOD failure detection >= 75%.")
    lines.append("")
    lines.append("## Final Fields")
    lines.append("")
    lines.append("```text")
    lines.append(f"CLEAN_TEMPORAL_COMPLETED_CAMPAIGNS = {len(completed_campaigns)}")
    lines.append(f"CLEAN_TEMPORAL_COMPLETED_JOBS = {len(completed_jobs)}")
    lines.append(f"CLEAN_FEATURE_AUDIT_FAILURES = {len(audit_failures)}")
    lines.append(f"CSV_RESULTS = {CSV_OUT.relative_to(WORKSPACE)}")
    lines.append("```")
    lines.append("")

    REPORT.write_text("\n".join(lines))
    print(REPORT)
    print(CSV_OUT)


if __name__ == "__main__":
    main()
