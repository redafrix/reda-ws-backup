# SimVLA H10 TopK8 Official OOD Cap-300 Audit

Date: 2026-06-23

## Dataset

Source dataset:
`/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_20260622`

Derived cap-300 dataset:
`/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623`

Derivation rule:
- Keep only rows where `timestep < 300`.
- Label an episode success only if the original rollout succeeded before 300 steps.
- Any episode that reaches 300 steps is labeled failure.
- This is an offline derived dataset, not a fresh recollection.

Counts:

| Dataset | Episodes | Success | Failure | Rows |
|---|---:|---:|---:|---:|
| Original max-800 | 180 | 149 | 31 | 44,630 |
| Derived cap-300 | 180 | 143 | 37 | 28,031 |

Six original successes were converted to failures because they only succeeded after the 300-step cap.

## Model And Evaluation

Detector:
`/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`

Evaluation output:
`/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/simvla_libero_goal_object_ood_h10_uncertainty_180ep_cap300_20260623_selected_cap_topk8_offline_eval_corrected_mass_policy_online_ace`

Same corrected H10 TopK8 feature path was used:
- History: `16x21`
- Action chunk: `10x7`
- Static: `51`
- TopK8 uncertainty dims: `[6,21,25,27,23,2,26,24]`
- ACE formula matches online `run_policy_matrix.py`
- No explicit task id or timestep input

## Cap-300 Results

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| `score_q95_K3` | 95.1% | 100.0% | 62.2% | 100.0% | 100.0% | 0.083 | 0.0% |
| `score_q99_K3` | 60.1% | 89.2% | 2.7% | 21.6% | 86.5% | 0.272 | 10.8% |
| `score_q95_mass_conformal_0p15` | 95.8% | 100.0% | 62.2% | 100.0% | 100.0% | 0.081 | 0.0% |
| `score_q95_mass_10` | 33.6% | 91.9% | 2.7% | 13.5% | 86.5% | 0.338 | 8.1% |
| `score_q95_mass_20` | 18.9% | 91.9% | 0.0% | 0.0% | 83.8% | 0.437 | 8.1% |
| `score_q95_mass_50` | 0.0% | 83.8% | 0.0% | 0.0% | 0.0% | 0.693 | 16.2% |

## Comparison To Original Max-800 Audit

| Policy | Max-800 Success FA | Max-800 Failure Det | Max-800 Det@25 | Cap-300 Success FA | Cap-300 Failure Det | Cap-300 Det@25 |
|---|---:|---:|---:|---:|---:|---:|
| `score_q95_K3` | 95.3% | 100.0% | 100.0% | 95.1% | 100.0% | 100.0% |
| `score_q99_K3` | 60.4% | 100.0% | 90.3% | 60.1% | 89.2% | 21.6% |
| saved `q95_mass_0.15` | 96.0% | 100.0% | 100.0% | 95.8% | 100.0% | 100.0% |
| `q95_mass_10` | 34.9% | 100.0% | 93.5% | 33.6% | 91.9% | 13.5% |
| `q95_mass_20` | 20.8% | 96.8% | 90.3% | 18.9% | 91.9% | 0.0% |
| `q95_mass_50` | 2.7% | 96.8% | 16.1% | 0.0% | 83.8% | 0.0% |

## Interpretation

The cap-300 dataset is stricter. It removes late failure evidence and relabels six slow successes as failures. The detector still fires strongly under low thresholds, but calibrated mass policies detect fewer failures and much later. This confirms that the H10 TopK8 detector's useful offline OOD behavior on the official 18-task suite depends heavily on the allowed episode horizon and threshold/mass calibration.

