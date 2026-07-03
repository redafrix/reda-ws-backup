# Risk-Aware SimVLA v2_018 Reproduction Package

This package contains the scripts, configs, detector artifacts, and reports needed to reproduce the risk-aware SimVLA experiments used in the 4-task deployment comparison.

## What This Is

The risk-aware policy wraps SimVLA inference with a temporal risk detector:

- Base VLA: SimVLA action chunk sampler.
- Risk detector: `v2_018_transformer_k16`.
- Detector architecture: transformer sequence model, history length `k=16`, width `128`, layers `3`, heads `4`, dropout `0.1`.
- Detector output: scalar risk score in `[0, 1]` for the current action candidate/context.
- Deployment policy: `risk_filtered_lowest_score_candidate_v2_strict_margin`.
- Calibration policy: score row threshold `q95` plus conformal episode mass threshold with `alpha=0.15`.

At runtime, the policy samples the normal/main SimVLA action chunk plus 8 extra candidate chunks. It scores the main and candidate chunks with the risk detector. If strict margin rules allow intervention, it executes the lowest-risk candidate; otherwise it executes the main action. The executed policy is still first-action-only receding horizon, not full chunk open-loop.

## Package Layout

- `fiper_ws/scripts/`
  - Training, split building, policy/evaluation, and analysis scripts for the `v2_018_transformer_k16` detector.
- `fiper_ws/configs/`
  - Current baseline detector config and campaign configs.
- `fiper_ws/current_baseline/`
  - Human-readable selected baseline definition.
- `fiper_ws/experiments/current_baseline_v2_018_20260528/`
  - Detector artifacts pulled from Bob.
  - Includes `model.pt`, `config.json`, `normalization.json`, `thresholds.json`, `policy_thresholds.json`, `FEATURE_AUDIT.json`, `metrics.json`, `summary.json`, and training histories.
  - Excludes heavy `scores.jsonl` files.
- `fiper_ws/realtime_deployment/scripts/`
  - Risk-aware rollout runner and same-seed baseline runner.
- `fiper_ws/realtime_deployment/configs/`
  - Exact 4-task deployment configs and 5000-seed plans.
- `fiper_ws/realtime_deployment/reports/`
  - Preflight, smoke, launch, status, and timing reports.
- `FOUR_TASK_RESULTS_SUMMARY.md`
  - Final paired comparison from Bob/Sam.
- `MANIFEST.json`
  - File list with SHA256 hashes.

## Main Training Path

Use this when training the detector on a new dataset.

1. Prepare or collect FIPER receding-horizon JSONL data.

   Required row-level inputs:
   - current proprioception
   - previous proprio/action/ACE history
   - main candidate action chunk, normalized
   - ACE candidate chunks, normalized
   - episode outcome label, success vs failure/timeout
   - no reward/success/future/object-pose leakage as detector inputs

2. Build experiment splits.

   Main scripts:
   - `fiper_ws/scripts/prepare_fiper_experiment_splits_v2.py`
   - `fiper_ws/scripts/build_target_object_pick_basket_splits_v2.py`
   - `fiper_ws/scripts/materialize_fiper_split.py`

   The previous deployment used three detector families:
   - `00_global_main`: used for `libero_10_with_milk/task7`
   - `01_ood_task_8_9`: used for `libero_10_with_milk/task8`
   - `fold_00_holdout_alphabet_soup_bbq_sauce`: used for fold00 seen/unseen object tasks

3. Train the temporal risk model.

   Main script:
   - `fiper_ws/scripts/run_clean_temporal_nextgen_campaign_v2.py`

   Current selected config:
   - `fiper_ws/configs/current_baseline_v2_018_transformer_k16.json`

   Relevant architecture parameters:
   - model kind: `transformer`
   - history steps: `16`
   - width: `128`
   - layers: `3`
   - heads: `4`
   - dropout: `0.1`

4. Verify feature hygiene.

   Every trained detector directory should contain `FEATURE_AUDIT.json`. It must confirm:
   - no reward input
   - no success input
   - no future timestep leakage
   - no object pose leakage
   - no OOD rows used for train in OOD split experiments

5. Calibrate policy thresholds.

   The selected deployment policy uses:
   - row score threshold from success calibration rows: `q95`
   - conformal mass threshold from success validation episodes
   - `alpha = 0.15`

   Supporting scripts:
   - `fiper_ws/scripts/analyze_transformer_k16_online_policy_v1.py`
   - `fiper_ws/scripts/analyze_ood_policy_sweep_from_scores_v1.py`

## Main Deployment Path

Use this when running risk-aware SimVLA on real rollouts.

1. Put the trained detector directory somewhere accessible.

   Required files:
   - `model.pt`
   - `config.json`
   - `normalization.json`
   - `thresholds.json` or `policy_thresholds.json`
   - `FEATURE_AUDIT.json`

2. Create a risk-aware config.

   Exact configs used in the 4-task comparison:
   - `fiper_ws/realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_seen_task7_20260529.json`
   - `fiper_ws/realtime_deployment/configs/riskaware_actionmod_v2_strict_sam_ood_task8_20260529.json`
   - `fiper_ws/realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_seen_butter_task2_20260529.json`
   - `fiper_ws/realtime_deployment/configs/riskaware_actionmod_v2_strict_bob_fold00_unseen_alphabet_soup_task0_20260529.json`

3. Run risk-aware rollout.

   Main script:
   - `fiper_ws/realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py`

   Important settings:
   - `action_selection_policy = risk_filtered_lowest_score_candidate_v2_strict_margin`
   - `ace_candidate_count = 8`
   - unique main and ACE sampling seeds enforced per timestep
   - first-action-only execution
   - action modification enabled only when strict risk-margin conditions pass

4. Run exact same-seed baseline.

   Main script:
   - `fiper_ws/realtime_deployment/scripts/run_baseline_simvla_same_seed_one_task_v1.py`

   This baseline replays the same reset seeds and, when available, the risk-aware main action sampling seeds. It does not use ACE, risk model scores, or action modification.

## Known Caveat For Same-Seed Baseline

The same-seed baseline is exact for reset seeds and ordered pairing. It also reuses risk-aware main action seeds while the risk-aware seed trace exists.

If a baseline episode lasts longer than the matching risk-aware episode, the baseline must generate fallback main action seeds for later timesteps. This happened in some 4-task episodes and is reported in `FOUR_TASK_RESULTS_SUMMARY.md`.

## Environment Assumptions

The scripts assume a SimVLA/LIBERO-PRO environment equivalent to the internship machines. Path variables are mostly controlled by `REDA_WS`, but a new machine may need path edits for:

- SimVLA modified checkout
- LIBERO-PRO checkout
- `asynchvla_ws/src`
- activation scripts
- MuJoCo/OpenGL variables

Useful reference:
- `REMOTE_EXPERIMENT_GUIDE.md`

## Minimal Files To Port To A New PC

For training from scratch:

- `fiper_ws/scripts/run_clean_temporal_nextgen_campaign_v2.py`
- split/materialization scripts in `fiper_ws/scripts/`
- `fiper_ws/configs/current_baseline_v2_018_transformer_k16.json`
- your new FIPER JSONL data

For inference with existing tested detectors:

- `fiper_ws/realtime_deployment/scripts/run_riskaware_simvla_one_task_v1.py`
- one detector directory under `fiper_ws/experiments/current_baseline_v2_018_20260528/.../jobs/v2_018_transformer_k16`
- matching realtime deployment config

For paired baseline comparison:

- `fiper_ws/realtime_deployment/scripts/run_baseline_simvla_same_seed_one_task_v1.py`
- same seed plan/config used by risk-aware
