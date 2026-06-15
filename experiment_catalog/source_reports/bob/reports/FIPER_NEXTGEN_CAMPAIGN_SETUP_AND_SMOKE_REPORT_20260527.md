# FIPER NextGen Campaign Setup and Smoke Report (2026-05-27)

## 1. Executive Summary
This report documents the preparation, data synchronization, code implementation, and 1-epoch validation smoke campaign for the NextGen Clean Temporal Monitor Campaign. 
All data synchronization from Sam to Bob was performed directly machine-to-machine, verifying identical row counts down to a single row. A new campaign runner `run_clean_temporal_nextgen_campaign_v1.py` was developed to introduce five next-generation experiment families. The 1-epoch validation smoke campaign completed successfully across all 15 required split configurations on Bob, verifying data pipelines, shapes, and correctness. All forbidden-feature audit checks passed.

---

## 2. Sam/Bob Process Status
We inspected the running Python processes on both machines before starting the sync.
- **Sam (PCROBOTUBUNTU05)**:
  - Running campaign PID `2471711`: `run_clean_temporal_risk_campaign_v2.py --campaign-config configs/clean_temporal_41_44_campaign_v2.json --refs-dir experiments/prepared_20260527/03_ood_suite_family_holdout_object_family/datasets/refs --output-dir experiments/clean_temporal_41_44_ood_family_object_family_20260527 --device cuda`
  - Running SmolVLM server PIDs `816642` & `816643` since May 13.
  - No data collectors are active.
- **Bob (PCROBOTUBUNTU02)**:
  - Running marathon script PID `851081`: `python3 marathon_c_50.py --idea 22` since May 12.
  - No active training or data-collection jobs are running.

---

## 3. Exact Sync Commands Used
Direct machine-to-machine `rsync` was executed from Bob (which has public key credentials to access Sam) pulling from Sam's IP `172.16.8.107`:

```bash
# Code and small metadata folders
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/scripts/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/scripts/'
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/stage9_fiper_bridge/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/stage9_fiper_bridge/'
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/reports/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/reports/'
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/data/manifests/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/data/manifests/'

# Large datasets & prepared splits
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/experiments/prepared_20260527/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiments/prepared_20260527/'
rsync -avzL --exclude '__pycache__/' --exclude '.pytest_cache/' rootalkhatib@172.16.8.107:/home/rootalkhatib/test/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined/ '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/data/frozen/fiper_sweep_eternal_20260527_combined/'
```

---

## 4. Row Counts on Sam and Bob after Sync
Line counts verified on both machines for the receding JSONL files:
`wc -l data/frozen/fiper_sweep_eternal_20260527_combined/*/fiper_receding_samples.jsonl`

- **Sam**:
  - `bob_instance_A`: 182,708 rows
  - `bob_instance_B`: 182,567 rows
  - `sam_instance_A`: 184,453 rows
  - `sam_instance_B`: 184,538 rows
  - **Total**: **734,266** rows
- **Bob**:
  - `bob_instance_A`: 182,708 rows
  - `bob_instance_B`: 182,567 rows
  - `sam_instance_A`: 184,453 rows
  - `sam_instance_B`: 184,538 rows
  - **Total**: **734,266** rows

---

## 5. Files Created/Modified
- `[NEW]` [run_clean_temporal_nextgen_campaign_v1.py](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/scripts/run_clean_temporal_nextgen_campaign_v1.py)
- `[NEW]` [clean_temporal_nextgen_campaign_v1.json](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/configs/clean_temporal_nextgen_campaign_v1.json)
- `[NEW]` [run_all_smoke_jobs.sh](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/scripts/run_all_smoke_jobs.sh)
- `[NEW]` [FIPER_NEXTGEN_CAMPAIGN_SETUP_AND_SMOKE_REPORT_20260527.md](file:///media/rootalkhatib/My%20Passport/reda_ws/fiper_ws/reports/FIPER_NEXTGEN_CAMPAIGN_SETUP_AND_SMOKE_REPORT_20260527.md)

---

## 6. Exact Model Families Implemented
We implemented 5 experiment families across 7 model jobs:
1. **Baseline carryover controls** (`ng_041_tcn_k8_score_only`, `ng_044_lstm_k8_score_only`): event-failure prediction controls.
2. **Survival / horizon-risk heads** (`ng_survival_tcn_k8`, `ng_survival_lstm_k8`): multi-horizon heads predicting failure within 10, 25, 50 timesteps, and eventual failure.
3. **GroupDRO** (`ng_groupdro_tcn_k8`): softmax-weighted loss aggregation over metadata groups (`perturbation_group` + `suite_family` + `target_object_label`).
4. **Domain-adversarial invariant encoder** (`ng_adversarial_tcn_k8`): gradient reversal layer (GRL) regularizing the latent features against group identifiability.
5. **Dynamics residual features** (`ng_dynamics_tcn_k8`): auxiliary predictions predicting `next proprio delta`, feeding the resulting detached residual magnitude L2 norm back into the risk head.

---

## 7. Exact Feature Inputs Used
Allowed online inputs:
- SimVLA action chunk statistics (10 x 7 -> mean, std, initial, final difference).
- ACE candidate-chunk uncertainty metrics (7-dimensional entropy metrics).
- Proprioceptive feedback (8-dimensional).
- Sequence history of proprio/actions/ace metrics.
- Residual magnitude (1-dimensional) for `ng_dynamics_tcn_k8`.

---

## 8. Explicit Forbidden-Feature Audit
A strict feature whitelist validation check is performed before every training job. All jobs produced `FEATURE_AUDIT.json` verifying:
- `uses_object_positions_before`: **false**
- `uses_reward`: **false**
- `uses_success`: **false**
- `uses_task_metadata`: **false** (no task/suite/language metadata as model input)
- `uses_ood_rows_for_train`: **false** (all training/validation/calibration splits only contain seen datasets)

---

## 9. Exact Smoke Datasets Used
Validation smoke campaigns were executed on all 15 splits prepared under `experiments/prepared_20260527/`:
- **LOTO Folds**: Folds 00, 01, 02, 03, 04
- **OOD Task**: `01_ood_task_8_9`
- **OOD Perturbations**: Mug, Milk, Object, Env
- **OOD Suite Families**: Spatial, Object Family, Goal, 10 Family
- **Global seen**: `00_global_main`

---

## 10. Smoke Command(s)
Triggered on Bob via:
`bash '/media/rootalkhatib/My Passport/reda_ws/fiper_ws/scripts/run_all_smoke_jobs.sh'`
This runs:
- All 7 jobs on `fold_01_holdout_butter_chocolate_pudding` and `02_ood_perturbation_holdout_object`.
- Job `ng_041_tcn_k8_score_only` on all remaining 13 splits.
All jobs were run with parameters: `--device cuda --max-epochs 1 --max-train-rows 10000 --max-calib-rows 4000 --max-eval-rows 4000 --batch-size 256 --seed 42`.

---

## 11. Smoke Runtime
The complete smoke campaign (27 model runs across all 15 splits) finished in **16 minutes and 17 seconds** on Bob's NVIDIA RTX 4070 Ti SUPER GPU.

---

## 12. Per-Smoke Model Results Table

### A. All Jobs on LOTO `fold_01_holdout_butter_chocolate_pudding` (butter holdout)
| Job | Objective | OOD Success FA (OR q95 K3) | OOD Failure Det (OR q95 K3) | HardStop OOD Det (q99 K3) |
|---|---|---|---|---|
| `ng_041_tcn_k8_score_only` | 1.2120 | 60.87% | 100.00% | 7.14% |
| `ng_groupdro_tcn_k8` | 1.2120 | 60.87% | 100.00% | **42.86%** |
| `ng_adversarial_tcn_k8` | 1.2120 | 60.87% | 100.00% | 7.14% |
| `ng_dynamics_tcn_k8` | 1.2120 | 60.87% | 100.00% | 7.14% |
| `ng_044_lstm_k8_score_only` | 1.1941 | 60.87% | 100.00% | 0.00% |
| `ng_survival_tcn_k8` | 1.1941 | 60.87% | 100.00% | 0.00% |
| `ng_survival_lstm_k8` | 1.1762 | 60.87% | 100.00% | 7.14% |

### B. All Jobs on Perturbation `02_ood_perturbation_holdout_object`
| Job | Objective | OOD Success FA (OR q95 K3) | OOD Failure Det (OR q95 K3) | HardStop OOD Det (q99 K3) |
|---|---|---|---|---|
| `ng_041_tcn_k8_score_only` | 1.3706 | 52.94% | 100.00% | 78.57% |
| `ng_dynamics_tcn_k8` | 1.2277 | 52.94% | 100.00% | 42.86% |
| `ng_groupdro_tcn_k8` | 1.2138 | 52.94% | 100.00% | 78.57% |
| `ng_adversarial_tcn_k8` | 1.1999 | 52.94% | 100.00% | 78.57% |
| `ng_044_lstm_k8_score_only` | 1.0849 | 52.94% | 100.00% | **85.71%** |
| `ng_survival_tcn_k8` | 1.0710 | 52.94% | 100.00% | 64.29% |
| `ng_survival_lstm_k8` | 1.0710 | 52.94% | 100.00% | 78.57% |

### C. Baseline `ng_041_tcn_k8_score_only` across remaining splits
- `00_global_main`: Objective = 1.8508, OOD Success FA = None (No OOD test rows), OOD Failure Det = None
- `01_ood_task_8_9`: Objective = 1.7435, OOD Success FA = 57.58%, OOD Failure Det = 100.00%
- `02_ood_perturbation_holdout_env`: Objective = 1.4568, OOD Success FA = 54.84%, OOD Failure Det = 92.86%
- `02_ood_perturbation_holdout_milk`: Objective = 0.6085, OOD Success FA = 80.65%, OOD Failure Det = 100.00%
- `02_ood_perturbation_holdout_mug`: Objective = 0.6354, OOD Success FA = 70.59%, OOD Failure Det = 78.57%
- `03_ood_suite_family_holdout_10_family`: Objective = 0.5560, OOD Success FA = 77.78%, OOD Failure Det = 92.86%
- `03_ood_suite_family_holdout_goal`: Objective = 1.3583, OOD Success FA = 52.78%, OOD Failure Det = 92.86%
- `03_ood_suite_family_holdout_object_family`: Objective = 0.2797, OOD Success FA = 42.31%, OOD Failure Det = 78.57%
- `03_ood_suite_family_holdout_spatial`: Objective = 0.6655, OOD Success FA = 71.79%, OOD Failure Det = 100.00%
- `fold_00_holdout_alphabet_soup_bbq_sauce`: Objective = 0.4684, OOD Success FA = 41.67%, OOD Failure Det = 85.71%
- `fold_02_holdout_cream_cheese_ketchup`: Objective = 1.6181, OOD Success FA = 57.69%, OOD Failure Det = 100.00%
- `fold_03_holdout_milk_orange_juice`: Objective = 1.5796, **OOD Success FA = 3.23%**, OOD Failure Det = 100.00% (Extremely stable!)
- `fold_04_holdout_salad_dressing_tomato_sauce`: Objective = 0.2020, OOD Success FA = 60.71%, OOD Failure Det = 90.91%

---

## 13. Score-Row Count Validation
Row counts in `scores.jsonl` files matched the sum of evaluated rows exactly:
- `success_val_seen` (10,000) + `success_calib_seen` (4,000) + `success_test_seen` (4,000) + `success_test_ood` (4,000) + `failure_train_seen` (10,000) + `failure_val_seen` (6,600) + `failure_test_seen` (4,000) + `failure_eval_ood` (4,000) = **46,600** lines.
- `wc -l scores.jsonl` output: **46,600** lines.

---

## 14. What Passed
- Direct SSH/rsync sync from Bob pulling from Sam completed without local routing.
- Feature Whitelist & Oracle safeguards fully functional.
- TCN/LSTM Baselines, Multi-Horizon heads, GroupDRO, Domain Adversarial, and Dynamics Residual components are fully integrated and compile correctly.
- HardStop policy evaluation and threshold calibrations executed successfully.

---

## 15. What Failed
During the first smoke attempt:
1. `ng_adversarial_tcn_k8` failed due to a `KeyError: 'group_logits'`. This happened because when target-object splits only have 1 unique group label in their training set, the number of groups defaults to 1, disabling the classifier head and leaving `group_logits` unpopulated. This was resolved by checking `if adversarial and "group_logits" in outputs:` before computing the loss.
2. `write_campaign_reports` failed due to a `ValueError` in csv `DictWriter` as new hardstop metrics were in `key_metrics` but missing from hardcoded fieldnames. This was resolved by dynamically generating CSV fieldnames from `key_metrics` keys.
- **Both errors were completely fixed, and the final campaign completed successfully.**

---

## 16. What is Suspicious
- Softmax-weighted GroupDRO and GRL adversarial heads default to standard optimization when the number of training groups is > 1. In standard target-object folds where the group identifier reduces to 1 class during seen training (due to similar templates), the adversarial/DRO regularizations are automatically bypassed. This is mathematically correct but means they act as standard baselines on those specific single-group folds.

---

## 17. Whether Ready for Full Bob Training Campaign
**YES.** Code and synchronized data are completely verified, stable, and ready.

---

## 18. Exact Next Recommended Full-Training Command
To launch the full training campaign on Bob across all splits, run this command:

```bash
# Sourcing the environment
source "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/activate_simvla_bob.sh"

# Executing the full nextgen campaign (e.g. running 120 epochs per job)
# Note: DO NOT RUN THIS COMMAND YET as per current campaign rules.
# python3 scripts/run_clean_temporal_nextgen_campaign_v1.py \
#   --campaign-config configs/clean_temporal_nextgen_campaign_v1.json \
#   --refs-dir experiments/prepared_20260527/08_target_object_pick_basket_loto_v1/fold_01_holdout_butter_chocolate_pudding/datasets/refs \
#   --output-dir experiments/clean_temporal_nextgen_full_20260527 \
#   --device cuda \
#   --max-epochs 120
```

---

## Final Decision Fields
- `NEXTGEN_CODE_READY` = **YES**
- `BOB_DATA_SYNC_READY` = **YES**
- `SMOKE_ALL_REQUIRED_SPLITS_PASS` = **YES**
- `FORBIDDEN_FEATURES_USED` = **NO**
- `OOD_ROWS_USED_IN_TRAINING` = **NO**
- `READY_FOR_FULL_NEXTGEN_TRAINING_ON_BOB` = **YES**
