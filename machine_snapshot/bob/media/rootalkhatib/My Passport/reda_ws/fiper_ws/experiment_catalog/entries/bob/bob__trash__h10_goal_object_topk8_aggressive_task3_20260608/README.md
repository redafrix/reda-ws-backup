# h10_goal_object_topk8_aggressive_task3_20260608

- **Catalog ID:** `bob:trash/h10_goal_object_topk8_aggressive_task3_20260608`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `complete_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
- **Checkpoint/model meaning:** SimVLA ckpt-60000 + H10 TopK8 (Aggressive 0.3 Threshold)
- **Trust level:** High; paired seed ablation
- **Catalog generated:** 2026-06-08

## What This Result Means

This ablation study tested the effect of lowering the risk threshold from the conservative `q95` (~0.615) to an aggressive **0.3**. It demonstrated significant success rate and efficiency gains on both Task 3 and Task 6 by allowing the detector to intervene more frequently.

## Episode Results

| Task | Policy | Success | Failure | SR | Mean steps | Mods |
|---|---|---:|---:|---:|---:|---:|
| Task 3 | Risk-TopK8 (Aggressive 0.3) | 19 | 81 | 19.0% | 276.69 | 29 |
| Task 6 | Risk-TopK8 (Aggressive 0.3) | 62 | 38 | 62.0% | 190.44 | 443 |

## Paired Outcome Analysis (vs Conservative q95)

- **Task 3:** +2% gain (2 rescues, 0 regressions).
- **Task 6:** +5% gain (17 rescues, 12 regressions).

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`.
See the Obsidian report for detailed plots and interpretation.
