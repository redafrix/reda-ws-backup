#!/usr/bin/env python3
"""Wait for cycle one, collect hard seen data, then retrain and evaluate."""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import time
from typing import Any


WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
AUTOMATION = WORKSPACE / "automation"
LOGS = WORKSPACE / "logs"
REPORTS = WORKSPACE / "reports/final_risk_pipeline_hard1000"
STATUS = AUTOMATION / "hard1000_pipeline_status.json"
LOCK = AUTOMATION / "hard1000_pipeline.lock"
STOP = AUTOMATION / "STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
FIRST_COMPLETE = AUTOMATION / "FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE"
COMPLETE = AUTOMATION / "HARD1000_COMBINED_TRAIN_AND_EVAL_COMPLETE"
MAIN_PIPELINE_STOP = AUTOMATION / "STOP_PIPELINE_AFTER_CURRENT_EPISODE"

ROUND_ID = 2
POLICY_SEED = 20260804
GENERATED = AUTOMATION / "generated/hard_round_002"
CANDIDATE_GENERATED = AUTOMATION / "generated/round_001"
HARD_OUTPUT = WORKSPACE / "outputs/final_seen_h10_round_002_seed20260804"
COMBINED_DATA = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v2_round0_hard1000"
COMBINED_MODEL = WORKSPACE / "models/isaac_h10_topk8_temporal_v2_round0_hard1000"
OOD_OUTPUT = WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728"
OOD_ARRAYS = WORKSPACE / "frozen_datasets/locked_h10_ood150_eval"
COMBINED_EVAL = WORKSPACE / "evaluations/locked_h10_ood150_topk8_v2_round0_hard1000"
OVERRIDE = AUTOMATION / "PROCEED_WITH_AUDITED_ROUND0_LIMITED_FAILURES"

BASE_PY = Path("/home/redafrix/miniconda3/bin/python")
ISAAC_PY = Path("/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python")
DISK_FLOOR = 100 * 1024**3


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def free_bytes() -> int:
    stat = os.statvfs("/mnt/ai")
    return stat.f_bavail * stat.f_frsize


def process_lines(pattern: str) -> list[str]:
    result = subprocess.run(
        ["pgrep", "-af", pattern], text=True, capture_output=True, check=False
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def update(phase: str, **extra: Any) -> None:
    write_json(
        STATUS,
        {
            "schema_version": "simvla_hard1000_pipeline_status_v1",
            "phase": phase,
            "updated_at_unix_s": time.time(),
            "ssd_free_bytes": free_bytes(),
            "first_cycle_complete": FIRST_COMPLETE.is_file(),
            "hard_round_committed": len(list((HARD_OUTPUT / "episodes").glob("*/COMMITTED"))),
            "stop_requested": STOP.is_file(),
            **extra,
        },
    )


def run_checked(
    command: list[str],
    log_name: str,
    phase: str,
    *,
    timeout_seconds: int | None = None,
    gpu_exclusive: bool = False,
) -> None:
    if free_bytes() < DISK_FLOOR:
        raise RuntimeError("SSD free space is below the 100 GiB safety floor")
    if gpu_exclusive and process_lines(
        "[c]ollect_isaac_risk.py|[t]rain_isaac_topk8.py|[t]rain_grad_accum.py"
    ):
        raise RuntimeError(f"refusing {phase}: another GPU job is active")
    update(phase, command=command, log=str(LOGS / log_name))
    path = LOGS / log_name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
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
                f"terminated rc={return_code}; log={path}"
            )
    if return_code:
        raise RuntimeError(f"{phase} failed rc={return_code}; log={path}")


def read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text())
    if not isinstance(payload, dict):
        raise RuntimeError(f"expected JSON object: {path}")
    return payload


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
            read_json(root / name)


def archive_round_audit_for_retry(attempt: int) -> None:
    reports = HARD_OUTPUT / "reports"
    archive = reports / "infrastructure_retry_evidence" / f"attempt_{attempt:02d}"
    archive.mkdir(parents=True, exist_ok=True)
    for name in (
        "exhaustive_audit.json",
        "exhaustive_audit.log",
        "round_audit_summary.json",
        "round_summary.log",
        "stage_status.json",
    ):
        source = reports / name
        if source.is_file():
            shutil.copy2(source, archive / name)


def hard_round_completion_state(summary_path: Path, audit_path: Path) -> str:
    if not summary_path.is_file() or not audit_path.is_file():
        return "missing"
    summary = read_json(summary_path)
    audit = read_json(audit_path)
    if (
        audit.get("pass")
        and summary.get("exhaustive_audit_pass")
        and int(summary.get("valid_episodes", 0)) == 1000
    ):
        return "complete"
    if int(summary.get("infrastructure_excluded_episodes", 0)) > 0:
        return "recoverable_infrastructure_exclusion"
    return "invalid"


def wait_for_first_cycle() -> None:
    while not FIRST_COMPLETE.is_file():
        original = json.loads((AUTOMATION / "pipeline_live_status.json").read_text())
        if original.get("phase") == "failed":
            update("waiting_for_first_pipeline_systemd_recovery", original_pipeline=original)
            time.sleep(60)
            continue
        update("waiting_for_first_train_and_locked_ood_eval", original_pipeline=original)
        time.sleep(5)
    # The first supervisor historically entered open-ended broad collection as
    # soon as its first model/evaluation completed. The requested H10 pipeline
    # instead hands the GPU to the fixed hard-1000 stage at this boundary.
    MAIN_PIPELINE_STOP.touch()
    while process_lines("[c]ollect_isaac_risk.py|[t]rain_isaac_topk8.py"):
        update("waiting_for_first_cycle_gpu_processes_to_exit")
        time.sleep(30)
    first_audit = OOD_OUTPUT / "reports/exhaustive_audit.json"
    first_eval = WORKSPACE / "evaluations/locked_h10_ood150_topk8_v1/LOCKED_OOD150_EVALUATION_COMPLETE"
    if not first_audit.is_file() or not json.loads(first_audit.read_text()).get("pass"):
        raise RuntimeError("first locked OOD-150 collection lacks a passing exhaustive audit")
    if not first_eval.is_file():
        raise RuntimeError("first locked OOD-150 evaluation is incomplete")


def ensure_hard_candidate_pool() -> None:
    required = (
        CANDIDATE_GENERATED / "manifest.json",
        CANDIDATE_GENERATED / "run_config.yaml",
        CANDIDATE_GENERATED / "generation_report.json",
    )
    if not all(path.is_file() for path in required):
        run_checked(
            [
                str(ISAAC_PY),
                str(AUTOMATION / "generate_official_seen_round.py"),
                "--round-id",
                "1",
                "--scene-seed",
                "20260801",
                "--policy-seed",
                "20260802",
                "--episodes",
                "4000",
            ],
            "hard1000_candidate_pool_generation.log",
            "generate_official_h10_hard_candidate_pool",
            timeout_seconds=60 * 60,
        )
    report = read_json(CANDIDATE_GENERATED / "generation_report.json")
    manifest = read_json(CANDIDATE_GENERATED / "manifest.json")
    if int(report.get("episode_count", 0)) != 4000:
        raise RuntimeError("hard candidate pool does not contain 4000 scenes")
    if not report.get("official_seen_sampler"):
        raise RuntimeError("hard candidate pool was not made by the official seen sampler")
    if int(report.get("source_fingerprint_overlap", -1)) != 0:
        raise RuntimeError("hard candidate pool overlaps the H10 Round-0 source scenes")
    if len(manifest.get("episodes", [])) != 4000:
        raise RuntimeError("hard candidate manifest episode count mismatch")


def validate_hard_manifest() -> None:
    manifest = json.loads((GENERATED / "manifest.json").read_text())
    report = json.loads((GENERATED / "generation_report.json").read_text())
    if len(manifest["episodes"]) != 1000:
        raise RuntimeError("hard manifest does not contain exactly 1000 episodes")
    fingerprints = [str(item["scene_fingerprint_sha256"]) for item in manifest["episodes"]]
    if len(set(fingerprints)) != 1000:
        raise RuntimeError("hard manifest contains duplicate scene fingerprints")
    required_zero = (
        "selected_scene_fingerprint_overlap_with_ood150",
        "selected_asset_variant_overlap_with_ood150",
        "selected_scene_fingerprint_overlap_with_committed_data",
    )
    if any(int(report[name]) != 0 for name in required_zero):
        raise RuntimeError("hard manifest failed OOD or prior-data overlap checks")
    provenance = manifest.get("provenance", {})
    source_manifest_value = provenance.get("source_manifest")
    source_manifest_sha256 = provenance.get("source_manifest_sha256")
    if not source_manifest_value or not source_manifest_sha256:
        raise RuntimeError("hard manifest is missing direct source-manifest provenance")
    source_manifest = Path(str(source_manifest_value)).resolve()
    if not source_manifest.is_file():
        raise RuntimeError(f"hard manifest source does not exist: {source_manifest}")
    if sha256_file(source_manifest) != str(source_manifest_sha256):
        raise RuntimeError("hard manifest source SHA-256 does not match the source file")
    config = (GENERATED / "run_config.yaml").read_text()
    required = (
        "max_steps: 2400",
        "success_threshold_m: 0.02",
        "settle_time_s: 0.2",
        "control_fps: 30",
        "save_training_rgb_arrays: false",
        "save_rgb_videos: false",
    )
    if any(value not in config for value in required):
        raise RuntimeError("hard run config changed a required scientific setting")


def ensure_hard_round() -> None:
    run_checked(
        [
            "/usr/bin/env",
            f"PYTHONPATH={WORKSPACE}:{WORKSPACE / 'src'}",
            "PYTHONDONTWRITEBYTECODE=1",
            str(ISAAC_PY),
            "-m",
            "pytest",
            "-p",
            "no:cacheprovider",
            "-q",
            str(WORKSPACE / "tests"),
        ],
        "hard1000_preflight_tests.log",
        "hard1000_cpu_regression_tests",
        timeout_seconds=20 * 60,
    )
    ensure_hard_candidate_pool()
    run_checked(
        [
            str(BASE_PY),
            str(AUTOMATION / "generate_hard_seen_round.py"),
            "--round-id",
            str(ROUND_ID),
            "--policy-seed",
            str(POLICY_SEED),
            "--episodes",
            "1000",
        ],
        "hard1000_generation.log",
        "generate_hard1000_manifest",
        timeout_seconds=30 * 60,
    )
    validate_hard_manifest()
    summary = HARD_OUTPUT / "reports/round_audit_summary.json"
    audit_path = HARD_OUTPUT / "reports/exhaustive_audit.json"
    for recovery_attempt in range(1, 4):
        completion_state = hard_round_completion_state(summary, audit_path)
        if completion_state == "complete":
            break
        if completion_state == "invalid":
            raise RuntimeError(
                "hard round summary is invalid without a recoverable infrastructure "
                f"exclusion: {read_json(summary)}"
            )
        if completion_state == "recoverable_infrastructure_exclusion":
            archive_round_audit_for_retry(recovery_attempt)
        command = [
            str(AUTOMATION / "run_production_round_stage.sh"),
            str(ROUND_ID),
            "enrichment",
            "20260803",
            str(POLICY_SEED),
            str(GENERATED),
        ]
        if STOP.is_file():
            (HARD_OUTPUT / "STOP_AFTER_CURRENT_EPISODE").touch()
        run_checked(
            command,
            "hard1000_collection_stage.log",
            "collect_and_audit_hard1000",
            gpu_exclusive=True,
        )
        live_path = HARD_OUTPUT / "live_status.json"
        live = read_json(live_path) if live_path.is_file() else {}
        if live.get("state") in {"paused_before_episode", "paused_after_current_episode"}:
            update("hard1000_paused_cleanly", live_status=live)
            raise SystemExit(0)
    else:
        raise RuntimeError("hard round still lacks 1000 valid episodes after 3 recovery passes")
    if not summary.is_file():
        live = json.loads((HARD_OUTPUT / "live_status.json").read_text())
        if live.get("state") in {"paused_before_episode", "paused_after_current_episode"}:
            update("hard1000_paused_cleanly", live_status=live)
            raise SystemExit(0)
        raise RuntimeError(f"hard round exited without audited summary: {live}")
    round_summary = read_json(summary)
    audit = read_json(HARD_OUTPUT / "reports/exhaustive_audit.json")
    if not audit.get("pass") or not round_summary.get("exhaustive_audit_pass"):
        raise RuntimeError("hard round did not pass exhaustive row parity audit")
    if int(round_summary["valid_episodes"]) != 1000:
        raise RuntimeError(
            "hard round has infrastructure exclusions; exactly 1000 valid episodes are required"
        )
    marker = HARD_OUTPUT / "reports/ROUND_ROWS_COMPRESSED"
    if not marker.is_file():
        run_checked(
            [str(BASE_PY), str(AUTOMATION / "compress_audited_round.py"), str(HARD_OUTPUT)],
            "hard1000_lossless_compression.log",
            "compress_audited_hard1000",
            timeout_seconds=4 * 60 * 60,
        )


def build_train_evaluate_combined() -> None:
    if not (COMBINED_DATA / "FROZEN_AND_VALIDATED").is_file():
        if COMBINED_DATA.exists():
            quarantine = COMBINED_DATA.with_name(
                f"{COMBINED_DATA.name}.incomplete-{int(time.time())}"
            )
            COMBINED_DATA.replace(quarantine)
        run_checked(
            [
                str(BASE_PY),
                str(WORKSPACE / "risk_head_pipeline/build_frozen_dataset.py"),
                "--output-root",
                str(COMBINED_DATA),
                "--label-contract",
                "strict_2cm",
                "--allow-limited-failures",
                "--minimum-total-failures",
                "1",
                "--minimum-holdout-failures",
                "10",
                "--limited-failure-override-file",
                str(OVERRIDE),
            ],
            "build_combined_5000_dataset.log",
            "freeze_combined_5000_dataset",
            timeout_seconds=4 * 60 * 60,
        )
    require_complete_artifact(
        COMBINED_DATA,
        "FROZEN_AND_VALIDATED",
        ("dataset_manifest.json", "normalization.json", "split_assignments.json"),
    )
    manifest = read_json(COMBINED_DATA / "dataset_manifest.json")
    episodes = sum(int(value["episodes"]) for value in manifest["splits"].values())
    if episodes != 5000:
        raise RuntimeError(f"combined frozen dataset has {episodes} episodes, expected 5000")
    if len(manifest["source_rounds"]) != 2:
        raise RuntimeError("combined dataset must contain exactly Round 0 and hard Round 2")

    if not (COMBINED_MODEL / "TRAINING_COMPLETE").is_file():
        run_checked(
            [
                str(BASE_PY),
                str(WORKSPACE / "risk_head_pipeline/train_isaac_topk8.py"),
                "--dataset-root",
                str(COMBINED_DATA),
                "--output-root",
                str(COMBINED_MODEL),
                "--workers",
                "8",
            ],
            "train_combined_5000_topk8.log",
            "train_combined_5000_topk8",
            timeout_seconds=4 * 60 * 60,
            gpu_exclusive=True,
        )
    require_complete_artifact(
        COMBINED_MODEL,
        "TRAINING_COMPLETE",
        ("model.pt", "model_manifest.json", "results.json", "thresholds.json"),
    )
    if not (OOD_ARRAYS / "EVAL_DATASET_COMPLETE").is_file():
        raise RuntimeError("first cycle did not leave finalized locked OOD arrays")
    if not (COMBINED_EVAL / "LOCKED_OOD150_EVALUATION_COMPLETE").is_file():
        run_checked(
            [
                str(BASE_PY),
                str(WORKSPACE / "risk_head_pipeline/evaluate_isaac_topk8.py"),
                "--model-root",
                str(COMBINED_MODEL),
                "--seen-dataset-root",
                str(COMBINED_DATA),
                "--ood-dataset-root",
                str(OOD_ARRAYS),
                "--output-root",
                str(COMBINED_EVAL),
                "--workers",
                "8",
            ],
            "evaluate_combined_5000_locked_ood150.log",
            "evaluate_combined_5000_locked_ood150",
            timeout_seconds=2 * 60 * 60,
            gpu_exclusive=True,
        )
    require_complete_artifact(
        COMBINED_EVAL,
        "LOCKED_OOD150_EVALUATION_COMPLETE",
        ("results.json", "scores.npz"),
    )
    expected_reports = (
        REPORTS / "FINAL_ISAAC_RISK_DATASET_REPORT_ROUND0_HARD1000.md",
        REPORTS / "ISAAC_TOPK8_RISK_TRAINING_REPORT_ROUND0_HARD1000.md",
        REPORTS / "ISAAC_SEEN_TO_OOD150_FINAL_EVAL_REPORT_ROUND0_HARD1000.md",
    )
    if not all(path.is_file() for path in expected_reports):
        run_checked(
            [
                str(BASE_PY),
                str(WORKSPACE / "risk_head_pipeline/generate_final_reports.py"),
                "--dataset-root",
                str(COMBINED_DATA),
                "--model-root",
                str(COMBINED_MODEL),
                "--evaluation-root",
                str(COMBINED_EVAL),
                "--report-root",
                str(REPORTS),
                "--report-suffix",
                "_ROUND0_HARD1000",
            ],
            "generate_combined_5000_reports.log",
            "generate_combined_5000_reports",
            timeout_seconds=30 * 60,
        )


def finalize() -> None:
    hard_summary = json.loads(
        (HARD_OUTPUT / "reports/round_audit_summary.json").read_text()
    )
    dataset = json.loads((COMBINED_DATA / "dataset_manifest.json").read_text())
    model = json.loads((COMBINED_MODEL / "results.json").read_text())
    evaluation = json.loads((COMBINED_EVAL / "results.json").read_text())
    summary = {
        "schema_version": "simvla_hard1000_combined_pipeline_result_v1",
        "hard_round": {
            "episodes": hard_summary["valid_episodes"],
            "successes": hard_summary["successes"],
            "failures": hard_summary["genuine_failures"],
            "audit_sha256": sha256_file(HARD_OUTPUT / "reports/exhaustive_audit.json"),
        },
        "combined_dataset": {
            "path": str(COMBINED_DATA),
            "manifest_sha256": sha256_file(COMBINED_DATA / "dataset_manifest.json"),
            "episodes": sum(int(value["episodes"]) for value in dataset["splits"].values()),
            "split_contract": dataset["split_contract"],
        },
        "combined_model": {
            "path": str(COMBINED_MODEL / "model.pt"),
            "sha256": sha256_file(COMBINED_MODEL / "model.pt"),
            "best_epoch": model["best_epoch"],
            "best_validation_auprc": model["best_validation_auprc"],
        },
        "locked_ood150": {
            "evaluation_path": str(COMBINED_EVAL),
            "results_sha256": sha256_file(COMBINED_EVAL / "results.json"),
            "step_auroc": evaluation["step_auroc"],
            "step_auprc": evaluation["step_auprc"],
            "used_for_training_or_selection": False,
        },
        "ood_scene_or_asset_overlap": 0,
        "complete": True,
    }
    write_json(REPORTS / "HARD1000_COMBINED_PIPELINE_RESULT.json", summary)
    COMPLETE.write_text("complete\n")
    update("complete", result=summary)


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOCK.open("w") as lock_handle:
        try:
            fcntl.flock(lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("another hard1000 orchestrator holds the lock") from error
        if COMPLETE.is_file():
            update("complete_already")
            return 0
        wait_for_first_cycle()
        ensure_hard_round()
        build_train_evaluate_combined()
        finalize()
    return 0


LOG = LOGS / "hard1000_pipeline.log"


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BaseException as error:
        if isinstance(error, SystemExit):
            raise
        update("failed", error_type=type(error).__name__, error=str(error))
        print(f"FATAL {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise
