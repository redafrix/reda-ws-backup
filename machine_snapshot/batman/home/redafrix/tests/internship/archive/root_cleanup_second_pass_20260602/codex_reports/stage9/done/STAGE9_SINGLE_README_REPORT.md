# Stage 9 LIBERO-PRO Action-Risk Dataset: Single Handoff Report

Generated: `2026-05-18T11:32:43`

## Executive Summary

Stage 9 built the foundation for a real LIBERO-PRO same-state counterfactual action-risk dataset, but it is **not ready for final data collection yet**.

The important progress is that the labeler is no longer using the wrong shortcut `EEF closer to target = GOOD_STRONG`. The labeler now separates labels into:

- `GOOD_STRONG`: reliable task/object progress.
- `GOOD_WEAK`: weak local signal, e.g. EEF approaches target before grasp.
- `BAD`: clear bad event or true no-progress failure.
- `AMBIGUOUS`: insufficient, mixed, missing, or weak evidence.

The rule unit tests pass, but the real SimVLA pilot still does not produce reliable strong labels. The latest real pilot produced:

```text
166 GOOD_WEAK / 122 AMBIGUOUS / 0 GOOD_STRONG / 0 BAD
```

So the current decision is:

```text
LABELER_READY_FOR_FINAL_COLLECTION = NO
```

The blocker is not the basic rule code anymore. The blocker is that the pilot is still sampling mostly approach-like states. We need a phase-selective state sampler that deliberately captures near-grasp, lift, transport, placement, stuck/no-progress, and failure-prone states from LIBERO-PRO rollouts.

## What Was Built

Stage 9 code lives on Bob under:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/src/data_collection_stage9/
```

Stage 9 data/reports live under:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/
```

Local report copies are here:

```text
/home/redafrix/tests/internship/codex_reports/stage9/
```

Implemented / modified files:

- `task_parser.py`: parses target object and goal/receptacle from task language plus observation keys.
- `label_rules.py`: four-class evidence-based labeler, current version `stage9_rules_v6_four_class_evidence`.
- `outcome_metrics.py`: computes target/object/eef/goal progress metrics.
- `collect_counterfactual_dataset.py`: collects same-state counterfactual samples from real SimVLA seeds and saves before/after images.
- `run_rule_unit_tests.py`: synthetic rule-test harness for every label rule.
- Existing validators/reports were kept and extended.

## Dataset Goal

The intended dataset is:

```text
history + current observation/proprio + real SimVLA candidate action
-> short-horizon action-risk label
```

The dataset must use:

- LIBERO-PRO only.
- Real SimVLA-generated actions only for training data.
- Same simulator state for all candidate actions at a context.
- Multiple real SimVLA random seeds per state.
- Short-horizon outcome evidence after resetting to the same state.

The dataset must not use:

- Synthetic wrong/random/perturbed actions as training data.
- Final episode success as the only target.
- Timestep/progress/episode length as model input.
- `EEF closer to target` as strong GOOD.
- Task/perturbation/env seed as model input.

## Label Semantics

### GOOD_STRONG

Reliable task-relevant progress. Allowed strong evidence:

- Success within horizon H.
- Target object moved closer to the correct goal/receptacle.
- Target object was lifted enough during pick/grasp/lift phase.
- Target object moved in correct direction with goal-distance support.

`GOOD_STRONG` is intended to be usable as a strong positive training label.

### GOOD_WEAK

Weak but useful local signal. Examples:

- EEF moved closer to the parsed target object before grasp.
- Gripper closed near target.
- Small target motion, not enough for strong progress.
- Weak alignment improvement.

`GOOD_WEAK` should be down-weighted or excluded from initial supervised training. It should not be treated as reliable positive label.

### BAD

Clear bad event or clear no-progress failure. Allowed bad evidence:

- Target object dropped.
- Target object moved clearly away from goal.
- EEF moved away from target during approach.
- Gripper opened/lost object with drop evidence.
- Confident bad contact, if a future contact classifier supports it.
- Unstable state.
- Zero reward and no EEF/target/goal progress.

`BAD` is intended to be a strong negative training label.

### AMBIGUOUS

Use when evidence is missing, weak, or mixed:

- Target object cannot be parsed.
- Goal/receptacle cannot be parsed where needed.
- Only random/non-target object changed.
- Only weak EEF motion occurred and it is below threshold.
- Conflicting evidence.
- Signals are insufficient.

`AMBIGUOUS` should be ignored or down-weighted in training.

## Rule Unit Tests

Rule-test runner:

```text
asynchvla_ws/src/data_collection_stage9/run_rule_unit_tests.py
```

Summary report:

```text
stage9_rule_unit_test_summary.md
```

Result:

```text
Target parser smoke: PASS
Rule unit tests: 10/10 PASS
```

Rules tested:

| Test | Expected | Result |
|---|---|---|
| Success within H | GOOD_STRONG | PASS |
| EEF-target approach | GOOD_WEAK | PASS |
| Wrong/non-target object | AMBIGUOUS | PASS |
| Target object lift | GOOD_STRONG | PASS |
| Object drop | BAD | PASS |
| Target-goal distance closer | GOOD_STRONG | PASS |
| No progress | BAD | PASS |
| Contact, unconfident | AMBIGUOUS | PASS |
| Gripper closes near target | GOOD_WEAK | PASS |
| Mixed progress + drop | BAD | PASS |

Important limitation: these are synthetic rule tests. They prove rule logic, not real dataset quality.

## Real Pilot Results

Latest real SimVLA pilot:

```text
asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3
```

Pilot command:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PYTHONPATH="$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.collect_counterfactual_dataset   --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug   --task-ids 0 1   --states-per-task 6   --simvla-seeds 0 1 2 3 4 5 6 7   --horizon 20   --history-k 8   --parent-roll-steps 40   --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3   --save-images
```

Pilot size:

```text
288 real SimVLA candidate action evaluations
```

Distribution:

```text
166 GOOD_WEAK
122 AMBIGUOUS
0 GOOD_STRONG
0 BAD
```

Interpretation:

- The labeler no longer produces fake `GOOD_STRONG` from EEF approach.
- The pilot still does not provide reliable positive/negative labels for training.
- SimVLA actions in this pilot mostly create weak approach behavior, not object/goal progress or clear failures.
- BAD is absent because no target drop, target-away, stuck/no-progress, or confident bad event occurred in this sampled set.

## Why Previous Results Were Wrong

Earlier versions failed in two opposite ways:

1. Strict object/reward-only labeler collapsed to all BAD because early valid approach has no sparse reward and no object movement.
2. Relaxed EEF-approach labeler collapsed to GOOD because `EEF closer to target/any object` was treated as GOOD.

The corrected version now maps EEF-target approach to `GOOD_WEAK`, not `GOOD_STRONG`.

That is the right semantic correction, but it also exposes the real problem: current state sampling is not producing strong evidence.

## What Signals Are Available

Confirmed available from LIBERO-PRO / robosuite wrappers:

- reward per step
- success check
- EEF pose
- gripper qpos
- object positions / body positions
- target height change
- target-to-EEF distance
- target-to-goal distance when goal parses
- simulator state save/restore
- before and after images
- raw contact list

Weak or unreliable:

- goal/receptacle parsing for all task types
- contact classification, because floor/object contacts exist at rest
- phase detection, currently heuristic

## Current Files You Should Read

Primary handoff:

```text
/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_SINGLE_README_REPORT.md
```

Detailed reports:

```text
/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_RULE_TEST_AND_LABELER_FIX_REPORT.md
/home/redafrix/tests/internship/codex_reports/stage9/STAGE9_RULE_TEST_PROGRESS.md
/home/redafrix/tests/internship/codex_reports/stage9/stage9_rule_unit_test_summary.md
/home/redafrix/tests/internship/codex_reports/stage9/stage9_harder_later_state_pilot_report.md
/home/redafrix/tests/internship/codex_reports/stage9/stage9_label_distribution_pilot_v3.md
/home/redafrix/tests/internship/codex_reports/stage9/stage9_label_consistency_audit_v3.md
/home/redafrix/tests/internship/codex_reports/stage9/stage9_visual_label_debug_v3.md
```

## Visual Debug

Visual examples are saved on Bob under:

```text
/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/visual_debug/harder_later_state_v3
```

The visual report is:

```text
/home/redafrix/tests/internship/codex_reports/stage9/stage9_visual_label_debug_v3.md
```

Available visual examples are `GOOD_WEAK` and `AMBIGUOUS`. No `GOOD_STRONG` or `BAD` examples were available in the latest real pilot.

## Current Blocker

The labeler is safer, but final collection is blocked because the real pilot does not contain strong labels.

The next missing component is a **phase-selective rollout-state sampler**.

It must sample states from:

- early approach
- near grasp
- after grasp / lift
- transport
- near placement
- slow/no-progress states
- failure-prone LIBERO-PRO perturbation states

Current collector only spreads parent rollout steps linearly. It does not detect and select semantically useful phases.

## What To Do Next

Do not launch final collection yet.

Next implementation task:

1. Build a parent rollout logger that records every decision step with task-progress metrics.
2. Classify each state into phase buckets using metrics, not timestep:
   - approach: target-to-EEF distance decreasing, no object motion
   - near grasp: EEF close to target, gripper closing
   - lift: target height increasing
   - transport: target moving with gripper/object relation
   - place: target-goal distance decreasing
   - stuck/no-progress: no EEF/target/goal progress
   - failure-risk: target-away/drop/unstable/contact indicators
3. Sample counterfactual states from each phase bucket.
4. Rerun pilot with real SimVLA seeds.
5. Require natural `GOOD_STRONG`, `BAD`, and `AMBIGUOUS` before final collection.

## Exact Continue Command

Start by rerunning rule tests to verify the labeler still passes:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PYTHONPATH="$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.run_rule_unit_tests
```

Then implement the phase-selective state sampler before another pilot.

## Final Decision

```text
LABELER_READY_FOR_FINAL_COLLECTION = NO
```

Reason:

- Rule unit tests pass.
- Target parser works on simple object/receptacle tasks.
- Real pilot only produced `GOOD_WEAK` and `AMBIGUOUS`.
- There are no real `GOOD_STRONG` or `BAD` examples yet.
- Final collection would mostly produce weak/unusable labels.

The correct next step is not to weaken the labeler. The correct next step is better state selection and stronger task/goal parsing.

## Report Inventory

```text
STAGE9_DATA_COLLECTION_PIPELINE_REPORT.md
STAGE9_RULE_TEST_AND_LABELER_FIX_REPORT.md
STAGE9_RULE_TEST_PROGRESS.md
stage9_contact_check_report.md
stage9_controlled_action_labeler_sanity.md
stage9_final_collection_plan.md
stage9_harder_later_state_pilot_report.md
stage9_implementation_plan.md
stage9_label_consistency_audit.md
stage9_label_consistency_audit_v2.md
stage9_label_consistency_audit_v3.md
stage9_label_distribution_pilot.md
stage9_label_distribution_pilot_v2.md
stage9_label_distribution_pilot_v3.md
stage9_label_learnability_smoke.md
stage9_label_rule_design_v3.md
stage9_labeler_fix_report.md
stage9_object_drop_detection.md
stage9_object_goal_distance_check.md
stage9_observation_signal_audit.md
stage9_pilot_collection_report.md
stage9_reset_determinism_report.md
stage9_rule_audit_report.md
stage9_rule_test_01_success.md
stage9_rule_test_02_eef_target_approach.md
stage9_rule_test_03_wrong_object.md
stage9_rule_test_04_object_lift.md
stage9_rule_test_05_object_drop.md
stage9_rule_test_06_object_goal_distance.md
stage9_rule_test_07_no_progress.md
stage9_rule_test_08_contact.md
stage9_rule_test_09_gripper_relation.md
stage9_rule_test_10_mixed_signal.md
stage9_rule_unit_test_summary.md
stage9_simvla_seed_repeatability.md
stage9_visual_label_debug_report.md
stage9_visual_label_debug_v2.md
stage9_visual_label_debug_v3.md
```
