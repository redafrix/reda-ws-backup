# Held-out last-two-task-IDs experiment

- **Catalog ID:** `dean:experiments/dean_ood_last2_taskids_full_v1_20260601`
- **Host:** `dean`
- **Kind:** `offline_experiment`
- **Status:** `artifacts_only_or_unknown`
- **Original path:** `/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601`
- **Checkpoint/model meaning:** offline detector models
- **Trust level:** completed canonical OOD split
- **Catalog generated:** 2026-06-05T11:53:02.370785+00:00

## What This Result Means

OOD split holding out the last two task IDs from each suite while using all other valid episodes for train, validation, and calibration.

## Episode Results

No episode-summary JSONL was discovered in this entry.

## Associated Configuration

| Config | Suite/task | Policy | Checkpoint field | Seeds |
|---|---|---|---|---:|
| `experiments/dean_ood_last2_taskids_full_v1_20260601/run_config.json` | ? | not declared | not declared | 0 |

## Artifact Summary

- Files: `18`
- Total size: `5.2 MiB`
- Latest modification: `2026-06-01T14:37:27.963871+00:00`

### Key Files

- `experiments/dean_ood_last2_taskids_full_v1_20260601/DEAN_OOD_LAST2_TASKIDS_FULL_V1_20260601.md`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/DEAN_UNCERTAINTY_TRANSFORMER_COMPARISON_REPORT.md`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/available_dataset_summary.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/base/metrics.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/base/model.pt`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/base/normalization.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/base/thresholds.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/unc_raw/metrics.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/unc_raw/model.pt`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/unc_raw/normalization.json`
- `experiments/dean_ood_last2_taskids_full_v1_20260601/ood_last2_taskids_full/unc_raw/thresholds.json`

## Navigation

Connect to `dean` and inspect `/home/dean/fiper_uncertainty_collection/experiments/dean_ood_last2_taskids_full_v1_20260601`.
Do not infer a policy comparison from directory names alone; use the checkpoint and meaning fields above.
