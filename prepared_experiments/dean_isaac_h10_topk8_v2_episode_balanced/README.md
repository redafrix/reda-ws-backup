# Isaac H10 TopK8 Temporal Risk V2 — Episode-Balanced Ablation

Status: PREPARED_NOT_RUN

Purpose: retrain the existing true-H10 TopK8 temporal risk head on the exact same frozen Seen4000 dataset while changing only the training/model-selection weighting from query-row-weighted to episode-balanced/class-balanced.

## Frozen V1 reference

- dataset: `frozen_datasets/isaac_seen_h10_topk8_v1`
- train/validation/test episodes: 2800 / 600 / 600
- train failure episodes: 64
- validation failure episodes: 14
- test failure episodes: 14
- train rows: 52825
- architecture: SeqRiskModel, static 51, history 16x21, action 10x7, width 128, 3 layers, 4 heads, FFN 512, dropout 0.1
- optimizer: AdamW, lr 2e-4, weight decay 1e-4, batch 512, 10 epochs, grad clip 1.0, seed 20260622
- V1 loss: row-weighted `BCEWithLogitsLoss(pos_weight=12.756510416666666)`
- V1 checkpoint selection: highest unweighted Seen-validation query-level AUPRC
- V1 best validation AUPRC: 0.8494462695568447
- V1 validation AUROC at best epoch: 0.9344901338018652
- V1 model SHA256: `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`

## Only intended scientific change

For each episode i with Ti query rows, every row gets inverse-duration weighting. Class balancing is applied at episode level, not row level.

Equivalent full-dataset objective:

`L = 0.5 * mean_over_success_episodes(mean_query_BCE_i) + 0.5 * mean_over_failure_episodes(mean_query_BCE_i)`

For the train split this is equivalent to per-row weights:

- success row in episode i: `0.5 / (2736 * Ti)`
- failure row in episode i: `0.5 / (64 * Ti)`

Do not reuse the V1 row-derived `pos_weight=12.756510416666666` in V2.

## What must remain unchanged

Architecture, features, history/action shapes, frozen Seen4000 episodes, train/validation/test membership, normalization, labels, optimizer family, lr, weight decay, batch size, epochs, gradient clipping, training seed.

## V2 model selection

Primary selection metric: episode-balanced Seen-validation AUPRC using per-row sample weight `1/Ti` so each validation episode contributes equal total mass. Preserve unweighted query-level AUPRC/AUROC as secondary metrics for direct comparison with V1.

Do not use OOD150 or OOD400 for checkpoint selection or threshold selection.

## Evaluation sequence

1. Train V2 on frozen Seen train split only.
2. Select checkpoint on Seen validation episode-balanced AUPRC only.
3. Derive V2 thresholds from Seen validation only.
4. Evaluate selected V2 once on frozen Seen test split.
5. Compare V1 vs V2 on the same Seen val/test metrics, including both query-level and episode-balanced metrics.
6. Evaluate V2 on existing OOD150 only after Seen selection is frozen; treat OOD150 as development/engineering evidence.
7. Do not open/run OOD400 in this task.

## HARD1000 isolation

HARD1000 is an independent live Isaac collection and must not be paused, restarted, killed, or modified. No second Isaac/Omniverse process may be launched. V2 training is allowed only after a read-only GPU/process preflight confirms enough headroom and the training process is a small standalone PyTorch risk-head job.
