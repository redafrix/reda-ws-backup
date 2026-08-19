# Side-by-Side Comparison: Seen Internal TEST vs Converted OOD150

> [!NOTE]
> **Methodology**: Operating thresholds are strictly calibrated on Seen VALIDATION data only. The table evaluates transfer performance on the locked internal Seen TEST split (736 episodes) and the converted exact-only OOD150 subset (136 episodes).

| Rule | Split | tau | Succ FA % | Fail Det % | Det@25 % | Det@50 % | Det@100 % | Never % |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| **Best F1** | **Seen internal TEST** | 0.5791 | 7.60% | 100.00% | 60.26% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5791 | 18.06% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **Fixed 0.5** | **Seen internal TEST** | 0.5000 | 17.48% | 100.00% | 69.23% | 91.03% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5000 | 25.00% | 100.00% | 75.00% | 89.06% | 100.00% | 0.00% |
| **q90 success** | **Seen internal TEST** | 0.5631 | 8.97% | 100.00% | 61.54% | 85.90% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.5631 | 19.44% | 100.00% | 70.31% | 85.94% | 100.00% | 0.00% |
| **q95 success** | **Seen internal TEST** | 0.6643 | 3.65% | 100.00% | 55.13% | 83.33% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.6643 | 13.89% | 100.00% | 59.38% | 81.25% | 100.00% | 0.00% |
| **q99 success** | **Seen internal TEST** | 0.8792 | 1.22% | 100.00% | 38.46% | 74.36% | 100.00% | 0.00% |
| | **OOD150 converted exact** | 0.8792 | 5.56% | 100.00% | 42.19% | 75.00% | 100.00% | 0.00% |
