# v7 Experiment 03 — No Task Embedding (Ablation of Idea 3)

**Ablation**: Removed task ID embedding vs exp01/exp02
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test
**Model**: 256/2L LSTM, MC loss, NO task embedding
**Hyperparams**: dropout=0.30, weight_decay=0.05, early_stop=40
**Best epoch**: 49
**Val Brier**: 0.044318 | **Test Brier**: 0.043929
**Test AUC-ROC**: 0.9971
**Stepwise acc @ step10, τ=0.5**: 75.1%
**Stepwise acc @ step20, τ=0.5**: 81.6%

**Comparison vs exp01 (with task embed)**:
- exp01: val=0.037176, test=0.038560, AUC=0.9967, step10=78.8%, step20=88.4%
- exp03: val=0.044318, test=0.043929, AUC=0.9971, step10=75.1%, step20=81.6%

**Conclusion**: Task embedding is **GENUINELY BENEFICIAL**. Removing it led to a ~19% increase in validation Brier and a significant drop in early prediction accuracy (e.g., -6.8% accuracy at step 20). The slight increase in AUC-ROC is negligible compared to the loss in calibration and predictive timing.
