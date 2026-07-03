# Model and Suite Identity Verification

This document summarizes the verified identities, file paths, and cryptographic hashes of the models, detectors, and task suites used in the online evaluation campaigns.

---

## 1. Checkpoint and Detector Identities

All weights and configurations stored on Bob (`pcrobot`) have been verified. Original SimVLA and modified SimVLA are verified as structurally and mathematically distinct.

| Model / Checkpoint | Target Path on Bob | File Size (Bytes) | SHA256 Hash |
| :--- | :--- | :---: | :--- |
| **Original SimVLA** | `checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO/model.safetensors` | 3,245,529,028 | `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be` |
| **Modified SimVLA (ckpt-60000)** | `checkpoints/simvla_libero_uncertainty/ckpt-60000/model.safetensors` | 3,245,557,952 | `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71` |
| **H10 Base Detector** | `experiments/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16/model.pt` | 2,598,868 | `802413d2b4acfd1e5094da726ad5b0489315efbdf1bd91cc962e73fe8149f702` |
| **H10 TopK8 Detector** | `models/h10_continuous/all_tasks_random/unc_topk8/model.pt` | 2,602,964 | `687b5d35eed65abfe63b5ff600e52c2228318ad94209e379e73fbaad981dbb2d` |
| **Old TopK8 Detector** | `realtime_deployment/dean_artifacts/current_dean_risk_models_20260602/all_tasks_full/unc_topk8/model.pt` | 2,602,964 | `0ea8e9431a67c1096cd4342b78e93766767234db294d4d9f86d10937e6a966c7` |

### Key Findings:
* **Uncertainty Head:** Verified present in the `ckpt-60000` checkpoint. The file is exactly **28,924 bytes larger** than the original paper backbone, representing the added variance prediction layers. Original SimVLA contains no uncertainty parameters or head outputs.
* **0 crossovers:** No configs or outputs had policy-label mismatches. Checkpoint directories mapped 1-to-1 with policy configurations. The old detector was strictly confined to Campaign 3.

---

## 2. Benchmark Suite and Asset Verification

Evaluations loaded the correct suites from the LIBERO-PRO repository asset tree (`/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/`).

### A. In-Distribution Suite: `libero_goal_object`
* **BDDL Path:** `libero/bddl_files/libero_goal_object/`
* **Init-State Path:** `libero/init_files/libero_goal_object/`
* **Verification:** Confirmed visual object perturbations (e.g. `white_cabinet` replacing `wooden_cabinet` and `bigger_akita_black_bowl` replacing `akita_black_bowl`). Init states are filtered/pruned (4.1 KB vs 37 KB for base LIBERO).

### B. Out-of-Distribution Suite: `libero_goal_swap`
* **BDDL Path:** `libero/bddl_files/libero_goal_swap/`
* **Init-State Path:** `libero/init_files/libero_goal_swap/`
* **Verification:** Swaps starting locations of key objects (e.g. cream cheese starts in bowl region and bowl starts in cream cheese region) while reverting visual textures to base forms. BDDL and init hashes are confirmed distinct from `libero_goal_object`.

### C. Fallback Risk
* **0 Fallback Risk:** The environment loader function `make_env` resolves suite directories from the task object registry. If BDDL or init files do not exist at the target path, it raises a `FileNotFoundError` immediately, preventing silent fallbacks.

---

## 3. Verified BDDL and Init Hashes

| Task ID | Suite | BDDL File | BDDL SHA256 | Init File | Init SHA256 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **3** | `libero_goal_object` | `open_the_top_drawer...bddl` | `2a8fd91a...` | `...pruned_init` | `ff0e2f9d...` |
| **6** | `libero_goal_object` | `put_the_cream_cheese...bddl` | `b3963241...` | `...pruned_init` | `deb570c0...` |
| **8** | `libero_goal_object` | `put_the_bowl_on_the_plate.bddl` | `b865b8aa...` | `...pruned_init` | `594af3f5...` |
| **3** | `libero_goal_swap` | `open_the_top_drawer...bddl` | `76c51c27...` | `...pruned_init` | `7927a80c...` |
| **6** | `libero_goal_swap` | `put_the_cream_cheese...bddl` | `86ab3eba...` | `...pruned_init` | `6e51541f...` |
| **8** | `libero_goal_swap` | `put_the_bowl_on_the_plate.bddl` | `c5a0dcb8...` | `...pruned_init` | `25c6f10a...` |
