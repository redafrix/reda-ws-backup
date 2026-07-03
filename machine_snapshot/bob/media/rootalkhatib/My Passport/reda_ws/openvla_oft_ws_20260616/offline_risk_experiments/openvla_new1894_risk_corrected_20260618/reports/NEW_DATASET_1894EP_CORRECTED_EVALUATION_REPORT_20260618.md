# Corrected Comparative Evaluation Report: New 1894-Episode Dataset

This corrected report compares the performance of the `SeqRiskModel` temporal Transformer risk model trained on the newly collected 1894-episode `libero_goal_object` dataset on Bob under two failure logging horizons: **800 steps max** (default) vs. **300 steps max** (truncated).

Correction relative to the previous Gemini report: all operating thresholds below are selected on the validation split, not the test split. Dataset counts are derived from the current JSONL files, not hard-coded.

---

## 1. Dataset & Split Stats
* **Total Collected Episodes:** 1894
* **Successful Episodes:** 789 (41.66%)
* **Failed Episodes:** 1105 (58.34%)
* **Train Split:** 1318 episodes
* **Val Split:** 277 episodes
* **Test Split:** 299 episodes (126 successful, 173 failed)
* **Threshold source:** validation split only
* **800-step val queries:** 1843 success / 16200 failure
* **300-step val queries:** 1843 success / 6156 failure

---

## 2. Step-Level Test Metrics Comparison

| Metric | 800-Step Model (Best F1 Th=0.4500) | 800-Step Model (Q95 Th=0.7861) | 300-Step Model (Best F1 Th=0.6200) | 300-Step Model (Q95 Th=0.7856) |
| :--- | :---: | :---: | :---: | :---: |
| **AUROC** | 0.9898 | 0.9898 | 0.9862 | 0.9862 |
| **AUPRC** | 0.9988 | 0.9988 | 0.9955 | 0.9955 |
| **F1-Score** | 0.9828 | 0.9745 | 0.9687 | 0.9607 |
| **Accuracy** | 0.9688 | 0.9548 | 0.9511 | 0.9401 |
| **Step FPR** | 0.2286 | 0.0792 | 0.1327 | 0.0713 |
| **Step FNR** | 0.0094 | 0.0414 | 0.0246 | 0.0566 |

---

## 3. Episode-Level Early Failure Detection Rates

Percentage of failed episodes in the test split (173 episodes) successfully flagged within early windows:

| Step Window | 800-Step Model (Best F1) | 800-Step Model (Q95) | 300-Step Model (Best F1) | 300-Step Model (Q95) |
| :--- | :---: | :---: | :---: | :---: |
| **First 10%** of execution | 98.27% | 98.27% | 96.53% | 90.17% |
| **First 25%** of execution | 100.00% | 100.00% | 98.84% | 97.11% |
| **First 50%** of execution | 100.00% | 100.00% | 100.00% | 100.00% |

---

## 4. Episode-Level False Alarm Rates (FPR)

Percentage of successful test episodes (126 episodes) triggering a false alarm at any step:

| Threshold Type | 800-Step Model False Alarm Rate | 300-Step Model False Alarm Rate |
| :--- | :---: | :---: |
| **Best F1** | 26.98% (34/126) | 26.98% (34/126) |
| **Q95** | 18.25% (23/126) | 19.84% (25/126) |
| **Q90** | 18.25% (23/126) | 26.98% (34/126) |

---

## 5. Validity Notes

* The original 20260618 report used test-set predictions to select `best_f1`, `q90`, and `q95` thresholds. This corrected run fixes that leakage.
* Splits are grouped by episode and non-overlapping, but they are not round-held-out. Future final runs should also test held-out rounds/seeds.
* Some tasks are nearly deterministic in this partial collection: tasks 2 and 9 have no successes, while tasks 5 and 7 have no failures. Task identity can therefore be a strong shortcut; ablations without task-id should be run before claiming the model learned transferable physical risk.
* `query_records.jsonl` can be joined to episodes by `(task_id, reset_seed)`, but `step_records.jsonl` lacks task/seed/episode identifiers. Future collection should add these identifiers to every step row.
