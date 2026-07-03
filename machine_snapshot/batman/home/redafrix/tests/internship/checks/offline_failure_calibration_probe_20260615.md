# Offline Failure-Calibration Probe

Model: `v2_018_transformer_k16`

Question: does adding failure episodes to the threshold calibration improve the offline detector tradeoff?

Definitions: `FA` = episode has at least one alarm on success episodes; `det` = episode has at least one alarm on failure episodes. `det25/det50` are approximate first-alarm timing metrics from logged timesteps.

| campaign | threshold | thr | seen_FA | ood_FA | seen_det | ood_det | ood_det25 | ood_det50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00_global_main | success_only_q95 | 0.4611 | 16.2% | n/a | 98.6% | n/a | n/a | n/a |
| 00_global_main | success_plus_failure_val_q95 | 0.9991 | 0.3% | n/a | 67.4% | n/a | n/a | n/a |
| 00_global_main | success_plus_failure_train_q95 | 0.9994 | 0.2% | n/a | 59.4% | n/a | n/a | n/a |
| 00_global_main | val_youden_any | 0.9268 | 4.9% | n/a | 96.4% | n/a | n/a | n/a |
| 01_ood_task_8_9 | success_only_q95 | 0.4851 | 18.9% | 31.6% | 99.2% | 100.0% | 59.7% | 80.6% |
| 01_ood_task_8_9 | success_plus_failure_val_q95 | 0.9929 | 0.8% | 3.5% | 60.0% | 52.8% | 16.7% | 30.6% |
| 01_ood_task_8_9 | success_plus_failure_train_q95 | 0.9959 | 0.0% | 3.2% | 40.0% | 33.3% | 15.3% | 18.1% |
| 01_ood_task_8_9 | val_youden_any | 0.8460 | 8.3% | 12.0% | 99.2% | 90.3% | 56.9% | 75.0% |
| 02_ood_perturbation_holdout_milk | success_only_q95 | 0.4689 | 24.7% | 41.2% | 98.9% | 97.4% | 69.7% | 90.9% |
| 02_ood_perturbation_holdout_milk | success_plus_failure_val_q95 | 0.9993 | 0.6% | 8.1% | 76.1% | 62.8% | 3.5% | 35.1% |
| 02_ood_perturbation_holdout_milk | success_plus_failure_train_q95 | 0.9997 | 0.4% | 5.1% | 59.8% | 34.6% | 1.7% | 12.1% |
| 02_ood_perturbation_holdout_milk | val_youden_any | 0.9935 | 3.4% | 18.8% | 91.3% | 89.6% | 20.3% | 66.2% |
| 02_ood_perturbation_holdout_mug | success_only_q95 | 0.4861 | 18.7% | 23.8% | 99.0% | 99.0% | 67.4% | 91.7% |
| 02_ood_perturbation_holdout_mug | success_plus_failure_val_q95 | 0.9994 | 0.8% | 1.2% | 72.4% | 62.2% | 5.7% | 28.0% |
| 02_ood_perturbation_holdout_mug | success_plus_failure_train_q95 | 0.9997 | 0.4% | 0.3% | 57.1% | 42.5% | 2.6% | 11.9% |
| 02_ood_perturbation_holdout_mug | val_youden_any | 0.9900 | 5.4% | 8.1% | 95.9% | 94.8% | 43.5% | 69.9% |
| 02_ood_perturbation_holdout_object | success_only_q95 | 0.6008 | 17.7% | 11.2% | 99.1% | 99.2% | 73.6% | 90.4% |
| 02_ood_perturbation_holdout_object | success_plus_failure_val_q95 | 0.9990 | 0.2% | 0.3% | 55.4% | 58.4% | 5.6% | 35.2% |
| 02_ood_perturbation_holdout_object | success_plus_failure_train_q95 | 0.9995 | 0.0% | 0.1% | 42.0% | 43.2% | 1.6% | 13.6% |
| 02_ood_perturbation_holdout_object | val_youden_any | 0.9640 | 6.4% | 3.4% | 94.6% | 90.4% | 56.8% | 80.8% |
| fold_00_holdout_alphabet_soup_bbq_sauce | success_only_q95 | 0.5133 | 16.2% | 26.1% | 100.0% | 97.6% | 26.2% | 88.1% |
| fold_00_holdout_alphabet_soup_bbq_sauce | success_plus_failure_val_q95 | 0.9605 | 6.6% | 2.4% | 90.5% | 69.0% | 0.0% | 47.6% |
| fold_00_holdout_alphabet_soup_bbq_sauce | success_plus_failure_train_q95 | 0.9838 | 2.9% | 0.5% | 57.1% | 42.9% | 0.0% | 16.7% |
| fold_00_holdout_alphabet_soup_bbq_sauce | val_youden_any | 0.8846 | 10.3% | 15.2% | 100.0% | 85.7% | 4.8% | 59.5% |
| fold_01_holdout_butter_chocolate_pudding | success_only_q95 | 0.5224 | 22.0% | 54.2% | 100.0% | 100.0% | 85.0% | 97.5% |
| fold_01_holdout_butter_chocolate_pudding | success_plus_failure_val_q95 | 0.9970 | 5.3% | 1.4% | 82.6% | 57.5% | 0.0% | 7.5% |
| fold_01_holdout_butter_chocolate_pudding | success_plus_failure_train_q95 | 0.9987 | 3.0% | 0.9% | 56.5% | 20.0% | 0.0% | 0.0% |
| fold_01_holdout_butter_chocolate_pudding | val_youden_any | 0.9117 | 12.1% | 25.9% | 91.3% | 100.0% | 57.5% | 85.0% |
| fold_02_holdout_cream_cheese_ketchup | success_only_q95 | 0.3793 | 34.8% | 75.2% | 100.0% | 100.0% | 100.0% | 100.0% |
| fold_02_holdout_cream_cheese_ketchup | success_plus_failure_val_q95 | 0.9990 | 0.8% | 32.0% | 84.6% | 90.0% | 56.7% | 76.7% |
| fold_02_holdout_cream_cheese_ketchup | success_plus_failure_train_q95 | 0.9996 | 0.8% | 26.1% | 69.2% | 73.3% | 43.3% | 63.3% |
| fold_02_holdout_cream_cheese_ketchup | val_youden_any | 0.9810 | 5.3% | 42.8% | 96.2% | 100.0% | 93.3% | 100.0% |
| fold_03_holdout_milk_orange_juice | success_only_q95 | 0.5515 | 24.2% | 20.2% | 100.0% | 100.0% | 54.2% | 100.0% |
| fold_03_holdout_milk_orange_juice | success_plus_failure_val_q95 | 0.9881 | 4.5% | 2.6% | 84.6% | 100.0% | 4.2% | 54.2% |
| fold_03_holdout_milk_orange_juice | success_plus_failure_train_q95 | 0.9930 | 3.0% | 0.9% | 57.7% | 79.2% | 0.0% | 29.2% |
| fold_03_holdout_milk_orange_juice | val_youden_any | 0.8936 | 14.4% | 7.0% | 100.0% | 100.0% | 25.0% | 95.8% |
| fold_04_holdout_salad_dressing_tomato_sauce | success_only_q95 | 0.4924 | 27.3% | 82.2% | 100.0% | 100.0% | 63.6% | 100.0% |
| fold_04_holdout_salad_dressing_tomato_sauce | success_plus_failure_val_q95 | 0.9826 | 4.5% | 2.1% | 64.3% | 54.5% | 0.0% | 27.3% |
| fold_04_holdout_salad_dressing_tomato_sauce | success_plus_failure_train_q95 | 0.9899 | 3.8% | 0.4% | 42.9% | 27.3% | 0.0% | 18.2% |
| fold_04_holdout_salad_dressing_tomato_sauce | val_youden_any | 0.9523 | 9.8% | 19.5% | 96.4% | 81.8% | 18.2% | 63.6% |

## Compact Verdict

### 00_global_main

- Baseline success-only q95: seen FA 16.2%, OOD FA n/a, seen det 98.6%, OOD det n/a, OOD det@25 n/a.

- success_plus_failure_val_q95: threshold 0.9991; seen FA 0.3%, OOD FA n/a, seen det 67.4%, OOD det n/a, OOD det@25 n/a.

- success_plus_failure_train_q95: threshold 0.9994; seen FA 0.2%, OOD FA n/a, seen det 59.4%, OOD det n/a, OOD det@25 n/a.

- val_youden_any: threshold 0.9268; seen FA 4.9%, OOD FA n/a, seen det 96.4%, OOD det n/a, OOD det@25 n/a.

### 01_ood_task_8_9

- Baseline success-only q95: seen FA 18.9%, OOD FA 31.6%, seen det 99.2%, OOD det 100.0%, OOD det@25 59.7%.

- success_plus_failure_val_q95: threshold 0.9929; seen FA 0.8%, OOD FA 3.5%, seen det 60.0%, OOD det 52.8%, OOD det@25 16.7%.

- success_plus_failure_train_q95: threshold 0.9959; seen FA 0.0%, OOD FA 3.2%, seen det 40.0%, OOD det 33.3%, OOD det@25 15.3%.

- val_youden_any: threshold 0.8460; seen FA 8.3%, OOD FA 12.0%, seen det 99.2%, OOD det 90.3%, OOD det@25 56.9%.

### 02_ood_perturbation_holdout_milk

- Baseline success-only q95: seen FA 24.7%, OOD FA 41.2%, seen det 98.9%, OOD det 97.4%, OOD det@25 69.7%.

- success_plus_failure_val_q95: threshold 0.9993; seen FA 0.6%, OOD FA 8.1%, seen det 76.1%, OOD det 62.8%, OOD det@25 3.5%.

- success_plus_failure_train_q95: threshold 0.9997; seen FA 0.4%, OOD FA 5.1%, seen det 59.8%, OOD det 34.6%, OOD det@25 1.7%.

- val_youden_any: threshold 0.9935; seen FA 3.4%, OOD FA 18.8%, seen det 91.3%, OOD det 89.6%, OOD det@25 20.3%.

### 02_ood_perturbation_holdout_mug

- Baseline success-only q95: seen FA 18.7%, OOD FA 23.8%, seen det 99.0%, OOD det 99.0%, OOD det@25 67.4%.

- success_plus_failure_val_q95: threshold 0.9994; seen FA 0.8%, OOD FA 1.2%, seen det 72.4%, OOD det 62.2%, OOD det@25 5.7%.

- success_plus_failure_train_q95: threshold 0.9997; seen FA 0.4%, OOD FA 0.3%, seen det 57.1%, OOD det 42.5%, OOD det@25 2.6%.

- val_youden_any: threshold 0.9900; seen FA 5.4%, OOD FA 8.1%, seen det 95.9%, OOD det 94.8%, OOD det@25 43.5%.

### 02_ood_perturbation_holdout_object

- Baseline success-only q95: seen FA 17.7%, OOD FA 11.2%, seen det 99.1%, OOD det 99.2%, OOD det@25 73.6%.

- success_plus_failure_val_q95: threshold 0.9990; seen FA 0.2%, OOD FA 0.3%, seen det 55.4%, OOD det 58.4%, OOD det@25 5.6%.

- success_plus_failure_train_q95: threshold 0.9995; seen FA 0.0%, OOD FA 0.1%, seen det 42.0%, OOD det 43.2%, OOD det@25 1.6%.

- val_youden_any: threshold 0.9640; seen FA 6.4%, OOD FA 3.4%, seen det 94.6%, OOD det 90.4%, OOD det@25 56.8%.

### fold_00_holdout_alphabet_soup_bbq_sauce

- Baseline success-only q95: seen FA 16.2%, OOD FA 26.1%, seen det 100.0%, OOD det 97.6%, OOD det@25 26.2%.

- success_plus_failure_val_q95: threshold 0.9605; seen FA 6.6%, OOD FA 2.4%, seen det 90.5%, OOD det 69.0%, OOD det@25 0.0%.

- success_plus_failure_train_q95: threshold 0.9838; seen FA 2.9%, OOD FA 0.5%, seen det 57.1%, OOD det 42.9%, OOD det@25 0.0%.

- val_youden_any: threshold 0.8846; seen FA 10.3%, OOD FA 15.2%, seen det 100.0%, OOD det 85.7%, OOD det@25 4.8%.

### fold_01_holdout_butter_chocolate_pudding

- Baseline success-only q95: seen FA 22.0%, OOD FA 54.2%, seen det 100.0%, OOD det 100.0%, OOD det@25 85.0%.

- success_plus_failure_val_q95: threshold 0.9970; seen FA 5.3%, OOD FA 1.4%, seen det 82.6%, OOD det 57.5%, OOD det@25 0.0%.

- success_plus_failure_train_q95: threshold 0.9987; seen FA 3.0%, OOD FA 0.9%, seen det 56.5%, OOD det 20.0%, OOD det@25 0.0%.

- val_youden_any: threshold 0.9117; seen FA 12.1%, OOD FA 25.9%, seen det 91.3%, OOD det 100.0%, OOD det@25 57.5%.

### fold_02_holdout_cream_cheese_ketchup

- Baseline success-only q95: seen FA 34.8%, OOD FA 75.2%, seen det 100.0%, OOD det 100.0%, OOD det@25 100.0%.

- success_plus_failure_val_q95: threshold 0.9990; seen FA 0.8%, OOD FA 32.0%, seen det 84.6%, OOD det 90.0%, OOD det@25 56.7%.

- success_plus_failure_train_q95: threshold 0.9996; seen FA 0.8%, OOD FA 26.1%, seen det 69.2%, OOD det 73.3%, OOD det@25 43.3%.

- val_youden_any: threshold 0.9810; seen FA 5.3%, OOD FA 42.8%, seen det 96.2%, OOD det 100.0%, OOD det@25 93.3%.

### fold_03_holdout_milk_orange_juice

- Baseline success-only q95: seen FA 24.2%, OOD FA 20.2%, seen det 100.0%, OOD det 100.0%, OOD det@25 54.2%.

- success_plus_failure_val_q95: threshold 0.9881; seen FA 4.5%, OOD FA 2.6%, seen det 84.6%, OOD det 100.0%, OOD det@25 4.2%.

- success_plus_failure_train_q95: threshold 0.9930; seen FA 3.0%, OOD FA 0.9%, seen det 57.7%, OOD det 79.2%, OOD det@25 0.0%.

- val_youden_any: threshold 0.8936; seen FA 14.4%, OOD FA 7.0%, seen det 100.0%, OOD det 100.0%, OOD det@25 25.0%.

### fold_04_holdout_salad_dressing_tomato_sauce

- Baseline success-only q95: seen FA 27.3%, OOD FA 82.2%, seen det 100.0%, OOD det 100.0%, OOD det@25 63.6%.

- success_plus_failure_val_q95: threshold 0.9826; seen FA 4.5%, OOD FA 2.1%, seen det 64.3%, OOD det 54.5%, OOD det@25 0.0%.

- success_plus_failure_train_q95: threshold 0.9899; seen FA 3.8%, OOD FA 0.4%, seen det 42.9%, OOD det 27.3%, OOD det@25 0.0%.

- val_youden_any: threshold 0.9523; seen FA 9.8%, OOD FA 19.5%, seen det 96.4%, OOD det 81.8%, OOD det@25 18.2%.
