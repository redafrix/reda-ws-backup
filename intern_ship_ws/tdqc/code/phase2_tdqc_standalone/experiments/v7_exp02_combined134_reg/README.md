# v7 Experiment 02 — Combined Ideas 1+3+4 (regularized)

**Ideas combined**: MC loss (1) + Task embedding (3) + 256/2L LSTM (4)
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test episodes
**Hyperparams**: dropout=0.30, weight_decay=0.05, early_stop_patience=40
**Best epoch**: 85
**Val Brier**: 0.037634 | **Test Brier**: 0.039086
**Test AUC-ROC**: 0.9971
**Stepwise acc @ step10, τ=0.5**: 79.1%
**Stepwise acc @ step20, τ=0.5**: 84.8%

**Status**: DONE. Slightly worse than exp01 best (val=0.0372) — more regularization reduced overfit but also slightly capped peak performance at step 20. However, calibration is more robust and training was more stable.

**Comparison vs exp01**:
- AUC-ROC improved slightly (0.9971 vs 0.9967).
- Step 10 accuracy improved (79.1% vs 78.8%).
- Step 20 accuracy decreased (84.8% vs 88.4%).
