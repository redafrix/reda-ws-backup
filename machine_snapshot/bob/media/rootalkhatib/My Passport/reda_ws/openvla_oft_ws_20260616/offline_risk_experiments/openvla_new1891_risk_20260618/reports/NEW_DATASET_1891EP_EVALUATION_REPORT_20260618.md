# Comparative Evaluation Report: New 1,891-Episode Dataset

This report compares the performance of the `SeqRiskModel` temporal Transformer risk model trained on the newly collected 1,891-episode dataset on Bob under two failure logging horizons: **800 steps max** (default) vs. **300 steps max** (truncated).

---

## 1. Dataset & Split Stats
* **Total Collected Episodes:** 1,891
* **Successful Episodes:** 788 (41.67%)
* **Failed Episodes:** 1,103 (58.33%)
* **Train Split:** 1318 episodes
* **Val Split:** 277 episodes
* **Test Split:** 299 episodes (126 successful, 173 failed)

---

## 2. Step-Level Test Metrics Comparison

| Metric | 800-Step Model (Best F1 Th=0.3600) | 800-Step Model (Q95 Th=0.8298) | 300-Step Model (Best F1 Th=0.2500) | 300-Step Model (Q95 Th=0.8225) |
| :--- | :---: | :---: | :---: | :---: |
| **AUROC** | 0.9898 | 0.9898 | 0.9832 | 0.9832 |
| **AUPRC** | 0.9988 | 0.9988 | 0.9945 | 0.9945 |
| **F1-Score** | 0.9830 | 0.9696 | 0.9678 | 0.9441 |
| **Accuracy** | 0.9690 | 0.9466 | 0.9493 | 0.9168 |
| **Step FPR** | 0.2433 | 0.0503 | 0.1620 | 0.0503 |
| **Step FNR** | 0.0076 | 0.0537 | 0.0184 | 0.0928 |

---

## 3. Episode-Level Early Failure Detection Rates

Percentage of failed episodes in the test split (173 episodes) successfully flagged within early windows:

| Step Window | 800-Step Model (Best F1) | 800-Step Model (Q95) | 300-Step Model (Best F1) | 300-Step Model (Q95) |
| :--- | :---: | :---: | :---: | :---: |
| **First 10%** of execution | 98.27% | 97.69% | 97.69% | 86.13% |
| **First 25%** of execution | 100.00% | 100.00% | 98.84% | 98.84% |
| **First 50%** of execution | 100.00% | 100.00% | 100.00% | 98.84% |

---

## 4. Episode-Level False Alarm Rates (FPR)

Percentage of successful test episodes (126 episodes) triggering a false alarm at any step:

| Threshold Type | 800-Step Model False Alarm Rate | 300-Step Model False Alarm Rate |
| :--- | :---: | :---: |
| **Best F1** | 27.78% (35/126) | 26.98% (34/126) |
| **Q95** | 15.87% (20/126) | 14.29% (18/126) |
| **Q90** | 18.25% (23/126) | 15.87% (20/126) |
