# Stage 9 Rule Test Progress

Updated: `2026-05-18T11:27:46`

## Current Step

Final report written after rule tests and harder/later-state pilot.

## Completed Tests

- Rule audit
- Label design v3
- 10/10 rule unit tests
- Harder/later-state real SimVLA pilot
- Label consistency audit v3
- Visual label debug v3

## Passed Tests

- Target parser smoke: PASS
- Rule unit tests: 10/10 PASS

## Failed Tests

- Pilot readiness gate: FAIL because no `GOOD_STRONG` or `BAD` real SimVLA samples appeared.

## Files Changed

- `task_parser.py`
- `label_rules.py`
- `outcome_metrics.py`
- `collect_counterfactual_dataset.py`
- `run_rule_unit_tests.py`

## Reports Written

See `STAGE9_RULE_TEST_AND_LABELER_FIX_REPORT.md`.

## Current Blocker

Need phase-selective rollout-state sampler and stronger goal parsing before final collection.

## Exact Next Command To Continue

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh
export LIBERO_CONFIG_PATH="/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"
export MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PYTHONPATH="$PWD/asynchvla_ws/src:$PYTHONPATH"
python3 -m data_collection_stage9.run_rule_unit_tests
```
