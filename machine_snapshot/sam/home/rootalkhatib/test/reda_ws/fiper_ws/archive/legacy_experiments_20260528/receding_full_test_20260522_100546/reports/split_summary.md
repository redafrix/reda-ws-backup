# Split Construction & Leakage Audit Report

This report summarizes the datasets splits generated for RND training, conformal threshold calibration, and challenge evaluations.

## Dataset Splits Overview
| Split File | Episodes | Rows | Purpose |
|---|---|---|---|
| `success_train.jsonl` | 21 | 3003 | RND training |
| `success_calib.jsonl` | 7 | 866 | Threshold calibration |
| `success_test.jsonl` | 8 | 1268 | False alarm testing |
| `ood_suite_success_test.jsonl` | 14 | 1729 | Held-out suite false alarm testing |
| `failure_eval_all.jsonl` | 24 | 9600 | Full failure evaluations |
| `failure_eval_early.jsonl` | N/A | 2400 | Early-episode failure evaluation (first 25%) |
| `failure_eval_late.jsonl` | N/A | 2400 | Late-episode failure evaluation (last 25%) |
| `failure_eval_near_end.jsonl` | N/A | 1200 | Near-end failure evaluation (last 50 steps) |

## Leakage Audit Details
- **Episode-level partition check:** `PASSED`
- **No overlap between train, calib, test, OOD, and failure episodes.**