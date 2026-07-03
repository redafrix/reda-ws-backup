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
