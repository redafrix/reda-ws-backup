#!/usr/bin/env python3
"""Master OOD400 Pipeline Orchestrator.

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
import subprocess
import sys
import time
import traceback
from typing import Any

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
        }
        self.lock_path.write_text(json.dumps(lock_data, indent=2) + "\n")

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

    def count_completed_baseline(self) -> set[str]:
        episodes_dir = self.baseline_output_dir / "episodes"
        if not episodes_dir.exists():
            return set()
        completed = set()
        for p in episodes_dir.iterdir():
            if p.is_dir() and (p / "summary.json").exists():
                completed.add(p.name)
        return completed

    def run_stage_wait_baseline(self) -> None:
        print("=== STAGE: WAIT_BASELINE ===", flush=True)
        retries = 0
        while True:
            completed_set = self.count_completed_baseline()
            completed_cnt = len(completed_set)
            print(f"[WAIT_BASELINE] Completed {completed_cnt}/400 episodes in {self.baseline_output_dir}", flush=True)

            if completed_cnt >= 400:
                print("All 400 baseline episodes detected!", flush=True)
                break

            # Check process liveness
            res = subprocess.run(["pgrep", "-f", "run_ood400_simvla.py"], capture_output=True, text=True)
            pids = [p.strip() for p in res.stdout.splitlines() if p.strip() and int(p.strip()) != os.getpid()]

            if not pids:
                print(f"[WAIT_BASELINE] Baseline process died at {completed_cnt}/400 episodes. Initiating recovery...", flush=True)
                if retries >= 2:
                    raise RuntimeError(f"Baseline collection died twice before completion. Completed: {completed_cnt}/400")
                retries += 1
                self.log_event("BASELINE_CRASH_RECOVERY", {"completed_before_recovery": completed_cnt, "attempt": retries})

                # Launch recovery for remaining episodes
                cmd = [
                    str(ISAAC_PY),
                    str(self.runner_script),
                    "--run-config", str(self.run_config_path),
                    "--manifest", str(self.manifest_path),
                    "--output-dir", str(self.baseline_output_dir),
                    "--mode", "baseline",
                    "--offset", "0",
                    "--count", "400",
                    "--execution-mode", "chunk_h10",
                    "--risk-model-path", str(self.model_path),
                    "--risk-normalization", str(self.norm_path),
                    "--headless",
                ]
                env = {**os.environ, "PYTHONPATH": f"{WORKSPACE}:{WORKSPACE}/src:{self.code_dir}"}
                subprocess.Popen(cmd, env=env)
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
        from prepare_ood400_topk import prepare_topk_controller
        controller_spec = prepare_topk_controller(
            selection_json_path=self.offline_evidence_dir / "ONLINE_A_SELECTION.json",
            baseline_decisions_path=self.baseline_output_dir / "canonical_decisions.jsonl",
            output_dir=self.active_evidence_dir,
            model_path=self.model_path,
            norm_path=self.norm_path,
            manifest_path=self.manifest_path,
            runner_path=self.runner_script,
            runtime_path=self.runtime_script,
        )
        self.set_state("ACTIVE_SMOKE", {"controller_spec": controller_spec})

    def run_stage_active_smoke(self) -> None:
        print("=== STAGE: ACTIVE_SMOKE ===", flush=True)
        smoke_dir = WORKSPACE / "smokes/ood400_active_smoke3"
        if smoke_dir.exists():
            import shutil
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

        # Audit smoke
        smoke_summaries = [json.loads(l) for l in (smoke_dir / "episode_summaries.jsonl").read_text().splitlines() if l.strip()]
        if len(smoke_summaries) != 3:
            raise RuntimeError(f"Active smoke failed: expected 3 summaries, got {len(smoke_summaries)}")

        print("Active 3-episode smoke PASSED!", flush=True)
        self.set_state("ACTIVE400_RUN")

    def run_stage_active400_run(self) -> None:
        print("=== STAGE: ACTIVE400_RUN ===", flush=True)
        sel = json.loads((self.offline_evidence_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
        a_val = float(sel["selected_threshold_a"])
        a_rule = str(sel["selected_rule_name"])
        rule_slug = a_rule.replace(" ", "_")

        active_output_dir = WORKSPACE / f"online_evals/isaac_ood400_topk_main_v2_{rule_slug}_C090_v1"
        active_output_dir.mkdir(parents=True, exist_ok=True)

        retries = 0
        while True:
            episodes_dir = active_output_dir / "episodes"
            completed_cnt = len(list(episodes_dir.glob("*/summary.json"))) if episodes_dir.exists() else 0
            print(f"[ACTIVE400_RUN] Progress: {completed_cnt}/400 episodes in {active_output_dir}", flush=True)

            if completed_cnt >= 400:
                print("All 400 active episodes completed!", flush=True)
                break

            # Check if runner is alive
            res = subprocess.run(["pgrep", "-f", "run_ood400_simvla.py"], capture_output=True, text=True)
            pids = [p.strip() for p in res.stdout.splitlines() if p.strip() and int(p.strip()) != os.getpid()]

            if not pids:
                if retries >= 2:
                    raise RuntimeError(f"Active run died twice before completion. Completed: {completed_cnt}/400")
                retries += 1
                self.log_event("ACTIVE_CRASH_RECOVERY", {"completed": completed_cnt, "attempt": retries})

                cmd = [
                    str(ISAAC_PY),
                    str(self.runner_script),
                    "--run-config", str(self.run_config_path),
                    "--manifest", str(self.manifest_path),
                    "--output-dir", str(active_output_dir),
                    "--mode", "online",
                    "--offset", "0",
                    "--count", "400",
                    "--execution-mode", "chunk_h10",
                    "--risk-model-path", str(self.model_path),
                    "--risk-normalization", str(self.norm_path),
                    "--main-threshold", str(a_val),
                    "--main-threshold-name", a_rule,
                    "--selected-cap", "0.90",
                    "--headless",
                ]
                env = {**os.environ, "PYTHONPATH": f"{WORKSPACE}:{WORKSPACE}/src:{self.code_dir}"}
                subprocess.Popen(cmd, env=env)
                time.sleep(10)
            else:
                time.sleep(60)

        self.set_state("FINAL_ACTIVE_AUDIT", {"active_output_dir": str(active_output_dir)})

    def run_stage_final_active_audit(self) -> None:
        print("=== STAGE: FINAL_ACTIVE_AUDIT ===", flush=True)
        state_data = json.loads(self.state_path.read_text(encoding="utf-8"))
        sel = json.loads((self.offline_evidence_dir / "ONLINE_A_SELECTION.json").read_text(encoding="utf-8"))
        rule_slug = sel["selected_rule_name"].replace(" ", "_")
        active_output_dir = Path(state_data.get("metadata", {}).get("active_output_dir", WORKSPACE / f"online_evals/isaac_ood400_topk_main_v2_{rule_slug}_C090_v1"))

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
        )
        self.set_state("PAIRED_COMPARISON", {"active_video_manifest": vid_manifest})

    def run_stage_paired_comparison(self) -> None:
        print("=== STAGE: PAIRED_COMPARISON ===", flush=True)
        # Already computed in audit_active_run, verify existence
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
