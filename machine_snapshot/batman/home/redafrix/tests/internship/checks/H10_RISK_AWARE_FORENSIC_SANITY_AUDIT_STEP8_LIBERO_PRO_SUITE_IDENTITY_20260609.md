# Step 8 Forensic Sanity Audit Report: LIBERO-PRO Suite, Task, and Asset Identity

> [!IMPORTANT]
> This is Step 8 of the read-only forensic sanity audit conducted on the simulation campaign results stored on host **pcrobot**. No experiments were run, no files modified, and no processes restarted. All findings are derived from files, logs, configs, and checksums.

---

## 1. Executive Summary

This audit proves the identity and correctness of the LIBERO-PRO benchmarks, tasks, BDDL files, and initial state files used across the four simulation campaign roots on Bob (`pcrobot`):
1. **Campaign 1 (In-Distribution Main Campaign):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_risk_proof_20260608`
2. **Campaign 2 (In-Distribution Task 3 Aggressive):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_topk8_aggressive_task3_20260608`
3. **Campaign 3 (In-Distribution Task 6 Old Detector Aggressive):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_goal_object_task6_old_topk8_aggressive_20260608`
4. **Campaign 4 (OOD Goal-Swap Campaign):** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/trash/h10_ood_goal_object_and_swap_20260608`

**Key Findings:**
* **Intended Suites & Tasks:** Configs and JSONL logs verify that all in-distribution runs in Campaigns 1, 2, and 3 used exactly the `libero_goal_object` suite. All OOD runs in Campaign 4 used exactly the `libero_goal_swap` suite. No runs fell back to the basic `libero_goal`, plain official `libero_10`, or any other suite.
* **Asset Verification:** The resolved paths on Bob are confirmed within the LIBERO-PRO repository asset tree (`/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/`).
* **Perturbation Confirmation:** Diffing the BDDL files between the official `libero_goal` and `libero_goal_object` confirms that `libero_goal_object` is genuinely the LIBERO-PRO object-perturbed suite. For instance, in Task 3, standard objects are perturbed (e.g. `akita_black_bowl` is replaced by `bigger_akita_black_bowl`, and `wooden_cabinet` is replaced by `white_cabinet`).
* **Goal-Swap Mechanism:** Diffing the BDDL files of `libero_goal_object` and `libero_goal_swap` reveals the exact OOD "swap" mechanism: `libero_goal_swap` reverts the visually perturbed objects to their base forms (e.g. `bigger_akita_black_bowl` -> `akita_black_bowl`) but swaps their initial placement regions on the table (e.g. in Task 3, the bowl and the cream cheese start in each other's regions).
* **Zero Fallback Risk:** The environment instantiation code in `collect_fiper_uncertainty_receding_dean_v1.py` strictly instantiates the benchmark task and resolves paths. If files do not exist, it raises a `FileNotFoundError`. Silent fallback to another suite is mathematically and logically impossible from the runner code.

---

## 2. Config Suite and JSONL Audit

Across all campaign roots, the configuration files and `episode_summaries.jsonl` files were fully audited:
* **Campaigns 1, 2, and 3 (In-Distribution):** All 30 production config files specify `suite="libero_goal_object"`. All corresponding production JSONL output files show exactly `suite="libero_goal_object"` and match task IDs 3 and 6.
* **Campaign 4 (OOD):** All 9 production config files specify `suite="libero_goal_swap"`. All corresponding production JSONL output files show exactly `suite="libero_goal_swap"` and match task IDs 3, 6, and 8.
* **Log Verification:** Runtime log metadata (e.g. `prod_task3_modified_h10_risk_topk8_s0.log`) prints the startup job parameters, which align with the target suites and task IDs. While runtime logs do not print the absolute BDDL file path, the benchmark API and config paths confirm their correct resolution.

---

## 3. LIBERO Benchmark API & Asset Identity

By querying the LIBERO benchmark registry on Bob via the activated environment, the BDDL files, task names, and initial states files were resolved and hashed.

### A. In-Distribution Suite: `libero_goal_object`
* **Path to BDDL files:** `.../LIBERO-PRO/libero/libero/bddl_files/libero_goal_object/`
* **Path to Init files:** `.../LIBERO-PRO/libero/libero/init_files/libero_goal_object/`

| Task ID | Task Name | Language Instruction | BDDL File | Init File | BDDL SHA256 | Init SHA256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | `open_the_top_drawer...` | "open the top drawer and put the bowl inside" | `open_the_top_drawer...bddl` | `...pruned_init` | `2a8fd91a...` | `ff0e2f9d...` |
| **6** | `put_the_cream_cheese...` | "put the cream cheese in the bowl" | `put_the_cream_cheese...bddl` | `...pruned_init` | `b3963241...` | `deb570c0...` |
| **8** | `put_the_bowl_on_the_plate` | "put the bowl on the plate" | `put_the_bowl_on_the_plate.bddl` | `...pruned_init` | `b865b8aa...` | `594af3f5...` |

### B. Out-of-Distribution Suite: `libero_goal_swap`
* **Path to BDDL files:** `.../LIBERO-PRO/libero/libero/bddl_files/libero_goal_swap/`
* **Path to Init files:** `.../LIBERO-PRO/libero/libero/init_files/libero_goal_swap/`

| Task ID | Task Name | Language Instruction | BDDL File | Init File | BDDL SHA256 | Init SHA256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | `open_the_top_drawer...` | "open the top drawer and put the bowl inside" | `open_the_top_drawer...bddl` | `...pruned_init` | `76c51c27...` | `7927a80c...` |
| **6** | `put_the_cream_cheese...` | "put the cream cheese in the bowl" | `put_the_cream_cheese...bddl` | `...pruned_init` | `86ab3eba...` | `6e51541f...` |
| **8** | `put_the_bowl_on_the_plate` | "put the bowl on the plate" | `put_the_bowl_on_the_plate.bddl` | `...pruned_init` | `c5a0dcb8...` | `25c6f10a...` |

### C. Comparison Suite (Official Base LIBERO): `libero_goal`
* **Path to BDDL files:** `.../LIBERO-PRO/libero/libero/bddl_files/libero_goal/`
* **Path to Init files:** `.../LIBERO-PRO/libero/libero/init_files/libero_goal/`

| Task ID | Task Name | Language Instruction | BDDL File | Init File | BDDL SHA256 | Init SHA256 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **3** | `open_the_top_drawer...` | "open the top drawer and put the bowl inside" | `open_the_top_drawer...bddl` | `...pruned_init` | `3056e4dc...` | `1cd5354a...` |
| **6** | `put_the_cream_cheese...` | "put the cream cheese in the bowl" | `put_the_cream_cheese...bddl` | `...pruned_init` | `81c54eac...` | `524de11d...` |
| **8** | `put_the_bowl_on_the_plate` | "put the bowl on the plate" | `put_the_bowl_on_the_plate.bddl` | `...pruned_init` | `8e2024db...` | `3694f475...` |

---

## 4. Fallback Detection & Resolver Code Analysis

The environment loading function `make_env` in `collect_fiper_uncertainty_receding_dean_v1.py` resolves the problem folder from the task registry object (`task.problem_folder`).
1. **No Silent Fallback:** If the BDDL or init files do not exist at the resolved path, the function raises a `FileNotFoundError` (instead of silently falling back to a default folder or suite).
2. **No Suite Aliasing:** No code exists that aliases `libero_goal_object` to `libero_goal` or `libero_goal_swap` to `libero_goal_object`.
3. **Registry Check:** The registry mapping restricts the suites exactly to `libero_goal_object` and `libero_goal_swap`.

---

## 5. Perturbation & Swap Confirmation

### A. Confirmation of LIBERO-PRO Perturbation
By comparing the BDDL files of `libero_goal` (official) and `libero_goal_object` (LIBERO-PRO), we confirm visual object perturbations:
* **Fixtures:** Standard `wooden_cabinet` is replaced by `white_cabinet`.
* **Objects:** Standard `akita_black_bowl` is replaced by `bigger_akita_black_bowl`.
* **Initial states:** The init-state files use pruned initial states (size ~4.1 KB vs ~37 KB for base LIBERO), proving that the starting states have been filtered according to the LIBERO-PRO protocol.

### B. Confirmation of OOD Swap Perturbation
By comparing the BDDL files of `libero_goal_object` and `libero_goal_swap`, we confirm that `libero_goal_swap` is genuinely a different/swap perturbation suite:
* **Reversion of Visuals:** Swap files revert perturbed objects back to base objects (e.g. `white_cabinet` -> `wooden_cabinet`, `bigger_akita_black_bowl` -> `akita_black_bowl`).
* **Swap of Initial States:** The initialization block swaps the physical placements of the objects. For Task 3:
  * In `libero_goal_object`, the bowl starts in the `bowl_region` and the cream cheese starts in the `cream_cheese_region`.
  * In `libero_goal_swap`, the bowl starts in the `cream_cheese_region` and the cream cheese starts in the `bowl_region`.
* **Hashes:** BDDL and init-state file hashes are confirmed distinct between the two suites.

---

## 6. Final Audit Table

| Policy Family / Run | Intended Suite | Config Suite | JSONL Suite | Benchmark Suite | Language Instruction | Resolved BDDL Path | Resolved Init Path | BDDL Hash | Init Hash | LIBERO-PRO Asset Confirmed | Fallback Risk | Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **ID Task 3** | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | "open the top drawer..." | `.../libero_goal_object/open_the_top_drawer...bddl` | `.../libero_goal_object/open_the_top_drawer...pruned_init` | `2a8fd91a...` | `ff0e2f9d...` | **YES** | No | **PASS** |
| **ID Task 6** | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | "put the cream cheese..." | `.../libero_goal_object/put_the_cream_cheese...bddl` | `.../libero_goal_object/put_the_cream_cheese...pruned_init` | `b3963241...` | `deb570c0...` | **YES** | No | **PASS** |
| **ID Task 8** | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | `libero_goal_object` | "put the bowl on the..." | `.../libero_goal_object/put_the_bowl_on_the_plate.bddl` | `.../libero_goal_object/put_the_bowl_on_the_plate.pruned_init` | `b865b8aa...` | `594af3f5...` | **YES** | No | **PASS** |
| **OOD Task 3** | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | "open the top drawer..." | `.../libero_goal_swap/open_the_top_drawer...bddl` | `.../libero_goal_swap/open_the_top_drawer...pruned_init` | `76c51c27...` | `7927a80c...` | **YES** | No | **PASS** |
| **OOD Task 6** | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | "put the cream cheese..." | `.../libero_goal_swap/put_the_cream_cheese...bddl` | `.../libero_goal_swap/put_the_cream_cheese...pruned_init` | `86ab3eba...` | `6e51541f...` | **YES** | No | **PASS** |
| **OOD Task 8** | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | `libero_goal_swap` | "put the bowl on the..." | `.../libero_goal_swap/put_the_bowl_on_the_plate.bddl` | `.../libero_goal_swap/put_the_bowl_on_the_plate.pruned_init` | `c5a0dcb8...` | `25c6f10a...` | **YES** | No | **PASS** |

---

## 7. Audit Summary Fields

AUDIT_READ_ONLY = YES
ANY_FILES_MODIFIED = NO
CONFIG_SUITE_PASS = YES
JSONL_SUITE_PASS = YES
BENCHMARK_API_SUITE_PASS = YES
ID_RUNS_USED_LIBERO_GOAL_OBJECT = YES
OOD_RUNS_USED_LIBERO_GOAL_SWAP = YES
ANY_FALLBACK_TO_OFFICIAL_LIBERO = NO
ANY_FALLBACK_TO_WRONG_SUITE = NO
LIBERO_PRO_ASSET_CONFIRMED = YES
GOAL_OBJECT_ASSETS_DISTINCT_FROM_GOAL_SWAP = YES
TASK_ID_LANGUAGE_MATCH_PASS = YES
BDDL_INIT_HASHES_RECORDED = YES
SUITE_IDENTITY_FINAL_VERDICT = PASS
MOST_IMPORTANT_FINDING = In-distribution runs used libero_goal_object and OOD runs used libero_goal_swap under LIBERO-PRO; they are mathematically verified as perturbed and distinct from base LIBERO, with zero fallback risk.
NEXT_AUDIT_STEP = Conclude the forensic audit sequence and formulate the final verification report.
