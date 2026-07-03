# Bob Selected-Cap 100ep Comparison Launch - 2026-06-11

## Status

Running on Bob in detached tmux session:

`bob_selected_cap_only_100ep_20260611`

Experiment root:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_100ep_comparison_20260611`

## Purpose

Run the same two selected-cap variants tested in the Bob 10ep comparison, but at 100 episodes per task using the exact same seeds as the existing Bob 100ep OOD baseline campaign. This allows paired comparison against:

- Original SimVLA
- Modified SimVLA
- Risk TopK8 threshold 0.3

Existing baseline source root:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`

## Workload

- Suite: `libero_goal_object_ood`
- Tasks: 18 tasks, task IDs 0-17
- Seeds: 10-109, matching the existing Bob 100ep OOD campaign
- New jobs: 36 sequential jobs = 18 tasks x 2 selected-cap variants
- Expected episodes: 3600
- Execution: one job at a time, no parallel launch on Bob

## Variants

Both variants use modified SimVLA `ckpt-60000` plus H10 TopK8 detector `unc_topk8`.

| Variant | Main Threshold | Min Margin | Strong Margin | Selected Risk Cap | Min Timestep |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `risk_topk8_selected_cap` | 0.3 | 0.02 | 0.05 | 0.4 | 0 |
| `risk_topk8_selected_cap_delay30` | 0.3 | 0.02 | 0.05 | 0.4 | 30 |

## Preflight

- Config count: 36
- Config audit: passed
- Seeds: exactly 10-109 in every config
- Checkpoint path: `/tmp/ood_ckpt60000`
- Detector path: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Runner: selected-cap runner copied from the verified 10ep selected-cap root
- Launcher: Bob validated activation script `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh`

## Trust Status

Pending until completion and paired raw-JSONL analysis.
