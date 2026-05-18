# Stage 8 Full Orchestration Manifest Report

Generated: `2026-05-15T20:09:16`

Scope: audit/reporting only. This report did not launch jobs, kill jobs, edit training/eval scripts, or change the manifest.

## 1. Current Live Status

- Watchdog running: `True`.
- Watchdog PID file value: `658116`.
- Watchdog launch mode: `nohup` via `asynchvla_ws/scripts/stage8_launch_72h_watchdog.sh`.
- Watchdog nohup log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.nohup.log`.
- Watchdog detailed tick log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log`.
- Running jobs now: `libero_pro_expanded_rollout_bob`.
- Done jobs: `13`.
- Failed jobs: `0`.
- Pending jobs: `5`.
- Bob active/idle: `active` because `libero_pro_expanded_rollout_bob` is running.
- Sam active/idle: `idle or waiting`; no Sam job is currently marked `RUNNING`, but completed Sam jobs have produced outputs and `calibration_mega_sam` is already marked `DONE`.
- Last dashboard update: Updated: `2026-05-15T20:06:37`.

### Requested Command Output: `stage8_status.sh`
```json
[
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:43+02:00",
    "job_id": "smoke_bob_cpu",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "614539",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:43+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:44+02:00",
    "job_id": "smoke_sam_cpu",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2122302",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:44+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:09:51+02:00",
    "job_id": "smoke_dependency_child",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "614763",
    "state": "DONE",
    "updated_at": "2026-05-15T15:09:51+02:00"
  },
  {
    "attempt": 2,
    "completed_at": "2026-05-15T15:10:18+02:00",
    "job_id": "smoke_retry_failure",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "615217",
    "state": "DONE",
    "updated_at": "2026-05-15T15:10:18+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:00:59+02:00",
    "job_id": "libero_pro_pilot_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "629034",
    "state": "DONE",
    "updated_at": "2026-05-15T16:00:59+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:39:23+02:00",
    "job_id": "stage8_sam_model_sweep",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2132768",
    "state": "DONE",
    "updated_at": "2026-05-15T15:39:23+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T15:39:35+02:00",
    "job_id": "stage8_sam_calibration_sweep",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2142583",
    "state": "DONE",
    "updated_at": "2026-05-15T15:39:35+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:14:44+02:00",
    "job_id": "flowtrace_experiments_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2164506",
    "state": "DONE",
    "updated_at": "2026-05-15T16:14:44+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:14:55+02:00",
    "job_id": "target_sweep_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2164866",
    "state": "DONE",
    "updated_at": "2026-05-15T16:14:55+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:49:59+02:00",
    "job_id": "architecture_loss_sweep_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2167999",
    "state": "DONE",
    "updated_at": "2026-05-15T16:49:59+02:00"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T19:41:31+02:00",
    "job_id": "normal_libero_hard_baseline_bob",
    "machine": "bob",
    "missing_outputs": [],
    "pid": "649690",
    "state": "DONE",
    "updated_at": "2026-05-15T19:41:31+02:00"
  },
  {
    "attempt": 1,
    "command_file": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/libero_pro_expanded_rollout_bob.sh",
    "job_id": "libero_pro_expanded_rollout_bob",
    "log_path": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_rollout_bob.log",
    "machine": "bob",
    "pid": "776740",
    "started_at": "2026-05-15T19:41:33+02:00",
    "state": "RUNNING",
    "updated_at": "2026-05-15T19:41:33+02:00"
  },
  {
    "job_id": "flowtrace_medium_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:50:11+02:00",
    "job_id": "calibration_mega_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2203428",
    "state": "DONE",
    "updated_at": "2026-05-15T16:50:11+02:00"
  },
  {
    "job_id": "normal_libero_hard_30eps_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "libero_pro_expanded_30eps_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "attempt": 1,
    "completed_at": "2026-05-15T16:15:03+02:00",
    "job_id": "history_models_sam",
    "machine": "sam",
    "missing_outputs": [],
    "pid": "2168517",
    "state": "DONE",
    "updated_at": "2026-05-15T16:15:03+02:00"
  },
  {
    "job_id": "switch_policy_analysis_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_final_report_bob",
    "machine": "bob",
    "state": "PENDING"
  }
]
```

### Requested Command Output: Dashboard
```markdown
# Stage 8 Live Dashboard

Updated: `2026-05-15T20:06:37`

## Machine Summary

| machine | running | done | failed | pending | GPU |
|---|---:|---:|---:|---:|---|
| bob | 1 | 5 | 0 | 5 | `NVIDIA GeForce RTX 4070 Ti SUPER, 7297 MiB, 16376 MiB, 79 %` |
| sam | 0 | 8 | 0 | 0 | `NVIDIA GeForce RTX 4070 Ti SUPER, 3645 MiB, 16376 MiB, 0 %` |

## Running Jobs

- `libero_pro_expanded_rollout_bob` on `bob` log `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_rollout_bob.log`

## Failed Jobs

- none

## Current Best Results

- LIBERO-PRO: `stage8_libero_pro_pilot_results.md`: | libero_object_with_mug | 0 | A_passive | 5 | 1.000 | 148.60 | 1.350 | 2.028 | 3.40 | 5.000 |
- Normal LIBERO hard task: `stage8_normal_libero_hard_task_baseline.md`: | libero_10 | 0 | A_passive | 10 | 1.000 | 241.70 | 1.248 | 2.192 | 7.40 | 10.000 |
- Model: Stage 6 `context_gated_action` remains the default unless Stage 8 sweep reports improve it.
- Calibration: see `stage8_calibration_mega_sweep.md` after the mega-sweep completes.
- Switch: see `stage8_switch_policy_results.md` after rollout logs accumulate.

## Backlog

- Running: `1`
- Pending: `5`
- Done: `13`
- Failed: `0`
- Backup jobs added this tick: `none`

## Blockers

- `libero_pro_pilot_bob.log` contains FileNotFoundError; likely missing LIBERO-PRO init states for some suites.
```

### Requested Command Output: Bob Process Snapshot
```text
root         664  0.0  0.0  44060 21964 ?        Ss   May11   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         982  0.0  0.0 121084 23960 ?        Ssl  May11   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
rootalk+  629551  0.0  0.0  12844  2144 ?        S    15:29   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && mv /tmp/stage8_scheduler_loop.sh asynchvla_ws/scripts/stage8_scheduler_loop.sh && chmod +x asynchvla_ws/scripts/stage8_scheduler_loop.sh && nohup asynchvla_ws/scripts/stage8_scheduler_loop.sh > asynchvla_ws/stage8_ultimate/logs/stage8_scheduler_loop.nohup.log 2>&1 & echo $! > asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid && echo scheduler_started
rootalk+  629554  0.0  0.0  12844  3632 ?        S    15:29   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  629790  0.0  0.0  12844  3684 ?        S    15:29   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  631249  0.0  0.0  12844  3716 ?        Ss   15:30   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && python3 - <<PY import json, subprocess, datetime from pathlib import Path root=Path("/media/rootalkhatib/My Passport/reda_ws") rows=json.loads(subprocess.check_output(["python3","asynchvla_ws/scripts/stage8_job_manager.py","status"],cwd=root,text=True)) lines=["# Stage 8 Queue Launch Status","",f"Generated: `{datetime.datetime.now().isoformat(timespec=\"seconds\")}`","", "## Launched Jobs", "", "| job | machine | state | log |", "|---|---|---:|---|"] for r in rows:     lines.append(f"| {r.get(\"job_id\")} | {r.get(\"machine\",\"\")} | {r.get(\"state\",\"\")} | `{r.get(\"log_path\",\"\")}` |") lines += ["", "## Scheduler", "", "- Bob scheduler loop: `asynchvla_ws/scripts/stage8_scheduler_loop.sh`", "- Bob scheduler pid file: `asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid`", "- Batman local report collector pid file: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid`", "", "## Current Interpretation", "", "- LIBERO-PRO pilot is running on Bob and is the primary benchmark.", "- Sam model sweep is running in parallel.", "- Normal LIBERO hard-task baseline and flowtrace medium extraction are queued behind the LIBERO-PRO pilot to avoid GPU collision.", "- Sam calibration is queued behind the Sam model sweep."] (root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md").write_text("\n".join(lines)+"\n") print(root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md") PY
rootalk+  631250  0.0  0.0  12840  1932 ?        S    15:30   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && python3 - <<PY import json, subprocess, datetime from pathlib import Path root=Path("/media/rootalkhatib/My Passport/reda_ws") rows=json.loads(subprocess.check_output(["python3","asynchvla_ws/scripts/stage8_job_manager.py","status"],cwd=root,text=True)) lines=["# Stage 8 Queue Launch Status","",f"Generated: `{datetime.datetime.now().isoformat(timespec=\"seconds\")}`","", "## Launched Jobs", "", "| job | machine | state | log |", "|---|---|---:|---|"] for r in rows:     lines.append(f"| {r.get(\"job_id\")} | {r.get(\"machine\",\"\")} | {r.get(\"state\",\"\")} | `{r.get(\"log_path\",\"\")}` |") lines += ["", "## Scheduler", "", "- Bob scheduler loop: `asynchvla_ws/scripts/stage8_scheduler_loop.sh`", "- Bob scheduler pid file: `asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid`", "- Batman local report collector pid file: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid`", "", "## Current Interpretation", "", "- LIBERO-PRO pilot is running on Bob and is the primary benchmark.", "- Sam model sweep is running in parallel.", "- Normal LIBERO hard-task baseline and flowtrace medium extraction are queued behind the LIBERO-PRO pilot to avoid GPU collision.", "- Sam calibration is queued behind the Sam model sweep."] (root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md").write_text("\n".join(lines)+"\n") print(root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md") PY
rootalk+  631253  0.0  0.0  12844  3672 ?        S    15:30   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  658116  0.0  0.0  30284 14964 ?        S    16:14   0:00 python3 asynchvla_ws/scripts/stage8_watchdog.py --hours 72 --interval-sec 600
rootalk+  776740  0.0  0.0  12844  3604 ?        S    19:41   0:00 bash /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/libero_pro_expanded_rollout_bob.sh
rootalk+  776746  0.0  0.0  12844  3704 ?        S    19:41   0:00 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
rootalk+  791358  0.0  0.0  11248  2076 ?        S    20:06   0:00 timeout 14400 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_object_with_mug --task-id 3 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_object_with_mug_task3.json
rootalk+  791359  131 12.5 22437800 4025260 ?    Rl   20:06   3:41 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_object_with_mug --task-id 3 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_object_with_mug_task3.json
rootalk+  851081  0.0  6.9 14518904 2216340 ?    S    May12   0:11 python3 marathon_c_50.py --idea 22
rootalk+ 3433103  0.0  0.0  14084  3808 ?        Ss   May13   0:00 tmux new-session -d -s stage5 -c /media/rootalkhatib/My Passport/reda_ws bash -l
```

### Requested Command Output: Bob tmux
```text
stage5: 1 windows (created Wed May 13 17:01:26 2026)
```

### Requested Command Output: Bob GPU
```text
Fri May 15 20:09:14 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.211.01             Driver Version: 570.211.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:A2:00.0 Off |                  N/A |
| 53%   78C    P2            233W /  285W |    7297MiB /  16376MiB |     24%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1148      G   /usr/lib/xorg/Xorg                       80MiB |
|    0   N/A  N/A            1586      G   /usr/bin/gnome-shell                      8MiB |
|    0   N/A  N/A          791359    C+G   python3                                4017MiB |
+-----------------------------------------------------------------------------------------+
```

### Sam GPU And Process Snapshot
```text
Fri May 15 20:09:14 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.211.01             Driver Version: 570.211.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:A2:00.0 Off |                  N/A |
| 32%   36C    P8             19W /  285W |    3645MiB /  16376MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1101      G   /usr/lib/xorg/Xorg                       56MiB |
|    0   N/A  N/A            1328      G   /usr/bin/gnome-shell                      7MiB |
|    0   N/A  N/A          816643      C   ...khatib/envs/simvla/bin/python       3556MiB |
+-----------------------------------------------------------------------------------------+
```
```text
root         644  0.0  0.0  44060 21952 ?        Ss   May12   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         952  0.0  0.0 121084 24012 ?        Ssl  May12   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
rootalk+  816642  0.0  0.0  12844  2152 ?        S    May13   0:00 bash -c cd ~/test/reda_ws/intern_ship_ws && nohup /home/rootalkhatib/envs/simvla/bin/python simvla/code/SimVLA/evaluation/libero/serve_smolvlm_libero.py --checkpoint ~/test/reda_ws/checkpoints/simvla_ckpt_50000/ckpt-50000 --smolvlm_model HuggingFaceTB/SmolVLM-500M-Instruct --norm_stats ~/test/reda_ws/intern_ship_ws/simvla/code/SimVLA/norm_stats/libero_norm.json > server.log 2>&1 &
```

## 2. Full Job Manifest Table

The table keeps commands as references to exact command blocks below to avoid unreadable table wrapping. The exact commands are included immediately after the table.

| job_id | machine | current status | priority | dependencies | expected outputs | log file | status file | max retries | retry/attempt | GPU | est. duration | start | end | failure/skip reason | purpose | command ref |
|---|---|---:|---:|---|---|---|---|---:|---:|---:|---:|---|---|---|---|---|
| `smoke_bob_cpu` | bob | DONE | 1 | none | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_bob_cpu.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json` | 1 | 1 | False | 1.0h |  | 2026-05-15T15:09:43+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: smoke_bob_cpu` |
| `smoke_sam_cpu` | sam | DONE | 1 | none | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_sam_cpu.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json` | 1 | 1 | False | 1.0h |  | 2026-05-15T15:09:44+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: smoke_sam_cpu` |
| `smoke_dependency_child` | bob | DONE | 2 | smoke_bob_cpu | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_dependency_child.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json` | 1 | 1 | False | 1.0h |  | 2026-05-15T15:09:51+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: smoke_dependency_child` |
| `smoke_retry_failure` | bob | DONE | 2 | none | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_retry_failure.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json` | 2 | 2 | False | 1.0h |  | 2026-05-15T15:10:18+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: smoke_retry_failure` |
| `libero_pro_pilot_bob` | bob | DONE | 10 | none | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_pilot_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json` | 1 | 1 | True | 28h |  | 2026-05-15T16:00:59+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: libero_pro_pilot_bob` |
| `stage8_sam_model_sweep` | sam | DONE | 11 | none | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_object_model_sweep.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_model_sweep.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json` | 1 | 1 | False | 18h |  | 2026-05-15T15:39:23+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: stage8_sam_model_sweep` |
| `stage8_sam_calibration_sweep` | sam | DONE | 20 | stage8_sam_model_sweep | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_calibration_sweep.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json` | 1 | 1 | False | 2h |  | 2026-05-15T15:39:35+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: stage8_sam_calibration_sweep` |
| `flowtrace_experiments_sam` | sam | DONE | 24 | stage8_sam_model_sweep | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/flowtrace_experiments_sam.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/flowtrace_experiments_sam.json` | 1 | 1 | False | 16h |  | 2026-05-15T16:14:44+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: flowtrace_experiments_sam` |
| `target_sweep_sam` | sam | DONE | 25 | stage8_sam_model_sweep | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_target_comparison.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/target_sweep_sam.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/target_sweep_sam.json` | 1 | 1 | False | 16h |  | 2026-05-15T16:14:55+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: target_sweep_sam` |
| `architecture_loss_sweep_sam` | sam | DONE | 26 | stage8_sam_model_sweep | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_model_sweep_results.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/architecture_loss_sweep_sam.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json` | 1 | 1 | False | 24h |  | 2026-05-15T16:49:59+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: architecture_loss_sweep_sam` |
| `normal_libero_hard_baseline_bob` | bob | DONE | 30 | libero_pro_pilot_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_baseline.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/normal_libero_hard_baseline_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_baseline_bob.json` | 1 | 1 | True | 24h |  | 2026-05-15T19:41:31+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: normal_libero_hard_baseline_bob` |
| `libero_pro_expanded_rollout_bob` | bob | RUNNING | 31 | normal_libero_hard_baseline_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_rollout_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_rollout_bob.json` | 1 | 1 | True | 42h | 2026-05-15T19:41:33+02:00 |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: libero_pro_expanded_rollout_bob` |
| `flowtrace_medium_bob` | bob | PENDING | 40 | libero_pro_pilot_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/flowtrace_medium_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/flowtrace_medium_bob.json` | 1 |  | True | 12h |  |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: flowtrace_medium_bob` |
| `calibration_mega_sam` | sam | DONE | 50 | architecture_loss_sweep_sam | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/calibration_mega_sam.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/calibration_mega_sam.json` | 1 | 1 | False | 8h |  | 2026-05-15T16:50:11+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: calibration_mega_sam` |
| `normal_libero_hard_30eps_bob` | bob | PENDING | 60 | flowtrace_medium_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/normal_libero_hard_30eps_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_30eps_bob.json` | 1 |  | True | 42h |  |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: normal_libero_hard_30eps_bob` |
| `libero_pro_expanded_30eps_bob` | bob | PENDING | 70 | libero_pro_expanded_rollout_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_30eps_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_expanded_30eps_bob.json` | 1 |  | True | 60h |  |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: libero_pro_expanded_30eps_bob` |
| `history_models_sam` | sam | DONE | 80 | target_sweep_sam | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_history_models.md` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/history_models_sam.log` | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/history_models_sam.json` | 1 | 1 | False | 1h |  | 2026-05-15T16:15:03+02:00 |  | Unmapped Stage 8 job; inspect exact command. | `Command: history_models_sam` |
| `switch_policy_analysis_bob` | bob | PENDING | 90 | libero_pro_expanded_rollout_bob, normal_libero_hard_30eps_bob | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/switch_policy_analysis_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/switch_policy_analysis_bob.json` | 1 |  | False | 2h |  |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: switch_policy_analysis_bob` |
| `stage8_final_report_bob` | bob | PENDING | 999 | switch_policy_analysis_bob, calibration_mega_sam, history_models_sam | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_final_report_bob.log` | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_final_report_bob.json` | 1 |  | False | 1h |  |  |  | Unmapped Stage 8 job; inspect exact command. | `Command: stage8_final_report_bob` |

### Exact Commands From Manifest

#### Command: `smoke_bob_cpu`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/results && echo bob_ok > asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt
```

#### Command: `smoke_sam_cpu`
```bash
cd /home/rootalkhatib/test/reda_ws && mkdir -p asynchvla_ws/stage8_ultimate/results && echo sam_ok > asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt
```

#### Command: `smoke_dependency_child`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt > asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt
```

#### Command: `smoke_retry_failure`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws"; f=asynchvla_ws/stage8_ultimate/results/smoke_retry_counter.txt; n=0; [ -f "$f" ] && n=$(cat "$f"); n=$((n+1)); echo $n > "$f"; if [ "$n" -lt 2 ]; then echo intentional_fail; exit 7; fi; echo retry_ok > asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt
```

#### Command: `libero_pro_pilot_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_libero_pro_pilot.sh
```

#### Command: `stage8_sam_model_sweep`
```bash
cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/reports && for split in holdout_libero_object holdout_object_bowl holdout_libero_spatial; do timeout 14400 python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split "$split" --variants action_only_baseline full_old_baseline context_gated_action seed_relative_pairwise per_step_error_head full_engineered_simvla_focused --epochs 80 --out-prefix stage8_${split}_model_sweep || echo "WARN model_sweep failed $split"; done; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.json asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
```

#### Command: `stage8_sam_calibration_sweep`
```bash
cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py && cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration*.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
```

#### Command: `flowtrace_experiments_sam`
```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_flowtrace_experiments.sh
```

#### Command: `target_sweep_sam`
```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_target_sweep.sh
```

#### Command: `architecture_loss_sweep_sam`
```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_architecture_sweep.sh
```

#### Command: `normal_libero_hard_baseline_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_normal_libero_hard_baseline.sh
```

#### Command: `libero_pro_expanded_rollout_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=5 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
```

#### Command: `flowtrace_medium_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && source asynchvla_ws/scripts/activate_simvla_bob.sh && python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json --split-name stage8_flowtrace_medium --max-contexts 300 --max-calib 100 --max-test-id 100 --max-test-ood 100 --cap-per-file 40 --simvla-seeds 0 1 2 3 4 && python3 - <<'PY'
from pathlib import Path
import torch
base=Path('asynchvla_ws/data/processed_stage7_flow/stage8_flowtrace_medium')
lines=['# Stage 8 Flowtrace Results','',f'Dataset: `{base}`','']
for p in sorted(base.glob('flowtrace_multiseed_trace_*.pt')):
 d=torch.load(p,map_location='cpu'); samples=d.get('samples',[]); lines.append(f'- `{p.name}`: {len(samples)} contexts, seeds={d.get("seeds")}')
Path('asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md').write_text('\n'.join(lines)+'\n')
PY
```

#### Command: `calibration_mega_sam`
```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_calibration_mega.sh
```

#### Command: `normal_libero_hard_30eps_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=30 bash asynchvla_ws/scripts/stage8_run_normal_libero_hard_30.sh
```

#### Command: `libero_pro_expanded_30eps_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=30 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
```

#### Command: `history_models_sam`
```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_history_models.sh
```

#### Command: `switch_policy_analysis_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_switch_policy_analysis.sh
```

#### Command: `stage8_final_report_bob`
```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && python3 asynchvla_ws/scripts/stage8_write_final_report.py
```

## 3. Completed Jobs: Exact Details

### `smoke_bob_cpu`

- Machine: `bob`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/results && echo bob_ok > asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_bob_cpu.log`.
- Status file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_bob_cpu.json`.
- Output files validity: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:09:43+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Purpose: infrastructure smoke only; no scientific metrics.

### `smoke_sam_cpu`

- Machine: `sam`.
- Command: ```bash
cd /home/rootalkhatib/test/reda_ws && mkdir -p asynchvla_ws/stage8_ultimate/results && echo sam_ok > asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_sam_cpu.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_sam_cpu.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_sam_cpu.txt`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:09:44+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Purpose: infrastructure smoke only; no scientific metrics.

### `smoke_dependency_child`

- Machine: `bob`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/results/smoke_bob_cpu.txt > asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_dependency_child.log`.
- Status file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_dependency_child.json`.
- Output files validity: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_dependency_child.txt`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:09:51+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Purpose: infrastructure smoke only; no scientific metrics.

### `smoke_retry_failure`

- Machine: `bob`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws"; f=asynchvla_ws/stage8_ultimate/results/smoke_retry_counter.txt; n=0; [ -f "$f" ] && n=$(cat "$f"); n=$((n+1)); echo $n > "$f"; if [ "$n" -lt 2 ]; then echo intentional_fail; exit 7; fi; echo retry_ok > asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/smoke_retry_failure.log`.
- Status file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/smoke_retry_failure.json`.
- Output files validity: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/results/smoke_retry_success.txt`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:10:18+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Purpose: infrastructure smoke only; no scientific metrics.

### `libero_pro_pilot_bob`

- Machine: `bob`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_libero_pro_pilot.sh
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_pilot_bob.log`.
- Status file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/libero_pro_pilot_bob.json`.
- Output files validity: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_pilot_results.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:00:59+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Scientific result: partial LIBERO-PRO pilot. Only `libero_object_with_mug` produced JSON outputs; `libero_goal_object` and `libero_object_env` had missing `.pruned_init` files.
- Completed result files: `libero_object_with_mug_task0/1/2.json`.
- Most important metrics excerpt:
```markdown
# Stage 8 LIBERO-PRO Pilot Results

- Input dir: `asynchvla_ws/stage8_ultimate/results/libero_pro_pilot`
- Files: `3`
- Episodes: `75`

## Aggregate By Suite/Task/Mode

| suite | task | mode | episodes | success_rate | avg_steps | avg_unc | max_unc | avg_rejects | reward_sum |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| libero_object_with_mug | 0 | A_passive | 5 | 1.000 | 148.60 | 1.350 | 2.028 | 3.40 | 5.000 |
| libero_object_with_mug | 0 | B_deliberation | 5 | 1.000 | 203.20 | 1.298 | 2.094 | 3.60 | 5.000 |
| libero_object_with_mug | 0 | C_random_seed | 5 | 1.000 | 151.00 | 1.387 | 2.140 | 4.60 | 5.000 |
| libero_object_with_mug | 0 | D_low_uncertainty_reject_log | 5 | 1.000 | 148.60 | 1.350 | 2.028 | 3.40 | 5.000 |
| libero_object_with_mug | 0 | E_conservative_switch_proxy | 5 | 1.000 | 150.20 | 1.362 | 2.090 | 3.80 | 5.000 |
| libero_object_with_mug | 1 | A_passive | 5 | 1.000 | 145.20 | 1.284 | 2.020 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | B_deliberation | 5 | 1.000 | 135.20 | 1.365 | 2.092 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | C_random_seed | 5 | 0.800 | 225.60 | 1.264 | 2.036 | 3.80 | 4.000 |
| libero_object_with_mug | 1 | D_low_uncertainty_reject_log | 5 | 1.000 | 145.20 | 1.284 | 2.020 | 3.60 | 5.000 |
| libero_object_with_mug | 1 | E_conservative_switch_proxy | 5 | 1.000 | 155.60 | 1.278 | 2.069 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | A_passive | 5 | 1.000 | 149.20 | 1.401 | 2.067 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | B_deliberation | 5 | 1.000 | 190.60 | 1.339 | 2.239 | 5.00 | 5.000 |
| libero_object_with_mug | 2 | C_random_seed | 5 | 0.800 | 263.00 | 1.297 | 2.084 | 5.80 | 4.000 |
| libero_object_with_mug | 2 | D_low_uncertainty_reject_log | 5 | 1.000 | 149.20 | 1.401 | 2.067 | 4.20 | 5.000 |
| libero_object_with_mug | 2 | E_conservative_switch_proxy | 5 | 1.000 | 149.40 | 1.389 | 2.085 | 4.80 | 5.000 |

## Episode Rows
```

### `stage8_sam_model_sweep`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && mkdir -p asynchvla_ws/stage8_ultimate/reports && for split in holdout_libero_object holdout_object_bowl holdout_libero_spatial; do timeout 14400 python3 asynchvla_ws/src/rater_stage6/run_stage6_experiments.py --split "$split" --variants action_only_baseline full_old_baseline context_gated_action seed_relative_pairwise per_step_error_head full_engineered_simvla_focused --epochs 80 --out-prefix stage8_${split}_model_sweep || echo "WARN model_sweep failed $split"; done; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true; cp asynchvla_ws/outputs/reports/stage6/stage8_*_model_sweep.json asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_model_sweep.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_model_sweep.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_holdout_libero_object_model_sweep.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:39:23+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Datasets: `holdout_libero_object`, `holdout_object_bowl`, `holdout_libero_spatial`.
- Variants tested: `action_only_baseline`, `full_old_baseline`, `context_gated_action`, `seed_relative_pairwise`, `per_step_error_head`, `full_engineered_simvla_focused`.
- Training target: chunk-level normalized action L2 error from existing candidate datasets.
- Losses/architectures: Huber regression for ordinary regressors; pairwise auxiliary ranking loss for `seed_relative_pairwise`; per-step Huber plus chunk Huber for `per_step_error_head`.
- Key model-sweep summary:
### `stage8_holdout_libero_object_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.732 | 1.6146127796173095 | 1.6617511279582977 | 1.592023931980133 | 0.696448 |
| `full_old_baseline` | `test_ood` | 0.8088 | 1.6057030193805695 | 1.6617511279582977 | 1.592023931980133 | 0.8974201904761906 |
| `context_gated_action` | `test_ood` | 0.9148 | 1.5985954656600951 | 1.6617511279582977 | 1.592023931980133 | 0.9673478095238094 |
| `seed_relative_pairwise` | `test_ood` | 0.892 | 1.5981725873947144 | 1.6617511279582977 | 1.592023931980133 | 0.9796906666666666 |
| `per_step_error_head` | `test_ood` | 0.896 | 1.5978919959068298 | 1.6617511279582977 | 1.592023931980133 | 0.9428175238095238 |
| `full_engineered_simvla_focused` | `test_ood` | 0.9076 | 1.597651682138443 | 1.6617511279582977 | 1.592023931980133 | 0.9615542857142857 |

### `stage8_holdout_object_bowl_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.7344 | 1.5696335773468018 | 1.6193222782611847 | 1.5511432602405548 | 0.8518491428571429 |
| `full_old_baseline` | `test_ood` | 0.8724 | 1.5573115348815918 | 1.6193222782611847 | 1.5511432602405548 | 0.9916617142857144 |
| `context_gated_action` | `test_ood` | 0.9268 | 1.5548980807065964 | 1.6193222782611847 | 1.5511432602405548 | 0.9953493333333333 |
| `seed_relative_pairwise` | `test_ood` | 0.8986 | 1.556008264541626 | 1.6193222782611847 | 1.5511432602405548 | 0.994471619047619 |
| `per_step_error_head` | `test_ood` | 0.9004 | 1.5550851006507873 | 1.6193222782611847 | 1.5511432602405548 | 0.998208 |
| `full_engineered_simvla_focused` | `test_ood` | 0.902 | 1.5565832848548888 | 1.6193222782611847 | 1.5511432602405548 | 0.9975070476190475 |

### `stage8_holdout_libero_spatial_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.731 | 1.8844778707623482 | 1.9262300634384155 | 1.863301387131214 | 0.7777333333333333 |
| `full_old_baseline` | `test_ood` | 0.857 | 1.8685039988160133 | 1.9262300634384155 | 1.863301387131214 | 0.9575904761904762 |
| `context_gated_action` | `test_ood` | 0.909 | 1.864876043498516 | 1.9262300634384155 | 1.863301387131214 | 0.9542690476190475 |
| `seed_relative_pairwise` | `test_ood` | 0.928 | 1.865409253537655 | 1.9262300634384155 | 1.863301387131214 | 0.9882 |
| `per_step_error_head` | `test_ood` | 0.906 | 1.8655538269877434 | 1.9262300634384155 | 1.863301387131214 | 0.9577904761904762 |
| `full_engineered_simvla_focused` | `test_ood` | 0.9205 | 1.8656731334328651 | 1.9262300634384155 | 1.863301387131214 | 0.9483857142857143 |


### `stage8_sam_calibration_sweep`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && source asynchvla_ws/scripts/activate_simvla_sam.sh && export REDA_WS="/home/rootalkhatib/test/reda_ws" && python3 asynchvla_ws/src/calibration_stage8/run_calibration_sweep.py && cp asynchvla_ws/stage8_ultimate/reports/stage8_calibration*.md asynchvla_ws/stage8_ultimate/reports/ 2>/dev/null || true
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_calibration_sweep.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/stage8_sam_calibration_sweep.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_sweep_summary.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T15:39:35+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Calibration methods actually implemented in `run_calibration_sweep.py`: global residual conformal, SimVLA-only residual conformal, affine plus residual; binned residual code exists but is not emitted as a report method.
- Not implemented in this completed sweep: isotonic, Platt/logistic, quantile conformal, ensemble mean+std, small OOD calibration pools.
- Best-method excerpt:
```markdown
# Stage 8 Calibration Best Method

- `holdout_object_bowl` `full_old_baseline` `test_id_simvla` `affine_plus_residual_simvla` coverage=0.899 width=0.358
- `holdout_libero_spatial` `action_only_baseline` `test_id_all` `affine_plus_residual_all` coverage=0.899 width=0.582
- `holdout_scene_kitchen_scene2` `context_gated_action` `test_id_all` `affine_plus_residual_all` coverage=0.903 width=0.234
- `holdout_libero_spatial` `action_only_baseline` `test_id_all` `global_residual_all` coverage=0.896 width=0.603
- `holdout_scene_kitchen_scene2` `action_only_baseline` `test_id_all` `affine_plus_residual_simvla` coverage=0.896 width=0.646
- `holdout_libero_object` `action_only_baseline` `test_id_all` `affine_plus_residual_all` coverage=0.896 width=1.582
- `holdout_object_cabinet` `full_old_baseline` `test_ood_simvla` `affine_plus_residual_all` coverage=0.896 width=0.265
- `holdout_object_bowl` `full_old_baseline` `test_id_simvla` `global_residual_all` coverage=0.904 width=0.375
- `holdout_libero_object` `full_old_baseline` `test_ood_all` `affine_plus_residual_all` coverage=0.905 width=0.403
- `holdout_libero_spatial` `full_engineered_simvla_focused` `test_ood_simvla` `affine_plus_residual_all` coverage=0.895 width=0.243
```

### `flowtrace_experiments_sam`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_flowtrace_experiments.sh
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/flowtrace_experiments_sam.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/flowtrace_experiments_sam.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:14:44+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Manager status is `DONE` because an expected placeholder report exists.
- Internal experiment result: failed for all splits due hardcoded Bob path on Sam (`PermissionError: /media/rootalkhatib/My Passport`).
- Therefore `flowtrace_only`, `action_only + flowtrace`, `context_gated + flowtrace`, and `seed_relative + flowtrace` were **not scientifically evaluated** by this job.
- Log excerpt:
```text
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py", line 183, in <module>
    main()
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py", line 167, in main
    ROUT.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  [Previous line repeated 2 more times]
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
PermissionError: [Errno 13] Permission denied: '/media/rootalkhatib/My Passport'
[stage8] WARN flowtrace failed split=holdout_object_bowl
[stage8] flowtrace experiments split=holdout_libero_spatial
Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports/stage7'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs/reports'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/outputs'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/media/rootalkhatib/My Passport/reda_ws'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py", line 183, in <module>
    main()
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_flowtrace_experiments.py", line 167, in main
    ROUT.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1179, in mkdir
    self.parent.mkdir(parents=True, exist_ok=True)
  [Previous line repeated 2 more times]
  File "/home/rootalkhatib/envs/simvla/lib/python3.10/pathlib.py", line 1175, in mkdir
    self._accessor.mkdir(self, mode)
PermissionError: [Errno 13] Permission denied: '/media/rootalkhatib/My Passport'
[stage8] WARN flowtrace failed split=holdout_libero_spatial
[stage8] job flowtrace_experiments_sam exit 0 at 2026-05-15T16:14:42+02:00
```

### `target_sweep_sam`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_target_sweep.sh
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/target_sweep_sam.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/target_sweep_sam.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_target_comparison.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:14:55+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- Manager status is `DONE` because an expected placeholder report exists.
- Internal experiment result: failed. Multi-expert target builder looked for Bob-style paths on Sam and target experiment then hit missing `single_l2` target columns / empty parts.
- Therefore multi-expert K=5/10/20, softmin, pairwise target, bad-action target, and progress/success target were **not scientifically evaluated** by this job.
- Log excerpt:
```text
[stage8] job target_sweep_sam attempt 1 start 2026-05-15T16:14:37+02:00
Activated AsyncVLA Sam SimVLA env
  PYTHON_BIN=/home/rootalkhatib/envs/simvla/bin/python3
  REDA_WS=/home/rootalkhatib/test/reda_ws
Python 3.10.20
[stage8] building multi-expert targets split=holdout_libero_object
No split dir /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/processed_stage5/holdout_libero_object
[stage8] target experiments split=holdout_libero_object
Traceback (most recent call last):
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 134, in <module>
    main()
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 113, in main
    staged_split, parts = stage_temp_candidates(args.split, target_col, suffix)
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 64, in stage_temp_candidates
    raise KeyError(f"row missing target {target_col}: {list(new)[:6]}...")
KeyError: "row missing target single_l2: ['context_id', 'sample_id', 'task_name', 'source_hdf5', 'language_instruction', 'candidate_type']..."
[stage8] WARN target failed split=holdout_libero_object
[stage8] building multi-expert targets split=holdout_object_bowl
No split dir /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/processed_stage5/holdout_object_bowl
[stage8] target experiments split=holdout_object_bowl
Traceback (most recent call last):
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 134, in <module>
    main()
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 113, in main
    staged_split, parts = stage_temp_candidates(args.split, target_col, suffix)
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 64, in stage_temp_candidates
    raise KeyError(f"row missing target {target_col}: {list(new)[:6]}...")
KeyError: "row missing target single_l2: ['context_id', 'sample_id', 'task_name', 'source_hdf5', 'language_instruction', 'candidate_type']..."
[stage8] WARN target failed split=holdout_object_bowl
[stage8] building multi-expert targets split=holdout_libero_spatial
No split dir /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/processed_stage5/holdout_libero_spatial
[stage8] target experiments split=holdout_libero_spatial
[stage] target=single_l2 staged_split=holdout_libero_spatial__MET_single_l2 parts=[]
Traceback (most recent call last):
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 134, in <module>
    main()
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage7/run_stage7_multi_expert_target_experiments.py", line 118, in main
    res = train_variant(staged_split, v, epochs=args.epochs, quick=False)
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage6/run_stage6_experiments.py", line 72, in train_variant
    xtr,ytr,ystep_tr=build_matrix(train_rows,mode,seed_stats); xcal,ycal,ystep_cal=build_matrix(parts['calib'],mode,seed_stats)
  File "/home/rootalkhatib/test/reda_ws/asynchvla_ws/src/rater_stage6/run_stage6_experiments.py", line 34, in build_matrix
    ystep=torch.stack([r['true_per_step_l2_error'].float() for r in rows])
RuntimeError: stack expects a non-empty TensorList
[stage8] WARN target failed split=holdout_libero_spatial
[stage8] job target_sweep_sam exit 0 at 2026-05-15T16:14:50+02:00
```

### `architecture_loss_sweep_sam`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_architecture_sweep.sh
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/architecture_loss_sweep_sam.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/architecture_loss_sweep_sam.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_model_sweep_results.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:49:59+02:00`.
- Affects future jobs: dependencies using this job can now launch.

### `normal_libero_hard_baseline_bob`

- Machine: `bob`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_normal_libero_hard_baseline.sh
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/normal_libero_hard_baseline_bob.log`.
- Status file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/status/normal_libero_hard_baseline_bob.json`.
- Output files validity: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_baseline.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T19:41:31+02:00`.
- Affects future jobs: dependencies using this job can now launch.

### `calibration_mega_sam`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_calibration_mega.sh
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/calibration_mega_sam.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/calibration_mega_sam.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_calibration_mega_sweep.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:50:11+02:00`.
- Affects future jobs: dependencies using this job can now launch.

### `history_models_sam`

- Machine: `sam`.
- Command: ```bash
cd "/home/rootalkhatib/test/reda_ws" && bash asynchvla_ws/scripts/stage8_run_sam_history_models.sh
```
- Log file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/history_models_sam.log`.
- Status file: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/status/history_models_sam.json`.
- Output files validity: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_history_models.md`: exists.
- Start: `not tracked`.
- End: `2026-05-15T16:15:03+02:00`.
- Affects future jobs: dependencies using this job can now launch.
- This is a placeholder/report-only job. It did not train LSTM, GRU, Transformer, TCN, or Mamba.
- Reason: rollout sequence data is required before history models can be trained without leakage.
- Report excerpt:
```markdown
# Stage 8 History Models

Status: pending rollout sequence data.

History/window models require rollout traces with previous selected actions, previous uncertainty, proprio, and optionally VLM/flowtrace features. This job intentionally does not train a history model until rollout logs are available.

Planned windows:

- 2
- 4
- 8
- 16 as backup if enough data exists

Planned models:

- GRU/LSTM
- small Transformer
- TCN
- Mamba only if already installed

No future information, timestep, episode progress, or trajectory length will be used as inputs.
```

## 4. Running Jobs: Exact Details

### `libero_pro_expanded_rollout_bob`

- Machine: `bob`.
- PID: `776740`.
- Launch mode: manager-created `nohup` shell script `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/libero_pro_expanded_rollout_bob.sh`.
- Command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=5 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
```
- Log file: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_rollout_bob.log`.
- Last 50 log lines:
```text
  ep2 mode=A_passive success=True steps=168
  ep3 mode=A_passive success=True steps=141
  ep4 mode=A_passive success=True steps=155
[mode] B_deliberation
  ep0 mode=B_deliberation success=True steps=279
  ep1 mode=B_deliberation success=True steps=184
  ep2 mode=B_deliberation success=True steps=144
  ep3 mode=B_deliberation success=True steps=142
  ep4 mode=B_deliberation success=True steps=204
[mode] C_random_seed
  ep0 mode=C_random_seed success=True steps=274
  ep1 mode=C_random_seed success=False steps=600
  ep2 mode=C_random_seed success=True steps=144
  ep3 mode=C_random_seed success=True steps=140
  ep4 mode=C_random_seed success=True steps=157
[mode] D_low_uncertainty_reject_log
  ep0 mode=D_low_uncertainty_reject_log success=True steps=144
  ep1 mode=D_low_uncertainty_reject_log success=True steps=138
  ep2 mode=D_low_uncertainty_reject_log success=True steps=168
  ep3 mode=D_low_uncertainty_reject_log success=True steps=141
  ep4 mode=D_low_uncertainty_reject_log success=True steps=155
[done] wrote asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_object_with_mug_task2.json
[stage8] LIBERO-PRO expanded episodes=5 suite=libero_object_with_mug task=3 out=asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_object_with_mug_task3.json
/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages/transformers/utils/hub.py:110: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead.
  warnings.warn(
[robosuite WARNING] No private macro file found! (__init__.py:7)
[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)
[robosuite WARNING] To setup, run: python /home/rootalkhatib/envs/simvla/lib/python3.10/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)
[setup] device=cuda
[setup] loading SimVLA
`torch_dtype` is deprecated! Use `dtype` instead!
[LiberoJointActionSpace] Loaded state norm stats, dim=8
[LiberoJointActionSpace] Loaded actions norm stats, dim=7
[setup] loaded norm_stats from /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/norm_stats/libero_norm.json
[setup] loading rater
[setup] rater feature_mode=M3_gated_base kind=gated in_dim=1456
/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/benchmark/__init__.py:273: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  init_states = torch.load(init_states_path)
[info] Using default task order for benchmark 'libero_object_with_mug' (10 tasks).
[task] 'pick the chocolate pudding and place it in the basket', 50 init states
[mode] A_passive
  ep0 mode=A_passive success=True steps=141
  ep1 mode=A_passive success=True steps=143
  ep2 mode=A_passive success=True steps=141
  ep3 mode=A_passive success=True steps=143
  ep4 mode=A_passive success=True steps=142
[mode] B_deliberation
  ep0 mode=B_deliberation success=True steps=142
  ep1 mode=B_deliberation success=True steps=172
  ep2 mode=B_deliberation success=True steps=147
```
- Current progress: not detectable.
- Expected outputs: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`.
- Next dependent jobs after completion: `libero_pro_expanded_30eps_bob, switch_policy_analysis_bob`.
- Health: appears healthy.

## 5. Pending Jobs: Exact Future Plan

### `flowtrace_medium_bob`

- Machine: `bob`.
- Why pending: waits for dependencies or GPU availability. Dependency states: `libero_pro_pilot_bob=DONE`.
- What it will do: Unmapped Stage 8 job; inspect exact command.
- Exact command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && source asynchvla_ws/scripts/activate_simvla_bob.sh && python3 asynchvla_ws/src/data_building/build_flowtrace_multiseed_dataset.py --split-manifest asynchvla_ws/data/splits/holdout_libero_object.json --split-name stage8_flowtrace_medium --max-contexts 300 --max-calib 100 --max-test-id 100 --max-test-ood 100 --cap-per-file 40 --simvla-seeds 0 1 2 3 4 && python3 - <<'PY'
from pathlib import Path
import torch
base=Path('asynchvla_ws/data/processed_stage7_flow/stage8_flowtrace_medium')
lines=['# Stage 8 Flowtrace Results','',f'Dataset: `{base}`','']
for p in sorted(base.glob('flowtrace_multiseed_trace_*.pt')):
 d=torch.load(p,map_location='cpu'); samples=d.get('samples',[]); lines.append(f'- `{p.name}`: {len(samples)} contexts, seeds={d.get("seeds")}')
Path('asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md').write_text('\n'.join(lines)+'\n')
PY
```
- Expected output/report: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_flowtrace_results.md`.
- Idea tested: Unmapped Stage 8 job; inspect exact command.
- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.
- Success/failure metrics: flowtrace dataset existence, context counts, compact flow metadata availability..

### `normal_libero_hard_30eps_bob`

- Machine: `bob`.
- Why pending: waits for dependencies or GPU availability. Dependency states: `flowtrace_medium_bob=PENDING`.
- What it will do: Unmapped Stage 8 job; inspect exact command.
- Exact command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=30 bash asynchvla_ws/scripts/stage8_run_normal_libero_hard_30.sh
```
- Expected output/report: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_normal_libero_hard_task_results.md`.
- Idea tested: Unmapped Stage 8 job; inspect exact command.
- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.
- Success/failure metrics: hard-task success/progress at 30 episodes and whether uncertainty predicts slow/fail episodes..

### `libero_pro_expanded_30eps_bob`

- Machine: `bob`.
- Why pending: waits for dependencies or GPU availability. Dependency states: `libero_pro_expanded_rollout_bob=RUNNING`.
- What it will do: Unmapped Stage 8 job; inspect exact command.
- Exact command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && STAGE8_EPISODES=30 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
```
- Expected output/report: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_libero_pro_expanded_rollout_results.md`.
- Idea tested: Unmapped Stage 8 job; inspect exact command.
- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.
- Success/failure metrics: larger LIBERO-PRO success/progress and switch proxy stability..

### `switch_policy_analysis_bob`

- Machine: `bob`.
- Why pending: waits for dependencies or GPU availability. Dependency states: `libero_pro_expanded_rollout_bob=RUNNING, normal_libero_hard_30eps_bob=PENDING`.
- What it will do: Unmapped Stage 8 job; inspect exact command.
- Exact command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_run_switch_policy_analysis.sh
```
- Expected output/report: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/reports/stage8_switch_policy_results.md`.
- Idea tested: Unmapped Stage 8 job; inspect exact command.
- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.
- Success/failure metrics: accepted vs rejected risk, fallback seed policy, warning proxy summary..

### `stage8_final_report_bob`

- Machine: `bob`.
- Why pending: waits for dependencies or GPU availability. Dependency states: `switch_policy_analysis_bob=PENDING, calibration_mega_sam=DONE, history_models_sam=DONE`.
- What it will do: Unmapped Stage 8 job; inspect exact command.
- Exact command: ```bash
cd "/media/rootalkhatib/My Passport/reda_ws" && python3 asynchvla_ws/scripts/stage8_write_final_report.py
```
- Expected output/report: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md`.
- Idea tested: Unmapped Stage 8 job; inspect exact command.
- Why it matters: tests whether uncertainty is deployment-relevant beyond static action-L2 metrics.
- Success/failure metrics: complete artifact synthesis and final decision..

## 6. Backup Jobs / Watchdog Behavior

- Watchdog script: `asynchvla_ws/scripts/stage8_watchdog.py`.
- Watchdog interval: every `600` seconds.
- Watchdog duration: up to `72` hours from launch.
- It checks job status through `stage8_job_manager.py status`.
- It checks Bob/Sam GPU usage for dashboard display.
- If a machine is idle and has pending work, it calls `stage8_job_manager.py launch-ready --limit 2`.
- If a job failed, retry behavior is handled by `stage8_job_manager.py launch-ready`; it retries while `attempt <= max_retries`.
- If the main queue becomes empty before 72 hours, the watchdog adds backup jobs.

### Backup Jobs Implemented In Code

| backup job | machine | purpose |
|---|---|---|
| `backup_libero_pro_30eps_bob` | Bob | more LIBERO-PRO rollout episodes using `stage8_run_libero_pro_expanded.sh` with 30 episodes/task |
| `backup_normal_libero_50eps_bob` | Bob | normal LIBERO hard tasks at 50 episodes/task |
| `backup_sam_calibration_extra` | Sam | extra q=0.95 calibration sweep |
| `backup_sam_model_extra_seeds` | Sam | extra training for `context_gated_action` and `seed_relative_pairwise` on `holdout_libero_object` |
| `backup_flowtrace_large_bob` | Bob | larger flowtrace extraction for `holdout_libero_object` |

### What The Watchdog Does Not Fully Do

- It does not directly copy the dashboard to Batman every hour. A separate Batman-side local collector process was previously launched for report copying; the watchdog itself only writes the Bob dashboard.
- It does not add new instruction-perturbation or environment-perturbation jobs beyond the existing valid-suite list.
- It does not add real history model training; history training still needs rollout sequence data.

### Watchdog Code Excerpt
```python
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
```

## 7. Ideas Coverage Checklist

| item | status | explanation |
|---|---:|---|
| A. LIBERO-PRO setup/import/reset | DONE | Smoke passed; LIBERO-PRO repo/config available and env reset/rollout works. |
| A. LIBERO-PRO pilot rollout | DONE | Completed only for `libero_object_with_mug`; other attempted suites hit missing init states. |
| A. LIBERO-PRO expanded rollout | QUEUED | `libero_pro_expanded_rollout_bob` and 30eps job are pending. |
| A. object perturbation | DONE/QUEUED | `with_mug` done; more object perturbation variants queued. |
| A. initial-state perturbation | QUEUED | `libero_object_temp_x*` variants queued as position/init perturbation style tests. |
| A. instruction perturbation | NOT INCLUDED | No validated instruction-perturbation suite with local init states is in the manifest. |
| A. environment perturbation | BLOCKED | `libero_object_env` failed due missing `.pruned_init` files. |
| A. A_passive | DONE/RUNNING/QUEUED | Used in pilot and current/queued rollouts. |
| A. B_deliberation | DONE/RUNNING/QUEUED | Used in pilot and current/queued rollouts. |
| A. C_random_seed | DONE/RUNNING/QUEUED | Used in pilot and current/queued rollouts. |
| A. D_reject_log | DONE/RUNNING/QUEUED | `D_low_uncertainty_reject_log` used. |
| A. E_conservative_switch_proxy | DONE | Used in pilot and normal hard baseline; not included in expanded LIBERO-PRO script. |
| B. hard task scan | DONE | Stage 7 hard scan identified tasks. |
| B. hard task 10 episodes | RUNNING | `normal_libero_hard_baseline_bob`. |
| B. hard task 30 episodes | QUEUED | `normal_libero_hard_30eps_bob`. |
| B. hard task 50 episodes backup | BACKUP ONLY | `backup_normal_libero_50eps_bob`. |
| B. libero_spatial task 5 | RUNNING | Currently being processed. |
| B. libero_goal task 0 | QUEUED | In normal hard scripts. |
| B. libero_goal task 9 | QUEUED | In normal hard scripts. |
| B. libero_10 task 0/1 | QUEUED | In normal hard scripts. |
| C. flowtrace extraction | QUEUED | `flowtrace_medium_bob`; Sam flowtrace experiment failed internally. |
| C. flowtrace_only | BLOCKED | Attempted on Sam but failed due path issue; not scientifically evaluated. |
| C. action_only + flowtrace | BLOCKED | Attempted on Sam but failed due path issue. |
| C. context_gated + flowtrace | BLOCKED | Attempted on Sam but failed due path issue. |
| C. seed_relative + flowtrace | BLOCKED | Attempted on Sam but failed due path issue. |
| D. single expert L2 | DONE/RUNNING | Base target in completed and running model sweeps. |
| D. multi-expert min-distance K=5 | BLOCKED | Target job failed due path/target-column issues. |
| D. multi-expert min-distance K=10 | BLOCKED | Target job failed. |
| D. multi-expert min-distance K=20 | BLOCKED | Target job failed. |
| D. softmin expert distance | BLOCKED | Target job failed. |
| D. pairwise seed ranking target | RUNNING | `seed_relative_pairwise` is in architecture sweep; true target-sweep pairwise job failed. |
| D. bad-action classification target | NOT INCLUDED | Not implemented in current runner; only AUROC evaluation exists. |
| D. rollout progress target | BLOCKED | Needs rollout/progress labels. |
| D. hybrid target | NOT INCLUDED | Deferred until target components work. |
| E. action_only_mlp | DONE/RUNNING | Completed first sweep; running architecture sweep. |
| E. full_old_mlp | DONE/RUNNING | Completed first sweep; running architecture sweep. |
| E. context_gated_action | DONE/RUNNING | Completed first sweep; running architecture sweep. |
| E. seed_relative_rater | RUNNING | Included in architecture sweep. |
| E. context_gated + seed_relative | NOT INCLUDED | No explicit combined architecture variant in manifest. |
| E. per_step_error_head | DONE/RUNNING | Completed first sweep; running architecture sweep. |
| E. pairwise_ranker | DONE/RUNNING | `seed_relative_pairwise` uses pairwise auxiliary loss. |
| E. heteroscedastic head | NOT INCLUDED | Model class exists, but no manifest variant uses it. |
| E. quantile heads | NOT INCLUDED | No q=0.8/0.9/0.95 quantile training job exists. |
| E. ensemble | BACKUP ONLY | Only backup extra seeds, not full ensemble calibration/training. |
| E. LSTM/GRU | NOT INCLUDED | History job is placeholder only. |
| E. Transformer | NOT INCLUDED | History job is placeholder only. |
| E. TCN | NOT INCLUDED | History job is placeholder only. |
| E. Mamba | NOT INCLUDED | Dependency/model not tested. |
| F. Huber | DONE/RUNNING | Main regression loss. |
| F. Huber + pairwise | DONE/RUNNING | `seed_relative_pairwise`. |
| F. Huber + bad-action BCE | NOT INCLUDED | Not in current runner. |
| F. quantile pinball | NOT INCLUDED | Not in current runner. |
| F. heteroscedastic NLL | NOT INCLUDED | Model code exists, no job uses it. |
| F. progress classification | BLOCKED | Needs rollout labels. |
| G. global residual conformal | DONE | Initial calibration sweep. |
| G. SimVLA-only conformal | DONE | Implemented as simvla residual mode in calibration sweep. |
| G. binned conformal 5 bins | NOT INCLUDED | Helper exists but report methods do not emit binned method. |
| G. binned conformal 10 bins | NOT INCLUDED | Not emitted. |
| G. affine+residual | DONE | Initial calibration sweep. |
| G. isotonic regression | NOT INCLUDED | No current implementation. |
| G. Platt/logistic | NOT INCLUDED | No current implementation. |
| G. quantile conformal | NOT INCLUDED | No quantile model/conformal job. |
| G. ensemble mean+std | NOT INCLUDED | No ensemble model available. |
| G. split/perturbation stratified | NOT INCLUDED | Placeholder text only. |
| G. small OOD calibration 10/25/50/100 | NOT INCLUDED | Not implemented. |
| H. accept/reject seed0 | DONE/RUNNING/QUEUED | D reject log and switch analysis. |
| H. conservative fallback lowest-uncertainty seed | DONE | Pilot and normal hard baseline include E; expanded LIBERO-PRO does not. |
| H. warning/intervention proxy | QUEUED | Switch analysis over logs. |
| H. oracle expert fallback | NOT INCLUDED | No expert-action runtime substitution job. |

## 8. Current Best-Known Results

- Best LIBERO-PRO result so far: `libero_object_with_mug` pilot. `A_passive`, `B_deliberation`, `D_reject_log`, and `E_conservative_switch_proxy` reached 100% success on tasks 0-2 except random-seed mode lost one episode each on tasks 1 and 2. This is a small/easy pilot, not final evidence.
- Best normal-LIBERO hard-task result: not available yet; hard-task benchmark is running.
- Best model so far: Stage 6/early Stage 8 controlled-OOD reports still point to context-aware variants. In the first Sam sweep, `context_gated_action`, `seed_relative_pairwise`, `per_step_error_head`, and `full_engineered_simvla_focused` substantially beat action-only on AUROC; exact winner varies by split.
- Best action-only baseline: completed in `stage8_sam_model_sweep`; action-only is weaker on controlled OOD AUROC than context-aware variants in the parsed sweep.
- Best context-aware result: `context_gated_action` / `seed_relative_pairwise` / `full_engineered_simvla_focused` depending split; running architecture sweep should refine this.
- Best calibration method: current report ranks residual/affine residual variants, but calibration coverage remains a partial controlled-OOD analysis, not LIBERO-PRO rollout-risk calibration.
- Best switch proxy result: not available yet beyond pilot; switch analysis is pending.
- Biggest failure/blocker: LIBERO-PRO missing init states for some suites, plus Sam flowtrace/target jobs internally failed due Bob-path assumptions.

### Current Parsed Model Sweep Summary

### `stage8_holdout_libero_object_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.732 | 1.6146127796173095 | 1.6617511279582977 | 1.592023931980133 | 0.696448 |
| `full_old_baseline` | `test_ood` | 0.8088 | 1.6057030193805695 | 1.6617511279582977 | 1.592023931980133 | 0.8974201904761906 |
| `context_gated_action` | `test_ood` | 0.9148 | 1.5985954656600951 | 1.6617511279582977 | 1.592023931980133 | 0.9673478095238094 |
| `seed_relative_pairwise` | `test_ood` | 0.892 | 1.5981725873947144 | 1.6617511279582977 | 1.592023931980133 | 0.9796906666666666 |
| `per_step_error_head` | `test_ood` | 0.896 | 1.5978919959068298 | 1.6617511279582977 | 1.592023931980133 | 0.9428175238095238 |
| `full_engineered_simvla_focused` | `test_ood` | 0.9076 | 1.597651682138443 | 1.6617511279582977 | 1.592023931980133 | 0.9615542857142857 |

### `stage8_holdout_object_bowl_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.7344 | 1.5696335773468018 | 1.6193222782611847 | 1.5511432602405548 | 0.8518491428571429 |
| `full_old_baseline` | `test_ood` | 0.8724 | 1.5573115348815918 | 1.6193222782611847 | 1.5511432602405548 | 0.9916617142857144 |
| `context_gated_action` | `test_ood` | 0.9268 | 1.5548980807065964 | 1.6193222782611847 | 1.5511432602405548 | 0.9953493333333333 |
| `seed_relative_pairwise` | `test_ood` | 0.8986 | 1.556008264541626 | 1.6193222782611847 | 1.5511432602405548 | 0.994471619047619 |
| `per_step_error_head` | `test_ood` | 0.9004 | 1.5550851006507873 | 1.6193222782611847 | 1.5511432602405548 | 0.998208 |
| `full_engineered_simvla_focused` | `test_ood` | 0.902 | 1.5565832848548888 | 1.6193222782611847 | 1.5511432602405548 | 0.9975070476190475 |

### `stage8_holdout_libero_spatial_model_sweep.json`

| variant | test split used | SimVLA pairwise | predicted-best error | seed0 error | oracle error | AUROC top-30/worst |
|---|---|---:|---:|---:|---:|---:|
| `action_only_baseline` | `test_ood` | 0.731 | 1.8844778707623482 | 1.9262300634384155 | 1.863301387131214 | 0.7777333333333333 |
| `full_old_baseline` | `test_ood` | 0.857 | 1.8685039988160133 | 1.9262300634384155 | 1.863301387131214 | 0.9575904761904762 |
| `context_gated_action` | `test_ood` | 0.909 | 1.864876043498516 | 1.9262300634384155 | 1.863301387131214 | 0.9542690476190475 |
| `seed_relative_pairwise` | `test_ood` | 0.928 | 1.865409253537655 | 1.9262300634384155 | 1.863301387131214 | 0.9882 |
| `per_step_error_head` | `test_ood` | 0.906 | 1.8655538269877434 | 1.9262300634384155 | 1.863301387131214 | 0.9577904761904762 |
| `full_engineered_simvla_focused` | `test_ood` | 0.9205 | 1.8656731334328651 | 1.9262300634384155 | 1.863301387131214 | 0.9483857142857143 |


## 9. Risk Assessment

- Could the queue finish before 72 hours? Yes on Sam; Bob rollout jobs are likely the bottleneck. The watchdog can add backups only after the full queue drains.
- Could Bob become idle? Less likely while rollout jobs remain. If Bob becomes idle and pending dependencies are satisfied, watchdog should launch the next Bob job.
- Could Sam become idle? Yes after `architecture_loss_sweep_sam` and `calibration_mega_sam`; backup Sam jobs exist but are limited.
- Are there enough backup jobs? Partially. There are backup LIBERO-PRO, hard-task, calibration, model-seed, and flowtrace jobs. There are no backup instruction-perturbation or real history-training jobs.
- Are failed jobs retried? Yes, up to each job's `max_retries`; however internal failures hidden behind `|| echo WARN` can still exit 0 and be marked DONE if placeholder reports exist.
- Are logs copied locally? A separate Batman-side local collector was launched earlier. The watchdog itself does not directly copy reports hourly despite the desired behavior.
- Is final report guaranteed to run? Not guaranteed before 72h; it depends on `switch_policy_analysis_bob`, `calibration_mega_sam`, and `history_models_sam`. If Bob rollout dependencies run long, final report may not launch before the user checks.
- What happens if LIBERO-PRO fails? Broken suites are logged as warnings and skipped by scripts; expanded jobs use suites with known local init states to reduce this risk.
- What happens if Sam fails? Sam jobs can retry once if the manager observes FAILED. But path bugs that exit 0 with placeholder reports will not be retried automatically.
- What happens if calibration jobs fail? Dependent final report may wait or fail depending status; backup calibration exists only if queue drains.
- Additional risk: old `stage8_scheduler_loop.sh` processes are still running alongside the new watchdog. The manager prevents duplicate completed jobs, but multiple launchers could race on pending jobs. No jobs were killed because this task is audit-only.

## 10. Recommended Correction Before Leaving

This report is audit-only and did not apply corrections. Recommended corrections if the user explicitly approves later:

1. Stop or disable the older `stage8_scheduler_loop.sh` processes and keep only `stage8_watchdog.py`, to avoid two launch controllers racing.
2. Fix Sam path portability in `run_stage7_flowtrace_experiments.py` and `run_stage7_multi_expert_target_experiments.py` by honoring `REDA_WS`, then rerun `flowtrace_experiments_sam` and `target_sweep_sam` as real jobs.
3. Change flowtrace/target wrapper scripts so internal experiment failures return non-zero instead of writing placeholder success reports.
4. Add real implementations for binned conformal output, isotonic/Platt/quantile calibration, heteroscedastic and quantile model variants, and small-OOD calibration pools if those are required for Stage 8 claims.
5. Add a Sam idle backup chain after `calibration_mega_sam`, because Sam may finish far earlier than Bob.
6. Add only validated LIBERO-PRO suites with existing `.pruned_init` files; do not use `libero_object_env` until data is fixed.

## 11. How The User Can Check Later

### Check dashboard
```bash
ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md'
```
### Check watchdog
```bash
ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && ps -fp $(cat asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid) && tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log'
```
### Check Bob GPU
```bash
ssh pcrobot 'nvidia-smi'
```
### Check Sam GPU
```bash
ssh sam 'nvidia-smi'
```
### Check final report
```bash
ssh pcrobot 'test -f "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md" && tail -80 "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/ASYNCVLA_SIMVLA_STAGE8_ULTIMATE_EXPERIMENT_REPORT.md" || echo not_ready'
```
### Collect reports
```bash
bash "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/stage8_collect_reports.sh"
```

## 12. Duplicate Report Check

```text
/home/redafrix/tests/internship/codex_reports/stage8/NEW_QUEUE_EXPANSION_READ/01_stage8_three_day_queue_expansion.md
/home/redafrix/tests/internship/codex_reports/stage8/NEW_QUEUE_EXPANSION_READ/02_stage8_watchdog_launch_report.md
/home/redafrix/tests/internship/codex_reports/stage8/NEW_QUEUE_EXPANSION_READ/README.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/01_stage8_plan_and_smoke_status.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/02_stage8_libero_pro_setup_and_smoke.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/03_stage8_queue_launch_status.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/04_stage8_live_dashboard.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/05_stage8_calibration_best_method.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/06_stage8_three_day_queue_expansion.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/07_stage8_watchdog_launch_report.md
/home/redafrix/tests/internship/codex_reports/stage8/READ_FIRST/README_READ_FIRST.md
/home/redafrix/tests/internship/codex_reports/stage8/sam_stage8_sam_training_smoke.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_best_method.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_by_domain.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_smoke.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_sweep_summary.json
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_sweep_summary.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_calibration_threshold_transfer.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_full_orchestration_manifest_report.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_libero_pro_setup_and_smoke.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_live_dashboard.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.log
/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid
/home/redafrix/tests/internship/codex_reports/stage8/stage8_machine_roles.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_manager_smoke.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_plan_and_smoke_status.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_queue_launch_status.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_status_check.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_three_day_queue_expansion.md
/home/redafrix/tests/internship/codex_reports/stage8/stage8_watchdog_launch_report.md
/home/redafrix/tests/internship/codex_reports/stage8/status_check_latest/stage8_status_check.md
```
