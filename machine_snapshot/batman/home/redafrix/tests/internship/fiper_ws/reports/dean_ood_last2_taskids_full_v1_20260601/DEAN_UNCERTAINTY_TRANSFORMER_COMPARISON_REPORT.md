# Dean Uncertainty Transformer Exploration v2

## Dataset

- Valid episodes used/indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks: `libero_10_object/task_4, libero_goal_object/task_9`

## Results

| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ood_last2_taskids_full | base |  |  |  |  | 26.0% | 86.0% | 39.8% | 78.5% | 2 |
| ood_last2_taskids_full | unc_raw |  |  |  |  | 28.9% | 84.9% | 35.5% | 83.9% | 2 |
