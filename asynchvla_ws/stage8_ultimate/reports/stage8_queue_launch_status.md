# Stage 8 Queue Launch Status

Generated: `2026-05-15T15:31:13`

## Launched Jobs

| job | machine | state | log |
|---|---|---:|---|
| smoke_bob_cpu | bob | DONE | `` |
| smoke_sam_cpu | sam | DONE | `` |
| smoke_dependency_child | bob | DONE | `` |
| smoke_retry_failure | bob | DONE | `` |
| libero_pro_pilot_bob | bob | RUNNING | `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage8_ultimate/logs/libero_pro_pilot_bob.log` |
| stage8_sam_model_sweep | sam | RUNNING | `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage8_ultimate/logs/stage8_sam_model_sweep.log` |
| stage8_sam_calibration_sweep | sam | PENDING | `` |
| normal_libero_hard_baseline_bob | bob | PENDING | `` |
| flowtrace_medium_bob | bob | PENDING | `` |

## Scheduler

- Bob scheduler loop: `asynchvla_ws/scripts/stage8_scheduler_loop.sh`
- Bob scheduler pid file: `asynchvla_ws/stage8_ultimate/status/stage8_scheduler_loop.pid`
- Batman local report collector pid file: `/home/redafrix/tests/internship/codex_reports/stage8/stage8_local_collect_loop.pid`

## Current Interpretation

- LIBERO-PRO pilot is running on Bob and is the primary benchmark.
- Sam model sweep is running in parallel.
- Normal LIBERO hard-task baseline and flowtrace medium extraction are queued behind the LIBERO-PRO pilot to avoid GPU collision.
- Sam calibration is queued behind the Sam model sweep.
