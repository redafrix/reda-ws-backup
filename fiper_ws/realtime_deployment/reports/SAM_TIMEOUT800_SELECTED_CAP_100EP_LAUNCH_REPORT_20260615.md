# Launch Report: Timeout 800 Selected Cap 100ep Sweep (Sam)

**Date:** June 15, 2026
**Target Host:** Sam (`rootalkhatib@100.112.19.30`)
**Workspace:** `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615`

## Purpose
Run a clean online OOD evaluation (100 episodes per task, 18 tasks) on Sam to compare three policies. This is a replication of the previously trusted `selected-cap` TopK8 gate, but with the environment / runner timeout drastically increased from 300 steps to **800 steps** to measure if policies can recover from failures given more time.

## Policies
1. `original_simvla` (baseline original backbone, no risk)
2. `modified_simvla` (ckpt-60000 backbone, no risk, fixed H10)
3. `risk_topk8_selected_cap` (ckpt-60000 backbone + TopK8 detector + selected cap gating)

## Experiment Configuration
* **Total Expected Episodes:** 5400 (18 tasks × 3 policies × 100 episodes)
* **Suite:** `libero_goal_object_ood` (using explicit OOD generated BDDL/init assets)
* **Seeds:** 10 to 109 across all policies for parity
* **Timeout / max_steps:** `800` (patched in configurations and correctly output to `run_manifest.json`)
* **Risk Selected Cap Values:**
  * `selection_main_threshold` = 0.3
  * `selection_streak_threshold` = 0.3
  * `selection_min_margin` = 0.02
  * `selection_strong_margin` = 0.05
  * `selection_max_selected_score` = 0.4

## Pre-flight Checks
* **Sam Reachable:** Yes
* **GPU & VRAM:** Sufficient (GeForce RTX 4070, ~16GB)
* **Original Checkpoint:** Transferred to Sam (`checkpoints/original_simvla_libero/YuankaiLuo_SimVLA-LIBERO`). `config.json` patched to use offline local SmolVLM weights.
* **Modified Checkpoint:** Verified on Sam (`checkpoints/ckpt-60000`).
* **SmolVLM Cache:** Present at `/tmp/ood_smolvlm_cache`
* **Smoke Test Pass:** 100%. Task 0 and Task 17 evaluated successfully on Seed 10 across all 3 policies without tracebacks, NaNs, or configuration errors.
* **OOD Asset Verification:** Dynamic environment loader confirmed explicit fallback to OOD assets. No silent fallback to base assets occurred.

## Launch State
* **Method:** Sequential full sweep across all tasks.
* **Tmux Session:** `sam_timeout800_selected_cap_100ep_20260615`
* **Supervisor Log:** `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615/sweep_supervisor.log`
* **Health:** Nominal. GPU active (4.1GB VRAM, 57% Vol, 143W). No early crashes or OOMs detected.

*Note: This evaluation cannot be directly compared to the 300-step timeout evaluations without normalizing by length or acknowledging the extended horizon. Ensure downstream analysis accounts for the 800-step max parameter.*