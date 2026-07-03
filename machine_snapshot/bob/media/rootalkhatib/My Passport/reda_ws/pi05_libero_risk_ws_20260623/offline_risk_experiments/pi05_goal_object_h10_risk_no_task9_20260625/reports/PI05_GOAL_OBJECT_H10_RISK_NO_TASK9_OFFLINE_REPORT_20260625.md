# Pi0.5 Goal-Object H10 Risk Model Offline Report (Task 9 Excluded)

This report evaluates the temporal sequence risk model (`SeqRiskModel`) trained offline on the frozen Pi0.5 complete-round dataset with invalid task 9 excluded on Bob (`PCROBOTUBUNTU02`).

Task 9 (`put the wine bottle on the rack`) is excluded because audit on 2026-06-25 showed the rack target was invalid/non-visible in the collected videos and all 409 episodes timed out. The MuJoCo target site existed only as a tiny `wine_rack_stand_1_top_region` marker, unlike the valid OOD rack tasks.

The model uses historical actions, proprioception, and active camera correlation entropy (ACE) to predict step-level risk labels. All calibration thresholds are calculated strictly on the validation split.

---

## 1. Dataset & Split Stats
* **Total Clean Frozen Episodes (Task 9 Excluded):** 3681
* **Successful Episodes:** 3298
* **Failed Episodes:** 383
* **Train Split:** 2568 episodes
* **Val Split:** 545 episodes
* **Test Split:** 568 episodes (503 success, 65 fail)

---

## 2. Step-Level Test Metrics (Best F1 Val Threshold)
* **AUROC:** 0.9065
* **AUPRC:** 0.8942
* **F1-Score:** 0.8046
* **Step FPR:** 0.1339
* **Step FNR:** 0.2084

---

## 3. Episode-Level Test Evaluation Table

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1  |  29.62% |    98.46% |  66.2% |  93.8% |  98.5% | 0.106 |   1.5% |
| q90          |  27.63% |    98.46% |  64.6% |  92.3% |  98.5% | 0.112 |   1.5% |
| q95          |  12.33% |    98.46% |  35.4% |  78.5% |  96.9% | 0.165 |   1.5% |
| q99          |   3.58% |    95.38% |   3.1% |  41.5% |  73.8% | 0.346 |   4.6% |
| q95_K3       |   9.94% |    98.46% |  33.8% |  78.5% |  95.4% | 0.168 |   1.5% |
| q99_K3       |   3.18% |    92.31% |   3.1% |  38.5% |  70.8% | 0.348 |   7.7% |
| q95_mass_1   |   7.36% |    96.92% |   9.2% |  66.2% |  90.8% | 0.219 |   3.1% |
| q95_mass_5   |   3.98% |    95.38% |   0.0% |  47.7% |  80.0% | 0.317 |   4.6% |
| q95_mass_10  |   2.19% |    95.38% |   0.0% |  29.2% |  73.8% | 0.379 |   4.6% |
| q95_mass_20  |   1.79% |    92.31% |   0.0% |  12.3% |  63.1% | 0.454 |   7.7% |
| q95_mass_50  |   0.20% |    80.00% |   0.0% |   0.0% |  20.0% | 0.622 |  20.0% |


---

## 4. Conformal Score Thresholds
* **Best F1 Threshold:** 0.5500
* **Q90 Score Threshold:** 0.5642
* **Q95 Score Threshold:** 0.7782
* **Q99 Score Threshold:** 0.9651

---

## 5. Security & Anticheating Verification
* **No explicit task id input:** Verified. Feature dimensionality does not contain task identifiers.
* **No explicit timestep input:** Verified. Timestep indexes are excluded from inputs.
* **Non-overlapping grouped split:** Verified. Episodes are split grouped by episode ID to prevent row leakage.
* **Normalization on train split only:** Verified. Standardizer statistics computed strictly from the train split.
* **Thresholds calibrated on val split only:** Verified. Thresholds chosen using validation success queries.
* **Pi0.5 candidate ACE is real:** Verified. ACE computed from flow noise samples.
* **Uncertainty TopK8 masked:** Verified. Logged values are zeros as Pi0.5 has no internal TopK uncertainty.
* **Invalid task exclusion:** Verified. Task 9 is excluded from training, validation, testing, normalization, and threshold calibration.
