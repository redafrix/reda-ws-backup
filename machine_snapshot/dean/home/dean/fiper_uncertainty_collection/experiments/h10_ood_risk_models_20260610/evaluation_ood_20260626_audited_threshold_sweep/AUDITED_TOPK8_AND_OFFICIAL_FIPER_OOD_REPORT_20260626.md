# Audited TopK8 Threshold Sweep on LIBERO Goal-Object OOD

This audit does not retrain or recalibrate. It loads the saved row-level scores from the prior TopK8 evaluation and recomputes episode metrics on the OOD dataset only.

## Dataset Checks

- Dataset: `/home/dean/fiper_uncertainty_collection/data/simvla_goal_object_ood_ablation_20260625/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`
- Rows: `44630`
- Episodes: `180`
- Success episodes: `149`
- Failure episodes: `31`
- Label-order check against `scores.npz`: `PASS`

## Selected Policies

| Policy | Threshold | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Query Time | Mean Timestep Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| any_row_fixed_0.3_online_gate | 0.3 | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 0.011 | 0.010 | 0.00% |
| any_row_fixed_0.5 | 0.5 | 97.99% | 100.00% | 100.00% | 100.00% | 100.00% | 0.016 | 0.015 | 0.00% |
| any_row_q95 | 0.615541 | 97.99% | 100.00% | 100.00% | 100.00% | 100.00% | 0.023 | 0.022 | 0.00% |
| any_row_q99 | 0.966594 | 67.79% | 100.00% | 51.61% | 96.77% | 100.00% | 0.100 | 0.099 | 0.00% |
| q95_mass_0.15 | 0.15 | 95.97% | 100.00% | 100.00% | 100.00% | 100.00% | 0.027 | 0.025 | 0.00% |
| q95_mass_0.2 | 0.2 | 94.63% | 100.00% | 100.00% | 100.00% | 100.00% | 0.029 | 0.028 | 0.00% |
| q95_mass_0.5 | 0.5 | 93.29% | 100.00% | 100.00% | 100.00% | 100.00% | 0.038 | 0.037 | 0.00% |
| q95_mass_1 | 1 | 89.93% | 100.00% | 96.77% | 100.00% | 100.00% | 0.067 | 0.065 | 0.00% |
| q95_mass_2 | 2 | 84.56% | 100.00% | 74.19% | 100.00% | 100.00% | 0.088 | 0.087 | 0.00% |
| q95_mass_5 | 5 | 63.09% | 100.00% | 22.58% | 96.77% | 96.77% | 0.134 | 0.133 | 0.00% |
| q95_mass_10 | 10 | 34.90% | 100.00% | 12.90% | 93.55% | 96.77% | 0.157 | 0.156 | 0.00% |
| q95_mass_20 | 20 | 20.81% | 96.77% | 3.23% | 90.32% | 96.77% | 0.166 | 0.165 | 3.23% |
| q99_mass_0.15 | 0.15 | 52.35% | 100.00% | 19.35% | 90.32% | 96.77% | 0.154 | 0.153 | 0.00% |
| q99_mass_0.5 | 0.5 | 28.86% | 93.55% | 9.68% | 90.32% | 93.55% | 0.140 | 0.139 | 6.45% |
| q99_mass_1 | 1 | 20.81% | 93.55% | 6.45% | 90.32% | 90.32% | 0.171 | 0.170 | 6.45% |

## Best Tradeoff Candidates

| Constraint | Policy | Threshold | Success FA | Failure Det | Det@25 | Det@50 | Mean Query Time | Never |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| best_overall_det_minus_fa | q95_mass_50 | 50 | 2.68% | 96.77% | 16.13% | 90.32% | 0.288 | 3.23% |
| best_FA_le_50 | q95_mass_50 | 50 | 2.68% | 96.77% | 16.13% | 90.32% | 0.288 | 3.23% |
| best_FA_le_25 | q95_mass_50 | 50 | 2.68% | 96.77% | 16.13% | 90.32% | 0.288 | 3.23% |
| best_FA_le_10 | q95_mass_50 | 50 | 2.68% | 96.77% | 16.13% | 90.32% | 0.288 | 3.23% |

## Official FIPER Result on Same OOD Dataset

```csv
Method,Window,Style,Success FA,Failure Det,Det@10,Det@25,Det@50,Mean Time,Never
entropy,29,Baseline (actual steps),1.0,1.0,1.0,1.0,1.0,0.03649193548387096,0.0
entropy,29,FIPER Forensic (max 300 steps),1.0,1.0,0.8064516129032258,1.0,1.0,0.09429280397022337,0.0
rnd_oe,48,Baseline (actual steps),1.0,1.0,1.0,1.0,1.0,0.0012500000000000002,0.0
rnd_oe,48,FIPER Forensic (max 300 steps),1.0,1.0,1.0,1.0,1.0,0.0,0.0
rnd_oe_and_entropy,48/16,Baseline (actual steps),1.0,1.0,0.967741935483871,1.0,1.0,0.05088709677419354,0.0
rnd_oe_and_entropy,48/16,FIPER Forensic (max 300 steps),1.0,1.0,0.25806451612903225,0.967741935483871,1.0,0.13280828568346104,0.0
```

## Interpretation

- The saved online selected-cap threshold `q95_mass_0.15` is not a good offline operating point on this OOD set: it detects all failures, but with very high false alarms.
- The official FIPER no-retrain ablation is worse as an OOD safety detector because every reported variant false-alarms on every successful OOD episode.
- For a paper table, use the sweep rows rather than only the saved online threshold, and clearly state that the OOD set was used only for test-time threshold comparison, not for training.

