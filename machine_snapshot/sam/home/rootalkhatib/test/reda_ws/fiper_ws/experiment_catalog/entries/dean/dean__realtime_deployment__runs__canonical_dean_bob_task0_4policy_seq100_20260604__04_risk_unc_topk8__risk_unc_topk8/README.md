# Canonical four-policy Task 0 replication

- **Catalog ID:** `dean:realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8`
- **Host:** `dean`
- **Kind:** `realtime_result`
- **Status:** `inactive_with_results`
- **Original path:** `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8`
- **Checkpoint/model meaning:** explicit per-policy checkpoint
- **Trust level:** canonical and fully audited on 2026-06-05
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

Back-to-back 100-episode comparison of original SimVLA, modified ckpt-60000, base risk-aware policy, and top-8 uncertainty risk-aware policy.

## Important Warning

> Interpret Bob and Dean as separate replications, not identical trajectory replays.

## Episode Results

| File | Rows | Success | Failure | Errors | Unique seeds | Mean steps |
|---|---:|---:|---:|---:|---:|---:|
| `realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8/episode_summaries.jsonl` | 100 | 20 | 80 | 0 | 100 | 270.39 |

## Associated Configuration

No configuration was automatically associated with this entry.

## Artifact Summary

- Files: `4`
- Total size: `19.2 MiB`
- Latest modification: `2026-06-05T03:36:25.329838+00:00`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/realtime_deployment/runs/canonical_dean_bob_task0_4policy_seq100_20260604/04_risk_unc_topk8/risk_unc_topk8`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
