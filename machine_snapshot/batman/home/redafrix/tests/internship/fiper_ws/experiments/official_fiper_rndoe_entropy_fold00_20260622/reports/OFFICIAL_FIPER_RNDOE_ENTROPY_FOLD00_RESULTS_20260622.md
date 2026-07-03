# Official FIPER RND-OE + Entropy Fold00 Results (2026-06-22)

This report summarizes the closest official-FIPER offline ablation run on the materialized fold00 LIBERO data.

## Paths

- Experiment root: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622`
- Materialized data: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/official_fiper_data`
- Option A results: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/option_a_results`
- Option B results: `/home/dean/fiper_uncertainty_collection/experiments/official_fiper_rndoe_entropy_fold00_20260622/option_b_results`

## Validation Tail

```text
[robosuite WARNING] No private macro file found! (__init__.py:7)
[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)
[robosuite WARNING] To setup, run: python /home/dean/.local/lib/python3.10/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)
Gym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.
Please upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.
See the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1782210027.068808   10452 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
I0000 00:00:1782210027.101813   10452 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1782210028.083243   10452 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.

libero_fold00
obs_embeddings (170943, 960) action_preds (170943, 9, 10, 7)
rollouts 1042 steps 170943 calib 135 test 410 success 979 failed 63 id 789 ood 253

libero_fold00_hygiene
obs_embeddings (170943, 960) action_preds (170943, 9, 10, 7)
rollouts 1042 steps 170943 calib 497 test 410 success 979 failed 63 id 789 ood 253

VALIDATION_PASS
```

## Option A: Official Semantics

Option A uses `libero_fold00`: official-style calibration on `success_calib_seen` and testing on seen/OOD success/failure test splits.

### `option_a_results/complete_results.csv`

Rows: `18600` Columns: `['Method', 'Task', 'TWA', 'TWA_std', 'Accuracy', 'Accuracy_std', 'Det. Time', 'Det. Time_std', 'HID', 'Window', 'Quantile', 'TPR', 'TPR_std', 'TNR', 'TNR_std', 'Threshold', 'ID S', 'ID F', 'OOD S', 'OOD F']`

| Method   | Task          |   TWA |   TWA_std |   Accuracy |   Accuracy_std |   Det. Time |   Det. Time_std |   HID |   Window |   Quantile |   TPR |   TPR_std |   TNR |   TNR_std | Threshold    |   ID S |   ID F |   OOD S |   OOD F |
|:---------|:--------------|------:|----------:|-----------:|---------------:|------------:|----------------:|------:|---------:|-----------:|------:|----------:|------:|----------:|:-------------|-------:|-------:|--------:|--------:|
| entropy  | libero_fold00 | 0.488 |         0 |      0.514 |              0 |       0.053 |               0 |     0 |        1 |       0.9  | 1     |         0 | 0.029 |         0 | tvt_quantile |  0.704 |      1 |   0.713 |   0.946 |
| entropy  | libero_fold00 | 0.617 |         0 |      0.932 |              0 |       0.631 |               0 |     0 |        1 |       0.9  | 1     |         0 | 0.865 |         0 | tvt_cp_band  |  0.54  |      1 |   0.542 |   0.95  |
| entropy  | libero_fold00 | 0.623 |         0 |      0.763 |              0 |       0.49  |               0 |     0 |        1 |       0.9  | 0.571 |         0 | 0.954 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.491 |         0 |      0.519 |              0 |       0.055 |               0 |     0 |        1 |       0.91 | 1     |         0 | 0.037 |         0 | tvt_quantile |  0.702 |      1 |   0.711 |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.932 |              0 |       0.632 |               0 |     0 |        1 |       0.91 | 1     |         0 | 0.865 |         0 | tvt_cp_band  |  0.537 |      1 |   0.539 |   0.95  |
| entropy  | libero_fold00 | 0.624 |         0 |      0.758 |              0 |       0.482 |               0 |     0 |        1 |       0.91 | 0.556 |         0 | 0.96  |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.502 |         0 |      0.53  |              0 |       0.057 |               0 |     0 |        1 |       0.92 | 1     |         0 | 0.061 |         0 | tvt_quantile |  0.7   |      1 |   0.709 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.941 |              0 |       0.653 |               0 |     0 |        1 |       0.92 | 1     |         0 | 0.882 |         0 | tvt_cp_band  |  0.553 |      1 |   0.555 |   0.948 |
| entropy  | libero_fold00 | 0.61  |         0 |      0.735 |              0 |       0.495 |               0 |     0 |        1 |       0.92 | 0.508 |         0 | 0.963 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.504 |         0 |      0.54  |              0 |       0.072 |               0 |     0 |        1 |       0.93 | 1     |         0 | 0.081 |         0 | tvt_quantile |  0.698 |      1 |   0.707 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.942 |              0 |       0.657 |               0 |     0 |        1 |       0.93 | 1     |         0 | 0.885 |         0 | tvt_cp_band  |  0.547 |      1 |   0.549 |   0.948 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.721 |              0 |       0.498 |               0 |     0 |        1 |       0.93 | 0.476 |         0 | 0.965 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.515 |         0 |      0.553 |              0 |       0.076 |               0 |     0 |        1 |       0.94 | 1     |         0 | 0.107 |         0 | tvt_quantile |  0.696 |      1 |   0.705 |   0.946 |
| entropy  | libero_fold00 | 0.615 |         0 |      0.944 |              0 |       0.657 |               0 |     0 |        1 |       0.94 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.547 |      1 |   0.548 |   0.948 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.721 |              0 |       0.498 |               0 |     0 |        1 |       0.94 | 0.476 |         0 | 0.965 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.526 |         0 |      0.569 |              0 |       0.087 |               0 |     0 |        1 |       0.95 | 1     |         0 | 0.138 |         0 | tvt_quantile |  0.694 |      1 |   0.702 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.944 |              0 |       0.659 |               0 |     0 |        1 |       0.95 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.543 |      1 |   0.544 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.687 |              0 |       0.523 |               0 |     0 |        1 |       0.95 | 0.397 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.539 |         0 |      0.588 |              0 |       0.097 |               0 |     0 |        1 |       0.96 | 1     |         0 | 0.176 |         0 | tvt_quantile |  0.691 |      1 |   0.699 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.945 |              0 |       0.662 |               0 |     0 |        1 |       0.96 | 1     |         0 | 0.89  |         0 | tvt_cp_band  |  0.537 |      1 |   0.537 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.687 |              0 |       0.523 |               0 |     0 |        1 |       0.96 | 0.397 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.56  |         0 |      0.617 |              0 |       0.114 |               0 |     0 |        1 |       0.97 | 1     |         0 | 0.233 |         0 | tvt_quantile |  0.688 |      1 |   0.696 |   0.947 |
| entropy  | libero_fold00 | 0.613 |         0 |      0.947 |              0 |       0.667 |               0 |     0 |        1 |       0.97 | 1     |         0 | 0.893 |         0 | tvt_cp_band  |  0.529 |      1 |   0.53  |   0.948 |
| entropy  | libero_fold00 | 0.573 |         0 |      0.679 |              0 |       0.558 |               0 |     0 |        1 |       0.97 | 0.381 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.584 |         0 |      0.656 |              0 |       0.143 |               0 |     0 |        1 |       0.98 | 1     |         0 | 0.311 |         0 | tvt_quantile |  0.684 |      1 |   0.691 |   0.947 |
| entropy  | libero_fold00 | 0.606 |         0 |      0.948 |              0 |       0.684 |               0 |     0 |        1 |       0.98 | 1     |         0 | 0.896 |         0 | tvt_cp_band  |  0.501 |      1 |   0.499 |   0.948 |
| entropy  | libero_fold00 | 0.573 |         0 |      0.679 |              0 |       0.558 |               0 |     0 |        1 |       0.98 | 0.381 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.619 |         0 |      0.716 |              0 |       0.195 |               0 |     0 |        1 |       0.99 | 1     |         0 | 0.432 |         0 | tvt_quantile |  0.678 |      1 |   0.685 |   0.947 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.955 |              0 |       0.706 |               0 |     0 |        1 |       0.99 | 1     |         0 | 0.911 |         0 | tvt_cp_band  |  0.55  |      1 |   0.552 |   0.949 |
| entropy  | libero_fold00 | 0.568 |         0 |      0.669 |              0 |       0.575 |               0 |     0 |        1 |       0.99 | 0.349 |         0 | 0.988 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.5   |         0 |      0.532 |              0 |       0.064 |               0 |     0 |        2 |       0.9  | 1     |         0 | 0.063 |         0 | tvt_quantile |  0.712 |      1 |   0.722 |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.944 |              0 |       0.655 |               0 |     0 |        2 |       0.9  | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.57  |      1 |   0.572 |   0.948 |
| entropy  | libero_fold00 | 0.608 |         0 |      0.766 |              0 |       0.551 |               0 |     0 |        2 |       0.9  | 0.571 |         0 | 0.96  |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.503 |         0 |      0.539 |              0 |       0.071 |               0 |     0 |        2 |       0.91 | 1     |         0 | 0.078 |         0 | tvt_quantile |  0.711 |      1 |   0.72  |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.944 |              0 |       0.655 |               0 |     0 |        2 |       0.91 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.568 |      1 |   0.57  |   0.948 |
| entropy  | libero_fold00 | 0.585 |         0 |      0.725 |              0 |       0.588 |               0 |     0 |        2 |       0.91 | 0.476 |         0 | 0.974 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.515 |         0 |      0.555 |              0 |       0.08  |               0 |     0 |        2 |       0.92 | 1     |         0 | 0.11  |         0 | tvt_quantile |  0.709 |      1 |   0.718 |   0.947 |
| entropy  | libero_fold00 | 0.623 |         0 |      0.935 |              0 |       0.625 |               0 |     0 |        2 |       0.92 | 1     |         0 | 0.87  |         0 | tvt_cp_band  |  0.585 |      1 |   0.588 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.709 |              0 |       0.567 |               0 |     0 |        2 |       0.92 | 0.444 |         0 | 0.974 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.528 |         0 |      0.571 |              0 |       0.085 |               0 |     0 |        2 |       0.93 | 1     |         0 | 0.141 |         0 | tvt_quantile |  0.707 |      1 |   0.716 |   0.947 |

### `option_a_results/summaries/summary_00.csv`

Rows: `3` Columns: `['Method', 'TWA', 'Accuracy', 'Det. Time', 'Window', 'HID', 'Threshold', 'TWA_std', 'Accuracy_std', 'Det. Time_std', 'TPR', 'TPR_std', 'TNR', 'TNR_std']`

| Method             |   TWA |   Accuracy |   Det. Time | Window   |   HID | Threshold    |   TWA_std |   Accuracy_std |   Det. Time_std |   TPR |   TPR_std |   TNR |   TNR_std |
|:-------------------|------:|-----------:|------------:|:---------|------:|:-------------|----------:|---------------:|----------------:|------:|----------:|------:|----------:|
| entropy            | 0.639 |      0.817 |       0.356 | 29       |     0 | tvt_quantile |     0     |          0     |           0     | 1     |     0     | 0.634 |     0     |
| rnd_oe_and_entropy | 0.622 |      0.782 |       0.368 | 48/11    |     0 | tvt_quantile |     0.022 |          0.044 |           0.049 | 0.862 |     0.091 | 0.702 |     0.004 |
| rnd_oe             | 0.552 |      0.611 |       0.13  | 48       |     0 | tvt_quantile |     0.025 |          0.043 |           0.07  | 0.865 |     0.091 | 0.356 |     0.009 |


### Option A Log Tail

```text
/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/hydra/_internal/hydra.py:119: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/1.2/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  ret = run_job(
-------------- Seed: 0 ----------------
-------------- Task: libero_fold00 ----------------
Training rnd_oe
RND Model rnd_oe already exists. Skipping training.
-------------- Seed: 1 ----------------
-------------- Task: libero_fold00 ----------------
Training rnd_oe
RND Model rnd_oe already exists. Skipping training.
-------------- Seed: 2 ----------------
-------------- Task: libero_fold00 ----------------
Training rnd_oe
RND Model rnd_oe already exists. Skipping training.
-------------- Seed: 42 ----------------
-------------- Task: libero_fold00 ----------------
Training rnd_oe
RND Model rnd_oe already exists. Skipping training.
-------------- Seed: 43 ----------------
-------------- Task: libero_fold00 ----------------
Training rnd_oe
RND Model rnd_oe already exists. Skipping training.
               Method    TWA  Accuracy  ...  TPR_std    TNR  TNR_std
0             entropy  0.639     0.817  ...    0.000  0.634    0.000
2  rnd_oe_and_entropy  0.622     0.782  ...    0.091  0.702    0.004
1              rnd_oe  0.552     0.611  ...    0.091  0.356    0.009

[3 rows x 14 columns]
```

## Option B: Hygiene Training

Option B trains RND on `success_train_seen` through `libero_fold00_hygiene`, copies the trained RND checkpoints, then evaluates on `libero_fold00` with calibration/test semantics.

### `option_b_results/complete_results.csv`

Rows: `18600` Columns: `['Method', 'Task', 'TWA', 'TWA_std', 'Accuracy', 'Accuracy_std', 'Det. Time', 'Det. Time_std', 'HID', 'Window', 'Quantile', 'TPR', 'TPR_std', 'TNR', 'TNR_std', 'Threshold', 'ID S', 'ID F', 'OOD S', 'OOD F']`

| Method   | Task          |   TWA |   TWA_std |   Accuracy |   Accuracy_std |   Det. Time |   Det. Time_std |   HID |   Window |   Quantile |   TPR |   TPR_std |   TNR |   TNR_std | Threshold    |   ID S |   ID F |   OOD S |   OOD F |
|:---------|:--------------|------:|----------:|-----------:|---------------:|------------:|----------------:|------:|---------:|-----------:|------:|----------:|------:|----------:|:-------------|-------:|-------:|--------:|--------:|
| entropy  | libero_fold00 | 0.488 |         0 |      0.514 |              0 |       0.053 |               0 |     0 |        1 |       0.9  | 1     |         0 | 0.029 |         0 | tvt_quantile |  0.704 |      1 |   0.713 |   0.946 |
| entropy  | libero_fold00 | 0.617 |         0 |      0.932 |              0 |       0.631 |               0 |     0 |        1 |       0.9  | 1     |         0 | 0.865 |         0 | tvt_cp_band  |  0.54  |      1 |   0.542 |   0.95  |
| entropy  | libero_fold00 | 0.623 |         0 |      0.763 |              0 |       0.49  |               0 |     0 |        1 |       0.9  | 0.571 |         0 | 0.954 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.491 |         0 |      0.519 |              0 |       0.055 |               0 |     0 |        1 |       0.91 | 1     |         0 | 0.037 |         0 | tvt_quantile |  0.702 |      1 |   0.711 |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.932 |              0 |       0.632 |               0 |     0 |        1 |       0.91 | 1     |         0 | 0.865 |         0 | tvt_cp_band  |  0.537 |      1 |   0.539 |   0.95  |
| entropy  | libero_fold00 | 0.624 |         0 |      0.758 |              0 |       0.482 |               0 |     0 |        1 |       0.91 | 0.556 |         0 | 0.96  |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.502 |         0 |      0.53  |              0 |       0.057 |               0 |     0 |        1 |       0.92 | 1     |         0 | 0.061 |         0 | tvt_quantile |  0.7   |      1 |   0.709 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.941 |              0 |       0.653 |               0 |     0 |        1 |       0.92 | 1     |         0 | 0.882 |         0 | tvt_cp_band  |  0.553 |      1 |   0.555 |   0.948 |
| entropy  | libero_fold00 | 0.61  |         0 |      0.735 |              0 |       0.495 |               0 |     0 |        1 |       0.92 | 0.508 |         0 | 0.963 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.504 |         0 |      0.54  |              0 |       0.072 |               0 |     0 |        1 |       0.93 | 1     |         0 | 0.081 |         0 | tvt_quantile |  0.698 |      1 |   0.707 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.942 |              0 |       0.657 |               0 |     0 |        1 |       0.93 | 1     |         0 | 0.885 |         0 | tvt_cp_band  |  0.547 |      1 |   0.549 |   0.948 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.721 |              0 |       0.498 |               0 |     0 |        1 |       0.93 | 0.476 |         0 | 0.965 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.515 |         0 |      0.553 |              0 |       0.076 |               0 |     0 |        1 |       0.94 | 1     |         0 | 0.107 |         0 | tvt_quantile |  0.696 |      1 |   0.705 |   0.946 |
| entropy  | libero_fold00 | 0.615 |         0 |      0.944 |              0 |       0.657 |               0 |     0 |        1 |       0.94 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.547 |      1 |   0.548 |   0.948 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.721 |              0 |       0.498 |               0 |     0 |        1 |       0.94 | 0.476 |         0 | 0.965 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.526 |         0 |      0.569 |              0 |       0.087 |               0 |     0 |        1 |       0.95 | 1     |         0 | 0.138 |         0 | tvt_quantile |  0.694 |      1 |   0.702 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.944 |              0 |       0.659 |               0 |     0 |        1 |       0.95 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.543 |      1 |   0.544 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.687 |              0 |       0.523 |               0 |     0 |        1 |       0.95 | 0.397 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.539 |         0 |      0.588 |              0 |       0.097 |               0 |     0 |        1 |       0.96 | 1     |         0 | 0.176 |         0 | tvt_quantile |  0.691 |      1 |   0.699 |   0.946 |
| entropy  | libero_fold00 | 0.614 |         0 |      0.945 |              0 |       0.662 |               0 |     0 |        1 |       0.96 | 1     |         0 | 0.89  |         0 | tvt_cp_band  |  0.537 |      1 |   0.537 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.687 |              0 |       0.523 |               0 |     0 |        1 |       0.96 | 0.397 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.56  |         0 |      0.617 |              0 |       0.114 |               0 |     0 |        1 |       0.97 | 1     |         0 | 0.233 |         0 | tvt_quantile |  0.688 |      1 |   0.696 |   0.947 |
| entropy  | libero_fold00 | 0.613 |         0 |      0.947 |              0 |       0.667 |               0 |     0 |        1 |       0.97 | 1     |         0 | 0.893 |         0 | tvt_cp_band  |  0.529 |      1 |   0.53  |   0.948 |
| entropy  | libero_fold00 | 0.573 |         0 |      0.679 |              0 |       0.558 |               0 |     0 |        1 |       0.97 | 0.381 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.584 |         0 |      0.656 |              0 |       0.143 |               0 |     0 |        1 |       0.98 | 1     |         0 | 0.311 |         0 | tvt_quantile |  0.684 |      1 |   0.691 |   0.947 |
| entropy  | libero_fold00 | 0.606 |         0 |      0.948 |              0 |       0.684 |               0 |     0 |        1 |       0.98 | 1     |         0 | 0.896 |         0 | tvt_cp_band  |  0.501 |      1 |   0.499 |   0.948 |
| entropy  | libero_fold00 | 0.573 |         0 |      0.679 |              0 |       0.558 |               0 |     0 |        1 |       0.98 | 0.381 |         0 | 0.977 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.619 |         0 |      0.716 |              0 |       0.195 |               0 |     0 |        1 |       0.99 | 1     |         0 | 0.432 |         0 | tvt_quantile |  0.678 |      1 |   0.685 |   0.947 |
| entropy  | libero_fold00 | 0.602 |         0 |      0.955 |              0 |       0.706 |               0 |     0 |        1 |       0.99 | 1     |         0 | 0.911 |         0 | tvt_cp_band  |  0.55  |      1 |   0.552 |   0.949 |
| entropy  | libero_fold00 | 0.568 |         0 |      0.669 |              0 |       0.575 |               0 |     0 |        1 |       0.99 | 0.349 |         0 | 0.988 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.5   |         0 |      0.532 |              0 |       0.064 |               0 |     0 |        2 |       0.9  | 1     |         0 | 0.063 |         0 | tvt_quantile |  0.712 |      1 |   0.722 |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.944 |              0 |       0.655 |               0 |     0 |        2 |       0.9  | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.57  |      1 |   0.572 |   0.948 |
| entropy  | libero_fold00 | 0.608 |         0 |      0.766 |              0 |       0.551 |               0 |     0 |        2 |       0.9  | 0.571 |         0 | 0.96  |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.503 |         0 |      0.539 |              0 |       0.071 |               0 |     0 |        2 |       0.91 | 1     |         0 | 0.078 |         0 | tvt_quantile |  0.711 |      1 |   0.72  |   0.946 |
| entropy  | libero_fold00 | 0.616 |         0 |      0.944 |              0 |       0.655 |               0 |     0 |        2 |       0.91 | 1     |         0 | 0.888 |         0 | tvt_cp_band  |  0.568 |      1 |   0.57  |   0.948 |
| entropy  | libero_fold00 | 0.585 |         0 |      0.725 |              0 |       0.588 |               0 |     0 |        2 |       0.91 | 0.476 |         0 | 0.974 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.515 |         0 |      0.555 |              0 |       0.08  |               0 |     0 |        2 |       0.92 | 1     |         0 | 0.11  |         0 | tvt_quantile |  0.709 |      1 |   0.718 |   0.947 |
| entropy  | libero_fold00 | 0.623 |         0 |      0.935 |              0 |       0.625 |               0 |     0 |        2 |       0.92 | 1     |         0 | 0.87  |         0 | tvt_cp_band  |  0.585 |      1 |   0.588 |   0.948 |
| entropy  | libero_fold00 | 0.583 |         0 |      0.709 |              0 |       0.567 |               0 |     0 |        2 |       0.92 | 0.444 |         0 | 0.974 |         0 | ct_quantile  |  0.712 |      1 |   0.723 |   0.951 |
| entropy  | libero_fold00 | 0.528 |         0 |      0.571 |              0 |       0.085 |               0 |     0 |        2 |       0.93 | 1     |         0 | 0.141 |         0 | tvt_quantile |  0.707 |      1 |   0.716 |   0.947 |

### `option_b_results/summaries/summary_00.csv`

Rows: `3` Columns: `['Method', 'TWA', 'Accuracy', 'Det. Time', 'Window', 'HID', 'Threshold', 'TWA_std', 'Accuracy_std', 'Det. Time_std', 'TPR', 'TPR_std', 'TNR', 'TNR_std']`

| Method             |   TWA |   Accuracy |   Det. Time | Window   |   HID | Threshold    |   TWA_std |   Accuracy_std |   Det. Time_std |   TPR |   TPR_std |   TNR |   TNR_std |
|:-------------------|------:|-----------:|------------:|:---------|------:|:-------------|----------:|---------------:|----------------:|------:|----------:|------:|----------:|
| entropy            | 0.639 |      0.817 |       0.356 | 29       |     0 | tvt_quantile |     0     |          0     |           0     | 1     |     0     | 0.634 |     0     |
| rnd_oe_and_entropy | 0.625 |      0.808 |       0.415 | 48/16    |     0 | tvt_quantile |     0.013 |          0.018 |           0.036 | 0.883 |     0.036 | 0.733 |     0.005 |
| rnd_oe             | 0.553 |      0.625 |       0.159 | 48       |     0 | tvt_quantile |     0.017 |          0.018 |           0.048 | 0.898 |     0.037 | 0.353 |     0.009 |


### Option B Train Log Tail

```text
Epoch 1: Train Loss: 1.2235, Val Loss: 0.4334:   0%|          | 0/250 [00:08<?, ?it/s]
Epoch 1: Train Loss: 1.2235, Val Loss: 0.4334:   0%|          | 1/250 [00:08<35:32,  8.56s/it]
Epoch 2: Train Loss: 0.3084, Val Loss: 0.2424:   0%|          | 1/250 [00:17<35:32,  8.56s/it]
Epoch 2: Train Loss: 0.3084, Val Loss: 0.2424:   1%|          | 2/250 [00:17<35:26,  8.57s/it]
Epoch 3: Train Loss: 0.1986, Val Loss: 0.2034:   1%|          | 2/250 [00:25<35:26,  8.57s/it]
Epoch 3: Train Loss: 0.1986, Val Loss: 0.2034:   1%|          | 3/250 [00:25<35:17,  8.57s/it]
Epoch 4: Train Loss: 0.1671, Val Loss: 0.2719:   1%|          | 3/250 [00:34<35:17,  8.57s/it]
Epoch 4: Train Loss: 0.1671, Val Loss: 0.2719:   2%|▏         | 4/250 [00:34<35:10,  8.58s/it]
Epoch 5: Train Loss: 0.2208, Val Loss: 0.2569:   2%|▏         | 4/250 [00:42<35:10,  8.58s/it]
Epoch 5: Train Loss: 0.2208, Val Loss: 0.2569:   2%|▏         | 5/250 [00:42<35:02,  8.58s/it]
Epoch 6: Train Loss: 0.1626, Val Loss: 0.1413:   2%|▏         | 5/250 [00:51<35:02,  8.58s/it]
Epoch 6: Train Loss: 0.1626, Val Loss: 0.1413:   2%|▏         | 6/250 [00:51<34:55,  8.59s/it]
Epoch 7: Train Loss: 0.1520, Val Loss: 0.2774:   2%|▏         | 6/250 [01:00<34:55,  8.59s/it]
Epoch 7: Train Loss: 0.1520, Val Loss: 0.2774:   3%|▎         | 7/250 [01:00<34:47,  8.59s/it]
Epoch 8: Train Loss: 0.2269, Val Loss: 0.1849:   3%|▎         | 7/250 [01:08<34:47,  8.59s/it]
Epoch 8: Train Loss: 0.2269, Val Loss: 0.1849:   3%|▎         | 8/250 [01:08<34:37,  8.58s/it]
Epoch 9: Train Loss: 0.1578, Val Loss: 0.1016:   3%|▎         | 8/250 [01:17<34:37,  8.58s/it]
Epoch 9: Train Loss: 0.1578, Val Loss: 0.1016:   4%|▎         | 9/250 [01:17<34:28,  8.58s/it]
Epoch 10: Train Loss: 0.1501, Val Loss: 0.2290:   4%|▎         | 9/250 [01:25<34:28,  8.58s/it]
Epoch 10: Train Loss: 0.1501, Val Loss: 0.2290:   4%|▍         | 10/250 [01:25<34:20,  8.59s/it]
Epoch 11: Train Loss: 0.1984, Val Loss: 0.2173:   4%|▍         | 10/250 [01:34<34:20,  8.59s/it]
Epoch 11: Train Loss: 0.1984, Val Loss: 0.2173:   4%|▍         | 11/250 [01:34<34:11,  8.59s/it]
Epoch 12: Train Loss: 0.1923, Val Loss: 0.1832:   4%|▍         | 11/250 [01:42<34:11,  8.59s/it]
Epoch 12: Train Loss: 0.1923, Val Loss: 0.1832:   5%|▍         | 12/250 [01:42<34:02,  8.58s/it]
Epoch 13: Train Loss: 0.1295, Val Loss: 0.0813:   5%|▍         | 12/250 [01:51<34:02,  8.58s/it]
Epoch 13: Train Loss: 0.1295, Val Loss: 0.0813:   5%|▌         | 13/250 [01:51<33:53,  8.58s/it]
Epoch 14: Train Loss: 0.1407, Val Loss: 0.1765:   5%|▌         | 13/250 [02:00<33:53,  8.58s/it]
Epoch 14: Train Loss: 0.1407, Val Loss: 0.1765:   6%|▌         | 14/250 [02:00<33:44,  8.58s/it]
Epoch 15: Train Loss: 0.1349, Val Loss: 0.0766:   6%|▌         | 14/250 [02:08<33:44,  8.58s/it]
Epoch 15: Train Loss: 0.1349, Val Loss: 0.0766:   6%|▌         | 15/250 [02:08<33:36,  8.58s/it]
Epoch 16: Train Loss: 0.1853, Val Loss: 0.1651:   6%|▌         | 15/250 [02:17<33:36,  8.58s/it]
Epoch 16: Train Loss: 0.1853, Val Loss: 0.1651:   6%|▋         | 16/250 [02:17<33:27,  8.58s/it]
Epoch 17: Train Loss: 0.1538, Val Loss: 0.0987:   6%|▋         | 16/250 [02:25<33:27,  8.58s/it]
Epoch 17: Train Loss: 0.1538, Val Loss: 0.0987:   7%|▋         | 17/250 [02:25<33:19,  8.58s/it]
Epoch 18: Train Loss: 0.1260, Val Loss: 0.1911:   7%|▋         | 17/250 [02:34<33:19,  8.58s/it]
Epoch 18: Train Loss: 0.1260, Val Loss: 0.1911:   7%|▋         | 18/250 [02:34<33:08,  8.57s/it]
Epoch 19: Train Loss: 0.1667, Val Loss: 0.1727:   7%|▋         | 18/250 [02:42<33:08,  8.57s/it]
Epoch 19: Train Loss: 0.1667, Val Loss: 0.1727:   8%|▊         | 19/250 [02:42<32:59,  8.57s/it]
Epoch 20: Train Loss: 0.1584, Val Loss: 0.1469:   8%|▊         | 19/250 [02:51<32:59,  8.57s/it]
Epoch 20: Train Loss: 0.1584, Val Loss: 0.1469:   8%|▊         | 20/250 [02:51<32:51,  8.57s/it]
Epoch 21: Train Loss: 0.1451, Val Loss: 0.0729:   8%|▊         | 20/250 [03:00<32:51,  8.57s/it]
Epoch 21: Train Loss: 0.1451, Val Loss: 0.0729:   8%|▊         | 21/250 [03:00<32:43,  8.57s/it]
Epoch 22: Train Loss: 0.0872, Val Loss: 0.1791:   8%|▊         | 21/250 [03:08<32:43,  8.57s/it]
Epoch 22: Train Loss: 0.0872, Val Loss: 0.1791:   9%|▉         | 22/250 [03:08<32:34,  8.57s/it]
Epoch 23: Train Loss: 0.1273, Val Loss: 0.1748:   9%|▉         | 22/250 [03:17<32:34,  8.57s/it]
Epoch 23: Train Loss: 0.1273, Val Loss: 0.1748:   9%|▉         | 23/250 [03:17<32:25,  8.57s/it]
Epoch 24: Train Loss: 0.1516, Val Loss: 0.1705:   9%|▉         | 23/250 [03:25<32:25,  8.57s/it]
Epoch 24: Train Loss: 0.1516, Val Loss: 0.1705:  10%|▉         | 24/250 [03:25<32:16,  8.57s/it]
Epoch 25: Train Loss: 0.0964, Val Loss: 0.1368:  10%|▉         | 24/250 [03:34<32:16,  8.57s/it]
Epoch 25: Train Loss: 0.0964, Val Loss: 0.1368:  10%|█         | 25/250 [03:34<32:08,  8.57s/it]
Epoch 26: Train Loss: 0.1181, Val Loss: 0.0852:  10%|█         | 25/250 [03:43<32:08,  8.57s/it]
Epoch 26: Train Loss: 0.1181, Val Loss: 0.0852:  10%|█         | 26/250 [03:43<32:00,  8.57s/it]
Epoch 27: Train Loss: 0.1317, Val Loss: 0.1513:  10%|█         | 26/250 [03:51<32:00,  8.57s/it]
Epoch 27: Train Loss: 0.1317, Val Loss: 0.1513:  11%|█         | 27/250 [03:51<31:52,  8.58s/it]
Epoch 28: Train Loss: 0.1387, Val Loss: 0.1313:  11%|█         | 27/250 [04:00<31:52,  8.58s/it]Early stopping triggered due to validation loss not improving over the last 7 epochs.

                                                                                                
Saving checkpoint with seed 43
Error executing job with overrides: ["tasks=['libero_fold00_hygiene']", "rnd_models=['rnd_oe']", "methods=['entropy']", 'train_rnd=True']
Traceback (most recent call last):
  File "/home/dean/fiper_uncertainty_collection/external/fiper/scripts/run_fiper.py", line 155, in main
    resultsmanager.create_summary()
  File "/home/dean/fiper_uncertainty_collection/external/fiper/evaluation/results_manager.py", line 275, in create_summary
    summary_df = self._load_dataframe()
  File "/home/dean/fiper_uncertainty_collection/external/fiper/evaluation/results_manager.py", line 94, in _load_dataframe
    df = pd.read_csv(os.path.join(self.results_dir, filename))
  File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/pandas/io/parsers/readers.py", line 1898, in _make_engine
    return mapping[engine](f, **self.options)
  File "/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/pandas/io/parsers/c_parser_wrapper.py", line 93, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 581, in pandas._libs.parsers.TextReader.__cinit__
pandas.errors.EmptyDataError: No columns to parse from file

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
```

### Option B Eval Log Tail

```text
/home/redafrix/miniconda3/envs/simvla/lib/python3.10/site-packages/hydra/_internal/hydra.py:119: UserWarning: Future Hydra versions will no longer change working directory at job runtime by default.
See https://hydra.cc/docs/1.2/upgrades/1.1_to_1.2/changes_to_job_working_dir/ for more information.
  ret = run_job(
-------------- Seed: 0 ----------------
-------------- Task: libero_fold00 ----------------
-------------- Seed: 1 ----------------
-------------- Task: libero_fold00 ----------------
-------------- Seed: 2 ----------------
-------------- Task: libero_fold00 ----------------
-------------- Seed: 42 ----------------
-------------- Task: libero_fold00 ----------------
-------------- Seed: 43 ----------------
-------------- Task: libero_fold00 ----------------
               Method    TWA  Accuracy  ...  TPR_std    TNR  TNR_std
0             entropy  0.639     0.817  ...    0.000  0.634    0.000
2  rnd_oe_and_entropy  0.625     0.808  ...    0.036  0.733    0.005
1              rnd_oe  0.553     0.625  ...    0.037  0.353    0.009

[3 rows x 14 columns]
```

## Final Flags

- MATERIALIZATION_COMPLETE = YES if validation tail contains `VALIDATION_PASS`
- DATASET_VALIDATION_PASS = YES if validation tail contains `VALIDATION_PASS`
- OPTION_A_PASS = YES if Option A CSVs/logs exist and no error appears in log tail
- OPTION_B_PASS = YES if Option B CSVs/logs exist and no error appears in log tail
- SAFE_TO_COMPARE_WITH_NEXTGEN = check the tables above before marking trusted
