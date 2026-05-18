# Stage 9 Rule Test 07: no_progress_rule_test

Status: `PASS`

Expected: `BAD`

Actual: `BAD`

Note: No EEF/target/goal/reward progress is BAD.

Before image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_07_no_progress_rule_test/before.png`

After image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_07_no_progress_rule_test/after.png`

```json
{
  "test_name": "no_progress_rule_test",
  "expected": "BAD",
  "actual": "BAD",
  "status": "PASS",
  "note": "No EEF/target/goal/reward progress is BAD.",
  "before_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_07_no_progress_rule_test/before.png",
  "after_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_07_no_progress_rule_test/after.png",
  "outcome": {
    "H_used": 20,
    "reward_sum_H": 0.0,
    "nonzero_reward_count_H": 0,
    "success_before": false,
    "success_after": false,
    "success_within_H": false,
    "done_within_H": false,
    "delta": {
      "eef_delta": 0.0,
      "object_delta_max": 0.0,
      "height_drop_max": 0.0,
      "task_progress": {
        "task_context_available": true,
        "target_base": "alphabet_soup_1",
        "goal_base": "basket_1",
        "relation": "place_or_put",
        "parse_confidence": "MEDIUM",
        "target_pos_available": true,
        "goal_pos_available": true,
        "target_motion": 0.0,
        "target_to_goal_delta": 0.0,
        "target_to_eef_before": 0.3,
        "target_to_eef_delta": 0.0
      }
    }
  },
  "label_output": {
    "label": "BAD",
    "label_confidence": "MEDIUM",
    "bad_event_type": "zero_reward_no_eef_target_or_goal_progress",
    "label_reasons": [
      "zero_reward_no_eef_target_or_goal_progress"
    ],
    "numeric_evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.0,
      "object_delta_max": 0.0,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 0.0,
      "target_height_delta": null,
      "target_height_drop": null,
      "target_to_goal_delta": 0.0,
      "target_to_eef_before": 0.3,
      "target_to_eef_after": null,
      "target_to_eef_delta": 0.0,
      "gripper_closed_near_target": null,
      "gripper_opened_near_target": null,
      "non_target_motion_max": null,
      "unstable_state": null,
      "bad_contact_confident": null,
      "phase": "approach"
    },
    "rule_version": "stage9_rules_v6_four_class_evidence",
    "strong_good_evidence": [],
    "weak_good_evidence": [],
    "bad_evidence": [
      "zero_reward_no_eef_target_or_goal_progress"
    ]
  }
}
```
