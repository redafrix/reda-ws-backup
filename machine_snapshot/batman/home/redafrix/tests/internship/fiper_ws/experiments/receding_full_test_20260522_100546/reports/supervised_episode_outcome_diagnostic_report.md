# Episode Outcome Separability Diagnostic Report

This diagnostic experiment evaluates how well we can distinguish success vs failure steps using various action features via supervised classifiers.
Note: This is an offline diagnostic only, not a runtime safety monitor.

## Classification Performance Summary
| Feature Set | LR AUROC | LR AUPRC | MLP AUROC | MLP AUPRC | LR Brier Score |
|---|---|---|---|---|---|
| Action Chunk Only | 0.9665 | 0.9681 | 0.9969 | 0.9958 | 0.1678 |
| ACE Metrics Only | 0.9679 | 0.9598 | 0.9959 | 0.9944 | 0.1619 |
| RND Score Only | 0.9979 | 0.9968 | 0.9979 | 0.9968 | 0.1832 |
| ACE + RND Combined | 0.9965 | 0.9952 | 0.9998 | 0.9997 | 0.1391 |

## Logistic Regression Coefficient Analysis (ACE Features)
Positive coefficients mean higher values correlate with failure; negative coefficients correlate with success.

| Feature | Coefficient | Coefficient Magnitude |
|---|---|---|
| ACE score (Gaussian Entropy) | 2.4647 | 2.4647 |
| Action std mean | -0.5063 | 0.5063 |
| Action pairwise distance mean | 2.1409 | 2.1409 |
| Gripper std | 1.2137 | 1.2137 |
| Translation std | -0.5226 | 0.5226 |
| Rotation std | -1.3526 | 1.3526 |
| Effective diversity score | 0.0000 | 0.0000 |
| Near-duplicate pairs | 0.0000 | 0.0000 |