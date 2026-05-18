# Stage 9 Episode Outcome Alignment Report

Generated: `2026-05-18`

## Inputs

- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/risky_state_mining_medium_v1`
- `asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/phase_balanced_v1_run2`

## Parent Success/Failure Analysis

```json
{
  "bad_distance_to_failure_or_timeout_mean": 3.2153846153846155,
  "bad_parent_phases": {
    "STUCK_OR_NO_PROGRESS": 57,
    "TRANSPORT": 48
  },
  "bad_samples_before_parent_failure_or_timeout": 65,
  "episodes_with_bad": 10,
  "episodes_without_bad": 49,
  "good_strong_parent_phases": {
    "GRASP_OR_LIFT": 15,
    "STUCK_OR_NO_PROGRESS": 136,
    "TRANSPORT": 223
  },
  "num_parent_episodes": 59,
  "num_samples": 968,
  "parent_success_known_episodes": 52,
  "parent_success_rate_with_bad": 0.1,
  "parent_success_rate_with_good_strong": 0.0,
  "parent_success_rate_without_bad": 0.0,
  "parent_success_rate_without_good_strong": 0.03333333333333333
}
```

## Whether BAD Appears Before Failures

- BAD samples before recorded parent failure/timeout: `65`
- BAD parent phases: `{'TRANSPORT': 48, 'STUCK_OR_NO_PROGRESS': 57}`

## Whether GOOD_STRONG Appears More In Successful Episodes

- Parent success rate with GOOD_STRONG episodes: `0.0`
- Parent success rate without GOOD_STRONG episodes: `0.03333333333333333`

## Whether Current BAD Labels Make Sense With Full Episode Outcomes

Contradiction detected: `NO`

The episode fields are useful as an audit signal only. They are not sufficient label proof because a parent rollout can fail for reasons unrelated to a specific same-state candidate action.

## Limitations

- Parent outcome fields are missing or weak for older phase-balanced samples.
- Parent reward windows around selected states are not fully stored; only history reward tails are available.
- Distance to failure/timeout is only approximate because it uses saved parent step index and parent episode length.
- This audit does not replace replay or same-state counterfactual comparison.
