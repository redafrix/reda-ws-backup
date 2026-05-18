# Stage 9 Rule Unit Test Summary

Generated: `2026-05-18T16:02:09`

Target parser pass: `True`

Rule version: `stage9_rules_v7_corrected_strong_bad_only`

Passed: `10/10`

| Rule | Status | Expected | Actual | Strong Evidence Allowed? |
|---|---:|---|---|---|
| success_rule_test | PASS | GOOD_STRONG | GOOD_STRONG | yes |
| eef_target_approach_rule_test | PASS | GOOD_WEAK | GOOD_WEAK | weak/no |
| wrong_object_rule_test | PASS | AMBIGUOUS | AMBIGUOUS | weak/no |
| object_lift_rule_test | PASS | GOOD_STRONG | GOOD_STRONG | yes |
| object_drop_rule_test | PASS | BAD | BAD | yes |
| object_goal_distance_rule_test | PASS | GOOD_STRONG | GOOD_STRONG | yes |
| no_progress_rule_test | PASS | BAD | BAD | yes |
| contact_rule_test | PASS | AMBIGUOUS | AMBIGUOUS | weak/no |
| gripper_relation_rule_test | PASS | GOOD_WEAK | GOOD_WEAK | weak/no |
| mixed_signal_rule_test | PASS | BAD | BAD | yes |

Gate decision: `PASS`

```json
{
  "generated": "2026-05-18T16:02:09",
  "rule_version": "stage9_rules_v7_corrected_strong_bad_only",
  "target_parser_pass": true,
  "target_parser_output": {
    "task_language": "pick the alphabet soup and place it in the basket",
    "relation": "place_or_put",
    "mentioned_bases": [
      "alphabet_soup_1",
      "basket_1"
    ],
    "target_base": "alphabet_soup_1",
    "goal_base": "basket_1",
    "target_body_prefix": "alphabet_soup_1",
    "goal_body_prefix": "basket_1",
    "parse_confidence": "MEDIUM"
  },
  "num_tests": 10,
  "pass_count": 10,
  "fail_count": 0,
  "results": [
    {
      "name": "success_rule_test",
      "expected": "GOOD_STRONG",
      "actual": "GOOD_STRONG",
      "status": "PASS"
    },
    {
      "name": "eef_target_approach_rule_test",
      "expected": "GOOD_WEAK",
      "actual": "GOOD_WEAK",
      "status": "PASS"
    },
    {
      "name": "wrong_object_rule_test",
      "expected": "AMBIGUOUS",
      "actual": "AMBIGUOUS",
      "status": "PASS"
    },
    {
      "name": "object_lift_rule_test",
      "expected": "GOOD_STRONG",
      "actual": "GOOD_STRONG",
      "status": "PASS"
    },
    {
      "name": "object_drop_rule_test",
      "expected": "BAD",
      "actual": "BAD",
      "status": "PASS"
    },
    {
      "name": "object_goal_distance_rule_test",
      "expected": "GOOD_STRONG",
      "actual": "GOOD_STRONG",
      "status": "PASS"
    },
    {
      "name": "no_progress_rule_test",
      "expected": "BAD",
      "actual": "BAD",
      "status": "PASS"
    },
    {
      "name": "contact_rule_test",
      "expected": "AMBIGUOUS",
      "actual": "AMBIGUOUS",
      "status": "PASS"
    },
    {
      "name": "gripper_relation_rule_test",
      "expected": "GOOD_WEAK",
      "actual": "GOOD_WEAK",
      "status": "PASS"
    },
    {
      "name": "mixed_signal_rule_test",
      "expected": "BAD",
      "actual": "BAD",
      "status": "PASS"
    }
  ]
}
```
