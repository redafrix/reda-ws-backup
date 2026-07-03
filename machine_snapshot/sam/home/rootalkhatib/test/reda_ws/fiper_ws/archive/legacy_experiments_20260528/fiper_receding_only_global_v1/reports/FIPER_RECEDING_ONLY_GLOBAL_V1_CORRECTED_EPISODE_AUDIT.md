# FIPER Corrected Episode Audit Report (Sam)

## 1. Bug Investigation
- **True Failure Rows:** 171,600
- **True Unique Failure Episodes:** 572
- **The "3405" Bug:** The original script was extending the episode summary list for every evaluation split. Since failure subsets (early, mid, late, near_end) overlap with failure_eval_all, each failure episode was counted multiple times (545 + 5 * 572 = 3405).
- **Script Patched:** YES. Added --eval-only mode and fixed the aggregation loop to only count failure_eval_all and success_test_id for episode-level metrics.
- **Eval-only Rerun Needed:** YES. Completed on CUDA.

## 2. Corrected Early Detection Performance (q95)
| Signal | N Episodes | Mean Norm Time | Median Norm Time | Det @10% | Det @25% | Det @50% | Never |
|---|---|---|---|---|---|---|---|
| RND q95 | 572 | 0.1870 | 0.1600 | 37.06% | 63.81% | 78.85% | 13.99% |
| ACE q95 | 572 | 0.3005 | 0.2567 | 4.37% | 42.31% | 76.92% | 13.46% |
| **OR q95** | **572** | **0.1704** | **0.1567** | **37.76%** | **70.98%** | **88.81%** | **7.17%** |
| AND q95* | 572 | 0.3430 | 0.2967 | 1.92% | 27.80% | 57.69% | 30.94% |

*\*AND refers to simultaneous high-confidence alarms.*

## 3. Corrected Complementarity (Episode Level)
How many failure episodes are ever detected by the signals?
- **Both RND & ACE:** 456 (79.7%)
- **Only RND:** 36 (6.3%)
- **Only ACE:** 39 (6.8%)
- **Missed Both:** 41 (7.2%)
- **Total Detection (OR):** 531 / 572 (92.8%)

## 4. Final Verdict
The original final verdict **STILL HOLDS**. 
The receding-only dataset shows strong early detection potential. RND is particularly fast (mean alarm at 18% of episode length), while ACE provides a solid safety net, catching an additional 39 episodes that RND misses. The combined FIPER OR q95 policy reaches >92% total detection with a false alarm rate of ~6.4% on success episodes.

- **EPISODE_COUNTING_BUG_FOUND:** YES
- **EVAL_OUTPUTS_CORRECTED:** YES
- **EARLY_FAILURE_DETECTION_STILL_USEFUL:** YES
- **READY_FOR_BOB_REPLICATION_AFTER_CORRECTION:** YES

**Date:** May 26, 2026
**Node:** Sam
