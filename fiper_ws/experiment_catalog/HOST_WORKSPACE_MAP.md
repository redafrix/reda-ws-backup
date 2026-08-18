# Host Workspace Map

Updated: 2026-07-30 after the Dean hardware replacement and external-SSD relocation.

---

## Current Topology Override (2026-07-30)

This section overrides older host/path assumptions elsewhere in the catalog.

* The external 2 TB SSD `My Passport` volume that previously hosted Bob's
  `/media/rootalkhatib/My Passport/reda_ws` tree is no longer attached to Bob.
* That volume is now attached to the replacement Dean workstation at
  `/media/redafrix/My Passport1`.
* Bob remains reachable as `pcrobot`, but
  `/media/rootalkhatib/My Passport/reda_ws` is currently absent there. Treat all
  old Bob paths under that mount as historical logical paths until the volume is
  moved again or a new mount is explicitly verified.
* The replacement Dean workstation is reached directly with SSH alias `dean`.
  Its hostname is also `Batman`, but it is not the local laptop.
* SSH enters as user `dean`; current Isaac/OpenPI work and user services run as
  user `redafrix`. A failed `systemctl --user` query from the `dean` account does
  not prove that a `redafrix` user service is down.
* The replacement Dean has an NVIDIA GeForce RTX 5090 with 32,607 MiB VRAM,
  driver `580.95.05`, and a dedicated internal AI SSD mounted at `/mnt/ai`.
* Two external volumes are attached to Dean:
  `/media/redafrix/My Passport1` (2 TB SSD, former Bob experiment disk,
  `/dev/sda1`, exFAT, non-rotational) and `/media/redafrix/My Passport`
  (separate 4 TB HDD, `/dev/sdb1`, NTFS, rotational). These desktop-user mounts may be
  unreadable from noninteractive SSH sessions logged in as `dean`.

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
* **Git Status 2026-07-03:** Git was rebuilt after the broken `.git` directory was moved to `.git.broken_20260703_112818`. Remote is `https://github.com/redafrix/reda-ws-backup.git`. Catalog branches `catalog/batman-20260703`, `catalog/bob-20260703`, `catalog/sam-20260703`, `catalog/dean-20260703`, and `catalog/cross-machine-20260703` were pushed; keep heavy artifacts out of Git.
* **Primary Obsidian Report:** `/home/redafrix/Documents/Obsidian Vault/FIPER Risk-Aware Report 20260602/FIPER Risk-Aware SimVLA - Full Report.md`
* **Deep Audit 2026-07-03:** Local archives were scanned and indexed in `DEEP_EXPERIMENT_COVERAGE_AUDIT_20260703.md`, including Stage6-9 reports, Pi0.5/OpenVLA scripts, official-FIPER scripts, video-smoke material, and older Isaac folders.

---

## Bob (pcrobot)
* **Current Storage Override 2026-07-30:** the external `My Passport` experiment
  disk has been moved to Dean. The historical workspace paths below are not
  currently mounted on Bob.
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
* **Current Lightweight Catalog Mirror:** `/home/rootalkhatib/experiment_catalog_current`
  (created after the external disk moved to Dean)
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
* **Status 2026-07-30:** Reachable, but
  `/media/rootalkhatib/My Passport/reda_ws` is absent. Bob's root filesystem is
  still present; do not launch or resume any experiment that assumes the
  external paths until the volume location is deliberately changed.
* **Completed Recent Experiments:** OpenVLA OOD, Pi0.5 official OOD/goal-swap, cross-suite official OOD datasets, promoted official-source H10 TopK8 model, Bob official FIPER seen train/eval, and Bob official FIPER seen-threshold cross-suite OOD evaluation.
* **Deep Audit Additions 2026-07-03:** The audit explicitly re-indexed Bob `bob_risk_matrix_campaign_20260605`, `libero_goal_object_ood_full_sweep_20260609`, `libero_goal_object_ood_audit_20260609`, `re_run_v2_018_audit_20260624`, Pi0.5 no-task9/40ep/10ep smoke roots, OpenVLA smoke roots, and cross-suite per-dataset training/eval roots.
* **OpenVLA Key Paths:**
  - Final dataset: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/datasets/openvla_goal_object_final_1890_complete_rounds_20260618`
  - Final risk model: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/offline_risk_experiments/openvla_final1890_risk_20260618`
  - Active online OOD output: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/online_evals/libero_goal_object_ood_openvla_basic_vs_risk_100ep_20260618`
* **Isaac Lab Note:** Bob now has NVIDIA driver 595.71.05 and an isolated Isaac Lab 6.0 env. Do not disturb `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab` or `/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0` during SimVLA/OpenVLA/FIPER jobs.

---

## Dean (replacement workstation)
* **Hostname:** `Batman` (note: the hostname on Dean is also "Batman" — not a mistake, the machine was named this way)
* **SSH User:** `dean`
* **Workload User:** `redafrix`
* **GPU:** NVIDIA GeForce RTX 5090 (32,607 MiB)
* **NVIDIA Driver:** `580.95.05`
* **SSH Alias:** `dean` (direct, verified working on 2026-07-30)
* **System Disk:** `/dev/sdc2`, about 74 GiB free at the 2026-07-30 audit
* **AI SSD:** `/mnt/ai`, label `AI_SSD`, about 374 GiB free at the 2026-07-30 audit
* **Former Bob Disk:** `/media/redafrix/My Passport1` (2 TB SSD, `/dev/sda1`, exFAT, non-rotational)
* **Additional External Disk:** `/media/redafrix/My Passport` (4 TB HDD, `/dev/sdb1`, NTFS, rotational)
* **Main Workspaces:**
  - `/mnt/ai/pi05/openpi` (OpenPI checkout and isolated environment)
  - `/mnt/ai/pi05/datasets/reaching_pose_v1_4400_pi05_fullpose_v3`
  - `/mnt/ai/pi05/training/reaching_pose_v1_4400_pi05_fullpose_v3`
  - `/mnt/ai/isaac/franka_wrist_camera_isaaclab`
  - `/mnt/ai/isaac/IsaacLab-6.0`
  - `/mnt/ai/isaac/envs/env_isaaclab_6_0`
  - `/mnt/ai/projects/SimVLA_Gontary`
  - `/media/redafrix/My Passport/reda_ws` (historical Bob workspace tree on the relocated disk)
* **Current Role:** Primary Isaac Sim/Isaac Lab and pi0.5/OpenPI training host.
  Historical Dean FIPER work remains provenance but is not the active campaign.
* **Active Training 2026-07-30:** `pi05_franka_reach_fullpose_v3_stock_production`,
  target 30,000 optimizer updates, effective batch 256, stock pi0.5 32D
  objective. Live audit reached step 24,500 with finite loss/gradients and
  finalized checkpoints through 24,000.
* **Current SimVLA Work:** `/mnt/ai/projects/SimVLA_Gontary` is prepared for the
  RTX 5090. The exact 150-scene full-OOD Isaac protocol was found on
  `origin/mimic-video-h15-beta-nll-eval`, but the owner's evaluated checkpoint,
  normalization assets, and generated 150-episode result payload are still
  missing.
* **Codex Context Source:** session
  `019f7eed-ad2e-7893-88dd-17d805ce9187`, stored at
  `/home/redafrix/.codex/sessions/2026/07/20/rollout-2026-07-20T11-48-53-019f7eed-ad2e-7893-88dd-17d805ce9187.jsonl`.

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
* **Deep Audit Addition 2026-07-03:** Sam video-review reels at `/home/rootalkhatib/test/reda_ws/fiper_ws/trash/video_reels_libero_goal_and_ood_20260616` are now recorded as visual/manual-review provenance.

---

## Connectivity Summary

| Host | Direct SSH | Via Proxy | Status |
| :--- | :---: | :---: | :--- |
| Bob (`pcrobot`) | ✅ Works | N/A | **Online** |
| Dean (`dean`) | ✅ Works | Not needed | **Online; replacement RTX 5090 workstation** |
| Sam (`sam`) | ✅ Works | N/A | **Online** |

> [!NOTE]
> Bob no longer carries the external experiment disk. Use the current topology
> override above before following any historical absolute path.
