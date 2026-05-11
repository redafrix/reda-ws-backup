# v7 Experiment 01 — Combined Ideas 1+3+4 (v7 dataset, first run)

**Ideas combined**: MC loss (1) + Task embedding (3) + 256/2L LSTM (4)
**Dataset**: v7 11D, 31537 train / 3942 val / 3942 test episodes
**Hyperparams**: dropout=0.05, weight_decay=0.01, epochs=500
**Best epoch**: 61 (early overfit — val kept worsening after epoch 61)
**Val Brier**: 0.037176 | **Test Brier**: 0.038560
**Test AUC-ROC**: 0.9967
**Early AUC @ step 20**: 0.884
**Stepwise accuracy @ step 10, τ=0.5**: 78.8%
**Status**: DONE. Overfit after epoch 61. See v7_exp02 for regularized version.
