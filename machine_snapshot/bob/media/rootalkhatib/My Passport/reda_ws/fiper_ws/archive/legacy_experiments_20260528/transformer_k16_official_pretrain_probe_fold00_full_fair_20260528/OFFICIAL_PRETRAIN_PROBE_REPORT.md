# Transformer K16 Official Pretrain Fold 00 Full Fair Report

## Setup & Command

- Target Fold: `fold_00_holdout_alphabet_soup_bbq_sauce`
- Official Stride: `5`
- Max Rows Per Split: `Full Data (No cap)`
- Pretrain Epochs: `10`
- Max Fine-tune Epochs: `120`
- Patience: `18`
- Learning Rate: `0.0002`
- Batch Size: `384`
- Device: `cuda`
- Exclusion Check: Held-out official objects `['alphabet_soup', 'bbq_sauce']` were **successfully excluded** from pretraining.
- Forbidden Features Check: No reward, success, object poses, language or future labels were used.

## Episode Counts Per Split

| Split | Number of Episodes |
|---|---:|
| success_train_seen | 497 |
| success_val_seen | 135 |
| success_calib_seen | 135 |
| success_test_seen | 136 |
| success_test_ood | 211 |
| failure_train_seen | 63 |
| failure_val_seen | 21 |
| failure_test_seen | 21 |
| failure_eval_ood | 42 |

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
| 1 | 0.304893 | 0.300573 | 0.9058 | 0.9059 |
| 2 | 0.224439 | 0.221265 | 0.9144 | 0.9186 |
| 3 | 0.188240 | 0.187536 | 0.9148 | 0.9110 |
| 4 | 0.162105 | 0.163043 | 0.9022 | 0.9156 |
| 5 | 0.146338 | 0.143478 | 0.9154 | 0.9162 |
| 6 | 0.130878 | 0.130231 | 0.9136 | 0.9130 |
| 7 | 0.121289 | 0.119472 | 0.8948 | 0.8851 |
| 8 | 0.111749 | 0.112227 | 0.9043 | 0.9016 |
| 9 | 0.103648 | 0.102747 | 0.8922 | 0.8879 |
| 10 | 0.097019 | 0.098185 | 0.8943 | 0.8811 |
| 11 | 0.090847 | 0.091683 | 0.8814 | 0.8835 |
| 12 | 0.086335 | 0.086684 | 0.8862 | 0.8807 |
| 13 | 0.082187 | 0.082499 | 0.8736 | 0.8835 |
| 14 | 0.076420 | 0.078828 | 0.8911 | 0.8869 |
| 15 | 0.074408 | 0.075769 | 0.8859 | 0.8880 |
| 16 | 0.070351 | 0.073949 | 0.8812 | 0.8814 |
| 17 | 0.067284 | 0.068640 | 0.8790 | 0.8786 |
| 18 | 0.063093 | 0.066405 | 0.8723 | 0.8865 |
| 19 | 0.060013 | 0.064544 | 0.8784 | 0.8834 |
| 20 | 0.056301 | 0.061406 | 0.8831 | 0.8870 |
| 21 | 0.053965 | 0.059322 | 0.8700 | 0.8763 |
| 22 | 0.052392 | 0.056072 | 0.8780 | 0.8883 |
| 23 | 0.050648 | 0.055637 | 0.8874 | 0.8896 |

## Conformal Policy Calibration Metrics
- **Existing Real v2_018:** $q_{95}$ Row Threshold = `0.51326`, Conformal Mass Threshold = `0.08968`
- **Baseline Model (Random-Init):** $q_{95}$ Row Threshold = `0.72413`, Conformal Mass Threshold = `0.63399` (Best Epoch: `5`)
- **Pretrained Model (Official Pretrain):** $q_{95}$ Row Threshold = `0.76922`, Conformal Mass Threshold = `0.28226` (Best Epoch: `5`)

## Evaluation Metrics Comparison

| Model Configuration | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Existing Real v2_018 | 15.4% | 25.6% | 95.2% | 0.0% | 26.2% | 85.7% | 0.332 | 4.8% |
| Baseline (Random-Init) | 16.2% | 28.9% | 95.2% | 0.0% | 23.8% | 83.3% | 0.344 | 4.8% |
| Official-Pretrained | 18.4% | 28.4% | 95.2% | 0.0% | 14.3% | 85.7% | 0.336 | 4.8% |

## Decision Rule Checking & Final Verdict

- `MECHANICAL_RUN_PASS` = **YES**
- `REPORT_CONTRADICTION_FIXED` = **YES**
- `OFFICIAL_HELDOUT_OBJECTS_EXCLUDED` = **YES**
- `OFFICIAL_PRETRAIN_BEATS_REAL_EXISTING_V2_018` = **NO**
- `OFFICIAL_PRETRAIN_REDUCES_OOD_FA_WITHOUT_LOSING_FAILURE_DETLECTION` = **NO**
- `READY_FOR_ALL_FOLDS_OFFICIAL_PRETRAIN` = **NO**

### Decision Rule Verification Notes
- Existing Real v2_018 OOD FA: `25.6%` vs Pretrained OOD FA: `28.4%` (Lower OOD FA: **False**)
- Existing Real v2_018 Failure Det: `95.2%` vs Pretrained Failure Det: `95.2%` (Within 5%: **True**)
- Existing Real v2_018 Det@50: `85.7%` vs Pretrained Det@50: `85.7%` (Within 5%: **True**)
