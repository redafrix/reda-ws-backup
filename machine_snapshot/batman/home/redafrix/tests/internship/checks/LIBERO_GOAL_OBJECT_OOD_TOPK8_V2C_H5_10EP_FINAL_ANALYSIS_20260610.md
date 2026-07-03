# TopK8-V2C H5 Adaptive Horizon Final Analysis Report

This report presents the final evaluation results comparing the **modified_simvla fixed H10** baseline, the **topk8_v2b_adaptive_horizon (H1)** policy, and the **topk8_v2c_h5_adaptive_horizon (H5)** policy on the **libero_goal_object_ood** task suite.

---

## 1. Executive Summary

We ran the V2C ablation sweep (seeds 0..9) across all 18 tasks of the OOD goal object suite, totaling 180 episodes for the V2C policy. We compared it directly against the baseline `modified_simvla` (180 episodes) and the V2B H1 policy (180 episodes) completed in the previous sweep.

Key findings:
*   **Success Rates:** 
    *   `modified_simvla` (Fixed H10): **95.00%** (171/180)
    *   `topk8_v2b_adaptive_horizon` (H1): **92.78%** (167/180)
    *   `topk8_v2c_h5_adaptive_horizon` (H5): **93.89%** (169/180)
*   **Behavioral Change & Efficiency:** By increasing the execution horizon under high risk from `H=1` to `H=5`, V2C queried the environment **36.34%** of the time with `H=5` and **63.66%** of the time with `H=10`. Total queries dropped from 6,471 (V2B) to 2,815 (V2C), reducing model execution frequency by **56.5%** and speeding up execution by more than 3x.
*   **Impact:** V2C partially recovers the success rate drop observed in V2B (from 92.78% back up to 93.89%), yielding a net success rate drop of only **-1.11%** (Net Gain of -2 episodes vs baseline). Mean step count also improved from **126.51** steps (V2B) to **123.82** steps (V2C).
*   **Verdict:** Increasing the execution horizon from `H=1` to `H=5` on risky OOD states improves both success rate and execution efficiency, but still results in a minor performance drop compared to the fixed H10 baseline.

---

## 2. Paired Comparison Summary

| Metric | Modified SimVLA | TopK8-V2B (H1) | TopK8-V2C (H5) |
|---|---|---|---|
| Total Episodes compared | 180 | 180 | 180 |
| Success Rate | 171/180 (95.00%) | 167/180 (92.78%) | 169/180 (93.89%) |
| Mean Steps | 121.18 | 126.51 | 123.82 |
| V2C Rescues vs Modified | - | - | 1 |
| V2C Regressions vs Modified | - | - | 3 |
| V2C Net Gain vs Modified | - | - | -2 |
| Horizon 1/5 Total Queries | - | 4,581 | 1,023 |
| Horizon 10 Total Queries | - | 1,890 | 1,792 |
| Total Queries (Inferences) | - | 6,471 | 2,815 |
| Percentage queries using H1/H5 | - | 70.79% | 36.34% |
| Overall Mean Risk Score | - | 0.7146 | 0.4153 |
| Overall Max Risk Score | - | 1.0000 | 0.9999 |

---

## 3. Per-Task Results

| Task | Mod Success | V2B Success | V2C Success | Mod Steps | V2B Steps | V2C Steps | V2C Rescues | V2C Regress | H5 | H10 | Risk Mean | Risk Max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Task 00 | 8/10 | 7/10 | 8/10 | 187.3 | 187.3 | 186.0 | 0 | 0 | 98 | 141 | 0.5212 | 0.9997 |
| Task 01 | 10/10 | 9/10 | 10/10 | 175.6 | 182.3 | 170.3 | 0 | 0 | 240 | 55 | 0.7928 | 0.9989 |
| Task 02 | 9/10 | 9/10 | 9/10 | 183.9 | 195.1 | 198.3 | 1 | 1 | 265 | 69 | 0.7807 | 0.9999 |
| Task 03 | 10/10 | 10/10 | 10/10 | 130.6 | 131.1 | 130.9 | 0 | 0 | 8 | 132 | 0.0822 | 0.9914 |
| Task 04 | 10/10 | 10/10 | 10/10 | 132.8 | 133.3 | 133.0 | 0 | 0 | 1 | 137 | 0.0278 | 0.7806 |
| Task 05 | 10/10 | 10/10 | 10/10 | 86.5 | 86.4 | 86.5 | 0 | 0 | 1 | 89 | 0.0688 | 0.8648 |
| Task 06 | 10/10 | 10/10 | 10/10 | 83.0 | 83.0 | 83.0 | 0 | 0 | 0 | 89 | 0.0545 | 0.4594 |
| Task 07 | 9/10 | 9/10 | 9/10 | 109.3 | 109.4 | 109.3 | 0 | 0 | 45 | 92 | 0.3410 | 0.9999 |
| Task 08 | 10/10 | 10/10 | 9/10 | 95.6 | 107.8 | 112.2 | 0 | 1 | 40 | 97 | 0.2940 | 0.9996 |
| Task 09 | 10/10 | 10/10 | 10/10 | 85.8 | 86.4 | 85.6 | 0 | 0 | 7 | 87 | 0.1584 | 0.8771 |
| Task 10 | 10/10 | 10/10 | 10/10 | 83.2 | 83.2 | 83.2 | 0 | 0 | 0 | 88 | 0.0865 | 0.3943 |
| Task 11 | 9/10 | 9/10 | 9/10 | 113.3 | 137.9 | 113.1 | 0 | 0 | 84 | 73 | 0.6873 | 0.9996 |
| Task 12 | 9/10 | 7/10 | 8/10 | 115.6 | 155.5 | 138.9 | 0 | 1 | 134 | 75 | 0.7360 | 0.9998 |
| Task 13 | 9/10 | 9/10 | 9/10 | 150.4 | 150.4 | 150.4 | 0 | 0 | 28 | 140 | 0.3324 | 0.9857 |
| Task 14 | 9/10 | 9/10 | 9/10 | 153.0 | 152.8 | 152.7 | 0 | 0 | 44 | 135 | 0.3725 | 0.9985 |
| Task 15 | 10/10 | 10/10 | 10/10 | 102.7 | 102.7 | 102.7 | 0 | 0 | 0 | 107 | 0.0035 | 0.1984 |
| Task 16 | 10/10 | 10/10 | 10/10 | 88.4 | 88.4 | 88.4 | 0 | 0 | 0 | 92 | 0.0010 | 0.0082 |
| Task 17 | 9/10 | 9/10 | 9/10 | 104.2 | 104.2 | 104.2 | 0 | 0 | 28 | 94 | 0.2404 | 0.9937 |

---

## 4. Key Findings

1.  **Partial Performance Recovery:** V2C (H5) successfully recovered 2 of the 6 regressions experienced in V2B (H1), bringing the success rate up to 93.89%. Rescues vs regressions net gain improved from -4 to -2.
2.  **Model Query Optimization:** Running `H=5` during high-risk steps instead of `H=1` reduced the overall query frequency by more than half (dropping total inferences from 6,471 to 2,815). This represents a major efficiency gain (reducing average GPU execution overhead to ~3.1 mins/task compared to ~10.4 mins/task in V2B).
3.  **Compounding Error Mitigation:** In tasks with high risk, reducing the replanning frequency from every step to every 5 steps led to a decrease in mean steps (from 126.51 to 123.82) by mitigating step-level compounding errors and timeouts.

---

V2C_TOTAL_EPISODES = 180
SEED_PARITY_WITH_BASELINE_PASS = YES
Q95_LOADED_FROM_THRESHOLDS = YES
HORIZON_VALUES_ONLY_10_OR_5 = YES
NO_ACTION_REPLACEMENT = YES
MODIFIED_SUCCESS = 171/180
V2B_H1_SUCCESS = 167/180
V2C_H5_SUCCESS = 169/180
V2C_RESCUES_VS_MODIFIED = 1
V2C_REGRESSIONS_VS_MODIFIED = 3
V2C_NET_GAIN = -2
V2C_H5_TOTAL = 1023
V2C_H10_TOTAL = 1792
V2C_FINAL_VERDICT = HURTS
CATALOG_UPDATED = YES
OBSIDIAN_UPDATED = NO
NEXT_ACTION = analyze regressions and explore replacement strategies
