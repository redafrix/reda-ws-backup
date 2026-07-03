# Transformer K16 Official Pretrain Probe Report

## Setup & Command

- Target Fold: `fold_00_holdout_alphabet_soup_bbq_sauce`
- Official Stride: `5`
- Max Rows Per Split: `10000`
- Pretrain Epochs: `10`
- Fine-tune Epochs: `10`
- Learning Rate: `0.0002`
- Batch Size: `384`
- Device: `cuda`
- Exclusion Check: Held-out official objects `['alphabet_soup', 'bbq_sauce']` were **successfully excluded** from pretraining.
- Forbidden Features Check: No reward, success, object poses, language or future labels were used.

## Training Loss History

### Stage A: Action Encoder Pretraining Loss
| Pretrain Epoch | MSE Loss |
|---|---|
| 1 | 0.486006 |
| 2 | 0.031170 |
| 3 | 0.000946 |
| 4 | 0.000042 |
| 5 | 0.000002 |
| 6 | 0.000000 |
| 7 | 0.000000 |
| 8 | 0.000000 |
| 9 | 0.000000 |
| 10 | 0.000000 |

### Stage B: Fine-Tuning Loss Curve Comparison
| Epoch | Baseline Train Loss | Pretrained Train Loss | Baseline Val AUC | Pretrained Val AUC |
|---|---|---|---|---|
| 1 | 0.124304 | 0.129352 | 0.7643 | 0.7592 |
| 2 | 0.027102 | 0.026643 | 0.7502 | 0.7717 |
| 3 | 0.019942 | 0.020050 | 0.7118 | 0.7354 |
| 4 | 0.014937 | 0.015568 | 0.6848 | 0.7129 |
| 5 | 0.011061 | 0.011380 | 0.6496 | 0.6578 |
| 6 | 0.009981 | 0.009428 | 0.6502 | 0.6705 |
| 7 | 0.008865 | 0.008188 | 0.6245 | 0.6231 |
| 8 | 0.008374 | 0.008236 | 0.6421 | 0.6317 |
| 9 | 0.008113 | 0.007712 | 0.6125 | 0.6270 |
| 10 | 0.007572 | 0.006632 | 0.6141 | 0.6286 |

## Conformal Policy Calibration Metrics
- **Baseline Model:** $q_{95}$ Row Threshold = `0.99690`, Conformal Mass Threshold = `0.00102` (Best Epoch: `1`)
- **Pretrained Model:** $q_{95}$ Row Threshold = `0.99890`, Conformal Mass Threshold = `0.00046` (Best Epoch: `2`)

## Evaluation Metrics Comparison

| Model Configuration | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Random-Init Baseline | 15.4% | 0.0% | 81.0% | 0.0% | 0.0% | 35.7% | 0.536 | 19.0% |
| Official-Pretrained | 11.8% | 0.0% | 81.0% | 0.0% | 2.4% | 38.1% | 0.515 | 19.0% |

## Final Verdict

- `OFFICIAL_PRETRAIN_SMOKE_PASS` = **YES**
- `OFFICIAL_PRETRAIN_IMPROVES_OVER_RANDOM_INIT` = **YES**
- `OFFICIAL_PRETRAIN_REDUCES_FA_WITHOUT_HURTING_DETECTION` = **NO**
- `READY_FOR_ALL_FOLDS_OFFICIAL_PRETRAIN_RUN` = **NO**
