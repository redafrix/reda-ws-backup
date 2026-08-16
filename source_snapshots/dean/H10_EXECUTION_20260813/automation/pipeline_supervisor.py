#!/usr/bin/env python3
"""Persistent serial GPU orchestrator for seen collection, training, and locked evaluation."""

from __future__ import annotations

import json
import os
os.environ["OMNI_KIT_ACCEPT_EULA"] = "YES"
from pathlib import Path
import re
import signal
import shutil
import subprocess
import sys
import time
from typing import Any

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
AUTOMATION = WORKSPACE / "automation"
OUTPUTS = WORKSPACE / "outputs"
REPORTS = WORKSPACE / "reports/final_risk_pipeline"
LOGS = WORKSPACE / "logs"
STATE_PATH = AUTOMATION / "pipeline_state.json"
STATUS_PATH = AUTOMATION / "pipeline_live_status.json"
STOP_MARKER = AUTOMATION / "STOP_PIPELINE_AFTER_CURRENT_EPISODE"
LIMITED_FAILURE_OVERRIDE = AUTOMATION / "PROCEED_WITH_AUDITED_ROUND0_LIMITED_FAILURES"
FIRST_CYCLE_COMPLETE = AUTOMATION / "FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE"
FROZEN_DATA = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1"
MODEL_ROOT = WORKSPACE / "models/isaac_h10_topk8_temporal_v1"
OOD_OUTPUT = OUTPUTS / "final_locked_h10_ood150_seed20260728"
OOD_ARRAYS = WORKSPACE / "frozen_datasets/locked_h10_ood150_eval"
OOD_EVAL = WORKSPACE / "evaluations/locked_h10_ood150_topk8_v1"
BASE_PYTHON = Path("/home/redafrix/miniconda3/bin/python")
ISAAC_PYTHON = Path("/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python")
POLL_SECONDS = 60
DISK_FLOOR = 100 * 1024**3


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def read_json(path: Path, default: Any = None) -> Any:
    return json.loads(path.read_text()) if path.is_file() else default


def log(message: str) -> None:
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%S%z')}] {message}", flush=True)


def free_bytes() -> int:
    stat = os.statvfs("/mnt/ai")
    return stat.f_bavail * stat.f_frsize


def process_lines(pattern: str) -> list[str]:
    result = subprocess.run(
        ["pgrep", "-af", pattern], text=True, capture_output=True, check=False
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def collector_active() -> bool:
    return bool(process_lines("[c]ollect_isaac_risk.py"))


def trainer_active() -> bool:
    return bool(process_lines("[t]rain_isaac_topk8.py|[t]rain_grad_accum.py"))


def update_status(phase: str, **extra: Any) -> None:
    payload = {
        "schema_version": "simvla_isaac_risk_pipeline_status_v1",
        "phase": phase,
        "updated_at_unix_s": time.time(),
        "collector_active": collector_active(),
        "risk_trainer_active": bool(process_lines("[t]rain_isaac_topk8.py")),
        "pi05_trainer_active": bool(process_lines("[t]rain_grad_accum.py")),
        "ssd_free_bytes": free_bytes(),
        "stop_requested": STOP_MARKER.is_file(),
        **extra,
    }
    write_json(STATUS_PATH, payload)


def canonical_round_roots() -> list[Path]:
    roots = []
    for root in sorted(OUTPUTS.glob("final_seen_h10_round_*_seed*")):
        if "SUPERSEDED" in root.name or "TIMEOUT3600" in root.name:
            continue
        manifest = read_json(root / "run_manifest.json", {})
        if manifest.get("round", {}).get("enabled"):
            roots.append(root)
    return roots


def audited_summaries() -> list[dict[str, Any]]:
    summaries = []
    for root in canonical_round_roots():
        path = root / "reports/round_audit_summary.json"
        audit = root / "reports/exhaustive_audit.json"
        if not path.is_file() or not audit.is_file():
            continue
        summary = read_json(path)
        if summary.get("exhaustive_audit_pass") and read_json(audit).get("pass"):
            summaries.append(summary)
    return summaries


def aggregate_collection() -> dict[str, Any]:
    summaries = audited_summaries()
    return {
        "audited_rounds": len(summaries),
        "audited_broad_rounds": sum(
            item.get("round", {}).get("round_kind") == "broad" for item in summaries
        ),
        "episodes": sum(int(item["valid_episodes"]) for item in summaries),
        "successes": sum(int(item["successes"]) for item in summaries),
        "failures": sum(int(item["genuine_failures"]) for item in summaries),
        "rows": sum(int(item["decision_rows"]) for item in summaries),
    }


def sufficient_data(counts: dict[str, Any]) -> bool:
    if LIMITED_FAILURE_OVERRIDE.is_file():
        return (
            counts["audited_broad_rounds"] >= 1
            and counts["successes"] >= 3000
            and counts["failures"] >= 1
        )
    return (
        counts["audited_broad_rounds"] >= 1
        and counts["successes"] >= 3000
        and counts["failures"] >= 300
        and counts["failures"] >= 267
    )


def round_id_from_root(root: Path) -> int:
    match = re.match(r"final_seen_h10_round_(\d{3})_seed\d+$", root.name)
    if not match:
        raise ValueError(root)
    return int(match.group(1))


def next_round_id() -> int:
    values = [round_id_from_root(root) for root in canonical_round_roots()]
    return max(values, default=0) + 1


def seeds_for_round(round_id: int) -> tuple[int, int]:
    scene_seed = 20260801 + 2 * (round_id - 1)
    return scene_seed, scene_seed + 1


def output_for_round(round_id: int, policy_seed: int) -> Path:
    return OUTPUTS / f"final_seen_h10_round_{round_id:03d}_seed{policy_seed}"


def run_checked(
    command: list[str],
    log_path: Path,
    phase: str,
    *,
    timeout_seconds: int | None = None,
) -> None:
    if collector_active() or trainer_active():
        raise RuntimeError(f"refusing {phase}: another GPU job is active")
    update_status(phase, command=command, log=str(log_path))
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a") as handle:
        handle.write(f"\n[{time.strftime('%Y-%m-%dT%H:%M:%S%z')}] COMMAND={command!r}\n")
        handle.flush()
        process = subprocess.Popen(
            command,
            stdout=handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            return_code = process.wait(timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            handle.write(
                f"\nTIMEOUT phase={phase} timeout_seconds={timeout_seconds}; "
                "sending SIGINT to process group\n"
            )
            handle.flush()
            os.killpg(process.pid, signal.SIGINT)
            try:
                return_code = process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    return_code = process.wait(timeout=120)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    return_code = process.wait()
            raise RuntimeError(
                f"{phase} timed out after {timeout_seconds}s; "
                f"terminated rc={return_code}; log={log_path}"
            )
    if return_code:
        raise RuntimeError(f"{phase} failed rc={return_code}; log={log_path}")


def require_complete_artifact(
    root: Path, marker: str, required_files: tuple[str, ...]
) -> None:
    if not (root / marker).is_file():
        raise RuntimeError(f"missing completion marker: {root / marker}")
    missing = [name for name in required_files if not (root / name).is_file()]
    if missing:
        raise RuntimeError(f"completed artifact {root} is missing files: {missing}")
    for name in required_files:
        if name.endswith(".json"):
            payload = read_json(root / name)
            if not isinstance(payload, (dict, list)):
                raise RuntimeError(f"invalid JSON artifact: {root / name}")


def request_active_round_stop() -> None:
    for root in canonical_round_roots():
        status = read_json(root / "live_status.json", {})
        if status.get("state") in {"running", "infrastructure_error_skipped"}:
            (root / "STOP_AFTER_CURRENT_EPISODE").touch()


def monitor_process(
    process: subprocess.Popen[Any], output: Path, phase: str, command: list[str]
) -> int:
    first_commit_seen = any((output / "episodes").glob("*/COMMITTED"))
    while process.poll() is None:
        if STOP_MARKER.is_file():
            (output / "STOP_AFTER_CURRENT_EPISODE").touch()
        disk = free_bytes()
        if disk < DISK_FLOOR:
            (output / "STOP_AFTER_CURRENT_EPISODE").touch()
            update_status(
                "blocked_disk_floor_stopping_after_episode",
                active_output=str(output),
                command=command,
            )
        commits = len(list((output / "episodes").glob("*/COMMITTED")))
        if commits and not first_commit_seen:
            first_commit_seen = True
            gpu = subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw",
                    "--format=csv,noheader,nounits",
                ],
                text=True,
                capture_output=True,
                check=False,
            ).stdout.strip()
            write_json(
                REPORTS / f"round_{round_id_from_root(output):03d}_first_commit_health.json",
                {
                    "pass": True,
                    "output": str(output),
                    "committed_episodes": commits,
                    "collector_alive": True,
                    "gpu_snapshot": gpu,
                    "ssd_free_bytes": disk,
                    "checked_at_unix_s": time.time(),
                },
            )
        update_status(
            phase,
            active_output=str(output),
            committed_episodes=commits,
            live_status=read_json(output / "live_status.json", {}),
            command=command,
        )
        time.sleep(POLL_SECONDS)
    return int(process.returncode or 0)


def run_round(round_id: int, kind: str) -> None:
    scene_seed, policy_seed = seeds_for_round(round_id)
    generated = AUTOMATION / "generated" / f"round_{round_id:03d}"
    generator = (
        [
            str(ISAAC_PYTHON),
            str(AUTOMATION / "generate_official_seen_round.py"),
            "--round-id",
            str(round_id),
            "--scene-seed",
            str(scene_seed),
            "--policy-seed",
            str(policy_seed),
        ]
        if kind == "broad"
        else [
            str(BASE_PYTHON),
            str(AUTOMATION / "generate_seen_enrichment_round.py"),
            "--round-id",
            str(round_id),
            "--policy-seed",
            str(policy_seed),
        ]
    )
    generation_log = LOGS / f"round_{round_id:03d}_generation.log"
    if not (generated / "generation_report.json").is_file():
        run_checked(generator, generation_log, f"generate_{kind}_round_{round_id:03d}")
    report = read_json(generated / "generation_report.json")
    output = Path(report["output_dir"])
    command = [
        str(AUTOMATION / "run_production_round_stage.sh"),
        str(round_id),
        kind,
        str(scene_seed),
        str(policy_seed),
        str(generated),
    ]
    if (output / "reports/round_audit_summary.json").is_file():
        return
    if collector_active() or trainer_active():
        raise RuntimeError("refusing round launch while another GPU job is active")
    stage_log = LOGS / f"round_{round_id:03d}_supervisor_stage.log"
    handle = stage_log.open("a")
    handle.write(f"\nCOMMAND={command!r}\n")
    handle.flush()
    process = subprocess.Popen(command, stdout=handle, stderr=subprocess.STDOUT)
    rc = monitor_process(process, output, f"collect_{kind}_round_{round_id:03d}", command)
    handle.close()
    if rc:
        raise RuntimeError(f"round {round_id} stage failed rc={rc}; log={stage_log}")
    if not (output / "reports/round_audit_summary.json").is_file():
        live = read_json(output / "live_status.json", {})
        if live.get("state") in {
            "paused_before_episode",
            "paused_after_episode",
            "paused_after_current_episode",
        }:
            log(f"round {round_id} paused cleanly before audit: {live}")
            return
        raise RuntimeError(
            f"round {round_id} exited without a complete audited summary: {live}"
        )
    run_checked(
        [
            str(BASE_PYTHON),
            str(AUTOMATION / "compress_audited_round.py"),
            str(output),
        ],
        LOGS / f"round_{round_id:03d}_lossless_compression.log",
        f"compress_audited_round_{round_id:03d}",
    )


def ensure_round_zero_finished() -> None:
    root = OUTPUTS / "final_seen_h10_round_000_seed20260730"
    summary = root / "reports/round_audit_summary.json"
    while not summary.is_file():
        if STOP_MARKER.is_file():
            request_active_round_stop()
            update_status("stopping_round_zero_after_current_episode")
            time.sleep(POLL_SECONDS)
            if not collector_active():
                raise SystemExit(0)
            continue
        if free_bytes() < DISK_FLOOR:
            (root / "STOP_AFTER_CURRENT_EPISODE").touch()
            update_status("blocked_disk_floor_round_zero", active_output=str(root))
            time.sleep(POLL_SECONDS)
            continue
        if not collector_active():
            stage_status = read_json(root / "reports/stage_status.json", {})
            live = read_json(root / "live_status.json", {})
            tmux = subprocess.run(
                ["tmux", "has-session", "-t", "simvla-risk-h10-final-seen-r000"],
                check=False,
            )
            if live.get("state") == "complete":
                if tmux.returncode == 0:
                    update_status(
                        "round_zero_complete_waiting_for_stage_audit",
                        active_output=str(root),
                        stage_status=stage_status,
                    )
                    time.sleep(POLL_SECONDS)
                    continue
                audit_path = root / "reports/exhaustive_audit.json"
                audit = read_json(audit_path, {})
                if not audit.get("pass"):
                    run_checked(
                        [
                            str(ISAAC_PYTHON),
                            str(WORKSPACE / "scripts/audit_corrected_collection.py"),
                            str(root),
                            "--report-json",
                            str(audit_path),
                            "--expected-outcome",
                            "production_round",
                        ],
                        LOGS / "round_000_recovered_exhaustive_audit.log",
                        "recover_round_000_exhaustive_audit",
                    )
                if not summary.is_file():
                    run_checked(
                        [
                            str(ISAAC_PYTHON),
                            str(WORKSPACE / "scripts/summarize_production_round.py"),
                            str(root),
                            "--audit-json",
                            str(audit_path),
                            "--report-json",
                            str(summary),
                        ],
                        LOGS / "round_000_recovered_summary.log",
                        "recover_round_000_summary",
                    )
                continue
            if tmux.returncode != 0:
                action = "resume" if (root / "run_manifest.json").is_file() else "start"
                log(
                    f"{action} H10 Round 0; existing atomic state={live}"
                )
                subprocess.run(
                    [str(WORKSPACE / "scripts/final_seen_h10_round_000.sh"), action],
                    check=True,
                )
        update_status(
            "collect_round_000",
            active_output=str(root),
            committed_episodes=len(list((root / "episodes").glob("*/COMMITTED"))),
            live_status=read_json(root / "live_status.json", {}),
        )
        time.sleep(POLL_SECONDS)
    audit = read_json(root / "reports/exhaustive_audit.json", {})
    if not audit.get("pass"):
        raise RuntimeError("Round 0 summary exists without a passing exhaustive audit")
    if not (root / "reports/ROUND_ROWS_COMPRESSED").is_file():
        run_checked(
            [
                str(BASE_PYTHON),
                str(AUTOMATION / "compress_audited_round.py"),
                str(root),
            ],
            LOGS / "round_000_lossless_compression.log",
            "compress_audited_round_000",
        )


def train_and_evaluate_first_model() -> None:
    limited_failure_args: list[str] = []
    if LIMITED_FAILURE_OVERRIDE.is_file():
        limited_failure_args = [
            "--allow-limited-failures",
            "--minimum-total-failures",
            "1",
            "--minimum-holdout-failures",
            "10",
            "--limited-failure-override-file",
            str(LIMITED_FAILURE_OVERRIDE),
        ]
    if not (FROZEN_DATA / "FROZEN_AND_VALIDATED").is_file():
        run_checked(
            [
                str(BASE_PYTHON),
                str(WORKSPACE / "risk_head_pipeline/build_frozen_dataset.py"),
                "--output-root",
                str(FROZEN_DATA),
                "--label-contract",
                "strict_2cm",
                *limited_failure_args,
            ],
            LOGS / "build_frozen_seen_dataset.log",
            "freeze_seen_scientific_dataset",
            timeout_seconds=4 * 60 * 60,
        )
    require_complete_artifact(
        FROZEN_DATA,
        "FROZEN_AND_VALIDATED",
        ("dataset_manifest.json", "normalization.json", "split_assignments.json"),
    )
    if not (MODEL_ROOT / "TRAINING_COMPLETE").is_file():
        run_checked(
            [
                str(BASE_PYTHON),
                str(WORKSPACE / "risk_head_pipeline/train_isaac_topk8.py"),
                "--dataset-root",
                str(FROZEN_DATA),
                "--output-root",
                str(MODEL_ROOT),
                "--workers",
                "8",
            ],
            LOGS / "train_isaac_topk8.log",
            "train_topk8_on_gpu",
            timeout_seconds=4 * 60 * 60,
        )
    require_complete_artifact(
        MODEL_ROOT,
        "TRAINING_COMPLETE",
        ("model.pt", "model_manifest.json", "results.json", "thresholds.json"),
    )
    generated_ood = AUTOMATION / "generated/locked_ood150"
    if not all(
        (generated_ood / name).is_file()
        for name in ("manifest.json", "run_config.yaml", "preparation_report.json")
    ):
        run_checked(
            [str(ISAAC_PYTHON), str(AUTOMATION / "prepare_locked_ood150.py")],
            LOGS / "prepare_locked_ood150.log",
            "prepare_locked_ood150",
            timeout_seconds=30 * 60,
        )
    ood_audit_path = OOD_OUTPUT / "reports/exhaustive_audit.json"
    ood_audit = read_json(ood_audit_path, {})
    if not ood_audit.get("pass"):
        run_checked(
            [str(AUTOMATION / "run_locked_ood150_stage.sh")],
            LOGS / "locked_ood150_stage.log",
            "collect_and_audit_locked_ood150",
        )
        ood_audit = read_json(ood_audit_path, {})
    if not ood_audit.get("pass"):
        raise RuntimeError("locked OOD-150 collection lacks a passing audit")
    if not (OOD_ARRAYS / "EVAL_DATASET_COMPLETE").is_file():
        run_checked(
            [
                str(BASE_PYTHON),
                str(WORKSPACE / "risk_head_pipeline/build_locked_eval_dataset.py"),
                "--collection-root",
                str(OOD_OUTPUT),
                "--audit-json",
                str(ood_audit_path),
                "--output-root",
                str(OOD_ARRAYS),
            ],
            LOGS / "build_locked_ood150_arrays.log",
            "build_locked_ood150_eval_arrays",
            timeout_seconds=2 * 60 * 60,
        )
    require_complete_artifact(
        OOD_ARRAYS,
        "EVAL_DATASET_COMPLETE",
        ("manifest.json", "episodes.json"),
    )
    if not (OOD_EVAL / "LOCKED_OOD150_EVALUATION_COMPLETE").is_file():
        run_checked(
            [
                str(BASE_PYTHON),
                str(WORKSPACE / "risk_head_pipeline/evaluate_isaac_topk8.py"),
                "--model-root",
                str(MODEL_ROOT),
                "--seen-dataset-root",
                str(FROZEN_DATA),
                "--ood-dataset-root",
                str(OOD_ARRAYS),
                "--output-root",
                str(OOD_EVAL),
                "--workers",
                "8",
            ],
            LOGS / "evaluate_locked_ood150.log",
            "evaluate_locked_ood150_once",
            timeout_seconds=2 * 60 * 60,
        )
    require_complete_artifact(
        OOD_EVAL,
        "LOCKED_OOD150_EVALUATION_COMPLETE",
        ("results.json", "scores.npz"),
    )
    expected_reports = (
        REPORTS / "FINAL_ISAAC_RISK_DATASET_REPORT.md",
        REPORTS / "ISAAC_TOPK8_RISK_TRAINING_REPORT.md",
        REPORTS / "ISAAC_SEEN_TO_OOD150_FINAL_EVAL_REPORT.md",
    )
    if not all(path.is_file() for path in expected_reports):
        run_checked(
            [
                str(BASE_PYTHON),
                str(WORKSPACE / "risk_head_pipeline/generate_final_reports.py"),
            ],
            LOGS / "generate_final_risk_reports.log",
            "generate_final_risk_reports",
            timeout_seconds=30 * 60,
        )
    temporary = FIRST_CYCLE_COMPLETE.with_suffix(".tmp")
    temporary.write_text("complete\n")
    temporary.replace(FIRST_CYCLE_COMPLETE)


def continuous_collection() -> None:
    while not STOP_MARKER.is_file():
        if free_bytes() < DISK_FLOOR:
            update_status("continuous_collection_blocked_disk_floor")
            time.sleep(POLL_SECONDS)
            continue
        round_id = next_round_id()
        run_round(round_id, "broad")
    request_active_round_stop()


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    if STOP_MARKER.is_file() and FIRST_CYCLE_COMPLETE.is_file():
        update_status("stopped_by_marker")
        return 0
    if process_lines("[t]rain_grad_accum.py"):
        raise RuntimeError("pi0.5 training is active; risk pipeline will not compete")
    ensure_round_zero_finished()
    if not FIRST_CYCLE_COMPLETE.is_file():
        while True:
            counts = aggregate_collection()
            update_status("assess_initial_collection_gate", collection=counts)
            if sufficient_data(counts):
                break
            round_id = next_round_id()
            kind = "broad" if counts["audited_broad_rounds"] < 2 else "enrichment"
            run_round(round_id, kind)
            if STOP_MARKER.is_file():
                update_status("stopped_after_initial_collection_episode")
                return 0
        train_and_evaluate_first_model()
        # The requested finite pipeline hands the GPU to the separately
        # resumable hard-1000 orchestrator after the first locked evaluation.
        # Open-ended broad collection must not race that handoff.
        subprocess.run(
            [str(AUTOMATION / "hard1000_pipeline_tmux.sh"), "ensure"],
            check=True,
        )
        update_status(
            "first_train_and_locked_eval_complete_handed_off_to_hard1000",
            collection=aggregate_collection(),
            model_root=str(MODEL_ROOT),
            locked_ood_eval=str(OOD_EVAL),
        )
        return 0
    if FIRST_CYCLE_COMPLETE.is_file():
        subprocess.run(
            [str(AUTOMATION / "hard1000_pipeline_tmux.sh"), "ensure"],
            check=True,
        )
        update_status("first_cycle_already_complete_hard1000_handoff_ensured")
        return 0
    update_status("stopped_cleanly_without_completed_first_cycle")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BaseException as error:
        if isinstance(error, SystemExit):
            raise
        update_status("failed", error_type=type(error).__name__, error=str(error))
        log(f"FATAL {type(error).__name__}: {error}")
        raise
