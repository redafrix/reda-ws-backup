# Bob q95 OOD Goal-Object Final Analysis

Date: 2026-06-10

## Run

- Host: Bob (`pcrobot`)
- Root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_threshold_q95_20260610`
- Suite: `libero_goal_object_ood`
- Tasks: 0-17
- Policy: `modified_h10_risk_topk8`
- Threshold: `q95` / `0.6155413389205933`
- Episodes: 100 per task, 1,800 total risk episodes
- Baseline comparison root: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`
- Baselines: `original_simvla` and `modified_simvla`, seeds 10-109

## Global Result

| Policy | Successes | Success Rate | Mean Steps |
|---|---:|---:|---:|
| Original SimVLA | 1,668 / 1,800 | 92.67% | 127.62 |
| Modified SimVLA | 1,718 / 1,800 | 95.44% | 119.89 |
| Risk TopK8 q95 | 1,710 / 1,800 | 95.00% | 120.78 |

Paired comparison against modified SimVLA:

- Rescues: 10
- Regressions: 18
- Net gain: -8
- Action modifications: 408 total modifications across 290 modified episodes

## Per-Task q95 vs Modified SimVLA

| Task | Modified | q95 Risk | Rescues | Regressions | Net |
|---:|---:|---:|---:|---:|---:|
| 0 | 85/100 | 86/100 | 6 | 5 | +1 |
| 1 | 98/100 | 97/100 | 0 | 1 | -1 |
| 2 | 84/100 | 82/100 | 0 | 2 | -2 |
| 3 | 98/100 | 97/100 | 0 | 1 | -1 |
| 4 | 98/100 | 98/100 | 0 | 0 | 0 |
| 5 | 100/100 | 99/100 | 0 | 1 | -1 |
| 6 | 100/100 | 100/100 | 0 | 0 | 0 |
| 7 | 90/100 | 88/100 | 0 | 2 | -2 |
| 8 | 95/100 | 95/100 | 0 | 0 | 0 |
| 9 | 97/100 | 97/100 | 0 | 0 | 0 |
| 10 | 100/100 | 100/100 | 0 | 0 | 0 |
| 11 | 98/100 | 97/100 | 0 | 1 | -1 |
| 12 | 98/100 | 94/100 | 0 | 4 | -4 |
| 13 | 90/100 | 91/100 | 1 | 0 | +1 |
| 14 | 93/100 | 95/100 | 3 | 1 | +2 |
| 15 | 97/100 | 97/100 | 0 | 0 | 0 |
| 16 | 99/100 | 99/100 | 0 | 0 | 0 |
| 17 | 98/100 | 98/100 | 0 | 0 | 0 |

## Verdict

The q95 sweep is mechanically valid and complete, but it is negative scientifically. It underperforms the modified SimVLA baseline by 8 successes and underperforms the threshold 0.5 risk sweep globally.

This means q95 is too conservative for this OOD online replacement policy: it removes many interventions, but the remaining interventions still include enough regressions to lose globally.
