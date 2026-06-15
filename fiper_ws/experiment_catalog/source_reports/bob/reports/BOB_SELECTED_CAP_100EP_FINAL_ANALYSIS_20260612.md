# Bob Selected-Cap 100ep Final Analysis - 2026-06-12

## Scope

Experiment root:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611`

Baseline comparison root:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`

All policies below are evaluated on the same `libero_goal_object_ood` suite, all 18 tasks, and the same reset seeds `10..109`.

## Global Results

| Policy | Success | Rate | Mean Steps | Episodes With Mods | Total Mods |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Original SimVLA | 1,668/1,800 | 92.67% | 127.62 | 0 | 0 |
| Modified SimVLA | 1,718/1,800 | 95.44% | 119.89 | 0 | 0 |
| TopK8 threshold 0.3 | 1,713/1,800 | 95.17% | 120.08 | 833 | 2,553 |
| Selected-cap | 1,713/1,800 | 95.17% | 119.72 | 690 | 1,440 |
| Selected-cap delay30 | 1,723/1,800 | 95.72% | 119.20 | 523 | 1,013 |

## Paired Results

Against Modified SimVLA:

| Policy | Rescues | Regressions | Net |
| :--- | ---: | ---: | ---: |
| Original SimVLA | 57 | 107 | -50 |
| TopK8 threshold 0.3 | 24 | 29 | -5 |
| Selected-cap | 20 | 25 | -5 |
| Selected-cap delay30 | 21 | 16 | +5 |

Against TopK8 threshold 0.3:

| Policy | Rescues | Regressions | Net |
| :--- | ---: | ---: | ---: |
| Selected-cap | 14 | 14 | 0 |
| Selected-cap delay30 | 26 | 16 | +10 |

## Interpretation

On Bob, selected-cap alone did not improve over Modified SimVLA. Its global success matched TopK8 threshold 0.3 and remained net negative against Modified SimVLA.

The `delay30` variant was the best Bob result in this family: it achieved 1,723/1,800, or 95.72%, with a paired net gain of +5 over Modified SimVLA and +10 over TopK8 threshold 0.3. It also reduced interventions strongly: 1,013 total modifications versus 2,553 for threshold 0.3.

This is a small but mechanically valid positive result. It should not be treated as universally robust because Dean's delay30 replication was net negative on a different seed block.
