# Stage 8 Final Plan Before 72h

Generated: `2026-05-15T21:10:36`

## Objective
Turn the current Stage 8 queue into a 72-hour unattended campaign with LIBERO-PRO as the primary benchmark, normal LIBERO as baseline/fallback, and Sam kept busy with real model/data/calibration work.

## Immediate Actions
- Audit current Bob/Sam jobs and GPU state.
- Remove obsolete `stage8_scheduler_loop.sh` processes only; keep `stage8_watchdog.py` and active experiment jobs.
- Patch Stage 7/8 scripts to honor `REDA_WS` on Sam instead of hard-coded Bob paths.
- Run real smoke tests for Sam flowtrace, multi-expert targets, model training, calibration, and history availability.
- Search Bob/Sam for previous uncertainty-feature assets and classify reusable vs TDQC/failure-only artifacts.
- Expand the manifest with real pending jobs for LIBERO-PRO rollout, hard-LIBERO baseline, flowtrace, targets, architectures/losses, calibration, history, switch analysis, and backups.
- Restart the watchdog only if needed to pick up backup-policy changes; do not kill active rollout jobs.

## Constraints
- No TDQC `.pt` files as primary training data.
- No final success/failure as only target.
- No timestep/progress/episode length as rater inputs.
- No competing Bob GPU rollout while Bob is busy.
- Failed wrappers must exit nonzero; placeholder success reports are not acceptable for new jobs.
