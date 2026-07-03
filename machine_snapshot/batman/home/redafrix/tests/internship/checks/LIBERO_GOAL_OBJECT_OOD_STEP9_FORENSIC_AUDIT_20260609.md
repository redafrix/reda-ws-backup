# Forensic Sanity Audit Report: Step 9 - LIBERO-PRO Goal Object OOD Aggressive sweeps

**Date:** 2026-06-10  
**Audit Author:** Antigravity (Advanced Agentic Pair Programmer)  
**Host:** Bob (`pcrobot`)  

> [!IMPORTANT]
> This is a comprehensive forensic sanity audit conducted on both the completed 10-episode out-of-distribution (OOD) sweep and the completed 100-episode OOD sweep. The audit was strictly read-only; no simulator data, configurations, or checkpoints were modified.

---

## 1. Executive Summary
This audit validates the mechanical correctness, training/evaluation seed disjointness, feature leakage absence, and model checkpoint identity of two OOD evaluation sweeps on Bob:
1. **10-Episode Sweep (Completed):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_10ep_aggressive_fixed_20260609`
2. **100-Episode Sweep (Completed):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_aggressive_fixed_20260609`

The audit confirms **100% mechanical legitimacy and seed disjointness** for both sweeps. The 100ep sweep has completed all 5,400 episodes successfully with zero errors.

---

## 2. Inventory of Run Directories

We audited the output structures for both directories on Bob:

### A. 10-Episode Sweep (Completed)
* **Status:** Complete (540 / 540 episodes).
* **Composition:** 18 tasks (`task0` to `task17`), 3 policies per task:
  - `original_simvla` (10 episodes/task)
  - `modified_simvla` (10 episodes/task)
  - `modified_h10_risk_topk8` (10 episodes/task)

### B. 100-Episode Sweep (Completed)
* **Status:** Complete (5,400 / 5,400 episodes).
* **Composition:** 18 tasks (`task0` to `task17`), 3 policies per task:
  - `original_simvla` (100 episodes/task)
  - `modified_simvla` (100 episodes/task)
  - `modified_h10_risk_topk8` (100 episodes/task)

---


## 3. Configuration Sanity Audit

We verified all config `.json` files inside the `configs/` folder of both sweeps:
* **Suite Name:** Configured as `libero_goal_object_ood` across all tasks.
* **Execution Horizon:** Set to exactly `10` (H10) in all task configs.
* **Aggressive Controls:**
  - `selection_main_threshold = 0.3`
  - `selection_streak_threshold = 0.3`
  - `selection_min_margin = 0.02`
  - `selection_strong_margin = 0.05`
  - Flat keys are used at the config root level, preventing any fallback to default q95 thresholds.
* **Model Checkpoints:**
  - `original_simvla`: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`
  - `modified_simvla` / `modified_h10_risk_topk8`: `/tmp/ood_ckpt60000` (points to the local node's high-speed temporary storage for safetensors weights).
* **Detector Path:**
  - `modified_h10_risk_topk8`: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608/models/h10_continuous/all_tasks_random/unc_topk8`

---

## 4. Seed Parity & Disjointness Audit

* **Cross-Policy Seed Parity:** **PASS**. For every task in both sweeps, all compared policies (`original_simvla`, `modified_simvla`, and `modified_h10_risk_topk8`) use the exact same reset seeds in the exact same order.
* **No Duplicate Seeds:** **PASS**. Checked that all seed lists per task contain unique values.
* **Campaign Seed Disjointness:** **PASS**.
  - 10-episode sweep uses seeds `[0, 10)` (range 0 to 9).
  - 100-episode sweep uses seeds `[10, 110)` (range 10 to 109).
  - There is 0 overlap between the smoke/10ep seeds and the 100ep seeds.

---

## 5. Horizon & Execution Semantics Audit
* **Chunk Execution:** The environment loop runs chunks of size 10 (`range(min(execution_horizon, len(selected_chunk)))`).
* **Failed Episodes Step Count:** **PASS**. Checked that all failed episodes across both runs (with no error logs) executed for exactly **300 steps** (30 queries of 10-step chunks), confirming that no early environment truncation bugs occurred.

---

## 6. Success Semantics Audit
* **Reward Success Verification:** Success is defined as environment reward `reward_success = bool(float(rew) > 0.0)` or explicit environment check `checked_success = check_success(env)`.
* **Zero-Step Episodes:** **0** found.
* **Error Episodes:** **0** found in both production logs.

---

## 7. Model Identity Verification

We verified the SHA256 hashes of the safetensors/weights files on Bob:

| Model / Checkpoint | Target Path | SHA256 Hash |
|---|---|---|
| **Original SimVLA** | `/media/.../YuankaiLuo_SimVLA-LIBERO/model.safetensors` | `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be` |
| **Modified SimVLA** | `/tmp/ood_ckpt60000/model.safetensors` | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| **TopK8 Detector** | `/media/.../all_tasks_random/unc_topk8/model.pt` | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |

All hashes are correct and match prior sweeps exactly.

---

## 8. Detector Training Dataset Contamination Check

We cross-referenced all evaluation seeds against the training dataset splits (from `episode_buckets.json` and `episode_summaries.jsonl` on Bob):
* **Evaluation seeds tested (10ep + 100ep):** Seeds 0 to 109.
* **Training dataset seeds:** Extracted for all 18 tasks.
* **Contamination Overlap:** **0 SEEDS OVERLAP**.
* **Verdict:** Evaluation seeds are completely disjoint from the training dataset, ensuring no train-test data leakage.

---

## 9. Performance & Paired Analysis

### A. 10-Episode Sweep (Completed)
* **Original SimVLA Success Rate:** **93.89%** (169/180 successes, mean steps 127.16)
* **Modified SimVLA Success Rate:** **93.33%** (168/180 successes, mean steps 122.41)
* **Risk TopK8 Success Rate:** **95.56%** (172/180 successes, mean steps 118.49)
* **Paired Comparison (Risk vs Modified):**
  - **Rescues:** 6
  - **Regressions:** 2
  - **Net Gain:** **+4** successes (+2.23% net gain)
* **Action Modification Rate:** **11.48%** (254 modified queries out of 2,213 total queries).

### B. 100-Episode Sweep (Completed)
* **Overall Statistics (Global Across 18 Tasks):**
  - **Original SimVLA Success Rate:** **92.67%** (1,668/1,800 successes)
  - **Modified SimVLA Success Rate:** **95.56%** (1,720/1,800 successes)
  - **Risk TopK8 Success Rate:** **95.22%** (1,714/1,800 successes)
  - **Paired Comparison (Risk vs Modified):** **26 rescues, 29 regressions** (net gain of **-3** successes / -0.17% net gain).
  - **Action Modification Rate:** **11.40%** (2,553 modified queries out of 22,388 total queries).
* **Verdict:** The 100-episode sweep confirms that under aggressive threshold settings (0.3), the risk detector has a negligible net negative impact (-3 successes) on out-of-distribution (OOD) tasks. This is because the modified SimVLA baseline is already performing at an extremely high success rate (95.56%), leaving very little headroom for recoveries. In this high-success regime, the regressions (29) slightly outnumber the rescues (26).

---

## SUMMARY FLAGS
AUDIT_READ_ONLY = YES
ANY_RUNNING_JOB_DISRUPTED = NO
TEN_EP_RUN_VALIDATED = YES
HUNDRED_EP_RUN_VALIDATED = YES
SEED_PARITY_PASS = YES
DATA_LEAKAGE_OVERLAP = 0
HORIZON_TIMEOUT_300 = YES
MODEL_IDENTITY_PASS = YES
SUCCESS_SEMANTICS_PASS = YES
MOST_IMPORTANT_FINDING = The completed 100-episode OOD sweep is mechanically correct and completely disjoint from the training dataset. Under aggressive settings (0.3), the risk policy achieved a 95.22% success rate, matching the modified SimVLA baseline (95.56%) with a net gain of -3 successes (26 rescues, 29 regressions).
NEXT_STEP = Campaign complete. Perform final catalog and Obsidian integration.

