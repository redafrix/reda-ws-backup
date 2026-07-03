# Selected-Cap TopK8 Offline Evaluation on LIBERO Goal-Object OOD

- Dataset root: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`
- Risk model dir: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Rows: `44630`
- Episodes: `180`
- Success episodes: `149`
- Failure episodes: `31`
- Runtime seconds: `33.3`

## Threshold Metrics

| Threshold | Value | AUROC | AUPRC | Step FPR | Step FNR | Episode false alarm | Failure detection | Det@10 | Det@25 | Det@50 | Mean detection frac |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed_0.3_online_gate | 0.3000 | 0.7298 | 0.7891 | 100.00% | 0.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.0012500000000000002 |
| fixed_0.5 | 0.5000 | 0.7298 | 0.7891 | 100.00% | 0.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.0012500000000000002 |
| conformal_mass | 0.1500 | 0.7298 | 0.7891 | 100.00% | 0.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.0012500000000000002 |
| q95 | 0.6155 | 0.7298 | 0.7891 | 100.00% | 0.07% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.0012500000000000002 |
| q99 | 0.9666 | 0.7298 | 0.7891 | 0.00% | 100.00% | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% | NA |

## Legitimacy Notes

- Dataset collection uses modified SimVLA with uncertainty head, not the risk-aware selected-cap policy.
- This script only loads the selected-cap TopK8 detector after collection and scores rows offline.
- Inputs exclude explicit task id and explicit timestep.
