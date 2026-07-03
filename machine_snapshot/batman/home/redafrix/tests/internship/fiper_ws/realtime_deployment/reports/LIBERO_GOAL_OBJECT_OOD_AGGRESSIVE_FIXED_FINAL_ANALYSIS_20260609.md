# LIBERO_GOAL_OBJECT_OOD_AGGRESSIVE_FIXED_FINAL_ANALYSIS_20260609

## 1. Execution Overview
- **Tasks**: 18
- **Policies**: 3 (original_simvla, modified_simvla, risk_topk8)
- **Episodes per Policy**: 10
- **Total Episodes Executed**: 540
- **Seed Parity Check**: PASS
- **Old Invalid Root Excluded**: YES (All configs pointed exclusively to the new aggressive_fixed root).

## 2. Total Success Rates
- **original_simvla**: 169 / 180 (93.9%)
- **modified_simvla**: 168 / 180 (93.3%)
- **risk_topk8**: 172 / 180 (95.6%)

## 3. Paired Comparisons (Total)
- **modified_simvla vs original_simvla**: 8 Rescues, 9 Regressions
- **risk_topk8 vs modified_simvla**: 6 Rescues, 2 Regressions
- **risk_topk8 vs original_simvla**: 9 Rescues, 6 Regressions

## 4. Action Modification Stats (risk_topk8)
- **Total Modifications Across All Episodes**: 254
- **Episodes with >=1 Modification**: 80

## 5. Per-Task Breakdown

| Task | Orig SR | Mod SR | Risk SR | Risk vs Mod (Res/Reg) | Risk vs Orig (Res/Reg) |
|---|---|---|---|---|---|
| 0 | 8/10 | 8/10 | 8/10 | 2 / 2 | 1 / 1 |
| 1 | 10/10 | 9/10 | 9/10 | 0 / 0 | 0 / 1 |
| 2 | 9/10 | 8/10 | 9/10 | 1 / 0 | 1 / 1 |
| 3 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 4 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 5 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 6 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 7 | 9/10 | 9/10 | 9/10 | 0 / 0 | 1 / 1 |
| 8 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 9 | 10/10 | 9/10 | 9/10 | 0 / 0 | 0 / 1 |
| 10 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 11 | 9/10 | 10/10 | 10/10 | 0 / 0 | 1 / 0 |
| 12 | 9/10 | 10/10 | 10/10 | 0 / 0 | 1 / 0 |
| 13 | 6/10 | 8/10 | 9/10 | 1 / 0 | 3 / 0 |
| 14 | 10/10 | 9/10 | 10/10 | 1 / 0 | 0 / 0 |
| 15 | 10/10 | 10/10 | 10/10 | 0 / 0 | 0 / 0 |
| 16 | 10/10 | 9/10 | 9/10 | 0 / 0 | 0 / 1 |
| 17 | 9/10 | 9/10 | 10/10 | 1 / 0 | 1 / 0 |

## 6. Final Verdict
**Does aggressive TopK8 help on libero_goal_object_ood?**
YES. The aggressive TopK8 detector successfully provided net rescues over both the original and modified baselines, justifying the 0.3 threshold configuration.