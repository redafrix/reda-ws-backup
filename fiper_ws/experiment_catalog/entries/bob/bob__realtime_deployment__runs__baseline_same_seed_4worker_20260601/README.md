# Paired no-risk baseline for the four-task campaign

- **Catalog ID:** `bob:realtime_deployment/runs/baseline_same_seed_4worker_20260601`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/baseline_same_seed_4worker_20260601`
- **Checkpoint/model meaning:** modified SimVLA uncertainty checkpoint ckpt-60000
- **Trust level:** paired result; checkpoint semantics corrected on 2026-06-05
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Modified SimVLA ckpt-60000 without ACE selection or risk-based action replacement. Reset seeds match the corresponding risk-aware campaign.

## Important Warning

> Older reports call this vanilla SimVLA; that label is incorrect.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/baseline_same_seed_4worker_20260601/bob_w0_fold00_seen_butter_t2/episode_summary_wbob_w0_fold00_seen_butter_t2.jsonl` | 450 | 172 | 278 | 0 | 450 | 263.34 |
| `realtime_deployment/runs/baseline_same_seed_4worker_20260601/bob_w1_fold00_unseen_alphabet_soup_t0/episode_summary_wbob_w1_fold00_unseen_alphabet_soup_t0.jsonl` | 552 | 395 | 157 | 0 | 552 | 212.14 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/baseline_same_seed_bob_fold00_seen_butter_task2_20260601.json` | libero_object_with_mug / 2 | not declared | not declared | 5000 |
| `realtime_deployment/configs/baseline_same_seed_bob_fold00_unseen_alphabet_soup_task0_20260601.json` | libero_object_with_mug / 0 | not declared | not declared | 5000 |

## Artifact Summary

- Files: `12`
- Total size: `32.5 MiB`
- Latest modification: `2026-06-01T15:43:29.790000+00:00`

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/baseline_same_seed_4worker_20260601`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
