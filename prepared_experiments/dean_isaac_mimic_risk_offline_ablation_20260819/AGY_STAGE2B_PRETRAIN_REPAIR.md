# Stage 2B — mandatory pre-training repair and integrity freeze

Agy is an operator/coder. The scientific design in `FINAL_ADAPTATION_SPEC_V1.md` remains frozen and MUST NOT change.

Machine: Dean only.
Canonical workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`
Derived dataset: `$W/derived_datasets/isaac_mimic_h10_c0dyn_v1`
Branch: `experiment/dean-isaac-mimic-risk-offline-ablation-20260819`

## Absolute rules

- NO training in this stage.
- NO validation scoring with an actual trained model.
- NO held-out test scoring.
- NO Isaac Sim.
- NO SimVLA inference.
- NO recollection.
- NO feature redesign.
- NO architecture redesign.
- DO NOT touch HARD1000, OOD150 or OOD400.
- Do not rewrite heavy feature arrays unless an integrity check below fails.

The materialized feature values from Stage2 are provisionally accepted. This stage repairs code/provenance/guards before training.

## 1. Fix the trainer CLI crash

In `implementation/train.py`, the current final print incorrectly references undefined variables:

`res[best_epoch]` and `res[best_val_auprc]`.

Fix it to use literal dictionary keys:

`res['best_epoch']`
`res['best_val_auprc']`

Add a unit test that executes `main()` or an equivalent CLI path with `train_single_seed` mocked, and proves the post-seed reporting path does not raise and can continue across multiple seeds.

Do not train a model for this test.

## 2. Hard-bind the action adapter to the accepted Round0 runtime

The current provenance identifies an Isaac controller source in the reproduction workspace, but Stage2 must prove it is the semantics actually bound to accepted Round0.

Mechanically trace accepted Round0 manifests/source fingerprints/configs to the exact controller/action implementation used during `final_seen_h10_round_000_seed20260730`.

Create:
`source_provenance/ROUND0_ACTION_BINDING.json`

It must include:
- accepted Round0 manifest path + SHA256;
- runtime/collector source path + SHA256;
- action/controller source path actually referenced/bound by that runtime;
- exact 7D layout and units;
- whether the reproduction-workspace `reaching_pose_actions.py` is byte-identical, source-equivalent by recorded hash/commit, or merely a later copy;
- evidence chain from Round0 -> runtime -> action conversion.

Require one of:
- `BYTE_IDENTICAL_TO_ROUND0_SOURCE`
- `RECORDED_HASH_OR_COMMIT_EQUIVALENT`

If neither can be proven, STOP and return ACTION_BINDING_INCOMPLETE. Do not train.

Do not change the 7D->10D formula if binding succeeds.

## 3. Repair materializer safety — no silent defaults

In `implementation/materialize.py`, replace silent defaults for split/label with hard failures.

Current unsafe behavior includes equivalents of:
- missing split -> `train`
- missing label -> `0`

New requirements:
- every one of the 4000 accepted episode IDs must exist in the frozen split mapping;
- split must be exactly one of train/validation/test;
- episode label must be explicitly present and in {0,1};
- every episode directory included must contain its accepted risk row file;
- zstd subprocess return code must be checked and must equal 0;
- total rows must equal 75603;
- episode counts must equal 2800/600/600;
- row counts must equal 52825/11410/11368;
- failure episode counts must equal 64/14/14;
- query key `(episode_id, decision_index)` must be unique globally;
- decision indices inside each episode must be contiguous from 0 to N-1 and rows must be in that order.

Add production integrity function(s) that can audit the ALREADY MATERIALIZED arrays against source rows without rewriting feature arrays.

## 4. Freeze a complete V2 derived-dataset manifest without changing feature arrays

Do NOT rematerialize heavy arrays if integrity checks pass.

Create:
`$W/derived_datasets/isaac_mimic_h10_c0dyn_v1/dataset_manifest_v2.json`

and a small Git mirror summary under:
`prepared_experiments/dean_isaac_mimic_risk_offline_ablation_20260819/audit/DATASET_FREEZE_V2.json`

V2 manifest MUST contain:
- original Stage2 dataset manifest SHA256 `730ac7e73ac31047490b81c00955bc1d46fd809e016069a530a71f2112ae3ef3`;
- normalization SHA256 `40ff9aeab3adfd80d30ac7b689733a55d9551a780ebd80b2789805cee7e60e0a`;
- source Round0 run manifest path + SHA256;
- source frozen dataset manifest SHA256;
- source split_assignments SHA256;
- `FINAL_ADAPTATION_SPEC_V1.md` Git blob/content SHA256;
- action-adapter provenance file SHA256;
- Round0 action-binding provenance SHA256;
- implementation file SHA256s for constants/action_adapter/c0_dynamics/candidate_features/dataset/model/train/evaluate/calibration/metrics/materialize;
- feature scalar order: all 37 names in exact order;
- horizon channel order: all 6 names;
- candidate subset declaration main+alt1..7;
- row/episode counts and failure episode counts;
- train positive/negative row counts and pos_weight;
- SHA256 for each heavy NPY array: scalar37, horizon10x6, labels, episode_index, decision_index, split_index;
- duplicate-query count (must 0);
- noncontiguous-decision episode count (must 0);
- all-finite result;
- C0 recurrence parity result/worst error;
- explicit `held_out_test_not_scored=true`.

## 5. Add missing validation row best-F1 threshold

`FINAL_ADAPTATION_SPEC_V1.md` requires supplementary validation-derived row best-F1. Current `calibration.py` does not implement it.

Implement a pure function:

`compute_best_f1_threshold(y_true, y_scores)`

Alarm convention remains `score >= threshold`.

Algorithm:
- candidate thresholds = sorted unique finite validation scores;
- compute binary F1 for every candidate threshold using validation rows only;
- maximize F1;
- deterministic tie-break: choose the HIGHEST threshold among equal-max-F1 candidates (more conservative false-alarm behavior);
- return threshold, F1, precision, recall.

`run_validation_and_calibrate` must add:
- `row_best_f1_threshold`
- its validation F1/precision/recall

to `FROZEN_VALIDATION_SELECTION.json`.

This is SUPPLEMENTARY. Primary threshold remains conformal alpha=0.10.

Add exact unit tests including ties.

## 6. Strengthen validation freeze and held-out-test leakage guard

Current evaluator only checks that a freeze JSON exists. That is insufficient.

When writing `FROZEN_VALIDATION_SELECTION.json`, include and freeze:
- model checkpoint absolute path;
- model checkpoint SHA256;
- seed;
- selected epoch;
- training summary SHA256;
- derived `dataset_manifest_v2.json` SHA256;
- normalization SHA256;
- `FINAL_ADAPTATION_SPEC_V1.md` SHA256;
- implementation Git commit;
- validation row count;
- validation episode count;
- validation failure episode count;
- all calibrated thresholds.

Before held-out test scoring, `run_held_out_test` MUST verify:
- supplied checkpoint SHA exactly equals frozen checkpoint SHA;
- dataset_manifest_v2 SHA exactly equals frozen SHA;
- normalization SHA exactly equals frozen SHA;
- implementation/spec hashes match;
- split counts still match frozen values.

If any mismatch: refuse test evaluation.

Add unit tests proving a wrong checkpoint or modified normalization causes refusal.

## 7. Verify Det@25 / Det@50 convention BEFORE test use

Do not redefine the experiment.

Locate the existing Isaac offline evaluator/metric source used for the previous true-H10 detector reports on Dean.

Mechanically compare its first-alarm normalized timing convention against current `compute_episode_evaluation`.

Create:
`source_provenance/EPISODE_TIMING_METRIC_PARITY.json`

Record:
- previous evaluator path + SHA256 + function;
- exact formula for normalized first-alarm time;
- exact Det@25 and Det@50 inequalities;
- current formula;
- parity YES/NO.

If parity is NO, modify `implementation/metrics.py` to match the PREVIOUS ISAAC evaluator exactly and add fixture tests.

Do not inspect any test-set scores to do this; source-code parity only.

## 8. Training reproducibility guard

Keep the fixed seeds 0..4 and existing optimizer/hyperparameters.

Add to `set_seed` / trainer manifest:
- Python seed;
- NumPy seed;
- torch CPU seed;
- torch CUDA seed;
- DataLoader shuffle generator explicitly seeded with the same seed;
- `num_workers=0` fixed;
- record torch version/CUDA version/device name.

Do NOT force deterministic algorithms if they would change/disable required Transformer kernels; simply record the runtime determinism flags and all seeds.

## 9. Pretraining integrity run

Run all unit tests after repairs.

Then run the full source-vs-derived integrity audit over all 75,603 rows WITHOUT rewriting heavy arrays.

Require:
- action binding complete;
- 4000 episodes;
- 75603 unique query rows;
- exact split rows/episodes;
- failure episodes 64/14/14;
- NPY hashes recorded;
- all finite;
- recurrence parity worst max abs remains 0.0 or <=1e-5;
- test scores still never computed.

NO training.

## 10. Git

Commit small code/tests/provenance/audit summaries only.
Do not commit heavy arrays.

Commit message exactly:
`fix(dean): harden Isaac Mimic pretraining freeze and leakage guards`

Push branch.

## RETURN ONLY

ACTION_BINDING:
status:
round0_manifest_sha256:
controller_source:
controller_sha256:
relationship_to_adapter_source:

DATASET_FREEZE_V2:
manifest_path:
manifest_sha256:
rows:
episodes:
train/val/test_rows:
train/val/test_episodes:
train/val/test_failure_episodes:
duplicate_queries:
noncontiguous_episodes:
all_finite:
recurrence_worst_max_abs:
normalization_sha256:
heavy_array_hashes_recorded:

CODE_REPAIRS:
trainer_cli_fixed:
best_f1_added:
freeze_checkpoint_binding_added:
test_guard_hash_binding_added:
dataloader_seeded:

TIMING_METRIC_PARITY:
status:
previous_source:
formula:

TESTS:
passed:
total:

TRAINING_RUN:
NO

VALIDATION_MODEL_SCORING_RUN:
NO

TEST_EVAL_RUN:
NO

ISAAC_SIM_LAUNCHED:
NO

HARD1000_TOUCHED:
NO

COMMIT:
<sha or NONE>
