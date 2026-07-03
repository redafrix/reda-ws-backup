import os
import subprocess

synthesis_report = """# H10 Risk-Aware SimVLA Forensic Synthesis Report

> [!IMPORTANT]
> This is the final forensic synthesis report summarizing the results of the multi-step sanity audit conducted on H10 risk-aware SimVLA simulation results on host **pcrobot**. The audit was strictly read-only; no code, configuration, or raw simulation files were modified.

---

## 1. Mechanical Trustworthiness of Results

We evaluated the mechanical setup, file integrity, seed parity, and log correctness across all campaigns.

* **Task 3 Aggressive TopK8:** **TRUSTWORTHY.** Ran to completion (100 episodes). It has perfect seed parity with the baseline, correct H10 execution horizon semantics, correct success definition, and clean, non-duplicated JSONL outputs.
* **Task 6 Aggressive TopK8:** **TRUSTWORTHY.** Ran to completion (100 episodes). It shares identical seed alignment with the baseline and exhibits correct environment execution and clean JSONL logs.
* **Task 6 Old-Detector Aggressive:** **TRUSTWORTHY.** Ran to completion (100 episodes) with correct seed parity, clean logs, and correct execution paths.
* **OOD Goal-Swap Production:** **TRUSTWORTHY.** All 900 episodes across 3 tasks (100 per policy per task) completed successfully. Seeds matched perfectly between baseline, modified, and risk policies. The logs are clean.
* **Main Campaign Task 8 Incomplete Runs:** **NOT TRUSTWORTHY.** These runs were killed prematurely by a `KeyboardInterrupt` propagated from the supervisor, leaving only 5/100 completed episodes for `modified_simvla` and 2/100 completed episodes for `modified_h10_risk_topk8`. No scientific conclusions can be drawn from these runs.

---

## 2. Scientific Strength vs. Weakness

Our audit evaluated the scientific setup of the in-distribution and OOD experiments:

* **Seen Tasks vs. Unseen Seeds (Task-Level Overlap):** **WEAK.** The detector was trained on a split (`continuous_chunk10_flat`) that explicitly included **1,368 episodes of Task 3** and **1,423 episodes of Task 6**. Consequently, the evaluations on Tasks 3 and 6 represent **in-distribution** performance (evaluating seen tasks on unseen seeds), not zero-shot generalization. The model had already memorized task contexts and visual layouts.
* **Init-State Overlap:** **WEAK.** LIBERO has only 10 fixed initial state configurations (indices 0-9) per task. Both detector training and online testing reset the environment to this same pool, meaning the starting physical configurations (spatial placements and orientations) are identical in distribution.
* **No Seed Leakage:** **STRONG.** Evaluation seeds (100 per task) share **0% overlap** with any seeds used during detector training, validation, or calibration.
* **Feature Leakage Audit:** **STRONG.** Pass. No future information, simulator object positions, success flags, or rewards are leaked to the feature vector at runtime. Excluded fields are correctly omitted.
* **H10 Execution Audit:** **STRONG.** Pass. Chunk execution correctly runs 10 steps of the selected chunk, early stopping is correct.
* **Raw JSONL Pairing Audit:** **STRONG.** Pass. After correcting a template compilation bug in Step 2, the bottom-up recomputation directly from the JSONLs confirms that the pairing is mathematically sound and the intersection between rescues and regressions is strictly empty.

---

## 3. What the Risk-Aware Layer Improved

Under the aggressive threshold of `0.3` (where candidate replacement occurs whenever the main chunk risk exceeds `0.3`), the paired counts show:

* **Task 3 Aggressive TopK8:** Succeeded in rescuing **2** failing episodes and caused **0** regressions, achieving a net gain of **+2** successes (17/100 baseline -> 19/100 risk).
* **Task 6 New TopK8:** Rescued **19** failing episodes but caused **14** regressions, achieving a net gain of **+5** successes (57/100 baseline -> 62/100 risk).
* **Task 6 Old Detector:** Rescued **13** failing episodes but caused **10** regressions, achieving a net gain of **+3** successes (57/100 baseline -> 60/100 risk).
* **OOD Goal-Swap:** Rescued **2** failing episodes but caused **4** regressions, achieving a net loss of **-2** successes (8/300 baseline -> 6/300 risk across all three tasks).

---

## 4. What is Broken or Weak

Our deep analysis of query logs and threshold sensitivity reveals critical weaknesses:

* **Aggressive TopK8 is Overactive:** At threshold `0.3`, the detector intervenes on **94.7%** (new TopK8 Task 6) and **98.9%** (new TopK8 Task 3) of queries. It is essentially running a brute-force replacement search at every single step rather than surgical safety intervention.
* **Regressions are Real:** Because the detector is overactive, it constantly replaces safe baseline trajectories with candidate chunks that fail, leading to **14 regressions** in Task 6.
* **Detector Predicts Risk, Not Recoverability:** The detector only models if the main chunk will fail, not if the alternative will succeed. When an episode is on a failing path, the baseline risk is very high (mean risk in regressions is **0.8162**), and the selected candidate risk remains extremely high (**0.8012**). These replacement actions still lead to failure.
* **Threshold Tuning Alone is Insufficient:** Raising the threshold to `0.4`, `0.5`, or `0.6155` does **NOT** prevent any of the 14 regressions (all reached a max baseline risk above `0.99`). However, raising it to `0.6155` causes 3 rescues to be lost, dropping the net gain to **+2**.
* **OOD Goal-Swap Failed Badly:** Out of 300 OOD episodes, the detector intervened aggressively (up to 100% of episodes in `cream_cheese_bowl`) on tasks the base policy simply could not solve, causing "panic interventions" with zero success and a net loss of -2.
* **Full-Suite Goal-Swap Was Not Run:** Verification was restricted to Tasks 3, 6, and 8, meaning full-suite generalization was never demonstrated.

---

## 5. Proposed Next Experiments

We propose two minimal experiments to resolve outstanding questions:

### Experiment 1: Random Candidate Selection (RCS) Ablation
* **Purpose:** Determine if the success rate boost (+5% in Task 6) is driven by the detector's risk guidance or simply by candidate sampling diversity (trying 8 alternative chunks).
* **Task/Suite:** `libero_goal_object` Task 6.
* **Policies:** Baseline `modified_simvla`, Aggressive TopK8 risk-aware, and Random Candidate Selection (RCS).
* **Seeds/Episodes:** Same 100 seeds from Task 6.
* **Execution:** If `main_score >= 0.3`, instead of choosing the candidate with the lowest detector risk, select one of the 8 candidate chunks at random and execute it.
* **Expected Evidence:** If the RCS success rate is close to 62%, the detector's guidance is not helping (brute-force sampling dominance). If it drops to 57% or below, the detector's risk guidance provides a real filtering effect.
* **Why cheap/clean:** Reuses the exact same simulation infrastructure and seeds, requiring only a simple change to the selection logic in `run_policy_matrix.py` (no training, only 100 episodes).

### Experiment 2: Zero-Shot Generalization General Task Audit
* **Purpose:** Verify true zero-shot generalization of the risk detector on held-out tasks that were completely unseen during training.
* **Task/Suite:** `libero_goal_object` Tasks 8 and 9.
* **Policies:** Baseline `modified_simvla` vs Risk-aware TopK8 using a detector trained on a held-out split like `ood_last2_taskids_full` (where Tasks 8 and 9 were excluded from training).
* **Seeds/Episodes:** 100 seeds per task (unseen during training and evaluation).
* **Expected Evidence:** Positive net gain (rescues > regressions) on unseen tasks, showing the detector has learned task-agnostic risk representations.
* **Why cheap/clean:** Verifies the zero-shot capability on unseen tasks using existing models and files without needing to retrain new policies.

---

## 6. Final Verdict

**Verdict:** **RESULTS_MECHANICALLY_VALID_BUT_WEAK**

* **Rationale:** The raw simulation execution and evaluations are mechanically correct, and the pairing analysis is sound. However, the scientific value is weak: the tests represent in-distribution performance on seen tasks rather than generalization, the threshold of 0.3 is overactive (acting as a brute-force replacer), and OOD goal-swap tests failed completely.

---

## 7. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
MECHANICAL_VALIDITY_VERDICT = VALID
SCIENTIFIC_STRENGTH_VERDICT = WEAK
FEATURE_LEAKAGE_FOUND = NO
SEED_LEAKAGE_FOUND = NO
PAIRING_BUG_FIXED = YES
OOD_GOAL_SWAP_VERDICT = FAIL
MAIN_TASK8_VERDICT = INCOMPLETE
FINAL_VERDICT = RESULTS_MECHANICALLY_VALID_BUT_WEAK
BEST_NEXT_EXPERIMENT = Run a Random Candidate Selection (RCS) ablation on Task 6 to test if the improvement is just due to sampling diversity.
DO_NOT_CLAIM = Do not claim zero-shot generalization, do not claim that raising the threshold solves regressions, and do not claim risk-aware improvements on OOD goal-swap tasks.
"""

# Write locally
local_path = "/home/redafrix/tests/internship/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md"
with open(local_path, "w") as f:
    f.write(synthesis_report)
print(f"Synthesis Report written locally to {local_path}")

# Write to pcrobot
remote_path = "/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md"
print("Uploading Synthesis Report to pcrobot...")
p = subprocess.Popen(f"ssh pcrobot \"cat > '{remote_path}'\"", shell=True, stdin=subprocess.PIPE)
p.communicate(input=synthesis_report.encode())
if p.returncode == 0:
    print("Synthesis Report successfully written on pcrobot.")
else:
    print(f"Failed to write report on pcrobot. Exit code: {p.returncode}")

