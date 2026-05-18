#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import time
from datetime import datetime, timedelta
from pathlib import Path
from statistics import mean
from typing import Any

BOB_ROOT = Path("/media/rootalkhatib/My Passport/reda_ws")
SAM_ROOT = Path("/home/rootalkhatib/test/reda_ws")
REL = Path("asynchvla_ws/stage8_ultimate")
MANIFEST = BOB_ROOT / REL / "configs/stage8_job_manifest.json"
WATCHDOG_LOG = BOB_ROOT / REL / "logs/stage8_watchdog.log"
DASHBOARD = BOB_ROOT / REL / "reports/stage8_live_dashboard.md"
LOCAL_STAGE8 = Path("/home/redafrix/tests/internship/codex_reports/stage8")


def now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def run(cmd: list[str], cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)


def shell(cmd: str, cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess:
    return run(["bash", "-lc", cmd], cwd=cwd, timeout=timeout)


def manager(*args: str, timeout: int | None = 120) -> subprocess.CompletedProcess:
    return run(["python3", "asynchvla_ws/scripts/stage8_job_manager.py", *args], cwd=BOB_ROOT, timeout=timeout)


def load_manifest() -> dict[str, Any]:
    return json.loads(MANIFEST.read_text())


def save_manifest(man: dict[str, Any]) -> None:
    MANIFEST.write_text(json.dumps(man, indent=2, sort_keys=True) + "\n")


def root_for(machine: str) -> Path:
    return BOB_ROOT if machine == "bob" else SAM_ROOT


def make_job(job_id: str, machine: str, priority: int, command: str, *, gpu: bool = False,
             deps: list[str] | None = None, retries: int = 1, expected: list[str] | None = None,
             hours: float = 6.0) -> dict[str, Any]:
    base = root_for(machine) / REL
    return {
        "job_id": job_id,
        "machine": machine,
        "priority": priority,
        "command": command,
        "command_file": str(base / "jobs" / f"{job_id}.sh"),
        "expected_outputs": expected or [],
        "log_path": str(base / "logs" / f"{job_id}.log"),
        "status_path": str(base / "status" / f"{job_id}.json"),
        "max_retries": retries,
        "dependencies": deps or [],
        "smoke_command": None,
        "timeout_hours": hours,
        "gpu_required": gpu,
    }


def add_jobs(jobs: list[dict[str, Any]], reason: str) -> list[str]:
    man = load_manifest()
    by_id = {j["job_id"]: j for j in man["jobs"]}
    added = []
    for job in jobs:
        if job["job_id"] in by_id:
            continue
        job["added_by_watchdog_reason"] = reason
        by_id[job["job_id"]] = job
        added.append(job["job_id"])
    if added:
        man["jobs"] = sorted(by_id.values(), key=lambda j: (j.get("priority", 999), j["job_id"]))
        man["updated_at"] = now()
        man.setdefault("watchdog_added_jobs", []).extend({"job_id": j, "reason": reason, "time": now()} for j in added)
        save_manifest(man)
    return added


def status_rows() -> list[dict[str, Any]]:
    cp = manager("status", timeout=180)
    if cp.returncode != 0:
        return [{"job_id": "status_error", "machine": "bob", "state": "FAILED", "error": cp.stdout[-2000:]}]
    return json.loads(cp.stdout)


def machine_gpu(machine: str) -> str:
    if machine == "bob":
        cp = shell("nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv,noheader 2>/dev/null || true", timeout=10)
    else:
        cp = run(["ssh", "-o", "BatchMode=yes", "sam", "nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv,noheader 2>/dev/null || true"], timeout=20)
    return cp.stdout.strip().replace("\n", "; ") or "unknown"


def parse_best_rollout() -> tuple[str, str]:
    reports = [
        BOB_ROOT / REL / "reports/stage8_libero_pro_expanded_rollout_results.md",
        BOB_ROOT / REL / "reports/stage8_libero_pro_pilot_results.md",
        BOB_ROOT / REL / "reports/stage8_normal_libero_hard_task_results.md",
        BOB_ROOT / REL / "reports/stage8_normal_libero_hard_task_baseline.md",
    ]
    best_lp = "not available"
    best_hard = "not available"
    for p in reports:
        if not p.exists():
            continue
        txt = p.read_text(errors="ignore")
        lines = [l for l in txt.splitlines() if l.startswith("|") and "success_rate" not in l and "---" not in l]
        for line in lines[:20]:
            if "libero_" in line and "1.000" in line:
                if "libero_pro" in p.name or "with_" in line or "temp_" in line:
                    best_lp = f"`{p.name}`: {line}"
                else:
                    best_hard = f"`{p.name}`: {line}"
                break
    return best_lp, best_hard


def update_dashboard(rows: list[dict[str, Any]], added: list[str] | None = None) -> None:
    DASHBOARD.parent.mkdir(parents=True, exist_ok=True)
    by_machine = {"bob": [], "sam": []}
    for r in rows:
        by_machine.setdefault(r.get("machine", "unknown"), []).append(r)
    best_lp, best_hard = parse_best_rollout()
    completed = [r for r in rows if r.get("state") == "DONE"]
    failed = [r for r in rows if r.get("state") == "FAILED"]
    running = [r for r in rows if r.get("state") == "RUNNING"]
    pending = [r for r in rows if r.get("state") == "PENDING"]
    blockers = []
    for p in [BOB_ROOT / REL / "logs/libero_pro_pilot_bob.log", BOB_ROOT / REL / "logs/libero_pro_expanded_rollout_bob.log"]:
        if p.exists() and "FileNotFoundError" in p.read_text(errors="ignore")[-20000:]:
            blockers.append(f"`{p.name}` contains FileNotFoundError; likely missing LIBERO-PRO init states for some suites.")
    lines = [
        "# Stage 8 Live Dashboard",
        "",
        f"Updated: `{now()}`",
        "",
        "## Machine Summary",
        "",
        "| machine | running | done | failed | pending | GPU |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for m in ["bob", "sam"]:
        rs = by_machine.get(m, [])
        lines.append(f"| {m} | {sum(r.get('state')=='RUNNING' for r in rs)} | {sum(r.get('state')=='DONE' for r in rs)} | {sum(r.get('state')=='FAILED' for r in rs)} | {sum(r.get('state')=='PENDING' for r in rs)} | `{machine_gpu(m)}` |")
    lines += [
        "",
        "## Running Jobs",
        "",
    ]
    lines += [f"- `{r.get('job_id')}` on `{r.get('machine')}` log `{r.get('log_path','')}`" for r in running] or ["- none"]
    lines += ["", "## Failed Jobs", ""]
    lines += [f"- `{r.get('job_id')}` on `{r.get('machine')}`: `{r.get('error','')}`" for r in failed] or ["- none"]
    lines += [
        "",
        "## Current Best Results",
        "",
        f"- LIBERO-PRO: {best_lp}",
        f"- Normal LIBERO hard task: {best_hard}",
        "- Model: Stage 6 `context_gated_action` remains the default unless Stage 8 sweep reports improve it.",
        "- Calibration: see `stage8_calibration_mega_sweep.md` after the mega-sweep completes.",
        "- Switch: see `stage8_switch_policy_results.md` after rollout logs accumulate.",
        "",
        "## Backlog",
        "",
        f"- Running: `{len(running)}`",
        f"- Pending: `{len(pending)}`",
        f"- Done: `{len(completed)}`",
        f"- Failed: `{len(failed)}`",
        f"- Backup jobs added this tick: `{', '.join(added or []) if added else 'none'}`",
        "",
        "## Blockers",
        "",
    ]
    lines += [f"- {b}" for b in blockers] or ["- none currently detected"]
    DASHBOARD.write_text("\n".join(lines) + "\n")


def compatible_pending_exists(rows: list[dict[str, Any]], machine: str) -> bool:
    return any(r.get("machine") == machine and r.get("state") == "PENDING" for r in rows)


def running_exists(rows: list[dict[str, Any]], machine: str) -> bool:
    return any(r.get("machine") == machine and r.get("state") == "RUNNING" for r in rows)


def backup_jobs() -> list[dict[str, Any]]:
    b = str(BOB_ROOT)
    s = str(SAM_ROOT)
    return [
        make_job("backup_libero_pro_30eps_bob", "bob", 200, f'cd "{b}" && STAGE8_EPISODES=30 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh',
                 gpu=True, deps=["libero_pro_expanded_rollout_bob"], expected=[str(BOB_ROOT / REL / "reports/stage8_libero_pro_expanded_rollout_results.md")], hours=36),
        make_job("backup_normal_libero_50eps_bob", "bob", 210, f'cd "{b}" && STAGE8_EPISODES=50 bash asynchvla_ws/scripts/stage8_run_normal_libero_hard_30.sh',
                 gpu=True, deps=["normal_libero_hard_30eps_bob"], expected=[str(BOB_ROOT / REL / "reports/stage8_normal_libero_hard_task_results.md")], hours=36),
        make_job("backup_sam_calibration_extra", "sam", 220, f'cd "{s}" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="{s}" && python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py --target-coverage 0.95 && cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md asynchvla_ws/stage8_ultimate/reports/stage8_calibration_backup_q095.md',
                 deps=["calibration_mega_sam"], expected=[str(SAM_ROOT / REL / "reports/stage8_calibration_backup_q095.md")], hours=3),
        make_job("backup_sam_model_extra_seeds", "sam", 230, f'cd "{s}" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="{s}" && python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split holdout_libero_object --variants context_gated_action seed_relative_pairwise --epochs 180 --out-prefix stage8_backup_extra_seeds && cp asynchvla_ws/outputs/reports/stage6/stage8_backup_extra_seeds.* asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true',
                 deps=["architecture_loss_sweep_sam"], expected=[str(SAM_ROOT / REL / "reports/stage8_backup_extra_seeds.md")], hours=8),
        make_job("backup_flowtrace_large_bob", "bob", 240, f'cd "{b}" && source asynchvla_ws/scripts/activate_simvla_bob.sh && python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json --split-name stage8_flowtrace_large --max-contexts 800 --max-calib 200 --max-test-id 200 --max-test-ood 200 --cap-per-file 80 --simvla-seeds 0 1 2 3 4 && echo "# Stage 8 Extra Flowtrace Large" > asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_large.md',
                 gpu=True, deps=["flowtrace_medium_bob"], expected=[str(BOB_ROOT / REL / "reports/stage8_flowtrace_large.md")], hours=24),
    ]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=72.0)
    ap.add_argument("--interval-sec", type=int, default=600)
    ap.add_argument("--once", action="store_true")
    args = ap.parse_args()

    WATCHDOG_LOG.parent.mkdir(parents=True, exist_ok=True)
    deadline = datetime.now() + timedelta(hours=args.hours)
    first = True
    while first or (datetime.now() < deadline and not args.once):
        first = False
        tick_added: list[str] = []
        try:
            rows = status_rows()
            active_or_pending = any(r.get("state") in ("RUNNING", "PENDING") for r in rows)
            if not active_or_pending:
                tick_added.extend(add_jobs(backup_jobs(), "queue_empty_before_72h"))

            # If a machine is idle but has pending work, ask the manager to launch.
            for machine in ["bob", "sam"]:
                if not running_exists(rows, machine) and compatible_pending_exists(rows, machine):
                    cp = manager("launch-ready", "--limit", "2", timeout=180)
                    with WATCHDOG_LOG.open("a") as f:
                        f.write(f"\n[{now()}] launch-ready for {machine}\n{cp.stdout}\n")
                    rows = status_rows()

            # If all current work is done and no backup has been added yet, add backups.
            rows = status_rows()
            if not any(r.get("state") in ("RUNNING", "PENDING") for r in rows):
                tick_added.extend(add_jobs(backup_jobs(), "all_jobs_done_before_72h"))
                cp = manager("launch-ready", "--limit", "4", timeout=180)
                with WATCHDOG_LOG.open("a") as f:
                    f.write(f"\n[{now()}] backup launch-ready\n{cp.stdout}\n")
                rows = status_rows()

            update_dashboard(rows, tick_added)
            with WATCHDOG_LOG.open("a") as f:
                f.write(f"[{now()}] watchdog tick ok pending={sum(r.get('state')=='PENDING' for r in rows)} running={sum(r.get('state')=='RUNNING' for r in rows)} added={tick_added}\n")
        except Exception as exc:
            with WATCHDOG_LOG.open("a") as f:
                f.write(f"[{now()}] watchdog error {exc!r}\n")
        if args.once:
            break
        time.sleep(args.interval_sec)


if __name__ == "__main__":
    main()
