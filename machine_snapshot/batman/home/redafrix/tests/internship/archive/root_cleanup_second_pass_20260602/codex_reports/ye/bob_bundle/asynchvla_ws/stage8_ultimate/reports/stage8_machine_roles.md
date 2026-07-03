# Stage 8 Machine Roles

Generated: `2026-05-15T15:23:52`

## Bob

- Alias: `pcrobot`
- Workspace: `/media/rootalkhatib/My Passport/reda_ws`
- Branch: `bob`
- Role: rollout-heavy jobs, LIBERO-PRO pilot, normal LIBERO hard-task fallback, core final evaluation.
- GPU: RTX 4070 Ti SUPER, 16 GB class.
- Current status: LIBERO-PRO smoke, normal LIBERO smoke, calibration smoke, and flowtrace smoke passed.

## Sam

- Alias: `sam`
- Workspace: `/home/rootalkhatib/test/reda_ws`
- Branch: `sam`
- Role: model training, calibration sweeps, data/feature jobs. Sam rollout remains secondary until an explicit LIBERO-PRO rollout smoke passes there.
- GPU: RTX 4070 Ti SUPER, 16 GB class.
- Current status: Python/CUDA works; Stage 5 processed data and Stage 6 checkpoints are present; rater/training smoke passed. An older GPU process is present, so Stage 8 manager should not schedule Sam GPU-heavy jobs unless memory/process state is clear.

## Role Assignment

- Bob keeps the rollout queue busy.
- Sam runs CPU/lightweight training and calibration first.
- GPU-heavy Sam jobs are deferred until the old GPU process is cleared or proven safe.
