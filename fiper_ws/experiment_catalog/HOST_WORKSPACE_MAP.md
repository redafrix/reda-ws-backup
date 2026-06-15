# Host Workspace Map

Updated: 2026-06-10 by Codex full workspace audit.

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

---

## Bob (pcrobot)
* **Hostname:** `PCROBOTUBUNTU02`
* **User:** `rootalkhatib`
* **GPU:** NVIDIA GeForce RTX 4070 (16 GB)
* **SSH Alias:** `pcrobot`
* **Tailscale IP:** `100.105.217.20`
* **Main Workspace:** `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
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
* **Active Experiments:** None known as of the latest 2026-06-10 catalog update. OOD 0.3/0.5/q95 full-suite sweeps are complete.

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
* **Active Experiments:** selected-cap OOD 100ep confirmation running in tmux `dean_selected_cap_t03_c04_100ep_20260610` as of 2026-06-10. The selected-cap margin-0.10 10ep diagnostic has completed and was not selected for scaling.

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
* **Role:** Historical evaluation host (libero_10 milk task 7 baseline, joint 4-worker campaign runs from May 29, 2026 and June 1, 2026). Also used for the 2026-06-10 V2B/V2C/V2D adaptive-horizon OOD diagnostics. Currently idle with no active experiments.

---

## Connectivity Summary

| Host | Direct SSH | Via Proxy | Status |
| :--- | :---: | :---: | :--- |
| Bob (`pcrobot`) | ✅ Works | N/A | **Online** |
| Dean (`dean`) | ❌ Times out from Batman in latest check | ✅ `dean-via-bob` works | **Online via Bob** |
| Sam (`sam`) | ✅ Works | N/A | **Online** |

> [!NOTE]
> Dean direct SSH has alternated between working and timing out from Batman. Treat `dean-via-bob` as the reliable route for experiment control unless direct SSH is freshly verified in the current session.
