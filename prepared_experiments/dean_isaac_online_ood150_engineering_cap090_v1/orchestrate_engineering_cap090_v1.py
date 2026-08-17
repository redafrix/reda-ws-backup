#!/usr/bin/env python3
"""End-to-end resumable orchestrator for Isaac Online OOD150 Engineering Controller (A=0.799012, C=0.900, M=0.0)."""

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
from typing import Any

import numpy as np

WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")
PROTOCOL_DIR = WORKSPACE / "online_evals/isaac_ood150_engineering_cap090_v1"
RUNS_DIR = PROTOCOL_DIR / "runs"
DEFINITIVE_RUN_DIR = RUNS_DIR / "definitive_full150"
SHADOW_GATE_DIR = RUNS_DIR / "shadow_gate"
HARD1000_DIR = WORKSPACE / "outputs/final_seen_h10_round_002_seed20260804"

MODEL_PATH = WORKSPACE / "models/isaac_h10_topk8_temporal_v1/model.pt"
NORM_PATH = WORKSPACE / "frozen_datasets/isaac_seen_h10_topk8_v1/normalization.json"
OOD_MANIFEST = WORKSPACE / "automation/generated/locked_ood150/manifest.json"
RUN_CONFIG = WORKSPACE / "automation/generated/locked_ood150/run_config.yaml"

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


# ==============================================================================
# STAGE 0: PREFLIGHT
# ==============================================================================
def run_stage_0_preflight() -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_0_PREFLIGHT"})

    # 1. Check no active Isaac OOD rollouts
    active_isaac = check_active_processes(["run_isaac_online_risk.py", "simvla_reaching_rollout.py"])
    if active_isaac:
        raise RuntimeError(f"Active Isaac rollout processes detected: {active_isaac}")

    # 2. Check HARD1000 status (paused at 249)
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

    # 3. Model & Normalization SHA256
    model_sha = sha256_f(MODEL_PATH)
    norm_sha = sha256_f(NORM_PATH)
    if model_sha != EXPECTED_MODEL_SHA:
        raise RuntimeError(f"Model SHA mismatch: {model_sha} != {EXPECTED_MODEL_SHA}")
    if norm_sha != EXPECTED_NORM_SHA:
        raise RuntimeError(f"Normalization SHA mismatch: {norm_sha} != {EXPECTED_NORM_SHA}")

    # 4. Locked OOD150 membership
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

    # Verify shadow gate output
    samples_file = SHADOW_GATE_DIR / "risk_receding_samples.jsonl"
    if not samples_file.exists():
        raise RuntimeError(f"Shadow gate failed: {samples_file} not created")

    rows = [json.loads(line) for line in samples_file.read_text().splitlines() if line.strip()]
    if not rows:
        raise RuntimeError("Shadow gate produced 0 rows")

    # Verify every row has 9 candidate scores and shadow mode executed candidate 0
    for r in rows:
        orisk = r.get("online_risk", {})
        cand_scores = orisk.get("candidate_scores")
        if not cand_scores or len(cand_scores) != 9:
            raise RuntimeError(f"Shadow row missing 9 candidate scores: {orisk}")
        # In shadow mode, executed action chunk must strictly equal candidate 0
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
# STAGE 4 & 5: LAUNCH DEFINITIVE ACTIVE OOD150 WITH 10-EPISODE HEALTH GATE
# ==============================================================================
def run_stage_4_launch_definitive() -> subprocess.Popen:
    log_event("STAGE_START", {"stage": "STAGE_4_LAUNCH_DEFINITIVE_OOD150"})

    DEFINITIVE_RUN_DIR.mkdir(parents=True, exist_ok=True)
    runner_script = PROTOCOL_DIR / "run_isaac_online_risk.py"

    cmd = [
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

    log_path = DEFINITIVE_RUN_DIR / "launch.log"
    log_file = open(log_path, "a")
    proc = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True)

    log_event("DEFINITIVE_RUN_LAUNCHED", {"pid": proc.pid, "log_path": str(log_path)})
    return proc


def audit_definitive_progress(target_episodes: int = 10) -> dict[str, Any]:
    samples_file = DEFINITIVE_RUN_DIR / "risk_receding_samples.jsonl"
    summaries_file = DEFINITIVE_RUN_DIR / "episode_summaries.jsonl"

    if not samples_file.exists() or not summaries_file.exists():
        return {"completed_episodes": 0, "rows": 0}

    summaries = [json.loads(l) for l in summaries_file.read_text().splitlines() if l.strip()]
    rows = [json.loads(l) for l in samples_file.read_text().splitlines() if l.strip()]

    completed_eps = len(summaries)
    unique_ids = set(s["source_episode_id"] for s in summaries)
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

        main_s = cand_scores[0]
        alt_scores = cand_scores[1:]
        best_alt_idx = int(np.argmin(alt_scores)) + 1
        best_alt_s = cand_scores[best_alt_idx]

        # Audit decision rule
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

        logged_sel_idx = orisk.get("selected_candidate_index", 0)
        logged_interv = orisk.get("is_intervention", False)

        if logged_sel_idx != expected_sel_idx or logged_interv != expected_interv:
            selection_mismatches += 1

        if logged_interv:
            replacements += 1
            ep_src_id = r.get("metadata", {}).get("source_episode_id")
            eps_with_repl.add(ep_src_id)
            cand_hist[logged_sel_idx] += 1

        # Audit execution action vs selected chunk
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


def run_stage_5_health_gate(proc: subprocess.Popen) -> bool:
    log_event("STAGE_START", {"stage": "STAGE_5_HEALTH_GATE_10EP"})
    print("Waiting for 10 completed episodes to run Stage 5 Health Gate...")

    while True:
        if proc.poll() is not None:
            # Process ended
            break
        audit = audit_definitive_progress()
        eps = audit["completed_episodes"]
        if eps >= 10:
            print(f"Reached {eps} completed episodes. Requesting clean stop after episode 10...")
            # Place STOP_AFTER_CURRENT_EPISODE
            (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").touch()
            # Wait for process to exit cleanly
            proc.wait(timeout=300)
            if (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").exists():
                (DEFINITIVE_RUN_DIR / "STOP_AFTER_CURRENT_EPISODE").unlink()
            break
        time.sleep(10)

    # Perform full 10-episode forensic audit
    audit = audit_definitive_progress()
    (PROTOCOL_DIR / "STAGE5_HEALTH_GATE_10EP.json").write_text(json.dumps(audit, indent=2))

    if audit["selection_mismatches"] > 0 or audit["execution_mismatches"] > 0:
        raise RuntimeError(f"Stage 5 Health Gate FAILED on mismatches: {audit}")

    if audit["accepted_replacements"] == 0:
        log_event("ZERO_INTERVENTION_HEALTH_GATE", audit)
        print("\n" + "=" * 80)
        print("STAGE 5 HEALTH GATE: ZERO INTERVENTIONS DETECTED AT 10 EPISODES.")
        print("Stopping safely as required by protocol for review.")
        print("=" * 80 + "\n")
        return False

    print("\n" + "=" * 80)
    print(f"STAGE 5 HEALTH GATE PASSED! {audit['accepted_replacements']} replacements across {audit['episodes_with_replacement']} episodes.")
    print("Resuming definitive run automatically from episode 11 to 150...")
    print("=" * 80 + "\n")
    log_event("STAGE_COMPLETE", {"stage": "STAGE_5_HEALTH_GATE_10EP", "result": audit})
    return True


# ==============================================================================
# STAGE 6: COMPLETE 150 EPISODES
# ==============================================================================
def run_stage_6_completion(proc: subprocess.Popen) -> dict[str, Any]:
    log_event("STAGE_START", {"stage": "STAGE_6_COMPLETE_150"})
    print("Running remaining episodes to complete full 150 OOD campaign...")

    proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"Definitive run exited with return code {proc.returncode}")

    audit = audit_definitive_progress()
    summaries_file = DEFINITIVE_RUN_DIR / "episode_summaries.jsonl"
    summaries = [json.loads(l) for l in summaries_file.read_text().splitlines() if l.strip()]

    if len(summaries) != 150:
        raise RuntimeError(f"Expected 150 completed episodes, got {len(summaries)}")

    new_successes = sum(1 for s in summaries if s.get("success", False))
    new_failures = 150 - new_successes
    historical_successes = 72
    historical_failures = 78

    # Paired comparison
    ood_hist_summaries = [
        json.loads(l)
        for l in (WORKSPACE / "outputs/final_locked_h10_ood150_seed20260728/episode_summaries.jsonl").read_text().splitlines()
        if l.strip()
    ]
    hist_by_src = {s["source_episode_id"]: s.get("success", False) for s in ood_hist_summaries}

    rescues = 0
    regressions = 0
    persisted_success = 0
    persisted_failure = 0

    for s in summaries:
        src_id = s["source_episode_id"]
        h_succ = hist_by_src.get(src_id, False)
        n_succ = s.get("success", False)
        if not h_succ and n_succ:
            rescues += 1
        elif h_succ and not n_succ:
            regressions += 1
        elif h_succ and n_succ:
            persisted_success += 1
        else:
            persisted_failure += 1

    comparison = {
        "total_episodes": 150,
        "historical_successes": historical_successes,
        "active_new_successes": new_successes,
        "success_delta_absolute": new_successes - historical_successes,
        "success_delta_percentage_points": (new_successes - historical_successes) / 150.0 * 100.0,
        "rescues_baseline_fail_to_new_succ": rescues,
        "regressions_baseline_succ_to_new_fail": regressions,
        "persisted_success": persisted_success,
        "persisted_failure": persisted_failure,
        "audit_metrics": audit,
    }

    (PROTOCOL_DIR / "STAGE6_COMPLETION.json").write_text(json.dumps(comparison, indent=2))
    (PROTOCOL_DIR / "FINAL_RESULT.json").write_text(json.dumps(comparison, indent=2))
    (PROTOCOL_DIR / "FINAL_PAIRED_COMPARISON.json").write_text(json.dumps(comparison, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_6_COMPLETE_150", "result": comparison})
    return comparison


# ==============================================================================
# STAGE 7: FINAL EVIDENCE FREEZE & GIT PUSH
# ==============================================================================
def run_stage_7_freeze_evidence() -> None:
    log_event("STAGE_START", {"stage": "STAGE_7_FINAL_EVIDENCE_FREEZE"})

    # Write summary markdown report
    res = json.loads((PROTOCOL_DIR / "FINAL_RESULT.json").read_text())
    report_md = f"""# Definitive Active Online OOD150 Result (Engineering Cap 0.90)

## Executive Summary
- **Protocol ID:** `isaac_ood150_definitive_active_cap090_v1`
- **Main Alarm Threshold ($A$):** `{FROZEN_A}` (Seen V1 `best_val_f1`)
- **Alternative Safe Cap ($C$):** `{FROZEN_C}` (Engineering operating point)
- **Minimum Delta ($M$):** `{FROZEN_M}`
- **Active Success Count:** **{res['active_new_successes']} / 150** ({res['active_new_successes']/150*100:.1f}%)
- **Historical Baseline Success Count:** **{res['historical_successes']} / 150** ({res['historical_successes']/150*100:.1f}%)
- **Net Absolute Delta:** **{res['success_delta_absolute']:+d} episodes** ({res['success_delta_percentage_points']:+.1f} percentage points)

## Paired Category Analysis
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

    # Generate SHA256 sums
    sha_txt = ""
    for f in sorted(PROTOCOL_DIR.glob("*.json")) + sorted(PROTOCOL_DIR.glob("*.md")) + sorted(PROTOCOL_DIR.glob("*.py")):
        if f.is_file() and not f.name.endswith("SHA256SUMS.txt"):
            sha_txt += f"{sha256_f(f)}  {f.name}\n"
    (PROTOCOL_DIR / "FINAL_SHA256SUMS.txt").write_text(sha_txt)

    log_event("STAGE_COMPLETE", {"stage": "STAGE_7_FINAL_EVIDENCE_FREEZE"})


# ==============================================================================
# STAGE 8: RESUME HARD1000
# ==============================================================================
def run_stage_8_resume_hard1000() -> None:
    log_event("STAGE_START", {"stage": "STAGE_8_RESUME_HARD1000"})
    print("Resuming HARD1000 campaign from episode 249...")

    stop_p1 = WORKSPACE / "automation/STOP_HARD1000_PIPELINE_AFTER_CURRENT_EPISODE"
    stop_p2 = HARD1000_DIR / "STOP_AFTER_CURRENT_EPISODE"
    if stop_p1.exists():
        stop_p1.unlink()
    if stop_p2.exists():
        stop_p2.unlink()

    hard1000_script = WORKSPACE / "automation/hard1000_pipeline.py"
    log_file = open(WORKSPACE / "logs/hard1000_pipeline.log", "a")
    proc = subprocess.Popen([MINICONDA_PYTHON, "-u", str(hard1000_script)], stdout=log_file, stderr=subprocess.STDOUT)
    time.sleep(5)

    hard_status = json.loads((HARD1000_DIR / "live_status.json").read_text())
    (PROTOCOL_DIR / "STAGE8_HARD1000_RESUMED.json").write_text(json.dumps(hard_status, indent=2))
    log_event("STAGE_COMPLETE", {"stage": "STAGE_8_RESUME_HARD1000", "status": hard_status, "pipeline_pid": proc.pid})


# ==============================================================================
# MAIN ORCHESTRATOR LOOP
# ==============================================================================
def main() -> None:
    PROTOCOL_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()

    print("\n" + "=" * 80)
    print("STARTING END-TO-END ORCHESTRATOR (Engineering Cap 0.90)")
    print(f"Current State: {state['current_stage']} (status: {state['status']})")
    print("=" * 80 + "\n")

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
        proc = run_stage_4_launch_definitive()
        state["definitive_pid"] = proc.pid
        state["status"] = "RUNNING_DEFINITIVE"
        save_state(state)

        # Stage 5: Health gate at 10 episodes
        health_passed = run_stage_5_health_gate(proc)
        state["health_gate_passed"] = health_passed
        if not health_passed:
            state["status"] = "STOPPED_AT_ZERO_INTERVENTION_HEALTH_GATE"
            save_state(state)
            return

        # Relaunch from episode 11 to 150
        proc2 = run_stage_4_launch_definitive()
        state["definitive_pid"] = proc2.pid
        state["current_stage"] = "STAGE_6_COMPLETE_150"
        save_state(state)

        # Stage 6
        run_stage_6_completion(proc2)
        state["current_stage"] = "STAGE_7_FINAL_EVIDENCE_FREEZE"
        save_state(state)

    # Stage 7
    if state["current_stage"] == "STAGE_7_FINAL_EVIDENCE_FREEZE":
        run_stage_7_freeze_evidence()
        state["current_stage"] = "STAGE_8_RESUME_HARD1000"
        save_state(state)

    # Stage 8
    if state["current_stage"] == "STAGE_8_RESUME_HARD1000":
        run_stage_8_resume_hard1000()
        state["current_stage"] = "COMPLETE"
        state["status"] = "ALL_STAGES_COMPLETE"
        save_state(state)

    print("\n" + "=" * 80)
    print("ALL ORCHESTRATOR STAGES COMPLETED SUCCESSFULLY!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
