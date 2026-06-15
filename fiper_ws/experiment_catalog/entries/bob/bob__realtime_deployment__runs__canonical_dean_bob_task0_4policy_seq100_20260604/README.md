# canonical_dean_bob_task0_4policy_seq100_20260604

- **Catalog ID:** `bob:realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`
- **Host:** `bob`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`
- **Checkpoint/model meaning:** not verified
- **Trust level:** inventory only; interpretation unverified
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Purpose not yet semantically verified. Use the listed raw artifacts and reports before drawing conclusions.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/01_original_simvla/simvla_only/episode_summaries.jsonl` | 100 | 10 | 90 | 0 | 100 | 284.64 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/02_modified_simvla_ckpt60000/simvla_only/episode_summaries.jsonl` | 100 | 28 | 72 | 0 | 100 | 262.84 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/03_risk_base/risk_base/episode_summaries.jsonl` | 100 | 25 | 75 | 0 | 100 | 265.04 |
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8/episode_summaries.jsonl` | 100 | 26 | 74 | 0 | 100 | 262.65 |

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_bob_modified_simvla_ckpt60000.json` | libero_object_object / 0 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_bob_original_simvla.json` | libero_object_object / 0 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_bob_risk_base.json` | libero_object_object / 0 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |
| `realtime_deployment/configs/canonical_dean_bob_task0_4policy_seq100_20260604_bob_risk_unc_topk8.json` | libero_object_object / 0 | not declared | /media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000 | 100 |

## Artifact Summary

- Files: `22`
- Total size: `60.4 MiB`
- Latest modification: `2026-06-04T22:13:43.250000+00:00`

## Navigation

Connect to `bob` and inspect `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
