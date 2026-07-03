# Selected-Cap TopK8 Offline Evaluation on LIBERO Goal-Object OOD

- Dataset root: `/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`
- Risk model dir: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/unc_topk8`
- Rows: `44630`
- Episodes: `180`
- Success episodes: `149`
- Failure episodes: `31`
- Runtime seconds: `34.3`

## Policy Metrics

Primary policy is the historical selected-cap TopK8 offline policy: cumulative conformal risk mass above the q95 row threshold.

| Threshold | Value | AUROC | AUPRC | Step FPR | Step FNR | Episode false alarm | Failure detection | Det@10 | Det@25 | Det@50 | Mean detection frac |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| score_q95_mass_conformal | 0.1500 | 0.7330 | 0.7567 | 38.01% | 23.91% | 95.97% | 100.00% | 100.00% | 100.00% | 100.00% | 0.025475392627881628 |
| any_row_fixed_0.3_online_gate | 0.3000 | 0.7330 | 0.7567 | 51.89% | 13.92% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.011209677419354839 |
| any_row_fixed_0.5 | 0.5000 | 0.7330 | 0.7567 | 42.94% | 20.62% | 97.99% | 100.00% | 100.00% | 100.00% | 100.00% | 0.01633064516129032 |
| any_row_q95 | 0.6155 | 0.7330 | 0.7567 | 38.01% | 23.91% | 97.99% | 100.00% | 100.00% | 100.00% | 100.00% | 0.023225806451612898 |
| any_row_q99 | 0.9666 | 0.7330 | 0.7567 | 20.58% | 43.92% | 67.79% | 100.00% | 51.61% | 96.77% | 100.00% | 0.09971774193548384 |

## Legitimacy Notes

- Dataset collection uses modified SimVLA with uncertainty head, not the risk-aware selected-cap policy.
- This script only loads the selected-cap TopK8 detector after collection and scores rows offline.
- Primary policy uses `mass_t += max(0, score_t - q95)` and alarms when mass reaches the saved conformal-mass threshold.
- Inputs exclude explicit task id and explicit timestep.
