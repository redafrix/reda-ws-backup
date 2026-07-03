# Early Task 7 first-action comparison

- **Catalog ID:** `bob:realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528`
- **Checkpoint/model meaning:** modified SimVLA uncertainty checkpoint ckpt-60000
- **Trust level:** raw canonical 100-episode summaries exist; checkpoint label corrected on 2026-06-05
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Historical 100-seed first-action receding-horizon comparison. Both policy paths used the modified ckpt-60000 sampler, despite reports using the word vanilla for the baseline.

## Important Warning

> The observed 58% versus 61% result does not compare against original SimVLA.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528/episode_summary_w1.jsonl` | 50 | 30 | 20 | 0 | 50 | 264.38 |
| `realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528/episode_summary_w0.jsonl` | 50 | 31 | 19 | 0 | 50 | 270.72 |
| `realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528/episode_summaries_canonical_100.jsonl` | 100 | 61 | 39 | 0 | 100 | 267.55 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528.json` | libero_10_with_milk / 7 | not declared | not declared | 100 |

## Artifact Summary

- Files: `9`
- Total size: `26.0 MiB`
- Latest modification: `2026-05-29T07:31:07.850000+00:00`

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/riskaware_actionmod_v2_strict_libero10_milk_task7_bob_full_20260528`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
