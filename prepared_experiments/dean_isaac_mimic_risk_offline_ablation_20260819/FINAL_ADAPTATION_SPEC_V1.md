# FINAL ADAPTATION SPEC V1 — Isaac Round0 -> portable Mimic H10 Single-Head monitor

This file is the scientific/implementation decision. Agy does not modify it.

## 1. Primary experiment identity

Name: `isaac_mimic_h10_c0dyn_v1`

Machine: Dean only.

Source workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Source episodes:
`outputs/final_seen_h10_round_000_seed20260730`

No recollection. No Isaac rollout. No SimVLA reinference.

Reuse the frozen episode split exactly:
- train: 2800 episodes / 52825 rows / 64 failure episodes
- validation: 600 episodes / 11410 rows / 14 failure episodes
- held-out test: 600 episodes / 11368 rows / 14 failure episodes

Expected total: 4000 episodes, 3908 success, 92 failure, 75603 query rows.

## 2. Which Mimic contract controls this experiment

The original executable friend/W2A K1 risk-head source was not recovered after the Dean/Bob-disk search.

Therefore the PRIMARY implementation contract is the previously inspected user-provided portable H10 handoff, transcribed in:

`MIMIC_H10_HANDOFF_CONTRACT.md`

Use its:
- 37 current-query scalars;
- 10x6 horizon tensor;
- scalar encoder;
- H10 horizon Transformer;
- 64D query encoder;
- 1-layer temporal GRU hidden 128;
- eventual-failure target;
- optimizer/training constants;
- successful-episode-max calibration family.

Do NOT use the existing Isaac SeqRiskModel Transformer.
Do NOT construct a 74+16 hybrid.

One supplemental temporal choice is frozen from the paper-level selected K1 monitor because the portable transcription does not state a fixed query-window length:

**Temporal window = exactly 8 query records ending at the current query.**

Startup windows are LEFT zero-padded after feature standardization. No task ID, timestep, reward, future observation, scene ID or outcome-derived quantity enters the inputs.

## 3. Candidate subset — fixed before training

Round0 stores 9 genuine final H10 proposals:
- candidate0 = main
- alternatives 1..8

Portable handoff requires exactly 8 candidates.

Primary subset is frozen as:

`[candidate0, alternative1, alternative2, alternative3, alternative4, alternative5, alternative6, alternative7]`

Equivalently, main + the first seven alternatives in stored order.

The eighth stored alternative is not used in primary feature computation. It remains available only for audit/sensitivity work after the primary result is frozen.

No candidate is selected by outcome/risk/distance.

## 4. Action representation

Final-candidate disagreement and horizon features use the retained ENVIRONMENT action chunks, transformed into the portable handoff's 10D monitor representation:

`[translation3, rotation6d6, gripper1]`

The 7D->10D rotation conversion MUST be derived from two already-located source families:

A. Isaac Round0 actual 7D action-controller semantics in the canonical workspace.
B. Mimic geometry conversion source already found at:
`/mnt/ai/projects/simvla_reproduction_workspace/franka_wrist_camera_isaaclab/src/franka_wrist_camera_scene/mimic_video/geometry.py`

Do not guess Euler order, units, axis-angle convention or 6D row/column serialization.

Before materialization, create a small provenance JSON proving the exact mapping and round-trip tests. If exact parity cannot be established, STOP.

Internal denoising dynamics remain in SimVLA native NORMALIZED 7D space. Do not convert X_d/V_d to 10D.

## 5. Exact nine final-candidate disagreement scalars

Let C have shape [8,10,10] after the source-backed 7D->10D monitor conversion.

Use population variance (`ddof=0`). Pairwise quantities use the 28 unordered off-diagonal candidate pairs.

1. `w2a_action_variance_mean`
   = mean over H10 and 10 action coordinates of Var_candidate(C)

2. `w2a_action_variance_max`
   = maximum over H10 and 10 coordinates of Var_candidate(C)

3. `w2a_pairwise_mse_mean`
   = mean over the 28 unordered candidate pairs of mean((Ci-Cj)^2) over all 10x10 entries

4. `w2a_first_candidate_vs_mean_mse`
   = mean((C0 - mean_candidate(C))^2)

For position endpoints, cumulative position for candidate c at horizon index h is:
`P[c,h] = sum_{k=0..h} C[c,k,0:3]`.

5. `w2a_endpoint_position_spread_mean_m`
   = mean pairwise Euclidean distance over the 28 pairs using P[:,9]

6. `w2a_endpoint_position_spread_max_m`
   = max pairwise Euclidean distance over the 28 pairs using P[:,9]

7. `w2a_position_variance_mean`
   = mean Var_candidate(C[:,:,0:3])

8. `w2a_rotation_variance_mean`
   = mean Var_candidate(C[:,:,3:9])

9. `w2a_gripper_variance_mean`
   = mean Var_candidate(C[:,:,9])

## 6. Exact 10x6 horizon tensor

For each horizon index h=0..9:

1. `position_variance_mean[h]`
   = mean over xyz of Var_candidate(C[:,h,0:3])

2. `position_variance_max[h]`
   = max over xyz of Var_candidate(C[:,h,0:3])

3. `rotation_variance_mean[h]`
   = mean over 6D rotation coordinates of Var_candidate(C[:,h,3:9])

4. `gripper_variance[h]`
   = Var_candidate(C[:,h,9])

5. `cumulative_position_spread_mean[h]`
   = mean pairwise L2 distance over P[:,h]

6. `cumulative_position_spread_max[h]`
   = max pairwise L2 distance over P[:,h]

Result shape is exactly [10,6].

## 7. Candidate0 exact denoising reconstruction

Round0 preserves:
- initial_noise [10,7]
- update_vector_trace [10,70]
- final_action_normalized [10,7]

Source-backed dt = -0.1.

For denoising index d=0..9:

`X_0 = initial_noise`

`X_d = initial_noise + sum_{i=0}^{d-1} U_i`, for d=1..9,
where `U_i = update_vector_trace[i].reshape(10,7)`.

`X_10 = final_action_normalized` is retained for parity only and is the post-step final state.

`V_d = U_d / (-0.1) = -10 * U_d`, d=0..9.

Every materialized query MUST assert:
`X_10_from_updates = initial_noise + sum_{i=0..9} U_i`
matches `final_action_normalized` within a frozen numerical tolerance selected from source dtype (default max_abs <= 1e-5; if violated, STOP and report before changing tolerance).

## 8. Twenty-five denoising-dynamics scalars — exact Isaac proxy definition

The portable handoff expects five cross-candidate denoising traces. Alternatives' intermediate X_d/V_d do not exist in Round0 and SHALL NOT be fabricated.

To preserve the handoff's 5-trace x 5-summary structure, use five genuine candidate0 denoising traces computed from exact reconstructed X_d/V_d. These are explicitly named C0 proxies and are not described as cross-candidate dynamics.

For each d=0..9:

A. `c0_residual_to_final_mse[d]`
   = mean((X_d - X_10)^2) over 10x7

B. `c0_state_variance_max[d]`
   = max over the 7 action coordinates of population variance across the 10 H10 action indices in X_d[:,j]

C. `c0_state_variance_mean[d]`
   = mean over the 7 action coordinates of population variance across the 10 H10 action indices in X_d[:,j]

D. `c0_velocity_mse_mean[d]`
   = mean(V_d^2) over 10x7

E. `c0_vector_field_l2_mean[d]`
   = mean over the 10 H10 action indices of ||V_d[h,:]||_2

For EACH of A..E, summarize in this exact order:
1. first = trace[0]
2. last = trace[9]
3. mean
4. max
5. last_minus_first = trace[9]-trace[0]

Concatenate A then B then C then D then E -> exactly 25 scalars.

The following genuine saved traces are retained in the derived audit sidecar but NOT fed to the primary model because they are not needed to fill the frozen 5x5 proxy contract:
- denoise_mean_trace
- velocity_norm_trace
- update_norm_trace
- path_variance
- last_step_variance

## 9. Three temporal-change scalars

At current query q:

1. `history_available` = 0 if q=0 else 1
2. `abs_delta_action_variance_mean`
   = 0 if q=0 else abs(current w2a_action_variance_mean - previous query value)
3. `abs_delta_endpoint_spread_mean`
   = 0 if q=0 else abs(current w2a_endpoint_position_spread_mean_m - previous query value)

Total current-query scalar vector:
`9 + 25 + 3 = 37`.

## 10. Query encoder and temporal model — exact primary architecture

Current-query scalar branch:
- input 37
- Linear(37,128)
- LayerNorm(128)
- GELU
- Dropout(0.1)

Horizon branch:
- input [10,6]
- Linear(6,128)
- learned positional embedding [10,128]
- TransformerEncoder: 2 layers, 4 heads, FFN 512, dropout 0.1
- mean pool over H10 -> 128

Fuse current query:
- concat scalar 128 + horizon 128 -> 256
- Linear(256,128)
- GELU
- Dropout(0.1)
- Linear(128,64)
- GELU
= query embedding 64

Temporal window:
- exactly 8 query embeddings ending at current query
- left zero padding for startup
- GRU input=64, hidden=128, num_layers=1, batch_first=True
- take final GRU output/state corresponding to the 8-slot window
- Linear(128,1) -> risk logit
- sigmoid only for evaluation/calibration

No task/timestep/reward/future/scene identifiers.

## 11. Dataset and normalization

Derived heavy dataset root:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`

Do not modify `$W/frozen_datasets/isaac_seen_h10_topk8_v1`.

For every accepted Round0 query store:
- episode_id
- decision_index
- split
- label
- scalar37 float32
- horizon10x6 float32
- source hashes / candidate subset declaration
- audit-only candidate0 reconstruction parity values

Feature normalization:
- fit ONLY on train split
- scalar37: per-coordinate mean/std
- horizon10x6: per-channel mean/std using all train queries and all 10 horizon positions, producing 6 channel means/stds
- std floor = 1e-6
- apply before 8-query window zero-padding so padded zeros represent train mean

Labels are unchanged parent episode failure labels.

## 12. Training

Training unit = one query-centered 8-record window.

Use every train query once per epoch.

Loss:
`BCEWithLogitsLoss(pos_weight = N_negative_train_rows / N_positive_train_rows)`
where counts are computed mechanically from TRAIN only and written to manifest.

Do not use synthetic failures or OOD rows.

Fixed handoff hyperparameters:
- batch size 64
- epochs 25
- AdamW
- lr 1e-3
- weight_decay 1e-4
- grad_clip_norm 1.0
- dropout 0.1
- seeds 0,1,2,3,4

For each seed independently:
- train 25 epochs
- checkpoint each epoch
- select epoch with highest validation row AUPRC
- tie -> earliest epoch

No cross-seed cherry-picking.

Primary deterministic model for controller-style reporting = seed 0.
Seeds 1..4 are robustness repeats and all are reported.

Model root:
`$W/models/isaac_mimic_h10_c0dyn_v1/seed_<seed>`

## 13. Calibration — validation only

For each frozen seed checkpoint:

Compute query risk scores on validation episodes.
For each SUCCESSFUL validation episode e:
`g_e = max_t score[e,t]`.

Friend-style corrected episode-max threshold at alpha:
`k = min(n, ceil((n+1)*(1-alpha)))`
`tau_alpha = k-th order statistic of sorted successful validation episode maxima`.

Required alphas:
- 0.05
- 0.10 PRIMARY
- 0.15

Also record supplementary validation-derived thresholds:
- fixed 0.5
- row-level best-F1
- empirical successful-episode-max q90/q95/q99

No test/OOD score may influence any threshold.

## 14. Held-out test metrics

Only after models + thresholds are frozen.

For each seed and threshold report:
- row AUROC
- row AUPRC
- successful episode false alarms: count / 586 and percent
- failed episode detection: count / 14 and percent
- Det@25: count / 14 and percent
- Det@50: count / 14 and percent
- never detected: count / 14
- first-alarm normalized timing for detected failures

Use the existing Isaac evaluator's frozen Det@25/Det@50 timing convention for direct comparability; do not redefine it.

Primary operating point = seed0, alpha=0.10.
Also report all five seeds and mean/std as robustness, but never hide the integer denominators.

## 15. OOD lock

OOD150/OOD400 are not touched until:
- derived dataset is frozen;
- all five seen models are trained;
- validation thresholds are frozen;
- held-out seen test result is generated.

Only after that may the seed0 alpha=0.10 checkpoint/threshold be applied unchanged to OOD150 as a transfer test.

## 16. Invalid paths explicitly prohibited

- no reuse of invalid commit 70327b4b candidate trace reconstruction
- no alternative X_d/V_d fabrication
- no linear interpolation between initial noise and final chunks
- no policy reinference
- no new simulator state restoration
- no task ID/timestep leakage
- no resplitting the 4000 episodes
- no use of test/OOD for feature or threshold decisions
