# 🦾 Risk-Aware 4-Worker Config and Smoke Audit Report

**Date:** May 29, 2026  
**Status:** ALL SMOKE TESTS PASSED (4/4 Completed successfully)  
**Full Campaign Launch Status:** NOT LAUNCHED (Stopped as requested)  

---

## 1. Blocker Verification & Resolutions

### Blocker 1: `--seeds-file` Runner Support
*   **Issue:** `run_riskaware_simvla_one_task_v1.py` does not natively support the `--seeds-file` argument.
*   **Resolution:** Option B was successfully implemented. Rather than patching the runner, we generated the four config files with the 1,000 unique seeds embedded directly within the `"seeds"` configuration list. This keeps configuration self-contained and avoids modifications to core runner script logic.

### Blocker 2: Config Files Generation
*   **Issue:** The 4 required risk-aware worker config files did not exist.
*   **Resolution:** The four configuration files were successfully created and distributed across Sam and Bob. The seed lists were copied directly from the seed plans.

### Blocker 3: Fold00 Normalization Sync
*   **Issue:** Fold00 normalization was copied from global, so Fold00 needed a smoke test validation.
*   **Resolution:** Copied `normalization.json` from the global main detector path `00_global_main/jobs/v2_018_transformer_k16` to `fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16/` on both nodes. The smoke tests on Bob validated that both the seen and unseen target object setups successfully loaded normalization parameters, initialized the risk-aware SimVLA models, and completed rollout steps without configuration errors.

---

## 2. Seed Plans and Hash Audit

All seed plan files contain exactly 1,000 unique integer seeds and have 1,002 lines of code.

| File Path | Seeds Count | Line Count | SHA256 Checksum |
|---|---|---|---|
| `realtime_deployment/configs/seed_plans/worker_sam_0_seeds_1000.json` | 1,000 | 1,002 | `a5487dfece5d25cd60595956786fab0b24d292d367149308ce9c91f20a73c8b5` |
| `realtime_deployment/configs/seed_plans/worker_sam_1_seeds_1000.json` | 1,000 | 1,002 | `d50e5865206ed5f9f3d0f17ac618cac4e3d6fc8f70962831521816802fd3b253` |
| `realtime_deployment/configs/seed_plans/worker_bob_0_seeds_1000.json` | 1,000 | 1,002 | `513e62cd203c543cf79495b72379fa1e1cb867b2d2ddc76f93343a0d63808092` |
| `realtime_deployment/configs/seed_plans/worker_bob_1_seeds_1000.json` | 1,000 | 1,002 | `6d569449f52ba36fd53f0e113961f02197bb45445b232be7b70cfddb803aee78` |

---

## 3. Config Paths and Hash Audit

Configs embedded the 1,000 seed plans directly under `"seeds"`.

| File Path | Machine | SHA256 Checksum |
|---|---|---|
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_seen_task7_20260529.json` | Sam | `e5ecd071d6368f6d7d99e3b4ffdbdc2675b1deb730aab65dfb90babaff4a0807` |
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_ood_task8_20260529.json` | Sam | `7f62844c2b2b8d9cb671ad284cc7a57b88633811bf8b183b06b66115ca417a6c` |
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_seen_butter_task2_20260529.json` | Bob | `e2c22991e5ea3ede54ecca6ec5b98686adb50d6182e72cdf72828b2ef38d34f6` |
| `realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json` | Bob | `9bf2df0531e0aea5023f6cd134cffc0c88e3e47138ced6329316567a5beb5221` |

---

## 4. Detector Path and Thresholds Audit

The correct detectors and conformal risk threshold quantiles were loaded and utilized for each worker:

### Sam Worker 0: `worker_sam_0_seen_hard_control`
*   **Detector Dir:** `experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16`
*   **q95 Row Threshold:** `0.4610767066478729` (Expected: ~0.4611)
*   **q99 Row Threshold:** `0.9912812113761902` (Expected: ~0.9913)

### Sam Worker 1: `worker_sam_1_ood_task_id`
*   **Detector Dir:** `experiments/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16`
*   **q95 Row Threshold:** `0.4851045608520508` (Expected: ~0.4851)
*   **q99 Row Threshold:** `0.9277384877204895` (Expected: ~0.9277)

### Bob Worker 0: `worker_bob_0_fold00_seen_butter_task2`
*   **Detector Dir:** `experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16`
*   **q95 Row Threshold:** `0.5132626295089722` (Expected: ~0.5133)
*   **q99 Row Threshold:** `0.9693111777305603` (Expected: ~0.9693)

### Bob Worker 1: `worker_bob_1_fold00_unseen_alphabet_soup_task0`
*   **Detector Dir:** `experiments/current_baseline_v2_018_20260528/fold_00_holdout_alphabet_soup_bbq_sauce/jobs/v2_018_transformer_k16`
*   **q95 Row Threshold:** `0.5132626295089722` (Expected: ~0.5133)
*   **q99 Row Threshold:** `0.9693111777305603` (Expected: ~0.9693)

---

## 5. Smoke Result Table

All runs had **zero** seed collisions and **zero** main seed collisions with ACE candidates. All action seeds are unique at every single timestep.

| Machine | Worker Name | Suite | Task ID | First Reset Seed | Outcome | Num Steps | Wall Time (s) | Action Mods Count | First Mod Timestep | Step Score Line Count | Seed Collisions |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sam** | `worker_sam_0_seen_hard_control` | `libero_10_with_milk` | 7 | `444349652` | success | 286 | 523.65 | 26 | 122 | 286 | 0 |
| **Sam** | `worker_sam_1_ood_task_id` | `libero_10_with_milk` | 8 | `1587198020` | success | 232 | 245.72 | 1 | 200 | 232 | 0 |
| **Bob** | `worker_bob_0_fold00_seen_butter_task2` | `libero_object_with_mug` | 2 | `2136803351` | success | 202 | 376.85 | 1 | 131 | 202 | 0 |
| **Bob** | `worker_bob_1_fold00_unseen_alphabet_soup_task0` | `libero_object_with_mug` | 0 | `537593528` | failure_or_timeout | 300 | 331.23 | 33 | 158 | 300 | 0 |

---

## 6. Campaign Readiness Confirmation

*   **Deduplication & Execution:** Duplicate execution processes on Bob for `bob1_smoke` were cleanly terminated and the output directory purged before starting a single clean rollout. Output files are fully validated and consistent.
*   **Policy Name Check:** Configs and runs successfully executed using policy `risk_filtered_lowest_score_candidate_v2_strict_margin` under risk-aware modification controls.
*   **Launch Prevention:** No further episodes have been scheduled. The full multi-day campaign of 1,000 episodes per worker is **NOT launched** yet. We are awaiting explicit instruction from the user.
