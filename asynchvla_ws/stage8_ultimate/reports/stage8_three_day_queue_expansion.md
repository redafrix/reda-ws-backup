# Stage 8 Three-Day Queue Expansion

Generated: `2026-05-15T16:16:39`

Scope: continued Stage 8 without restarting or killing existing jobs. Existing completed jobs were not duplicated. Running jobs were left running.

## Manifest Validation

- Manifest path: `asynchvla_ws/stage8_ultimate/configs/stage8_job_manifest.json`
- JSON validation: PASS via `python3 -m json.tool`.
- New shell scripts: syntax checked with `bash -n`.
- New Python scripts: compiled with `python3 -m py_compile`.
- Watchdog one-shot validation: PASS; it detected idle Sam and launched compatible pending Sam jobs.

## Job Groups Added

- Group A LIBERO-PRO expanded rollouts on Bob: `libero_pro_expanded_rollout_bob`, `libero_pro_expanded_30eps_bob`.
- Group B normal LIBERO hard-task scale-up on Bob: `normal_libero_hard_30eps_bob`.
- Group C flowtrace experiments on Sam: `flowtrace_experiments_sam`.
- Group D target sweep on Sam: `target_sweep_sam`.
- Group E architecture/loss sweep on Sam: `architecture_loss_sweep_sam`.
- Group F calibration mega-sweep on Sam: `calibration_mega_sam`.
- Group G history/window placeholder job on Sam: `history_models_sam`.
- Group H switch policy analysis on Bob: `switch_policy_analysis_bob`.
- Group I final report job on Bob: `stage8_final_report_bob`.

New job IDs:

- `flowtrace_experiments_sam`
- `target_sweep_sam`
- `architecture_loss_sweep_sam`
- `libero_pro_expanded_rollout_bob`
- `calibration_mega_sam`
- `normal_libero_hard_30eps_bob`
- `libero_pro_expanded_30eps_bob`
- `history_models_sam`
- `switch_policy_analysis_bob`
- `stage8_final_report_bob`

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

## Machine Assignment

- Bob remains rollout/evaluation focused.
- Sam remains model training, calibration, target, and feature focused.
- Sam is not assigned rollout jobs because Sam rollout environment has not been fully verified.

## Backup Policy

The 72-hour watchdog will add backup jobs if the queue empties before 72 hours:

- Backup A: more LIBERO-PRO rollout episodes.
- Backup B: more normal LIBERO hard-task episodes.
- Backup C: extra calibration sweeps.
- Backup D: extra model seeds.
- Backup E: additional OOD-style splits if available through existing manifests/jobs.
- Backup F: larger flowtrace datasets.
- Backup G: extra history-window reports/models if rollout data exists.

## Notes

- The previous `libero_object_env` LIBERO-PRO suite was avoided in expanded rollout jobs because the pilot found missing `.pruned_init` files.
- Expanded LIBERO-PRO jobs use suites that have local init states, including object/spatial/goal/10 perturbation variants and temperature/with-object variants.
- No TDQC `.pt` files are used as training data.
- No success/failure-only target is introduced as the only training target.
