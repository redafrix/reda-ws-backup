# Dean Uncertainty Feature Comparison Final Audit (2026-06-01)

## Objective

Test whether the new SimVLA uncertainty features help the current transformer risk detector.

The comparison is controlled as:

- Same Dean dataset snapshot.
- Same splits.
- Same transformer architecture as the current baseline family: history 16, width 128, 3 layers, 4 heads, dropout 0.1.
- Same training limits and calibration policy.
- Two variants per split:
  - `base`: old inputs only.
  - `uncertainty`: old inputs plus `simvla_uncertainty_49d` and `simvla_uncertainty_delta_49d`.

## Dean Collection Status

Dean data collection was paused before training. No collector or training process remained active after this comparison. GPU returned idle after completion.

## Dataset Snapshot

- Valid episodes indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks:
  - `libero_10_object/task_4`
  - `libero_goal_object/task_9`

Suite support:

| Suite | Total | Success | Failure |
|---|---:|---:|---:|
| libero_10_object | 295 | 41 | 254 |
| libero_90 | 2935 | 2590 | 345 |
| libero_goal_object | 299 | 231 | 68 |
| libero_object_object | 329 | 224 | 105 |
| libero_spatial_object | 333 | 319 | 14 |

## Splits Run

Only three feasible splits were run:

- `random_mixed`: sanity/mixed split.
- `ood_suite_libero90`: hold out `libero_90` as OOD.
- `ood_task_holdout`: task-id holdout.

Important caveat: `seen_failure` test buckets are tiny in the OOD splits (`1` episode), so seen failure detection metrics are not decision-grade. The decision should be based on OOD success FA and OOD failure detection.

## Calibration Fix

The first full run was invalid because conformal mass calibrated to `0.0`, and the evaluation used `mass >= threshold`, causing false all-episode triggering. That run was archived as:

`/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_transformer_comparison_v1_20260601_BAD_ZERO_CONFORMAL`

The clean run used `--min-conformal-mass 0.15`, and all final threshold files report `conformal_mass = 0.15`.

## Results

| Split | Variant | Seen FA | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---|---:|---:|---:|---:|---:|---:|
| random_mixed | base | 0.0% | n/a | n/a | n/a | n/a | 10 |
| random_mixed | uncertainty | 0.0% | n/a | n/a | n/a | n/a | 14 |
| ood_suite_libero90 | base | 5.7% | 26.9% | 74.6% | 41.9% | 67.7% | 2 |
| ood_suite_libero90 | uncertainty | 0.8% | 1.5% | 51.9% | 0.0% | 0.0% | 7 |
| ood_task_holdout | base | 5.0% | 4.6% | 69.4% | 0.8% | 9.7% | 4 |
| ood_task_holdout | uncertainty | 1.1% | 1.2% | 54.8% | 0.0% | 0.0% | 6 |

## Verdict

The uncertainty features do reduce false alarms strongly, but they reduce OOD failure detection too much.

- `ood_suite_libero90`: OOD FA improves from `26.9%` to `1.5%`, but OOD detection drops from `74.6%` to `51.9%`, and Det@50 drops from `67.7%` to `0.0%`.
- `ood_task_holdout`: OOD FA improves from `4.6%` to `1.2%`, but OOD detection drops from `69.4%` to `54.8%`, and Det@50 drops from `9.7%` to `0.0%`.

Decision: do not replace the base detector with the current uncertainty-augmented detector. The uncertainty features are promising for false-alarm suppression, but as raw appended inputs they make the detector too conservative and hurt detection/early warning.

## Artifacts

Remote Dean output:

`/home/dean/fiper_uncertainty_collection/experiments/dean_uncertainty_transformer_comparison_v1_20260601`

Local copied report/csv:

`fiper_ws/reports/dean_uncertainty_transformer_comparison_v1_20260601/`

Main files:

- `DEAN_UNCERTAINTY_TRANSFORMER_COMPARISON_REPORT.md`
- `dean_uncertainty_comparison_results.csv`
- `available_dataset_summary.json`
- `run_config.json`
- per-split/per-variant `model.pt`, `normalization.json`, `thresholds.json`, `metrics.json`, `history.json`

