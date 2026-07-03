# H10 TopK8 OOD180 Cap-300 Extended Threshold Sweep

No retrain. No OOD recalibration of the model. This sweep reuses the saved H10 TopK8 row scores and evaluates many episode-level alarm policies under the cap-300 label rule.

## Dataset

- Source dataset: `/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`
- Cap rule: keep only rows with `timestep < 300`; success only if the original rollout succeeded before step 300; otherwise failure.
- Episodes: `180`
- Cap-300 successes: `143`
- Cap-300 failures: `37`
- Original successful episodes converted to cap-300 failures: `6`
- Kept rows: `28031`
- Dropped rows: `16599`
- Saved row thresholds: q95=`0.615541`, q99=`0.966594`, saved mass=`0.150000`

## Selected Policies

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `q95_K3` | 95.1% | 100.0% | 62.2% | 100.0% | 100.0% | 0.083 | 0.0% |
| `q99_K3` | 60.1% | 89.2% | 2.7% | 21.6% | 86.5% | 0.272 | 10.8% |
| `q95_mass_0.15` | 95.8% | 100.0% | 62.2% | 100.0% | 100.0% | 0.081 | 0.0% |
| `q95_mass_1` | 89.5% | 94.6% | 21.6% | 75.7% | 94.6% | 0.176 | 5.4% |
| `q95_mass_5` | 62.2% | 91.9% | 2.7% | 16.2% | 89.2% | 0.279 | 8.1% |
| `q95_mass_10` | 33.6% | 91.9% | 2.7% | 13.5% | 86.5% | 0.338 | 8.1% |
| `q95_mass_20` | 18.9% | 91.9% | 0.0% | 0.0% | 83.8% | 0.437 | 8.1% |
| `q95_mass_30` | 15.4% | 89.2% | 0.0% | 0.0% | 24.3% | 0.515 | 10.8% |
| `q95_mass_40` | 1.4% | 83.8% | 0.0% | 0.0% | 10.8% | 0.592 | 16.2% |
| `q95_mass_50` | 0.0% | 83.8% | 0.0% | 0.0% | 0.0% | 0.693 | 16.2% |
| `q99_mass_0.5` | 27.3% | 86.5% | 0.0% | 10.8% | 83.8% | 0.341 | 13.5% |
| `q99_mass_1` | 18.9% | 86.5% | 0.0% | 5.4% | 75.7% | 0.412 | 13.5% |
| `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |
| `q99_mass_5` | 0.0% | 40.5% | 0.0% | 0.0% | 0.0% | 0.814 | 59.5% |
| `q99_mass_10` | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.000 | 100.0% |

## Best Candidates by False-Alarm Constraint

| Constraint | Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| best_overall | `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| best_FA_le_50 | `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| best_FA_le_35 | `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| best_FA_le_25 | `fixed_0.5_mass_30` | 17.5% | 91.9% | 0.0% | 0.0% | 83.8% | 0.445 | 8.1% |
| best_FA_le_15 | `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |
| best_FA_le_10 | `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |
| best_FA_le_5 | `q99_mass_2` | 1.4% | 83.8% | 0.0% | 0.0% | 27.0% | 0.548 | 16.2% |

## Interpretation

The cap-300 rule is stricter than the full-length 800-step audit. It rewards alarms that happen early enough to matter before a 300-step timeout and penalizes policies that detect only after the useful intervention window.

Full CSV: `/home/dean/fiper_uncertainty_collection/experiments/h10_ood_risk_models_20260610/evaluation_ood_20260626_cap300_extended_sweep_20260629/topk8_ood180_cap300_extended_sweep.csv`
