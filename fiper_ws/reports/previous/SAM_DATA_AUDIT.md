# 📊 DATA COLLECTION AUDIT REPORT: SAM NODE (PCROBOTUBUNTU05)

**Audit Date:** Friday, May 22, 2026
**Campaign:** `fiper_sweep_20260522`
**Status:** 🟢 ACTIVE & HEALTHY

---

## 🚀 Execution Overview
Two parallel instances are running on Sam using the `v2` round-robin collector.

| Instance | Focus | PID | CPU Usage | Memory | Log File |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Instance A** | Mug Suites | `3182724` | ~117% | 14.4% | `instance_A.log` |
| **Instance B** | Milk Suites | `3182725` | ~117% | 14.0% | `instance_B.log` |

---

## 📈 Performance Metrics (Real-time)

### Instance A (Mug)
- **Suites:** `libero_spatial_with_mug`, `libero_object_with_mug`, `libero_goal_with_mug`.
- **Episodes Completed:** ~22
- **Success Rate:** **86.4%** (19 Success / 3 Failure)
- **Efficiency:** Average episode duration ~130 steps. 300-step timeouts are correctly pruning failures.

### Instance B (Milk)
- **Suites:** `libero_spatial_with_milk`, `libero_goal_with_milk` (Note: `object_with_milk` is skipping).
- **Episodes Completed:** ~24
- **Success Rate:** **87.5%** (21 Success / 3 Failure)
- **Efficiency:** Higher success rate observed in goal-oriented milk tasks (~70-90 steps).

---

## 🛑 Critical Findings & Issues

### 1. Missing Suite: `libero_object_with_milk`
- **Issue:** The launch script requested `libero_object_with_milk`, but the benchmark dictionary does not contain this suite.
- **Evidence:** `Skipping unavailable libero_object_with_milk_t0: "suite libero_object_with_milk not available"`
- **Analysis:** A query of the Sam benchmark dict reveals the available milk suites are:
  - `libero_goal_with_milk`
  - `libero_spatial_with_milk`
  - `libero_10_with_milk` (The "Object" tasks are likely consolidated here).
- **Impact:** Instance B is currently sweeping only 2 suites instead of 3.

### 2. Data Persistence Check
- **Location:** `/home/rootalkhatib/test/reda_ws/asynchvla_ws/stage9_libero_pro_risk_data/campaigns/fiper_sweep_20260522/`
- **File Structure:** 
  - `fiper_receding_samples.jsonl`: **OK.** Metadata and action/outcome pairs are being appended here.
  - `images/` & `states/`: **EMPTY.** 
  - **Reason:** The `v2` collector is designed to be "Lean Mode". It stores the receding horizon transitions (1st action and outcome) directly in the `.jsonl` file to save disk I/O, rather than dumping thousands of individual `.npz` files per sweep.

---

## 🛠 Recommendations for Next Session

1.  **Fix Instance B Suites:** The next session should restart Instance B with the correct suite name: `libero_10_with_milk` instead of `libero_object_with_milk`.
2.  **Suite Rotation:** Once Sam completes 100 sweeps of Mug/Milk, rotate it to the Object/Env perturbation suites currently assigned to Bob, in case Bob remains blocked.
3.  **Data Sync:** Periodic `rsync` of the `.jsonl` files from Sam to Batman for offline safety analysis.

---
**Audit Conclusion:** Sam is performing optimally with high success rates. The diversity goal is being met through the round-robin logic. Fix the suite name in Instance B to reach full capacity.
