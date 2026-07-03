# Offline Risk Model Evaluation Report (Old 6000 Episodes)

This report details the implementation, training, and evaluation results of the offline risk baseline models trained on the old 6000 episode dataset of the plain `libero_goal` suite.

---

## 1. Dataset & Splits Summary
* **Dataset Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/openvla_goal_object_pro_risk_data_10000ep_round_robin_20260616_discarded`
* **Task Suite:** `libero_goal` (plain, not libero_goal_object)
* **Total Episode Count:** 6,009
* **Successful Episodes:** 5,828
* **Failed Episodes:** 181 (3.0% failure rate)

### Splits (Stratified, Task-Aware)
* **Train Split:** 4,197 episodes (12300 step failures / 70710 step-level queries)
* **Val Split:** 896 episodes (2500 step failures / 15026 step-level queries)
* **Test Split:** 916 episodes (3300 step failures / 15814 step-level queries)

---

## 2. Feature & Target Formulation
* **Feature Schema:**
  - One-hot Task ID (10 dimensions)
  - Normalized env timestep (1 dimension)
  - Robot Proprioception (8 dimensions)
  - Action Chunk Norm Statistics (6 dimensions: mean, std, min, max, l1_norm, l2_norm)
  - **Total Feature Dimensions ($x_t$):** 25
* **History ($K=16$ steps):** 
  - For the GRU/Transformer model, we stack a sequence of length 16 steps ($x_{t-15}, \dots, x_t$). Since queries are spaced by 8 execution steps, 16 queries span the last executed steps.
* **Target Label ($y_t$):** 
  - `episode_failure_label`: 1.0 if the episode ultimately failed, 0.0 if the episode succeeded.

---

## 3. Model Architectures & Training
* **Model A (SeqRiskModel Transformer):**
  - Architecture: Input (25) -> Linear (128) -> LayerNorm -> Transformer Encoder (3 layers, 4 attention heads) -> MLP -> Logits
  - Evaluates temporal sequences of past action-proprioception features.
* **Training Settings:**
  - Device: cuda:0
  - Loss Function: Weighted BCEWithLogitsLoss (positive class weight = 4.75)
  - Optimizer: AdamW (lr=1e-3, weight_decay=1e-4)
  - Epochs: 15 (with Early Stopping)

---

## 4. Evaluation Results

### Validation Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | 0.9986 | 0.9943 | 0.9884 | 0.9646 | 0.0034 | 0.0528 |

### Test Split Metrics
| Model | AUROC | AUPRC | Accuracy (Best Th) | F1 (Best Th) | FPR | FNR |
|---|---|---|---|---|---|---|
| **SeqRiskModel** | 0.9953 | 0.9908 | 0.9841 | 0.9609 | 0.0038 | 0.0618 |

---

## 5. Threshold Analysis
### SeqRiskModel Transformer Thresholds
* **Fixed 0.3:** Accuracy = 0.9712, F1 = 0.9343
* **Fixed 0.5:** Accuracy = 0.9807, F1 = 0.9539
* **Q90 Successes (0.0662):** Accuracy = 0.9229, F1 = 0.8430
* **Q95 Successes (0.1950):** Accuracy = 0.9607, F1 = 0.9128
* **Q99 Successes (0.5780):** Accuracy = 0.9822, F1 = 0.9573
* **Best F1 (0.7100):** Accuracy = 0.9841, F1 = 0.9609

---

## 6. Conclusions & Next Steps
- **Model Performance:** The SeqRiskModel Transformer achieves an AUROC of **0.9953** and AUPRC of **0.9908**.
- **Online Deploy Readiness:** This model generates standardizer weights (`normalization.json`), decision boundaries (`thresholds.json`), and PyTorch weights (`model.pt`) fully compatible with the `run_policy_matrix.py` deployment interface.
