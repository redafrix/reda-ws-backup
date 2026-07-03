# Clean Offline Original FIPER vs v2_018 Comparison

- Created: 2026-06-19 19:02:13
- Refs dir: `/home/dean/fiper_uncertainty_collection/experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_00_holdout_alphabet_soup_bbq_sauce/datasets/refs`
- Training hygiene:
  - Original FIPER RND trained only on `success_train_seen`.
  - Original FIPER thresholds calibrated only on `success_calib_seen`.
  - v2_018 retrained with the clean temporal campaign code on seen success/failure train rows.
  - OOD rows are evaluation-only for both methods.

## Main Shared Metrics

| Method / Policy | Seen FA | OOD FA | Seen Failure Det | OOD Failure Det | OOD Det@10 | OOD Det@25 | OOD Det@50 | Mean OOD Det Time | OOD Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Original FIPER RND score q95 K3 | 30.9% | 64.5% | 81.0% | 81.0% | 4.8% | 54.8% | 73.8% | 0.275 | 19.0% |
| Original FIPER ACE q95 K3 | 33.1% | 38.9% | 95.2% | 73.8% | 0.0% | 31.0% | 61.9% | 0.341 | 26.2% |
| Original FIPER OR q95 K3 | 50.0% | 73.5% | 95.2% | 90.5% | 4.8% | 61.9% | 85.7% | 0.260 | 9.5% |
| Original FIPER AND q95 K3 | 8.1% | 15.2% | 76.2% | 59.5% | 0.0% | 14.3% | 38.1% | 0.447 | 40.5% |
| Selected v2_018 score q95 K3 | 15.4% | 27.0% | 100.0% | 95.2% | 0.0% | 23.8% | 88.1% | 0.343 | 4.8% |
| Selected v2_018 ACE q95 K3 | 33.1% | 38.9% | 95.2% | 73.8% | 0.0% | 31.0% | 61.9% | 0.341 | 26.2% |
| Selected v2_018 OR q95 K3 | 37.5% | 46.9% | 100.0% | 100.0% | 0.0% | 35.7% | 95.2% | 0.308 | 0.0% |
| Selected v2_018 AND q95 K3 | 7.4% | 8.1% | 85.7% | 59.5% | 0.0% | 7.1% | 38.1% | 0.466 | 40.5% |

## v2_018 Run Details

- Best epoch: `1`
- Feature audit history dim: `21`
- Feature audit static dim: `43`
- Uses reward: `False`
- Uses success: `False`
- Uses object poses: `False`
- Uses task metadata as input: `False`
- Uses OOD rows for train: `False`

## Verdict

Use the `eventual_or_q95_K3` rows when comparing closest to the older FIPER alarm logic.
Use the `eventual_score_q95_K3` rows when comparing learned-risk score-only behavior.
