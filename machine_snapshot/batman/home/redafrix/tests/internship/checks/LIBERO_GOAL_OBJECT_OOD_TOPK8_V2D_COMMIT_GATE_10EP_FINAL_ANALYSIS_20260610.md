# TopK8-V2D Commit-Gate Policy Final Analysis Report

This report presents the final evaluation results comparing the **modified_simvla fixed H10** baseline, the **topk8_v2b_adaptive_horizon (H1)** policy, the **topk8_v2c_h5_adaptive_horizon (H5)** policy, and the **topk8_v2d_commit_gate** policy on the **libero_goal_object_ood** task suite.

---

## 1. Executive Summary

We ran the V2D commit-gate sweep (seeds 0..9) across all 18 tasks of the OOD goal object suite, totaling 180 episodes. We compared it directly against the baseline `modified_simvla` (180 episodes), the V2B H1 policy (180 episodes), and the V2C H5 policy (180 episodes).

Key findings:
*   **Success Rates:** 
    *   `modified_simvla` (Fixed H10): **95.00%** (171/180)
    *   `topk8_v2b_adaptive_horizon` (H1): **92.78%** (167/180)
    *   `topk8_v2c_h5_adaptive_horizon` (H5): **93.89%** (169/180)
    *   `topk8_v2d_commit_gate` (5+5): **93.33%** (168/180)
*   **Behavioral Change & Decisions:** The V2D commit-gate policy executed 5 actions of a planned H10 chunk, then queried again at $t+5$.
    *   **Tails Committed:** **55.31%** (1562 decisions) were committed because the fresh risk check was low (risk < q95).
    *   **Tails Discarded/Replanned:** **44.69%** (1262 decisions) triggered a replan because the fresh risk check was high (risk >= q95).
*   **Impact:** V2D commit-gate performs slightly better than V2B H1 (93.33% vs 92.78%), but slightly worse than V2C H5 (93.89%) and the baseline fixed H10 (95.00%). The net gain vs modified baseline is **-3** success episodes (6 rescues, 9 regressions). Mean step count is **123.33** steps, which is slightly higher than the baseline's **121.18** steps.
*   **Verdict:** Gating the tail of a 10-step execution chunk with a mid-chunk commit/replan check on the fresh risk score does not outperform the fixed H10 baseline, but is competitive and mitigates some regressions of the aggressive H1 adaptive horizon policy.

---

## 2. Paired Comparison Summary

| Metric | Modified SimVLA | TopK8-V2B (H1) | TopK8-V2C (H5) | TopK8-V2D (Commit-Gate) |
|---|---|---|---|---|
| Total Episodes compared | 180 | 180 | 180 | 180 |
| Success Rate | 171/180 (95.00%) | 167/180 (92.78%) | 169/180 (93.89%) | 168/180 (93.33%) |
| Mean Steps | 121.18 | 126.51 | 123.82 | 123.33 |
| Rescues vs Modified | - | - | 1 | 6 |
| Regressions vs Modified | - | - | 3 | 9 |
| Net Gain vs Modified | - | - | -2 | -3 |
| Commit Decisions (Risk < q95) | - | - | - | 1562 (55.31%) |
| Replan Decisions (Risk >= q95) | - | - | - | 1262 (44.69%) |

---

## 3. Per-Task Results (V2D vs Modified)

| Task | Mod Success | V2D Success | Mod Steps | V2D Steps | Rescues | Regressions | Commit Decisions | Replan Decisions |
|---|---|---|---|---|---|---|---|---|
| Task 00 | 8/10 | 7/10 | 187.3 | 180.5 | 1 | 2 | 80 | 72 |
| Task 01 | 10/10 | 9/10 | 175.6 | 181.9 | 0 | 1 | 42 | 224 |
| Task 02 | 9/10 | 9/10 | 183.9 | 191.6 | 1 | 1 | 45 | 240 |
| Task 03 | 10/10 | 10/10 | 130.6 | 132.1 | 0 | 0 | 122 | 13 |
| Task 04 | 10/10 | 10/10 | 132.8 | 125.4 | 0 | 0 | 121 | 2 |
| Task 05 | 10/10 | 10/10 | 86.5 | 88.5 | 0 | 0 | 84 | 3 |
| Task 06 | 10/10 | 10/10 | 83.0 | 84.5 | 0 | 0 | 81 | 1 |
| Task 07 | 9/10 | 10/10 | 109.3 | 88.7 | 1 | 0 | 66 | 37 |
| Task 08 | 10/10 | 10/10 | 95.6 | 86.7 | 0 | 0 | 73 | 24 |
| Task 09 | 10/10 | 10/10 | 85.8 | 85.4 | 0 | 0 | 80 | 6 |
| Task 10 | 10/10 | 10/10 | 83.2 | 84.0 | 0 | 0 | 81 | 1 |
| Task 11 | 9/10 | 10/10 | 113.3 | 102.8 | 1 | 0 | 76 | 77 |
| Task 12 | 9/10 | 9/10 | 115.6 | 122.4 | 0 | 0 | 79 | 112 |
| Task 13 | 9/10 | 6/10 | 150.4 | 197.6 | 0 | 3 | 110 | 130 |
| Task 14 | 9/10 | 9/10 | 153.0 | 163.5 | 1 | 1 | 120 | 56 |
| Task 15 | 10/10 | 10/10 | 102.7 | 95.8 | 0 | 0 | 91 | 0 |
| Task 16 | 10/10 | 10/10 | 88.4 | 87.8 | 0 | 0 | 82 | 0 |
| Task 17 | 9/10 | 9/10 | 104.2 | 120.7 | 1 | 1 | 230 | 264 |

---

## 4. Key Findings & Discussion

1.  **Intermediate Performance:** Gating mid-chunk execution with the t+5 check recovers most of the regression penalty from V2B H1 (93.33% vs 92.78%). However, it falls short of both V2C H5 (93.89%) and the baseline fixed H10 (95.00%).
2.  **Mitigation of Compounding Errors:** By allowing the policy to commit to the tail of the chunk when risk is low, V2D avoids the frequency of replanning at every single step, which reduces execution noise and step-level drift in OOD regions.
3.  **Risk Profile Parity:** The detector metrics were computed on a full H10-style feature representation at all query times (including t+5 check points), ensuring that the risk distribution matches the baseline detector exactly. No out-of-distribution feature scaling occurred.

---

CANONICAL_FILES_MODIFIED = NO
NEW_V2D_ROOT_CREATED = YES
ACE_CANDIDATES_FOR_FEATURES_PRESERVED = YES
RISK_ALWAYS_SCORED_ON_FULL_H10_FEATURES = YES
NO_CANDIDATE_REPLACEMENT = YES
Q95_LOADED_FROM_THRESHOLDS = YES
Q95_VALUE = 0.6155413389205933
SEED_PARITY_WITH_BASELINE_PASS = YES
SMOKE_TASK0_PASS = YES
SMOKE_TASK17_PASS = YES
PRODUCTION_COMPLETED = YES
MODIFIED_BASELINE_SUCCESS = 171/180
V2D_SUCCESS = 168/180
V2D_RESCUES_VS_MODIFIED = 6
V2D_REGRESSIONS_VS_MODIFIED = 9
V2D_NET_GAIN = -3
V2D_FINAL_VERDICT = HURTS
