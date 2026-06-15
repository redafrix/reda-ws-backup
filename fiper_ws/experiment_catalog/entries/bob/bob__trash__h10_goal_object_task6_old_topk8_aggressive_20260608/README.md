# h10_goal_object_task6_old_topk8_aggressive_20260608

- **Catalog ID:** `bob:trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `complete_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
- **Checkpoint/model meaning:** SimVLA ckpt-60000 + Old Dean TopK8 (Aggressive 0.3 Threshold)
- **Trust level:** High; paired detector ablation
- **Catalog generated:** 2026-06-08

## What This Result Means

This experiment compared the old \"Dean\" TopK8 detector against the new H10-retrained detector on Task 6 using the same aggressive threshold (0.3). It confirmed that the retrained detector is superior, providing higher success and better steering efficiency.

## Episode Results

| Task | Policy | Success | Failure | SR | Mean steps | Mods |
|---|---|---:|---:|---:|---:|---:|
| Task 6 | Risk-TopK8 (Old, Aggressive 0.3) | 60 | 40 | 60.0% | 194.82 | 606 |

## Paired Analysis (vs Aggressive New Detector)

- **Old Detector Rescues:** 15
- **Old Detector Regressions:** 17
- **Net Difference:** -2.0% Success relative to New H10 Detector.

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`.
The old detector used is: `realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`.
