# Protocol Amendment 01 — Goal-Object split correction

This amendment supersedes only the split-allocation subsection of `PROTOCOL.md`. All other protocol requirements remain unchanged.

Reason: the original 600/200/200 allocation had training, development and calibration but no independent held-out seen Goal-Object test set. Because the stated primary outputs include false-alarm/detection metrics on seen data, an untouched seen test assignment is required.

## Correct 1000-episode design

Official LIBERO-PRO Goal-Object only, 10 tasks, 50 official init states per task, 2 independent policy-sampling seeds per `(task_id, init_state_idx)`.

The two policy-seed replicas from the same init state must always remain in the same assignment.

Assignment by official init-state index, identically for all 10 tasks:

- `train`: init states 0..24 -> 25 x 2 x 10 = **500 episodes**
- `id_development`: init states 25..34 -> 10 x 2 x 10 = **200 episodes**
- `seen_test`: init states 35..44 -> 10 x 2 x 10 = **200 episodes**
- `successful_calibration_pool`: init states 45..49 -> 5 x 2 x 10 = **100 episodes**

Total planned collection: **1000 complete episodes**.

No query-level/random splitting is permitted. No init-state group may cross assignments.

## Training / selection / threshold rules

- feature normalization: fit on `train` only
- positive-class weight: derive from `train` only
- checkpoint/model-seed selection: `id_development` only
- `seen_test`: untouched until architecture/checkpoint/model-seed are frozen
- operating thresholds: derive only from **successful episodes** inside `successful_calibration_pool`
- if fewer than 100 calibration-pool episodes are successful, use the actually available successful calibration episodes and report their count; do not move episodes from train/dev/test and do not collect adaptive extra episodes after seeing model scores
- no OOD data may influence training, checkpoint selection, normalization, thresholds, or model-seed choice

This amendment is frozen before any new data collection begins.
