# Dean Uncertainty Top-K Feature Sweep v1

## Method

This run keeps the canonical transformer architecture and canonical episode splits fixed.
It adds only the top-K uncertainty dimensions selected from seen train/validation rows.
Test and OOD rows are not used for feature ranking.

## Results

| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|
| all_tasks_full | ref_base | 14.2% | 95.8% | 54.0% | 89.0% |  | 8 |
| all_tasks_full | ref_unc_raw | 16.8% | 97.5% | 67.1% | 87.8% |  | 4 |
| all_tasks_full | unc_topk8 | 15.0% | 97.5% | 65.0% | 89.5% | 0.205 | 3 |
| all_tasks_full | unc_topk16 | 15.6% | 97.9% | 61.2% | 86.9% | 0.226 | 2 |
| all_tasks_full | unc_topk32 | 18.9% | 97.9% | 65.4% | 89.9% | 0.203 | 4 |
| ood_last2_taskids_full | ref_base | 26.0% | 86.0% | 39.8% | 78.5% |  | 2 |
| ood_last2_taskids_full | ref_unc_raw | 28.9% | 84.9% | 35.5% | 83.9% |  | 2 |
| ood_last2_taskids_full | unc_topk8 | 23.0% | 89.2% | 37.6% | 77.4% | 0.339 | 1 |
| ood_last2_taskids_full | unc_topk16 | 29.4% | 89.2% | 28.0% | 72.0% | 0.366 | 1 |
| ood_last2_taskids_full | unc_topk32 | 21.3% | 80.6% | 22.6% | 69.9% | 0.366 | 2 |
