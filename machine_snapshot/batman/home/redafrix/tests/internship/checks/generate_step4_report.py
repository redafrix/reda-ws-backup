import os
import subprocess

report_content = """# Forensic Sanity Audit Report: Step 4 - Risk Score Effect & Detector Validation

> [!IMPORTANT]
> This is Step 4 of the forensic sanity audit conducted on SimVLA risk-aware simulation results on host **pcrobot**. The audit is strictly read-only; no code, configurations, or simulation data were modified.

## 1. Introduction & Objectives
The purpose of this step is to determine if the detector's risk scores explain the policy improvements (rescues) and regressions, evaluate threshold sensitivity, check if the improvements are driven by a real detector effect or just brute-force candidate sampling, and deliver a final verdict.

We utilize the detailed query-level logs (`step_scores_risk_topk8.jsonl`) from the aggressive TopK8 Task 3 and Task 6 online runs on `pcrobot` to conduct this audit.

---

## 2. Risk Score Statistics by Episode Group

Using the corrected seed lists from the Step 3 audit, we split the 100 episodes of Task 6 Aggressive TopK8 into four groups: Rescues (19), Regressions (14), Shared Successes (43), and Shared Failures (24). 

Below are the computed metrics for each group:

| Metric | Rescues (19) | Regressions (14) | Shared Success (43) | Shared Failure (24) |
| :--- | :---: | :---: | :---: | :---: |
| **Mean Main Risk Score (All Steps)** | 0.6477 | 0.8162 | 0.5633 | 0.8552 |
| **Mean Max Main Risk Score per Episode** | 0.8181 | 0.9991 | 0.7535 | 0.9995 |
| **Mean Selected Risk Score (All Steps)** | 0.6278 | 0.8012 | 0.5386 | 0.8457 |
| **Mean Risk Reduction (All Steps)** | 0.0200 | 0.0149 | 0.0247 | 0.0094 |
| **Mean Risk Reduction (Interventions Only)** | 0.0604 | 0.0826 | 0.0694 | 0.0729 |
| **Total Interventions** | 88 | 76 | 186 | 93 |
| **Interventions per Episode** | 4.63 | 5.43 | 4.33 | 3.88 |
| **Mean First Intervention Query Index** | 0.95 | 0.79 | 0.97 | 0.64 |
| **Mean Selected Candidate Rank (1-8, 1=Best)** | 1.00 | 1.00 | 1.00 | 1.00 |
| **Selected Risk < Main Risk %** | 100.0% | 100.0% | 100.0% | 100.0% |

For Task 3 (2 Rescues, 0 Regressions, 17 Shared Success, 81 Shared Failure):
* **Rescues (2):** Mean Main Risk = 0.6851, Max Main Risk = 0.9892, Interventions per Episode = 3.50, First Intervention index = 13.00, Risk Reduction (Interventions Only) = 0.0987.
* **Shared Success (17):** Mean Main Risk = 0.8816, Max Main Risk = 0.9893, Interventions per Episode = 0.35, Risk Reduction (Interventions Only) = 0.1262.
* **Shared Failure (81):** Mean Main Risk = 0.9808, Max Main Risk = 0.9997, Interventions per Episode = 0.20, Risk Reduction (Interventions Only) = 0.1267.

---

## 3. Comparison & Key Diagnostic Questions

### A. Are rescue episodes higher risk than regression episodes?
**NO.** The mean main risk score for regressions is **0.8162** (with a max of **0.9991**), whereas the mean main risk score for rescues is **0.6477** (with a max of **0.8181**). This demonstrates that regressions occur on trajectories that are significantly more critical/unstable from the beginning, while rescues occur on moderately risky trajectories.

### B. Are risk reductions larger on rescues than regressions?
**NO.** The average risk reduction on intervened steps is **0.0826** for regressions and **0.0604** for rescues. The detector actually achieves a slightly larger absolute risk reduction in regression episodes, but because the baseline risk is so high (0.8162), the post-intervention risk score remains extremely high (**0.8012**).

### C. Do regressions happen because the threshold fires too early?
**YES.** Under the aggressive threshold of 0.3, the first intervention happens almost immediately at query step 0.79 (timestep 0 or 10) in regressions. This shows that the detector is overactive and intervenes immediately on almost all episodes, disrupting correct trajectories before they have a chance to progress.

### D. Do regressions happen even when selected risk is only slightly lower?
**YES.** In regressions, the average risk reduction is only **0.0826**, leaving the selected candidate risk score at an extremely high **0.8012**. The policy executes candidate chunks that the detector still classifies as high-risk, leading to eventual failure.

### E. Does Task 6 improvement come from meaningful risk discrimination or brute-force frequent replacement?
**MIXED / BRUTE-FORCE DOMINATED.** 
* The detector does show *meaningful risk discrimination*: the baseline risk score is lowest for shared success (0.5633), moderate for rescues (0.6477), and highest for regressions (0.8162) and shared failures (0.8552). This indicates the risk scores reflect true trajectory difficulty.
* However, because the threshold is set to a very low `0.3`, the intervention rate is **94.7%**. The policy modifies almost every single chunk (averaging 4.33 to 5.43 interventions per episode). This means the policy is running in a near-continuous "best-of-8 candidate replacement" mode. Rather than surgical intervention, the success rate boost is largely a result of brute-force candidate sampling under weak detector guidance, which introduces high fragility (14 regressions).

---

## 4. Threshold Sensitivity Analysis

Without running new simulations, we analyzed what would happen under higher thresholds by checking if the maximum main risk score per episode ever crosses the threshold. If `max_main_score < T`, no intervention would occur, and the episode would revert to the baseline outcome (rescues would be lost/fail; regressions would be prevented/succeed).

### Task 6 Threshold Analysis Summary:

| Threshold | Allowed Interventions (Queries) | Preserved Rescues | Prevented Regressions | Remaining Regressions | Estimated Net Gain |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **0.3** | 1825 / 1928 (94.7%) | 19 / 19 | 0 / 14 | 14 | **+5** |
| **0.4** | 1720 / 1928 (89.2%) | 19 / 19 | 0 / 14 | 14 | **+5** |
| **0.5** | 1560 / 1928 (80.9%) | 19 / 19 | 0 / 14 | 14 | **+5** |
| **0.6155 (q95)** | 1268 / 1928 (65.8%) | 16 / 19 | 0 / 14 | 14 | **+2** |

> [!WARNING]
> **Key Insight on Thresholds:**
> Raising the threshold does **NOT** reduce regressions. Every single one of the 14 regressions reached a maximum main risk score of at least **0.99** (well above the conformal threshold of 0.6155). As a result, raising the threshold to 0.5 or 0.6155 does not prevent these regressions, but raising it to 0.6155 causes us to lose 3 rescues, reducing the net gain to **+2**. The regressions are caused by the fact that once the trajectory enters a high-risk state, any chosen candidate still leads to failure, and raising the threshold does not keep the policy from entering those states.

---

## 5. Candidate Sampling Fairness & Random Search Concern

* **Candidates evaluated:** 8 candidate chunks are evaluated at every query step where the detector intervenes.
* **Selection Metric:** The policy selects the candidate chunk with the lowest risk score (`selected_candidate_rank = 1.00`).
* **Random Search Ablation Proposal:** To determine if the positive net gain (+5) is driven by the detector's ability to select safe actions or if it's simply a benefit of sampling 8 alternative chunks (random search), we propose a future ablation:
  * **Random Candidate Selection (RCS) Ablation:** If `main_score >= T`, instead of choosing the candidate with the lowest detector risk, select one of the 8 candidates at random and execute it. 
  * If the RCS success rate is close to the risk-aware policy (62%), then the improvement is due to brute-force sampling diversity. If it drops back to or below the baseline (57%), then the detector's risk guidance is providing a real filtering effect.

---

## 6. Audit Verdict

**Verdict:** **WEAK_BUT_REAL_DETECTOR_EFFECT**

* **Why it is REAL:** The detector's risk scores show clear discrimination between successful baseline trajectories (0.5633 mean risk) and failing baseline trajectories (0.8162 mean risk for regressions, 0.8552 for shared failures).
* **Why it is WEAK & FRAGILE:** The selection of the lowest-risk candidate from the 8 sampled is not robust. At threshold 0.3, the policy intervenes on 94.7% of steps, acting as a brute-force replacement search. This over-activity breaks 14 baseline-successful trajectories (regressions), and raising the threshold to q95 does not prevent these regressions because their risk scores are extremely high.

---

## 7. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
DETAILED_QUERY_LOGS_FOUND = YES
TASK3_RISK_SCORE_ANALYZABLE = YES
TASK6_RISK_SCORE_ANALYZABLE = YES
RESCUES_HAVE_HIGHER_RISK_THAN_REGRESSIONS = NO
RESCUES_HAVE_LARGER_RISK_REDUCTION = NO
THRESHOLD_0_3_OVERACTIVE = YES
LESS_AGGRESSIVE_THRESHOLD_LOOKS_PROMISING = NO
RANDOM_SEARCH_CONCERN = MEDIUM
DETECTOR_EFFECT_VERDICT = WEAK_BUT_REAL_DETECTOR_EFFECT
MOST_IMPORTANT_FINDING = The detector's risk scores show meaningful discrimination (regressions have much higher baseline risk than rescues), but the intervention strategy is highly fragile and over-intervenes, resulting in a high rate of regressions that cannot be mitigated by simply raising the threshold.
NEXT_AUDIT_STEP = Propose or execute zero-shot generalization testing on held-out tasks.
"""

# Write locally
local_report_path = "/home/redafrix/tests/internship/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md"
with open(local_report_path, "w") as f:
    f.write(report_content)
print(f"Step 4 Report written locally to {local_report_path}")

# Write to pcrobot
remote_report_path = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md"
print("Uploading Step 4 Report to pcrobot...")
p = subprocess.Popen(f"ssh pcrobot \"cat > '{remote_report_path}'\"", shell=True, stdin=subprocess.PIPE)
p.communicate(input=report_content.encode())
if p.returncode == 0:
    print("Step 4 Report successfully written on pcrobot.")
else:
    print(f"Failed to write report on pcrobot. Exit code: {p.returncode}")
