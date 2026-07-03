# Dean Selected-Cap Delay30 100ep Final Analysis - 2026-06-12

## Scope

Experiment root:

`/home/dean/fiper_uncertainty_collection/realtime_deployment/ood_gate_experiments_20260610/selected_cap_t03_c04_delay30_100ep_20260611`

This run evaluates the selected-cap gate with `selection_min_timestep=30`, preventing action replacements before query 3. It uses the same 18-task `libero_goal_object_ood` suite as the earlier Dean selected-cap run, but a different reset seed block.

## Global Results

| Run | Seeds | Modified SimVLA | Risk Policy | Risk Result | Paired Outcome |
| :--- | :---: | ---: | :--- | ---: | :--- |
| Old selected-cap | 300-399 | 1,726/1,800 (95.89%) | selected-cap | 1,741/1,800 (96.72%) | 38 rescues / 23 regressions, net +15 |
| New delay30 | 400-499 | 1,721/1,800 (95.61%) | selected-cap delay30 | 1,718/1,800 (95.44%) | 19 rescues / 22 regressions, net -3 |

## Interpretation

On Dean, delay30 did not improve the selected-cap strategy. It reduced the total number of modifications, but the success-rate effect became slightly negative compared with its own paired Modified SimVLA baseline.

The earlier Dean selected-cap run without delay remains the strongest verified Dean result.
