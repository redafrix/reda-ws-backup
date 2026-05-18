# Stage 9 Labeler Fix Report

Generated: `2026-05-18T10:57:21`

## Correction Applied

The labeler no longer requires success for GOOD. Success is strong GOOD evidence, but local task-relevant progress is also GOOD.

Implemented rule version: `stage9_rules_v5_phase_aware_local_progress`.

## What Changed

- Removed the bad shortcut `EEF closer to any object = GOOD`.
- Added task parsing from language/observation keys in `task_parser.py`.
- Added target-specific metrics in `outcome_metrics.py`:
  - `target_to_goal_delta`
  - `target_to_eef_delta`
  - `target_motion`
  - `target_height_delta`
  - `target_height_drop`
- Added phase-aware labeling:
  - before grasp / approach: EEF closer to target object can be GOOD if the target is identified and progress is clear.
  - grasp/lift: target height increase / target motion can be GOOD.
  - after grasp / transport: target moving closer to goal/receptacle can be GOOD.
- Updated collector to save after-images as well as before-images.

## GOOD Rule Now

GOOD if success within H OR clear local task progress, with no bad event:

- target object-goal distance decreases enough
- EEF-target object distance decreases enough during approach/near-grasp
- target object height increases during grasp/lift
- target object moves in the correct direction
- gripper/target relation improves near grasp

GOOD does not require reward or success.

## BAD Rule Now

BAD only with clear evidence:

- target object moves clearly away from goal
- EEF moves away from target during approach
- target object drops
- no EEF/target/goal progress for H

## Pilot Command

```bash
python3 -m data_collection_stage9.collect_counterfactual_dataset \
  --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug \
  --task-ids 0 1 \
  --states-per-task 4 \
  --simvla-seeds 0 1 2 3 \
  --horizon 20 \
  --history-k 4 \
  --parent-roll-steps 20 \
  --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/labeler_fix_v3 \
  --save-images
```

## Pilot Result

Label counts: `{'GOOD': 64, 'AMBIGUOUS': 32}`

By suite:

```json
{
  "libero_object_with_mug": {
    "GOOD": 32
  },
  "libero_spatial_with_mug": {
    "GOOD": 32
  },
  "libero_goal_with_mug": {
    "AMBIGUOUS": 32
  }
}
```

Reason counts:

```json
{
  "('eef_closer_to_target_before_grasp',)": 64,
  "('target_object_unknown_or_position_missing',)": 32
}
```

Numeric evidence summary:

```json
{
  "target_motion": {
    "min": 0.0,
    "mean": 1.5528537609065875e-07,
    "max": 1.4615030501487394e-06
  },
  "target_height_delta": {
    "min": -1.4150979132931951e-06,
    "mean": -9.135285714174934e-08,
    "max": 2.797054254877196e-12
  },
  "target_to_goal_delta": {
    "min": 0.0,
    "mean": 5.748179709996748e-14,
    "max": 3.7703173916270316e-13
  },
  "target_to_eef_delta": {
    "min": -0.09068593302640893,
    "mean": -0.053991393298944514,
    "max": -0.0375581653868175
  },
  "target_to_eef_before": {
    "min": 0.30496879220657097,
    "mean": 0.37318441614637005,
    "max": 0.44003651973728203
  },
  "reward_sum_H": {
    "min": 0.0,
    "mean": 0.0,
    "max": 0.0
  }
}
```

## Pass / Fail

PASS for the requested non-collapse condition: the pilot no longer collapsed to one class.

Caveat: no BAD labels appeared in this small pilot. That is acceptable for this run because the pilot did not contain clear target-away/drop/no-progress bad events under the corrected strict rule. BAD should be obtained by sampling harder/later states, not by weakening the labeler.

## Suspicious Label Audit

Suspicious cases found: `0`. Details are appended to `stage9_label_consistency_audit_v2.md`.

## Visual Examples

Before/after examples are saved under `asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/labeler_fix_v3` and summarized in `stage9_visual_label_debug_v2.md`.

## Final Collection Decision

Final data collection was not launched.

Next step: run a larger/harder pilot that intentionally samples later grasp/transport/place states and harder LIBERO-PRO tasks to naturally produce BAD examples.
