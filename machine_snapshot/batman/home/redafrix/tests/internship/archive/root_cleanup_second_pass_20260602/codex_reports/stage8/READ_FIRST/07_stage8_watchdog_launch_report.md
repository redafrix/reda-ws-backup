# Stage 8 Watchdog Launch Report

Generated: `2026-05-15T16:16:39`

## 1. Is The Watchdog Running?

Yes. Verified process exists after launch.

## 2. PID / Session

- Launch mode: `nohup`
- PID file: `asynchvla_ws/stage8_ultimate/status/stage8_watchdog.pid`
- PID: `658116`
- Log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.nohup.log`
- Detailed tick log: `asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log`

## 3. Is Bob Active Or Queued?

Bob is active and queued. Current status includes a running normal LIBERO hard-task rollout and pending Bob rollout/flowtrace/switch/final jobs.

## 4. Is Sam Active Or Queued?

Sam is active and queued. The watchdog launched Sam jobs after detecting idle Sam. Current status includes the architecture/loss sweep running and calibration work pending.

## 5. Pending Job Count

Pending count at report time: `7`.

## 6. Backup Jobs If Queue Empties

The watchdog can add:

- `backup_libero_pro_30eps_bob`
- `backup_normal_libero_50eps_bob`
- `backup_sam_calibration_extra`
- `backup_sam_model_extra_seeds`
- `backup_flowtrace_large_bob`

These are added only if the main queue becomes empty before 72 hours.

## 7. Live Dashboard

- Bob: `asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md`
- Local duplicate path target: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_live_dashboard.md`

The existing Batman-side local collector continues duplicating reports periodically.

## 8. Exact Commands To Check Later

```bash
ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && bash asynchvla_ws/scripts/stage8_status.sh'
ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && tail -80 asynchvla_ws/stage8_ultimate/logs/stage8_watchdog.log'
ssh pcrobot 'cd "/media/rootalkhatib/My Passport/reda_ws" && cat asynchvla_ws/stage8_ultimate/reports/stage8_live_dashboard.md'
```

## Current Queue State

| job | machine | state | log |
|---|---|---:|---|
| `smoke_bob_cpu` | `bob` | DONE | `` |
| `smoke_sam_cpu` | `sam` | DONE | `` |
| `smoke_dependency_child` | `bob` | DONE | `` |
| `smoke_retry_failure` | `bob` | DONE | `` |
| `libero_pro_pilot_bob` | `bob` | DONE | `` |
| `stage8_sam_model_sweep` | `sam` | DONE | `` |
| `stage8_sam_calibration_sweep` | `sam` | DONE | `` |
| `flowtrace_experiments_sam` | `sam` | DONE | `` |
| `target_sweep_sam` | `sam` | DONE | `` |
| `architecture_loss_sweep_sam` | `sam` | RUNNING | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/architecture_loss_sweep_sam.log` |
| `normal_libero_hard_baseline_bob` | `bob` | RUNNING | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/normal_libero_hard_baseline_bob.log` |
| `libero_pro_expanded_rollout_bob` | `bob` | PENDING | `` |
| `flowtrace_medium_bob` | `bob` | PENDING | `` |
| `calibration_mega_sam` | `sam` | PENDING | `` |
| `normal_libero_hard_30eps_bob` | `bob` | PENDING | `` |
| `libero_pro_expanded_30eps_bob` | `bob` | PENDING | `` |
| `history_models_sam` | `sam` | DONE | `` |
| `switch_policy_analysis_bob` | `bob` | PENDING | `` |
| `stage8_final_report_bob` | `bob` | PENDING | `` |
