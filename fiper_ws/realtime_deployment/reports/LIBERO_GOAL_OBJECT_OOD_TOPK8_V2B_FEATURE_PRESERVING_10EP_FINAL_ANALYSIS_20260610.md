# TopK8-V2B Feature Preserving Adaptive Horizon Final Analysis Report

This report presents the final evaluation results comparing the **modified_simvla fixed H10** baseline and the **topk8_v2b_adaptive_horizon** policy on the **libero_goal_object_ood** task suite.

---

## 1. Executive Summary

We ran a paired 10-episode sweep (seeds 0..9) across all 18 tasks of the OOD goal object suite, totaling 360 episodes (180 episodes per policy).
The key findings are:
*   **Success Rate:** The baseline `modified_simvla` achieved **95.00%** (171/180), while `topk8_v2b_adaptive_horizon` achieved **92.78%** (167/180).
*   **Behavioral Change:** V2B did change behavior dynamically. Out of 6,471 total policy queries, it spent **70.79%** of the queries executing with Horizon 1 (replanning every step due to high risk) and **29.21%** with Horizon 10.
*   **Impact:** V2B yields a net success rate drop of **-2.22%** (Net Gain of -4 episodes) and increases the mean step count from **121.18** to **126.51** steps.
*   **Conformal Thresholding Behavior:** The `q95` threshold of `0.6155` successfully prevented the complete horizon collapse observed in V2. In tasks with low OOD shift/low difficulty (like Tasks 4, 5, 6, 10, 15, 16), V2B ran almost entirely at H10. In tasks with high risk (like Tasks 0, 1, 2, 11, 12, 17), V2B spent >70-90% of its steps at H1. However, switching to H1 under OOD uncertainty did not lead to improved success rates, instead occasionally causing minor regressions due to more frequent query points accumulating compounding errors or timing out.

---

## 2. Paired Comparison Summary

| Metric | Value |
|---|---|
| Total Episodes compared | 180 |
| `modified_simvla` Success Rate | 171/180 (95.00%) |
| `topk8_v2b_adaptive_horizon` Success Rate | 167/180 (92.78%) |
| Paired Rescues (Mod Fail -> V2B Success) | 2 |
| Paired Regressions (Mod Success -> V2B Fail) | 6 |
| Net Episode Gain | -4 |
| Shared Successes | 165 |
| Shared Failures | 7 |
| `modified_simvla` Mean Steps | 121.18 |
| `topk8_v2b_adaptive_horizon` Mean Steps | 126.51 |
| Total Horizon 1 Queries | 4,581 |
| Total Horizon 10 Queries | 1,890 |
| Percentage of Queries using H1 | 70.79% |
| Overall Mean Risk Score | 0.7146 |
| Overall Max Risk Score | 1.0000 |

---

## 3. Per-Task Results

| Task | Mod Success | V2B Success | Mod Steps | V2B Steps | Rescues | Regressions | H1 | H10 | Risk Mean | Risk Max |
|---|---|---|---|---|---|---|---|---|---|---|
| Task 00 | 8/10 | 7/10 | 187.3 | 187.3 | 0 | 1 | 439 | 146 | 0.7954 | 0.9995 |
| Task 01 | 10/10 | 9/10 | 175.6 | 182.3 | 0 | 1 | 944 | 92 | 0.8901 | 0.9998 |
| Task 02 | 9/10 | 9/10 | 183.9 | 195.1 | 1 | 1 | 1070 | 91 | 0.8895 | 0.9999 |
| Task 03 | 10/10 | 10/10 | 130.6 | 131.1 | 0 | 0 | 24 | 134 | 0.1650 | 0.9997 |
| Task 04 | 10/10 | 10/10 | 132.8 | 133.3 | 0 | 0 | 3 | 138 | 0.0389 | 0.7806 |
| Task 05 | 10/10 | 10/10 | 86.5 | 86.4 | 0 | 0 | 3 | 89 | 0.0875 | 0.9650 |
| Task 06 | 10/10 | 10/10 | 83.0 | 83.0 | 0 | 0 | 0 | 89 | 0.0545 | 0.4594 |
| Task 07 | 9/10 | 9/10 | 109.3 | 109.4 | 0 | 0 | 194 | 95 | 0.6497 | 0.9999 |
| Task 08 | 10/10 | 10/10 | 95.6 | 107.8 | 0 | 0 | 108 | 102 | 0.5163 | 0.9999 |
| Task 09 | 10/10 | 10/10 | 85.8 | 86.4 | 0 | 0 | 57 | 85 | 0.4279 | 0.9830 |
| Task 10 | 10/10 | 10/10 | 83.2 | 83.2 | 0 | 0 | 0 | 88 | 0.0865 | 0.3943 |
| Task 11 | 9/10 | 9/10 | 113.3 | 137.9 | 1 | 1 | 603 | 78 | 0.9018 | 1.0000 |
| Task 12 | 9/10 | 7/10 | 115.6 | 155.5 | 0 | 2 | 586 | 100 | 0.8686 | 0.9999 |
| Task 13 | 9/10 | 9/10 | 150.4 | 150.4 | 0 | 0 | 140 | 140 | 0.5869 | 0.9913 |
| Task 14 | 9/10 | 9/10 | 153.0 | 152.8 | 0 | 0 | 220 | 135 | 0.6731 | 0.9984 |
| Task 15 | 10/10 | 10/10 | 102.7 | 102.7 | 0 | 0 | 0 | 107 | 0.0035 | 0.1984 |
| Task 16 | 10/10 | 10/10 | 88.4 | 88.4 | 0 | 0 | 0 | 92 | 0.0010 | 0.0082 |
| Task 17 | 9/10 | 9/10 | 104.2 | 104.2 | 0 | 0 | 190 | 89 | 0.6507 | 0.9951 |

---

## 4. Key Behavioral Findings

1.  **True Conformal Adaptivity:** Unlike V2 which collapsed to 100% Horizon 1 due to zeroed out ACE features causing false-positive shift flags, the feature-preserving V2B runner shows distinct regional behavior:
    *   **In-distribution or Low-uncertainty states:** In tasks such as Task 6, Task 15, and Task 16, risk scores remained virtually zero (`0.0010` to `0.0545`), resulting in 100% Horizon 10 execution.
    *   **High-uncertainty states:** In tasks with significant goal/object changes (Tasks 0, 1, 2, 11, 12), risk scores frequently exceeded `0.6155`, forcing Horizon 1 execution to adaptively replan at each timestep.
2.  **No Performance Benefit:** Running with a shorter horizon on OOD states did not prevent failures or rescue performance. Instead, it slightly hurt performance (success dropped from 95.0% to 92.78%). Frequent replanning in SimVLA can accumulate compounding step-level errors or cause timeouts (indicated by higher mean steps for V2B).
3.  **Recommendation:** Conformal risk-based horizon switching can flag OOD states cleanly, but dynamically reducing SimVLA execution horizon to H1 under risk may degrade the policy quality due to execution frequency shift.

---

V2B_TOTAL_EPISODES = 360
SEED_PARITY_PASS = YES
V2B_RUNTIME_BEHAVIOR_CONFIRMED = YES
V2B_HORIZON1_TOTAL = 4581
V2B_HORIZON10_TOTAL = 1890
MODIFIED_SUCCESS = 171/180
V2B_SUCCESS = 167/180
V2B_RESCUES_VS_MODIFIED = 2
V2B_REGRESSIONS_VS_MODIFIED = 6
V2B_NET_GAIN = -4
V2B_FINAL_VERDICT = HURTS
CATALOG_UPDATED = NO
OBSIDIAN_UPDATED = NO
NEXT_ACTION = analyze regressions and explore replacement strategies
