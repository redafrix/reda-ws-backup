# Stage 9 Label Distribution Pilot v3

Generated: `2026-05-18T11:27:46`

Dataset: `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3/counterfactual_samples.jsonl`

## Counts

```json
{
  "GOOD_WEAK": 166,
  "AMBIGUOUS": 122
}
```

## By Suite

```json
{
  "libero_object_with_mug": {
    "GOOD_WEAK": 94,
    "AMBIGUOUS": 2
  },
  "libero_spatial_with_mug": {
    "GOOD_WEAK": 72,
    "AMBIGUOUS": 24
  },
  "libero_goal_with_mug": {
    "AMBIGUOUS": 96
  }
}
```

## By Phase

```json
{
  "approach": {
    "GOOD_WEAK": 152,
    "AMBIGUOUS": 120
  },
  "near_grasp": {
    "GOOD_WEAK": 14,
    "AMBIGUOUS": 2
  }
}
```

## Reasons

```json
{
  "('eef_closer_to_target_before_grasp',)": 144,
  "('no_clear_task_relevant_progress_or_bad_event',)": 26,
  "('weak_target_alignment_improved',)": 22,
  "('target_object_unknown_or_position_missing',)": 96
}
```

## Numeric Evidence Summary

```json
{
  "target_motion": {
    "min": 0.0,
    "mean": 0.000304670071228287,
    "max": 0.006663863023274103
  },
  "target_height_delta": {
    "min": -8.299720145029527e-05,
    "mean": 6.78408488512715e-05,
    "max": 0.0015381926717787583
  },
  "target_height_drop": {
    "min": -0.0015381926717787583,
    "mean": -6.78408488512715e-05,
    "max": 8.299720145029527e-05
  },
  "target_to_goal_delta": {
    "min": 0.0,
    "mean": 0.0002409608921091494,
    "max": 0.002673192847461592
  },
  "target_to_eef_delta": {
    "min": -0.1278261412403674,
    "mean": -0.04723862028304954,
    "max": 0.03416396718345879
  },
  "target_to_eef_before": {
    "min": 0.025637936953109664,
    "mean": 0.26482838646320117,
    "max": 0.44003651973728203
  },
  "reward_sum_H": {
    "min": 0.0,
    "mean": 0.0,
    "max": 0.0
  },
  "eef_delta": {
    "min": 0.010320244200976828,
    "mean": 0.08113576294613677,
    "max": 0.12900168372780124
  }
}
```

## Interpretation

The pilot did not collapse to one class, but it also did not produce `GOOD_STRONG` or `BAD`. It produced weak target-approach labels and ambiguous labels only. This means labels are safer than before, but the dataset is not ready for final collection.
