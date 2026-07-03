# Dean Uncertainty Top-K Temporal v1

## Method

This run starts from `unc_topk8` but moves the same selected uncertainty dimensions into the transformer temporal stream.

- Current static input: canonical base static features + current selected uncertainty top-8.
- History tokens: previous proprio/action/ACE history + previous selected uncertainty top-8.
- The current timestep's uncertainty is not inserted into previous-history tokens.
- Top-8 dimensions are reused from the prior seen train/validation ranking; test/OOD rows are not used for feature selection.

## Results

| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|
| all_tasks_full | ref_base | 14.2% | 95.8% | 54.0% | 89.0% |  | 8 |
| all_tasks_full | ref_unc_topk8 | 15.0% | 97.5% | 65.0% | 89.5% | 0.205 | 3 |
| all_tasks_full | unc_topk8_temporal_v1 | 14.6% | 96.6% | 55.3% | 86.1% | 0.243 | 12 |
| ood_last2_taskids_full | ref_base | 26.0% | 86.0% | 39.8% | 78.5% |  | 2 |
| ood_last2_taskids_full | ref_unc_topk8 | 23.0% | 89.2% | 37.6% | 77.4% | 0.339 | 1 |
| ood_last2_taskids_full | unc_topk8_temporal_v1 | 51.1% | 80.6% | 43.0% | 74.2% | 0.251 | 6 |

## Verdict Inputs

### all_tasks_full

- Base: FA 14.2%, Det 95.8%, Det@25 54.0%, Det@50 89.0%.
- Top-K8: FA 15.0%, Det 97.5%, Det@25 65.0%, Det@50 89.5%.
- Temporal Top-K8: FA 14.6%, Det 96.6%, Det@25 55.3%, Det@50 86.1%.

### ood_last2_taskids_full

- Base: FA 26.0%, Det 86.0%, Det@25 39.8%, Det@50 78.5%.
- Top-K8: FA 23.0%, Det 89.2%, Det@25 37.6%, Det@50 77.4%.
- Temporal Top-K8: FA 51.1%, Det 80.6%, Det@25 43.0%, Det@50 74.2%.

