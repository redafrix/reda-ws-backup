# dean_three_policy_seen_object_task0_100eps_20260603

- **Catalog ID:** `dean:realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603`
- **Host:** `dean`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603`
- **Checkpoint/model meaning:** not verified
- **Trust level:** inventory only; interpretation unverified
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603/risk_unc_topk8/episode_summaries.jsonl` | 35 | 14 | 21 | 0 | 35 | 249.29 |
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603/simvla_only/episode_summaries.jsonl` | 100 | 34 | 66 | 0 | 100 | 255.82 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/dean_task0_riskbase_shard0_50_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/dean_task0_riskbase_shard50_100_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/dean_task0_topk8_shard70_100_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/dean_three_policy_seen_object_task0_100eps_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/topk8_parallel_after_simvla_20260603/shard_a_35_53.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/topk8_parallel_after_simvla_20260603/shard_b_53_70.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |

## Artifact Summary

- Files: `8`
- Total size: `17.1 MiB`
- Latest modification: `2026-06-03T10:40:30.863291+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
