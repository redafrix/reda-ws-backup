#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any


WORKSPACE = Path(__file__).resolve().parent.parent
EXPERIMENTS = WORKSPACE / "experiments"
REPORT = WORKSPACE / "reports/FIPER_CLEAN_TEMPORAL_41_44_PARTIAL_RESULTS_AUDIT_20260527.md"
CSV_IN = WORKSPACE / "reports/FIPER_CLEAN_TEMPORAL_41_44_FULL_AUDIT_RESULTS_20260527.csv"

EXPECTED_JOBS = {
    "clean_041_tcn_k8_no_current_proprio",
    "clean_041_tcn_k8_with_current_proprio",
    "clean_041_tcn_k16_no_current_proprio",
    "clean_044_lstm_k8_with_current_proprio",
    "clean_044_lstm_k16_with_current_proprio",
}

EXPECTED_CAMPAIGNS = [
    "target_object_fold00",
    "target_object_fold01",
    "target_object_fold02",
    "target_object_fold03",
    "target_object_fold04",
    "global_main",
    "ood_task_8_9",
    "ood_perturbation_mug",
    "ood_perturbation_milk",
    "ood_perturbation_object",
    "ood_perturbation_env",
    "ood_family_spatial",
    "ood_family_object_family",
    "ood_family_goal",
    "ood_family_10_family",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def as_float(value: str | None) -> float | None:
    if value in (None, "", "None", "NA"):
        return None
    return float(value)


def pct(value: float | None) -> str:
    return "NA" if value is None else f"{100.0 * value:.2f}%"


def num(value: float | None) -> str:
    return "NA" if value is None else f"{value:.4f}"


def avg(values: list[float | None]) -> float | None:
    clean = [v for v in values if v is not None]
    return None if not clean else mean(clean)


def campaign_name(path: Path) -> str:
    return path.name.replace("clean_temporal_41_44_", "").replace("_20260527", "")


def score_line_count(path: Path) -> int:
    with path.open("rb") as f:
        return sum(1 for _ in f)


def audit_artifacts() -> tuple[list[dict[str, Any]], list[str]]:
    audits: list[dict[str, Any]] = []
    notes: list[str] = []
    for campaign_dir in sorted(EXPERIMENTS.glob("clean_temporal_41_44_*_20260527")):
        name = campaign_name(campaign_dir)
        if "smoke" in name or "invalid" in name:
            continue
        jobs_dir = campaign_dir / "jobs"
        if not jobs_dir.exists():
            continue
        for job_dir in sorted(p for p in jobs_dir.iterdir() if p.is_dir()):
            entry: dict[str, Any] = {
                "campaign": name,
                "job": job_dir.name,
                "status": "incomplete",
                "feature_bad": None,
                "score_rows_expected": None,
                "score_rows_actual": None,
                "score_row_match": None,
                "best_epoch": None,
                "epochs_run": None,
                "model": None,
                "mode": None,
            }
            summary_path = job_dir / "summary.json"
            metrics_path = job_dir / "metrics.json"
            audit_path = job_dir / "FEATURE_AUDIT.json"
            scores_path = job_dir / "scores.jsonl"
            history_path = job_dir / "training_history.json"
            if not (summary_path.exists() and metrics_path.exists()):
                audits.append(entry)
                continue
            summary = load_json(summary_path)
            metrics = load_json(metrics_path)
            audit = load_json(audit_path) if audit_path.exists() else {}
            history = json.loads(history_path.read_text()) if history_path.exists() else []
            entry["status"] = "complete"
            entry["best_epoch"] = summary.get("best_epoch")
            entry["epochs_run"] = len(history)
            entry["model"] = summary.get("model")
            entry["mode"] = summary.get("mode")
            bad_flags = [
                "uses_object_positions_before",
                "uses_reward",
                "uses_success",
                "uses_task_metadata",
                "uses_ood_rows_for_train",
            ]
            entry["feature_bad"] = any(bool(audit.get(flag)) for flag in bad_flags)
            row_metrics = metrics.get("row_metrics", {})
            # The runner scores every loaded split except success_train_seen.
            expected = sum(int(v.get("rows", 0)) for k, v in row_metrics.items() if k != "success_train_seen")
            actual = score_line_count(scores_path) if scores_path.exists() else None
            entry["score_rows_expected"] = expected
            entry["score_rows_actual"] = actual
            entry["score_row_match"] = actual == expected
            if entry["feature_bad"]:
                notes.append(f"Feature audit failed: {name}/{job_dir.name}")
            if actual != expected:
                notes.append(f"Score row mismatch: {name}/{job_dir.name}: expected {expected}, actual {actual}")
            audits.append(entry)
    return audits, notes


def load_policy_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not CSV_IN.exists():
        return rows
    for raw in csv.DictReader(CSV_IN.open()):
        row = dict(raw)
        for key in [
            "seen_success_fa",
            "ood_success_fa",
            "seen_fail_det",
            "seen_fail_det25",
            "seen_fail_mean_time",
            "ood_fail_det",
            "ood_fail_det10",
            "ood_fail_det25",
            "ood_fail_det50",
            "ood_fail_mean_time",
            "ood_fail_never",
            "balanced_score",
        ]:
            row[key] = as_float(row.get(key))
        rows.append(row)
    return rows


def top_rows(rows: list[dict[str, Any]], campaign_prefix: str | None = None, limit: int = 10) -> list[dict[str, Any]]:
    selected = rows
    if campaign_prefix:
        selected = [r for r in rows if r["campaign"].startswith(campaign_prefix)]
    return sorted(selected, key=lambda r: r["balanced_score"] if r["balanced_score"] is not None else -999, reverse=True)[:limit]


def low_fa_rows(rows: list[dict[str, Any]], campaign_prefix: str | None = None, max_fa: float = 0.30, min_det: float = 0.75, limit: int = 10) -> list[dict[str, Any]]:
    selected = rows
    if campaign_prefix:
        selected = [r for r in rows if r["campaign"].startswith(campaign_prefix)]
    selected = [
        r for r in selected
        if r["ood_success_fa"] is not None
        and r["ood_success_fa"] <= max_fa
        and r["ood_fail_det"] is not None
        and r["ood_fail_det"] >= min_det
    ]
    return sorted(selected, key=lambda r: ((r["ood_fail_det25"] or 0.0), -(r["ood_success_fa"] or 1.0)), reverse=True)[:limit]


def aggregate_by_job(rows: list[dict[str, Any]], campaigns: set[str], policy: str = "score_q95_K3") -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["campaign"] in campaigns and row["policy"] == policy:
            grouped[row["job"]].append(row)
    out: list[dict[str, Any]] = []
    for job, items in sorted(grouped.items()):
        out.append({
            "job": job,
            "n": len(items),
            "ood_success_fa": avg([r["ood_success_fa"] for r in items]),
            "ood_fail_det": avg([r["ood_fail_det"] for r in items]),
            "ood_fail_det25": avg([r["ood_fail_det25"] for r in items]),
            "ood_fail_mean_time": avg([r["ood_fail_mean_time"] for r in items]),
            "seen_success_fa": avg([r["seen_success_fa"] for r in items]),
        })
    return out


def append_rows_table(lines: list[str], title: str, rows: list[dict[str, Any]]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    if not rows:
        lines.append("No rows matched.")
        lines.append("")
        return
    lines.append("| Rank | Campaign | Job | Policy | Score | Seen FA | OOD FA | OOD Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean Time | Never |")
    lines.append("|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for i, r in enumerate(rows, start=1):
        lines.append(
            f"| {i} | `{r['campaign']}` | `{r['job']}` | `{r['policy']}` | {num(r['balanced_score'])} | "
            f"{pct(r['seen_success_fa'])} | {pct(r['ood_success_fa'])} | {pct(r['ood_fail_det'])} | "
            f"{pct(r['ood_fail_det10'])} | {pct(r['ood_fail_det25'])} | {pct(r['ood_fail_det50'])} | "
            f"{num(r['ood_fail_mean_time'])} | {pct(r['ood_fail_never'])} |"
        )
    lines.append("")


def main() -> None:
    audits, audit_notes = audit_artifacts()
    rows = load_policy_rows()
    complete_jobs = {(a["campaign"], a["job"]) for a in audits if a["status"] == "complete"}
    incomplete_jobs = [a for a in audits if a["status"] != "complete"]
    campaign_job_counts = Counter(c for c, _ in complete_jobs)
    completed_campaigns = sorted(campaign_job_counts)
    missing_campaigns = [c for c in EXPECTED_CAMPAIGNS if campaign_job_counts.get(c, 0) == 0]
    partial_campaigns = [
        c for c in EXPECTED_CAMPAIGNS
        if 0 < campaign_job_counts.get(c, 0) < len(EXPECTED_JOBS)
    ]
    feature_bad = [a for a in audits if a["feature_bad"]]
    score_mismatch = [a for a in audits if a["status"] == "complete" and not a["score_row_match"]]
    supervised_jobs = [a for a in audits if a["status"] == "complete" and a["mode"] == "supervised"]

    target_strong = {f"target_object_fold0{i}" for i in range(4)}
    target_all = {f"target_object_fold0{i}" for i in range(5)}

    lines: list[str] = []
    lines.append("# FIPER Clean Temporal 41/44 Partial Results Audit")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("Read-only analysis of completed artifacts while the full sequential Sam sweep may still be running. Smoke runs are excluded.")
    lines.append("")
    lines.append("## Artifact Integrity")
    lines.append("")
    lines.append(f"- Completed jobs: `{len(complete_jobs)}`")
    lines.append(f"- Incomplete/failed job dirs: `{len(incomplete_jobs)}`")
    lines.append(f"- Completed campaigns: `{len(completed_campaigns)}`")
    lines.append(f"- Policy rows loaded: `{len(rows)}`")
    lines.append(f"- Feature audit failures: `{len(feature_bad)}`")
    lines.append(f"- Score-row mismatches: `{len(score_mismatch)}`")
    lines.append(f"- Supervised risk jobs: `{len(supervised_jobs)}`")
    lines.append("")
    lines.append("Completed campaign job counts:")
    for campaign in EXPECTED_CAMPAIGNS:
        lines.append(f"- `{campaign}`: {campaign_job_counts.get(campaign, 0)} / {len(EXPECTED_JOBS)} jobs")
    lines.append("")
    if audit_notes:
        lines.append("Audit notes:")
        for note in audit_notes[:50]:
            lines.append(f"- {note}")
        lines.append("")
    lines.append("Interpretation guardrail: jobs marked `supervised` train on seen success plus seen failure rows. They are not success-only RND; they are legitimate only if OOD rows remain excluded from train/val/calib.")
    lines.append("")

    append_rows_table(lines, "Top Overall Completed Policies", top_rows(rows, None, 15))
    append_rows_table(lines, "Top Target-Object Policies", top_rows([r for r in rows if r["campaign"].startswith("target_object_")], None, 15))
    append_rows_table(lines, "Target-Object Low-FA Candidates", low_fa_rows(rows, "target_object_", 0.30, 0.75, 15))
    append_rows_table(lines, "Top OOD Task 8/9 Policies", top_rows(rows, "ood_task_8_9", 10))
    append_rows_table(lines, "OOD Task 8/9 Low-FA Candidates", low_fa_rows(rows, "ood_task_8_9", 0.30, 0.75, 10))
    append_rows_table(lines, "Top OOD Perturbation Mug Policies", top_rows(rows, "ood_perturbation_mug", 10))
    append_rows_table(lines, "OOD Perturbation Mug Low-FA Candidates", low_fa_rows(rows, "ood_perturbation_mug", 0.30, 0.75, 10))
    append_rows_table(lines, "Top OOD Perturbation Milk Policies", top_rows(rows, "ood_perturbation_milk", 10))
    append_rows_table(lines, "OOD Perturbation Milk Low-FA Candidates", low_fa_rows(rows, "ood_perturbation_milk", 0.30, 0.75, 10))

    lines.append("## Target-Object Fold Average By Job")
    lines.append("")
    lines.append("Averaged over folds 00-03 only; fold04 is lower support and should not drive decisions.")
    lines.append("")
    lines.append("| Job | Folds | Seen FA | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for r in aggregate_by_job(rows, target_strong, "score_q95_K3"):
        lines.append(
            f"| `{r['job']}` | {r['n']} | {pct(r['seen_success_fa'])} | {pct(r['ood_success_fa'])} | "
            f"{pct(r['ood_fail_det'])} | {pct(r['ood_fail_det25'])} | {num(r['ood_fail_mean_time'])} |"
        )
    lines.append("")
    lines.append("Same policy averaged over all target-object folds, including low-support fold04:")
    lines.append("")
    lines.append("| Job | Folds | Seen FA | OOD Success FA | OOD Failure Det | OOD Det@25 | Mean Time |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for r in aggregate_by_job(rows, target_all, "score_q95_K3"):
        lines.append(
            f"| `{r['job']}` | {r['n']} | {pct(r['seen_success_fa'])} | {pct(r['ood_success_fa'])} | "
            f"{pct(r['ood_fail_det'])} | {pct(r['ood_fail_det25'])} | {num(r['ood_fail_mean_time'])} |"
        )
    lines.append("")

    lines.append("## Current Judgment")
    lines.append("")
    if feature_bad or score_mismatch:
        lines.append("Do not trust these results yet: artifact integrity checks failed.")
    else:
        lines.append("The completed artifacts pass the local sanity checks: no forbidden feature flags and score row counts match the evaluated rows.")
    lines.append("")
    lines.append("- The clean temporal supervised models are clearly less pathological than the old action-only target-object result, but target-object OOD is not solved: useful detection usually still costs substantial successful-OOD alarms.")
    lines.append("- OOD task 8/9 and OOD perturbation mug look substantially healthier than target-object folds so far.")
    lines.append("- The sweep is incomplete until the remaining perturbation/family/global reruns finish; current conclusions are partial.")
    lines.append("- `global_main` must be rerun after the empty-OOD split patch; old global-main job dirs only contain configs and are not valid results.")
    lines.append("")
    lines.append("## Final Fields")
    lines.append("")
    lines.append("```text")
    lines.append(f"PARTIAL_AUDIT_COMPLETED_JOBS = {len(complete_jobs)}")
    lines.append(f"PARTIAL_AUDIT_COMPLETED_CAMPAIGNS = {len(completed_campaigns)}")
    lines.append(f"PARTIAL_AUDIT_PARTIAL_CAMPAIGNS = {', '.join(partial_campaigns) if partial_campaigns else 'NONE'}")
    lines.append(f"PARTIAL_AUDIT_MISSING_CAMPAIGNS = {', '.join(missing_campaigns) if missing_campaigns else 'NONE'}")
    lines.append(f"PARTIAL_AUDIT_FEATURE_FAILURES = {len(feature_bad)}")
    lines.append(f"PARTIAL_AUDIT_SCORE_ROW_MISMATCHES = {len(score_mismatch)}")
    lines.append("RESULTS_ARE_FINAL = NO")
    lines.append("```")
    lines.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines))
    print(REPORT)


if __name__ == "__main__":
    main()
