# Conservative top-8 intervention pilot

- **Catalog ID:** `bob:realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7`
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
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7/02_topk8_protective/risk_unc_topk8/episode_summaries.jsonl` | 12 | 9 | 3 | 0 | 12 | 190.33 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7/smoke_preflight/02_topk8_protective/risk_unc_topk8/episode_summaries.jsonl` | 1 | 0 | 1 | 0 | 1 | 300.00 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7/01_modified_simvla/simvla_only/episode_summaries.jsonl` | 12 | 9 | 3 | 0 | 12 | 190.33 |
| `realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7/03_topk8_balanced/risk_unc_topk8/episode_summaries.jsonl` | 12 | 9 | 3 | 0 | 12 | 190.33 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_01_modified_simvla.json` | libero_object_object / 7 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_02_topk8_protective.json` | libero_object_object / 7 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |
| `realtime_deployment/configs/conservative_topk8_midrange_pilot_20260605_bob_task7_03_topk8_balanced.json` | libero_object_object / 7 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 50 |

## Artifact Summary

- Files: `20`
- Total size: `5.8 MiB`
- Latest modification: `2026-06-05T09:00:49.560000+00:00`

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/conservative_topk8_midrange_pilot_20260605_bob_task7`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
