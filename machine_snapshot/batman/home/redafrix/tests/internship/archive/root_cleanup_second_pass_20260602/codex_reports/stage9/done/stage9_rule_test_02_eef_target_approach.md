# Stage 9 Rule Test 02: eef_target_approach_rule_test

Status: `PASS`

Expected: `GOOD_WEAK`

Actual: `GOOD_WEAK`

Note: EEF-target approach before grasp is weak only, not strong.

Before image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_02_eef_target_approach_rule_test/before.png`

After image: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_02_eef_target_approach_rule_test/after.png`

```json
{
  "test_name": "eef_target_approach_rule_test",
  "expected": "GOOD_WEAK",
  "actual": "GOOD_WEAK",
  "status": "PASS",
  "note": "EEF-target approach before grasp is weak only, not strong.",
  "before_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_02_eef_target_approach_rule_test/before.png",
  "after_image": "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/rule_tests/test_02_eef_target_approach_rule_test/after.png",
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
        "target_to_eef_before": 0.3,
        "target_to_eef_after": 0.24,
        "target_to_eef_delta": -0.06
      }
    }
  },
  "label_output": {
    "label": "GOOD_WEAK",
    "label_confidence": "MEDIUM",
    "bad_event_type": null,
    "label_reasons": [
      "eef_closer_to_target_before_grasp"
    ],
    "numeric_evidence": {
      "reward_sum_H": 0.0,
      "nonzero_reward_count_H": 0,
      "success": false,
      "eef_delta": 0.05,
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
      "target_to_goal_delta": null,
      "target_to_eef_before": 0.3,
      "target_to_eef_after": 0.24,
      "target_to_eef_delta": -0.06,
      "gripper_closed_near_target": null,
      "gripper_opened_near_target": null,
      "non_target_motion_max": null,
      "unstable_state": null,
      "bad_contact_confident": null,
      "phase": "approach"
    },
    "rule_version": "stage9_rules_v6_four_class_evidence",
    "strong_good_evidence": [],
    "weak_good_evidence": [
      "eef_closer_to_target_before_grasp"
    ],
    "bad_evidence": []
  }
}
```
