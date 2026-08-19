# Final Corrected True-H10 Isaac Results — 2026-08-18

> [!IMPORTANT]
> **HISTORICAL 2026-08-18 LOCK**
> For the current 3cm/350/no-dwell main dataset/model/results, see [CURRENT_MAIN_ISAAC_RESULTS_20260819.md](CURRENT_MAIN_ISAAC_RESULTS_20260819.md).

Canonical workspace: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813`.

## Seen4000 and V1 detector

| Split | Episodes | Success | Failure | Decision rows |
|---|---:|---:|---:|---:|
| Train | 2800 | 2736 | 64 | 52825 |
| Validation | 600 | 586 | 14 | 11410 |
| Test | 600 | 586 | 14 | 11368 |
| **Total** | **4000** | **3908** | **92** | **75603** |

- Execution: true `chunk_h10`.
- Model: `isaac_h10_topk8_temporal_v1`.
- Model SHA-256: `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`.
- Normalization SHA-256: `78c934b33e0536bd7cb6b7e5b1962da32305729f602d8269d3a38422841ce050`.
- Best epoch: 6.
- Validation AUROC/AUPRC: `0.9344901338018652 / 0.8494462695568447`.
- Selected Seen threshold `best_val_f1`: `0.7990124225616455`.

V1 is a risk detector for the current/main H10 proposal. The other eight samples contribute ACE/disagreement context, but are not eight independently supervised candidate outcomes.

## Locked historical OOD150 detector

- 150 episodes: 72 success / 78 failure.
- 5887 decision rows.
- Step AUROC: **0.9165517741946905**.
- Step AUPRC: **0.9800307261831581**.
- At `best_val_f1`: success false alarms 1.3889%, failure detection 100%, detected by 10%/25%/50% progress = 6.4103% / 39.7436% / 100%.

## Definitive active OOD150 controller

Frozen controller: `A=0.7990124225616455`, `C=0.9`, `M=0.0`.

- `A` is Seen-validation calibrated.
- `C` is an engineering operating point selected from preserved real live nine-candidate OOD-development decisions.
- The final 150 is therefore a locked-membership active engineering evaluation, not a pristine untouched holdout for controller hyperparameter selection.

| Metric | Historical baseline | Active |
|---|---:|---:|
| Success | 72/150 (48.0%) | **75/150 (50.0%)** |
| Failure | 78/150 | 75/150 |
| Net | — | **+3 episodes / +2.0 pp** |

Paired: **11 rescues, 8 regressions, 64 persisted successes, 67 persisted failures**. Arithmetic check: `75 = 72 + 11 - 8`.

Controller audit: 5757 decisions; 3327 alarms; 2952 decisions with a lower-risk alternative; 57 accepted replacements in 36/150 episodes; candidate histogram `{1:9,2:6,3:6,4:9,5:6,6:12,7:7,8:2}`; selection mismatches 0; execution mismatches 0; max action difference 0.0.

Membership audit: 150 expected, 150 actual, 150 unique; no missing, extra, or duplicate IDs; historical membership exact.

## Primary evidence

Directory: `prepared_experiments/dean_isaac_online_ood150_engineering_cap090_v1/`.

Use `FINAL_RESULT.json`, `FINAL_MEMBERSHIP_AUDIT.json`, `FINAL_CONTROLLER_AUDIT.json`, `FINAL_PAIRED_COMPARISON.json`, `FINAL_RUN_MANIFEST.json`, and `CONTROLLER_PROVENANCE_CORRECTION.json`.

Evidence commits: `840d9b4ae44a9f83cd90d19ce663c7d5f3a7c442`, `556aa351ba107d2f28d91582cc1b5f602f87fecf`, `06d9d55c0c2a166719c4aaae0534cf973689f93e`.

## HARD1000

HARD1000 is active, not a final result. It resumed from the preserved 249-episode state. Stage 8 verified count 250 with new source ID 776; a later sanity check observed 255 unique episodes with the original 249 snapshot unchanged.

## Invalid / superseded evidence

Commit `70327b4b31bde35c01fda29a807f9100b5295a62` is invalid for historical 9-candidate alternative scores: the archive lacked candidates 1–8 diffusion traces, so trace-dependent features were incorrectly reused from candidate 0. Correction commit: `86f5baf3281596df2305409499fc9e0c21d119ed`.

Older H1/receding-H1 Isaac results are historical diagnostics and are superseded for the intended true-H10 protocol.
