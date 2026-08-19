# Converted OOD150 Paper-Style Threshold Transfer Table

> [!NOTE]
> **Scope**: EXACT-ONLY NEW-PROTOCOL OOD150 SUBSET (136 episodes: 72 success, 64 failure). Frozen Seen validation thresholds.

| Rule | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Det@OODMeanSucc100 % | Det@Canonical18Q % | Never % |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Best F1 | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 82.81% | 85.94% | 0.00% |
| Fixed 0.5 | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 89.06% | 89.06% | 0.00% |
| q90 success | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 84.38% | 85.94% | 0.00% |
| q95 success | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 78.12% | 81.25% | 0.00% |
| q99 success | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 67.19% | 75.00% | 0.00% |
