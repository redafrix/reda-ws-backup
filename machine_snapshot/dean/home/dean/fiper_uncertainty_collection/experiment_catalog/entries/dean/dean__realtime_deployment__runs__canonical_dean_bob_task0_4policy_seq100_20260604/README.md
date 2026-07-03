# canonical_dean_bob_task0_4policy_seq100_20260604

- **Catalog ID:** `dean:realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`
- **Host:** `dean`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`
- **Checkpoint/model meaning:** not verified
- **Trust level:** inventory only; interpretation unverified
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/02_modified_simvla_ckpt60000/simvla_only/episode_summaries.jsonl` | 100 | 22 | 78 | 0 | 100 | 269.00 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/01_original_simvla/simvla_only/episode_summaries.jsonl` | 100 | 14 | 86 | 0 | 100 | 279.74 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8/episode_summaries.jsonl` | 100 | 20 | 80 | 0 | 100 | 270.39 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/03_risk_base/risk_base/episode_summaries.jsonl` | 100 | 25 | 75 | 0 | 100 | 269.96 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_dean_modified_simvla_ckpt60000.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_dean_original_simvla.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_dean_risk_base.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_dean_risk_unc_topk8.json` | libero_object_object / 0 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |

## Artifact Summary

- Files: `22`
- Total size: `61.4 MiB`
- Latest modification: `2026-06-05T03:36:26.108834+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
