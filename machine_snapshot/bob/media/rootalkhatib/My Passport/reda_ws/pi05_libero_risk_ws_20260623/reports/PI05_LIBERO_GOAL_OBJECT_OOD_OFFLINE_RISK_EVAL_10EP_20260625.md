# Pi0.5 Offline OOD Detector Evaluation Report
    
This report evaluates the OOD generalization of the trained Pi0.5 H10 risk head evaluated strictly on the clean `pi05_basic_h10` online OOD dataset (which reflects natural Pi0.5 behaviour without risk intervention).

* **Dataset source:** `policy_pi05_basic_h10` query records
* **Total episodes:** 180
* **Risk Model Checkpoint:** `pi05_goal_object_h10_risk_20260625`

---

## 1. Step-Level Classification Metrics
* **Step AUROC:** 0.5593
* **Step AUPRC:** 0.1975
* **Step F1:** 0.2349
* **Step FPR:** 0.9946
* **Step FNR:** 0.0187

---

## 2. Episode-Level Early Detection Table

| Policy | Success FA | Failure Det | Det@10 | Det@25 | Det@50 | Mean Time | Never |
|---|---:|---:|---:|---:|---:|---:|---:|
| best_val_f1  | 100.00% |   100.00% | 100.0% | 100.0% | 100.0% | 0.013 |   0.0% |
| q90          | 100.00% |   100.00% | 100.0% | 100.0% | 100.0% | 0.013 |   0.0% |
| q95          | 100.00% |   100.00% | 100.0% | 100.0% | 100.0% | 0.013 |   0.0% |
| q99          |  27.27% |    50.00% |  25.0% |  25.0% |  50.0% | 0.188 |  50.0% |
| q95_K3       |  94.32% |   100.00% |  75.0% | 100.0% | 100.0% | 0.047 |   0.0% |
| q99_K3       |  19.32% |    50.00% |  25.0% |  25.0% |  25.0% | 0.375 |  50.0% |
| q95_mass_1   |  38.64% |   100.00% |  25.0% |  50.0% |  75.0% | 0.281 |   0.0% |
| q95_mass_5   |   0.00% |    50.00% |   0.0% |  25.0% |  50.0% | 0.356 |  50.0% |
| q95_mass_10  |   0.00% |    50.00% |   0.0% |   0.0% |  25.0% | 0.613 |  50.0% |
| q95_mass_20  |   0.00% |    25.00% |   0.0% |   0.0% |   0.0% | 0.912 |  75.0% |
| q95_mass_50  |   0.00% |     0.00% |   0.0% |   0.0% |   0.0% | 1.000 | 100.0% |


---

## 3. Operating Point Recommendation
We select `q95_mass_10` as our official operating point:
* **Success False Alarm Rate:** 0.00%
* **Failure Detection Rate:** 50.00%
* **Never Detected Rate:** 50.00%
* **Mean Detection Fraction:** 0.613

This is a mixed OOD result: `q95_mass_10` preserves zero success false alarms on this 180-episode official OOD set, but detects only 50.00% of the four failures and detects them late. The raw q95/q90 thresholds detect all failures but false-alarm on all successful episodes. Therefore this Pi0.5 risk head is not cleanly calibrated for this OOD suite under the current operating point.
