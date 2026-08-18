#!/usr/bin/env python3
"""End-to-end resumable state-machine orchestrator for Isaac Online OOD150 Engineering Controller (A=0.799012, C=0.900, M=0.0)."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import traceback
from typing import Any

import numpy as np

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
PROTOCOL_DIR = WORKSPACE / "online_evals/isaac_ood150_engineering_cap090_v1"
RUNS_DIR = PROTOCOL_DIR / "runs"
DEFINITIVE_RUN_DIR = RUNS_DIR / "definitive_full150"
SHADOW_GATE_DIR = RUNS_DIR / "shadow_gate"
HARD1000_DIR = WORKSPACE / "outputs/final_seen_h10_round_002_seed20260804"
GIT_REPO_DIR = Path("/home/redafrix/tests/internship")
GIT_EXPERIMENT_SUBDIR = GIT_REPO_DIR / "prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1"
GIT_BRANCH = "experiment/dean-isaac-online-ood150-20260817"

MODEL_PATH = WORKSPACE / "models/isaac_h10_topk8_temporal_v1/model.pt"
NORM_PATH = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json"
OOD_MANIFEST = WORKSPACE / "automation/generated/locked_ood150/manifest.json"
RUN_CONFIG = WORKSPACE / "automation/generated/locked_ood150/run_config.yaml"
HISTORICAL_OOD150_SUMMARIES = WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728/episode_summaries.jsonl"

EXPECTED_MODEL_SHA = "ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38"
EXPECTED_NORM_SHA = "78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050"

FROZEN_A = 0.7990124225616455
FROZEN_C = 0.9000000000000000
FROZEN_M = 0.0

STATE_FILE = PROTOCOL_DIR / "ORCHESTRATOR_STATE.json"
EVENTS_FILE = PROTOCOL_DIR / "ORCHESTRATOR_EVENTS.jsonl"
CONTROLLER_FILE = PROTOCOL_DIR / "SELECTED_ENGINEERING_CONTROLLER.json"

ISAAC_PYTHON = "/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python"
MINICONDA_PYTHON = "/home/redafrix/miniconda3/bin/python"


def sha256_f(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def log_event(event_type: str, data: dict[str, Any]) -> None:
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "data": data,
    }
    print(f"[{payload['timestamp']}] [{event_type}] {json.dumps(data)}")
    with open(EVENTS_FILE, "a") as f:
        f.write(json.dumps(payload) + "\n")


def load_state() -> dict[str, Any]:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {
        "schema_version": "isaac_online_orchestrator_state_v1",
        "current_stage": "STAGE_0_PREFLIGHT",
        "status": "INITIALIZED",
        "definitive_pid": None,
        "health_gate_passed": False,
        "completed_episodes_count": 0,
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }


def save_state(state: dict[str, Any]) -> None:
    state["last_updated"] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2))


def check_active_processes(patterns: list[str]) -> list[tuple[int, str]]:
    matches = []
    my_pid = os.getpid()
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        if pid == my_pid:
            continue
        try:
            cmd = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode().strip()
            if any(p in cmd for p in patterns):
                matches.append((pid, cmd))
        except (OSError, UnicodeDecodeError):
            continue
    return matches


def is_pid_alive(pid: int | None, expected_pattern: str = "") -> bool:
    if pid is None or pid <= 0:
        return False
    proc_path = Path(f"/proc/{pid}")
    if not proc_path.exists():
        return False
    if not expected_pattern:
        return True
    try:
        cmd = (proc_path / "cmdline").read_bytes().replace(b"\0", b" ").decode().strip()
        return expected_pattern in cmd
    except (OSError, UnicodeDecodeError):
        return False


def get_committed_summaries(run_dir: Path) -> list[dict[str, Any]]:
    summaries_file = run_dir / "episode_summaries.jsonl"
    if not summaries_file.exists():
        return []
    return [json.loads(line) for line in summaries_file.read_text().splitlines() if line.strip()]


def build_definitive_command() -> list[str]:
    runner_script = PROTOCOL_DIR / "run_isaac_online_risk.py"
    return [
        ISAAC_PYTHON,
        str(runner_script),
        "--run-config", str(RUN_CONFIG),
        "--manifest", str(OOD_MANIFEST),
        "--output-dir", str(DEFINITIVE_RUN_DIR),
        "--risk-model-root", str(WORKSPACE / "models/isaac_h10_topk8_temporal_v1"),
        "--risk-normalization", str(NORM_PATH),
        "--controller-config", str(CONTROLLER_FILE),
        "--online-mode", "active",
        "--online-role", "full150",
        "--protocol-id", "isaac_ood150_definitive_active_cap090_v1",
        "--execution-mode", "chunk_h10",
        "--offset", "0",
        "--count", "150",
        "--headless",
    ]


# ==============================================================================
# STAGE 0: PREFLIGHT
# ==============================================================================
def run_stage_0_preflight() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_0_PREFLIGHT"})

    active_isaac = check_active_processes(["run_isaac_online_risk.py", "simvla_reaching_rollout.py"])
    if active_isaac:
        raise RuntimeError(f"Active Isaac rollout processes detected: {active_isaac}")

    hard_status_p = HARD1000_DIR / "live_status.json"
    if not hard_status_p.exists():
        raise RuntimeError(f"HARD1000 live_status.json not found at {hard_status_p}")
    hard_status = json.loads(hard_status_p.read_text())
    if hard_status.get("completed_episodes") != 249:
        raise RuntimeError(f"HARD1000 completed_episodes is {hard_status.get('completed_episodes')}, expected 249")
    if hard_status.get("active_collector_pid") is not None:
        raise RuntimeError(f"HARD1000 has active collector PID: {hard_status.get('active_collector_pid')}")
    if hard_status.get("active_pipeline_pid") is not None:
        raise RuntimeError(f"HARD1000 has active pipeline PID: {hard_status.get('active_pipeline_pid')}")

    model_sha = sha256_f(MODEL_PATH)
    norm_sha = sha256_f(NORM_PATH)
    if model_sha != EXPECTED_MODEL_SHA:
        raise RuntimeError(f"Model SHA mismatch: {model_sha} != {EXPECTED_MODEL_SHA}")
    if norm_sha != EXPECTED_NORM_SHA:
        raise RuntimeError(f"Normalization SHA mismatch: {norm_sha} != {EXPECTED_NORM_SHA}")

    ood_mdata = json.loads(OOD_MANIFEST.read_text())
    if len(ood_mdata.get("episodes", [])) != 150:
        raise RuntimeError(f"OOD manifest episode count is {len(ood_mdata.get('episodes', []))}, expected 150")

    result = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_sha256": model_sha,
        "normalization_sha256": norm_sha,
        "hard1000_paused_at": 249,
        "locked_ood_episodes": 150,
        "main_threshold": FROZEN_A,
        "alternative_cap": FROZEN_C,
        "min_delta": FROZEN_M,
    }
    (PROTOCOL_DIR / "STAGE0_PREFLIGHT.json").write_text(json.dumps(result, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_0_PREFLIGHT", "result": result})
    return result


# ==============================================================================
# STAGE 1: FREEZE CONTROLLER
# ==============================================================================
def run_stage_1_freeze_controller() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_1_FREEZE_CONTROLLER"})

    controller_payload = {
        "schema_version": "isaac_online_engineering_controller_v1",
        "main_threshold_name": "best_val_f1",
        "main_threshold_value": FROZEN_A,
        "main_threshold_provenance": "Seen-calibrated V1 best_val_f1 decision boundary on seen validation split",
        "alternative_cap_name": "engineering_live_cap_090",
        "alternative_cap_value": FROZEN_C,
        "alternative_cap_provenance": "Engineering controller operating point chosen from preserved real live 9-candidate development decisions (dev40/shadow3)",
        "min_delta": FROZEN_M,
        "model_sha256": EXPECTED_MODEL_SHA,
        "normalization_sha256": EXPECTED_NORM_SHA,
        "controller_semantics": "if main_score < 0.7990124225616455: return 0; elif best_alt_score >= main_score: return 0; elif best_alt_score > 0.9000000000000000: return 0; else: return best_alt_idx",
        "development_viability_metrics": {
            "historical_live_decisions_evaluated": 1660,
            "historical_live_alarms": 928,
            "predicted_replacements": 20,
            "replacement_rate_on_alarms_pct": 2.1551724137931036,
            "affected_episodes": 11,
            "total_episodes_evaluated": 46,
            "median_delta": 0.019708752632141113,
        },
    }
    CONTROLLER_FILE.write_text(json.dumps(controller_payload, indent=2))
    ctrl_sha = sha256_f(CONTROLLER_FILE)

    result = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "controller_path": str(CONTROLLER_FILE),
        "controller_sha256": ctrl_sha,
        "main_threshold": FROZEN_A,
        "alternative_cap": FROZEN_C,
        "min_delta": FROZEN_M,
    }
    (PROTOCOL_DIR / "STAGE1_CONTROLLER_FROZEN.json").write_text(json.dumps(result, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_1_FREEZE_CONTROLLER", "result": result})
    return result


# ==============================================================================
# STAGE 2: UNIT TESTS
# ==============================================================================
def run_stage_2_unit_tests() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_2_UNIT_TESTS"})

    test_script = PROTOCOL_DIR / "test_engineering_controller.py"
    if not test_script.exists():
        local_test = Path(__file__).resolve().parent / "test_engineering_controller.py"
        if local_test.exists():
            shutil.copy2(local_test, test_script)

    cmd = [MINICONDA_PYTHON, str(test_script)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Unit tests failed:\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}")

    result = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stdout": res.stdout,
        "stderr": res.stderr,
    }
    (PROTOCOL_DIR / "STAGE2_UNIT_TESTS.json").write_text(json.dumps(result, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_2_UNIT_TESTS", "result": result})
    return result


# ==============================================================================
# STAGE 3: FUNCTIONAL SHADOW GATE
# ==============================================================================
def run_stage_3_shadow_gate() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_3_SHADOW_GATE"})

    if SHADOW_GATE_DIR.exists():
        shutil.rmtree(SHADOW_GATE_DIR)
    SHADOW_GATE_DIR.mkdir(parents=True)

    runner_script = PROTOCOL_DIR / "run_isaac_online_risk.py"
    if not runner_script.exists():
        shutil.copy2(Path(__file__).resolve().parent / "run_isaac_online_risk.py", runner_script)

    runtime_script = PROTOCOL_DIR / "online_isaac_runtime.py"
    if not runtime_script.exists():
        shutil.copy2(Path(__file__).resolve().parent / "online_isaac_runtime.py", runtime_script)

    cmd = [
        ISAAC_PYTHON,
        str(runner_script),
        "--run-config", str(RUN_CONFIG),
        "--manifest", str(OOD_MANIFEST),
        "--output-dir", str(SHADOW_GATE_DIR),
        "--risk-model-root", str(WORKSPACE / "models/isaac_h10_topk8_temporal_v1"),
        "--risk-normalization", str(NORM_PATH),
        "--controller-config", str(CONTROLLER_FILE),
        "--online-mode", "shadow",
        "--online-role", "shadow",
        "--protocol-id", "isaac_ood150_shadow_gate_v1",
        "--execution-mode", "chunk_h10",
        "--offset", "0",
        "--count", "1",
        "--headless",
    ]

    log_path = SHADOW_GATE_DIR / "shadow_gate_launch.log"
    with open(log_path, "w") as logf:
        proc = subprocess.run(cmd, stdout=logf, stderr=subprocess.STDOUT, text=True)

    if proc.returncode != 0:
        raise RuntimeError(f"Shadow gate launch failed with code {proc.returncode}. Log: {log_path}")

    samples_file = SHADOW_GATE_DIR / "risk_receding_samples.jsonl"
    if not samples_file.exists():
        raise RuntimeError(f"Shadow gate failed: {samples_file} not created")

    rows = [json.loads(line) for line in samples_file.read_text().splitlines() if line.strip()]
    if not rows:
        raise RuntimeError("Shadow gate produced 0 rows")

    for r in rows:
        orisk = r.get("online_risk", {})
        cand_scores = orisk.get("candidate_scores")
        if not cand_scores or len(cand_scores) != 9:
            raise RuntimeError(f"Shadow row missing 9 candidate scores: {orisk}")
        exec_chunk = np.array(r["executed_action_sequence"])
        main_chunk = np.array(r["main_candidate_action_chunk_env"])[:len(exec_chunk)]
        if not np.allclose(exec_chunk, main_chunk, atol=1e-4):
            raise RuntimeError("Shadow mode executed action does not match candidate 0 action chunk")

    result = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "episodes_completed": 1,
        "rows_verified": len(rows),
        "shadow_execution_parity": True,
        "nine_candidate_scores_logged": True,
    }
    (PROTOCOL_DIR / "STAGE3_SHADOW_GATE.json").write_text(json.dumps(result, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_3_SHADOW_GATE", "result": result})
    return result


# ==============================================================================
# AUDIT HELPER (Fix 5: accurate key parsing & count tracking)
# ==============================================================================
def audit_definitive_progress() -> dict[str, Any]:
    samples_file = DEFINITIVE_RUN_DIR / "risk_receding_samples.jsonl"
    summaries_file = DEFINITIVE_RUN_DIR / "episode_summaries.jsonl"

    if not samples_file.exists() or not summaries_file.exists():
        return {
            "completed_episodes": 0,
            "unique_source_ids_count": 0,
            "total_decisions": 0,
            "alarms": 0,
            "best_alt_lower_than_main": 0,
            "cap_passes": 0,
            "accepted_replacements": 0,
            "episodes_with_replacement": 0,
            "candidate_histogram": {},
            "selection_mismatches": 0,
            "execution_mismatches": 0,
            "max_action_diff": 0.0,
        }

    summaries = [json.loads(l) for l in summaries_file.read_text().splitlines() if l.strip()]
    rows = [json.loads(l) for l in samples_file.read_text().splitlines() if l.strip()]

    completed_eps = len(summaries)
    source_ids = [s["source_episode_id"] for s in summaries]
    unique_ids = set(source_ids)
    if len(unique_ids) != completed_eps:
        raise RuntimeError(f"Duplicate source episode IDs detected: {len(unique_ids)} != {completed_eps}")

    alarms = 0
    best_alt_lower_main = 0
    cap_passes = 0
    replacements = 0
    eps_with_repl = set()
    cand_hist = Counter()
    selection_mismatches = 0
    execution_mismatches = 0
    max_action_diff = 0.0

    for r in rows:
        orisk = r.get("online_risk", {})
        cand_scores = orisk.get("candidate_scores")
        if not cand_scores or len(cand_scores) != 9:
            continue

        main_s = float(cand_scores[0])
        alt_scores = cand_scores[1:]
        best_alt_idx = int(np.argmin(alt_scores)) + 1
        best_alt_s = float(cand_scores[best_alt_idx])

        # Exact controller rule
        expected_sel_idx = 0
        expected_reason = "main_below_alarm_threshold"
        expected_interv = False

        if main_s >= FROZEN_A:
            alarms += 1
            if best_alt_s < main_s:
                best_alt_lower_main += 1
                if best_alt_s <= FROZEN_C:
                    cap_passes += 1
                    expected_sel_idx = best_alt_idx
                    expected_reason = "argmin_on_alarm_cap_pass"
                    expected_interv = True
                else:
                    expected_reason = "best_alternative_above_cap"
            else:
                expected_reason = "main_is_lowest"

        logged_sel_idx = int(orisk.get("selected_candidate_index", 0))
        logged_interv = (
            logged_sel_idx > 0
            or bool(orisk.get("proposed_modification", False))
            or bool(orisk.get("is_intervention", False))
        )

        if logged_sel_idx != expected_sel_idx or logged_interv != expected_interv:
            selection_mismatches += 1

        if logged_interv:
            replacements += 1
            ep_src_id = r.get("metadata", {}).get("source_episode_id")
            if ep_src_id is not None:
                eps_with_repl.add(ep_src_id)
            cand_hist[logged_sel_idx] += 1

        # Audit execution action chunk vs selected chunk
        exec_seq = np.array(r["executed_action_sequence"])
        if logged_sel_idx == 0:
            expected_chunk = np.array(r["main_candidate_action_chunk_env"])
        else:
            expected_chunk = np.array(r["ace_candidate_chunks_env"][logged_sel_idx - 1])
        expected_chunk = expected_chunk[:len(exec_seq)]

        diff = float(np.max(np.abs(exec_seq - expected_chunk)))
        if diff > max_action_diff:
            max_action_diff = diff
        if diff > 1e-4:
            execution_mismatches += 1

    return {
        "completed_episodes": completed_eps,
        "unique_source_ids_count": len(unique_ids),
        "total_decisions": len(rows),
        "alarms": alarms,
        "best_alt_lower_than_main": best_alt_lower_main,
        "cap_passes": cap_passes,
        "accepted_replacements": replacements,
        "episodes_with_replacement": len(eps_with_repl),
        "candidate_histogram": dict(cand_hist),
        "selection_mismatches": selection_mismatches,
        "execution_mismatches": execution_mismatches,
        "max_action_diff": max_action_diff,
    }


# ==============================================================================
# STAGE 4 & 5: LAUNCH DEFINITIVE ACTIVE OOD150 & HEALTH GATE
# ==============================================================================
def launch_definitive_process() -> int:
    DEFINITIVE_RUN_DIR.mkdir(parents=True, exist_ok=True)
    cmd = build_definitive_command()
    log_path = DEFINITIVE_RUN_DIR / "launch.log"
    log_file = open(log_path, "a")
    proc = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True)
    log_event("DEFINITIVE_RUN_LAUNCHED", {"pid": proc.pid, "log_path": str(log_path)})
    return proc.pid


def run_stage_5_health_gate(definitive_pid: int | None) -> bool:
    log_event("STAGE_START", {"stage": "STAGE_5_HEALTH_GATE_10EP"})
    print("Executing Stage 5 Health Gate at target = 10 completed episodes...")

    requested_gate_target = 10

    # If child is still alive and we haven't requested pause, monitor until target reached
    while True:
        audit = audit_definitive_progress()
        completed = audit["completed_episodes"]
        if completed >= requested_gate_target:
            if is_pid_alive(definitive_pid, "run_isaac_online_risk.py"):
                print(f"Reached {completed} episodes. Requesting clean pause...")
                (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").touch()
                # Wait for process to exit cleanly
                timeout_s = 300
                start_t = time.time()
                while is_pid_alive(definitive_pid, "run_isaac_online_risk.py") and (time.time() - start_t < timeout_s):
                    time.sleep(5)
                if (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").exists():
                    (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").unlink()
            break
        if not is_pid_alive(definitive_pid, "run_isaac_online_risk.py"):
            break
        time.sleep(10)

    # Re-audit after process has paused/exited
    audit = audit_definitive_progress()
    actual_completed_at_gate = audit["completed_episodes"]

    gate_record = {
        "status": "EVALUATED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "requested_gate_target": requested_gate_target,
        "actual_completed_at_gate": actual_completed_at_gate,
        "audit_metrics": audit,
    }

    if actual_completed_at_gate > 11:
        gate_record["status"] = "HEALTH_GATE_OVERSHOOT"
        (PROTOCOL_DIR / "STAGE5_HEALTH_GATE_10EP.json").write_text(json.dumps(gate_record, indent=2))
        log_event("HEALTH_GATE_OVERSHOOT", gate_record)
        raise RuntimeError(f"Health gate overshoot: {actual_completed_at_gate} > 11 completed episodes")

    if audit["selection_mismatches"] > 0 or audit["execution_mismatches"] > 0:
        gate_record["status"] = "FAILED_ON_MISMATCHES"
        (PROTOCOL_DIR / "STAGE5_HEALTH_GATE_10EP.json").write_text(json.dumps(gate_record, indent=2))
        raise RuntimeError(f"Health gate parity audit failed: {audit}")

    if audit["accepted_replacements"] == 0:
        gate_record["status"] = "ZERO_INTERVENTION_HEALTH_GATE"
        (PROTOCOL_DIR / "STAGE5_HEALTH_GATE_10EP.json").write_text(json.dumps(gate_record, indent=2))
        log_event("ZERO_INTERVENTION_HEALTH_GATE", gate_record)
        print("\n" + "=" * 80)
        print("STAGE 5 HEALTH GATE: ZERO INTERVENTIONS DETECTED. SAFE STOP FOR REVIEW.")
        print("=" * 80 + "\n")
        return False

    gate_record["status"] = "PASSED"
    (PROTOCOL_DIR / "STAGE5_HEALTH_GATE_10EP.json").write_text(json.dumps(gate_record, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_5_HEALTH_GATE_10EP", "result": gate_record})
    print("\n" + "=" * 80)
    print(f"STAGE 5 HEALTH GATE PASSED! ({audit['accepted_replacements']} replacements across {audit['episodes_with_replacement']} episodes, actual completed: {actual_completed_at_gate})")
    print("=" * 80 + "\n")
    return True


def load_locked_source_episode_ids(manifest_path: Path = OOD_MANIFEST) -> list[int]:
    """Canonical loader for locked OOD150 source episode IDs matching runner semantics."""
    resolved_path = Path(manifest_path).resolve()
    if not resolved_path.is_file():
        raise FileNotFoundError(f"Locked manifest not found: {resolved_path}")
    payload = json.loads(resolved_path.read_text(encoding="utf-8"))
    raw_episodes = payload.get("episodes", [])
    if len(raw_episodes) != 150:
        raise ValueError(f"Expected 150 episodes in manifest, got {len(raw_episodes)}")
    source_ids: list[int] = []
    for ep in raw_episodes:
        if "scene" in ep and "source_episode_id" in ep["scene"]:
            source_ids.append(int(ep["scene"]["source_episode_id"]))
        elif "source_episode_id" in ep:
            source_ids.append(int(ep["source_episode_id"]))
        elif "benchmark_episode_id" in ep:
            source_ids.append(int(ep["benchmark_episode_id"]))
        else:
            raise KeyError(f"Unable to extract source_episode_id from manifest episode entry: {list(ep.keys())}")
    if len(source_ids) != 150:
        raise ValueError(f"Expected 150 extracted source IDs, got {len(source_ids)}")
    if len(set(source_ids)) != 150:
        raise ValueError(f"Duplicate source IDs in manifest: {len(set(source_ids))} != 150")
    return source_ids


# ==============================================================================
# STAGE 6: RESUMABLE TOP-LEVEL COMPLETION & MEMBERSHIP AUDIT (Bugs 1 & 4)
# ==============================================================================
def run_stage_6_complete_150(state: dict[str, Any]) -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_6_COMPLETE_150"})
    print("Executing Stage 6: Full 150 Episodes Completion and Strict Membership Gate...")

    pid = state.get("definitive_pid")

    while True:
        summaries = get_committed_summaries(DEFINITIVE_RUN_DIR)
        completed_count = len(summaries)
        state["completed_episodes_count"] = completed_count
        save_state(state)

        if completed_count >= 150:
            print(f"All 150 episodes committed (count: {completed_count}). Proceeding to final audit.")
            # Verify no running Isaac processes remain
            active_isaac = check_active_processes(["run_isaac_online_risk.py"])
            if active_isaac:
                print(f"Waiting for Isaac runner to exit cleanly: {active_isaac}")
                time.sleep(5)
            break

        # Check if child is alive
        if not is_pid_alive(pid, "run_isaac_online_risk.py"):
            print(f"Child process {pid} is not alive and only {completed_count}/150 episodes committed. Relaunching...")
            new_pid = launch_definitive_process()
            state["definitive_pid"] = new_pid
            pid = new_pid
            save_state(state)

        time.sleep(15)

    # 1. Strict Fail-Closed Membership Validation against canonical locked manifest
    expected_source_ids = load_locked_source_episode_ids(OOD_MANIFEST)
    expected_set = set(expected_source_ids)

    summaries = get_committed_summaries(DEFINITIVE_RUN_DIR)
    new_source_ids = [int(s["source_episode_id"]) for s in summaries]
    actual_set = set(new_source_ids)

    missing_ids = sorted(list(expected_set - actual_set))
    extra_ids = sorted(list(actual_set - expected_set))
    duplicate_ids = [id_ for id_, count in Counter(new_source_ids).items() if count > 1]
    exact_match = (
        len(expected_source_ids) == 150
        and len(new_source_ids) == 150
        and len(missing_ids) == 0
        and len(extra_ids) == 0
        and len(duplicate_ids) == 0
    )

    # 2. Strict Historical Baseline Membership Validation
    if not HISTORICAL_OOD150_SUMMARIES.exists():
        raise RuntimeError(f"Historical OOD150 summaries not found at {HISTORICAL_OOD150_SUMMARIES}")
    ood_hist_summaries = [json.loads(l) for l in HISTORICAL_OOD150_SUMMARIES.read_text().splitlines() if l.strip()]
    hist_source_ids = [int(s["source_episode_id"]) for s in ood_hist_summaries]
    hist_set = set(hist_source_ids)

    hist_missing = sorted(list(expected_set - hist_set))
    hist_extra = sorted(list(hist_set - expected_set))
    hist_exact_match = (
        len(hist_source_ids) == 150
        and len(hist_set) == 150
        and len(hist_missing) == 0
        and len(hist_extra) == 0
    )

    membership_audit = {
        "schema_version": "isaac_online_final_membership_audit_v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "expected_count": len(expected_source_ids),
        "actual_count": len(new_source_ids),
        "unique_actual_count": len(actual_set),
        "missing_ids": missing_ids,
        "extra_ids": extra_ids,
        "duplicate_ids": duplicate_ids,
        "exact_match": exact_match,
        "historical_count": len(hist_source_ids),
        "historical_unique": len(hist_set),
        "historical_missing": hist_missing,
        "historical_extra": hist_extra,
        "historical_exact_match": hist_exact_match,
        "extraction_method": "canonical locked manifest scene.source_episode_id parser matching runner semantics",
    }
    (PROTOCOL_DIR / "FINAL_MEMBERSHIP_AUDIT.json").write_text(json.dumps(membership_audit, indent=2))

    if not exact_match:
        raise RuntimeError(f"Strict final active membership gate FAILED: {membership_audit}")
    if not hist_exact_match:
        raise RuntimeError(f"Strict final historical membership gate FAILED: {membership_audit}")

    # 3. Paired Comparison with Historical OOD150 (Direct explicit assertion & lookup)
    hist_succ_by_src = {int(s["source_episode_id"]): bool(s["success"]) for s in ood_hist_summaries}
    active_succ_by_src = {int(s["source_episode_id"]): bool(s.get("success", False)) for s in summaries}

    for src_id in expected_source_ids:
        if src_id not in hist_succ_by_src:
            raise RuntimeError(f"Source episode ID {src_id} not found in historical OOD150 baseline!")
        if src_id not in active_succ_by_src:
            raise RuntimeError(f"Source episode ID {src_id} not found in active OOD150 run!")

    historical_successes = sum(1 for src_id in expected_source_ids if hist_succ_by_src[src_id])
    active_successes = sum(1 for src_id in expected_source_ids if active_succ_by_src[src_id])

    rescues = 0
    regressions = 0
    persisted_success = 0
    persisted_failure = 0

    for src_id in expected_source_ids:
        h_succ = hist_succ_by_src[src_id]
        n_succ = active_succ_by_src[src_id]
        if not h_succ and n_succ:
            rescues += 1
        elif h_succ and not n_succ:
            regressions += 1
        elif h_succ and n_succ:
            persisted_success += 1
        else:
            persisted_failure += 1

    # 4. Assert Paired Arithmetic
    arithmetic_ok = (active_successes == historical_successes + rescues - regressions)
    if not arithmetic_ok:
        raise RuntimeError(
            f"Arithmetic invariant failed: active ({active_successes}) != "
            f"historical ({historical_successes}) + rescues ({rescues}) - regressions ({regressions})"
        )

    net_delta = rescues - regressions
    if net_delta != (active_successes - historical_successes):
        raise RuntimeError(f"Net delta mismatch: {net_delta} != {active_successes - historical_successes}")

    audit_metrics = audit_definitive_progress()

    comparison = {
        "schema_version": "isaac_online_definitive_final_result_v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "protocol_id": "isaac_ood150_definitive_active_cap090_v1",
        "total_episodes": 150,
        "historical_baseline_successes": historical_successes,
        "active_new_successes": active_successes,
        "success_delta_absolute": active_successes - historical_successes,
        "success_delta_percentage_points": (active_successes - historical_successes) / 150.0 * 100.0,
        "rescues_baseline_fail_to_new_succ": rescues,
        "regressions_baseline_succ_to_new_fail": regressions,
        "persisted_success": persisted_success,
        "persisted_failure": persisted_failure,
        "paired_arithmetic_verified": True,
        "controller_parameters": {
            "main_alarm_threshold": FROZEN_A,
            "alternative_safe_cap": FROZEN_C,
            "min_delta": FROZEN_M,
        },
        "audit_metrics": audit_metrics,
        "membership_audit": membership_audit,
    }

    (PROTOCOL_DIR / "STAGE6_COMPLETION.json").write_text(json.dumps(comparison, indent=2))
    (PROTOCOL_DIR / "FINAL_RESULT.json").write_text(json.dumps(comparison, indent=2))
    (PROTOCOL_DIR / "FINAL_PAIRED_COMPARISON.json").write_text(json.dumps(comparison, indent=2))
    (PROTOCOL_DIR / "FINAL_CONTROLLER_AUDIT.json").write_text(json.dumps(audit_metrics, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_6_COMPLETE_150", "result": comparison})
    return comparison


# ==============================================================================
# STAGE 7: FINAL EVIDENCE FREEZE & REAL GIT PUSH (Bugs 2 & 3)
# ==============================================================================
def run_stage_7_freeze_evidence() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_7_FINAL_EVIDENCE_FREEZE"})
    print("Executing Stage 7: Evidence Freeze, Provenance Correction, and Verified Git Push...")

    # 1. Create CONTROLLER_PROVENANCE_CORRECTION.json (Bug 3)
    provenance_correction = {
        "schema_version": "isaac_controller_provenance_correction_v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "main_threshold": FROZEN_A,
        "main_threshold_source": "Seen validation best_val_f1",
        "alternative_cap": FROZEN_C,
        "alternative_cap_source": "Preserved real live 9-candidate OOD development decisions",
        "ood_development_used_for_alternative_cap_selection": True,
        "definitive_ood150_is_not_pristine_untouched_for_controller_selection": True,
        "raw_run_manifest_known_metadata_issue": "ood_dev_used_for_controller_pair_selection was derived from current run role and is false for full150 despite development-informed cap",
        "scientific_interpretation": {
            "main_detector_threshold": "Seen-calibrated V1 best_val_f1 decision boundary",
            "alternative_cap": "Engineering controller operating point chosen from preserved real live 9-candidate development decisions",
            "definitive_ood150_status": "Active engineering evaluation on locked OOD150 membership; NOT a pristine untouched OOD holdout for controller hyperparameter selection",
        },
    }
    (PROTOCOL_DIR / "CONTROLLER_PROVENANCE_CORRECTION.json").write_text(json.dumps(provenance_correction, indent=2))

    # 2. Create FINAL_RUN_MANIFEST.json with corrected provenance
    raw_manifest_p = DEFINITIVE_RUN_DIR / "run_manifest.json"
    if not raw_manifest_p.exists():
        raise RuntimeError(f"Raw run manifest not found at {raw_manifest_p}")
    raw_manifest = json.loads(raw_manifest_p.read_text())
    raw_manifest_sha = sha256_f(raw_manifest_p)

    final_run_manifest = dict(raw_manifest)
    final_run_manifest["raw_run_manifest_sha256"] = raw_manifest_sha
    final_run_manifest["online_risk_intervention"]["ood_dev_used_for_controller_pair_selection"] = True
    final_run_manifest["online_risk_intervention"]["alternative_cap_provenance"] = "Preserved real live 9-candidate OOD development decisions"
    final_run_manifest["online_risk_intervention"]["provenance_correction_applied"] = True
    (PROTOCOL_DIR / "FINAL_RUN_MANIFEST.json").write_text(json.dumps(final_run_manifest, indent=2))

    # 3. Write FINAL_REPORT.md
    res = json.loads((PROTOCOL_DIR / "FINAL_RESULT.json").read_text())
    report_md = f"""# Definitive Active Online OOD150 Result (Engineering Cap 0.90)

## Executive Summary
- **Protocol ID:** `isaac_ood150_definitive_active_cap090_v1`
- **Main Alarm Threshold ($A$):** `{FROZEN_A}` (Seen V1 `best_val_f1`)
- **Alternative Safe Cap ($C$):** `{FROZEN_C}` (Engineering development-informed operating point)
- **Minimum Delta ($M$):** `{FROZEN_M}`
- **Active Success Count:** **{res['active_new_successes']} / 150** ({res['active_new_successes']/150*100:.1f}%)
- **Historical Baseline Success Count:** **{res['historical_baseline_successes']} / 150** ({res['historical_baseline_successes']/150*100:.1f}%)
- **Net Absolute Delta:** **{res['success_delta_absolute']:+d} episodes** ({res['success_delta_percentage_points']:+.1f} percentage points)

## Provenance Note
- **Main Detector Threshold:** Seen-calibrated (`best_val_f1` on seen validation split).
- **Alternative Cap:** Engineering development-informed (derived from preserved live 9-candidate OOD decisions).
- **Evaluation Status:** Active engineering evaluation on locked OOD150 membership (NOT a pristine untouched OOD holdout for controller selection).

## Paired Analysis
- **Rescues (Baseline Fail -> Active Success):** {res['rescues_baseline_fail_to_new_succ']}
- **Regressions (Baseline Success -> Active Fail):** {res['regressions_baseline_succ_to_new_fail']}
- **Persisted Successes:** {res['persisted_success']}
- **Persisted Failures:** {res['persisted_failure']}

## Controller Decision Statistics
- **Total Online Decisions:** {res['audit_metrics']['total_decisions']}
- **Total Alarms:** {res['audit_metrics']['alarms']}
- **Accepted Action Replacements:** {res['audit_metrics']['accepted_replacements']}
- **Episodes with Interventions:** {res['audit_metrics']['episodes_with_replacement']} / 150
- **Candidate Replacement Histogram:** `{res['audit_metrics']['candidate_histogram']}`
"""
    (PROTOCOL_DIR / "FINAL_REPORT.md").write_text(report_md)

    # 4. Generate FINAL_SHA256SUMS.txt
    sha_txt = ""
    for f in sorted(PROTOCOL_DIR.glob("*.json")) + sorted(PROTOCOL_DIR.glob("*.md")) + sorted(PROTOCOL_DIR.glob("*.py")):
        if f.is_file() and not f.name.endswith("SHA256SUMS.txt"):
            sha_txt += f"{sha256_f(f)}  {f.name}\n"
    (PROTOCOL_DIR / "FINAL_SHA256SUMS.txt").write_text(sha_txt)

    # 5. Synchronize small final evidence into local git repository and push (Bug 2)
    GIT_EXPERIMENT_SUBDIR.mkdir(parents=True, exist_ok=True)
    files_to_sync = [
        "SELECTED_ENGINEERING_CONTROLLER.json",
        "CONTROLLER_PROVENANCE_CORRECTION.json",
        "STAGE6_RECOVERY_NOTE.json",
        "STAGE_6_COMPLETE_150_FAILED.json",
        "FINAL_RESULT.json",
        "FINAL_CONTROLLER_AUDIT.json",
        "FINAL_PAIRED_COMPARISON.json",
        "FINAL_MEMBERSHIP_AUDIT.json",
        "FINAL_RUN_MANIFEST.json",
        "FINAL_REPORT.md",
        "FINAL_SHA256SUMS.txt",
        "STAGE0_PREFLIGHT.json",
        "STAGE1_CONTROLLER_FROZEN.json",
        "STAGE2_UNIT_TESTS.json",
        "STAGE3_SHADOW_GATE.json",
        "STAGE5_HEALTH_GATE_10EP.json",
        "STAGE6_COMPLETION.json",
    ]
    for fname in files_to_sync:
        src = PROTOCOL_DIR / fname
        if src.exists():
            shutil.copy2(src, GIT_EXPERIMENT_SUBDIR / fname)

    # Git commit and push
    subprocess.run(["git", "-C", str(GIT_REPO_DIR), "add", str(GIT_EXPERIMENT_SUBDIR.relative_to(GIT_REPO_DIR))], check=True)
    commit_res = subprocess.run(
        ["git", "-C", str(GIT_REPO_DIR), "commit", "-m", "feat(ood150): freeze final evidence for definitive online OOD150 campaign"],
        capture_output=True,
        text=True,
    )
    push_res = subprocess.run(
        ["git", "-C", str(GIT_REPO_DIR), "push", "origin", GIT_BRANCH],
        capture_output=True,
        text=True,
        check=True,
    )

    # 6. Verify remote ref resolves to local commit SHA
    head_commit = subprocess.run(
        ["git", "-C", str(GIT_REPO_DIR), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    ls_remote = subprocess.run(
        ["git", "-C", str(GIT_REPO_DIR), "ls-remote", "origin", f"refs/heads/{GIT_BRANCH}"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    remote_commit = ls_remote.split()[0] if ls_remote else ""
    if remote_commit != head_commit:
        raise RuntimeError(f"Remote commit verification failed: local={head_commit} remote={remote_commit}")

    stage7_record = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "FINAL_EVIDENCE_GIT_COMMIT": head_commit,
        "FINAL_EVIDENCE_GIT_BRANCH": GIT_BRANCH,
        "remote_verified": True,
        "synced_files": files_to_sync,
    }
    (PROTOCOL_DIR / "STAGE7_FINAL_EVIDENCE_FREEZE.json").write_text(json.dumps(stage7_record, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_7_FINAL_EVIDENCE_FREEZE", "result": stage7_record})
    return stage7_record


# ==============================================================================
# STAGE 8: STRICT HARD1000 PRE-RESUME GUARD & POST-RESUME VERIFICATION (Bug 6)
# ==============================================================================
def run_stage_8_resume_hard1000() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_8_RESUME_HARD1000"})
    print("Executing Stage 8: Strict Pre-Resume HARD1000 Guard and Verified Resumption...")

    # 1. Pre-Resume Guards
    if not (PROTOCOL_DIR / "FINAL_RESULT.json").exists():
        raise RuntimeError("Stage 8 Pre-Guard Failed: FINAL_RESULT.json does not exist")
    mem_audit = json.loads((PROTOCOL_DIR / "FINAL_MEMBERSHIP_AUDIT.json").read_text())
    if not mem_audit.get("exact_match", False):
        raise RuntimeError("Stage 8 Pre-Guard Failed: FINAL_MEMBERSHIP_AUDIT exact_match is not true")
    stage7_rec = json.loads((PROTOCOL_DIR / "STAGE7_FINAL_EVIDENCE_FREEZE.json").read_text())
    if not stage7_rec.get("remote_verified", False):
        raise RuntimeError("Stage 8 Pre-Guard Failed: Stage 7 git evidence was not remote-verified")

    # Verify no active definitive Isaac processes
    active_isaac = check_active_processes(["run_isaac_online_risk.py"])
    if active_isaac:
        raise RuntimeError(f"Stage 8 Pre-Guard Failed: active Isaac online runners still alive: {active_isaac}")

    # Verify HARD1000 directory state
    hard_status_p = HARD1000_DIR / "live_status.json"
    hard_summaries_p = HARD1000_DIR / "episode_summaries.jsonl"
    if not hard_status_p.exists() or not hard_summaries_p.exists():
        raise RuntimeError("Stage 8 Pre-Guard Failed: HARD1000 status or summaries missing")

    hard_status = json.loads(hard_status_p.read_text())
    if hard_status.get("completed_episodes") != 249:
        raise RuntimeError(f"Stage 8 Pre-Guard Failed: HARD1000 completed_episodes is {hard_status.get('completed_episodes')}, expected 249")

    hard_summaries = [json.loads(l) for l in hard_summaries_p.read_text().splitlines() if l.strip()]
    if len(hard_summaries) != 249:
        raise RuntimeError(f"Stage 8 Pre-Guard Failed: HARD1000 summaries count is {len(hard_summaries)}, expected 249")

    # Record PRE-resume snapshot and SHA256 of the 249 episode identity set
    pre_source_ids = [s["source_episode_id"] for s in hard_summaries]
    pre_global_ids = [s.get("global_episode_id", f"s{s['source_episode_id']}") for s in hard_summaries]
    if len(set(pre_source_ids)) != 249:
        raise RuntimeError("Stage 8 Pre-Guard Failed: duplicate IDs detected in original 249 HARD episodes")

    pre_snapshot_hash = hashlib.sha256(json.dumps(pre_source_ids).encode()).hexdigest()

    # Check no existing HARD collectors / pipeline alive
    active_hard = check_active_processes(["hard1000_pipeline.py", "collect_isaac_risk.py"])
    if active_hard:
        raise RuntimeError(f"Stage 8 Pre-Guard Failed: existing HARD processes alive: {active_hard}")

    # 2. Resume HARD1000 Cleanly
    stop_p1 = WORKSPACE / "automation/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
    stop_p2 = HARD1000_DIR / "STOP_AFTER_CURRENT_EPISODE"
    if stop_p1.exists():
        stop_p1.unlink()
    if stop_p2.exists():
        stop_p2.unlink()

    hard1000_script = WORKSPACE / "automation/hard1000_pipeline.py"
    log_file = open(WORKSPACE / "logs/hard1000_pipeline.log", "a")
    pipe_proc = subprocess.Popen([MINICONDA_PYTHON, "-u", str(hard1000_script)], stdout=log_file, stderr=subprocess.STDOUT)

    # 3. Post-Resume Verification
    time.sleep(10)
    if not is_pid_alive(pipe_proc.pid):
        raise RuntimeError("HARD1000 pipeline failed to remain alive after launch")

    print(f"HARD1000 pipeline launched under PID {pipe_proc.pid}. Waiting for new episode progress (completed > 249)...")
    timeout_s = 600
    start_t = time.time()
    resumed_status = None
    new_episode_verified = False

    while time.time() - start_t < timeout_s:
        hard_status = json.loads(hard_status_p.read_text())
        current_completed = hard_status.get("completed_episodes", 0)

        # Verify existing 249 episodes not overwritten
        curr_summaries = [json.loads(l) for l in hard_summaries_p.read_text().splitlines() if l.strip()]
        curr_source_ids = [s["source_episode_id"] for s in curr_summaries]
        if curr_source_ids[:249] != pre_source_ids:
            raise RuntimeError("HARD1000 post-resume integrity check FAILED: original 249 episodes modified!")

        if current_completed > 249:
            new_id = curr_source_ids[249]
            if new_id in set(pre_source_ids):
                raise RuntimeError(f"New HARD episode ID {new_id} was already present in old 249 set!")
            new_episode_verified = True
            resumed_status = hard_status
            break
        time.sleep(15)

    if not new_episode_verified:
        raise RuntimeError(f"HARD1000 did not progress to > 249 episodes within {timeout_s}s timeout")

    stage8_record = {
        "status": "PASSED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pre_resume_249_hash": pre_snapshot_hash,
        "pipeline_pid": pipe_proc.pid,
        "resumed_completed_episodes": resumed_status.get("completed_episodes"),
        "new_episode_id_verified": new_id,
    }
    (PROTOCOL_DIR / "STAGE8_HARD1000_RESUMED.json").write_text(json.dumps(stage8_record, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_8_RESUME_HARD1000", "result": stage8_record})

    # 4. Final Follow-Up Evidence Commit (Item 9)
    try:
        files_to_sync_final = [
            "STAGE7_FINAL_EVIDENCE_FREEZE.json",
            "STAGE8_HARD1000_RESUMED.json",
            "STAGE6_RECOVERY_NOTE.json",
            "STAGE_6_COMPLETE_150_FAILED.json",
            "ORCHESTRATOR_STATE.json",
            "ORCHESTRATOR_EVENTS.jsonl",
            "FINAL_SHA256SUMS.txt",
        ]
        for fname in files_to_sync_final:
            src = PROTOCOL_DIR / fname
            if src.exists():
                shutil.copy2(src, GIT_EXPERIMENT_SUBDIR / fname)

        subprocess.run(["git", "-C", str(GIT_REPO_DIR), "add", str(GIT_EXPERIMENT_SUBDIR.relative_to(GIT_REPO_DIR))], check=True)
        subprocess.run(
            ["git", "-C", str(GIT_REPO_DIR), "commit", "-m", "feat(ood150): add final post-resume execution evidence and recovery records"],
            capture_output=True,
            text=True,
        )
        subprocess.run(
            ["git", "-C", str(GIT_REPO_DIR), "push", "origin", GIT_BRANCH],
            capture_output=True,
            text=True,
            check=True,
        )
        final_head = subprocess.run(
            ["git", "-C", str(GIT_REPO_DIR), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        stage8_record["FINAL_FOLLOWUP_GIT_COMMIT"] = final_head
        (PROTOCOL_DIR / "STAGE8_HARD1000_RESUMED.json").write_text(json.dumps(stage8_record, indent=2))
    except Exception as e:
        print(f"Warning: follow-up evidence git commit failed: {e}")

    return stage8_record


# ==============================================================================
# MAIN ORCHESTRATOR LOOP (Bug 7: Fail-Closed Wrapping)
# ==============================================================================
def record_stage_failure(stage_name: str, exc: Exception) -> None:
    tb_str = traceback.format_exc()
    fail_record = {
        "status": "FAILED",
        "stage": stage_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "exception": str(exc),
        "traceback": tb_str,
    }
    log_event("STAGE_FAILED", fail_record)
    (PROTOCOL_DIR / f"{stage_name}_FAILED.json").write_text(json.dumps(fail_record, indent=2))

    state = load_state()
    state["status"] = "FAILED"
    state["failed_stage"] = stage_name
    save_state(state)
    print(f"\n[FAIL-CLOSED] Orchestrator halted at {stage_name} due to exception: {exc}\n")


def main() -> None:
    PROTOCOL_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()

    print("\n" + "=" * 80)
    print("STARTING END-TO-END ORCHESTRATOR (Engineering Cap 0.90 - Repaired)")
    print(f"Current State: {state['current_stage']} (status: {state['status']})")
    print("=" * 80 + "\n")

    try:
        # Stage 0
        if state["current_stage"] == "STAGE_0_PREFLIGHT":
            run_stage_0_preflight()
            state["current_stage"] = "STAGE_1_FREEZE_CONTROLLER"
            save_state(state)

        # Stage 1
        if state["current_stage"] == "STAGE_1_FREEZE_CONTROLLER":
            run_stage_1_freeze_controller()
            state["current_stage"] = "STAGE_2_UNIT_TESTS"
            save_state(state)

        # Stage 2
        if state["current_stage"] == "STAGE_2_UNIT_TESTS":
            run_stage_2_unit_tests()
            state["current_stage"] = "STAGE_3_SHADOW_GATE"
            save_state(state)

        # Stage 3
        if state["current_stage"] == "STAGE_3_SHADOW_GATE":
            run_stage_3_shadow_gate()
            state["current_stage"] = "STAGE_4_LAUNCH_DEFINITIVE_OOD150"
            save_state(state)

        # Stage 4 & 5
        if state["current_stage"] == "STAGE_4_LAUNCH_DEFINITIVE_OOD150":
            pid = state.get("definitive_pid")
            if not is_pid_alive(pid, "run_isaac_online_risk.py"):
                pid = launch_definitive_process()
                state["definitive_pid"] = pid
                state["status"] = "RUNNING_DEFINITIVE"
                save_state(state)

            health_passed = run_stage_5_health_gate(pid)
            state["health_gate_passed"] = health_passed
            if not health_passed:
                state["status"] = "STOPPED_AT_ZERO_INTERVENTION_HEALTH_GATE"
                save_state(state)
                return

            # Launch/relaunch from episode 11 to 150
            proc_pid = launch_definitive_process()
            state["definitive_pid"] = proc_pid
            state["current_stage"] = "STAGE_6_COMPLETE_150"
            state["status"] = "RUNNING_DEFINITIVE"
            save_state(state)

        # Stage 6: Genuine Top-Level Resumable State Handler (Bug 1)
        if state["current_stage"] == "STAGE_6_COMPLETE_150":
            run_stage_6_complete_150(state)
            state["current_stage"] = "STAGE_7_FINAL_EVIDENCE_FREEZE"
            save_state(state)

        # Stage 7: Real Git Evidence Push (Bug 2 & 3)
        if state["current_stage"] == "STAGE_7_FINAL_EVIDENCE_FREEZE":
            run_stage_7_freeze_evidence()
            state["current_stage"] = "STAGE_8_RESUME_HARD1000"
            save_state(state)

        # Stage 8: Verified HARD1000 Resumption (Bug 6)
        if state["current_stage"] == "STAGE_8_RESUME_HARD1000":
            run_stage_8_resume_hard1000()
            state["current_stage"] = "COMPLETE"
            state["status"] = "ALL_STAGES_COMPLETE"
            save_state(state)

        print("\n" + "=" * 80)
        print("ALL ORCHESTRATOR STAGES COMPLETED SUCCESSFULLY!")
        print("=" * 80 + "\n")

    except Exception as exc:
        record_stage_failure(state["current_stage"], exc)
        raise


if __name__ == "__main__":
    main()
