# GITHUB PUSH AND WORKSPACE SYNC REPORT - 2026-06-16

This report documents the status of the FIPER/SimVLA internship workspaces, audits performed, catalog synchronization, and GitHub pushes.

---

## 1. Disk Space Table

| Host | Path Checked | Filesystem Type | Total Size | Used Space | Available Space | Use % |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Batman (Local)** | `/home/redafrix/tests/internship` | ext4 | 302 GB | 272 GB | **15 GB** | 95% |
| **Bob (pcrobot)** | `/media/rootalkhatib/My Passport` | exfat | 1.9 TB | 1.4 TB | **523 GB** | 72% |
| **Sam (sam)** | `/home/rootalkhatib/test/reda_ws` | ext4 | 468 GB | 382 GB | **63 GB** | 87% |
| **Dean (dean)** | `/home/dean` | ext4 | 469 GB | 407 GB | **39 GB** | 92% |

*Verdict:* Bob has more than enough space (523 GB available). No disk space issues on any host.

---

## 2. Running-Process Safety Audit

We checked for running experiments (Python/GPU simulation jobs or active TMUX sessions). No active evaluation campaigns were running.

* **Bob (pcrobot):**
  - Found an old python process running on CPU since May 12: `python3 marathon_c_50.py --idea 22` (PID 851081).
  - No active GPU processes or active TMUX evaluation campaigns.
  - Leftover detached TMUX sessions: `ood_production_aggressive_fixed_100ep_20260609`, `stage5`, `task6_aggressive_20260608`, `task6_aggressive_old_detector_20260608`.
* **Sam (sam):**
  - Found policy render sweep scripts currently active on CPU:
    - `/home/rootalkhatib/envs/simvla/bin/python3 .../run_render_sweep.py` (PID 1150315)
    - `python3 .../run_policy_matrix_render.py` (PID 1154979) for `task16_risk_topk8_selected_cap.json`.
  - These jobs are rendering video reels and do not interfere with git sync or evaluation directories.
* **Dean (dean):**
  - No active Python, TMUX, or GPU experiment processes.

---

## 3. Experiment Map Audit & Catalog Check

The canonical local catalog files under `fiper_ws/experiment_catalog/` were verified as fully up-to-date and registered with recent work:
* **Sam Timeout800 selected-cap 100ep Campaign:** Registered in `MASTER_EXPERIMENT_INDEX.md`, `TRUSTED_RESULTS_SUMMARY.md`, `KEY_RESULTS.md`, and `hosts/sam.md`. Verified results: Original 1,716/1,800 (95.33%), Modified 1,744/1,800 (96.89%), Selected-cap 1,754/1,800 (97.44%), paired net +10 vs Modified.
* **Bob/Dean Selected-Cap 100ep Runs:** Confirmed registered and trusted positive on Dean (+15 net vs Modified), and small positive on Bob (+5 net with delay30).
* **Presentation Work:** Confirmed separated and logged in `presenation/README.md` and `vla_branch_10slides_v2_20260615/`.
* **Video Reel Work:** Verified that final reels exist under `presenation/video_reels_20260616/libero_goal_basic_10_tasks_success_reel_4x.mp4` (196 KB).

---

## 4. Catalog Synchronization Status

All catalog files in `/home/redafrix/tests/internship/fiper_ws/experiment_catalog` were successfully synchronized to all remote hosts:
* **Bob:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiment_catalog/`
* **Sam:** `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog/`
* **Dean:** `/home/dean/fiper_uncertainty_collection/experiment_catalog/`

**Checksum Verification:**
* Verified checksum of `SYNC_STATUS.md` after sync across all hosts (Match: `c6ba02da8f43a11f59071dab36070d21`).

---

## 5. Git Repositories Discovered

* **Local (Batman):** The root `/home/redafrix/tests/internship` is not a git repository. Checked its four sub-repositories (all pointing to their own upstreams):
  - `./franka_wrist_camera_isaaclab-test/franka_wrist_camera_isaaclab`
  - `./isaac_dynamicVLA-test/IsaacLab`
  - `./isaac_dynamicVLA-test/dynamic-vla`
  - `./fiper_ws/external/fiper`
* **Bob:** `/media/rootalkhatib/My Passport/reda_ws` (Git repository pointing to `reda-ws-backup.git`)
* **Sam:** `/home/rootalkhatib/test/reda_ws` (Git repository pointing to `reda-ws-backup.git`)
* **Dean:** `/home/dean/fiper_uncertainty_collection` (Git repository pointing to `reda-ws-backup.git`)

---

## 6. Branches and Commits Pushed

The lightweight code, documentation, and experiment catalog updates were staged, checked for large files, and pushed:

| Host | Branch Pushed | Commit Hash | Message | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Bob** | `bob` | `a5ff896` | `docs: update experiment catalog sync status and register latest Sam timeout800 results` | **Pushed** |
| **Sam** | `sam` | `6af5931af` | `docs: register latest Sam timeout800 results and add policy rendering scripts` | **Pushed** |
| **Dean** | `dean` | `45d745c` | `docs: update experiment catalog sync status and register latest Sam timeout800 results` | **Pushed** |

---

## 7. Files Intentionally Excluded (Large Files Safety)

We verified that all large files are correctly ignored by `.gitignore` across all nodes:
* `*.safetensors`, `*.pt`, `*.pth`, `*.ckpt` (checkpoints)
* `*.zip`, `*.tar.gz`, `*.jsonl`, `*.csv` (datasets and logs)
* `runs/`, `data/`, `datasets/`, `checkpoints/` directories
* `fiper_ws/trash/`, `fiper_ws/collection/`, `fiper_ws/scratch/`, `fiper_ws/experiments/`
* Specifically, the following heavy files are excluded:
  - `./v8_experiment_package.zip` (100MB+ zip)
  - `./checkpoints/ckpt-50000.zip` (model weights)
  - `./checkpoints/simvla_ckpt_50000/ckpt-50000/model.safetensors` (model weights)
  - `fiper_ws/realtime_deployment/smolvlm_cache/model.safetensors` (cached weights)
  - `intern_ship_ws/ood_data/phase2_tdqc_goal_object_ood_denoise_20260504_104916/combined_goal_object_ood.jsonl` (raw logs)

---

## 8. Network and Host Reachability

* **Bob (`pcrobot`):** Fully reachable.
* **Sam (`sam`):** Fully reachable (re-integrated successfully, now online).
* **Dean (`dean` via Tailscale/Bob):** Fully reachable (direct tailscale SSH alias `dean` worked successfully).
* **Blockers:** None.
