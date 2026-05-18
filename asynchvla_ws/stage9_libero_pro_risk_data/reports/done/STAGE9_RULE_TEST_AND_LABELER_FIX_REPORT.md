# Stage 9 Rule Test And Labeler Fix Report

Generated: `2026-05-18T11:27:46`

LABELER_READY_FOR_FINAL_COLLECTION = NO

## 1. Is Target Parsing Reliable?

Partially. The unit test for `pick the alphabet soup and place it in the basket` passed and parsed `alphabet_soup_1` as target and `basket_1` as goal. Reliability is medium for object/receptacle tasks whose object names appear directly in observation keys. It is not yet proven for all LIBERO-PRO task types.

## 2. Is Goal Parsing Reliable?

Partially. Goal/receptacle parsing is heuristic from language and observation keys. It works for basket-style tasks in the unit test, but is not fully reliable for drawer/cabinet/microwave/stove/articulation tasks.

## 3. Which Rule Tests Passed?

All 10 synthetic rule unit tests passed:

- success -> `GOOD_STRONG`
- EEF-target approach -> `GOOD_WEAK`
- wrong object -> `AMBIGUOUS`
- object lift -> `GOOD_STRONG`
- object drop -> `BAD`
- object-goal closer -> `GOOD_STRONG`
- no progress -> `BAD`
- unconfident contact -> `AMBIGUOUS`
- gripper closes near target -> `GOOD_WEAK`
- mixed progress + drop -> `BAD`

See `stage9_rule_unit_test_summary.md`.

## 4. Which Rules Are Blocked?

No unit rule is blocked synthetically. Real-data evidence for BAD remains blocked by pilot sampling: the current real SimVLA pilot did not contain clear drop, target-away, unstable, or no-progress failures.

## 5. Which Rules Are Allowed As Strong Evidence?

Allowed strong evidence after unit tests:

- success within H
- target object closer to correct goal/receptacle
- target object lifted
- target object moving in correct direction with goal-distance support
- target object drop
- target object away-from-goal movement
- true no-progress with no EEF/target/goal progress

## 6. Which Rules Are Weak Evidence Only?

- EEF closer to target before grasp
- gripper closes near target
- small target motion below strong threshold
- unconfident contact evidence

These should not be used as strong training labels.

## 7. Did The New Pilot Produce GOOD_STRONG / BAD / AMBIGUOUS?

Pilot label counts:

```json
{
  "GOOD_WEAK": 166,
  "AMBIGUOUS": 122
}
```

The pilot produced `GOOD_WEAK` and `AMBIGUOUS`, but no `GOOD_STRONG` or `BAD`.

## 8. Are Labels Trustworthy Enough For Final Data Collection?

No. The rule logic is now safer, but the pilot does not yet demonstrate real strong positive/negative labels from real SimVLA actions. Final collection would mostly produce weak labels and ambiguous samples.

## 9. Exact Blocker Remaining

The collector must sample genuinely informative phases/states:

- near grasp
- after grasp/lift
- transport
- near placement
- failure-prone perturbation states
- no-progress/stuck states

The current parent-rollout sampling still mostly sees approach behavior. Also, goal parsing needs improvement for non-basket tasks.

## 10. Exact Next Command To Continue If Interrupted

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PYTHONPATH="$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.run_rule_unit_tests
```

Then implement a phase-selective rollout-state sampler before rerunning the pilot.

## Reports Written

- `stage9_rule_audit_report.md`
- `stage9_label_rule_design_v3.md`
- `stage9_rule_test_01_success.md` through `stage9_rule_test_10_mixed_signal.md`
- `stage9_rule_unit_test_summary.md`
- `stage9_harder_later_state_pilot_report.md`
- `stage9_label_distribution_pilot_v3.md`
- `stage9_label_consistency_audit_v3.md`
- `stage9_visual_label_debug_v3.md`
