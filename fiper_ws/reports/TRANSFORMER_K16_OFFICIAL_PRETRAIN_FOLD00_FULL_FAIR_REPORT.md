# Transformer K16 Official Pretrain Fold 00 Full Fair Report

This report presents a fair, uncapped validation of action encoder pretraining on `fold_00_holdout_alphabet_soup_bbq_sauce` using the full dataset and NextGen early stopping parameters. It compares the existing real `v2_018_transformer_k16` baseline, a new random-init baseline trained with the updated parameters, and the new official-pretrained model.

## 1. Execution Setup & Exact Commands

### Target Machine & User
- **Host:** Bob (`pcrobot` / `PCROBOTUBUNTU02`)
- **User:** `rootalkhatib`

### Exact Command Run
```bash
ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && python3 scripts/run_transformer_k16_official_pretrain_probe_v1.py --fold fold_00_holdout_alphabet_soup_bbq_sauce --official-stride 5 --pretrain-epochs 10 --max-epochs 120 --patience 18 --batch-size 384 --device cuda --output-dir experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528"
```

---

## 2. Process & GPU Status

- **Running campaigns:** None active before or after execution.
- **GPU Memory Usage Before:** `15MiB / 8188MiB`
- **GPU Memory Usage After:** `15MiB / 8188MiB` (returned to idle)

---

## 3. Scope of Objects & Feature Hygiene

- **Official Seen Objects Used (Pretraining):** `['butter', 'chocolate_pudding', 'cream_cheese', 'ketchup', 'milk', 'orange_juice', 'salad_dressing', 'tomato_sauce']`
- **Official Held-out Objects Excluded (Forbidden):** `['alphabet_soup', 'bbq_sauce']` (strictly validated to prevent leakage)
- **Forbidden Deploy-time Features Used:** None. Fine-tuning and evaluation used only FIPER receding splits, with zero access to reward, success signals, object poses, language context, or future outcomes.

---

## 4. Exact Files Created

The experiment generated the following files in the remote workspace on Bob:
1. **Script:** `scripts/run_transformer_k16_official_pretrain_probe_v1.py`
2. **Pretrained Weights:** `experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528/pretrained_encoder.pt`
3. **Training History (Baseline):** `experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528/baseline_history.json`
4. **Training History (Pretrained):** `experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528/pretrained_history.json`
5. **Pretrain Loss History:** `experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528/pretrain_loss_history.json`
6. **Topline MD Report:** `experiments/transformer_k16_official_pretrain_probe_fold00_full_fair_20260528/OFFICIAL_PRETRAIN_PROBE_REPORT.md`

---

## 5. Episode Counts Per Split

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

---

## 6. Training Loss History

### Stage A: Action Encoder Pretraining Loss (Official Chunks)
- **Epoch 1:** `0.486006`
- **Epoch 5:** `0.000002`
- **Epoch 10:** `0.000000` (reconstruction converges completely)

### Stage B: Fine-Tuning Loss Curve Comparison
Both the baseline and pretrained models trained with early stopping (patience = 18).
- **Baseline Model (Random-Init):** Best Epoch = `5` (validation score = `0.8341`), early stopped at Epoch `23`.
- **Pretrained Model (Official Pretrain):** Best Epoch = `5` (validation score = `0.8380`), early stopped at Epoch `23`.

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

---

## 7. Conformal Policy Calibration Metrics

All models are evaluated using the event-level conformal policy: row threshold $q_{95}$ calibrated on `success_calib_seen` and episode mass threshold calibrated on `success_val_seen` with $\alpha = 0.15$.

- **Existing Real v2_018:** $q_{95} = 0.51326$, Mass Threshold = `0.08968`
- **Baseline (Random-Init):** $q_{95} = 0.72413$, Mass Threshold = `0.63399`
- **Official-Pretrained:** $q_{95} = 0.76922$, Mass Threshold = `0.28226`

---

## 8. Evaluation Metrics Comparison

| Model Configuration | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Existing Real v2_018** | 15.4% | 25.6% | 95.2% | 0.0% | 26.2% | 85.7% | 0.332 | 4.8% |
| **Baseline (Random-Init)** | 16.2% | 28.9% | 95.2% | 0.0% | 23.8% | 83.3% | 0.344 | 4.8% |
| **Official-Pretrained** | 18.4% | 28.4% | 95.2% | 0.0% | 14.3% | 85.7% | 0.336 | 4.8% |

---

## 9. Decision Rule Checking & Final Verdict

### Decision Rule Check:
1. **OOD FA Reduction:** Pretrained OOD FA (`28.4%`) is **higher** than Existing Real v2_018 OOD FA (`25.6%`). (Condition `OOD_FA_reduced` = **False**)
2. **OOD Failure Recall Check:** Pretrained Failure Recall (`95.2%`) is within 5% of Existing Real (`95.2%`). (Condition `OOD_Recall_ok` = **True**)
3. **Early Warning Rate Check:** Pretrained Det@50 (`85.7%`) is within 5% of Existing Real (`85.7%`). (Condition `Det50_ok` = **True**)

Since pretraining fails the primary condition of lowering OOD False Alarms compared to the existing real campaign baseline on the full validation dataset, `READY_FOR_ALL_FOLDS_OFFICIAL_PRETRAIN` must be set to **NO**.

### Final Verdict:
- `MECHANICAL_RUN_PASS` = **YES**
- `REPORT_CONTRADICTION_FIXED` = **YES**
- `OFFICIAL_HELDOUT_OBJECTS_EXCLUDED` = **YES**
- `OFFICIAL_PRETRAIN_BEATS_REAL_EXISTING_V2_018` = **NO** (both Seen FA and OOD FA are higher, and Det@25 is lower)
- `OFFICIAL_PRETRAIN_REDUCES_OOD_FA_WITHOUT_LOSING_FAILURE_DETECTION` = **NO** (it actually increases OOD FA slightly)
- `READY_FOR_ALL_FOLDS_OFFICIAL_PRETRAIN` = **NO**
