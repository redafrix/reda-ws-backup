import json
import re

with open("/home/redafrix/tests/internship/audit_results.json", "r") as f:
    data = json.load(f)

# Hardcoded details from earlier audits or computed values
# We know the success rates and steps from audit_results.json

report = """# Forensic Sanity Audit Report: SimVLA Risk-Aware Simulation Results

> [!IMPORTANT]
> This is a formal forensic sanity audit conducted on the simulation campaign results stored on host **pcrobot**. The audit is strictly read-only; no code, configuration, or data files were modified.

## 1. Inventory of Run Directories

We audited the four target directories on `pcrobot` and classified all directories containing `episode_summaries.jsonl`. Production runs have been separated from smoke/online/test runs to ensure analysis integrity.

### A. Production Runs

| Suite | Task ID | Policy | Shard | Completed Episodes | Successes | Failures | Errors | Mean Steps | Outcome |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **libero_goal_object** (Campaign 1) | 3 | original_simvla | shard_0 | 50 | 5 | 45 | 0 | 293.64 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | original_simvla | shard_1 | 50 | 7 | 43 | 0 | 286.52 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | original_h10_risk_base | shard_0 | 50 | 5 | 45 | 0 | 293.64 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | original_h10_risk_base | shard_1 | 50 | 7 | 43 | 0 | 286.64 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | modified_simvla | shard_0 | 50 | 9 | 41 | 0 | 278.06 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | modified_simvla | shard_1 | 50 | 8 | 42 | 0 | 278.14 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | modified_h10_risk_topk8 | shard_0 | 50 | 9 | 41 | 0 | 278.10 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 3 | modified_h10_risk_topk8 | shard_1 | 50 | 8 | 42 | 0 | 278.14 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | original_simvla | shard_0 | 50 | 28 | 22 | 0 | 205.46 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | original_simvla | shard_1 | 50 | 25 | 25 | 0 | 206.54 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | original_h10_risk_base | shard_0 | 50 | 27 | 23 | 0 | 208.06 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | original_h10_risk_base | shard_1 | 50 | 24 | 26 | 0 | 209.08 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | modified_simvla | shard_0 | 50 | 31 | 19 | 0 | 195.96 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | modified_simvla | shard_1 | 50 | 26 | 24 | 0 | 205.58 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | modified_h10_risk_topk8 | shard_0 | 50 | 29 | 21 | 0 | 195.82 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 6 | modified_h10_risk_topk8 | shard_1 | 50 | 28 | 22 | 0 | 200.12 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 8 | original_simvla | shard_0 | 50 | 44 | 6 | 0 | 114.34 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 8 | original_simvla | shard_1 | 50 | 47 | 3 | 0 | 101.30 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 8 | original_h10_risk_base | shard_0 | 50 | 43 | 7 | 0 | 116.60 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 8 | original_h10_risk_base | shard_1 | 50 | 48 | 2 | 0 | 97.24 | COMPLETE |
| **libero_goal_object** (Campaign 1) | 8 | modified_simvla | shard_0 | 3 | 3 | 0 | 0 | 67.67 | **ABORTED** (SIGINT) |
| **libero_goal_object** (Campaign 1) | 8 | modified_simvla | shard_1 | 2 | 2 | 0 | 0 | 125.50 | **ABORTED** (SIGINT) |
| **libero_goal_object** (Campaign 1) | 8 | modified_h10_risk_topk8 | shard_0 | 1 | 1 | 0 | 0 | 73.00 | **ABORTED** (SIGINT) |
| **libero_goal_object** (Campaign 1) | 8 | modified_h10_risk_topk8 | shard_1 | 1 | 1 | 0 | 0 | 72.00 | **ABORTED** (SIGINT) |
| **libero_goal_object** (Campaign 2) | 3 | modified_h10_risk_topk8 | shard_0 | 50 | 10 | 40 | 0 | 276.28 | COMPLETE |
| **libero_goal_object** (Campaign 2) | 3 | modified_h10_risk_topk8 | shard_1 | 50 | 9 | 41 | 0 | 277.10 | COMPLETE |
| **libero_goal_object** (Campaign 2) | 6 | modified_h10_risk_topk8 | shard_0 | 50 | 33 | 17 | 0 | 188.78 | COMPLETE |
| **libero_goal_object** (Campaign 2) | 6 | modified_h10_risk_topk8 | shard_1 | 50 | 29 | 21 | 0 | 192.10 | COMPLETE |
| **libero_goal_object** (Campaign 3) | 6 | modified_h10_risk_topk8 | shard_0 | 50 | 33 | 17 | 0 | 182.62 | COMPLETE |
| **libero_goal_object** (Campaign 3) | 6 | modified_h10_risk_topk8 | shard_1 | 50 | 27 | 23 | 0 | 207.02 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 3 | original_simvla | all | 100 | 15 | 85 | 0 | 289.35 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 3 | modified_simvla | all | 100 | 9 | 91 | 0 | 294.16 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 3 | risk_topk8 (0.3 thresh) | all | 100 | 8 | 92 | 0 | 295.53 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 6 | original_simvla | all | 100 | 0 | 100 | 0 | 300.00 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 6 | modified_simvla | all | 100 | 0 | 100 | 0 | 300.00 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 6 | risk_topk8 (0.3 thresh) | all | 100 | 0 | 100 | 0 | 300.00 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 8 | original_simvla | all | 100 | 1 | 99 | 0 | 299.63 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 8 | modified_simvla | all | 100 | 3 | 97 | 0 | 297.52 | COMPLETE |
| **libero_goal_swap** (Campaign 4) | 8 | risk_topk8 (0.3 thresh) | all | 100 | 2 | 98 | 0 | 298.51 | COMPLETE |

### B. Smoke / Online Smoke / Test Runs (Excluded from conclusions)

| Campaign | Run Directory | Suite | Task ID | Policy | Episodes | Successes | Failures | Errors | Mean Steps |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| Campaign 2 | `runs/online_smoke/task3_aggressive/risk_topk8` | libero_goal_object | 3 | risk_topk8 | 2 | 0 | 1 | 1 | 150.00 |
| Campaign 2 | `runs/online_smoke/task6_aggressive/risk_topk8` | libero_goal_object | 6 | risk_topk8 | 1 | 1 | 0 | 0 | 84.00 |
| Campaign 3 | `runs/online_smoke/task6_aggressive_old_detector/risk_topk8` | libero_goal_object | 6 | risk_topk8 | 1 | 1 | 0 | 0 | 214.00 |
| Campaign 4 | `runs/online/libero_goal_swap/top_drawer_bowl/original_simvla/simvla_only` | libero_goal_swap | 3 | simvla_only | 4 | 0 | 2 | 2 | 150.00 |
| Campaign 4 | `runs/online/libero_goal_swap/top_drawer_bowl/risk_topk8/risk_topk8` | libero_goal_swap | 3 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/top_drawer_bowl/modified_simvla/simvla_only` | libero_goal_swap | 3 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/cream_cheese_bowl/original_simvla/simvla_only` | libero_goal_swap | 6 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/cream_cheese_bowl/modified_simvla/simvla_only` | libero_goal_swap | 6 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/cream_cheese_bowl/risk_topk8/risk_topk8` | libero_goal_swap | 6 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/bowl_on_plate/original_simvla/simvla_only` | libero_goal_swap | 8 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/bowl_on_plate/modified_simvla/simvla_only` | libero_goal_swap | 8 | simvla_only | 2 | 0 | 2 | 0 | 300.00 |
| Campaign 4 | `runs/online/libero_goal_swap/bowl_on_plate/risk_topk8/risk_topk8` | libero_goal_swap | 8 | risk_topk8 | 2 | 0 | 2 | 0 | 300.00 |

---

## 2. Configuration Sanity Audit

We inspected all production config files (`*.json`) to verify settings.

> [!NOTE]
> Config files in Campaign 1 (`h10_goal_object_risk_proof_20260608`) use `selection_main_threshold = "q95"`, while Campaign 2 and Campaign 3 use a hardcoded value `0.3` for aggressive testing.

### Key Config Findings:
1. **Suite & Task IDs:** Properly configured as `libero_goal_object` (Campaigns 1, 2, 3) and `libero_goal_swap` (Campaign 4), mapping correctly to task IDs 3, 6, and 8.
2. **Task Language:** Not explicitly defined in any configuration JSON files (defaulted to `N/A`). BDDL BDDL path mapping handled it dynamically.
3. **Model Checkpoint Paths:**
   - Original SimVLA: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO` (verified SHA256 matches)
   - Modified SimVLA: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/simvla_libero_uncertainty/ckpt-60000` (verified SHA256 matches)
4. **Detector Paths:**
   - New Detector (Campaigns 1, 2, 4): `.../h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`
   - Old Detector (Campaign 3): `.../realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8`
5. **Execution Horizon:** Set to exactly `10` (H10) in all JSON config files.
6. **Thresholds:**
   - Conservative (Campaign 1): `main="q95"`, `streak="q95"` (Conformal thresholds loaded dynamically: q95 is `0.6155` for topk8 and `0.6451` for base model)
   - Aggressive (Campaign 2 & 3): `main=0.3`, `streak=0.3`, margin minimized to `0.02` (main margin) and `0.05` (strong margin).
7. **Seeds:**
   - Reset seed list matches the correct lists (50 reset seeds per shard, summing to 100 seeds).
   - Global/action seed: `global_action_seed` is set to `206080920` (Task 3), `206080923` (Task 6), `206080925` (Task 8) across all policies.
   - Model load seed: `model_load_seed = 206080911` is set globally.
8. **Output Directories:** Matches their respective run path structures.

---

## 3. Seed Parity Audit

We cross-referenced reset seeds across all campaigns.

### Key Parity Findings:
- **Completed runs (Tasks 3 and 6):** **100% PERFECT PARITY**. Across Campaign 1, 2, and 3, all compared policies (`modified_simvla` vs `modified_h10_risk_topk8` vs `original_simvla` etc.) share the exact same seeds in the exact same order.
- **Cross-shard disjointness:** Seeds for `shard_0` and `shard_1` are completely disjoint (as they should be, to cover 100 unique seeds without overlap).
- **Interrupted runs (Task 8):** Cross-policy seed parity is broken because the modified runs were killed early. However, the configured seed lists in the config files match perfectly.
- **Candidate/Action seeds:** The action/candidate seeds (`global_action_seed` and `model_load_seed`) are identical across compared policies, ensuring that SimVLA candidate generation is deterministic and fair.

---

## 4. Horizon and Execution Semantics

We audited the runner code (`run_policy_matrix.py`) and step logs.

> [!TIP]
> The H10 execution horizon works by selecting a 10-action chunk and executing all 10 actions sequentially unless terminated early by success, environment termination (`done`), or reaching the 300 maximum steps.

### Horizon Sanity Checks:
- **Failed Episodes:** For failed episodes, the step count is exactly `300` across all policies, which corresponds to exactly 30 queries of 10 steps each.
- **First-action check:** It is **not** accidentally first-action execution; the loop runs over `range(min(execution_horizon, len(selected_chunk)))`, executing all actions.
- **Consistency:** Baseline and risk-aware policies share the exact same environment loop and horizon settings. Risk-aware only changes candidate chunk selection, not reset or environment semantics.

---

## 5. Success Semantics Audit

We audited how success is parsed and logged.

### Success Sanity Checks:
- **Computation:** Success is defined as `reward_success = bool(float(rew) > 0.0)` or `checked_success = check_success(env)` (which dynamically maps to `env._check_success()` or `env.check_success()`).
- **Safety:** Exceptions or timeouts do not count as success. If an error occurs, `outcome = "error"` is logged, and `success = false` is enforced (via `success: bool(success) and not bool(error_message)`).
- **Stale/Mixed rows:** In the OOD Campaign 4 online test run for `top_drawer_bowl`, two error rows (`KeyError: 'global_action_seed'`) were present along with two rerun rows. This is due to log appending. No error rows or 0-step rows exist in any production runs.

---

## 6. Model Identity Verification

We verified the identity of checkpoints and detectors using SHA256 hashes.

| Model / Checkpoint | Expected Path | Verified File | SHA256 |
| :--- | :--- | :---: | :--- |
| **Original SimVLA** | `checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO` | `model.safetensors` | `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be` |
| **Modified SimVLA** | `checkpoints/simvla_libero_uncertainty/ckpt-60000` | `model.safetensors` | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| **New TopK8 Detector** | `models/h10_continuous/all_tasks_random/unc_topk8` | `model.pt` | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |
| **Old TopK8 Detector** | `dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8` | `model.pt` | `0ea8e9431a67c1096cd4342b78e93766767234db294d4d9f86d10937e6a966c7` |

All paths and hashes match their configurations exactly.

---

## 7. Detector Training and Data Leakage Audit

We audited the detector training dataset mapping and splits.

### Key Data Leakage Findings:
- **Task-Level Inclusion:** Tasks 3, 6, and 8 were **not** held out from the detector training data. The detector was trained on in-distribution data, including Tasks 3, 6, and 8.
  - Task 3 training count: 1309 failure + 59 success = 1368 episodes.
  - Task 6 training count: 653 failure + 770 success = 1423 episodes.
  - Task 8 training count: 106 failure + 1307 success = 1413 episodes.
- **Seed-Level Leakage Check:** We cross-referenced the 100 evaluation seeds of Tasks 3, 6, and 8 against the seeds used in the training, validation, and calibration datasets.
  - **Result: 0 SEEDS OVERLAP**.
  - All evaluation seeds are completely disjoint from the dataset. There is **no seed-level leakage** or train/test contamination.
- **Calibration Thresholds:** Conformal thresholds were verified to match the values inside the model's `thresholds.json` files. They were loaded dynamically by the runner script, not manually overridden.

---

## 8. Aggressive Threshold Audit

We audited Campaign 2 and 3 results (threshold 0.3) against baseline `modified_simvla`.

### Success Counts (from raw JSONL):
- **Task 3 Aggressive TopK8:** **19/100** successes (vs **17/100** baseline).
- **Task 6 Aggressive TopK8:** **62/100** successes (vs **57/100** baseline).
- **Task 6 Old Detector Aggressive:** **60/100** successes (vs **57/100** baseline).

### Paired Comparison (Seed-by-Seed):
1. **Task 3 (New Detector, 0.3 thresh vs baseline):**
   - Rescues (Base=Fail, Risk=Success): **2**
   - Regressions (Base=Success, Risk=Fail): **0**
   - Both Success: 17
   - Both Failure: 81
   - Net change: **+2**
2. **Task 6 (New Detector, 0.3 thresh vs baseline):**
   - Rescues (Base=Fail, Risk=Success): **19**
   - Regressions (Base=Success, Risk=Fail): **14**
   - Both Success: 43
   - Both Failure: 24
   - Net change: **+5**
3. **Task 6 (Old Detector, 0.3 thresh vs baseline):**
   - Rescues (Base=Fail, Risk=Success): **13**
   - Regressions (Base=Success, Risk=Fail): **10**
   - Both Success: 47
   - Both Failure: 30
   - Net change: **+3**

> [!WARNING]
> **Intervention Tradeoff:**
> - To achieve the +5% success rate improvement in Task 6, the policy intervened in **94% of episodes**, triggering **443 total modifications** (avg 4.43 per episode).
> - In contrast, the conservative `q95` threshold only intervened in 40% of episodes (53 total modifications) but yielded no success rate improvement.
> - The old detector was less efficient: it intervened in **99% of episodes** (606 total modifications, avg 6.06 per episode) to yield a +3% success improvement.

### Success-Only Step Metrics:
- **Task 3:** Success-only mean steps **increased** from 171.18 (baseline) to 177.32 (aggressive). Success-only efficiency did *not* improve; only all-episode mean steps improved slightly (278.10 to 276.69) because 2 failures became successes.
- **Task 6:** Success-only mean steps **improved** from 125.90 (baseline) to 123.29 (aggressive). The old detector success-only steps were 124.70.

---

## 9. Suspicious Findings

We scanned the directories and process tables for issues.

### Critical Sanity Issues:
1. **Incomplete Task 8 Production Runs:**
   - Modified policies in Campaign 1 were interrupted early.
   - `modified_simvla` only has 5/100 completed episodes.
   - `modified_h10_risk_topk8` only has 2/100 completed episodes.
   - Logs show a `KeyboardInterrupt` propagated from the supervisor, shutting down the run prematurely.
2. **Stale/Mixed JSONL Outputs:**
   - Campaign 4's online test run for `top_drawer_bowl` has 4 rows (2 error rows + 2 rerun failure rows) in `episode_summaries.jsonl` due to log appending after a `KeyError: 'global_action_seed'`.
   - Production runs are clean and do not contain stale/duplicate rows.

---

## 10. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
MAIN_H10_RESULTS_TRUSTWORTHY = NO
AGGRESSIVE_TASK3_TRUSTWORTHY = YES
AGGRESSIVE_TASK6_TRUSTWORTHY = YES
SEED_PARITY_PASS = YES
H10_EXECUTION_PASS = YES
MODEL_IDENTITY_PASS = YES
SUCCESS_SEMANTICS_PASS = YES
TRAIN_TEST_LEAKAGE_RISK = LOW
MOST_SUSPICIOUS_FINDING = Task 8 runs in the main campaign were interrupted early by a KeyboardInterrupt, leaving modified policies with only 1-3 completed episodes.
NEXT_AUDIT_STEP = Restart and complete the modified policies for Task 8 in Campaign 1 to get a trustworthy main campaign result.
"""

# Write local copy
with open("/home/redafrix/tests/internship/H10_RISK_AWARE_FORENSIC_SANITY_AUDIT_STEP1_20260609.md", "w") as f:
    f.write(report)

print("Report compiled locally.")
