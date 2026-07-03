# Dean Uncertainty Static Architecture Sweep v1

## Method

This sweep keeps the canonical transformer sequence path unchanged and keeps the same `unc_topk8` current uncertainty features.
Only the static/current branch or final fusion changes.

- `unc_topk8_deep_static_v1`: LayerNorm + 2-layer static MLP.
- `unc_topk8_gated_static_v1`: 2-layer static MLP plus learned gate between transformer CLS and static embedding.
- `unc_topk8_grouped_static_v1`: separate encoders for action stats, ACE, proprio, and top-8 uncertainty before fusion.

## Results

| Split | Policy | FA | Det | Det@25 | Det@50 | Mean Time | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|
| all_tasks_full | ref_base | 14.2% | 95.8% | 54.0% | 89.0% |  | 8 |
| all_tasks_full | ref_unc_topk8 | 15.0% | 97.5% | 65.0% | 89.5% | 0.205 | 3 |
| all_tasks_full | unc_topk8_deep_static_v1 | 15.8% | 97.0% | 61.2% | 87.8% | 0.230 | 2 |
| all_tasks_full | unc_topk8_gated_static_v1 | 17.0% | 97.0% | 62.0% | 89.0% | 0.212 | 5 |
| all_tasks_full | unc_topk8_grouped_static_v1 | 15.6% | 98.7% | 66.7% | 89.5% | 0.215 | 3 |
| ood_last2_taskids_full | ref_base | 26.0% | 86.0% | 39.8% | 78.5% |  | 2 |
| ood_last2_taskids_full | ref_unc_topk8 | 23.0% | 89.2% | 37.6% | 77.4% | 0.339 | 1 |
| ood_last2_taskids_full | unc_topk8_deep_static_v1 | 17.0% | 82.8% | 23.7% | 76.3% | 0.350 | 2 |
| ood_last2_taskids_full | unc_topk8_gated_static_v1 | 40.4% | 98.9% | 34.4% | 74.2% | 0.386 | 4 |
| ood_last2_taskids_full | unc_topk8_grouped_static_v1 | 35.7% | 79.6% | 57.0% | 72.0% | 0.182 | 1 |
