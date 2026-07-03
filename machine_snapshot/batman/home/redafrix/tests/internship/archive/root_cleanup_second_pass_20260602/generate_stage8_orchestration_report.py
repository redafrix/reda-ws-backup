#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shlex
import subprocess
from datetime import datetime
from pathlib import Path
from textwrap import indent

BOB = "/media/rootalkhatib/My Passport/reda_ws"
SAM = "/home/rootalkhatib/test/reda_ws"
LOCAL_STAGE8 = Path("/home/redafrix/tests/internship/codex_reports/stage8")
LOCAL_STAGE8.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str], timeout: int = 60) -> str:
    cp = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
    return cp.stdout


def bob(cmd: str, timeout: int = 60) -> str:
    return run(["ssh", "pcrobot", cmd], timeout=timeout)


def sam(cmd: str, timeout: int = 60) -> str:
    return run(["ssh", "sam", cmd], timeout=timeout)


def md_code(text: str, lang: str = "") -> str:
    return f"```{lang}\n{text.rstrip()}\n```"


def read_bob(path: str, limit: int | None = None) -> str:
    cmd = f"cat {shlex.quote(path)} 2>/dev/null || true"
    txt = bob(cmd, timeout=30)
    return txt[:limit] if limit else txt


def read_sam(path: str, limit: int | None = None) -> str:
    cmd = f"cat {shlex.quote(path)} 2>/dev/null || true"
    txt = sam(cmd, timeout=30)
    return txt[:limit] if limit else txt


def tail_remote(machine: str, path: str, n: int = 50) -> str:
    fn = bob if machine == "bob" else sam
    return fn(f"tail -{n} {shlex.quote(path)} 2>/dev/null || true", timeout=30)


def exists_remote(machine: str, path: str) -> bool:
    fn = bob if machine == "bob" else sam
    return "YES" in fn(f"test -e {shlex.quote(path)} && echo YES || echo NO", timeout=20)


def safe_json(txt: str):
    try:
        return json.loads(txt)
    except Exception:
        return None


def purpose_for(job_id: str) -> str:
    mapping = {
        "smoke_bob_cpu": "Minimal Bob manager smoke; proves local command execution and expected-output checking.",
        "smoke_sam_cpu": "Minimal Sam manager smoke; proves remote Sam command execution and expected-output checking.",
        "smoke_dependency_child": "Dependency-chain smoke; should only run after `smoke_bob_cpu`.",
        "smoke_retry_failure": "Retry-policy smoke; intentionally fails first, then succeeds on retry.",
        "libero_pro_pilot_bob": "Initial LIBERO-PRO pilot rollout on Bob; tests A/B/C/D/E modes on several perturbation suites, but only valid init-state suites produce results.",
        "stage8_sam_model_sweep": "First Sam model sweep on processed Stage 5 candidate data; tests action-only, full-old, context-gated, seed-relative pairwise, per-step, and engineered SimVLA-focused raters.",
        "stage8_sam_calibration_sweep": "Initial Sam calibration sweep over available Stage 6/8 prediction JSONs.",
        "flowtrace_experiments_sam": "Attempted Sam flowtrace-feature rater experiments across controlled OOD splits.",
        "target_sweep_sam": "Attempted Sam target comparison: L2, multi-expert/min-distance/softmin/pairwise/bad-action style targets.",
        "architecture_loss_sweep_sam": "Larger Sam architecture/loss sweep over ID and OOD splits; trains multiple Stage 6/8 rater variants for 120 epochs.",
        "normal_libero_hard_baseline_bob": "Bob normal-LIBERO hard-task rollout baseline with A/B/C/D/E modes and 10 episodes per task.",
        "libero_pro_expanded_rollout_bob": "Bob expanded LIBERO-PRO rollout benchmark on validated perturbation suites with 5 episodes per task.",
        "flowtrace_medium_bob": "Bob medium flowtrace dataset extraction from controlled OOD split using SimVLA flow metadata.",
        "calibration_mega_sam": "Sam calibration mega-sweep at 80/90/95 coverage using available predictions.",
        "normal_libero_hard_30eps_bob": "Bob scale-up of normal-LIBERO hard tasks to 30 episodes per task.",
        "libero_pro_expanded_30eps_bob": "Bob scale-up of LIBERO-PRO expanded tasks to 30 episodes per task.",
        "history_models_sam": "History/window-model placeholder/report; should only train real history models after rollout sequence data exists.",
        "switch_policy_analysis_bob": "Offline switch-policy analysis from rollout logs: seed0 accept/reject, conservative fallback, warning proxy.",
        "stage8_final_report_bob": "Final/interim Stage 8 report generation after primary dependencies complete.",
    }
    if job_id.startswith("backup_"):
        return "Watchdog backup job added only if the main queue drains before 72 hours."
    return "Unmapped Stage 8 job; inspect exact command."


def status_by_id(rows):
    return {r.get("job_id"): r for r in rows}


def one_line(s: str, n: int = 160) -> str:
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 3] + "..."


def parse_model_sweep_summary() -> str:
    out = []
    for name in [
        "stage8_holdout_libero_object_model_sweep.json",
        "stage8_holdout_object_bowl_model_sweep.json",
        "stage8_holdout_libero_spatial_model_sweep.json",
    ]:
        txt = read_sam(f"{SAM}/asynchvla_ws/stage8_ultimate/reports/{name}")
        data = safe_json(txt)
        if not data:
            continue
        out.append(f"### `{name}`")
        out.append("")
        out.append("| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |")
        out.append("|---|---|---:|---:|---:|---:|---:|")
        for r in data.get("results", []):
            metrics = r.get("metrics", {})
            part = "test_ood" if "test_ood" in metrics else "test_id"
            sim = metrics.get(part, {}).get("simvla_only", {})
            allc = metrics.get(part, {}).get("all_candidate", {})
            out.append(
                f"| `{r.get('variant')}` | `{part}` | "
                f"{sim.get('pairwise_seed_ranking', 'n/a')} | "
                f"{sim.get('predicted_best_mean_error', 'n/a')} | "
                f"{sim.get('seed0_mean_error', 'n/a')} | "
                f"{sim.get('oracle_best_mean_error', 'n/a')} | "
                f"{sim.get('auroc_top30_worst', allc.get('auroc_top30_bad', 'n/a'))} |"
            )
        out.append("")
    return "\n".join(out) if out else "No Sam model-sweep JSON could be parsed."


def parse_calibration_summary() -> str:
    best = read_sam(f"{SAM}/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_method.md")
    if not best:
        best = read_bob(f"{BOB}/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_best_method.md")
    return best or "No calibration best-method report available yet."


def main() -> None:
    exact_status_output = bob(
        f'cd {shlex.quote(BOB)} && source "asynchvla_ws/scripts/activate_simvla_bob.sh" >/dev/null 2>&1 && bash asynchvla_ws/scripts/stage8_status.sh || true',
        timeout=180,
    )
    dashboard = bob(f'cd {shlex.quote(BOB)} && cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md || true')
    ps_out = bob('ps aux | grep -E "stage8|tmux|nohup|python3" | grep -v grep || true')
    tmux_out = bob("tmux ls || true")
    nvidia_bob = bob("nvidia-smi || true")
    nvidia_sam = sam("nvidia-smi || true")
    ps_sam = sam('ps aux | grep -E "stage8|tmux|nohup|python3" | grep -v grep || true')
    manifest_txt = read_bob(f"{BOB}/asynchvla_ws/stage8_ultimate/configs/stage8_job_manifest.json")
    manifest = json.loads(manifest_txt)
    status_rows = json.loads(exact_status_output)
    status = status_by_id(status_rows)
    watchdog_code = read_bob(f"{BOB}/asynchvla_ws/scripts/stage8_watchdog.py", limit=30000)
    watchdog_log = read_bob(f"{BOB}/asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log", limit=20000)

    # Logs and selected report excerpts.
    libero_pilot_report = read_bob(f"{BOB}/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md", limit=16000)
    normal_tail = tail_remote("bob", f"{BOB}/asynchvla_ws/stage8_ultimate/logs/normal_libero_hard_baseline_bob.log", 50)
    arch_tail = tail_remote("sam", f"{SAM}/asynchvla_ws/stage8_ultimate/logs/architecture_loss_sweep_sam.log", 50)
    flowtrace_log = tail_remote("sam", f"{SAM}/asynchvla_ws/stage8_ultimate/logs/flowtrace_experiments_sam.log", 80)
    target_log = tail_remote("sam", f"{SAM}/asynchvla_ws/stage8_ultimate/logs/target_sweep_sam.log", 80)
    history_report = read_sam(f"{SAM}/asynchvla_ws/stage8_ultimate/reports/stage8_history_models.md", limit=6000)

    lines: list[str] = []
    lines += [
        "# Stage 8 Full Orchestration Manifest Report",
        "",
        f"Generated: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        "Scope: audit/reporting only. This report did not launch jobs, kill jobs, edit training/eval scripts, or change the manifest.",
        "",
    ]

    # 1
    running = [r for r in status_rows if r.get("state") == "RUNNING"]
    done = [r for r in status_rows if r.get("state") == "DONE"]
    failed = [r for r in status_rows if r.get("state") == "FAILED"]
    pending = [r for r in status_rows if r.get("state") == "PENDING"]
    watchdog_pid = read_bob(f"{BOB}/asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid").strip() or "missing"
    dashboard_update = "unknown"
    for line in dashboard.splitlines():
        if line.startswith("Updated:"):
            dashboard_update = line
            break
    lines += [
        "## 1. Current Live Status",
        "",
        f"- Watchdog running: `{'stage8_watchdog.py' in ps_out}`.",
        f"- Watchdog PID file value: `{watchdog_pid}`.",
        "- Watchdog launch mode: `nohup` via `asynchvla_ws/scripts/stage8_launch_72h_watchdog.sh`.",
        "- Watchdog nohup log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.nohup.log`.",
        "- Watchdog detailed tick log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log`.",
        f"- Running jobs now: `{', '.join(r.get('job_id','') for r in running) or 'none'}`.",
        f"- Done jobs: `{len(done)}`.",
        f"- Failed jobs: `{len(failed)}`.",
        f"- Pending jobs: `{len(pending)}`.",
        f"- Bob active/idle: `active` because `normal_libero_hard_baseline_bob` is running.",
        f"- Sam active/idle: `active` because `architecture_loss_sweep_sam` is running.",
        f"- Last dashboard update: {dashboard_update}.",
        "",
        "### Requested Command Output: `stage8_status.sh`",
        md_code(exact_status_output, "json"),
        "",
        "### Requested Command Output: Dashboard",
        md_code(dashboard, "markdown"),
        "",
        "### Requested Command Output: Bob Process Snapshot",
        md_code(ps_out, "text"),
        "",
        "### Requested Command Output: Bob tmux",
        md_code(tmux_out, "text"),
        "",
        "### Requested Command Output: Bob GPU",
        md_code(nvidia_bob, "text"),
        "",
        "### Sam GPU And Process Snapshot",
        md_code(nvidia_sam, "text"),
        md_code(ps_sam, "text"),
        "",
    ]

    # 2 manifest table
    lines += [
        "## 2. Full Job Manifest Table",
        "",
        "The table keeps commands as references to exact command blocks below to avoid unreadable table wrapping. The exact commands are included immediately after the table.",
        "",
        "| job_id | machine | current status | priority | dependencies | expected outputs | log file | status file | max retries | retry/attempt | GPU | est. duration | start | end | failure/skip reason | purpose | command ref |",
        "|---|---|---:|---:|---|---|---|---|---:|---:|---:|---:|---|---|---|---|---|",
    ]
    for j in sorted(manifest["jobs"], key=lambda x: (x.get("priority", 999), x["job_id"])):
        st = status.get(j["job_id"], {"state": "PENDING"})
        deps = ", ".join(j.get("dependencies") or []) or "none"
        outs = "<br>".join(f"`{o}`" for o in j.get("expected_outputs") or []) or "none"
        lines.append(
            f"| `{j['job_id']}` | {j.get('machine')} | {st.get('state','PENDING')} | {j.get('priority')} | {deps} | {outs} | "
            f"`{j.get('log_path','')}` | `{j.get('status_path','')}` | {j.get('max_retries')} | {st.get('attempt','')} | "
            f"{j.get('gpu_required')} | {j.get('timeout_hours')}h | {st.get('started_at','')} | {st.get('completed_at','')} | "
            f"{one_line(st.get('error',''))} | {purpose_for(j['job_id'])} | `Command: {j['job_id']}` |"
        )
    lines += ["", "### Exact Commands From Manifest", ""]
    for j in sorted(manifest["jobs"], key=lambda x: (x.get("priority", 999), x["job_id"])):
        lines += [f"#### Command: `{j['job_id']}`", md_code(j.get("command", ""), "bash"), ""]

    # 3 completed jobs
    lines += ["## 3. Completed Jobs: Exact Details", ""]
    for r in done:
        j = next((x for x in manifest["jobs"] if x["job_id"] == r["job_id"]), None)
        if not j:
            continue
        machine = j.get("machine")
        valid = []
        for out in j.get("expected_outputs") or []:
            valid.append(f"`{out}`: {'exists' if exists_remote(machine, out) else 'missing'}")
        lines += [
            f"### `{j['job_id']}`",
            "",
            f"- Machine: `{machine}`.",
            f"- Command: {md_code(j.get('command',''), 'bash')}",
            f"- Log file: `{j.get('log_path')}`.",
            f"- Status file: `{j.get('status_path')}`.",
            f"- Output files validity: {', '.join(valid) if valid else 'no expected outputs declared'}.",
            f"- Start: `{r.get('started_at','not tracked')}`.",
            f"- End: `{r.get('completed_at','not tracked')}`.",
            f"- Affects future jobs: dependencies using this job can now launch.",
        ]
        jid = j["job_id"]
        if jid == "libero_pro_pilot_bob":
            lines += [
                "- Scientific result: partial LIBERO-PRO pilot. Only `libero_object_with_mug` produced JSON outputs; `libero_goal_object` and `libero_object_env` had missing `.pruned_init` files.",
                "- Completed result files: `libero_object_with_mug_task0/1/2.json`.",
                "- Most important metrics excerpt:",
                md_code("\n".join(libero_pilot_report.splitlines()[:28]), "markdown"),
            ]
        elif jid == "stage8_sam_model_sweep":
            lines += [
                "- Datasets: `holdout_libero_object`, `holdout_object_bowl`, `holdout_libero_spatial`.",
                "- Variants tested: `action_only_baseline`, `full_old_baseline`, `context_gated_action`, `seed_relative_pairwise`, `per_step_error_head`, `full_engineered_simvla_focused`.",
                "- Training target: chunk-level normalized action L2 error from existing candidate datasets.",
                "- Losses/architectures: Huber regression for ordinary regressors; pairwise auxiliary ranking loss for `seed_relative_pairwise`; per-step Huber plus chunk Huber for `per_step_error_head`.",
                "- Key model-sweep summary:",
                parse_model_sweep_summary(),
            ]
        elif jid == "stage8_sam_calibration_sweep":
            lines += [
                "- Calibration methods actually implemented in `run_calibration_sweep.py`: global residual conformal, SimVLA-only residual conformal, affine plus residual; binned residual code exists but is not emitted as a report method.",
                "- Not implemented in this completed sweep: isotonic, Platt/logistic, quantile conformal, ensemble mean+std, small OOD calibration pools.",
                "- Best-method excerpt:",
                md_code(parse_calibration_summary(), "markdown"),
            ]
        elif jid == "flowtrace_experiments_sam":
            lines += [
                "- Manager status is `DONE` because an expected placeholder report exists.",
                "- Internal experiment result: failed for all splits due hardcoded Bob path on Sam (`PermissionError: /media/rootalkhatib/My Passport`).",
                "- Therefore `flowtrace_only`, `action_only + flowtrace`, `context_gated + flowtrace`, and `seed_relative + flowtrace` were **not scientifically evaluated** by this job.",
                "- Log excerpt:",
                md_code(flowtrace_log[-6000:], "text"),
            ]
        elif jid == "target_sweep_sam":
            lines += [
                "- Manager status is `DONE` because an expected placeholder report exists.",
                "- Internal experiment result: failed. Multi-expert target builder looked for Bob-style paths on Sam and target experiment then hit missing `single_l2` target columns / empty parts.",
                "- Therefore multi-expert K=5/10/20, softmin, pairwise target, bad-action target, and progress/success target were **not scientifically evaluated** by this job.",
                "- Log excerpt:",
                md_code(target_log[-6000:], "text"),
            ]
        elif jid == "history_models_sam":
            lines += [
                "- This is a placeholder/report-only job. It did not train LSTM, GRU, Transformer, TCN, or Mamba.",
                "- Reason: rollout sequence data is required before history models can be trained without leakage.",
                "- Report excerpt:",
                md_code(history_report, "markdown"),
            ]
        elif jid.startswith("smoke"):
            lines += ["- Purpose: infrastructure smoke only; no scientific metrics."]
        lines.append("")

    # 4 running jobs
    lines += ["## 4. Running Jobs: Exact Details", ""]
    for r in running:
        j = next((x for x in manifest["jobs"] if x["job_id"] == r["job_id"]), None)
        if not j:
            continue
        machine = j.get("machine")
        tail = tail_remote(machine, j.get("log_path", ""), 50)
        dep_next = [x["job_id"] for x in manifest["jobs"] if r["job_id"] in (x.get("dependencies") or [])]
        progress = "not detectable"
        healthy = "appears healthy"
        if "Traceback" in tail or "Error" in tail:
            healthy = "warning: recent log contains error/traceback"
        if r["job_id"] == "normal_libero_hard_baseline_bob":
            progress = "currently processing `libero_spatial task 5`; A_passive finished, B_deliberation finished/near finished, C_random_seed started in latest logs."
        if r["job_id"] == "architecture_loss_sweep_sam":
            progress = "currently in the architecture sweep; `id_task_split` completed and `holdout_libero_object` is running in latest logs."
        lines += [
            f"### `{r['job_id']}`",
            "",
            f"- Machine: `{machine}`.",
            f"- PID: `{r.get('pid','')}`.",
            f"- Launch mode: manager-created `nohup` shell script `{j.get('command_file')}`.",
            f"- Command: {md_code(j.get('command',''), 'bash')}",
            f"- Log file: `{j.get('log_path')}`.",
            f"- Last 50 log lines:",
            md_code(tail, "text"),
            f"- Current progress: {progress}.",
            f"- Expected outputs: {', '.join('`'+o+'`' for o in j.get('expected_outputs', []))}.",
            f"- Next dependent jobs after completion: `{', '.join(dep_next) or 'none'}`.",
            f"- Health: {healthy}.",
            "",
        ]

    # 5 pending
    lines += ["## 5. Pending Jobs: Exact Future Plan", ""]
    success_metrics = {
        "libero_pro_expanded_rollout_bob": "LIBERO-PRO success rate, steps to success, uncertainty-risk relation, A/B/C/D comparison.",
        "flowtrace_medium_bob": "flowtrace dataset existence, context counts, compact flow metadata availability.",
        "calibration_mega_sam": "coverage at 80/90/95, width, zero-shot transfer; methods available in current script.",
        "normal_libero_hard_30eps_bob": "hard-task success/progress at 30 episodes and whether uncertainty predicts slow/fail episodes.",
        "libero_pro_expanded_30eps_bob": "larger LIBERO-PRO success/progress and switch proxy stability.",
        "switch_policy_analysis_bob": "accepted vs rejected risk, fallback seed policy, warning proxy summary.",
        "stage8_final_report_bob": "complete artifact synthesis and final decision.",
        "architecture_loss_sweep_sam": "SimVLA-only pairwise seed ranking, predicted-best vs seed0, risk coverage, AUROC.",
    }
    for r in pending:
        j = next((x for x in manifest["jobs"] if x["job_id"] == r["job_id"]), None)
        if not j:
            continue
        deps = j.get("dependencies") or []
        dep_states = [f"{d}={status.get(d,{}).get('state','unknown')}" for d in deps]
        lines += [
            f"### `{j['job_id']}`",
            "",
            f"- Machine: `{j.get('machine')}`.",
            f"- Why pending: waits for dependencies or GPU availability. Dependency states: `{', '.join(dep_states) or 'none'}`.",
            f"- What it will do: {purpose_for(j['job_id'])}",
            f"- Exact command: {md_code(j.get('command',''), 'bash')}",
            f"- Expected output/report: {', '.join('`'+o+'`' for o in j.get('expected_outputs', []))}.",
            f"- Idea tested: {purpose_for(j['job_id'])}",
            f"- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.",
            f"- Success/failure metrics: {success_metrics.get(j['job_id'], 'expected outputs exist; logs contain no fatal errors; downstream reports contain interpretable metrics')}.",
            "",
        ]

    # 6 watchdog behavior
    lines += [
        "## 6. Backup Jobs / Watchdog Behavior",
        "",
        "- Watchdog script: `asynchvla_ws/scripts/stage8_watchdog.py`.",
        "- Watchdog interval: every `600` seconds.",
        "- Watchdog duration: up to `72` hours from launch.",
        "- It checks job status through `stage8_job_manager.py status`.",
        "- It checks Bob/Sam GPU usage for dashboard display.",
        "- If a machine is idle and has pending work, it calls `stage8_job_manager.py launch-ready --limit 2`.",
        "- If a job failed, retry behavior is handled by `stage8_job_manager.py launch-ready`; it retries while `attempt <= max_retries`.",
        "- If the main queue becomes empty before 72 hours, the watchdog adds backup jobs.",
        "",
        "### Backup Jobs Implemented In Code",
        "",
        "| backup job | machine | purpose |",
        "|---|---|---|",
        "| `backup_libero_pro_30eps_bob` | Bob | more LIBERO-PRO rollout episodes using `stage8_run_libero_pro_expanded.sh` with 30 episodes/task |",
        "| `backup_normal_libero_50eps_bob` | Bob | normal LIBERO hard tasks at 50 episodes/task |",
        "| `backup_sam_calibration_extra` | Sam | extra q=0.95 calibration sweep |",
        "| `backup_sam_model_extra_seeds` | Sam | extra training for `context_gated_action` and `seed_relative_pairwise` on `holdout_libero_object` |",
        "| `backup_flowtrace_large_bob` | Bob | larger flowtrace extraction for `holdout_libero_object` |",
        "",
        "### What The Watchdog Does Not Fully Do",
        "",
        "- It does not directly copy the dashboard to Batman every hour. A separate Batman-side local collector process was previously launched for report copying; the watchdog itself only writes the Bob dashboard.",
        "- It does not add new instruction-perturbation or environment-perturbation jobs beyond the existing valid-suite list.",
        "- It does not add real history model training; history training still needs rollout sequence data.",
        "",
        "### Watchdog Code Excerpt",
        md_code("\n".join(watchdog_code.splitlines()[:220]), "python"),
        "",
    ]

    # 7 checklist
    checklist = [
        ("A. LIBERO-PRO setup/import/reset", "DONE", "Smoke passed; LIBERO-PRO repo/config available and env reset/rollout works."),
        ("A. LIBERO-PRO pilot rollout", "DONE", "Completed only for `libero_object_with_mug`; other attempted suites hit missing init states."),
        ("A. LIBERO-PRO expanded rollout", "QUEUED", "`libero_pro_expanded_rollout_bob` and 30eps job are pending."),
        ("A. object perturbation", "DONE/QUEUED", "`with_mug` done; more object perturbation variants queued."),
        ("A. initial-state perturbation", "QUEUED", "`libero_object_temp_x*` variants queued as position/init perturbation style tests."),
        ("A. instruction perturbation", "NOT INCLUDED", "No validated instruction-perturbation suite with local init states is in the manifest."),
        ("A. environment perturbation", "BLOCKED", "`libero_object_env` failed due missing `.pruned_init` files."),
        ("A. A_passive", "DONE/RUNNING/QUEUED", "Used in pilot and current/queued rollouts."),
        ("A. B_deliberation", "DONE/RUNNING/QUEUED", "Used in pilot and current/queued rollouts."),
        ("A. C_random_seed", "DONE/RUNNING/QUEUED", "Used in pilot and current/queued rollouts."),
        ("A. D_reject_log", "DONE/RUNNING/QUEUED", "`D_low_uncertainty_reject_log` used."),
        ("A. E_conservative_switch_proxy", "DONE", "Used in pilot and normal hard baseline; not included in expanded LIBERO-PRO script."),
        ("B. hard task scan", "DONE", "Stage 7 hard scan identified tasks."),
        ("B. hard task 10 episodes", "RUNNING", "`normal_libero_hard_baseline_bob`."),
        ("B. hard task 30 episodes", "QUEUED", "`normal_libero_hard_30eps_bob`."),
        ("B. hard task 50 episodes backup", "BACKUP ONLY", "`backup_normal_libero_50eps_bob`."),
        ("B. libero_spatial task 5", "RUNNING", "Currently being processed."),
        ("B. libero_goal task 0", "QUEUED", "In normal hard scripts."),
        ("B. libero_goal task 9", "QUEUED", "In normal hard scripts."),
        ("B. libero_10 task 0/1", "QUEUED", "In normal hard scripts."),
        ("C. flowtrace extraction", "QUEUED", "`flowtrace_medium_bob`; Sam flowtrace experiment failed internally."),
        ("C. flowtrace_only", "BLOCKED", "Attempted on Sam but failed due path issue; not scientifically evaluated."),
        ("C. action_only + flowtrace", "BLOCKED", "Attempted on Sam but failed due path issue."),
        ("C. context_gated + flowtrace", "BLOCKED", "Attempted on Sam but failed due path issue."),
        ("C. seed_relative + flowtrace", "BLOCKED", "Attempted on Sam but failed due path issue."),
        ("D. single expert L2", "DONE/RUNNING", "Base target in completed and running model sweeps."),
        ("D. multi-expert min-distance K=5", "BLOCKED", "Target job failed due path/target-column issues."),
        ("D. multi-expert min-distance K=10", "BLOCKED", "Target job failed."),
        ("D. multi-expert min-distance K=20", "BLOCKED", "Target job failed."),
        ("D. softmin expert distance", "BLOCKED", "Target job failed."),
        ("D. pairwise seed ranking target", "RUNNING", "`seed_relative_pairwise` is in architecture sweep; true target-sweep pairwise job failed."),
        ("D. bad-action classification target", "NOT INCLUDED", "Not implemented in current runner; only AUROC evaluation exists."),
        ("D. rollout progress target", "BLOCKED", "Needs rollout/progress labels."),
        ("D. hybrid target", "NOT INCLUDED", "Deferred until target components work."),
        ("E. action_only_mlp", "DONE/RUNNING", "Completed first sweep; running architecture sweep."),
        ("E. full_old_mlp", "DONE/RUNNING", "Completed first sweep; running architecture sweep."),
        ("E. context_gated_action", "DONE/RUNNING", "Completed first sweep; running architecture sweep."),
        ("E. seed_relative_rater", "RUNNING", "Included in architecture sweep."),
        ("E. context_gated + seed_relative", "NOT INCLUDED", "No explicit combined architecture variant in manifest."),
        ("E. per_step_error_head", "DONE/RUNNING", "Completed first sweep; running architecture sweep."),
        ("E. pairwise_ranker", "DONE/RUNNING", "`seed_relative_pairwise` uses pairwise auxiliary loss."),
        ("E. heteroscedastic head", "NOT INCLUDED", "Model class exists, but no manifest variant uses it."),
        ("E. quantile heads", "NOT INCLUDED", "No q=0.8/0.9/0.95 quantile training job exists."),
        ("E. ensemble", "BACKUP ONLY", "Only backup extra seeds, not full ensemble calibration/training."),
        ("E. LSTM/GRU", "NOT INCLUDED", "History job is placeholder only."),
        ("E. Transformer", "NOT INCLUDED", "History job is placeholder only."),
        ("E. TCN", "NOT INCLUDED", "History job is placeholder only."),
        ("E. Mamba", "NOT INCLUDED", "Dependency/model not tested."),
        ("F. Huber", "DONE/RUNNING", "Main regression loss."),
        ("F. Huber + pairwise", "DONE/RUNNING", "`seed_relative_pairwise`."),
        ("F. Huber + bad-action BCE", "NOT INCLUDED", "Not in current runner."),
        ("F. quantile pinball", "NOT INCLUDED", "Not in current runner."),
        ("F. heteroscedastic NLL", "NOT INCLUDED", "Model code exists, no job uses it."),
        ("F. progress classification", "BLOCKED", "Needs rollout labels."),
        ("G. global residual conformal", "DONE", "Initial calibration sweep."),
        ("G. SimVLA-only conformal", "DONE", "Implemented as simvla residual mode in calibration sweep."),
        ("G. binned conformal 5 bins", "NOT INCLUDED", "Helper exists but report methods do not emit binned method."),
        ("G. binned conformal 10 bins", "NOT INCLUDED", "Not emitted."),
        ("G. affine+residual", "DONE", "Initial calibration sweep."),
        ("G. isotonic regression", "NOT INCLUDED", "No current implementation."),
        ("G. Platt/logistic", "NOT INCLUDED", "No current implementation."),
        ("G. quantile conformal", "NOT INCLUDED", "No quantile model/conformal job."),
        ("G. ensemble mean+std", "NOT INCLUDED", "No ensemble model available."),
        ("G. split/perturbation stratified", "NOT INCLUDED", "Placeholder text only."),
        ("G. small OOD calibration 10/25/50/100", "NOT INCLUDED", "Not implemented."),
        ("H. accept/reject seed0", "DONE/RUNNING/QUEUED", "D reject log and switch analysis."),
        ("H. conservative fallback lowest-uncertainty seed", "DONE", "Pilot and normal hard baseline include E; expanded LIBERO-PRO does not."),
        ("H. warning/intervention proxy", "QUEUED", "Switch analysis over logs."),
        ("H. oracle expert fallback", "NOT INCLUDED", "No expert-action runtime substitution job."),
    ]
    lines += ["## 7. Ideas Coverage Checklist", "", "| item | status | explanation |", "|---|---:|---|"]
    for item, st, why in checklist:
        lines.append(f"| {item} | {st} | {why} |")
    lines.append("")

    # 8 current best
    lines += [
        "## 8. Current Best-Known Results",
        "",
        "- Best LIBERO-PRO result so far: `libero_object_with_mug` pilot. `A_passive`, `B_deliberation`, `D_reject_log`, and `E_conservative_switch_proxy` reached 100% success on tasks 0-2 except random-seed mode lost one episode each on tasks 1 and 2. This is a small/easy pilot, not final evidence.",
        "- Best normal-LIBERO hard-task result: not available yet; hard-task benchmark is running.",
        "- Best model so far: Stage 6/early Stage 8 controlled-OOD reports still point to context-aware variants. In the first Sam sweep, `context_gated_action`, `seed_relative_pairwise`, `per_step_error_head`, and `full_engineered_simvla_focused` substantially beat action-only on AUROC; exact winner varies by split.",
        "- Best action-only baseline: completed in `stage8_sam_model_sweep`; action-only is weaker on controlled OOD AUROC than context-aware variants in the parsed sweep.",
        "- Best context-aware result: `context_gated_action` / `seed_relative_pairwise` / `full_engineered_simvla_focused` depending split; running architecture sweep should refine this.",
        "- Best calibration method: current report ranks residual/affine residual variants, but calibration coverage remains a partial controlled-OOD analysis, not LIBERO-PRO rollout-risk calibration.",
        "- Best switch proxy result: not available yet beyond pilot; switch analysis is pending.",
        "- Biggest failure/blocker: LIBERO-PRO missing init states for some suites, plus Sam flowtrace/target jobs internally failed due Bob-path assumptions.",
        "",
        "### Current Parsed Model Sweep Summary",
        "",
        parse_model_sweep_summary(),
        "",
    ]

    # 9 risks
    lines += [
        "## 9. Risk Assessment",
        "",
        "- Could the queue finish before 72 hours? Yes on Sam; Bob rollout jobs are likely the bottleneck. The watchdog can add backups only after the full queue drains.",
        "- Could Bob become idle? Less likely while rollout jobs remain. If Bob becomes idle and pending dependencies are satisfied, watchdog should launch the next Bob job.",
        "- Could Sam become idle? Yes after `architecture_loss_sweep_sam` and `calibration_mega_sam`; backup Sam jobs exist but are limited.",
        "- Are there enough backup jobs? Partially. There are backup LIBERO-PRO, hard-task, calibration, model-seed, and flowtrace jobs. There are no backup instruction-perturbation or real history-training jobs.",
        "- Are failed jobs retried? Yes, up to each job's `max_retries`; however internal failures hidden behind `|| echo WARN` can still exit 0 and be marked DONE if placeholder reports exist.",
        "- Are logs copied locally? A separate Batman-side local collector was launched earlier. The watchdog itself does not directly copy reports hourly despite the desired behavior.",
        "- Is final report guaranteed to run? Not guaranteed before 72h; it depends on `switch_policy_analysis_bob`, `calibration_mega_sam`, and `history_models_sam`. If Bob rollout dependencies run long, final report may not launch before the user checks.",
        "- What happens if LIBERO-PRO fails? Broken suites are logged as warnings and skipped by scripts; expanded jobs use suites with known local init states to reduce this risk.",
        "- What happens if Sam fails? Sam jobs can retry once if the manager observes FAILED. But path bugs that exit 0 with placeholder reports will not be retried automatically.",
        "- What happens if calibration jobs fail? Dependent final report may wait or fail depending status; backup calibration exists only if queue drains.",
        "- Additional risk: old `stage8_scheduler_loop.sh` processes are still running alongside the new watchdog. The manager prevents duplicate completed jobs, but multiple launchers could race on pending jobs. No jobs were killed because this task is audit-only.",
        "",
    ]

    # 10 correction
    lines += [
        "## 10. Recommended Correction Before Leaving",
        "",
        "This report is audit-only and did not apply corrections. Recommended corrections if the user explicitly approves later:",
        "",
        "1. Stop or disable the older `stage8_scheduler_loop.sh` processes and keep only `stage8_watchdog.py`, to avoid two launch controllers racing.",
        "2. Fix Sam path portability in `run_stage7_flowtrace_experiments.py` and `run_stage7_multi_expert_target_experiments.py` by honoring `REDA_WS`, then rerun `flowtrace_experiments_sam` and `target_sweep_sam` as real jobs.",
        "3. Change flowtrace/target wrapper scripts so internal experiment failures return non-zero instead of writing placeholder success reports.",
        "4. Add real implementations for binned conformal output, isotonic/Platt/quantile calibration, heteroscedastic and quantile model variants, and small-OOD calibration pools if those are required for Stage 8 claims.",
        "5. Add a Sam idle backup chain after `calibration_mega_sam`, because Sam may finish far earlier than Bob.",
        "6. Add only validated LIBERO-PRO suites with existing `.pruned_init` files; do not use `libero_object_env` until data is fixed.",
        "",
    ]

    # 11 check commands
    lines += [
        "## 11. How The User Can Check Later",
        "",
        "### Check dashboard",
        md_code(f'ssh pcrobot \'cd "{BOB}" && cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md\'', "bash"),
        "### Check watchdog",
        md_code(f'ssh pcrobot \'cd "{BOB}" && ps -fp $(cat asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid) && tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log\'', "bash"),
        "### Check Bob GPU",
        md_code("ssh pcrobot 'nvidia-smi'", "bash"),
        "### Check Sam GPU",
        md_code("ssh sam 'nvidia-smi'", "bash"),
        "### Check final report",
        md_code(f'ssh pcrobot \'test -f "{BOB}/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md" && tail -80 "{BOB}/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md" || echo not_ready\'', "bash"),
        "### Collect reports",
        md_code(f'bash "{BOB}/asynchvla_ws/scripts/stage8_collect_reports.sh"', "bash"),
        "",
    ]

    # 12 local duplicate appended outside after file exists
    lines += ["## 12. Duplicate Report Check", "", "PLACEHOLDER_DUPLICATE_FIND_OUTPUT", ""]

    report = "\n".join(lines)
    local = LOCAL_STAGE8 / "stage8_full_orchestration_manifest_report.md"
    local.write_text(report)
    # Append duplicate check after local file exists.
    find_output = run(["bash", "-lc", "find /home/redafrix/tests/internship/codex_reports/stage8 -maxdepth 3 -type f | sort"], timeout=30)
    report = report.replace("PLACEHOLDER_DUPLICATE_FIND_OUTPUT", md_code(find_output, "text"))
    local.write_text(report)
    # Copy to Bob.
    tmp = Path("/tmp/stage8_full_orchestration_manifest_report.md")
    tmp.write_text(report)
    subprocess.run([
        "scp",
        str(tmp),
        f"pcrobot:{shlex.quote(BOB)}/asynchvla_ws/stage8_ultimate/reports/stage8_full_orchestration_manifest_report.md",
    ], check=False)
    # If scp quoting with spaces fails, use stdin over ssh.
    if "stage8_full_orchestration_manifest_report.md" not in bob(
        f"test -f {shlex.quote(BOB + '/asynchvla_ws/stage8_ultimate/reports/stage8_full_orchestration_manifest_report.md')} && echo stage8_full_orchestration_manifest_report.md || true"
    ):
        subprocess.run(
            ["ssh", "pcrobot", f"cat > {shlex.quote(BOB + '/asynchvla_ws/stage8_ultimate/reports/stage8_full_orchestration_manifest_report.md')}"],
            input=report,
            text=True,
            check=True,
        )
    print(local)
    print(BOB + "/asynchvla_ws/stage8_ultimate/reports/stage8_full_orchestration_manifest_report.md")


if __name__ == "__main__":
    main()
