# Early Task 7 first-action comparison

- **Catalog ID:** `batman:realtime_deployment/runs/comparison_analysis_task7`
- **Host:** `batman`
- **Kind:** `realtime_run`
- **Status:** `inactive_with_results`
- **Original path:** `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/runs/comparison_analysis_task7`
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
| `realtime_deployment/runs/comparison_analysis_task7/bob_riskaware_episode_summary_w0.jsonl` | 50 | 31 | 19 | 0 | 50 | 270.72 |
| `realtime_deployment/runs/comparison_analysis_task7/sam_episode_summaries_canonical_100.jsonl` | 100 | 58 | 42 | 0 | 100 | 270.97 |
| `realtime_deployment/runs/comparison_analysis_task7/bob_episode_summaries_canonical_100.jsonl` | 100 | 61 | 39 | 0 | 100 | 267.55 |
| `realtime_deployment/runs/comparison_analysis_task7/sam_baseline_episode_summaries.jsonl` | 150 | 84 | 66 | 0 | 100 | 271.81 |
| `realtime_deployment/runs/comparison_analysis_task7/bob_riskaware_episode_summary_w1.jsonl` | 50 | 30 | 20 | 0 | 50 | 264.38 |
| `realtime_deployment/runs/comparison_analysis_task7/bob_chunk_riskaware_episode_summaries_100.jsonl` | 48 | 48 | 0 | 0 | 48 | 214.04 |
| `realtime_deployment/runs/comparison_analysis_task7/bob_chunk_baseline_episode_summaries_100.jsonl` | 100 | 98 | 2 | 0 | 100 | 218.14 |

## Associated Configuration

No configuration was automatically associated with this entry.

## Artifact Summary

- Files: `7`
- Total size: `225.1 KiB`
- Latest modification: `2026-05-29T11:49:23.135980+00:00`

## Navigation

Connect to `batman` and inspect `/home/redafrix/tests/internship/fiper_ws/realtime_deployment/runs/comparison_analysis_task7`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
