# Stage 9 Rule Test Progress

Updated: `2026-05-18T16:02:09`

## Current Step

Step 4 complete: rule unit tests executed.

## Completed Tests

10 rule tests plus target parser smoke.

## Passed Tests

10/10.

## Failed Tests

0/10.

## Files Changed

- `asynchvla_ws/src/data_collection_stage9/run_rule_unit_tests.py`
- `asynchvla_ws/src/data_collection_stage9/label_rules.py`

## Reports Written

- `stage9_rule_test_01_success.md` through `stage9_rule_test_10_mixed_signal.md`
- `stage9_rule_unit_test_summary.md`

## Current Blocker

None for rule tests; proceed to harder/later-state pilot.

## Exact Next Command To Continue

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PYTHONPATH="$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.collect_counterfactual_dataset --suites libero_object_with_mug libero_spatial_with_mug libero_goal_with_mug --task-ids 0 1 --states-per-task 6 --simvla-seeds 0 1 2 3 4 5 6 7 --horizon 20 --history-k 8 --parent-roll-steps 40 --out-dir asynchvla_ws/stage9_libero_pro_risk_data/data/pilot/harder_later_state_v3 --save-images
```
