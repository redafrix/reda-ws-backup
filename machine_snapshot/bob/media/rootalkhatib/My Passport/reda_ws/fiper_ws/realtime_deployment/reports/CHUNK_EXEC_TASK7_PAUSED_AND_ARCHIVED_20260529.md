# Chunk-Exec Task 7 Pause and Archive Report

**Date:** 2026-05-29  
**Status:** Experiments paused and archived cleanly. Returning to CLI 1's 4-worker campaign.

---

## 1. Executive Summary
This report documents the clean shutdown and archiving of all Task 7 `chunk_exec` (full-chunk receding horizon execution) experiments on Bob (`pcrobot`). In accordance with instructions, all active chunk execution tasks have been terminated, their raw outputs recorded, and all run directories consolidated under a central archive directory. No data was deleted, no reports were overwritten, and CLI 1's 4-worker preflight configuration and run files were left completely untouched.

---

## 2. Processes & Tmux Sessions Terminated
The following tmux sessions and processes on Bob were stopped cleanly:

- **Tmux Sessions Killed:**
  - `chunk_exec_rerun` (coordinator session for sequential v2 reruns)
  - `h5_baseline` (coordinator session for Horizon 5 baseline experiment)
- **Processes Killed:**
  - `run_riskaware_simvla_chunk_exec_v2.py` (PID: `2579173`)
  - `run_baseline_simvla_chunk_exec_h5_v1.py` (PID: `2589360`)
  - No baseline v2 chunk runner (`run_baseline_simvla_chunk_exec_v2.py`) was active at the time of shutdown.
- **Unrelated Processes Preserved:**
  - `marathon_c_50.py --idea 22` (PID: `851081`) and all system Python processes were left running.

---

## 3. Final Partial Progress Before Stop

Before killing the processes, final execution stats were recorded:

### A. Horizon 10 Risk-Aware Rerun (Incomplete)
- **Completed Episodes:** 61 (Indices 0 to 60)
- **Successes:** 60
- **Failures:** 1
- **Last Completed Episode:** Index 60 (Seed `1234978087`)
- **Episode 48 (Seed `1865224713`):** Completed as **Failure** (Steps: 300, 1 action modification attempted). The runner script patched with version `v2` successfully logged this failure without throwing `UnboundLocalError` or crashing.
- **Episode 93 (Seed `1517830958`):** Not reached before termination.
- **Conclusion Status:** **NOT AVAILABLE**. Because the risk-aware rerun was stopped early at episode 61/100, no final conclusion can be drawn about its overall 100-episode success rate.

### B. Horizon 5 Baseline Test (Incomplete)
- **Completed Episodes:** 75 (Indices 0 to 74)
- **Successes:** 70
- **Failures:** 5
- **Last Completed Episode:** Index 74 (Seed `1249209539`)
- **Failed Episode Seeds:**
  - Episode 0 (seed `889528444`)
  - Episode 18 (seed `1338331430`)
  - Episode 24 (seed `2125793409`)
  - Episode 25 (seed `2066021479`)
  - Episode 30 (seed `2103798454`)

---

## 4. Completed Experiments Verified

The following runs completed fully and were audited:

### A. Horizon 10 Baseline Rerun (Complete)
- **Completed Episodes:** 100/100
- **Success Rate:** **98/100** (98.00%)
- **Failure Seeds:** Exactly 2 failures: `1865224713` (Episode 48) and `1517830958` (Episode 93).
- **Legitimacy Audit:**
  - **No Hidden First-Action Behavior:** Confirmed that `sum(actions_executed_from_chunk) == sum(num_steps)` holds true (21,814 steps). Every single non-terminal chunk executed exactly 10 actions open-loop.
  - **Action Space:** Confirmed that it executes environment-space denormalized actions (`candidate_action_env`), not normalized actions.
  - **Success Semantics:** Confirmed matching condition `success = success or bool(rew > 0)` with the old first-action runner. No false success accounting.
  - **Reset state:** Modulo indexing `init_states[episode_index % len(init_states)]` is identical to old first-action, making paired comparison valid, but `reset_seed` only seeds the policy sampler (i.e. `RESET_SEED_MEANINGFUL = PARTIAL`).

### B. Baseline Spotcheck (Complete)
- **Completed Episodes:** 3/3
- **Reproduced Outcomes:**
  - Episode 0 (seed `889528444`): **Success** in 217 steps (matches full run).
  - Episode 48 (seed `1865224713`): **Failure** in 300 steps (matches full run).
  - Episode 93 (seed `1517830958`): **Failure** in 300 steps (matches full run).

---

## 5. Consolidated Archive Path
All run folders have been moved to the following location in Bob's workspace:
`realtime_deployment/runs/archive/chunk_exec_paused_20260529/`

**Consolidated Folders:**
- `baseline_simvla_chunk_exec_task7_100eps_rerun_v2_20260529/`
- `riskaware_actionmod_v2_strict_chunk_exec_task7_100eps_rerun_v2_20260529/`
- `baseline_simvla_chunk_exec_task7_100eps_h5_20260529/`
- `baseline_simvla_chunk_exec_task7_spotcheck_v2_20260529/`
- `chunk_exec_bad_audit_20260529/` (previously archived directory containing the unpatched runs)

---

## 6. CLI 1 Preflight Verification
All CLI 1 configurations, logs, and outputs relating to the 4-worker training/evaluation campaign were left completely untouched and are preserved in their original locations.
