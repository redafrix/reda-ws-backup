# dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8

- **Catalog ID:** `dean:realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8`
- **Host:** `dean`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8`
- **Checkpoint/model meaning:** not verified
- **Trust level:** inventory only; interpretation unverified
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8/shard_a_0_50/risk_base/episode_summaries.jsonl` | 50 | 18 | 32 | 0 | 50 | 251.54 |
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8/shard_b_50_100/risk_base/episode_summaries.jsonl` | 50 | 20 | 30 | 0 | 50 | 250.52 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/dean_task0_riskbase_shard0_50_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/dean_task0_riskbase_shard50_100_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |

## Artifact Summary

- Files: `8`
- Total size: `17.8 MiB`
- Latest modification: `2026-06-03T15:44:07.551499+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_riskbase_parallel_after_topk8`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
