# Final Comparative Evaluation Report: OpenVLA Goal-Object 1890-Episode Dataset

This corrected report compares the performance of the `SeqRiskModel` temporal Transformer risk model trained on the cleaned final 1890-episode `libero_goal_object` dataset on Bob under two failure logging horizons: **800 steps max** (default) vs. **300 steps max** (truncated).

All operating thresholds below are selected on the validation split, not the test split. This run uses the frozen complete-round dataset with reset seeds 100000..100188.

---

## 1. Dataset & Split Stats
* **Total Collected Episodes:** 1890
* **Successful Episodes:** 787 (41.64%)
* **Failed Episodes:** 1103 (58.36%)
* **Train Split:** 1314 episodes
* **Val Split:** 277 episodes
* **Test Split:** 299 episodes (126 successful, 173 failed)
* **Threshold source:** validation split only
* **800-step val queries:** 1778 success / 16200 failure
* **300-step val queries:** 1778 success / 6156 failure

---

## 2. Step-Level Test Metrics Comparison

| Metric | 800-Step Model (Best F1 Th=0.6000) | 800-Step Model (Q95 Th=0.8152) | 300-Step Model (Best F1 Th=0.4900) | 300-Step Model (Q95 Th=0.8049) |
| :--- | :---: | :---: | :---: | :---: |
| **AUROC** | 0.9893 | 0.9893 | 0.9852 | 0.9852 |
| **AUPRC** | 0.9988 | 0.9988 | 0.9952 | 0.9952 |
| **F1-Score** | 0.9831 | 0.9710 | 0.9681 | 0.9542 |
| **Accuracy** | 0.9693 | 0.9487 | 0.9499 | 0.9308 |
| **Step FPR** | 0.2306 | 0.0735 | 0.1481 | 0.0635 |
| **Step FNR** | 0.0089 | 0.0488 | 0.0219 | 0.0709 |

---

## 3. Episode-Level Early Failure Detection Rates

Percentage of failed episodes in the test split (173 episodes) successfully flagged within early windows:

| Step Window | 800-Step Model (Best F1) | 800-Step Model (Q95) | 300-Step Model (Best F1) | 300-Step Model (Q95) |
| :--- | :---: | :---: | :---: | :---: |
| **First 10%** of execution | 98.27% | 97.69% | 98.27% | 94.22% |
| **First 25%** of execution | 100.00% | 99.42% | 98.27% | 98.27% |
| **First 50%** of execution | 100.00% | 100.00% | 100.00% | 98.84% |

---

## 4. Episode-Level False Alarm Rates (FPR)

Percentage of successful test episodes (126 episodes) triggering a false alarm at any step:

| Threshold Type | 800-Step Model False Alarm Rate | 300-Step Model False Alarm Rate |
| :--- | :---: | :---: |
| **Best F1** | 30.95% (39/126) | 26.98% (34/126) |
| **Q95** | 19.84% (25/126) | 20.63% (26/126) |
| **Q90** | 21.43% (27/126) | 24.60% (31/126) |

---

## 5. Validity Notes

* The original 20260618 report used test-set predictions to select `best_f1`, `q90`, and `q95` thresholds. This corrected run fixes that leakage.
* Splits are grouped by episode and non-overlapping, but they are not round-held-out. Future final runs should also test held-out rounds/seeds.
* Some tasks are nearly deterministic in this partial collection: tasks 2 and 9 have no successes, while tasks 5 and 7 have no failures. Task identity can therefore be a strong shortcut; ablations without task-id should be run before claiming the model learned transferable physical risk.
* Final cleaned query and step records now include `episode_index_global`, `task_id`, `reset_seed`, `round_index`, and task metadata. The raw interrupted source lacked these identifiers on step rows, but the frozen final dataset fixes that.
