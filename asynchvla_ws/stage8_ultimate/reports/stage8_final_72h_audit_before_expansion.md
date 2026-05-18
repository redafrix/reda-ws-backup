# Stage 8 Final 72h Audit Before Expansion

Generated: `2026-05-15T21:10:55`

## stage8_status

```text
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

## live_dashboard

```text
# Stage 8 Live Dashboard

Updated: `2026-05-15T21:07:00`

## Machine Summary

| machine | running | done | failed | pending | GPU |
|---|---:|---:|---:|---:|---|
| bob | 1 | 5 | 0 | 5 | `NVIDIA GeForce RTX 4070 Ti SUPER, 7282 MiB, 16376 MiB, 79 %` |
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
- `libero_pro_expanded_rollout_bob.log` contains FileNotFoundError; likely missing LIBERO-PRO init states for some suites.

```

## manifest_head

```text
jobs 19
smoke_bob_cpu bob 1 False []
smoke_sam_cpu sam 1 False []
smoke_dependency_child bob 2 False ['smoke_bob_cpu']
smoke_retry_failure bob 2 False []
libero_pro_pilot_bob bob 10 True []
stage8_sam_model_sweep sam 11 False []
stage8_sam_calibration_sweep sam 20 False ['stage8_sam_model_sweep']
flowtrace_experiments_sam sam 24 False ['stage8_sam_model_sweep']
target_sweep_sam sam 25 False ['stage8_sam_model_sweep']
architecture_loss_sweep_sam sam 26 False ['stage8_sam_model_sweep']
normal_libero_hard_baseline_bob bob 30 True ['libero_pro_pilot_bob']
libero_pro_expanded_rollout_bob bob 31 True ['normal_libero_hard_baseline_bob']
flowtrace_medium_bob bob 40 True ['libero_pro_pilot_bob']
calibration_mega_sam sam 50 False ['architecture_loss_sweep_sam']
normal_libero_hard_30eps_bob bob 60 True ['flowtrace_medium_bob']
libero_pro_expanded_30eps_bob bob 70 True ['libero_pro_expanded_rollout_bob']
history_models_sam sam 80 False ['target_sweep_sam']
switch_policy_analysis_bob bob 90 False ['libero_pro_expanded_rollout_bob', 'normal_libero_hard_30eps_bob']
stage8_final_report_bob bob 999 False ['switch_policy_analysis_bob', 'calibration_mega_sam', 'history_models_sam']

```

## processes

```text
root         664  0.0  0.0  44060 21964 ?        Ss   May11   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         982  0.0  0.0 121084 23960 ?        Ssl  May11   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
rootalk+  629551  0.0  0.0  12844  2144 ?        S    15:29   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && mv /tmp/stage8_scheduler_loop.sh asynchvla_ws/scripts/stage8_scheduler_loop.sh && chmod +x asynchvla_ws/scripts/stage8_scheduler_loop.sh && nohup asynchvla_ws/scripts/stage8_scheduler_loop.sh > asynchvla_ws/stage8_ultimate/logs/stage8_scheduler_loop.nohup.log 2>&1 & echo $! > asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid && echo scheduler_started
rootalk+  629554  0.0  0.0  12844  3632 ?        S    15:29   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  629790  0.0  0.0  12844  3684 ?        S    15:29   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  631249  0.0  0.0  12844  3716 ?        Ss   15:30   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && python3 - <<PY import json, subprocess, datetime from pathlib import Path root=Path("/media/rootalkhatib/My Passport/reda_ws") rows=json.loads(subprocess.check_output(["python3","asynchvla_ws/scripts/stage8_job_manager.py","status"],cwd=root,text=True)) lines=["# Stage 8 Queue Launch Status","",f"Generated: `{datetime.datetime.now().isoformat(timespec=\"seconds\")}`","", "## Launched Jobs", "", "| job | machine | state | log |", "|---|---|---:|---|"] for r in rows:     lines.append(f"| {r.get(\"job_id\")} | {r.get(\"machine\",\"\")} | {r.get(\"state\",\"\")} | `{r.get(\"log_path\",\"\")}` |") lines += ["", "## Scheduler", "", "- Bob scheduler loop: `asynchvla_ws/scripts/stage8_scheduler_loop.sh`", "- Bob scheduler pid file: `asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid`", "- Batman local report collector pid file: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid`", "", "## Current Interpretation", "", "- LIBERO-PRO pilot is running on Bob and is the primary benchmark.", "- Sam model sweep is running in parallel.", "- Normal LIBERO hard-task baseline and flowtrace medium extraction are queued behind the LIBERO-PRO pilot to avoid GPU collision.", "- Sam calibration is queued behind the Sam model sweep."] (root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md").write_text("\n".join(lines)+"\n") print(root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md") PY
rootalk+  631250  0.0  0.0  12840  1932 ?        S    15:30   0:00 bash -c cd "/media/rootalkhatib/My Passport/reda_ws" && python3 - <<PY import json, subprocess, datetime from pathlib import Path root=Path("/media/rootalkhatib/My Passport/reda_ws") rows=json.loads(subprocess.check_output(["python3","asynchvla_ws/scripts/stage8_job_manager.py","status"],cwd=root,text=True)) lines=["# Stage 8 Queue Launch Status","",f"Generated: `{datetime.datetime.now().isoformat(timespec=\"seconds\")}`","", "## Launched Jobs", "", "| job | machine | state | log |", "|---|---|---:|---|"] for r in rows:     lines.append(f"| {r.get(\"job_id\")} | {r.get(\"machine\",\"\")} | {r.get(\"state\",\"\")} | `{r.get(\"log_path\",\"\")}` |") lines += ["", "## Scheduler", "", "- Bob scheduler loop: `asynchvla_ws/scripts/stage8_scheduler_loop.sh`", "- Bob scheduler pid file: `asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid`", "- Batman local report collector pid file: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid`", "", "## Current Interpretation", "", "- LIBERO-PRO pilot is running on Bob and is the primary benchmark.", "- Sam model sweep is running in parallel.", "- Normal LIBERO hard-task baseline and flowtrace medium extraction are queued behind the LIBERO-PRO pilot to avoid GPU collision.", "- Sam calibration is queued behind the Sam model sweep."] (root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md").write_text("\n".join(lines)+"\n") print(root/"asynchvla_ws/stage8_ultimate/reports/stage8_queue_launch_status.md") PY
rootalk+  631253  0.0  0.0  12844  3672 ?        S    15:30   0:00 bash asynchvla_ws/scripts/stage8_scheduler_loop.sh
rootalk+  658116  0.0  0.0  30504 15176 ?        S    16:14   0:00 python3 asynchvla_ws/scripts/stage8_watchdog.py --hours 72 --interval-sec 600
rootalk+  776740  0.0  0.0  12844  3604 ?        S    19:41   0:00 bash /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/libero_pro_expanded_rollout_bob.sh
rootalk+  776746  0.0  0.0  12844  3708 ?        S    19:41   0:00 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
rootalk+  825197  0.0  0.0  11248  2076 ?        S    21:00   0:00 timeout 14400 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_goal_with_mug --task-id 0 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_goal_with_mug_task0.json
rootalk+  825198  130 11.1 22149200 3574040 ?    Rl   21:00  13:22 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_goal_with_mug --task-id 0 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_goal_with_mug_task0.json
rootalk+  831393  1.0  0.0  24508 11664 ?        Ss   21:10   0:00 python3 -
rootalk+  851081  0.0  6.9 14518904 2216340 ?    S    May12   0:11 python3 marathon_c_50.py --idea 22
rootalk+ 3433103  0.0  0.0  14084  3808 ?        Ss   May13   0:00 tmux new-session -d -s stage5 -c /media/rootalkhatib/My Passport/reda_ws bash -l

```

## tmux

```text
stage5: 1 windows (created Wed May 13 17:01:26 2026)

```

## nvidia_smi

```text
Fri May 15 21:10:57 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.211.01             Driver Version: 570.211.01     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:A2:00.0 Off |                  N/A |
| 54%   79C    P2            168W /  285W |    7282MiB /  16376MiB |     82%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1148      G   /usr/lib/xorg/Xorg                       80MiB |
|    0   N/A  N/A            1586      G   /usr/bin/gnome-shell                      8MiB |
|    0   N/A  N/A          825198    C+G   python3                                4002MiB |
+-----------------------------------------------------------------------------------------+

```
