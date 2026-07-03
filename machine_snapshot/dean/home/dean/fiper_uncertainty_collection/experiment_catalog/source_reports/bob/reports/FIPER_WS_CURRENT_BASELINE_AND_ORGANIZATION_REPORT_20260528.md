# FIPER Workspace Current Baseline and Organization Report (May 28, 2026)

This report documents the consolidation, validation, and layout organization of the `fiper_ws` workspace on Bob and Sam.

## 1. Executive Summary
The workspace has been organized around the chosen baseline model (`v2_018_transformer_k16`). Unrelated and legacy campaigns (totaling over 37GB of experimental output across 44 jobs) have been moved to `archive/` to keep active directories clean and efficient. Complete synchronization between the main machine (Bob) and the remote validation machine (Sam) was performed using a precise relative path rsync. All feature hygiene checks and script compilations pass successfully.

## 2. Active Process Status
No active training, cleanup, or sync processes are currently running on Bob or Sam:
- **Bob processes checked:** `rsync`, `run_clean_temporal`, `collect_fiper` (none active)
- **Sam processes checked:** `rsync`, `run_clean_temporal`, `collect_fiper` (none active)

## 3. Chosen Baseline Definition
- **Baseline Name:** `v2_018_transformer_k16`
- **History steps ($k$):** 16
- **Architecture:** Sequence Transformer
- **Width:** 128 | **Layers:** 3 | **Heads:** 4 | **Dropout:** 0.1
- **Inputs:** Action (stats), ACE, ACE history, Proprioception
- **Calibrated Policy:** Conformal mass trigger using $q_{95}$ row threshold (calibrated on `success_calib_seen`) and episode conformal mass calibration (calibrated on `success_val_seen` with $\alpha = 0.15$).

## 4. Why it Was Chosen
The `v2_018_transformer_k16` baseline offers a balanced trade-off between out-of-distribution (OOD) False Alarm rate and failure detection recall. It is robust, lightweight, and serves as a highly repeatable reproduction point across multiple holdout folds.

## 5. Current Baseline Metrics
- **Seen False Alarm (FA):** 15.4%
- **OOD False Alarm (FA):** 25.6%
- **OOD Failure Detection Recall:** 95.2%
- **Detection Rate @10% time:** 0.0%
- **Detection Rate @25% time:** 26.2%
- **Detection Rate @50% time:** 85.7%
- **Mean Detection Time (ratio of episode):** 0.332

## 6. Capacity/History Sweep Verdict
The capacity sweep evaluated models from size tiny ($W=64, L=2$) to large ($W=256, L=6$) and history steps 16 to 32. 
- **Verdict:** None of the swept models met the scaling decision rule (OOD FA < 25.6% while preserving recall $\ge$ 90.2% and Det@50 $\ge$ 80.7%). 
- **Reason:** While some smaller capacity models (like `cap_09_tiny_k32` with 28.0% OOD FA and 95.2% recall) approached baseline performance, they did not beat the baseline OOD FA. Larger capacity models (like `cap_04_large_k32`) exhibited severe early overfitting, peaking around epoch 1–2, and suffered from degraded OOD FA (up to 43.1%).
- **Decision:** Do not scale any swept configuration. Retain the `v2_018_transformer_k16` baseline.

## 7. Dynamic Threshold Verdict
The dynamic threshold policy sweep did not provide sufficient improvement over the static conformal mass policy to justify replacement.

## 8. Official LIBERO Expert Data Verdict
Using official expert demonstrations as pretraining data or as an inference score veto resulted in a critical reduction in failure detection capabilities. Hence, this path has been rejected, and official expert demos are not included in the active pipeline.

## 9. ACE Sampling Ablation Results
We evaluated different subsampling rates of the Action Chunking Error (ACE) inputs to determine if reducing the frequency of error audits regularizes the policy.
- **existing_real_v2_018:** Seen FA 15.4% | OOD FA 25.6% | Recall 95.2% | Det@25 26.2% | Det@50 85.7% | Mean Time 0.332
- **full8 every 2 steps:** Seen FA 14.0% | OOD FA 26.5% | Recall 92.9% | Det@25 19.0% | Det@50 83.3% | Mean Time 0.354
- **first4 every step:** Seen FA 15.4% | OOD FA 28.0% | Recall 95.2% | Det@25 31.0% | Det@50 90.5% | Mean Time 0.312
- **first4 every 2 steps:** Seen FA 14.0% | OOD FA 20.4% | Recall 95.2% | Det@25 14.3% | Det@50 81.0% | Mean Time 0.378
- **Verdict:** While `first4 every 2 steps` significantly lowers OOD FA (to 20.4%), it severely hurts early detection (Det@25 drops from 26.2% to 14.3%, and mean time increases to 0.378). Therefore, it does NOT replace the baseline at this stage.

## 10. Final Current Workspace Layout
- `configs/`: Contains sweep and ablation jsons.
- `current_baseline/`: Contains chosen baseline description and readme.
- `scripts/`: Clean and compiled orchestration/analysis scripts.
- `reports/`: Markdown logs, csv tables, and this consolidation summary.
- `data/manifests/`: Manifest metadata.
- `data/frozen/`: Raw and receding temporal samples (734,266 lines total).
- `experiments/`: Only current/canonical sweeps and ablations kept active.

## 11. What Was Archived
- **On Bob:** Moved full 44-job tree `clean_temporal_nextgen_v2_full_all_20260527` to `archive/legacy_experiments_20260528/clean_temporal_nextgen_v2_full_all_20260527`.
- **On Sam:** Moved any legacy duplicates and partial files to `archive/legacy_experiments_20260528/...` and `archive/rsync_root_duplicates_20260528/`.

## 12. Exact Files/Directories Kept Current
- `./current_baseline`
- `./configs`
- `./scripts`
- `./reports`
- `./data/manifests/fiper_sweep_eternal_20260527_combined`
- `./experiments/prepared_20260527`
- `./experiments/current_baseline_v2_018_20260528`
- `./experiments/transformer_k16_online_policy_sweep_20260528`
- `./experiments/transformer_k16_dynamic_threshold_policy_sweep_20260528`
- `./experiments/transformer_capacity_history_sweep_fold00_v1_20260528`
- `./experiments/transformer_capacity_history_small_sweep_fold00_v1_20260528`
- `./experiments/transformer_k16_ace_sampling_ablation_fold00_v1_20260528`

## 13. Exact Commands Run
- **Consolidation:** `bash scripts/organize_fiper_ws_current_baseline_20260528.sh`
- **Verification of line count:** `wc -l data/frozen/fiper_sweep_eternal_20260527_combined/*/fiper_receding_samples.jsonl`
- **Rsync Sync Bob -> Sam:** `rsync -a --relative --human-readable --info=stats2 ... sam:/home/rootalkhatib/test/reda_ws/fiper_ws/`
- **Py-compile:** `python3 -m py_compile scripts/run_clean_temporal_nextgen_campaign_v2.py scripts/analyze_ace_sampling_ablation_fold00_v1.py scripts/analyze_capacity_sweep_fold00_v1.py`

## 14. Validation Results
- **Compile status:** All scripts compile cleanly (Python 3.10.12).
- **Line count status:** Both Bob and Sam match `734266` total receding rows.
- **Feature hygiene status:** PASS. All audited ablation jobs enforce zero leakage (reward false, success false, visual object poses false, task metadata false, OOD training leakage false, future timesteps false).

## 15. Remaining Caveats
- Conformal calibration thresholds remain highly sensitive to validation data distribution.
- Temporal sequence models continue to overfit very early, indicating a strong need for better regularization or sequence architecture in future campaign iterations.

---

### Final Decision Fields
```
CURRENT_BASELINE = v2_018_transformer_k16
CURRENT_POLICY = score_q95_mass_conformal_alpha_0.15
ACE_SAMPLING_ABLATION_REPLACES_BASELINE = NO
WORKSPACE_SYNC_PASS = YES
READY_FOR_NEXT_EXPERIMENTS = YES
```
