# Host Workspace Map

Updated: 2026-07-03 by Codex cross-machine catalog consolidation.

---

## Batman (Local)
* **Hostname:** `Batman`
* **User:** `redafrix`
* **GPU:** NVIDIA GeForce RTX 4060 (8 GB)
* **SSH Alias:** N/A (local)
* **Main Workspace:** `/home/redafrix/tests/internship`
* **fiper_ws:** `/home/redafrix/tests/internship/fiper_ws`
* **Experiment Catalog:** `/home/redafrix/tests/internship/fiper_ws/experiment_catalog`
* **Obsidian Vault:** `/home/redafrix/Documents/Obsidian Vault`
* **Forensic Checks:** `/home/redafrix/tests/internship/checks`
* **Role:** Orchestration, report generation, catalog maintenance, and local plotting/analysis. No active GPU training or online simulation.
* **Git Status 2026-07-03:** `/home/redafrix/tests/internship/.git` is an empty/broken directory; `git status` fails. GitHub push is blocked until the intended project remote is restored/provided.
* **Primary Obsidian Report:** `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`

---

## Bob (pcrobot)
* **Hostname:** `PCROBOTUBUNTU02`
* **User:** `rootalkhatib`
* **GPU:** NVIDIA GeForce RTX 4070 (16 GB)
* **SSH Alias:** `pcrobot`
* **Tailscale IP:** `100.105.217.20`
* **Main Workspace:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
* **OpenVLA-OFT Workspace:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
* **Pi0.5 Workspace:** `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623`
* **Cross-Suite Official OOD Workspace:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630`
* **Official FIPER Workspace:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701`
* **Isaac Lab Workspace:** `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab`
* **Experiment Catalog:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiment_catalog`
* **Forensic Reports:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/realtime_deployment/reports`
* **Datasets:**
  - `data/frozen/fiper_sweep_eternal_20260527_combined` (Bob+Sam sweep instances)
  - `data/live_local` (live local data)
* **Role:** Primary simulation host for all H10 campaigns:
  - In-distribution main campaign (Task 3/6/8)
  - Aggressive TopK8 ablations (Task 3, Task 6)
  - Old detector ablation (Task 6)
  - OOD goal-swap production
  - Full-suite `libero_goal_object_ood` 10ep/100ep threshold sweeps
  - Canonical 4-policy comparison (Task 0)
* **OpenVLA Role:** Isolated OpenVLA-OFT workspace, model smoke tests, OpenVLA plain-goal and goal-object datasets, OpenVLA risk training, and OpenVLA online OOD evaluation.
* **Status 2026-07-03:** Reachable. `/media/rootalkhatib/My Passport` has about 101G free but is 95% used. No catalog-critical tmux session was observed in the cross-machine audit.
* **Completed Recent Experiments:** OpenVLA OOD, Pi0.5 official OOD/goal-swap, cross-suite official OOD datasets, promoted official-source H10 TopK8 model, Bob official FIPER seen train/eval, and Bob official FIPER seen-threshold cross-suite OOD evaluation.
* **OpenVLA Key Paths:**
  - Final dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618`
  - Final risk model: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618`
  - Active online OOD output: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
* **Isaac Lab Note:** Bob now has NVIDIA driver 595.71.05 and an isolated Isaac Lab 6.0 env. Do not disturb `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab` or `/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0` during SimVLA/OpenVLA/FIPER jobs.

---

## Dean (dean-via-bob)
* **Hostname:** `Batman` (note: the hostname on Dean is also "Batman" — not a mistake, the machine was named this way)
* **User:** `dean`
* **GPU:** NVIDIA RTX A5000 (24 GB)
* **SSH Alias:** `dean` (direct currently times out from Batman) / `dean-via-bob` (via ProxyJump through pcrobot, working)
* **Tailscale IP:** `100.124.50.124`
* **Identity Key:** `/home/redafrix/tests/internship/id_dean`
* **Main Workspaces:**
  - `/home/dean/fiper_uncertainty_collection` (original uncertainty data collection and offline experiments)
  - `/home/redafrix/SimVLA_modified` (modified SimVLA checkpoint training)
  - `/home/dean/fiper_goal_object_collection_20260605` (newer goal-object production collection)
* **Experiment Catalog:** `/home/dean/fiper_uncertainty_collection/experiment_catalog`
* **Obsidian Vault:** `/home/redafrix/Documents/Obsidian Vault` (exists but mostly empty — 3 `.base` files and `Welcome.md`)
* **Datasets:**
  - `fiper_uncertainty_collection/runs/dean_object_uncertainty_20260529` — 4,257 episodes across 4 workers (original uncertainty data collection)
  - `fiper_goal_object_collection_20260605/runs/production_20260605/exact_200` — 200 validated episodes (chunk10 + receding)
  - `fiper_goal_object_collection_20260605/runs/production_20260605/continuous_100000` — 17,409 chunk10 episodes + 2,745 receding episodes (ongoing production)
* **Role:** Offline detector training, uncertainty feature collection, TopK feature sweep, canonical 4-policy replication (Task 0), conservative pilot runs, and 2026-06-10 selected-cap OOD diagnostic.
* **OOD Asset Note:** The canonical `/home/redafrix/LIBERO-PRO` tree still does not contain the generated `libero_goal_object_ood_temp` assets. For the 2026-06-10 selected-cap diagnostic, the OOD BDDL/init assets were copied into the isolated fallback tree `/home/dean/LIBERO-PRO` and the experiment-local collector resolves OOD paths there.
* **Status 2026-07-03:** Reachable, but root disk is critically full with about 3.8G free. Do not launch new materialization/training jobs on root without cleanup or external target.
* **Recent FIPER Work:** Official FIPER fold00 materialization/Option A/B, no-retrain goal-object-OOD ablation, cap300 sweeps, H10 TopK8 threshold sweeps, and strict official-FIPER OOD180 work are complete/present under `/home/dean/fiper_uncertainty_collection/experiments`.

---

## Sam
* **Hostname:** `PCROBOTUBUNTU05`
* **User:** `rootalkhatib`
* **GPU:** NVIDIA GeForce RTX 4070 Ti SUPER (16 GB)
* **SSH Alias:** `sam`
* **Tailscale IP:** `100.112.19.30`
* **Main Workspace:** `/home/rootalkhatib/test/reda_ws/fiper_ws`
* **Experiment Catalog:** `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog`
* **Datasets:**
  - `data/frozen/fiper_sweep_eternal_20260527_combined` (mirrored copy of Bob+Sam sweep instances)
  - `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626` — official seen-source dataset stopped at 4,469 episodes / 1,060,884 rows and transferred to Bob for cross-suite training/eval.
* **Role:** Historical evaluation host (libero_10 milk task 7 baseline, joint 4-worker campaign runs from May 29, 2026 and June 1, 2026), V2B/V2C/V2D diagnostics, timeout800 selected-cap run, and official seen-source data collection for cross-suite OOD.
* **Status 2026-07-03:** Reachable but root disk is critically full with about 1.9G free. Do not launch large jobs until cleanup.

---

## Connectivity Summary

| Host | Direct SSH | Via Proxy | Status |
| :--- | :---: | :---: | :--- |
| Bob (`pcrobot`) | ✅ Works | N/A | **Online** |
| Dean (`dean`) | ❌ Times out from Batman in latest check | ✅ `dean-via-bob` works | **Online via Bob** |
| Sam (`sam`) | ✅ Works | N/A | **Online** |

> [!NOTE]
> Dean direct SSH has alternated between working and timing out from Batman. Treat `dean-via-bob` as the reliable route for experiment control unless direct SSH is freshly verified in the current session.
