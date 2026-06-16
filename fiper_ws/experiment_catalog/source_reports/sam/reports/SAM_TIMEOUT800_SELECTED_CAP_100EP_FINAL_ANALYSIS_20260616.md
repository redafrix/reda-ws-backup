# Sam Timeout800 Selected-Cap 100ep Final Analysis - 2026-06-16

This report records the completed Sam evaluation with `max_steps=800` on the full generated `libero_goal_object_ood` suite.

## Run Identity

- Host: Sam (`sam`, `rootalkhatib@100.112.19.30`)
- Root: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615`
- Suite: `libero_goal_object_ood`
- Tasks: 18 tasks, IDs 0-17
- Seeds: 10-109 for every task and all policies
- Policies:
  - `original_simvla`
  - `modified_simvla`
  - `risk_topk8_selected_cap`
- Execution horizon: H10
- Timeout / max steps: 800
- Gate:
  - `selection_main_threshold = 0.3`
  - `selection_streak_threshold = 0.3`
  - `selection_min_margin = 0.02`
  - `selection_strong_margin = 0.05`
  - `selection_max_selected_score = 0.4`

## Verification

Raw JSONL audit on Sam passed:

- 54 `episode_summaries.jsonl` files found: 18 tasks x 3 policies.
- 100 rows per task/policy.
- Reset seeds are exactly `10..109` for every task and policy.
- Seed parity passed across all three policies.
- Suite field is `libero_goal_object_ood` for all checked rows.
- Config sample for task 0 and task 17 confirmed `max_steps=800`, selected-cap threshold `0.3`, cap `0.4`, min margin `0.02`, strong margin `0.05`.

## Global Results

| Policy | Success | Rate | Mean steps | Successes after 300 steps | Episodes with mods | Total mods |
|---|---:|---:|---:|---:|---:|---:|
| Original SimVLA | 1,716/1,800 | 95.33% | 153.98 | 40 | 0 | 0 |
| Modified SimVLA | 1,744/1,800 | 96.89% | 138.68 | 27 | 0 | 0 |
| Selected-cap risk-aware | 1,754/1,800 | 97.44% | 133.02 | 19 | 824 | 2,629 |

The selected-cap policy averaged `2629/1800 = 1.46` action modifications per episode.

## Paired Results

| Comparison | Rescues | Regressions | Net | Both success | Both fail |
|---|---:|---:|---:|---:|---:|
| Selected-cap vs Original SimVLA | 72 | 34 | +38 | 1,682 | 12 |
| Selected-cap vs Modified SimVLA | 37 | 27 | +10 | 1,717 | 19 |

## Per-Task Results

| Task | Original | Modified | Selected-cap | Risk vs Original | Risk vs Modified | Risk successes >300 | Avg mods / risk ep |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 93/100 | 94/100 | 98/100 | +5 (7/2) | +4 (6/2) | 5 | 4.01 |
| 1 | 99/100 | 99/100 | 99/100 | +0 (1/1) | +0 (1/1) | 1 | 1.57 |
| 2 | 96/100 | 94/100 | 95/100 | -1 (2/3) | +1 (2/1) | 4 | 1.68 |
| 3 | 99/100 | 98/100 | 98/100 | -1 (1/2) | +0 (0/0) | 1 | 0.25 |
| 4 | 100/100 | 99/100 | 100/100 | +0 (0/0) | +1 (1/0) | 2 | 0.28 |
| 5 | 100/100 | 99/100 | 99/100 | -1 (0/1) | +0 (0/0) | 0 | 0.52 |
| 6 | 100/100 | 100/100 | 100/100 | +0 (0/0) | +0 (0/0) | 0 | 0.33 |
| 7 | 96/100 | 98/100 | 98/100 | +2 (4/2) | +0 (1/1) | 1 | 0.37 |
| 8 | 98/100 | 94/100 | 95/100 | -3 (1/4) | +1 (2/1) | 0 | 0.67 |
| 9 | 99/100 | 99/100 | 98/100 | -1 (1/2) | -1 (0/1) | 0 | 0.71 |
| 10 | 100/100 | 100/100 | 100/100 | +0 (0/0) | +0 (0/0) | 0 | 0.47 |
| 11 | 91/100 | 93/100 | 93/100 | +2 (7/5) | +0 (5/5) | 0 | 4.72 |
| 12 | 96/100 | 94/100 | 97/100 | +1 (4/3) | +3 (5/2) | 0 | 5.05 |
| 13 | 75/100 | 88/100 | 95/100 | +20 (23/3) | +7 (10/3) | 2 | 3.08 |
| 14 | 82/100 | 96/100 | 94/100 | +12 (15/3) | -2 (3/5) | 2 | 1.86 |
| 15 | 95/100 | 100/100 | 99/100 | +4 (4/0) | -1 (0/1) | 0 | 0.13 |
| 16 | 98/100 | 100/100 | 98/100 | +0 (1/1) | -2 (0/2) | 0 | 0.25 |
| 17 | 99/100 | 99/100 | 98/100 | -1 (1/2) | -1 (1/2) | 1 | 0.34 |

## Interpretation

This is the strongest full-suite OOD result on Sam, but it answers a different question from the 300-step experiments because the timeout was increased to 800.

Main points:

- Selected-cap beats Original SimVLA by +38 paired successes and Modified SimVLA by +10 paired successes.
- The largest positive tasks are task 13, task 0, task 12, and task 4 versus the modified baseline.
- Task 14 is the main negative case versus the modified baseline: 3 rescues / 5 regressions, net -2.
- The 800-step timeout changes the difficulty profile: all policies benefit from longer recovery time, and Original SimVLA also improves strongly compared with earlier 300-step baselines.
- The risk policy did not simply win by using many late recoveries: it had 19 successful episodes after 300 steps, fewer than Original SimVLA (40) and Modified SimVLA (27), while also having lower mean steps.

## Correction to CLI Summary

The CLI summary said the risk policy had total 20 `>300` rescues and average modifications 1.49. Direct raw JSONL recomputation gives:

- risk successes after 300 steps: 19;
- total action modifications: 2,629;
- average modifications per risk episode: 1.46.

Use the recomputed JSONL values above as canonical.
