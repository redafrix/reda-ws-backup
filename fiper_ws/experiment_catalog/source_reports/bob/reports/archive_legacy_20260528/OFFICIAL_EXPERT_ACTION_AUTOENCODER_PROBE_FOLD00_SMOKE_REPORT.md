# Official LIBERO Expert Action Autoencoder Probe Fold 00 Smoke Report

This report summarizes the results of the Stage 9 / LIBERO-PRO / FIPER monitor experiment's GPU-based action-chunk autoencoder smoke test on `fold_00_holdout_alphabet_soup_bbq_sauce`.

## 1. Execution Setup & Exact Commands

### Target Machine & User
- **Host:** Bob (`pcrobot` / `PCROBOTUBUNTU02`) via SSH alias.
- **User:** `rootalkhatib`

### Exact Command Run
The following command was executed to run the GPU-based smoke test:
```bash
ssh pcrobot "cd '/media/rootalkhatib/My Passport/reda_ws/fiper_ws' && source ../asynchvla_ws/scripts/activate_simvla_bob.sh && python3 scripts/train_official_action_autoencoder_probe_v1.py --folds fold_00_holdout_alphabet_soup_bbq_sauce --max-rows-per-split 5000 --official-stride 5 --epochs 3 --output-dir experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528"
```

---

## 2. Process & GPU Status

### Process Status
No other campaign processes (`run_clean_temporal_nextgen_campaign_v2`, `run_nextgen_v2_full_all_splits`, or `probe_official`) were running before or after the smoke test.

### GPU Status Before Run
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
|=========================================+========================+===========|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |       N/A |
| N/A   44C    P0            590W /   80W |      15MiB /   8188MiB |     19%   |
+-----------------------------------------+------------------------+-----------+
```

### GPU Status After Run
The GPU successfully returned to idle:
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
|=========================================+========================+===========|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |       N/A |
| N/A   45C    P0            590W /   80W |      15MiB /   8188MiB |     19%   |
+-----------------------------------------+------------------------+-----------+
```

---

## 3. Scope of Objects & Feature Hygiene

- **Seen Objects Used (Training):** `['butter', 'chocolate_pudding', 'cream_cheese', 'ketchup', 'milk', 'orange_juice', 'salad_dressing', 'tomato_sauce']`
- **Held-out Objects Excluded (Forbidden):** `['alphabet_soup', 'bbq_sauce']` (strictly validated to prevent leakage)
- **Forbidden Deploy-time Features Used:** None. The model takes only the 10-step main action chunk (70 dimensions total), with no access to reward, success signals, object poses, language context, or future outcomes.

---

## 4. Exact Files Created

The experiment generated the following files in the workspace on Bob:
1. **Script:** `scripts/train_official_action_autoencoder_probe_v1.py`
2. **Results CSV:** `experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_results.csv`
3. **Results JSON:** `experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_results.json`
4. **Calibration JSON:** `experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/official_expert_action_autoencoder_calibration.json`
5. **Markdown Report:** `experiments/official_expert_action_autoencoder_probe_v1_fold00_smoke_20260528/OFFICIAL_EXPERT_ACTION_AUTOENCODER_PROBE_REPORT.md`

---

## 5. Fold 00 Smoke Metrics Table

Below are the detailed metrics computed on the 5,000 max rows per split for `fold_00`:

| Policy | Seen FA | OOD FA | OOD Failure Det | Det@10 | Det@25 | Det@50 | Mean Det Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `current_transformer_mass` | 15.4% | 25.6% | 95.2% | 0.0% | 26.2% | 85.7% | 0.332 | 4.8% |
| `official_autoencoder_mass` | 15.4% | 3.8% | 26.2% | 0.0% | 0.0% | 11.9% | 0.605 | 73.8% |
| `current_AND_official_autoencoder` | **3.7%** | **2.8%** | 26.2% | 0.0% | 9.5% | 26.2% | 0.314 | 73.8% |
| `current_OR_official_autoencoder` | 27.2% | 26.5% | 95.2% | 0.0% | 33.3% | 85.7% | 0.312 | 4.8% |

---

## 6. Honest Verdict

- **`OFFICIAL_ACTION_AE_SMOKE_PASS`:** **YES**
  - The script ran successfully end-to-end, trained the autoencoder on the GPU, calibrated thresholds properly, and produced all required files and metrics under 5,000 max rows.
- **`OFFICIAL_ACTION_AE_REDUCES_FA_WITHOUT_KILLING_DETECTION`:** **NO**
  - While using the autoencoder in an `AND` configuration successfully slashes False Alarms (OOD FA drops from 25.6% to 2.8%), it severely kills OOD Failure Detection (drops from 95.2% to 26.2%). Thus, the autoencoder model by itself is not sensitive enough to anomalous failure patterns to act as an effective safety veto without destroying monitor recall.
- **`READY_FOR_ALL_FOLDS_FULL_RUN`:** **NO**
  - Running a full campaign over all folds with this architecture is not recommended since the current formulation kills failure detection rates, matching the poor trade-off seen in the CPU Gaussian distance probe. Further architectural adjustments (e.g., conditioning on history or visual embeddings) are required before launching a full campaign.
