# Four-task risk-aware campaign

- **Catalog ID:** `bob:realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0`
- **Host:** `bob`
- **Kind:** `realtime_result`
- **Status:** `inactive_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0`
- **Checkpoint/model meaning:** modified SimVLA uncertainty checkpoint ckpt-60000
- **Trust level:** paired result; checkpoint semantics corrected on 2026-06-05
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Modified SimVLA ckpt-60000 plus the v2_018 base risk detector and ACE candidate selection.

## Important Warning

> This is not a comparison against original SimVLA.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0/episode_summary_wbob_w1_fold00_unseen_alphabet_soup_t0.jsonl` | 552 | 399 | 153 | 0 | 552 | 211.76 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json` | libero_object_with_mug / 0 | not declared | not declared | 5000 |

## Artifact Summary

- Files: `5`
- Total size: `117.3 MiB`
- Latest modification: `2026-06-01T07:47:47.750000+00:00`

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_4worker_20260529/bob_w1_fold00_unseen_alphabet_soup_t0`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
