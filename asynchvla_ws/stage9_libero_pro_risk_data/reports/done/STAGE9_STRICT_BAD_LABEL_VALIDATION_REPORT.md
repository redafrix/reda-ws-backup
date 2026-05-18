# Stage 9 Strict BAD Label Validation Report

Generated: `2026-05-18`

## Inputs

- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2`

## Summary

- Total BAD samples audited: `105`
- VALIDATED_BAD: `11`
- DOWNGRADE_TO_AMBIGUOUS: `22`
- INVALID_BAD: `72`
- NEEDS_MANUAL_REVIEW: `0`
- BAD labels can be trusted now: `NO`

## BAD Reasons Before Validation

```json
{
  "eef_moved_away_from_target_during_approach": 72,
  "target_object_moved_away_from_goal": 8,
  "zero_reward_no_eef_target_or_goal_progress": 25
}
```

## BAD Reasons After Strict Validation

```json
{
  "zero_reward_no_eef_target_or_goal_progress": 11
}
```

## Replay Results

```json
{
  "attempt_status": {
    "not_available_saved_action_too_short": 630,
    "ok": 210
  },
  "sample_replay_status": {
    "ok": 105
  }
}
```

## Same-State Comparison Results

```json
{
  "bad_with_better_same_state_seed": 17,
  "bad_with_successful_same_state_seed": 0,
  "bad_without_better_same_state_seed": 88
}
```

## Examples Of Valid BAD

```json
[
  {
    "dataset": "risky_state_mining_medium_v1",
    "failures": [],
    "parent_phase": "STUCK_OR_NO_PROGRESS",
    "reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "replay_status": "replay_confirmed",
    "same_state_has_better_seed": true,
    "sample_id": "libero_spatial_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s99_state_seed0",
    "status": "VALIDATED_BAD"
  },
  {
    "dataset": "risky_state_mining_medium_v1",
    "failures": [],
    "parent_phase": "STUCK_OR_NO_PROGRESS",
    "reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "replay_status": "replay_confirmed",
    "same_state_has_better_seed": true,
    "sample_id": "libero_spatial_with_mug_t5_r0_pSTUCK_OR_NO_PROGRESS_s99_state_seed3",
    "status": "VALIDATED_BAD"
  },
  {
    "dataset": "risky_state_mining_medium_v1",
    "failures": [],
    "parent_phase": "STUCK_OR_NO_PROGRESS",
    "reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "replay_status": "replay_confirmed",
    "same_state_has_better_seed": true,
    "sample_id": "libero_goal_with_mug_t2_r1_pSTUCK_OR_NO_PROGRESS_s96_state_seed1",
    "status": "VALIDATED_BAD"
  },
  {
    "dataset": "risky_state_mining_medium_v1",
    "failures": [],
    "parent_phase": "STUCK_OR_NO_PROGRESS",
    "reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "replay_status": "replay_confirmed",
    "same_state_has_better_seed": true,
    "sample_id": "libero_goal_with_mug_t2_r1_pSTUCK_OR_NO_PROGRESS_s96_state_seed4",
    "status": "VALIDATED_BAD"
  },
  {
    "dataset": "risky_state_mining_medium_v1",
    "failures": [],
    "parent_phase": "STUCK_OR_NO_PROGRESS",
    "reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "replay_status": "replay_confirmed",
    "same_state_has_better_seed": true,
    "sample_id": "libero_goal_with_mug_t2_r1_pSTUCK_OR_NO_PROGRESS_s96_state_seed5",
    "status": "VALIDATED_BAD"
  }
]
```

## Examples Of Invalid Or Suspicious BAD

```json
[
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed0",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed1",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed2",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed3",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed4",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_not_bad"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_not_bad",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed5",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed6",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed7",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_not_bad"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_not_bad",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed0",
    "status": "INVALID_BAD"
  },
  {
    "dataset": "risky_state_mining_v1",
    "failures": [
      "eef_away_parent_phase_not_approach_or_near_grasp",
      "eef_away_no_better_same_state_real_seed",
      "replay_reason_mismatch"
    ],
    "parent_phase": "TRANSPORT",
    "reasons": [
      "eef_moved_away_from_target_during_approach"
    ],
    "replay_status": "replay_reason_mismatch",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed1",
    "status": "INVALID_BAD"
  }
]
```

## Decision

Current BAD labels are not trustworthy unless the strict pass rate is at least 80%, replay confirms BAD, and same-state alternatives show the BAD action is truly worse. This run does not approve final collection unless the counts above satisfy those gates.

Artifacts:
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/strict_bad_labels/strict_bad_validation_results.json`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/strict_bad_labels/strict_bad_validation_results.csv`
- `asynchvla_ws/stage9_libero_pro_risk_data/validation/strict_bad_labels/corrected_label_suggestions.jsonl`
