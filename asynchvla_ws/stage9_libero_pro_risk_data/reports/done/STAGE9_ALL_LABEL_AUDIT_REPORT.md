# Stage 9 All Label Audit Report

Generated: `2026-05-18`

## Inputs

- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2`

## Label Distribution Before Correction

```json
{
  "AMBIGUOUS": 268,
  "BAD": 105,
  "GOOD_STRONG": 374,
  "GOOD_WEAK": 221
}
```

## Suspicious GOOD_STRONG

```json
[]
```

## Suspicious GOOD_WEAK

```json
[]
```

## Suspicious AMBIGUOUS

```json
[]
```

## Suspicious BAD

```json
[
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed0",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed1",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed2",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed3",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed4",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed5",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed6",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s0_state_seed7",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed0",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed1",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed2",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed3",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed4",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed5",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed6",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s1_state_seed7",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s2_state_seed0",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s2_state_seed1",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s2_state_seed2",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  },
  {
    "dataset": "risky_state_mining_v1",
    "flags": [
      "bad_failed_strict_validation"
    ],
    "original_label": "BAD",
    "same_state_has_better_seed": false,
    "sample_id": "libero_spatial_with_mug_t0_r0_pTRANSPORT_s2_state_seed3",
    "strong_bad": [
      "eef_moved_away_from_target_during_approach"
    ],
    "strong_good": [],
    "suggestion": "AMBIGUOUS"
  }
]
```

## Missed BAD Candidates

Count: `0`

```json
[]
```

## Corrected Label Suggestion Distribution

```json
{
  "AMBIGUOUS": 362,
  "BAD": 11,
  "GOOD_STRONG": 374,
  "GOOD_WEAK": 221
}
```

## Whether Labeler Rules Need Changes

Rules need changes: `YES`

The most important rule change is to stop accepting EEF-away as BAD unless the saved parent phase is truly APPROACH/NEAR_GRASP, the target parse is confident, same-state real SimVLA alternatives are better, and replay reproduces the bad evidence.
