# AGY Stage 7 — Strict Mimic Fidelity V2 one-time held-out seen evaluation

## Role
Mechanical execution only. Scientific design is frozen. Do not optimize for a better or worse result.

## Workspace / branch
Dean only.

Canonical workspace:
`/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`

Branch:
`experiment/dean-isaac-mimic-risk-offline-ablation-20260819`

Experiment:
`isaac_mimic_h10_strict_missingdyn_v2`

## Frozen Stage 6 identities
Before any held-out scoring, require exact equality for all of the following:

- dataset manifest SHA256: `852ad05e6208caba23c630174eb6784793304281169e5e24a25da22d030b57a1`
- normalization SHA256: `d055a71bc2e531264f35d8bdd91e545d3f3b39cbba1cc543699ec1b987107830`
- training freeze SHA256: `ecf7fa8e2b8b755663f81dfd1e2b63c2bd578a1da03ee38ea1a94bc24128d6fd`
- primary seed: `0`
- primary operating point: `conformal_alpha_0.10`
- primary seed0 checkpoint SHA256: `78b801c9071561108dded63d4e4b43fcf3b423932864f6817f808d6268e17fe6`
- primary seed0 alpha0.10 threshold: `0.6284286379814148`

Also verify every seed checkpoint SHA and every validation-freeze SHA from Stage 6 against `TRAINING_FREEZE.json` before scoring.

If any mismatch occurs: STOP BEFORE TEST SCORING.

## Dataset fidelity gate before scoring
Mechanically verify on the frozen V2 arrays:

- total rows = 75,603
- held-out test rows = 11,368
- held-out test episodes = 600
- held-out successes = 586
- held-out failures = 14
- scalar dims 9..33 are exactly zero for every held-out test row
- scalar dims 0..8 exactly equal the corresponding V1 frozen rows
- scalar dims 34..36 exactly equal the corresponding V1 frozen rows
- horizon10x6 exactly equals V1 frozen rows
- same episode IDs, split assignment, decision indices, and labels as the V1/TopK8 frozen source split

Prove exact TopK8 test membership from the frozen split assignments; do not rely on counts alone and do not compare local integer episode indices to source episode-ID strings.

## One-time held-out scoring
Only after every gate above passes:

Score the already-frozen strict V2 checkpoints for seeds 0,1,2,3,4 exactly once on the held-out seen split.

Use each seed's own already-frozen validation thresholds. Do not recompute or modify thresholds from test scores.

For every seed report threshold-independent row AUROC/AUPRC once, plus episode metrics for all frozen thresholds.

Primary result is permanently:
- seed = 0
- operating point = `conformal_alpha_0.10`
- threshold = `0.6284286379814148`

For the primary result report:
- row AUROC
- row AUPRC
- success false alarms count / 586 and percent
- failure detection count / 14 and percent
- Det@10 count / 14 and percent
- Det@25 count / 14 and percent
- Det@50 count / 14 and percent
- never detected count / 14
- mean first-alarm fraction

For robustness at alpha0.10 report the same key metrics for all five seeds and mean/std, while preserving raw denominators.

## Matched TopK8 comparison
Use only the EXISTING frozen TopK8 held-out seen result. Do not rerun TopK8.

Only after exact 600/600 test membership is proven, record two comparisons:

1. threshold-independent:
   - TopK8 AUROC/AUPRC vs strict V2 seed0 AUROC/AUPRC

2. matched validation calibration rule:
   - TopK8 `best_val_f1` vs strict V2 `row_best_f1`
   - success false alarms
   - failure detection
   - Det@10
   - Det@25
   - Det@50

Do not choose whichever operating point makes either model look better. Do not describe alpha0.10 vs TopK8 best-F1 as a matched calibration comparison.

## Output / freeze
Write a cryptographically bound held-out freeze containing:
- dataset manifest SHA
- normalization SHA
- training freeze SHA
- every checkpoint SHA
- every validation-freeze SHA
- exact test membership proof
- all five seed results
- primary seed0 alpha0.10 result
- matched TopK8 comparison
- explicit flags `test_used_for_selection=false`, `ood_scored=false`

Save raw per-row scores for forensic reproducibility only. They must not be used for any new selection, tuning, thresholding, or model choice.

## Prohibited
- no training
- no checkpoint changes
- no feature changes
- no architecture changes
- no normalization changes
- no threshold changes or recalibration
- no seed selection from test
- no test-driven model/feature decisions
- no OOD150
- no OOD400
- no HARD1000
- no Isaac Sim
- no SimVLA inference
- no recollection

## Return format
Return ONLY:

```text
PRETEST_GATE:
  status: PASSED|FAILED
  dataset_manifest_sha256: ...
  normalization_sha256: ...
  training_freeze_sha256: ...
  checkpoint_and_validation_bindings_all_match: YES|NO
  strict_zero_channels_test_rows: YES|NO
  exact_topk8_test_membership: YES|NO

PRIMARY_SEED0_ALPHA010:
  threshold: ...
  row_auroc: ...
  row_auprc: ...
  success_false_alarms: count/586 | percent
  failure_detection: count/14 | percent
  det10: count/14 | percent
  det25: count/14 | percent
  det50: count/14 | percent
  never_detected: count/14
  mean_first_alarm_fraction: ...

ROBUSTNESS_ALPHA010:
  seed0: AUROC | AUPRC | FA | Det | Det25 | Det50
  seed1: ...
  seed2: ...
  seed3: ...
  seed4: ...
  mean_std_auroc: ...
  mean_std_auprc: ...
  mean_std_fa_percent: ...
  mean_std_failure_detection_percent: ...
  mean_std_det25_percent: ...
  mean_std_det50_percent: ...

MATCHED_TOPK8_COMPARISON:
  membership_exact_match: YES|NO
  auroc_topk8/strict_v2/delta: ...
  auprc_topk8/strict_v2/delta: ...
  row_best_f1_FA_topk8/strict_v2: ...
  row_best_f1_Det_topk8/strict_v2: ...
  row_best_f1_Det10_topk8/strict_v2: ...
  row_best_f1_Det25_topk8/strict_v2: ...
  row_best_f1_Det50_topk8/strict_v2: ...

HELDOUT_FREEZE_SHA256:
  ...

TEST_USED_FOR_SELECTION:
  NO

OOD_SCORED:
  NO

NO_SIM_LAUNCHED:
  YES

HARD1000_TOUCHED:
  NO

COMMIT:
  <sha>
```
