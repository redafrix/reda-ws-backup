# Dean Uncertainty Transformer Comparison v1

## Dataset

- Valid episodes used/indexed: `4191`
- Successes: `3405`
- Failures/timeouts: `786`
- Excluded bad reset tasks: `libero_10_object/task_4, libero_goal_object/task_9`

## Results

| Split | Variant | Seen FA | Seen Det | Seen Det@25 | Seen Det@50 | OOD FA | OOD Det | OOD Det@25 | OOD Det@50 | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| random_mixed | base | 0.0% | 50.0% | 0.0% | 50.0% |  |  |  |  | 1 |
| random_mixed | uncertainty | 0.0% | 50.0% | 50.0% | 50.0% |  |  |  |  | 1 |
