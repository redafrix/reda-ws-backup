# Stage 8 Final 72h Launch Report

Generated: `2026-05-15T21:19:39`

## Watchdog
- Watchdog is running; current process list is included below.
- Old `stage8_scheduler_loop.sh` processes were stopped; active experiment jobs were not killed.

## Current Queue State
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
    "command_file": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/jobs/stage8_sam_flowtrace_real.sh",
    "job_id": "stage8_sam_flowtrace_real",
    "log_path": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_flowtrace_real.log",
    "machine": "sam",
    "pid": "2422750",
    "started_at": "2026-05-15T21:18:28+02:00",
    "state": "RUNNING",
    "updated_at": "2026-05-15T21:18:28+02:00"
  },
  {
    "attempt": 1,
    "command_file": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/jobs/stage8_sam_target_real.sh",
    "job_id": "stage8_sam_target_real",
    "log_path": "/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_target_real.log",
    "machine": "sam",
    "pid": "2423059",
    "started_at": "2026-05-15T21:18:29+02:00",
    "state": "RUNNING",
    "updated_at": "2026-05-15T21:18:29+02:00"
  },
  {
    "job_id": "stage8_sam_arch_big",
    "machine": "sam",
    "state": "PENDING"
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
    "job_id": "stage8_sam_calibration_real",
    "machine": "sam",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_sam_history_real",
    "machine": "sam",
    "state": "PENDING"
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
    "job_id": "stage8_libero_pro_20eps_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_libero_pro_50eps_backup_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_normal_libero_50eps_backup_bob",
    "machine": "bob",
    "state": "PENDING"
  },
  {
    "job_id": "stage8_switch_policy_extended_bob",
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

## Current Processes
```text
rootalk+  658116  0.0  0.0  30504 15184 ?        S    16:14   0:00 python3 asynchvla_ws/scripts/stage8_watchdog.py --hours 72 --interval-sec 600
rootalk+  776740  0.0  0.0  12844  3604 ?        S    19:41   0:00 bash /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/jobs/libero_pro_expanded_rollout_bob.sh
rootalk+  776746  0.0  0.0  12844  3708 ?        S    19:41   0:00 bash asynchvla_ws/scripts/stage8_run_libero_pro_expanded.sh
rootalk+  835660  0.0  0.0  11248  2080 ?        S    21:17   0:00 timeout 14400 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_goal_with_mug --task-id 2 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_goal_with_mug_task2.json
rootalk+  835661  132 11.0 21997672 3531748 ?    Rl   21:17   2:57 python3 asynchvla_ws/src/eval_stage7/libero_execution_uncertainty_eval.py --task-suite libero_goal_with_mug --task-id 2 --num-episodes 5 --max-steps 600 --modes A_passive B_deliberation C_random_seed D_low_uncertainty_reject_log --resolution 128 --unc-threshold 1.75 --out asynchvla_ws/stage8_ultimate/results/libero_pro_expanded_5eps/libero_goal_with_mug_task2.json

```

## Dashboard Snapshot
```markdown
# Stage 8 Live Dashboard

Updated: `2026-05-15T21:19:05`

## Machine Summary

| machine | running | done | failed | pending | GPU |
|---|---:|---:|---:|---:|---|
| bob | 1 | 5 | 0 | 9 | `NVIDIA GeForce RTX 4070 Ti SUPER, 7282 MiB, 16376 MiB, 57 %` |
| sam | 2 | 8 | 0 | 3 | `NVIDIA GeForce RTX 4070 Ti SUPER, 7204 MiB, 16376 MiB, 87 %` |

## Running Jobs

- `stage8_sam_flowtrace_real` on `sam` log `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_flowtrace_real.log`
- `stage8_sam_target_real` on `sam` log `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_target_real.log`
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

- Running: `3`
- Pending: `12`
- Done: `13`
- Failed: `0`
- Backup jobs added this tick: `none`

## Blockers

- `libero_pro_pilot_bob.log` contains FileNotFoundError; likely missing LIBERO-PRO init states for some suites.
- `libero_pro_expanded_rollout_bob.log` contains FileNotFoundError; likely missing LIBERO-PRO init states for some suites.

```

## Added Real Backlog
- `stage8_sam_flowtrace_real`: builds flowtrace trace/candidate datasets and trains flowtrace variants.
- `stage8_sam_target_real`: builds/evaluates single-expert and multi-expert targets across controlled OOD splits.
- `stage8_sam_arch_big`: expanded architecture/loss sweep including heteroscedastic and quantile-head jobs.
- `stage8_sam_calibration_real`: calibration sweeps at 0.80/0.90/0.95.
- `stage8_sam_history_real`: history availability/report job after calibration.
- `stage8_libero_pro_20eps_bob` and `stage8_libero_pro_50eps_backup_bob`: long LIBERO-PRO rollout backlog.
- `stage8_normal_libero_50eps_backup_bob`: hard normal-LIBERO backup.
- `stage8_switch_policy_extended_bob`: switch analysis after rollouts/calibration.

## Current Running Jobs
- Bob: `libero_pro_expanded_rollout_bob`.
- Sam: `stage8_sam_flowtrace_real` and `stage8_sam_target_real`.

## Check Later
```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source "asynchvla_ws/scripts/activate_simvla_bob.sh"
bash asynchvla_ws/scripts/stage8_status.sh
cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md
tail -80 asynchvla_ws/stage8_ultimate/logs/libero_pro_expanded_rollout_bob.log
ssh sam 'cd "/home/rootalkhatib/test/reda_ws" && tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_sam_flowtrace_real.log && tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_sam_target_real.log'
```
