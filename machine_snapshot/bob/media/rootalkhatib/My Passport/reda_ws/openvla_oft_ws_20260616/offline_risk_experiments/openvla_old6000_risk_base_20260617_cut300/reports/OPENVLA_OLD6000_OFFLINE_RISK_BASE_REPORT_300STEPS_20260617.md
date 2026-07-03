# Offline Risk Model Evaluation Report (Truncated 300 Steps)

This report details the implementation, training, and evaluation results of the offline risk baseline models trained on the old 6000 episode dataset of the plain `libero_goal` suite, where all failed episodes were truncated at step 300.

---

## 1. Dataset & Splits Summary
* **Total Episode Count:** 6,009
* **Successful Episodes:** 5,828
* **Failed Episodes:** 181 (truncated at 300 steps max)

### Step-level Queries (Truncated)
* **Train Split Queries:** 63084
* **Val Split Queries:** 13476
* **Test Split Queries:** 13768

---

## 2. Evaluation Results

### Validation Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | 0.9979 | 0.9759 | 0.9877 | 0.9126 | 0.0066 | 0.0874 |

### Test Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | 0.9983 | 0.9847 | 0.9881 | 0.9333 | 0.0046 | 0.0845 |

---

## 3. Threshold Analysis
### SeqRiskModel Transformer Thresholds
* **Fixed 0.3:** Accuracy = 0.9489, F1 = 0.7808
* **Fixed 0.5:** Accuracy = 0.9709, F1 = 0.8607
* **Q90 Successes (0.1649):** Accuracy = 0.9213, F1 = 0.6982
* **Q95 Successes (0.3725):** Accuracy = 0.9580, F1 = 0.8123
* **Q99 Successes (0.7921):** Accuracy = 0.9872, F1 = 0.9300
* **Best F1 (0.8700):** Accuracy = 0.9881, F1 = 0.9333
