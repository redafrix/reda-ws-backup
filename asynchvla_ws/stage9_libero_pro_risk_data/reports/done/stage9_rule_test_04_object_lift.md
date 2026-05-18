# Stage 9 Rule Test 04: object_lift_rule_test

Status: `PASS`

Expected: `GOOD_STRONG`

Actual: `GOOD_STRONG`

Note: Target lift is strong local progress.

Before image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_04_object_lift_rule_test/before.png`

After image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_04_object_lift_rule_test/after.png`

```json
{
  "test_name": "object_lift_rule_test",
  "expected": "GOOD_STRONG",
  "actual": "GOOD_STRONG",
  "status": "PASS",
  "note": "Target lift is strong local progress.",
  "before_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_04_object_lift_rule_test/before.png",
  "after_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_04_object_lift_rule_test/after.png",
  "outcome": {
    "H_used": 20,
    "reward_sum_H": 0.0,
    "nonzero_reward_count_H": 0,
    "success_before": false,
    "success_after": false,
    "success_within_H": false,
    "done_within_H": false,
    "delta": {
      "eef_delta": 0.05,
      "object_delta_max": 0.04,
      "height_drop_max": 0.0,
      "task_progress": {
        "task_context_available": true,
        "target_base": "alphabet_soup_1",
        "goal_base": "basket_1",
        "relation": "place_or_put",
        "parse_confidence": "MEDIUM",
        "target_pos_available": true,
        "goal_pos_available": true,
        "target_motion": 0.04,
        "target_height_delta": 0.05,
        "target_height_drop": -0.05,
        "target_to_eef_before": 0.05,
        "target_to_eef_delta": -0.01
      }
    }
  },
  "label_output": {
    "label": "GOOD_STRONG",
    "label_confidence": "HIGH",
    "bad_event_type": null,
    "label_reasons": [
      "target_object_lifted"
    ],
    "numeric_evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05,
      "object_delta_max": 0.04,
      "height_drop_max": 0.0,
      "target_base": "alphabet_soup_1",
      "goal_base": "basket_1",
      "task_relation": "place_or_put",
      "parse_confidence": "MEDIUM",
      "target_pos_available": true,
      "goal_pos_available": true,
      "target_motion": 0.04,
      "target_height_delta": 0.05,
      "target_height_drop": -0.05,
      "target_to_goal_delta": null,
      "target_to_eef_before": 0.05,
      "target_to_eef_after": null,
      "target_to_eef_delta": -0.01,
      "gripper_closed_near_target": null,
      "gripper_opened_near_target": null,
      "non_target_motion_max": null,
      "unstable_state": null,
      "bad_contact_confident": null,
      "phase": "grasp_or_lift"
    },
    "rule_version": "stage9_rules_v7_corrected_strong_bad_only",
    "strong_good_evidence": [
      "target_object_lifted"
    ],
    "weak_good_evidence": [
      "small_target_motion_not_strong",
      "weak_target_alignment_improved"
    ],
    "weak_negative_evidence": [
      "zero_reward_only_weak"
    ],
    "bad_evidence": []
  }
}
```
