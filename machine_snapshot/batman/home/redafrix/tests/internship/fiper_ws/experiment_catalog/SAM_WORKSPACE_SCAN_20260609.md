# Sam Workspace Scan Report

**Date:** 2026-06-09  
**Audit Author:** Antigravity (Workspace Catalog Audit)

This document maps the rediscovered and verified directories, runs, and report files located on the machine `Sam`.

---

## 1. Host & Hardware Identity
* **Hostname:** `PCROBOTUBUNTU05`
* **GPU:** `NVIDIA GeForce RTX 4070 Ti SUPER` (16,376 MiB total memory)
* **Access Status:** Online and fully reachable via SSH alias `sam` (Tailscale IP: `100.112.19.30`).
* **Active Status:** Host is active and online, but all execution campaigns are completed (no active tmux sessions or simulation runners).

---

## 2. Fiper Workspace Directories
The deep search on Sam identified the following canonical workspace folders under the user `rootalkhatib`:
* **Main Workspace Root:** `/home/rootalkhatib/test/reda_ws/fiper_ws`
* **Realtime Deployment Root:** `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment`
* **Reports Directory:** `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/reports`
* **Runs Directory:** `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/runs`
* **Catalog Directory:** `/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog` (Created on 2026-06-09 as part of sync)

---

## 3. Important Reports Found on Sam
The `/home/rootalkhatib/test/reda_ws/fiper_ws/realtime_deployment/reports/` folder contains several critical historical audit and setup files:
* `BASELINE_SIMVLA_LIBERO10_MILK_TASK7_SAM_V1_REPORT.md` (May 28, 2026)
* `BASELINE_SIMVLA_LIBERO10_MILK_TASK7_SAM_V1_SETUP_AND_LAUNCH_REPORT.md` (May 28, 2026)
* `REALTIME_TASK7_FINAL_CLEAN_AUDIT_AND_TIMING_REPORT_20260529.md` (May 29, 2026)
* `REALTIME_TASK7_SAM_BASELINE_VS_BOB_RISKAWARE_V2_STRICT_STATUS_OR_FINAL_REPORT_20260529.md` (May 29, 2026)
* `RISKAWARE_4WORKER_CONFIG_AND_SMOKE_AUDIT_20260529.md` (May 29, 2026)
* `RISKAWARE_4WORKER_FULL_CAMPAIGN_LAUNCH_REPORT_20260529.md` (May 29, 2026)
* `RISKAWARE_4WORKER_FULL_CAMPAIGN_STATUS_UPDATE_20260529.md` (May 29, 2026)
* `RISKAWARE_MULTI_TASK_4WORKER_PREFLIGHT_AUDIT_20260529.md` (May 29, 2026)

---

## 4. Run Evaluation Verification Table
We verified that the raw summary and log files exist on Sam for all documented evaluations:

| Campaign / Run Directory | Task/Suite | File Name | Size / Line Count | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| `baseline_simvla_libero10_milk_task7_sam_v1` | Libero-10 Milk Task 7 | `episode_summaries_canonical_100.jsonl` | 100 lines | **Verified & Complete (Trusted)** |
| `baseline_simvla_libero10_milk_task7_sam_v1` | Libero-10 Milk Task 7 | `episode_summaries.jsonl` (raw) | 150 lines | Contains duplicates, resolved in canonical |
| `baseline_same_seed_4worker_20260601/sam_w0_seen_task7` | Task 7 Seen | `episode_summary_wsam_w0_seen_task7.jsonl` | 450 lines | **Verified & Complete (Trusted)** |
| `baseline_same_seed_4worker_20260601/sam_w1_ood_task8` | Task 8 OOD | `episode_summary_wsam_w1_ood_task8.jsonl` | 429 lines | **Verified & Complete (Trusted)** |
| `riskaware_4worker_20260529/sam_w0_seen_task7` | Task 7 Seen | `episode_summary_wsam_w0_seen_task7.jsonl` | 450 lines | **Verified & Complete (Trusted)** |
| `riskaware_4worker_20260529/sam_w1_ood_task8` | Task 8 OOD | `episode_summary_wsam_w1_ood_task8.jsonl` | 429 lines | **Verified & Complete (Trusted)** |
| `baseline_simvla_chunk_exec_task7_10eps_sam_20260529` | Task 7 | `episode_summaries.jsonl` | 10 lines | **Verified & Complete (Pilot)** |
| `riskaware_actionmod_v2_strict_chunk_exec_task7_10eps_sam_20260529` | Task 7 | `episode_summaries.jsonl` | 10 lines | **Verified & Complete (Pilot)** |
| `smoke_worker_sam_0_seen_task7_20260529` | Task 7 Smoke | `episode_summary_wsam0_smoke.jsonl` | 1 line | **Verified (Smoke check only)** |
| `smoke_worker_sam_1_ood_task8_20260529` | Task 8 Smoke | `episode_summary_wsam1_smoke.jsonl` | 1 line | **Verified (Smoke check only)** |

---

## 5. Trust Verdict for Sam's Workspace
* **Main Trusted Benchmark:** The `baseline_simvla_libero10_milk_task7_sam_v1` run is trusted and forms the baseline for libero10 milk task 7 (100 canonical episodes verified).
* **Cross-Host Sync Status:** The files exist, their integrity matches their respective reports, and they are now formally cataloged.
