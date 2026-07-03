# Pi0.5 No-Task9 Risk Head: OOD Offline Evaluation

- Risk experiment: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/offline_risk_experiments/pi05_goal_object_h10_risk_no_task9_20260625`
- OOD source: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/online_evals/pi05_libero_goal_object_ood_basic_vs_selected_cap_10ep_20260625`
- Episodes: `180`
- Queries: `2370`

## Step Metrics

- AUROC: `0.6798`
- AUPRC: `0.2770`
- F1: `0.3377`
- FPR: `0.3434`
- FNR: `0.3500`

## Episode Metrics

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1 | 96.02% | 100.00% | 100.0% | 100.0% | 100.0% | 0.028 | 0.0% |
| q90 | 89.20% | 100.00% | 100.0% | 100.0% | 100.0% | 0.041 | 0.0% |
| q95 | 23.86% | 50.00% | 25.0% | 25.0% | 25.0% | 0.344 | 50.0% |
| q99 | 11.36% | 25.00% | 0.0% | 25.0% | 25.0% | 0.113 | 75.0% |
| q95_K3 | 15.91% | 50.00% | 25.0% | 25.0% | 25.0% | 0.419 | 50.0% |
| q99_K3 | 9.09% | 25.00% | 0.0% | 25.0% | 25.0% | 0.113 | 75.0% |
| q95_mass_1 | 10.80% | 50.00% | 0.0% | 25.0% | 25.0% | 0.581 | 50.0% |
| q95_mass_5 | 0.00% | 25.00% | 0.0% | 0.0% | 25.0% | 0.388 | 75.0% |
| q95_mass_10 | 0.00% | 25.00% | 0.0% | 0.0% | 0.0% | 0.838 | 75.0% |
| q95_mass_20 | 0.00% | 0.00% | 0.0% | 0.0% | 0.0% | 1.000 | 100.0% |
| q95_mass_50 | 0.00% | 0.00% | 0.0% | 0.0% | 0.0% | 1.000 | 100.0% |
