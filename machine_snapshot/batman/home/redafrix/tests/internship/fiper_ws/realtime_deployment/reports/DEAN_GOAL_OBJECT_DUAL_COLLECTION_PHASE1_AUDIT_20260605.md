# Dean Goal Object Dual Collection - Phase 1 Audit Report

**Date:** June 5, 2026
**Status:** Audit Complete - Ready for Implementation Phase

## 1. Connectivity & Environment Audit

- **Target Machine:** Dean (`100.124.50.124`)
- **Access Path:** Verified direct SSH is flaky; fallback `ssh dean-via-bob` (ProxyJump pcrobot) is stable and used for all operations.
- **Python Environment:** `/home/redafrix/miniconda3/envs/simvla/bin/python`
  - **Torch:** `2.6.0+cu124` (Verified with CUDA support)
  - **Imports:** `robosuite`, `mujoco`, `transformers`, `libero` verified.
- **GPU Status:** NVIDIA RTX A5000 (24.5 GB VRAM).
  - Currently IDLE (15 MiB used).
  - Persistence-M is ON.
- **System Resources:**
  - **RAM:** 31 GB total, ~26 GB available.
  - **Disk (/home/dean):** 56 GB available (88% used). 
    - *Warning:* 56 GB is sufficient for the 200 manifest episodes (~2-4 GB estimated), but may be insufficient for the full 100,000 episode random collection if full images are saved. Aggressive compression or periodic cleanup will be required.

## 2. Reproduction Bundle Audit

- **Isolated Directory:** Created at `/home/dean/fiper_goal_object_collection_20260605/`.
- **Extraction:** Bundle extracted successfully.
- **Internal Verification:** `verify_bundle.py` passed.
  - 200 unique episode identities confirmed.
  - Task IDs 0-9, State Indices 0-9 and 40-49.
  - BDDL language prompts and SHA-256 sums consistent.
- **Cross-Registry Comparison:** **CRITICAL FINDING**.
  - Compared bundled BDDL and `.pruned_init` files against Dean's existing `/home/redafrix/LIBERO-PRO`.
  - **Result:** 100% mismatch. Every BDDL and initialization file on Dean has a different SHA-256 than the reproduction bundle.
  - **Action:** The collector **MUST** explicitly point to the isolated bundle assets to ensure exact world-model reproduction.

## 3. Collector & Model Audit

- **Checkpoint (ckpt-60000):**
  - Verified at `/home/dean/checkpoints/simvla_libero_uncertainty/ckpt-60000/`.
  - `config.json` confirmed: `"predict_uncertainty": true`, `"num_actions": 10`.
  - `model.safetensors` size: 3.1 GB (Complete).
- **Existing Collector Audit:**
  - Analyzed `collect_fiper_uncertainty_receding_dean_v1.py`.
  - **Feature Support:** Correctly implements 49 uncertainty features (UNCERTAINTY_49D_KEYS) and their temporal deltas.
  - **ACE Support:** Correctly generates 8 ACE candidates per step using reproducible seeded noise.
  - **Image Support:** Records agentview and wrist images.
- **Gap Analysis for Implementation:**
  - **Mode 1:** Current loop logic is compliant (replan every step).
  - **Mode 2:** Needs implementation. Must execute 10-action chunk and record intermediate transitions (proprio, images, rewards) without replanning.
  - **Manifest Driver:** Needs to be added to iterate through the specific 200 episodes first.
  - **Asset Redirection:** Must use `PYTHONPATH` or explicit args to use bundled BDDL/init files.
  - **Worker-Independent Seeds:** Current seed logic uses `global_seed + worker_id`, which is worker-dependent. Must be updated to use a deterministic hash of `(episode_manifest_identity, timestep, global_seed)`.

## 4. Resource & Benchmarking Plan

- **Parallelism:** Dean's 24GB VRAM can comfortably fit ~4-6 parallel SimVLA workers (each ~3-4 GB).
- **Bottleneck:** CPU/RAM for Mujoco simulations and Disk I/O for image saving.
- **Benchmarking:** We will start with 4 workers and monitor `nvidia-smi` and `top`. If unreachable risk is detected (load > 2x CPU count), we will throttle.

## 5. Conclusion

Dean is healthy and the reproduction bundle is correctly isolated and verified as different from the local environment. The existing collector provides a strong 90% foundation for features and uncertainty logic but requires a custom wrapper/driver to fulfill the dual-mode manifest-driven requirement.

**Do not patch production files or launch collection yet.** Implementation will follow in Phase 2.
