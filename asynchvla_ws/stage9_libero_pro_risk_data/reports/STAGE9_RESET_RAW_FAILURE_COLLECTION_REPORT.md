# Stage 9 Reset + Raw Failure Episode Collection Report

Date: 2026-05-21

## Executive Summary

I stopped the active Stage 9 dense-risk collection, pushed the current `bob` branch checkpoint, cleaned the active Stage 9 data-labeling workspace by moving old experiments into one archive folder, implemented a raw failed-episode recorder, and collected 5 confirmed LIBERO-PRO failure/timeout episodes.

This is not a final action-risk dataset. It is a raw evidence dataset for designing a better continuous reward/scorer from full simulator traces.

## Stopped Runs

Stopped active Bob Stage 9 run:

- `stage9_v2_failure_mining_bob`
- active script: `launch_dense_15h_bob.sh`
- active collector: `collect_dense_failure_timestep_mining_v2.py`

Verified after stopping:

- no `collect_dense_failure_timestep_mining_v2.py` process remained
- no `collect_raw_failure_episodes_v1.py` process remained after the raw run completed
- only unrelated `stage5` tmux session remained

## Git Checkpoint

Before cleanup, I ran:

```bash
git push origin bob
```

Result:

```text
Everything up-to-date
```

The latest code checkpoint was already on `origin/bob` before cleanup. I then added the new raw failure recorder:

```text
asynchvla_ws/src/data_collection_stage9/collect_raw_failure_episodes_v1.py
```

## Workspace Cleanup

Active Stage 9 workspace:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data
```

Old data/reports/logs/training/validation/debug outputs were moved, not deleted, into:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/archives/reset_20260521_1430
```

Archive size:

```text
223G
```

Clean active folders now kept:

```text
archives/
configs/
data/
logs/
reports/
schemas/
scripts/
```

New raw data lives under:

```text
data/raw_failure_episodes/
```

## Raw Failure Recorder

New script:

```text
asynchvla_ws/src/data_collection_stage9/collect_raw_failure_episodes_v1.py
```

Purpose:

- collect full failed/timeout SimVLA parent episodes
- no action-risk labels
- no synthetic actions
- no final training data
- record full simulator evidence for later reward/scorer analysis

Per recorded failed episode it saves:

- `episode_metadata.json`
- `summary.json`
- `steps.jsonl`
- before/after raw observation NPZ for every step
- before/after simulator state NPZ for every step
- before/after agent-view images for every step
- before/after wrist-view images for every step
- executed SimVLA action and normalized action
- reward, done, success, info
- proprio before/after
- object body positions before/after
- contact summaries before/after
- detected phase
- task parser output
- simulator model names/shapes metadata

Failure acceptance rule:

```text
episode_success = false
AND episode reached done-without-success OR timeout at 400 steps
```

Scout failures that reproduced as success during full recording were not counted as confirmed failures.

## Raw Collection Command

Main run:

```bash
python3 -m data_collection_stage9.collect_raw_failure_episodes_v1 \
  --suites libero_spatial_with_mug libero_object_with_mug \
  --task-ids 0 1 2 3 4 5 \
  --max-failure-episodes 5 \
  --max-parent-episodes 80 \
  --rollouts-per-task 20 \
  --parent-max-steps 400 \
  --parent-policy-chunk-steps 10 \
  --history-k 8 \
  --policy-seed-base 2026052100 \
  --env-seed 20260521 \
  --resolution 128
```

Supplement run, because the main run found 4 confirmed failures before hitting the scout cap:

```bash
python3 -m data_collection_stage9.collect_raw_failure_episodes_v1 \
  --suites libero_spatial_with_mug libero_object_with_mug \
  --task-ids 0 5 1 2 3 4 \
  --max-failure-episodes 1 \
  --max-parent-episodes 50 \
  --rollouts-per-task 20 \
  --parent-max-steps 400 \
  --parent-policy-chunk-steps 10 \
  --history-k 8 \
  --policy-seed-base 2026053000 \
  --env-seed 20260522 \
  --resolution 128
```

## Raw Collection Results

Raw data root:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes
```

Size:

```text
19G
```

Main run path:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes/raw_failure_episodes_v1_20260521_1430
```

Supplement path:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes/raw_failure_episodes_v1_20260521_1444_supplement
```

Confirmed failed episodes collected:

```text
5
```

All confirmed failures:

| Episode | Suite | Task | Policy seed | Steps | Outcome | Phase counts |
|---|---|---:|---:|---:|---|---|
| `libero_spatial_with_mug_t0_r1_pseed2026052101` | spatial mug | 0 | `2026052101` | 400 | timeout/failure | `APPROACH:400` |
| `libero_spatial_with_mug_t0_r4_pseed2026052104` | spatial mug | 0 | `2026052104` | 400 | timeout/failure | `APPROACH:343, NEAR_GRASP:57` |
| `libero_spatial_with_mug_t0_r8_pseed2026052108` | spatial mug | 0 | `2026052108` | 400 | timeout/failure | `APPROACH:24, NEAR_GRASP:134, GRASP_OR_LIFT:166, TRANSPORT:76` |
| `libero_spatial_with_mug_t0_r16_pseed2026052116` | spatial mug | 0 | `2026052116` | 400 | timeout/failure | `APPROACH:400` |
| `libero_spatial_with_mug_t0_r1_pseed2026053001` | spatial mug | 0 | `2026053001` | 400 | timeout/failure | `APPROACH:400` |

Task language for all 5:

```text
pick up the black bowl between the plate and the ramekin and place it on the plate
```

Parsed target/goal:

```text
target = akita_black_bowl_1
goal = plate_1
parse_confidence = HIGH
```

## Reproducibility Notes

The main run scouted 80 episodes and accepted 4 confirmed failures.

Two scout failures reproduced as success when fully recorded and were not counted:

| Episode | Scout result | Recorded result | Recorded steps |
|---|---|---|---:|
| `libero_spatial_with_mug_t0_r6_pseed2026052106` | failure | success | 262 |
| `libero_spatial_with_mug_t1_r9_pseed2026052129` | failure | success | 112 |

These are kept in the raw folder as diagnostic cases, but they are not counted as confirmed failures.

## Current Status

Disk:

```text
1.9T total, 577G used, 1.3T available, 31% used
```

Dataset status:

```text
RAW_FAILURE_ANALYSIS_DATA_READY = YES
ACTION_RISK_TRAINING_DATA_READY = NO
```

Reason:

This reset produced raw failed-episode evidence for reward/scorer design. It does not produce final good/bad action labels.

## Next Discussion Point

Use the 5 confirmed failed episodes to design a continuous action-quality reward based on simulator facts:

- object-goal distance
- target object motion
- object height/lift/drop
- gripper-target relation
- EEF-target relation
- contact summaries
- reward/success signals
- phase-specific expectations
- comparison against successful/expert trajectories

The next step should be analysis, not another label collection run.
