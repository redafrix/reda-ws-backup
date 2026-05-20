from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path


FINAL_REPORT = "STAGE9_FINAL_20H_COLLECTION_AND_TRAINING_REPORT.md"
LIVE_DASHBOARD = "STAGE9_20H_LIVE_DASHBOARD.md"


BOB_TASKS = [
    ("libero_spatial_with_mug", list(range(10))),
    ("libero_object_with_mug", list(range(10))),
    ("libero_goal_with_mug", list(range(10))),
    ("libero_10_with_mug", list(range(10))),
]

SAM_TASKS = [
    ("libero_spatial_with_red_box", list(range(10))),
    ("libero_object_with_red_box", list(range(10))),
    ("libero_object_with_blue_stick", list(range(10))),
    ("libero_goal_with_red_box", list(range(10))),
    ("libero_object_temp_x0.1", list(range(10))),
    ("libero_object_temp_x0.3", list(range(10))),
]


def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def sample_label(row):
    label = row.get("label")
    if isinstance(label, dict):
        return label.get("label") or label.get("final_label")
    return label


def rows_from_root(root: Path):
    for file in sorted((root / "chunks").glob("*/counterfactual_samples.jsonl")):
        try:
            with file.open() as f:
                for line in f:
                    if line.strip():
                        yield json.loads(line)
        except Exception:
            continue


def summarize(root: Path) -> dict:
    labels = Counter()
    raw_labels = Counter()
    subtypes = Counter()
    reasons = Counter()
    tasks = Counter()
    phases = Counter()
    trace_bad = 0
    same_missing = 0
    evidence_missing = 0
    suspicious = 0
    total = 0
    states = set()
    for row in rows_from_root(root):
        total += 1
        label = sample_label(row)
        labels[label] += 1
        raw_labels[(row.get("raw_local_label") or {}).get("label")] += 1
        meta = row.get("metadata") or {}
        tasks[meta.get("task_name") or "unknown"] += 1
        phases[meta.get("parent_phase") or "unknown"] += 1
        states.add(meta.get("state_id") or row.get("sample_id"))
        label_obj = row.get("label") or {}
        if label == "VALIDATED_BAD":
            subtypes[label_obj.get("bad_subtype") or "unknown"] += 1
            for reason in label_obj.get("validated_bad_reasons") or label_obj.get("label_reasons") or []:
                reasons[reason] += 1
        trace = (row.get("outcome") or {}).get("horizon_trace") or {}
        trace_len = len(trace.get("rewards") or [])
        terminal_ok = bool((row.get("outcome") or {}).get("terminal_success") or (row.get("outcome") or {}).get("done_within_H"))
        if trace_len < 40 and not terminal_ok:
            trace_bad += 1
        if not label_obj.get("same_state_comparison"):
            same_missing += 1
        if not label_obj.get("label_evidence"):
            evidence_missing += 1
    validation_dir = root.parent.parent / "validation"
    for analysis in validation_dir.glob(f"{root.name}_*_analysis.json"):
        try:
            suspicious += int(json.loads(analysis.read_text()).get("suspicious_count", 0))
        except Exception:
            pass
    usage = shutil.disk_usage(root)
    return {
        "total_samples": total,
        "total_states": len(states),
        "label_counts": dict(labels),
        "raw_label_counts": dict(raw_labels),
        "bad_subtype_counts": dict(subtypes),
        "bad_reason_counts": dict(reasons),
        "task_counts": dict(tasks),
        "phase_counts": dict(phases),
        "trace_incomplete_count": trace_bad,
        "same_state_missing_count": same_missing,
        "label_evidence_missing_count": evidence_missing,
        "suspicious_count": suspicious,
        "disk_free_gb": round(usage.free / (1024 ** 3), 2),
    }


def write_dashboard(path: Path, role: str, status: str, root: Path, started: float, errors: list[str], active: dict | None = None) -> None:
    summary = summarize(root)
    elapsed = time.time() - started
    lines = [
        "# Stage 9 20h Live Dashboard",
        "",
        f"Updated: `{now()}`",
        f"Host: `{socket.gethostname()}`",
        f"Role: `{role}`",
        f"Status: `{status}`",
        f"Elapsed hours: `{elapsed / 3600:.2f}`",
        f"Dataset root: `{root}`",
        "",
        "## Counts",
        "",
        f"- total_samples: `{summary['total_samples']}`",
        f"- total_states: `{summary['total_states']}`",
        f"- label_counts: `{json.dumps(summary['label_counts'], sort_keys=True)}`",
        f"- bad_subtype_counts: `{json.dumps(summary['bad_subtype_counts'], sort_keys=True)}`",
        f"- bad_reason_counts: `{json.dumps(summary['bad_reason_counts'], sort_keys=True)}`",
        f"- suspicious_count: `{summary['suspicious_count']}`",
        f"- trace_incomplete_count: `{summary['trace_incomplete_count']}`",
        f"- same_state_missing_count: `{summary['same_state_missing_count']}`",
        f"- label_evidence_missing_count: `{summary['label_evidence_missing_count']}`",
        f"- disk_free_gb: `{summary['disk_free_gb']}`",
        "",
        "## Task/Phase",
        "",
        f"- task_counts: `{json.dumps(summary['task_counts'], sort_keys=True)[:3000]}`",
        f"- phase_counts: `{json.dumps(summary['phase_counts'], sort_keys=True)}`",
    ]
    if active:
        lines.extend(["", "## Active Chunk", "", "```json", json.dumps(active, indent=2, sort_keys=True), "```"])
    if errors:
        lines.extend(["", "## Errors", ""])
        lines.extend([f"- {e}" for e in errors[-30:]])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def append_report(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text.rstrip() + "\n\n")


def run_analyzer(workspace: Path, chunk_dir: Path, validation_dir: Path, log_path: Path) -> int:
    cmd = [
        sys.executable,
        str(workspace / "asynchvla_ws/src/data_collection_stage9/analyze_outcome_pilot.py"),
        str(chunk_dir),
        str(validation_dir),
        str(workspace),
    ]
    with log_path.open("a") as log:
        return subprocess.run(cmd, stdout=log, stderr=log).returncode


def chunk_queue(role: str):
    tasks = BOB_TASKS if role == "bob" else SAM_TASKS
    cycle = 0
    while True:
        seeds = list(range(cycle * 8, cycle * 8 + 8))
        for suite, task_ids in tasks:
            for task_id in task_ids:
                yield cycle, suite, task_id, seeds
        cycle += 1


def maybe_launch_training(args, root: Path, report: Path, logs_dir: Path, started_training: bool) -> bool:
    if started_training or not args.enable_training:
        return started_training
    summary = summarize(root)
    valid = int(summary["label_counts"].get("GOOD_STRONG", 0)) + int(summary["label_counts"].get("VALIDATED_BAD", 0))
    if valid < args.min_train_samples:
        return False
    train_dir = root.parent.parent / "training" / f"{root.name}_{args.role}_{time.strftime('%Y%m%d_%H%M%S')}"
    cmd = [
        "nohup",
        sys.executable,
        "-u",
        "-m",
        "data_collection_stage9.train_stage9_risk_baselines",
        "--data",
        str(root),
        "--out-dir",
        str(train_dir),
        "--epochs",
        "12",
        "--min-samples",
        str(args.min_train_samples),
    ]
    log_path = logs_dir / "training_baselines.log"
    with log_path.open("ab") as log:
        subprocess.Popen(cmd, stdout=log, stderr=log, cwd=str(args.workspace), env=os.environ.copy())
    append_report(report, f"## Training Launched\n\nStarted `{now()}` on `{args.role}` using `{root}`.\n\nLog: `{log_path}`\n\nOutput: `{train_dir}`")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=["bob", "sam"], required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--duration-hours", type=float, default=20.0)
    parser.add_argument("--max-total-states", type=int, default=32)
    parser.add_argument("--max-parent-episodes", type=int, default=12)
    parser.add_argument("--max-states-per-parent", type=int, default=4)
    parser.add_argument("--parent-roll-steps", type=int, default=160)
    parser.add_argument("--terminal-horizon", type=int, default=120)
    parser.add_argument("--save-trace-frames", action="store_true")
    parser.add_argument("--enable-training", action="store_true")
    parser.add_argument("--min-train-samples", type=int, default=5000)
    args = parser.parse_args()

    stage_root = args.workspace / "asynchvla_ws/stage9_libero_pro_risk_data"
    run_root = stage_root / "data/final_20h" / f"{args.role}_{time.strftime('%Y%m%d_%H%M%S')}"
    chunks_dir = run_root / "chunks"
    logs_dir = stage_root / "logs" / run_root.name
    reports_dir = stage_root / "reports"
    validation_dir = stage_root / "validation"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    report = reports_dir / FINAL_REPORT
    dashboard = reports_dir / LIVE_DASHBOARD
    started = time.time()
    stop_at = started + args.duration_hours * 3600
    errors: list[str] = []
    retry_count = Counter()
    started_training = False

    append_report(report, f"## Watchdog Started: {args.role}\n\nStarted `{now()}` on `{socket.gethostname()}`.\n\nDataset root: `{run_root}`\n")
    write_dashboard(dashboard, args.role, "starting", run_root, started, errors)

    for cycle, suite, task_id, seeds in chunk_queue(args.role):
        if time.time() >= stop_at:
            break
        task_key = f"{suite}_t{task_id}_cycle{cycle}"
        if retry_count[task_key] > 1:
            continue
        chunk_name = f"{args.role}_c{cycle:03d}_{suite}_t{task_id}_seeds{seeds[0]}-{seeds[-1]}"
        chunk_dir = chunks_dir / chunk_name
        chunk_log = logs_dir / f"{chunk_name}.log"
        active = {"chunk": chunk_name, "suite": suite, "task_id": task_id, "seeds": seeds}
        cmd = [
            sys.executable,
            "-u",
            "-m",
            "data_collection_stage9.collect_outcome_advantage_dataset",
            "--suites",
            suite,
            "--task-ids",
            str(task_id),
            "--max-total-states",
            str(args.max_total_states),
            "--max-parent-episodes",
            str(args.max_parent_episodes),
            "--max-states-per-parent",
            str(args.max_states_per_parent),
            "--parent-roll-steps",
            str(args.parent_roll_steps),
            "--risk-window",
            "12",
            "--pre-failure-distances",
            "40",
            "24",
            "12",
            "1",
            "--simvla-seeds",
            *[str(x) for x in seeds],
            "--eval-horizon",
            "40",
            "--terminal-horizon",
            str(args.terminal_horizon),
            "--history-k",
            "8",
            "--out-dir",
            str(chunk_dir),
            "--save-images",
        ]
        if args.save_trace_frames:
            cmd.extend(["--save-trace-frames", "--trace-frame-stride", "20"])
        write_dashboard(dashboard, args.role, "collecting", run_root, started, errors, active)
        with chunk_log.open("ab") as log:
            proc = subprocess.Popen(cmd, stdout=log, stderr=log, cwd=str(args.workspace), env=os.environ.copy())
            while proc.poll() is None:
                time.sleep(60)
                write_dashboard(dashboard, args.role, "collecting", run_root, started, errors, active)
                started_training = maybe_launch_training(args, run_root, report, logs_dir, started_training)
                if time.time() >= stop_at:
                    break
            rc = proc.poll()
            if rc is None:
                proc.terminate()
                try:
                    proc.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    proc.kill()
                break
        if rc != 0:
            retry_count[task_key] += 1
            msg = f"{now()} chunk failed rc={rc}: {chunk_name}; retry={retry_count[task_key]}"
            errors.append(msg)
            append_report(report, f"## Chunk Failure\n\n{msg}\n\nLog: `{chunk_log}`")
            if retry_count[task_key] <= 1:
                continue
            continue
        analysis_log = logs_dir / f"{chunk_name}_analysis.log"
        analysis_rc = run_analyzer(args.workspace, chunk_dir, validation_dir, analysis_log)
        if analysis_rc != 0:
            msg = f"{now()} analysis failed rc={analysis_rc}: {chunk_name}"
            errors.append(msg)
            append_report(report, f"## Analysis Failure\n\n{msg}\n\nLog: `{analysis_log}`")
        else:
            append_report(report, f"## Chunk Complete\n\nCompleted `{chunk_name}` at `{now()}`.\n\nChunk path: `{chunk_dir}`\n\nLog: `{chunk_log}`\n\nAnalysis log: `{analysis_log}`")
        write_dashboard(dashboard, args.role, "between_chunks", run_root, started, errors)
        started_training = maybe_launch_training(args, run_root, report, logs_dir, started_training)

    write_dashboard(dashboard, args.role, "finished", run_root, started, errors)
    final_summary = summarize(run_root)
    (run_root / "watchdog_summary.json").write_text(json.dumps(final_summary, indent=2, sort_keys=True) + "\n")
    append_report(report, f"## Watchdog Finished: {args.role}\n\nFinished `{now()}`.\n\nFinal local summary:\n\n```json\n{json.dumps(final_summary, indent=2, sort_keys=True)}\n```\n")


if __name__ == "__main__":
    main()
