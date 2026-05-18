#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import datetime
import subprocess

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws")
R = ROOT / "asynchvla_ws/stage8_ultimate/reports"
OUT = ROOT / "asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md"


def read(name: str, n: int = 12000) -> str:
    p = R / name
    if not p.exists():
        return f"_Missing: `{name}`_"
    txt = p.read_text(errors="ignore")
    return txt[:n]


def main():
    status = subprocess.run(["python3", "asynchvla_ws/scripts/stage8_job_manager.py", "status"], cwd=ROOT, text=True, stdout=subprocess.PIPE).stdout
    files = subprocess.run(["bash", "-lc", "find /home/redafrix/tests/internship/codex_reports/stage8 -maxdepth 3 -type f | sort"], text=True, stdout=subprocess.PIPE).stdout
    lines = [
        "# ASYNCVLA SimVLA Stage 8 Ultimate Experiment Report",
        "",
        f"Generated: `{datetime.datetime.now().isoformat(timespec='seconds')}`",
        "",
        "## Executive Summary",
        "",
        "This final report is generated from the currently available Stage 8 reports. If the 72-hour queue is still running, treat this as an interim report.",
        "",
        "## Queue Status",
        "",
        "```json",
        status.strip(),
        "```",
        "",
        "## LIBERO-PRO Results",
        "",
        read("stage8_libero_pro_expanded_rollout_results.md"),
        "",
        read("stage8_libero_pro_pilot_results.md"),
        "",
        "## Normal LIBERO Hard-Task Baseline",
        "",
        read("stage8_normal_libero_hard_task_results.md"),
        "",
        read("stage8_normal_libero_hard_task_baseline.md"),
        "",
        "## Flowtrace Results",
        "",
        read("stage8_flowtrace_results.md"),
        "",
        "## Target Comparison",
        "",
        read("stage8_target_comparison.md"),
        "",
        "## Model Sweep",
        "",
        read("stage8_model_sweep_results.md"),
        "",
        "## Calibration",
        "",
        read("stage8_calibration_mega_sweep.md"),
        "",
        read("stage8_calibration_best_method.md"),
        "",
        "## History Models",
        "",
        read("stage8_history_models.md"),
        "",
        "## Switch Policy",
        "",
        read("stage8_switch_policy_results.md"),
        "",
        "## Failure Analysis",
        "",
        "- Missing LIBERO-PRO init-state files block some perturbation suites; valid suites with local `.pruned_init` files should be preferred.",
        "- Deliberation must be judged by success/progress and steps, not only lower predicted uncertainty.",
        "",
        "## Final Decision",
        "",
        "Interim until the 72-hour queue completes. Current direction: keep LIBERO-PRO as the primary benchmark and use normal LIBERO only as baseline/fallback.",
        "",
        "## Artifact/report list",
        "",
        "```text",
        files.strip(),
        "```",
    ]
    OUT.write_text("\n".join(lines) + "\n")
    print(OUT)


if __name__ == "__main__":
    main()
