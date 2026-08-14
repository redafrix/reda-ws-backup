# Results Evidence Lock

Audit date: 2026-08-14

This file defines the evidence that may enter the current paper Results section.
It intentionally excludes unfinished experiments and older results superseded by
cleaner matched evaluations.

## Headline U-VOWEL Evidence

- Source archive: `/home/redafrix/Downloads/libero_router_tests_package_20260814.zip`
- Archived copy: `vowel_publication_workspace/90_source_snapshots/20260814_libero_router_tests_package/`
- Archive SHA-256: `8c96c0914e40c23315c4bfc122a03a32aaf8049a31a4c242de3521083f0d56cd`
- Structural audit: `vowel_publication_workspace/03_shared/evidence/fusion/LIBERO_ROUTER_RESULTS_AUDIT_20260814.md`
- Evidence level: episode-level raw JSONL, matched identities, independently recomputed summaries.

Permitted headline results:

| Protocol | Base WM H10 | HF SimVLA H10 | Fresh U-VOWEL | Latch-50 U-VOWEL |
|---|---:|---:|---:|---:|
| Official LIBERO-PRO | 812/2000 | 836/2000 | 885/2000 | 888/2000 |
| Project-specific Goal-Object-OOD | 823/900 | 841/900 | 859/900 | 861/900 |

The selected controller is the explicit latch-50 implementation. Historical
cached K1/K3 and legacy-cache results may appear only as diagnostics because
rejected world-model state could remain cached.

## VLA Risk-Monitor Evidence

### Promoted SimVLA checkpoint

- Model: `simvla_h10_topk8_official_goal_object_seen_main_20260701`
- Selection: highest source-validation AUPRC among repeated same-source runs;
  no OOD result used for checkpoint selection.
- Seen validation AUROC/AUPRC: 0.9345/0.9369.
- Source artifact: Git branch `catalog/bob-20260703`, path
  `machine_snapshot/bob/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/experiments/eval_promoted_single_model_all_ood_20260701/results.json`.
- OOD protocols: six frozen datasets totaling 680 episodes, with 331 successes
  and 349 failures.
- Thresholds: `best_val_f1`, fixed 0.5, and success-score q90/q95/q99 are all
  calibrated on seen data. Per-dataset oracle selection is not a headline claim.

### Official FIPER comparison

- Official repository commit: `13d79c5c3069def843e454787ff128defc249838`.
- Calibration: successful seen official `libero_goal_object` rollouts only.
- Test: the same six OOD datasets, with no OOD calibration or OOD threshold tuning.
- RND seeds: 0, 1, 2, 42, 43.
- Source artifact: Git branch `catalog/bob-20260703`, path
  `machine_snapshot/bob/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702/official_fiper_seen_thresholds_cross_suite_ood_aggregate.csv`.

## Cross-Backbone Online Evidence

These results support portability and limitations; protocols differ and must not
be pooled as a single benchmark.

| Backbone/protocol | Reference | Risk-aware | Difference |
|---|---:|---:|---:|
| SimVLA, six-suite replay | 392/680 | 403/680 | +11 |
| OpenVLA, Goal-Object-OOD, H8 reference | 976/1800 | 1014/1800 | +38 |
| Pi0.5, official Goal-Swap | 161/500 | 166/500 | +5 |
| Pi0.5, official OOD18 | 1754/1800 | 1736/1800 | -18 |

The fixed-H1 OpenVLA control reached 1022/1800, so the adaptive H1/H8 policy did
not outperform every fixed-horizon baseline. The Pi0.5 OOD18 result is a negative
control showing that a strong base policy can be harmed by nonselective action
replacement.

## Explicit Exclusions

- No IsaacLab number enters Results. The corrected H10 collection is ongoing;
  the completed H1 archive is superseded for the intended H10 protocol.
- No sim-to-real number enters Results because no completed matched physical
  evaluation artifact was located.
- The Pi0.5 task-9-inclusive offline headline is excluded because that local
  collection used an invalid rack scene for task 9.
- OOD-tuned mass-threshold sweeps are diagnostics, not deployment results.
- Historical TDQC, invalid leakage splits, stopped smokes and stale-cache
  controller outputs are excluded from headline tables.
- The 2,000 and 900 episodes are repeated initial states nested within tasks,
  not independent task samples. McNemar tests are descriptive and single-seed.

