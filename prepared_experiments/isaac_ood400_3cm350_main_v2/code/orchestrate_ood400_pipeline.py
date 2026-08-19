#!/usr/bin/env python3
"""Master OOD400 Pipeline Orchestrator (Hardened TMUX & Persistence V3).

State Machine:
  WAIT_BASELINE
  -> FINAL_BASELINE_AUDIT
  -> FREEZE_BASELINE_DATASET
  -> OFFLINE_RISK_EVAL
  -> BASELINE_VIDEO_BUILD
  -> SELECT_ONLINE_A
  -> FREEZE_CONTROLLER
  -> ACTIVE_SMOKE
  -> ACTIVE400_RUN
  -> FINAL_ACTIVE_AUDIT
  -> ACTIVE_VIDEO_BUILD
  -> PAIRED_COMPARISON
  -> PAPER_EVIDENCE_PACKAGE
  -> EXPERIMENT_MAP_SYNC
  -> PUBLICATION_SYNC
  -> COMPLETE
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback
from typing import Any

import numpy as np

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import sha256_file
from audit_freeze_ood400_baseline import audit_baseline_run, freeze_baseline_dataset
from offline_eval_ood400 import run_offline_evaluation
from build_ood400_review_video import build_review_videos
from select_ood400_online_threshold import select_online_threshold
from prepare_ood400_topk import prepare_topk_controller
from audit_ood400_active import audit_active_run
from sync_ood400_evidence import sync_evidence

ISAAC_PY = Path(os.environ.get("ISAAC_PYTHON", "/mnt/ai/isaac/envs/env_isaaclab_6_0/bin/python"))


def find_matching_runner(
    *,
    output_dir: Path,
    mode: str,
    manifest_path: Path,
    exclude_pid: int | None = None,
) -> list[int]:
    """Find running Isaac runner processes matching exact command line arguments."""
    output_dir_str = str(Path(output_dir).resolve())
    manifest_str = str(Path(manifest_path).resolve())
    matched_pids = []

    proc_dir = Path("/proc")
    if not proc_dir.exists():
        return []

    for p in proc_dir.iterdir():
        if p.is_dir() and p.name.isdigit():
            pid = int(p.name)
            if exclude_pid and pid == exclude_pid:
                continue
            cmdline_p = p / "cmdline"
            if not cmdline_p.exists():
                continue
            try:
                cmdline = cmdline_p.read_bytes().replace(b"\x00", b" ").decode("utf-8", errors="ignore")
            except (IOError, PermissionError):
                continue

            if "run_ood400_simvla.py" in cmdline:
                if f"--output-dir {output_dir_str}" in cmdline or f"--output-dir={output_dir_str}" in cmdline:
                    if f"--mode {mode}" in cmdline or f"--mode={mode}" in cmdline:
                        if manifest_str in cmdline:
                            matched_pids.append(pid)

    return matched_pids


class OOD400Orchestrator:
    def __init__(self, exp_dir: Path) -> None:
        self.exp_dir = Path(exp_dir).resolve()
        self.code_dir = self.exp_dir / "code"
        self.orch_dir = self.exp_dir / "orchestrator"
        self.orch_dir.mkdir(parents=True, exist_ok=True)

        self.state_path = self.orch_dir / "PIPELINE_STATE.json"
        self.events_path = self.orch_dir / "PIPELINE_EVENTS.jsonl"
        self.lock_path = self.orch_dir / "OOD400_PIPELINE_LOCK.json"
        self.complete_path = self.orch_dir / "PIPELINE_COMPLETE.json"
        self.failure_path = self.orch_dir / "PIPELINE_FAILURE.json"

        # Canonical paths
        self.manifest_path = WORKSPACE / "benchmarks/reaching_mimic_risk_ood400/full_ood400.json"
        self.model_path = WORKSPACE / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/model.pt"
        self.norm_path = WORKSPACE / "models/isaac_seen4904_h10_topk8_temporal_3cm350_main_v2/norm.npz"
        self.run_config_path = WORKSPACE / "configs/collect_reaching_pose_v1_simvla_ood400_3cm350_baseline_v1.yaml"
        self.runner_script = self.code_dir / "run_ood400_simvla.py"
        self.runtime_script = self.code_dir / "ood400_runtime.py"

        self.baseline_output_dir = WORKSPACE / "outputs/isaac_ood400_simvla_baseline_3cm350_v2"
        self.baseline_frozen_dir = WORKSPACE / "frozen_datasets/isaac_ood400_simvla_baseline_3cm350_v2"
        self.baseline_evidence_dir = self.exp_dir / "baseline"
        self.offline_evidence_dir = self.exp_dir / "offline_eval"
        self.active_evidence_dir = self.exp_dir / "active_eval"

        self.expected_hashes = {
            "manifest_sha256": "264dae5a7de872e5aee0a9554f88adfe7af3d38b5a7e29fd7f9b3e0d1c10da41",
            "runner_sha256": "a383960df348dc04b677c8cfd1c6984cacf7a1ddf50dc99a825ba6a73deea6d8",
            "runtime_sha256": "eee913f5137d46783bc5854bbaad55661a739b5b407aedd98c186bd48437b9fb",
            "model_sha256": "00ad096a9ca38577366e992e1d7f8aa25b6f56f2f2bd7354abce1790baf890f1",
            "norm_sha256": "6fbd2b221c4490c975e3e1492c96a9e879a586f0b3a4c4eaf97ea05920960341",
        }

        self._lock_file: Any = None

    def acquire_lock(self) -> None:
        self._lock_file = (self.orch_dir / "orchestrator.lock").open("w")
        try:
            fcntl.flock(self._lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (BlockingIOError, IOError):
            print("Another orchestrator instance holds the lock; exiting.", file=sys.stderr)
            sys.exit(0)

        lock_data = {
            "pid": os.getpid(),
            "start_time": datetime.now(timezone.utc).isoformat(),
            "exp_dir": str(self.exp_dir),
            "locked_hashes": self.expected_hashes,
        }
        self.lock_path.write_text(json.dumps(lock_data, indent=2) + "\n")

    def verify_recovery_hashes(self) -> None:
        current_hashes = {
            "manifest_sha256": sha256_file(self.manifest_path),
            "runner_sha256": sha256_file(self.runner_script),
            "runtime_sha256": sha256_file(self.runtime_script),
            "model_sha256": sha256_file(self.model_path),
            "norm_sha256": sha256_file(self.norm_path),
        }
        for k, expected_v in self.expected_hashes.items():
            if current_hashes[k] != expected_v:
                raise RuntimeError(f"Recovery hash gate failure for {k}: expected {expected_v}, got {current_hashes[k]}")

    def log_event(self, event_type: str, details: dict[str, Any]) -> None:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "details": details,
        }
        with self.events_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")
            f.flush()
        print(f"[{payload['timestamp']}] EVENT: {event_type} | {details}", flush=True)

    def load_state(self) -> str:
        if self.state_path.exists():
            data = json.loads(self.state_path.read_text(encoding="utf-8"))
            return str(data.get("state", "WAIT_BASELINE"))
        return "WAIT_BASELINE"

    def set_state(self, state: str, metadata: dict[str, Any] | None = None) -> None:
        payload = {
            "state": state,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "metadata": metadata or {},
        }
        temp_p = self.orch_dir / "PIPELINE_STATE.json.tmp"
        temp_p.write_text(json.dumps(payload, indent=2) + "\n")
        temp_p.replace(self.state_path)
        self.log_event("STATE_TRANSITION", {"new_state": state, "metadata": metadata})

    def is_episode_complete(self, ep_id: str, out_dir: Path) -> bool:
        ep_dir = out_dir / "episodes" / ep_id
        summary_p = ep_dir / "summary.json"
        decisions_p = ep_dir / "decisions.jsonl"
        vid_p = out_dir / "videos" / f"{ep_id}.mp4"

        if not summary_p.exists() or not decisions_p.exists() or not vid_p.exists():
            return False
        if vid_p.stat().st_size < 1000:
            return False
        try:
            json.loads(summary_p.read_text(encoding="utf-8"))
            return True
        except Exception:
            return False

    def count_completed_episodes(self, out_dir: Path) -> set[str]:
        episodes_dir = out_dir / "episodes"
        if not episodes_dir.exists():
            return set()
        completed = set()
        for p in episodes_dir.iterdir():
            if p.is_dir() and self.is_episode_complete(p.name, out_dir):
                completed.add(p.name)
        return completed

    def run_stage_wait_baseline(self) -> None:
        print("=== STAGE: WAIT_BASELINE ===", flush=True)
        retries = 0
        while True:
            completed_set = self.count_completed_episodes(self.baseline_output_dir)
            completed_cnt = len(completed_set)
            print(f"[WAIT_BASELINE] Completed {completed_cnt}/400 verified episodes in {self.baseline_output_dir}", flush=True)

            if completed_cnt >= 400:
                print("All 400 baseline episodes verified complete!", flush=True)
                break

            # Exact process liveness check
            pids = find_matching_runner(
                output_dir=self.baseline_output_dir,
                mode="baseline",
                manifest_path=self.manifest_path,
                exclude_pid=os.getpid(),
            )

            if not pids:
                print(f"[WAIT_BASELINE] Baseline process died at {completed_cnt}/400 episodes. Initiating recovery in TMUX...", flush=True)
                self.verify_recovery_hashes()
                if retries >= 2:
                    raise RuntimeError(f"Baseline collection died twice before completion. Completed: {completed_cnt}/400")
                retries += 1
                self.log_event("BASELINE_CRASH_RECOVERY", {"completed_before_recovery": completed_cnt, "attempt": retries})

                recovery_log_p = self.orch_dir / "BASELINE_RECOVERY.log"
                recovery_cmd = (
                    f"cd {WORKSPACE} && export PYTHONPATH={WORKSPACE}:{WORKSPACE}/src:{self.code_dir} && "
                    f"'{ISAAC_PY}' '{self.runner_script}' "
                    f"--run-config '{self.run_config_path}' "
                    f"--manifest '{self.manifest_path}' "
                    f"--output-dir '{self.baseline_output_dir}' "
                    f"--mode baseline --offset 0 --count 400 --execution-mode chunk_h10 "
                    f"--risk-model-path '{self.model_path}' "
                    f"--risk-normalization '{self.norm_path}' --headless "
                    f">> '{recovery_log_p}' 2>&1"
                )

                # Kill stale session if exists
                subprocess.run(["tmux", "kill-session", "-t", "ood400_baseline_resume"], capture_output=True)
                subprocess.run(["tmux", "new-session", "-d", "-s", "ood400_baseline_resume", recovery_cmd], check=True)
                subprocess.run(["tmux", "set-option", "-t", "ood400_baseline_resume", "remain-on-exit", "on"], check=True)
                time.sleep(10)
            else:
                time.sleep(60)

        self.set_state("FINAL_BASELINE_AUDIT")

    def run_stage_final_baseline_audit(self) -> None:
        print("=== STAGE: FINAL_BASELINE_AUDIT ===", flush=True)
        res = audit_baseline_run(
            output_dir=self.baseline_output_dir,
            manifest_path=self.manifest_path,
            evidence_dir=self.baseline_evidence_dir,
        )
        self.set_state("FREEZE_BASELINE_DATASET", {"baseline_audit": res})

    def run_stage_freeze_baseline_dataset(self) -> None:
        print("=== STAGE: FREEZE_BASELINE_DATASET ===", flush=True)
        manifest_audit = freeze_baseline_dataset(
            output_dir=self.baseline_output_dir,
            frozen_dir=self.baseline_frozen_dir,
            manifest_path=self.manifest_path,
        )
        self.set_state("OFFLINE_RISK_EVAL", {"frozen_manifest": manifest_audit})

    def run_stage_offline_risk_eval(self) -> None:
        print("=== STAGE: OFFLINE_RISK_EVAL ===", flush=True)
        metrics = run_offline_evaluation(
            frozen_dir=self.baseline_frozen_dir,
            model_path=self.model_path,
            norm_path=self.norm_path,
            output_dir=self.offline_evidence_dir,
            device_str="cuda:0",
        )
        self.set_state("BASELINE_VIDEO_BUILD", {"metrics": metrics})

    def run_stage_baseline_video_build(self) -> None:
        print("=== STAGE: BASELINE_VIDEO_BUILD ===", flush=True)
        vid_manifest = build_review_videos(
            episodes_summary_path=self.baseline_output_dir / "canonical_episode_summaries.jsonl",
            videos_dir=self.baseline_output_dir / "videos",
            output_dir=self.baseline_evidence_dir,
            mode="baseline",
            decisions_jsonl_path=self.baseline_output_dir / "canonical_decisions.jsonl",
        )
        self.set_state("SELECT_ONLINE_A", {"video_manifest": vid_manifest})

    def run_stage_select_online_a(self) -> None:
        print("=== STAGE: SELECT_ONLINE_A ===", flush=True)
        sel = select_online_threshold(
            sweep_json_path=self.offline_evidence_dir / "OOD400_THRESHOLD_SWEEP.json",
            output_path=self.offline_evidence_dir / "ONLINE_A_SELECTION.json",
        )
        self.set_state("FREEZE_CONTROLLER", {"selection": sel})

    def run_stage_freeze_controller(self) -> None:
        print("=== STAGE: FREEZE_CONTROLLER ===", flush=True)
        sel = json.loads((self.offline_evidence_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
        a_rule = str(sel["selected_rule_name"])
        rule_slug = a_rule.replace(" ", "_")
        active_output_dir = WORKSPACE / f"online_evals/isaac_ood400_topk_main_v2_{rule_slug}_C090_v1"

        controller_spec = prepare_topk_controller(
            selection_json_path=self.offline_evidence_dir / "ONLINE_A_SELECTION.json",
            baseline_decisions_path=self.baseline_output_dir / "canonical_decisions.jsonl",
            output_dir=self.active_evidence_dir,
            model_path=self.model_path,
            norm_path=self.norm_path,
            manifest_path=self.manifest_path,
            runner_path=self.runner_script,
            runtime_path=self.runtime_script,
            active_output_dir=active_output_dir,
        )
        self.set_state("ACTIVE_SMOKE", {"controller_spec": controller_spec, "active_output_dir": str(active_output_dir)})

    def run_stage_active_smoke(self) -> None:
        print("=== STAGE: ACTIVE_SMOKE ===", flush=True)
        smoke_dir = WORKSPACE / "smokes/ood400_active_smoke3"
        if smoke_dir.exists():
            shutil.rmtree(smoke_dir)
        smoke_dir.mkdir(parents=True, exist_ok=True)

        sel = json.loads((self.offline_evidence_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
        a_val = float(sel["selected_threshold_a"])
        a_rule = str(sel["selected_rule_name"])

        cmd = [
            str(ISAAC_PY),
            str(self.runner_script),
            "--run-config", str(self.run_config_path),
            "--manifest", str(self.manifest_path),
            "--output-dir", str(smoke_dir),
            "--mode", "online",
            "--offset", "0",
            "--count", "3",
            "--execution-mode", "chunk_h10",
            "--risk-model-path", str(self.model_path),
            "--risk-normalization", str(self.norm_path),
            "--main-threshold", str(a_val),
            "--main-threshold-name", a_rule,
            "--selected-cap", "0.90",
            "--headless",
        ]
        env = {**os.environ, "PYTHONPATH": f"{WORKSPACE}:{WORKSPACE}/src:{self.code_dir}"}
        subprocess.run(cmd, env=env, check=True)

        # Full smoke decision audit
        smoke_summaries = [json.loads(l) for l in (smoke_dir / "episode_summaries.jsonl").read_text().splitlines() if l.strip()]
        smoke_decisions = [json.loads(l) for l in (smoke_dir / "decisions.jsonl").read_text().splitlines() if l.strip()]

        if len(smoke_summaries) != 3:
            raise RuntimeError(f"Active smoke failed: expected 3 summaries, got {len(smoke_summaries)}")

        for d in smoke_decisions:
            scores = [float(s) for s in d["online_risk"]["candidate_scores"]]
            main_s = scores[0]
            alt_scores = scores[1:]
            best_alt_idx = 1 + int(np.argmin(alt_scores))
            best_alt_s = scores[best_alt_idx]

            if main_s < a_val:
                exp_idx = 0
            elif best_alt_s >= main_s:
                exp_idx = 0
            elif best_alt_s > 0.90:
                exp_idx = 0
            else:
                exp_idx = best_alt_idx

            act_idx = int(d.get("executed_candidate_index", d["online_risk"]["selected_candidate_index"]))
            if act_idx != exp_idx:
                raise RuntimeError(f"Active smoke selection mismatch: expected {exp_idx}, got {act_idx}")

            seq = np.asarray(d["executed_action_sequence"], dtype=np.float32)
            if act_idx == 0:
                expected_chunk = np.asarray(d["main_candidate_action_chunk_env"], dtype=np.float32)
            else:
                expected_chunk = np.asarray(d["ace_candidate_chunks_env"][act_idx - 1], dtype=np.float32)

            diff = float(np.max(np.abs(seq - expected_chunk[:len(seq)])))
            if diff > 1e-6:
                raise RuntimeError(f"Active smoke execution action mismatch: max diff = {diff}")

        print("Active 3-episode smoke fully audited and PASSED!", flush=True)
        self.set_state("ACTIVE400_RUN")

    def run_stage_active400_run(self) -> None:
        print("=== STAGE: ACTIVE400_RUN ===", flush=True)
        state_data = json.loads(self.state_path.read_text(encoding="utf-8"))
        sel = json.loads((self.offline_evidence_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
        a_val = float(sel["selected_threshold_a"])
        a_rule = str(sel["selected_rule_name"])
        rule_slug = a_rule.replace(" ", "_")

        active_output_dir = Path(state_data.get("metadata", {}).get("active_output_dir", WORKSPACE / f"online_evals/isaac_ood400_topk_main_v2_{rule_slug}_C090_v1"))
        active_output_dir.mkdir(parents=True, exist_ok=True)
        active_log_p = self.orch_dir / "ACTIVE400.log"

        retries = 0
        while True:
            completed_set = self.count_completed_episodes(active_output_dir)
            completed_cnt = len(completed_set)
            print(f"[ACTIVE400_RUN] Progress: {completed_cnt}/400 verified episodes in {active_output_dir}", flush=True)

            if completed_cnt >= 400:
                print("All 400 active episodes completed!", flush=True)
                break

            pids = find_matching_runner(
                output_dir=active_output_dir,
                mode="online",
                manifest_path=self.manifest_path,
                exclude_pid=os.getpid(),
            )

            if not pids:
                self.verify_recovery_hashes()
                if retries >= 2:
                    raise RuntimeError(f"Active run died twice before completion. Completed: {completed_cnt}/400")
                retries += 1
                self.log_event("ACTIVE_CRASH_RECOVERY", {"completed": completed_cnt, "attempt": retries})

                active_cmd = (
                    f"cd {WORKSPACE} && export PYTHONPATH={WORKSPACE}:{WORKSPACE}/src:{self.code_dir} && "
                    f"'{ISAAC_PY}' '{self.runner_script}' "
                    f"--run-config '{self.run_config_path}' "
                    f"--manifest '{self.manifest_path}' "
                    f"--output-dir '{active_output_dir}' "
                    f"--mode online --offset 0 --count 400 --execution-mode chunk_h10 "
                    f"--risk-model-path '{self.model_path}' "
                    f"--risk-normalization '{self.norm_path}' "
                    f"--main-threshold '{a_val}' --main-threshold-name '{a_rule}' --selected-cap 0.90 --headless "
                    f">> '{active_log_p}' 2>&1"
                )

                subprocess.run(["tmux", "kill-session", "-t", "ood400_topk_active"], capture_output=True)
                subprocess.run(["tmux", "new-session", "-d", "-s", "ood400_topk_active", active_cmd], check=True)
                subprocess.run(["tmux", "set-option", "-t", "ood400_topk_active", "remain-on-exit", "on"], check=True)
                time.sleep(10)
            else:
                time.sleep(60)

        self.set_state("FINAL_ACTIVE_AUDIT", {"active_output_dir": str(active_output_dir)})

    def run_stage_final_active_audit(self) -> None:
        print("=== STAGE: FINAL_ACTIVE_AUDIT ===", flush=True)
        state_data = json.loads(self.state_path.read_text(encoding="utf-8"))
        active_output_dir = Path(state_data["metadata"]["active_output_dir"])

        paired_res = audit_active_run(
            active_output_dir=active_output_dir,
            baseline_output_dir=self.baseline_output_dir,
            manifest_path=self.manifest_path,
            controller_json_path=self.active_evidence_dir / "FROZEN_CONTROLLER.json",
            evidence_dir=self.active_evidence_dir,
        )
        self.set_state("ACTIVE_VIDEO_BUILD", {"paired_res": paired_res, "active_output_dir": str(active_output_dir)})

    def run_stage_active_video_build(self) -> None:
        print("=== STAGE: ACTIVE_VIDEO_BUILD ===", flush=True)
        state_data = json.loads(self.state_path.read_text(encoding="utf-8"))
        active_output_dir = Path(state_data["metadata"]["active_output_dir"])

        vid_manifest = build_review_videos(
            episodes_summary_path=active_output_dir / "canonical_episode_summaries.jsonl",
            videos_dir=active_output_dir / "videos",
            output_dir=self.active_evidence_dir,
            mode="topk",
            decisions_jsonl_path=active_output_dir / "canonical_decisions.jsonl",
            controller_info=json.loads((self.active_evidence_dir / "FROZEN_CONTROLLER.json").read_text(encoding="utf-8")),
        )
        self.set_state("PAIRED_COMPARISON", {"active_video_manifest": vid_manifest})

    def run_stage_paired_comparison(self) -> None:
        print("=== STAGE: PAIRED_COMPARISON ===", flush=True)
        if not (self.active_evidence_dir / "PAIRED_COMPARISON.json").exists():
            raise FileNotFoundError("PAIRED_COMPARISON.json missing")
        self.set_state("PAPER_EVIDENCE_PACKAGE")

    def run_stage_paper_evidence_package(self) -> None:
        print("=== STAGE: PAPER_EVIDENCE_PACKAGE ===", flush=True)
        index_json = sync_evidence(exp_dir=self.exp_dir)
        self.set_state("EXPERIMENT_MAP_SYNC", {"index_json": index_json})

    def run_stage_experiment_map_sync(self) -> None:
        print("=== STAGE: EXPERIMENT_MAP_SYNC ===", flush=True)
        self.set_state("PUBLICATION_SYNC")

    def run_stage_publication_sync(self) -> None:
        print("=== STAGE: PUBLICATION_SYNC ===", flush=True)
        sync_evidence(exp_dir=self.exp_dir, publication_repo=Path("/home/redafrix/tests/u_vowel_publication_clean"))
        self.set_state("COMPLETE")

    def run_pipeline(self) -> None:
        self.acquire_lock()
        print(f"=== OOD400 Orchestrator started (PID: {os.getpid()}) ===", flush=True)

        stages = {
            "WAIT_BASELINE": self.run_stage_wait_baseline,
            "FINAL_BASELINE_AUDIT": self.run_stage_final_baseline_audit,
            "FREEZE_BASELINE_DATASET": self.run_stage_freeze_baseline_dataset,
            "OFFLINE_RISK_EVAL": self.run_stage_offline_risk_eval,
            "BASELINE_VIDEO_BUILD": self.run_stage_baseline_video_build,
            "SELECT_ONLINE_A": self.run_stage_select_online_a,
            "FREEZE_CONTROLLER": self.run_stage_freeze_controller,
            "ACTIVE_SMOKE": self.run_stage_active_smoke,
            "ACTIVE400_RUN": self.run_stage_active400_run,
            "FINAL_ACTIVE_AUDIT": self.run_stage_final_active_audit,
            "ACTIVE_VIDEO_BUILD": self.run_stage_active_video_build,
            "PAIRED_COMPARISON": self.run_stage_paired_comparison,
            "PAPER_EVIDENCE_PACKAGE": self.run_stage_paper_evidence_package,
            "EXPERIMENT_MAP_SYNC": self.run_stage_experiment_map_sync,
            "PUBLICATION_SYNC": self.run_stage_publication_sync,
        }

        try:
            while True:
                current_state = self.load_state()
                if current_state == "COMPLETE":
                    print("=== OOD400 Pipeline COMPLETE! ===", flush=True)
                    self.complete_path.write_text(json.dumps({
                        "status": "COMPLETE",
                        "completed_at": datetime.now(timezone.utc).isoformat(),
                    }, indent=2) + "\n")
                    break

                if current_state not in stages:
                    raise KeyError(f"Unknown pipeline state {current_state!r}")

                stage_fn = stages[current_state]
                stage_fn()

        except BaseException as e:
            traceback.print_exc()
            self.failure_path.write_text(json.dumps({
                "status": "FAILED",
                "failed_state": self.load_state(),
                "error": str(e),
                "traceback": traceback.format_exc(),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }, indent=2) + "\n")
            raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp-dir", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()

    orchestrator = OOD400Orchestrator(args.exp_dir)
    orchestrator.run_pipeline()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
