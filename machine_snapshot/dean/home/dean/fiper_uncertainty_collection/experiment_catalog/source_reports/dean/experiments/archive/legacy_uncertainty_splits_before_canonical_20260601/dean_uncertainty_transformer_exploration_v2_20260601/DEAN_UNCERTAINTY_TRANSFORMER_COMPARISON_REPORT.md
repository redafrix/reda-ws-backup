# Dean Uncertainty Transformer Exploration v2

## Dataset

- Valid episodes used/indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks: `libero_10_object/task_4, libero_goal_object/task_9`

## Results

| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all_tasks_random | base | 0.0% | 0.0% | 0.0% | 0.0% |  |  |  |  | 10 |
| all_tasks_random | unc_raw | 5.6% | 93.3% | 12.2% | 62.8% |  |  |  |  | 4 |
| all_tasks_random | unc_summary | 7.2% | 91.1% | 5.0% | 60.0% |  |  |  |  | 5 |
| all_tasks_random | unc_summary_only | 0.0% | 0.0% | 0.0% | 0.0% |  |  |  |  | 28 |
| all_tasks_random | unc_raw_dropout | 5.6% | 91.1% | 1.1% | 45.0% |  |  |  |  | 5 |
| ood_suite_libero90 | base | 6.5% | 91.0% | 51.1% | 64.7% | 31.2% | 81.9% | 42.3% | 72.7% | 1 |
| ood_suite_libero90 | unc_raw | 5.7% | 91.0% | 46.6% | 66.2% | 31.5% | 85.4% | 42.7% | 74.6% | 2 |
| ood_suite_libero90 | unc_summary | 2.4% | 88.0% | 44.4% | 60.9% | 27.7% | 72.7% | 37.7% | 63.8% | 1 |
| ood_suite_libero90 | unc_summary_only | 3.3% | 83.5% | 27.8% | 56.4% | 16.2% | 70.8% | 18.8% | 61.9% | 3 |
| ood_suite_libero90 | unc_raw_dropout | 5.7% | 85.7% | 43.6% | 66.2% | 29.6% | 81.5% | 43.1% | 71.9% | 2 |
| ood_task_holdout | base | 15.0% | 95.6% | 42.2% | 83.3% | 11.9% | 81.5% | 3.2% | 49.2% | 1 |
| ood_task_holdout | unc_raw | 1.7% | 87.8% | 0.0% | 42.8% | 1.9% | 62.9% | 0.0% | 7.3% | 5 |
| ood_task_holdout | unc_summary | 1.7% | 83.3% | 0.0% | 30.6% | 1.9% | 54.0% | 0.0% | 1.6% | 6 |
| ood_task_holdout | unc_summary_only | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 10 |
| ood_task_holdout | unc_raw_dropout | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 12 |
