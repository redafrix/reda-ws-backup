# Stage 9 Mini-Failure Event Detector Implementation Report

Date: 2026-05-21

## Executive Summary

I implemented a new Stage 9 mini-failure labeling layer that operates on raw simulator traces instead of terminal episode outcome. The detector labels local action timesteps and 10-step VLA chunks with continuous `risk_score` / `quality_score` values in `[0, 1]`, plus event evidence.

This directly targets the failure mode we identified: recoverable local errors can happen inside both successful and failed episodes, so full-episode success/failure is the wrong label source.

Current status:

```text
MINI_FAILURE_DETECTOR_IMPLEMENTED = YES
SMOKE_TEST_PASS = YES
REAL_RAW_TRACE_RUN_COMPLETED = YES
READY_FOR_TRAINING_USE = NO
```

The detector is now useful for review and calibration. It is not yet approved as final training labels until the review pack is manually checked and the thresholds are calibrated on expert/success controls.

## Files Added

On Bob:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/mini_failure_features.py
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/detect_mini_failures.py
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/label_mini_failure_windows.py
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/make_mini_failure_review_pack.py
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/run_mini_failure_detector_smoke.py
```

Local mirror:

```text
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/mini_failure_features.py
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/detect_mini_failures.py
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/label_mini_failure_windows.py
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/make_mini_failure_review_pack.py
/home/redafrix/tests/internship/stage9_v2_tools/data_collection_stage9/run_mini_failure_detector_smoke.py
```

## What The New Detector Does

The new code consumes raw recorded episode folders containing:

```text
episode_metadata.json
summary.json
steps.jsonl
obs_npz/
states/
images/
```

It extracts per-step simulator features:

- target object pose before/after
- goal object pose before/after
- EEF pose before/after
- gripper open/closed state
- target-EFF distance
- target-goal distance
- target height change
- object motions
- nearest object to gripper
- target-held estimate
- non-target-held estimate
- contact summaries
- phase
- reward/success/done as metadata, not label source

Then it detects local mini-failure events:

```text
missed_pick
wrong_object_picked
missed_place
drop_or_slip
transport_entanglement
target_moved_away_from_goal
```

It labels:

- every simulator step
- every 10-step VLA chunk
- pre-failure window before event onset
- failure-core window during the event

## Important Label Policy

The detector does not use episode failure as a direct label.

High risk requires local simulator evidence:

- wrong object actually moves with the gripper
- target was held then drops/slips
- gripper closes/lifts near target but target does not move
- target is released away from goal without placement success/progress
- target moves away from the goal
- contact/tangle evidence with no goal progress

No-progress alone is not made high-risk. It remains uncertain/weak unless tied to a concrete event.

## Continuous Label Schema

Step label output:

```json
{
  "schema_version": "stage9_mini_failure_step_label_v1",
  "episode_id": "...",
  "env_step": 123,
  "parent_chunk_index": 12,
  "risk_score": 0.87,
  "quality_score": 0.13,
  "confidence": 0.91,
  "risk_bin": "RISKY_STRONG",
  "label_source": "mini_failure_event_detector",
  "events": [
    {
      "event_type": "wrong_object_picked",
      "onset_step": 139,
      "role": "failure_core",
      "event_severity": 0.98,
      "event_confidence": 0.90
    }
  ],
  "episode_context": {
    "episode_success": false,
    "episode_failure": true,
    "episode_timeout": true,
    "episode_steps": 400
  }
}
```

Chunk label output:

```json
{
  "schema_version": "stage9_mini_failure_chunk_label_v1",
  "episode_id": "...",
  "chunk_index": 13,
  "start_step": 130,
  "end_step": 139,
  "risk_score": 0.98,
  "risk_score_mean": 0.53,
  "quality_score": 0.02,
  "confidence": 0.90,
  "risk_bin": "RISKY_STRONG",
  "event_types": ["wrong_object_picked"],
  "peak_step": 139
}
```

Risk bins are only for readability:

```text
0.00-0.20 SAFE_STRONG
0.20-0.40 SAFE_WEAK
0.40-0.65 UNCERTAIN
0.65-0.80 RISKY_WEAK
0.80-1.00 RISKY_STRONG
```

The continuous value is the main target.

## Smoke Test

Command run locally and on Bob:

```bash
python3 -m data_collection_stage9.run_mini_failure_detector_smoke
```

Synthetic controlled traces:

```text
missed_pick
wrong_object
drop
missed_place
```

Result:

```text
status = pass
```

The smoke test verifies that each synthetic scenario produces the expected event type.

## First Real Raw-Trace Run

Raw trace root:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes
```

Final detector output:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521
```

Command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src:$PYTHONPATH" \
python3 -m data_collection_stage9.detect_mini_failures \
  --raw-root "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/raw_failure_episodes" \
  --out-dir "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521" \
  --event-window 10 \
  --pre-failure-steps 10 \
  --chunk-size 10
```

Processed episodes:

```text
7
```

Note: the raw folder contains the 5 confirmed timeout/failure recordings plus 2 diagnostic recordings that scouted as failures but recorded as successes. I intentionally kept them in this pass because mini-failures can exist inside successful/recovered trajectories too.

## First Real Results

Total labels:

```text
step labels: 2374
chunk labels: 239
events: 18
```

Chunk risk distribution:

```json
{
  "RISKY_STRONG": 19,
  "RISKY_WEAK": 15,
  "SAFE_STRONG": 1,
  "SAFE_WEAK": 171,
  "UNCERTAIN": 33
}
```

Event distribution:

```json
{
  "wrong_object_picked": 7,
  "missed_place": 6,
  "missed_pick": 3,
  "drop_or_slip": 2
}
```

Risky chunk event counts:

```json
{
  "wrong_object_picked": 14,
  "missed_place": 11,
  "missed_pick": 6,
  "drop_or_slip": 4
}
```

## Per-Episode Events

```text
libero_spatial_with_mug_t0_r1_pseed2026052101
  wrong_object_picked: 2
  onsets: 139, 153

libero_spatial_with_mug_t0_r1_pseed2026053001
  wrong_object_picked: 3
  onsets: 110, 124, 264

libero_spatial_with_mug_t0_r4_pseed2026052104
  wrong_object_picked: 2
  onsets: 187, 201

libero_spatial_with_mug_t0_r6_pseed2026052106
  drop_or_slip: 1
  onset: 204

libero_spatial_with_mug_t0_r8_pseed2026052108
  missed_pick: 3
  missed_place: 6
  onsets: 54, 70, 84, 114, 128, 169, 183, 354, 382

libero_spatial_with_mug_t1_r9_pseed2026052129
  drop_or_slip: 1
  onset: 83

libero_spatial_with_mug_t0_r16_pseed2026052116
  no events
```

## Important Fix During Real Run

The first loose real run produced many suspicious `wrong_object_picked` events in APPROACH-only episodes. Inspecting event evidence showed a false-positive mechanism:

```text
closed gripper near a non-target object
but the non-target object did not actually move
```

I fixed this before accepting the current output.

Current `wrong_object_picked` now requires:

```text
non-target object near/held by gripper
AND non-target object motion over window >= 0.035
AND EEF lift >= 0.025
AND target remains mostly static
```

Current `missed_pick` now requires:

```text
gripper close/lift
AND EEF is near target within 0.085
AND target stays static
AND no non-target-held evidence
```

This reduced the real output from:

```text
65 events, 107 risky chunks
```

to:

```text
18 events, 34 risky chunks
```

That reduction is good. It means the detector is no longer flooding the dataset with weak/hover false positives.

## Review Pack

Review pack:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/review_pack
```

Contents:

```text
manifest.jsonl
summary.json
README.md
top_risk/
event_chunks/
low_risk_controls/
```

Each sheet shows:

- first / peak / last agent view
- first / peak / last wrist view
- risk score
- confidence
- event types
- peak step
- phase counts
- target/goal

Review pack size:

```text
100 items
```

## Outputs

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/mini_failure_events.jsonl
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/mini_failure_step_labels.jsonl
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/mini_failure_chunk_labels.jsonl
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/mini_failure_summary.json
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/STAGE9_MINI_FAILURE_DETECTION_REPORT.md
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/review_pack
```

Output folder size:

```text
123M
```

## Current Interpretation

This is the first result that matches the new labeling philosophy:

- failures are local events
- recovery does not erase prior bad chunks
- full episode success/failure is metadata only
- continuous risk is saved
- uncertain/no-event chunks are not forced high-risk
- wrong-object/drop/missed-place/missed-pick are explicit, auditable events

This is a better direction than the old same-state future-outcome labels.

However, this is not final yet. The detector is now producing plausible candidates, but the review pack needs manual checking. The most important review question is whether the `wrong_object_picked` detections are visually and physically correct in the raw videos/images, especially because some occur in episodes whose phase detector still says APPROACH.

## Remaining Blockers

1. Manual review of `mini_failure_v3_20260521/review_pack` is required.
2. Need run on clean successful/expert trajectories to measure false-positive rate.
3. Need run on more raw failure episodes across more tasks, not only this mug task.
4. Need calibrate thresholds per object/goal geometry.
5. Need decide whether `missed_place` should be split into:
   - bad release
   - lost grasp near place
   - recovery/regrasp attempt
6. Need add optional filtering for confirmed failure-only vs include recovered success episodes.
7. Need integrate this post-processor into the future collector so every raw episode gets event labels automatically.

## Exact Next Step

Manual review:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/data/mini_failure_labels/mini_failure_v3_20260521/review_pack/manifest.jsonl
```

If the review confirms the top detections are correct, run the detector on:

```text
1. more raw failure episodes
2. successful SimVLA episodes
3. expert LIBERO demonstration episodes
```

Then compare:

```text
expert demos: should have near-zero high-risk events
successful SimVLA: may have some recoverable mini-failures
failed SimVLA: should have more unrecovered mini-failures
```

Only after that should these continuous labels be used for training.

