# dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla

- **Catalog ID:** `dean:realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla`
- **Host:** `dean`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla`
- **Checkpoint/model meaning:** not verified
- **Trust level:** inventory only; interpretation unverified
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_c_70_100/risk_unc_topk8/episode_summaries.jsonl` | 30 | 10 | 20 | 0 | 30 | 251.43 |
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_b_53_70/risk_unc_topk8/episode_summaries.jsonl` | 17 | 7 | 10 | 0 | 17 | 249.94 |
| `realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla/shard_a_35_53/risk_unc_topk8/episode_summaries.jsonl` | 18 | 8 | 10 | 0 | 18 | 259.72 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/dean_task0_topk8_shard70_100_same_machine_20260603.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/topk8_parallel_after_simvla_20260603/shard_a_35_53.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/topk8_parallel_after_simvla_20260603/shard_b_53_70.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |

## Artifact Summary

- Files: `12`
- Total size: `11.7 MiB`
- Latest modification: `2026-06-03T14:21:14.784673+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/dean_three_policy_seen_object_task0_100eps_20260603_topk8_parallel_after_simvla`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
