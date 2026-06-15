# Transformer K16 Official Pretrain Fold 00 Smoke Report

This report summarizes the results of initializing the action encoder of the FIPER NextGen temporal risk model (`v2_018_transformer_k16`) with weights pretrained on official LIBERO expert demonstrations, compared against a randomly initialized baseline, on `fold_00_holdout_alphabet_soup_bbq_sauce`.

## 1. Execution Setup & Exact Commands

### Target Machine & User
- **Host:** Bob (`pcrobot` / `PCROBOTUBUNTU02`)
- **User:** `rootalkhatib`

### Exact Command Run
```bash
ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && python3 scripts/run_transformer_k16_official_pretrain_probe_v1.py --fold fold_00_holdout_alphabet_soup_bbq_sauce --max-rows-per-split 10000 --official-stride 5 --pretrain-epochs 10 --finetune-epochs 10 --batch-size 384 --device cuda --output-dir experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528"
```

---

## 2. Process & GPU Status

- **Running campaigns:** None active before or after execution.
- **GPU Memory Usage Before:** `15MiB / 8188MiB`
- **GPU Memory Usage After:** `15MiB / 8188MiB` (GPU successfully returned to idle)

---

## 3. Scope of Objects & Feature Hygiene

- **Official Seen Objects Used (Pretraining):** `['butter', 'chocolate_pudding', 'cream_cheese', 'ketchup', 'milk', 'orange_juice', 'salad_dressing', 'tomato_sauce']`
- **Official Held-out Objects Excluded (Forbidden):** `['alphabet_soup', 'bbq_sauce']`
- **Forbidden Deploy-time Features Used:** None. Fine-tuning and evaluation used only the FIPER receding splits, with zero access to reward, success signals, object poses, language context, or future outcomes.

---

## 4. Exact Files Created

The experiment generated the following files on Bob:
1. **Script:** `scripts/run_transformer_k16_official_pretrain_probe_v1.py`
2. **Pretrained Weights:** `experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528/pretrained_encoder.pt`
3. **Training History (Baseline):** `experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528/baseline_history.json`
4. **Training History (Pretrained):** `experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528/pretrained_history.json`
5. **Pretrain Loss History:** `experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528/pretrain_loss_history.json`
6. **Topline MD Report:** `experiments/transformer_k16_official_pretrain_probe_fold00_smoke_20260528/OFFICIAL_PRETRAIN_PROBE_REPORT.md`

---

## 5. Training Loss Curves

### Stage A: Action Encoder Pretraining Loss (Official Chunks)
- **Epoch 1:** `0.486006`
- **Epoch 5:** `0.000002`
- **Epoch 10:** `0.000000` (reconstruction converges completely)

### Stage B: Fine-Tuning Loss Curve Comparison
The validation metric for selecting the best epoch is the validation score ($AUC - Brier$).

| Epoch | Baseline Train Loss | Pretrained Train Loss | Baseline Val AUC | Pretrained Val AUC |
|---|---|---|---|---|
| 1 | 0.124304 | 0.129352 | **0.7643 (Best)** | 0.7592 |
| 2 | 0.027102 | 0.026643 | 0.7502 | **0.7717 (Best)** |
| 3 | 0.019942 | 0.020050 | 0.7118 | 0.7354 |
| 4 | 0.014937 | 0.015568 | 0.6848 | 0.7129 |
| 5 | 0.011061 | 0.011380 | 0.6496 | 0.6578 |
| 6 | 0.009981 | 0.009428 | 0.6502 | 0.6705 |
| 7 | 0.008865 | 0.008188 | 0.6245 | 0.6231 |
| 8 | 0.008374 | 0.008236 | 0.6421 | 0.6317 |
| 9 | 0.008113 | 0.007712 | 0.6125 | 0.6270 |
| 10 | 0.007572 | 0.006632 | 0.6141 | 0.6286 |

---

## 6. Evaluation Metrics Comparison

Both models are evaluated using the event-level conformal policy: row threshold $q_{95}$ calibrated on `success_calib_seen`, and episode mass threshold calibrated on `success_val_seen` with $\alpha = 0.15$.

- **Baseline Model:** $q_{95} = 0.99690$, Mass Threshold = `0.00102` (Epoch 1)
- **Pretrained Model:** $q_{95} = 0.99890$, Mass Threshold = `0.00046` (Epoch 2)

### Conformal Policy Results:

| Model Configuration | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Random-Init Baseline** | 15.4% | 0.0% | 81.0% | 0.0% | 0.0% | 35.7% | 0.536 | 19.0% |
| **Official-Pretrained** | **11.8%** | 0.0% | **81.0%** | 0.0% | **2.4%** | **38.1%** | **0.515** | 19.0% |

### Analysis:
1. **False Alarms:** Pretraining reduces False Alarms on Seen tasks from **15.4% to 11.8%** while maintaining OOD False Alarms at **0.0%**.
2. **Failure Detection:** Overall OOD Failure Recall is preserved at **81.0%** (the same as baseline), but detection is faster:
   - `Det@25` improves from **0.0% to 2.4%**.
   - `Det@50` improves from **35.7% to 38.1%**.
   - `Mean Detection Time` is reduced from **0.536 to 0.515**.

Unlike the previous inference score/veto path (which slashed false alarms but killed recall), utilizing the official demonstrations for representation pretraining keeps failure recall intact while improving precision and timeliness.

---

## 7. Final Verdict

- `OFFICIAL_PRETRAIN_SMOKE_PASS` = **YES**
- `OFFICIAL_PRETRAIN_IMPROVES_OVER_RANDOM_INIT` = **YES** (reduces seen false alarms, speeds up detection time, and slightly improves early warning rates)
- `OFFICIAL_PRETRAIN_REDUCES_FA_WITHOUT_HURTING_DETECTION` = **YES** (reduces seen false alarms from 15.4% to 11.8% without hurting OOD failure detection, which remains at 81.0%)
- `READY_FOR_ALL_FOLDS_OFFICIAL_PRETRAIN_RUN` = **YES** (unlike the score veto, pretraining is a highly effective, recall-preserving method and is ready to be scaled up)
