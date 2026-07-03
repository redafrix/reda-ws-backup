# Worklog

## 2026-06-05 - Audit

- Confirmed Bob has the official SimVLA checkpoint and modified checkpoint 60000.
- Confirmed checkpoint hashes:
  - official: `9d3b1767773da86906d771b1eca2c2911087371bf8b3890a7336b6773270f6be`
  - modified: `3fab12d94c963f530ddce9f66aed4bf2623b2a2bbd527c85918fce2fcf8aec71`
- Confirmed current detector identities:
  - base static dimension 43
  - Top-8 static dimension 51 with fixed dimensions `[6,21,25,27,23,2,26,24]`
- Confirmed Bob can SSH directly to Dean as user `dean`.
- Confirmed the exact chunk10 dataset has 200 completed episodes.
- Confirmed the exact receding dataset was still running and must be gated at 200.

## 2026-06-05 - Implementation

- Created a portable policy runner with baseline, shadow, and active modes.
- Added execution horizons 1 and 10 with query-cadence history semantics.
- Allowed the base detector with official SimVLA.
- Kept Top-8 restricted to modified SimVLA.
- Added exact BDDL/init-state manifest verification.
- Added resumability and action/chunk hash logging.
- Added a generic trainer for the two frozen architectures with native or
  stride-10 query cadence.
- Added direct Dean-to-Bob dataset synchronization with completion gates.
- Added a resumable dependency-aware scheduler and supervisor.
- Generated 371 queued jobs, including 100-episode paired evaluations.

## Next

1. Copy the campaign tree to Bob.
2. Run static validation and smoke the distinct runtime/training branches.
3. Launch the sequential supervisor in tmux.
4. Verify the first production job and campaign heartbeat.

## 2026-06-05 - Prelaunch Validation and Launch

- Added `CUBLAS_WORKSPACE_CONFIG=:4096:8` after the first foreground smoke
  exposed a cuBLAS determinism warning.
- Re-ran all 16 distinct runtime branches after cleaning smoke outputs:
  - original and modified checkpoints
  - baseline, base shadow, base active, Top-8 shadow, Top-8 active where valid
  - execution horizons 1 and 10
- All 16 runtime smokes passed with zero errors.
- Baseline and shadow traces matched exactly for every comparable branch:
  query index, environment timestep, main action seed, and main chunk SHA-256.
- No post-fix smoke log contained the cuBLAS determinism warning.
- Native chunk10 training smoke passed for both detector architectures and both
  configured splits using 200 episodes and 2,657 policy queries.
- Installed a Bob crontab reboot hook for `src/start_campaign.sh`.
- Launched tmux session `bob_risk_matrix_20260605`.
- Verified the first production job was healthy at 8/100 episodes with zero
  errors, zero seed collisions, and GPU inference active.

## 2026-06-05 - Balanced Cohort Correction

- Detected that the source identity CSV is grouped by task. Taking rows 0-99
  would cover only task IDs 0-4.
- Stopped the queue before the first baseline completed.
- Archived the partial eight-episode pre-correction run under
  `archive/pre_balanced100_20260605_175506/`.
- Added `exact_episodes_per_task=10` filtering in the runner.
- Verified the corrected cohort contains exactly 100 episodes with 10 episodes
  for each task ID 0 through 9.
- Restarted from a clean scheduler state. The corrected baseline passed task 0
  and advanced into task 1 with no errors or seed collisions.
- Added soft sequencing dependencies so a failed rollout cannot block unrelated
  later experiments. Dataset and model artifact dependencies remain hard.
