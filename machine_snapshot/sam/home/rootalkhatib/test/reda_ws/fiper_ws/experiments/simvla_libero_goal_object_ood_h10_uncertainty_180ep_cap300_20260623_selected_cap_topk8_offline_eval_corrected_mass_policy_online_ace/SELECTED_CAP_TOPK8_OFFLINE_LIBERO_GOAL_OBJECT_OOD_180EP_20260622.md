# Selected-Cap TopK8 Offline Evaluation on LIBERO Goal-Object OOD

- Dataset root: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623`
- Risk model dir: `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
- Rows: `28031`
- Episodes: `180`
- Success episodes: `143`
- Failure episodes: `37`
- Runtime seconds: `23.7`

## Policy Metrics

Primary policy is the historical selected-cap TopK8 offline policy: cumulative conformal risk mass above the q95 row threshold.

| Threshold | Value | AUROC | AUPRC | Step FPR | Step FNR | Episode false alarm | Failure detection | Det@10 | Det@25 | Det@50 | Mean detection frac |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| score_q95_mass_conformal | 0.1500 | 0.7409 | 0.6305 | 33.83% | 28.69% | 95.80% | 100.00% | 62.16% | 100.00% | 100.00% | 0.07791738226520835 |
| any_row_fixed_0.3_online_gate | 0.3000 | 0.7409 | 0.6305 | 49.31% | 15.85% | 100.00% | 100.00% | 91.89% | 100.00% | 100.00% | 0.039099099099099095 |
| any_row_fixed_0.5 | 0.5000 | 0.7409 | 0.6305 | 39.37% | 24.66% | 97.90% | 100.00% | 86.49% | 100.00% | 100.00% | 0.05234234234234234 |
| any_row_q95 | 0.6155 | 0.7409 | 0.6305 | 33.83% | 28.69% | 97.90% | 100.00% | 72.97% | 100.00% | 100.00% | 0.06873873873873874 |
| any_row_q99 | 0.9666 | 0.7409 | 0.6305 | 14.97% | 44.38% | 67.83% | 94.59% | 2.70% | 27.03% | 91.89% | 0.2621904761904762 |

## Legitimacy Notes

- Dataset collection uses modified SimVLA with uncertainty head, not the risk-aware selected-cap policy.
- This script only loads the selected-cap TopK8 detector after collection and scores rows offline.
- Primary policy uses `mass_t += max(0, score_t - q95)` and alarms when mass reaches the saved conformal-mass threshold.
- Inputs exclude explicit task id and explicit timestep.
