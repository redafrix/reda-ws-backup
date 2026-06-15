# FIPER ACE Sampling Ablation Fold00 Report

Policy: current score-only q95 row threshold from success_calib_seen plus conformal episode risk-mass threshold from success_val_seen, alpha=0.15.

| Job | ACE Candidates | ACE Stride | Seen FA | OOD FA | OOD Failure Det | Det@25 | Det@50 | Mean Time | Never | Best Epoch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `existing_real_v2_018` | 8 | 1 | 15.4% | 25.6% | 95.2% | 26.2% | 85.7% | 0.332 | 4.8% | 1 |
| `ace_ablate_00_control_full8_every_step` | 8 | 1 | 16.2% | 28.9% | 95.2% | 23.8% | 83.3% | 0.344 | 4.8% | 5 |
| `ace_ablate_01_full8_every_2_steps` | 8 | 2 | 14.0% | 26.5% | 92.9% | 19.0% | 83.3% | 0.354 | 7.1% | 1 |
| `ace_ablate_02_first4_every_step` | 4 | 1 | 15.4% | 28.0% | 95.2% | 31.0% | 90.5% | 0.312 | 4.8% | 2 |
| `ace_ablate_03_first4_every_2_steps` | 4 | 2 | 14.0% | 20.4% | 95.2% | 14.3% | 81.0% | 0.378 | 4.8% | 1 |

## Decision

Lowest OOD false-alarm ablation: `ace_ablate_03_first4_every_2_steps`.

Final fields:

```text
BEST_ABLATION_BY_OOD_FA = ace_ablate_03_first4_every_2_steps
BEST_ABLATION_OOD_FA = 0.203791
BEST_ABLATION_FAILURE_DET = 0.952381
BEST_ABLATION_DET_AT_25 = 0.142857
BEST_ABLATION_DET_AT_50 = 0.809524
```
