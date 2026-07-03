# Bob Selected-Cap 10ep Comparison Launch - 2026-06-11

## Status

Corrected run is running on Bob in detached tmux session:

`bob_selected_cap_only_10ep_20260611`

Experiment root:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_selected_cap_10ep_comparison_20260611`

## Purpose

Run the same 10-seed OOD goal-object task set as the previous Bob corrected 10ep sweep, but add the selected-cap gate and delay30 selected-cap gate so they can be paired against the existing Bob baselines:

- Original SimVLA
- Modified SimVLA baseline
- Risk TopK8 threshold 0.3
- Risk TopK8 threshold 0.5
- Risk TopK8 threshold q95
- Risk TopK8 selected-cap
- Risk TopK8 selected-cap delay30

## Workload

- Suite: `libero_goal_object_ood`
- Tasks: 18 tasks, task IDs 0-17
- Seeds: 0-9, exactly matching the previous corrected Bob 10ep OOD sweep
- Corrected new jobs: selected-cap and selected-cap delay30 only
- Execution: one job at a time, no parallel launch on Bob

## New Variants

All variants use modified SimVLA `ckpt-60000` plus H10 TopK8 detector `unc_topk8`.

| Variant | Main Threshold | Min Margin | Strong Margin | Selected Risk Cap | Min Timestep |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `risk_topk8_selected_cap` | 0.3 | 0.02 | 0.05 | 0.4 | 0 |
| `risk_topk8_selected_cap_delay30` | 0.3 | 0.02 | 0.05 | 0.4 | 30 |

## Source Controls

Runner copied from Dean selected-cap implementation:

`run_policy_matrix_selected_cap.py`

Launcher behavior was corrected to match Bob's previously validated launch path:

`source /media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh`

The first launch attempt failed before any episode started because it pointed at a nonexistent Python path. That failed supervisor log was moved under the experiment root `logs/` folder before relaunch.

The initial corrected queue also included unnecessary `threshold_05` and `q95` variants. That was stopped after `task0 selected_cap` completed and while `task0 threshold_05` was partially running. The active corrected queue is now `run_all_selected_cap_only_resume.py`, which skips already-complete jobs and runs only:

- `risk_topk8_selected_cap`
- `risk_topk8_selected_cap_delay30`

Partial `threshold_05/q95` outputs in this root are diagnostic only and must not be included in the selected-cap comparison.

## Baseline Source For Pairing

Existing corrected Bob 10ep OOD sweep:

`/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609`

## Trust Status

Pending until completion and paired raw-JSONL analysis. The launch is mechanically organized and intentionally sequential, but no result claim should be made from this run before final audit.
