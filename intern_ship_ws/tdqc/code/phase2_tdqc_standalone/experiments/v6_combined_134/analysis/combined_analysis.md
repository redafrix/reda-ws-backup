# TDQC Combined Experiment Analysis

This document compares the results of two combined TDQC architectures designed to improve manipulation failure prediction using GPU-accelerated training.

## Goal
Achieve a validation Brier score below **0.100** using exclusively `final_calibrated_3924rollouts_v6.pt` (8D features) on an RTX 4060 GPU.

## Experiment Configurations

| Feature | Experiment A (Idea 1+4) | Experiment B (Idea 1+3+4) |
| :--- | :--- | :--- |
| **Architecture** | 256 Hidden / 2L LSTM | 256 Hidden / 2L LSTM + **20-dim Task Embedding** |
| **Loss Function** | MC Target (Propagated terminal label) | MC Target (Propagated terminal label) |
| **Epochs** | 1000 | 1888 (Stopped early due to deterioration) |
| **Task Aware?** | No | Yes (via embedding sum) |

## Results Summary (Fixed Test Split)

| Metric | Experiment A (Idea 1+4) | Experiment B (Idea 1+3+4) | % Improvement |
| :--- | :--- | :--- | :--- |
| **Best Val Brier** | 0.1019 | **0.0899** | +11.8% |
| **Final Test Brier** | 0.0985 | **0.0932** | +5.4% |
| **Full Dataset Brier** | 0.0629 | **0.0620** | +1.4% |
| **Episode ROC-AUC** | **0.9971** | 0.9951 | -0.2% |

## Key Insights

1. **Synergy of MC Loss and Capacity**: Both experiments successfully broke the 0.100 barrier on the test set. For comparison, Idea 4 alone (Capacity) achieved 0.1103 and Idea 1 alone (MC) achieved 0.1172. Combining them brought scores down significantly.
2. **Impact of Task Embeddings**: Experiment B reached a record-low validation Brier of **0.0899** at epoch 120. While it showed signs of overfitting later in training (deteriorating to ~0.099), its best generalization point is superior to Experiment A.
3. **Training Dynamics**:
    - **Experiment A** showed stable convergence over 1000 epochs.
    - **Experiment B** converged very rapidly to its best generalization state but became unstable after epoch 500, likely due to the task embeddings allowing the model to "memorize" failure patterns for specific tasks too aggressively.
4. **Conclusion**: **Experiment B (Idea 1+3+4)** is the recommended architecture for the final TDQC deployment. It provides the best failure probability calibration (lowest Brier) while maintaining near-perfect failure detection (ROC-AUC > 0.99).

## Visuals
- [Experiment A Curves](combined_idea14/runs/combined_idea14/learning_curve.png)
- [Experiment B Curves](combined_idea134/runs/combined_idea134/training_curves.png)
