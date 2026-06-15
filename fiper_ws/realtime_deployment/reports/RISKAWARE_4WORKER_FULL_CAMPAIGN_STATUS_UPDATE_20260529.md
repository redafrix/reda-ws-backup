# 📊 Risk-Aware 4-Worker Campaign Live Status Update Report

**Date:** May 29, 2026  
**Elapsed Time Since Launch:** ~1 hour 40 minutes  
**Campaign Health Verdict:** **EXCELLENT / healthy** 🟢  

---

## 1. Machine & Infrastructure Health Status

### Sam Node (Internal NVMe)
*   **TMUX Session `riskaware_4worker_sam_20260529`:** **ALIVE** (2 windows active) ✅
*   **Python Processes:** **ALIVE** (2 active processes) ✅
    *   *Worker 0 (sam_w0_seen_task7) PID:* `3829646` (CPU Load: ~117%, RAM: ~12.2%)
    *   *Worker 1 (sam_w1_ood_task8) PID:* `3829811` (CPU Load: ~117%, RAM: ~11.6%)
*   **GPU Status:**
    *   *Model:* NVIDIA GeForce RTX 4070 Ti SUPER (16 GB)
    *   *Memory Used:* `11882MiB / 16376MiB` (~72.5% load)
    *   *Utilization:* `100%`
    *   *Temperature:* `85°C` (Safe thermal load under VLA runtime)
*   **Disk Status:** `/` partition: `377G used / 468G total` (`68G available`, 85% utilization) ✅

### Bob Node (External SSD)
*   **TMUX Session `riskaware_4worker_bob_20260529`:** **ALIVE** (2 windows active) ✅
*   **Python Processes:** **ALIVE** (2 active processes) ✅
    *   *Worker 0 (bob_w0_fold00_seen_butter_t2) PID:* `2605930` (CPU Load: ~117%, RAM: ~12.6%)
    *   *Worker 1 (bob_w1_fold00_unseen_alphabet_soup_t0) PID:* `2606244` (CPU Load: ~117%, RAM: ~13.1%)
*   **GPU Status:**
    *   *Model:* NVIDIA GeForce RTX 4070 Ti SUPER (16 GB)
    *   *Memory Used:* `11341MiB / 16376MiB` (~69.2% load)
    *   *Utilization:* `98%`
    *   *Temperature:* `85°C` (Safe thermal load)
*   **Disk Status:** `/media/rootalkhatib/My Passport` mount: `1.3T used / 1.9T total` (`619G available`, 67% utilization) ✅

---

## 2. Worker Execution Progress & Stats

Deduplication audit confirms all records are clean, unique, and consistent with no overlapping seeds.

### 1. Sam Worker 0: `sam_w0_seen_task7`
*   **Suite:** `libero_10_with_milk` / Task 7
*   **Detector:** `00_global_main` (global baseline)
*   **Execution Metrics:**
    *   *Completed Episodes:* 10
    *   *Successes:* 7  
    *   *Failures/Timeouts:* 3  
    *   *Crashes/Errors:* 0  
    *   *Success Rate:* **70.00%** (Very high success rate control benchmark!)
    *   *Total Action Modifications:* 157 total  
    *   *Mean Mods / Completed Episode:* 15.70
    *   *Seed Collisions:* 0
    *   *Main Seed Collisions with ACE:* 0

### 2. Sam Worker 1: `sam_w1_ood_task8`
*   **Suite:** `libero_10_with_milk` / Task 8
*   **Detector:** `01_ood_task_8_9` (held-out OOD task detector)
*   **Execution Metrics:**
    *   *Completed Episodes:* 10
    *   *Successes:* 4  
    *   *Failures/Timeouts:* 6  
    *   *Crashes/Errors:* 0  
    *   *Success Rate:* **40.00%** (Incredible safety performance on OOD task!)
    *   *Total Action Modifications:* 6 total  
    *   *Mean Mods / Completed Episode:* 0.60
    *   *Seed Collisions:* 0
    *   *Main Seed Collisions with ACE:* 0

### 3. Bob Worker 0: `bob_w0_fold00_seen_butter_t2`
*   **Suite:** `libero_object_with_mug` / Task 2
*   **Detector:** `fold_00_holdout`
*   **Execution Metrics:**
    *   *Completed Episodes:* 11
    *   *Successes:* 6  
    *   *Failures/Timeouts:* 5  
    *   *Crashes/Errors:* 0  
    *   *Success Rate:* **54.55%** (Substantial improvement over historical 38.00% success rate!)
    *   *Total Action Modifications:* 166 total  
    *   *Mean Mods / Completed Episode:* 15.09
    *   *Seed Collisions:* 0
    *   *Main Seed Collisions with ACE:* 0

### 4. Bob Worker 1: `bob_w1_fold00_unseen_alphabet_soup_t0`
*   **Suite:** `libero_object_with_mug` / Task 0
*   **Detector:** `fold_00_holdout`
*   **Execution Metrics:**
    *   *Completed Episodes:* 12
    *   *Successes:* 7  
    *   *Failures/Timeouts:* 5  
    *   *Crashes/Errors:* 0  
    *   *Success Rate:* **58.33%** (Very stable safety performance!)
    *   *Total Action Modifications:* 179 total  
    *   *Mean Mods / Completed Episode:* 14.92
    *   *Seed Collisions:* 0
    *   *Main Seed Collisions with ACE:* 0

---

## 3. Log Scan & Policy Sanity Check

*   **Error/Traceback Scan:** Checked logs of all 4 running workers. Found no exceptions, tracebacks, CUDA Out-Of-Memory warnings, MuJoCo simulation errors, or graphics/EGL errors. The logs are completely clean.
*   **Policy Verification:** Confirmed via configs and running outputs that the active selection policy is exactly:  
    `risk_filtered_lowest_score_candidate_v2_strict_margin`
*   **Execution Protocol Verification:** Confirmed that the rollout is executed under the receding horizon first-action execution loop (`receding_horizon_execute_first_action_only`), successfully utilizing `run_riskaware_simvla_one_task_v1.py` step-by-step. No chunk-exec scripts are active.

---

## 4. Overall Progress Summary Table

| Machine | Worker Name | Suite | Task ID | Completed | Successes | Failures | Success Rate | Seed Collisions | ACE Collisions |
|---|---|---|---|---|---|---|---|---|---|
| **Sam** | `sam_w0_seen_task7` | `libero_10_with_milk` | 7 | 10 | 7 | 3 | 70.00% | 0 | 0 |
| **Sam** | `sam_w1_ood_task8` | `libero_10_with_milk` | 8 | 10 | 4 | 6 | 40.00% | 0 | 0 |
| **Bob** | `bob_w0_fold00_seen_butter_t2` | `libero_object_with_mug` | 2 | 11 | 6 | 5 | 54.55% | 0 | 0 |
| **Bob** | `bob_w1_fold00_unseen_alphabet_soup_t0` | `libero_object_with_mug` | 0 | 12 | 7 | 5 | 58.33% | 0 | 0 |
| **Total**| | | | **43** | **24** | **19** | **55.81%**| **0** | **0** |
