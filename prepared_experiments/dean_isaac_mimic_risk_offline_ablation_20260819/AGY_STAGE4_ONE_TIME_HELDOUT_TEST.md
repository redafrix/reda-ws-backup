# Stage 4 — ONE-TIME held-out seen evaluation

This stage opens the frozen held-out seen test exactly once for the already-frozen models. Scientific design is closed.

Machine: Dean only.
Canonical workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Experiment: `isaac_mimic_h10_c0dyn_v1`

## Frozen references that MUST match before any test score is computed

Dataset manifest V2 SHA256:
`043f894e82c8cfc94c1ba8a5c788064a31d33f6112d1eefe09cbe14da40977d3`

Normalization SHA256:
`40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`

Training freeze SHA256:
`8d84010c2989d605a910775e4a762e084f9b34de6855b323781356d3258876a0`

All-seed validation freeze SHA256:
Use the actual Dean `VALIDATION_FREEZE_ALL_SEEDS.json` and verify it against the Stage3 recorded hash before scoring. Hard stop on mismatch.

Primary seed is PREDECLARED and immutable:
`seed = 0`

Primary operating point is PREDECLARED and immutable:
`conformal_alpha_0.10`

Primary seed0 checkpoint SHA256:
`4869526f636dc005b4cbcd85c8cfce1f307618fed9f81784f3fd3ee3c3180cf3`

Primary seed0 validation threshold:
`0.736110270023346`

Frozen best checkpoints:
- seed0: `4869526f636dc005b4cbcd85c8cfce1f307618fed9f81784f3fd3ee3c3180cf3`
- seed1: `9328a8102060bb46414b8f8bd3f71eedd61f4ce93949822dfe2138d4b9a40590`
- seed2: `199a17c2a34c56f4807869f2aa8cc556ba43a39c2bb000719612971ab1ccb693`
- seed3: `f745aa5392918b56135710e7cdb05e2a15c9bc19e9cd03284e5c9885fcfb20a8`
- seed4: `15825ca05155b6ba1248b5542454ae33bd210d77cf86522ceb28e28567d90cb7`

Expected held-out split:
- 600 episodes
- 586 successes
- 14 failures
- 11,368 query rows

## Absolute prohibitions

DO NOT:
- retrain any model;
- change any checkpoint;
- choose a different epoch;
- choose a best seed from test results;
- modify thresholds after seeing test;
- recalibrate on test;
- modify any feature/model/normalization;
- score OOD150/OOD400;
- launch Isaac Sim or SimVLA inference;
- touch HARD1000;
- overwrite validation freeze artifacts.

All five seeds are robustness repeats only. Seed0 remains the primary result even if another seed is better on test.

## 1. Pre-test cryptographic gate

Before reading/scoring test rows:

For each seed 0..4 verify:
- best checkpoint SHA matches frozen training freeze;
- validation freeze file exists;
- validation freeze checkpoint SHA matches that exact checkpoint;
- validation freeze dataset manifest SHA matches frozen V2;
- validation freeze normalization SHA matches frozen normalization;
- validation freeze selected epoch matches training freeze;
- validation threshold dictionary exists and contains exactly the frozen threshold families;
- seed identity matches.

Verify heavy arrays against `dataset_manifest_v2.json` hashes BEFORE test scoring.

If any mismatch: STOP without scoring test.

Write a small pretest gate JSON before scoring:
`evaluations/isaac_mimic_h10_c0dyn_v1/heldout_seen/PRETEST_GATE.json`

## 2. One-time scoring

Score held-out split exactly once for seeds 0,1,2,3,4.

Use production `run_held_out_test()` or a thin orchestrator around it. Do not duplicate/reimplement metric formulas.

For each seed apply ONLY that seed's own frozen validation-derived thresholds:
- fixed_0.5
- conformal_alpha_0.05
- conformal_alpha_0.10
- conformal_alpha_0.15
- empirical_q90
- empirical_q95
- empirical_q99
- row_best_f1

No test-derived threshold is allowed.

Save per-seed result:
`evaluations/isaac_mimic_h10_c0dyn_v1/heldout_seen/seed_<s>/HELD_OUT_TEST_RESULTS.json`

Also save raw test scores for forensic reproducibility OUTSIDE Git:
`.../seed_<s>/test_scores.npz`
with:
- score per query
- target per query
- episode index
- decision index

The score NPZ must not be used for any tuning.

## 3. Required primary result

Primary result = seed0 + `conformal_alpha_0.10`.

Report mechanically:
- threshold
- test row AUROC
- test row AUPRC
- success false alarms = integer / 586 and percent
- failure detection = integer / 14 and percent
- Det@10 = integer / 14 and percent
- Det@25 = integer / 14 and percent
- Det@50 = integer / 14 and percent
- never detected = integer / 14
- mean first alarm fraction among detected failures

Do not replace counts with percentages.

## 4. Robustness reporting

For all five seeds at each seed's `conformal_alpha_0.10` threshold, report the same episode metrics and row AUROC/AUPRC.

Compute mean/std across the five seeds for:
- row AUROC
- row AUPRC
- success false-alarm percentage
- failure-detection percentage
- Det@25 percentage
- Det@50 percentage

This is robustness reporting only. Do NOT select the best seed.

## 5. Full threshold table for seed0

For seed0 report all eight frozen operating points with:
- threshold
- success FA count/586
- failure detected count/14
- Det@10 count/14
- Det@25 count/14
- Det@50 count/14

## 6. Existing Isaac TopK8 comparison — same frozen held-out seen test

Read the already-existing TopK8 held-out seen results from the frozen Isaac evaluation artifacts only. DO NOT rerun/retrain it.

Mechanically establish that the comparison uses the SAME 600 held-out episode membership as this Mimic-style test. Compare episode-ID/fingerprint membership; hard stop on mismatch.

Create a comparison JSON containing only source-backed values:
- existing TopK8 row AUROC/AUPRC if available
- its frozen operating points and success-FA/failure-detection/Det@25/Det@50 values if available
- Mimic-style seed0 primary alpha=.10 result

Do NOT force threshold-to-threshold equivalence where calibration semantics differ. Label each operating point by its own calibration rule.

If exact same membership cannot be proven, mark comparison `NOT_DIRECTLY_COMPARABLE` and do not calculate deltas.

## 7. Freeze

Create:
`evaluations/isaac_mimic_h10_c0dyn_v1/heldout_seen/HELDOUT_SEEN_FREEZE.json`

It must contain:
- pretest gate SHA256
- dataset manifest SHA256
- normalization SHA256
- training freeze SHA256
- all-seed validation freeze SHA256
- all five checkpoint SHA256s
- all five validation-freeze SHA256s
- all five per-seed held-out result SHA256s
- primary seed = 0
- primary operating point = conformal_alpha_0.10
- primary result
- robustness aggregates
- explicit `test_used_for_selection=false`
- explicit `ood_scored=false`

Copy ONLY small JSON/summary artifacts into Git under:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/heldout_snapshot/`
Do not commit NPZ scores or model weights.

## 8. Independent integrity checks before commit

Mechanically verify:
- each test result has exactly 11,368 rows;
- each test result has exactly 600 episodes / 586 success / 14 failure;
- all five use identical test membership;
- no threshold differs from its corresponding validation freeze;
- seed0 checkpoint SHA and alpha=.10 threshold exactly match the predeclared values above;
- no test score path appears in any training/validation config or selection artifact;
- OOD has not been scored.

Commit exactly:
`experiment(dean): freeze one-time held-out Mimic H10 seen results`

Push branch.

## RETURN ONLY

PRETEST_GATE:
status:
dataset_manifest_sha256:
normalization_sha256:
training_freeze_sha256:
all_seed_validation_freeze_sha256:
checkpoint_and_freeze_bindings_all_match:

PRIMARY_SEED0_ALPHA010:
threshold:
row_auroc:
row_auprc:
success_false_alarms: <count>/586 | <percent>
failure_detection: <count>/14 | <percent>
det10: <count>/14 | <percent>
det25: <count>/14 | <percent>
det50: <count>/14 | <percent>
never_detected: <count>/14
mean_first_alarm_fraction:

ROBUSTNESS_ALPHA010:
seed0: <AUROC> | <AUPRC> | <FA count>/586 | <failure count>/14 | <det25 count>/14 | <det50 count>/14
seed1: ...
seed2: ...
seed3: ...
seed4: ...
mean_std_auroc:
mean_std_auprc:
mean_std_fa_percent:
mean_std_failure_detection_percent:
mean_std_det25_percent:
mean_std_det50_percent:

SEED0_ALL_THRESHOLDS:
fixed_0.5: <threshold> | <FA>/586 | <failure>/14 | <det10>/14 | <det25>/14 | <det50>/14
conformal_alpha_0.05: ...
conformal_alpha_0.10: ...
conformal_alpha_0.15: ...
empirical_q90: ...
empirical_q95: ...
empirical_q99: ...
row_best_f1: ...

TOPK8_COMPARISON:
membership_exact_match:
source_result_path:
source_operating_point:
topk8_metrics:
mimic_primary_metrics:
deltas_if_directly_comparable:

HELDOUT_FREEZE_SHA256:

TEST_USED_FOR_SELECTION:
NO

OOD_SCORED:
NO

ISAAC_SIM_LAUNCHED:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
