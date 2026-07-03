# Conservative top-8 intervention pilot

- **Catalog ID:** `dean:realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8`
- **Host:** `dean`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8`
- **Checkpoint/model meaning:** modified SimVLA ckpt-60000
- **Trust level:** experimental; do not use as a final result until completion audit
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Small active pilot testing stricter intervention rules for the top-8 uncertainty risk model.

## Important Warning

> Status and conclusions may change while the run is active.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8/02_topk8_protective/risk_unc_topk8/episode_summaries.jsonl` | 12 | 5 | 7 | 0 | 12 | 255.17 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8/01_modified_simvla/simvla_only/episode_summaries.jsonl` | 12 | 5 | 7 | 0 | 12 | 255.17 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8/smoke_preflight/03_topk8_balanced/risk_unc_topk8/episode_summaries.jsonl` | 1 | 0 | 1 | 0 | 1 | 300.00 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8/03_topk8_balanced/risk_unc_topk8/episode_summaries.jsonl` | 12 | 5 | 7 | 0 | 12 | 255.17 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_dean_task8_01_modified_simvla.json` | libero_object_object / 8 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_dean_task8_02_topk8_protective.json` | libero_object_object / 8 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_dean_task8_03_topk8_balanced.json` | libero_object_object / 8 | not declared | /home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |

## Artifact Summary

- Files: `20`
- Total size: `7.7 MiB`
- Latest modification: `2026-06-05T09:51:41.617723+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_dean_task8`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
