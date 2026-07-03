# Internship Research & Implementation: Master Repository Guide

This document is the **authoritative single source of truth** for the "Generalized VLA and Failure Detection" project.

---

## 🌟 Project North Star: Generalized Reliability
Robotic Vision-Language-Action (VLA) models often fail silently. This project aims to bridge the gap between **high-performance VLA models** and **reliable robotic deployment** using temporal difference learning for failure prediction (**TDQC**).

---

## 🔬 Implementation Track: TDQC Phase 2
The **Temporal-Difference Quality Calibration (TDQC)** system is our primary deliverable.

### 1. Architectural Standards (22D Suite-Aware)
- **Features:** Always use the 22-dimensional feature set (11 uncertainty + 11 delta/temporal).
- **Embeddings:** **STRICTLY use `suite_id`**, not `task_id`. Task IDs are not unique across LIBERO suites and cause signal collision.
- **Suite Mapping (11 IDs):**
  - `libero_10_lan=0`, `libero_10_object=1`, `libero_10_swap=2`
  - `libero_goal_lan=3`, `libero_goal_swap=4`
  - `libero_object_lan=5`, `libero_object_object=6`, `libero_object_swap=7`
  - `libero_spatial_lan=8`, `libero_spatial_object=9`, `libero_spatial_swap=10`
- **Embedding Layer:** `nn.Embedding(11, hidden_dim)`

### 2. The "Capsule" Protocol
- **Isolation:** Each run gets a new `experiments/vX_expXX/` folder.
- **Independence:** Library code (`code/`) and evaluation scripts (`analysis/`) are copied into the capsule. Never import from global `core/`.
- **Reproducibility:** Training stats (mean/std) are computed from the training set and saved inside the checkpoint.

---

## 📊 Dataset Standards (v8 Balanced)
We have transitioned to a balanced training regime to solve the "Accuracy Paradox" (where models get high accuracy by simply guessing "Success").
- **Location:** `data/v8_balanced/`
- **Balance:** Exactly 50/50 success/failure split.
- **OOD Protocol:** Use `v8_unseen_obj_ood.pt`. It contains specific objects (Chocolate Pudding, Orange Juice) that never appear in training.
- **Metrics:** Report **Stepwise AUC-ROC** alongside Accuracy to detect model "blindness" in early steps.

---

## 🛠 Engineering Standards & Launch Commands

### Environment
- **Activation:** `source intern_ship_ws/activate_simvla.sh`
- **Standard Training Params:** 
  - LSTM: 2 layers, 256 hidden units.
  - Dropout: 0.05, Weight Decay: 0.01.
  - **Early Stopping:** Standardized at `patience=40`.

### Training Template
```bash
PYTHONNOUSERSITE=1 PYTHONPATH=experiments/<EXP>/code/ \
python3 -u experiments/<EXP>/code/phase2_tdqc/train_tdqc.py \
    --train_path data/v8_balanced/v8_train.pt \
    --val_path data/v8_balanced/v8_val.pt \
    --test_path data/v8_balanced/v8_test.pt \
    --output_dir experiments/<EXP>/runs/ \
    --epochs 500 --early_stop_patience 40
```

---

## 📈 Active Experiment Snapshot (Exp 08)
- **Concept:** Balanced Baseline.
- **Hypothesis:** Training on a 50/50 split will force the model to learn early-step failure cues, improving OOD Stepwise AUC.
- **Status:** **[RUNNING]** PID 53986. Converging at ~Epoch 10.
- **Next Step:** Run parallel evaluations on `v8_test.pt` and `v8_unseen_obj_ood.pt`.

---

## 📜 Historical Discoveries
- **v7_exp07:** Discovered that `task_id` collisions (ID 0-9 reused across suites) were crippling early training. Switching to `suite_id` reduced Brier loss by 50% and boosted OOD AUC to 0.91.
- **The Accuracy Paradox:** High accuracy (~85%) on imbalanced sets often hides an AUC < 0.5. Balanced datasets are mandatory for training diagnostic reliability.
