#!/usr/bin/env python3
"""Validate NextGen v2 smoke/full campaign artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def split_name_from_refs(refs: str) -> str:
    path = Path(refs)
    return path.parents[1].name


def count_lines(path: Path) -> int:
    with path.open() as f:
        return sum(1 for _ in f)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--expected-splits", nargs="+", required=True)
    args = parser.parse_args()

    config = load_json(Path(args.config))
    job_names = [job["name"] for job in config["jobs"]]
    output_root = Path(args.output_root)
    expected_split_names = [split_name_from_refs(refs) for refs in args.expected_splits]

    failures: list[str] = []
    report: dict[str, Any] = {
        "output_root": str(output_root),
        "expected_jobs": len(job_names),
        "expected_splits": expected_split_names,
        "splits": {},
    }

    for split_name in expected_split_names:
        split_dir = output_root / split_name
        jobs_dir = split_dir / "jobs"
        split_report: dict[str, Any] = {"jobs": {}, "failed_jobs_lines": 0}
        report["splits"][split_name] = split_report

        if not jobs_dir.exists():
            failures.append(f"{split_name}: missing jobs dir {jobs_dir}")
            continue

        failed_jobs = split_dir / "failed_jobs.jsonl"
        if failed_jobs.exists():
            n_failed = count_lines(failed_jobs)
            split_report["failed_jobs_lines"] = n_failed
            if n_failed:
                failures.append(f"{split_name}: failed_jobs.jsonl has {n_failed} line(s)")

        for job_name in job_names:
            job_dir = jobs_dir / job_name
            job_report: dict[str, Any] = {}
            split_report["jobs"][job_name] = job_report
            required = ["summary.json", "metrics.json", "FEATURE_AUDIT.json", "scores.jsonl", "training_history.json", "model.pt"]
            for filename in required:
                path = job_dir / filename
                if not path.exists():
                    failures.append(f"{split_name}/{job_name}: missing {filename}")
            if not job_dir.exists():
                continue

            if (job_dir / "scores.jsonl").exists():
                n_scores = count_lines(job_dir / "scores.jsonl")
                job_report["score_rows"] = n_scores
                if n_scores <= 0:
                    failures.append(f"{split_name}/{job_name}: scores.jsonl is empty")

            if (job_dir / "FEATURE_AUDIT.json").exists():
                audit = load_json(job_dir / "FEATURE_AUDIT.json")
                job_report["feature_audit"] = {
                    "history_dim": audit.get("history_dim"),
                    "current_feature_dim": audit.get("current_feature_dim"),
                    "num_train_groups": audit.get("num_train_groups"),
                    "uses_group_metadata_as_training_label_only": audit.get("uses_group_metadata_as_training_label_only"),
                    "hardstop_is_real_residual_gate": audit.get("hardstop_is_real_residual_gate"),
                }
                for key in [
                    "uses_object_positions_before",
                    "uses_reward",
                    "uses_success",
                    "uses_task_metadata_as_input",
                    "uses_ood_rows_for_train",
                    "uses_future_timestep",
                ]:
                    if audit.get(key):
                        failures.append(f"{split_name}/{job_name}: forbidden audit flag {key}=true")
                if "groupdro" in job_name or "_adv_" in job_name:
                    if int(audit.get("num_train_groups") or 0) < 2:
                        failures.append(f"{split_name}/{job_name}: group-aware job has <2 train groups")
                if "dynamics" in job_name and not audit.get("hardstop_is_real_residual_gate"):
                    failures.append(f"{split_name}/{job_name}: dynamics job did not expose real residual gate")

            if (job_dir / "summary.json").exists():
                summary = load_json(job_dir / "summary.json")
                job_report["best_epoch"] = summary.get("best_epoch")
                job_report["objective"] = summary.get("objective")

    report["status"] = "PASS" if not failures else "FAIL"
    report["failures"] = failures
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "NEXTGEN_V2_VALIDATION_REPORT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")

    lines = [
        "# NextGen V2 Campaign Validation Report",
        "",
        f"Status: **{report['status']}**",
        f"Expected splits: {len(expected_split_names)}",
        f"Expected jobs per split: {len(job_names)}",
        "",
    ]
    if failures:
        lines.append("## Failures")
        for failure in failures[:200]:
            lines.append(f"- {failure}")
    else:
        lines.append("All expected job artifacts are present, score files are non-empty, and feature audits passed.")
    (output_root / "NEXTGEN_V2_VALIDATION_REPORT.md").write_text("\n".join(lines) + "\n")

    print(json.dumps({"status": report["status"], "failures": len(failures), "output_root": str(output_root)}, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
