# Phase 2: TDQC LSTM Calibrator (Standalone)

This directory is the finalized, consolidated environment for the **Failure Probability Estimator**. It allows the robot to predict, in real-time, the likelihood that a current rollout will eventually fail.

## 📈 Final Performance (1,600 Epochs)
- **Global Brier Score:** **0.0823** (Baseline Guessing: 0.207)
- **Step 100 Brier (Proactive):** **0.1041**
- **Step 50 Brier (Ultra-Early):** **0.1284**
- **Trajectory Accuracy (Step 50):** **81.27%**

## 🧠 Model Architecture
- **Type:** LSTM (Recurrent Neural Network).
- **Layers:** 1.
- **Hidden Units:** 128.
- **Input Features (8D):** 
  - `[Weighted Path Mean, Weighted Last Mean, First Path Mean, First Last Mean, Max Path, Max Last, Gripper Path, Gripper Last]`
  - These features are derived from the SimVLA attention maps and variance.

## 📂 Folder Structure
- **`code/`**: Training and loss logic (`tdqc_losses.py`, `train_tdqc.py`).
- **`data/`**: `final_calibrated_3751rollouts.pt` (70/15/15 split, Seed 0).
- **`results/checkpoints/`**: 
  - `lstm_td0_final_polish_v2/best.pt`: **The Golden Checkpoint.**
- **`results/plots/`**: Visual evidence of proactive signal separation.
- **`scripts/`**: Horizon-based evaluation scripts.

## 🚦 Operational Constraints (For Future Sessions)
1.  **Normalization:** You **MUST** use the `mean` and `std` tensors stored inside the `best.pt` checkpoint. Do not re-calculate them.
2.  **Dataset Split:** Always use **Seed 0** for `random_split` to prevent training/testing data leakage.
3.  **Threshold:** The optimal failure-trigger threshold is currently **0.5**. At Step 50, this yields >81% accuracy.

## 🚀 How to Evaluate
```bash
export PYTHONPATH=$PWD/code
# Evaluate the 5s horizon
python3 scripts/eval_50_steps.py \
    --ckpt_path results/checkpoints/lstm_td0_final_polish_v2/best.pt \
    --dataset_path data/final_calibrated_3751rollouts.pt
```
