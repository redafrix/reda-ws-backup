# Dean Uncertainty Transformer Exploration v2

## Dataset

- Valid episodes used/indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks: `libero_10_object/task_4, libero_goal_object/task_9`

## Results

| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all_tasks_random | base | 14.2% | 95.8% | 54.0% | 89.0% |  |  |  |  | 8 |
| all_tasks_random | unc_raw | 16.8% | 97.5% | 67.1% | 87.8% |  |  |  |  | 4 |
