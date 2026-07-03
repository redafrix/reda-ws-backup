# Obsidian Report Accuracy Audit - 2026-06-09

This document audits the claims made in the main Obsidian Vault report:
[FIPER Risk-Aware SimVLA - Full Report.md](file:///home/redafrix/Documents/Obsidian%20Vault/FIPER%20Risk-Aware%20Report%2020260602/FIPER%20Risk-Aware%20SimVLA%20-%20Full%20Report.md)
against the latest verified campaign results on the machines.

---

### 1. Claim: Task 3 query intervention rate is 98.9%
* **Section / Context:** Section 15 ("Task 3: Pick and Place Results (N=100)") and Section 8 ("Intervention Burden Versus Gain").
* **Verdict:** **WRONG**
* **Obsidian Claim:** Section 15 states "Total Mods: 29" for Task 3 aggressive, but does not explicitly print 98.9%. However, the Synthesis report (upon which these summaries are based) confused the gating threshold rate (percentage of queries where risk score exceeded 0.3, which is 98.88%) with the actual modification rate.
* **Correction:** The actual query-level modification rate for Task 3 aggressive TopK8 is only **1.04%** (29 modifications out of 2,776 queries). The policy rejected candidate replacement for 98.9% of queries because alternative chunks did not offer the required margin of improvement (T >= 0.05). The episode-level modification rate (episodes with at least one mod) is **14.0%** (14 out of 100).
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md#L10-L18)

---

### 2. Claim: OOD goal-swap results were positive
* **Section / Context:** Not mentioned in the Obsidian report (entirely absent from the Full Report).
* **Verdict:** **OUTDATED / WRONG**
* **Obsidian Claim:** The Obsidian report was written prior to the OOD goal-swap campaign (June 8, 2026) and therefore lists no results for it. The only OOD results listed are for Task 8 (+0.7 pts delta) and alphabet soup (+0.7 pts delta) from the older pre-H10 campaign.
* **Correction:** The production OOD goal-swap campaign on Bob (June 8, 2026) was **net negative**. Over 300 total episodes (100 per policy per task), the risk-aware TopK8 policy achieved a net loss of **-2** successes (8/300 baseline -> 6/300 risk) due to "panic interventions" on unsolvable swapped configurations.
* **Citation / Verified Path:** [OOD_GOAL_SWAP_FINAL_PAIRED_ANALYSIS_20260609.md](file:///home/redafrix/tests/internship/checks/OOD_GOAL_SWAP_FINAL_PAIRED_ANALYSIS_20260609.md) and [H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md#L40-L41)

---

### 3. Claim: Zero-shot/generalization was demonstrated from Task 3/6 results
* **Section / Context:** Section 15 ("Task 3: Pick and Place Results (N=100)" and "Task 6: Stacking Results (N=100)") and Section 17 ("Future Work").
* **Verdict:** **WRONG**
* **Obsidian Claim:** The report presents Tasks 3 and 6 as standard online evaluation benchmarks, implying they prove the effectiveness of the risk-aware layer. It does not explicitly warn that the detector had seen these tasks during training.
* **Correction:** Online evaluations on Tasks 3 and 6 represent **in-distribution** performance (seen tasks on unseen seeds), not zero-shot generalization. The risk detector was explicitly trained on the `continuous_chunk10_flat` dataset, which contained **1,368** episodes of Task 3 and **1,423** episodes of Task 6.
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md#L32-L36)

---

### 4. Claim: Task 8 modified results are complete
* **Section / Context:** Section 8 ("Real-Time Results" table: "libero_10_with_milk/task8 OOD task-id | 429 episodes | +0.7 pts delta").
* **Verdict:** **OUTDATED / WRONG**
* **Obsidian Claim:** Lists Task 8 as completed with 429 episodes and a tiny success delta. This refers to the historical campaign using pre-H10 detectors.
* **Correction:** For the current, specialized H10 campaign on Bob (using the H10-retrained TopK8 detector), the Task 8 modified runs are **incomplete and untrustworthy**. The runs were killed prematurely by a `KeyboardInterrupt` from the supervisor, leaving only 5/100 completed episodes for `modified_simvla` and 2/100 completed episodes for `modified_h10_risk_topk8`. No scientific conclusions should be drawn from them.
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md#L16-L17)

---

### 5. Claim: Full-suite goal-swap was run
* **Section / Context:** Not mentioned in the Obsidian report (absent).
* **Verdict:** **WRONG**
* **Obsidian Claim:** N/A (absent from report).
* **Correction:** Full-suite OOD goal-swap was never run. The OOD goal-swap evaluation was restricted only to Tasks 3, 6, and 8 (100 episodes per policy per task).
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md#L53-L54)

---

### 6. Claim: Model architecture inputs and routing (wrong wording about transformer/static MLP inputs)
* **Section / Context:** Section 12 ("Uncertainty TopK8 Extension"): "The uncertainty dimensions are appended to the current/static feature vector and enter through the static MLP branch."
* **Verdict:** **OK**
* **Obsidian Claim:** Appending uncertainty dimensions to the current/static feature vector of length 43, making it 51, and feeding it to the static branch is structurally correct.
* **Correction:** The statement is accurate. The static branch concatenated proprioception, ACE metrics, action statistics, and the selected 8 uncertainty dimensions into a 51-dimensional vector, which is processed by the static MLP block and joined with the CLS token output from the transformer.
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md#L70-L74)

---

### 7. Claim: Checkpoint and suite identities
* **Section / Context:** Section 12 ("Uncertainty TopK8 Extension") and Section 14 ("Bob H10-Retrained Detectors").
* **Verdict:** **OK**
* **Obsidian Claim:** Mentions that the modified SimVLA checkpoint `ckpt-60000` is used, and the H10 detectors were trained on `continuous_chunk10_flat` data.
* **Correction:** Checkpoint and suite identities are correct. Model identity audits confirm that original runs used the paper SimVLA, modified runs loaded the modified `ckpt-60000` with the uncertainty head, and the suites loaded were exactly `libero_goal_object` (in-distribution) and `libero_goal_swap` (OOD).
* **Citation / Verified Path:** [H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md) and [H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md)
