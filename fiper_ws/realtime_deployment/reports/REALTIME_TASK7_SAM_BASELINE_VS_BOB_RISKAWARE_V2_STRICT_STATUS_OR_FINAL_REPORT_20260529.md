# Deployment Comparison Report: Sam Baseline vs. Bob Risk-Aware (v2 Strict)
**Task:** `libero_10_with_milk` - Task 7
**Date:** May 29, 2026

This report presents a paired comparison analysis between the vanilla SimVLA baseline (run on Sam) and the risk-aware SimVLA deployment utilizing the `risk_filtered_lowest_score_candidate_v2_strict_margin` policy (run on Bob) over 100 trials using identical environmental reset seeds.

---

## 1. Process & Completion Status

| Machine | Experiment / Workspace | Completed Episodes | Status | Active PIDs |
|---|---|---|---|---|
| **Sam** | Baseline SimVLA (`sam_v1`) | 100 / 100 | **Completed** | None |
| **Bob** | Risk-Aware SimVLA (`bob_full_20260528`) | 100 / 100 | **Completed** | None |

Both runs have finished their 100-episode target cleanly, and no active processes remain running on either machine for these configurations.

---

## 2. Overall Performance Metrics

### Sam Baseline (Vanilla SimVLA)
*   **Total Episodes:** 100
*   **Successes:** 58
*   **Failures / Timeouts:** 42
*   **Success Rate:** **58.00%**
*   **Errors:** 0 (0.00%)
*   **Average Steps:** 270.97
*   **Median Steps:** 282.00

### Bob Risk-Aware (v2 Strict Policy)
*   **Total Episodes:** 100
*   **Successes:** 61
*   **Failures / Timeouts:** 39
*   **Success Rate:** **61.00%** (+3.00% improvement)
*   **Errors:** 0 (0.00%)
*   **Average Steps:** 267.55
*   **Median Steps:** 274.50

---

## 3. Paired Comparison Analysis
Because both runs used the exact same 100 reset seeds in the same episode-index order, we can pair the outcomes directly:

| Category | Count | Percentage | Description |
|---|---|---|---|
| **Baseline Failure $\rightarrow$ Risk-Aware Success** | 25 | 25.0% | **Improvement:** Risk-aware intervention recovered a failing run |
| **Baseline Success $\rightarrow$ Risk-Aware Failure** | 22 | 22.0% | **Degradation:** Action modification disrupted a successful trajectory |
| **Both Success** | 36 | 36.0% | **Neutral (Success):** Robot succeeded in both setups |
| **Both Failure** | 17 | 17.0% | **Neutral (Failure):** Robot timed out/failed in both setups |
| **Missing/Unpaired** | 0 | 0.0% | All 100 episodes paired perfectly |

### Detailed Trajectory Group Statistics
*   **Fail $\rightarrow$ Success Group (25 episodes):**
    *   *Sam Steps:* 300.00 (All timed out)
    *   *Bob Steps:* Mean = 245.48, Median = 241.00
    *   *Bob Interventions:* Mean = 15.04 mods, Median = 15.00 mods, Max = 35 mods
    *   *First Mod Step:* Mean = 61.16, Median = 53.00
*   **Success $\rightarrow$ Fail Group (22 episodes):**
    *   *Sam Steps:* Mean = 251.14, Median = 246.50
    *   *Bob Steps:* 300.00 (All timed out)
    *   *Bob Interventions:* Mean = 18.09 mods, Median = 17.00 mods, Max = 72 mods
    *   *First Mod Step:* Mean = 56.73, Median = 33.00
*   **Both Success Group (36 episodes):**
    *   *Sam Steps:* Mean = 249.22, Median = 245.50
    *   *Bob Steps:* Mean = 247.72, Median = 244.50
    *   *Bob Interventions:* Mean = 20.92 mods, Median = 17.50 mods, Max = 62 mods
    *   *First Mod Step:* Mean = 48.25, Median = 35.50
*   **Both Fail Group (17 episodes):**
    *   *Sam/Bob Steps:* 300.00 (All timed out)
    *   *Bob Interventions:* Mean = 20.06 mods, Median = 18.00 mods, Max = 48 mods
    *   *First Mod Step:* Mean = 76.65, Median = 84.00

---

## 4. Bob Intervention & Risk Statistics

*   **Total Modifications:** 1,868 across all 100 runs
*   **Modifications per Episode:**
    *   *Mean:* 18.68
    *   *Median:* 17.00
    *   *Max:* 72
    *   *Min:* 4
*   **First Modification Timestep Distribution:**
    *   *10th Percentile:* 22.90
    *   *25th Percentile:* 30.00
    *   *50th Percentile (Median):* 38.00
    *   *75th Percentile:* 92.50
    *   *90th Percentile:* 116.10
*   **Risk Profiles across all timesteps:**
    *   *Mean Main Risk:* 0.5561
    *   *Mean Selected Risk:* 0.5367
    *   *Mean Risk Reduction (Main - Selected):* **0.0194**

---

## 5. Seed, Leakage & Validation Checks

*   **Same Reset Seeds Verified:** **YES** (All 100 seeds matched perfectly)
*   **Unique Action-Sampling Seeds per Timestep:** **YES**
*   **Bob Seed Collisions:** **0**
*   **Bob Main-vs-ACE Collisions:** **0**
*   **Policy Name Verified:** `risk_filtered_lowest_score_candidate_v2_strict_margin`

---

## 6. Honest Verdict & Key Takeaways

1.  **Did risk-aware action selection improve success rate?**
    Yes, it improved the overall success rate by **3%** (from 58.00% to 61.00%) and decreased the average step counts overall (267.55 vs 270.97).
2.  **Did it hurt success rate?**
    It successfully rescued 25 episodes that would have failed under the baseline. However, it also introduced regressions in 22 episodes that would have succeeded under the baseline (causing them to time out in all 22 cases). This highlights that while the v2 strict policy is far less aggressive than v1 (averaging 18.68 modifications per episode instead of ~214 in the v1 smoke test), it still occasionally overrules valid actions, resulting in a slightly conservative slowdown that tips tight trajectories into timeouts.
3.  **Is this policy ready for more tasks?**
    It is ready for wider testing, but the close margin between recovered runs (25) and degraded runs (22) indicates the intervention criteria are still delicate.
4.  **What should be changed next?**
    *   **Adaptively Tune Margins:** Instead of a fixed $\Delta \ge 0.10$ threshold, scale the required improvement threshold dynamically based on the current main score or confidence interval.
    *   **Limit Modifications in Steady-State:** Implement a lockout mechanism or higher threshold when the robot is in a steady state (i.e. low risk or low variance among ACE candidates) to avoid disrupting working trajectories.
    *   **Investigate Timeout Causes:** Examine step-by-step trajectories of the 22 `Success -> Fail` episodes to see if the modifications resulted in cyclic behaviors, stuck orientations, or excessive deceleration.

---

## 7. Metadata Validation Fields

```ini
SAM_BASELINE_COMPLETE = YES
BOB_RISKAWARE_COMPLETE = YES
SAME_RESET_SEEDS_VERIFIED = YES
BOB_SEED_COLLISIONS = 0
BOB_MAIN_ACE_COLLISIONS = 0
FINAL_COMPARISON_READY = YES
FINAL_REPORT_PATH = realtime_deployment/reports/REALTIME_TASK7_SAM_BASELINE_VS_BOB_RISKAWARE_V2_STRICT_STATUS_OR_FINAL_REPORT_20260529.md
```
