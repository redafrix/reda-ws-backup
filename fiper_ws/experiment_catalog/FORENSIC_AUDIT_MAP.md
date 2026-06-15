# Forensic Audit Map

This map outlines the 8-step forensic sanity audit conducted on host **pcrobot** (Bob) for the H10 risk-aware SimVLA simulation results.

---

### Step 1: Sanity Audit
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md`
* **What it Checked:** File structure integrity, process logs, supervisor behavior, execution horizons, and exit codes across Task 3/6 aggressive campaigns and Task 8 runs.
* **Final Verdict:** **PASS (Mechanically Sound)** for Task 3/6 aggressive and Old Detector; **FAIL (Incomplete)** for Task 8 runs (killed by `KeyboardInterrupt`).

---

### Step 2: Data & Leakage Investigation
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP2_DATA_AND_LEAKAGE_20260609.md`
* **What it Checked:** Training dataset provenance, split details, seen-task overlaps, evaluation seed disjointness, feature leakage, candidate generation fairness, and log alignment.
* **Final Verdict:** **PARTIAL_TRUST**. Verified 0% seed leakage and correct candidate generation fairness (fair main-chunk fix). However, noted task-level overlap: Tasks 3 and 6 were seen during detector training, making evaluations in-distribution.
* **Known Corrections / Bugs:** Contains a compiler bug check where the generated list of Task 6 aggressive rescues and regressions had seed overlaps due to manual hardcoding template errors. (Corrected in Step 3).

---

### Step 3: Pairing Bugcheck
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP3_PAIRING_BUGCHECK_20260609.md`
* **What it Checked:** Verified the paired comparison logic bottom-up from raw JSONL files. Investigated why some seeds appeared in both the rescue and regression lists in the Step 2 report.
* **Final Verdict:** **VALID**. Confirmed the raw JSONL files are clean with no duplicates or stale entries. Recomputed the exact paired lists, proving the rescue and regression seed sets are strictly disjoint.
* **Known Corrections / Bugs:** Diagnosed the Step 2 report seed list overlap as a manual template copy-paste error. Provided the corrected disjoint lists of rescues and regressions.

---

### Step 4: Risk Score Effect
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP4_RISK_SCORE_EFFECT_20260609.md`
* **What it Checked:** Investigated if the success rate boost was due to genuine risk guidance or random candidate sampling. Sweep of alternate decision policies.
* **Final Verdict:** **WEAK_DETECTOR_EFFECT**. Analyzed risk scores: baseline risk on regressions was extremely high (mean 0.816) and chosen candidates also had very high risk (mean 0.801), indicating the detector predicts risk but does not guarantee the alternative is safe. Proposed a Random Candidate Selection (RCS) ablation to isolate the detector's filtering effect.

---

### Step 5: Synthesis Report
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SYNTHESIS_20260609.md`
* **What it Checked:** Combined findings from Steps 1-4 and OOD goal-swap reports to render a final verdict on campaign trustworthiness and propose next steps.
* **Final Verdict:** **RESULTS_MECHANICALLY_VALID_BUT_WEAK**. Scientific value is weak due to task overlap, high regression rate, and OOD goal-swap failure.
* **Known Corrections / Bugs:** Confused the gating threshold exceedance rate (98.9% for Task 3) with the actual query-level modification rate (which is 1.04%). (Corrected in Step 6).

---

### Step 6: Threshold & Gating Audit
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP6_THRESHOLD_GATE_AUDIT_20260609.md`
* **What it Checked:** Investigated the suspicious 98.9% intervention rate claim. Swept alternative gating rules (selected risk cap, min risk reduction, delayed intervention) on query logs to separate rescues from regressions.
* **Final Verdict:** **VALID**. Recomputed the true query modification rates (1.04% for Task 3, 22.98% for Task 6). Recommended testing a selected risk cap (`selected_risk <= 0.4`) and delayed intervention (`query_index >= 2`) to prevent regressions.

---

### Step 7: Model Identity and Policy-Label Correctness
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP7_MODEL_IDENTITY_20260609.md`
* **What it Checked:** Verified checkpoint weights, configs, hashes, and run log parameters to prove that each policy loaded the correct model backbone and risk detector.
* **Final Verdict:** **PASS**. Confirmed original SimVLA and modified SimVLA (`ckpt-60000`) are distinct (modified weights are 28.9 KB larger and hashes are distinct). Verified that all 60 configs and runs had 0 policy-label or checkpoint crossovers.

---

### Step 8: LIBERO-PRO Suite, Task, and Asset Identity
* **Local Path:** [/home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md](file:///home/redafrix/tests/internship/checks/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP8_LIBERO_PRO_SUITE_IDENTITY_20260609.md`
* **What it Checked:** Verified task suites, BDDL files, and initial states files using the benchmark registry API and file diffs. Checked for silent fallbacks.
* **Final Verdict:** **PASS**. Confirmed that in-distribution runs used `libero_goal_object` (LIBERO-PRO object perturbations) and OOD runs used `libero_goal_swap` (initial placement swap). Proved zero fallback risk (raises FileNotFoundError instead of silent fallback).

---

### Step 9: LIBERO-PRO Goal-Object-OOD Sweep Audit
* **Local Path:** [/home/redafrix/tests/internship/checks/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_20260609.md](file:///home/redafrix/tests/internship/checks/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_20260609.md)
* **Bob Path:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports/LIBERO_GOAL_OBJECT_OOD_STEP9_FORENSIC_AUDIT_20260609.md`
* **What it Checked:** Verified the completed 10-episode aggressive-fixed OOD run (540 episodes total, 18 tasks, 3 policies) and the currently running 100-episode aggressive-fixed OOD sweep on Bob.
* **Final Verdict:** **PASS (Mechanically Sound & Seed Disjoint)**. Confirmed both runs use correct aggressive threshold parameters (selection thresholds = 0.3), correct Safetensors model check-sums, and evaluation seeds are completely clean of train-set contamination.


