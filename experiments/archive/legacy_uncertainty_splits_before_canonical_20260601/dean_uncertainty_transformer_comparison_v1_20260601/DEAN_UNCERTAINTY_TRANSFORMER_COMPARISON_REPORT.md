# Dean Uncertainty Transformer Comparison v1

## Dataset

- Valid episodes used/indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks: `libero_10_object/task_4, libero_goal_object/task_9`

## Results

| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| random_mixed | base | 0.0% | 0.0% | 0.0% | 0.0% |  |  |  |  | 10 |
| random_mixed | uncertainty | 0.0% | 0.0% | 0.0% | 0.0% |  |  |  |  | 14 |
| ood_suite_libero90 | base | 5.7% | 100.0% | 0.0% | 0.0% | 26.9% | 74.6% | 41.9% | 67.7% | 2 |
| ood_suite_libero90 | uncertainty | 0.8% | 0.0% | 0.0% | 0.0% | 1.5% | 51.9% | 0.0% | 0.0% | 7 |
| ood_task_holdout | base | 5.0% | 100.0% | 0.0% | 100.0% | 4.6% | 69.4% | 0.8% | 9.7% | 4 |
| ood_task_holdout | uncertainty | 1.1% | 100.0% | 0.0% | 100.0% | 1.2% | 54.8% | 0.0% | 0.0% | 6 |
