# Stage 9 Final 20h Collection And Training Report

Generated: 2026-05-18
Latest update: 2026-05-19 09:15 CEST

## Current Status Update

The 20-hour run is still active.

Bob:

- Status: collecting LIBERO-PRO.
- Watchdog PID: `3106359`.
- Active collector PID at 2026-05-19 09:14 CEST: `3530823`.
- Active chunk: `bob_c003_libero_goal_with_mug_t3_seeds24-31`.
- Elapsed time: `13.61 / 20` hours.
- Approximate remaining time: `6.4` hours.
- GPU at check time: `9%`, `7280 MiB / 16376 MiB`.
- Disk: `1.4T` free on Bob workspace drive.

Sam:

- Status: sync/training support, not rollout collection.
- Watchdog PID: `595208`.
- Reason Sam is not collecting: Sam benchmark registry does not expose LIBERO-PRO `*_with_mug` suites; using normal LIBERO would violate the dataset requirement.
- Synced JSONL chunks at check time: `142`.
- Synced data size: `1.6G`.
- GPU at check time: `0%`, because the first baseline training run already completed.
- Disk: `192G` free.

Current Bob collection totals from live dashboard:

| Metric | Count |
|---|---:|
| Total samples | 36,608 |
| Total selected states | 1,426 |
| GOOD_STRONG | 17,326 |
| GOOD_WEAK | 3,731 |
| VALIDATED_BAD | 6,746 |
| AMBIGUOUS | 8,805 |

Current `VALIDATED_BAD` subtype distribution:

| bad_subtype | Count |
|---|---:|
| action_specific | 2,778 |
| state_context | 3,968 |
| unknown | 0 |

Current BAD reason distribution:

| Reason | Count |
|---|---:|
| no_progress_strong | 4,599 |
| repeated_same_state_failure_tail_no_progress | 4,041 |
| terminal_failure_with_successful_same_state_alternative | 2,778 |
| target_object_dropped | 241 |
| large_object_height_drop | 113 |
| target_object_moved_away_from_goal | 1 |

Current quality counters:

- Suspicious labels: `0`
- Same-state comparison missing: `0`
- Label evidence missing: `0`
- Live dashboard trace-incomplete counter: `279`

Note on trace counter: the running watchdog was started before the later dashboard-count fix that treats `terminal_done` before H=40 as valid terminal-before-H evidence. Per chunk analyzer logs, suspicious labels remain `0`. Final validation after the 20-hour run must recompute this with the current analyzer.

Current task coverage:

- `libero_spatial_with_mug`: tasks `0-9`, multiple seed cycles completed.
- `libero_object_with_mug`: tasks `0-9`, multiple seed cycles completed.
- `libero_10_with_mug`: tasks `0-9`, completed for earlier cycles.
- `libero_goal_with_mug`: tasks running now.

First Sam training run completed from the early synced dataset:

- Training dataset snapshot: `5,421` eligible samples.
- Snapshot labels: `GOOD_STRONG=4,392`, `VALIDATED_BAD=1,029`, `GOOD_WEAK=639`, `AMBIGUOUS=1,364`.
- Training output: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/training/synced_from_bob_sam_20260518_221649/training_summary.json`

First baseline test-unseen-task metrics:

| Model | AUROC BAD | AUPRC BAD | Brier | ECE |
|---|---:|---:|---:|---:|
| action_only_mlp | 0.445 | 0.396 | 0.332 | 0.330 |
| context_action_mlp | 0.527 | 0.485 | 0.273 | 0.258 |
| history_gru_k8 | 0.521 | 0.469 | 0.290 | 0.317 |
| small_history_transformer_k8 | 0.686 | 0.598 | 0.231 | 0.159 |

Best first model so far: `small_history_transformer_k8`.

Current decision:

`DATASET_READY_FOR_FULL_TRAINING = NO`

Reason: collection is still running and final full validation/splits are not complete yet.

## Executive Summary

Status: launched and running.

The final collection will use the corrected Stage 9 outcome/advantage pipeline:

- LIBERO-PRO only.
- Real SimVLA actions only.
- Same-state SimVLA seed counterfactuals.
- History K=8.
- H=40 saved traces.
- Final labels: `GOOD_STRONG`, `GOOD_WEAK`, `VALIDATED_BAD`, `AMBIGUOUS`.
- Training labels: mainly `GOOD_STRONG` vs `VALIDATED_BAD`.

Final huge collection is not considered complete until the 20-hour watchdogs finish and full validation passes.

`DATASET_READY_FOR_FULL_TRAINING = NO`

## Exact Code Changes

Applied before launch:

- Added `bad_subtype` to final label bundles.
- Allowed subtype values: `action_specific`, `state_context`, `unknown`.
- `VALIDATED_BAD` with unknown subtype is downgraded to `AMBIGUOUS`.
- Added `label_evidence` to every sample label.
- Extended strict analysis to count subtype distribution, detect missing subtype, and write corrected label suggestions.
- Added first-stage training script for:
  - `action_only_mlp`
  - `context_action_mlp`
  - `history_gru_k8`
  - `small_history_transformer_k8`
- Added detached 20-hour watchdog scripts.

Changed/created files:

- `asynchvla_ws/src/data_collection_stage9/collect_outcome_advantage_dataset.py`
- `asynchvla_ws/src/data_collection_stage9/analyze_outcome_pilot.py`
- `asynchvla_ws/src/data_collection_stage9/train_stage9_risk_baselines.py`
- `asynchvla_ws/stage9_libero_pro_risk_data/scripts/launch_20h_collection.sh`
- `asynchvla_ws/stage9_libero_pro_risk_data/scripts/stage9_20h_watchdog.py`

## Compile Gate

Bob: `py_compile` passed.

Sam: `py_compile` passed after syncing Stage 9 code from Bob.

## Smoke Test Results

Bob structural smoke:

- Path: `asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/final_pipeline_smoke_bob`
- Samples: 8
- Labels: `AMBIGUOUS=7`, `GOOD_WEAK=1`
- H=40 trace completeness: PASS
- Same-state comparison: PASS
- Label evidence present: PASS
- Suspicious labels: 0

Bob subtype smoke:

- Path: `asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/final_pipeline_smoke_bob_subtype`
- Samples: 16
- Labels: `VALIDATED_BAD=15`, `AMBIGUOUS=1`
- `bad_subtype`: `state_context=15`
- H=40 trace or terminal-before-H: PASS
- Same-state comparison: PASS
- Label evidence present: PASS
- No EEF-away BAD: PASS
- No final BAD unknown reason: PASS
- Suspicious labels: 0

Sam rollout smoke:

- Path: `asynchvla_ws/stage9_libero_pro_risk_data/data/smoke/final_pipeline_smoke_sam`
- Result: rollout unavailable for LIBERO-PRO.
- Reason: Sam benchmark registry exposes normal LIBERO names (`libero_spatial`, `libero_object`, `libero_goal`, `libero_90`, `libero_10`, `libero_100`) but not LIBERO-PRO `*_with_mug` suites.
- Decision: do not collect normal LIBERO on Sam. Sam will run sync/training support from Bob data.

## Bob/Sam Usage

Planned:

- Bob: main LIBERO-PRO collection.
- Sam: LIBERO-PRO rollout unavailable, so Sam is configured for Bob JSONL sync and first training after at least 5k eligible samples.

Launched:

- Bob detached watchdog: `pid=3106359`
- Bob log: `asynchvla_ws/stage9_libero_pro_risk_data/logs/stage9_20h_watchdog_bob_20260518_193710.log`
- Bob dataset root: `asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710`
- Sam detached sync/training watchdog: `pid=595208`
- Sam sync root: `asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/synced_from_bob`
- Sam sync/training log: `asynchvla_ws/stage9_libero_pro_risk_data/logs/stage9_20h_watchdog_sam_20260518_193600.log`

Note: an earlier Bob watchdog `bob_20260518_193456` was stopped because the launcher inherited the wrong `LIBERO_CONFIG_PATH` from activation and produced zero-sample chunks. The launcher now forces `LIBERO_CONFIG_PATH=$REDA_WS/asynchvla_ws/temp_config`.

## 20-hour Collection Stats

Running.

First validated chunk:

- Chunk: `bob_c000_libero_spatial_with_mug_t0_seeds0-7`
- Samples: 256
- States: 32
- Labels: `GOOD_STRONG=101`, `VALIDATED_BAD=83`, `AMBIGUOUS=72`
- Raw local labels: `BAD=106`, `AMBIGUOUS=81`, `GOOD_STRONG=52`, `GOOD_WEAK=17`
- Raw BAD downgraded: 33
- Corrected label suggestions: written.

## Label Distribution

Initial chunk:

- `GOOD_STRONG`: 101
- `VALIDATED_BAD`: 83
- `AMBIGUOUS`: 72
- `GOOD_WEAK`: 0

## VALIDATED_BAD Subtype Distribution

Initial chunk:

- `action_specific`: 11
- `state_context`: 72
- `unknown`: 0

## BAD Reasons

Initial chunk:

- `no_progress_strong`: 73
- `repeated_same_state_failure_tail_no_progress`: 72
- `terminal_failure_with_successful_same_state_alternative`: 11

## Quality Checks

Initial chunk checks:

- No final BAD unknown reason: PASS
- No final BAD from EEF-away alone: PASS
- `VALIDATED_BAD` has known subtype: PASS
- Full H=40 trace or terminal-before-H: PASS
- Same-state comparison exists: PASS
- Label evidence exists for every sample: PASS
- `GOOD_STRONG` has terminal success: PASS

## Suspicious Label Audit

Initial chunk suspicious labels: 0.

## Dataset Paths

- Bob active dataset root: `asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710`
- Sam synced JSONL root: `asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/synced_from_bob`
- Live dashboard: `asynchvla_ws/stage9_libero_pro_risk_data/reports/STAGE9_20H_LIVE_DASHBOARD.md`
- First chunk analysis: `asynchvla_ws/stage9_libero_pro_risk_data/validation/bob_c000_libero_spatial_with_mug_t0_seeds0-7_analysis.json`
- First chunk corrected suggestions: `asynchvla_ws/stage9_libero_pro_risk_data/validation/bob_c000_libero_spatial_with_mug_t0_seeds0-7_corrected_label_suggestions.jsonl`

## Split Paths

Pending.

## First Training Results

Pending. Training starts only after at least 5k eligible `GOOD_STRONG`/`VALIDATED_BAD` samples exist.

## Best First Model

Pending.

## Dataset Ready For Serious Model Training

`DATASET_READY_FOR_FULL_TRAINING = NO`

Current blocker: 20-hour collection and final validation are not complete yet.

## Errors / Crashes / Skipped Tasks

- Stopped `bob_20260518_193456`: zero-sample chunks caused by inherited normal LIBERO config path.
- Sam LIBERO-PRO rollout unavailable: benchmark registry lacks `*_with_mug` suites; Sam is running sync/training support instead.
## Chunk Complete

Completed `bob_c003_libero_goal_with_mug_t4_seeds24-31` at `2026-05-19 09:21:44`.

Chunk path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710/chunks/bob_c003_libero_goal_with_mug_t4_seeds24-31`

Log: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/bob_20260518_193710/bob_c003_libero_goal_with_mug_t4_seeds24-31.log`

Analysis log: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/bob_20260518_193710/bob_c003_libero_goal_with_mug_t4_seeds24-31_analysis.log`

## Chunk Complete

Completed `bob_c003_libero_goal_with_mug_t5_seeds24-31` at `2026-05-19 09:28:20`.

Chunk path: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/final_20h/bob_20260518_193710/chunks/bob_c003_libero_goal_with_mug_t5_seeds24-31`

Log: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/bob_20260518_193710/bob_c003_libero_goal_with_mug_t5_seeds24-31.log`

Analysis log: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/logs/bob_20260518_193710/bob_c003_libero_goal_with_mug_t5_seeds24-31_analysis.log`

