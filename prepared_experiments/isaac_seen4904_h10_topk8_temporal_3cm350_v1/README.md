# Main Isaac Risk Model (Exact 4,904 Episodes, 3cm/350-Tick Protocol)

## Summary
This directory records the frozen training metadata, split manifest, training curves, thresholds, and locked test evaluation for the new main Isaac risk head: `isaac_seen4904_h10_topk8_temporal_3cm350_v1`.

## Key Model Information
- **Dataset**: `isaac_seen4904_h10_3cm350_exact_v1` (4,904 episodes, 96,813 decision rows).
- **Split Proportions**: 70% Train (3,433 eps / 67,712 rows), 15% Validation (735 eps / 14,475 rows), 15% Test (736 eps / 14,626 rows), stratified by `source_campaign` and `binary_label`.
- **Architecture**: `SeqRiskModel` (hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, ffn=512, dropout=0.1).
- **Training Recipe**: 10 epochs, AdamW (lr=2e-4, weight_decay=1e-4), batch size 512, grad clip 1.0, weighted BCE loss (`pos_weight = 4.3443`).
- **Checkpoint Selection**: Epoch 10 selected by highest validation query-level AUPRC (`0.9087`).
- **Test Performance (Locked Test Split: 736 episodes / 14,626 rows)**:
  - Query AUROC: `0.9623` | Query AUPRC: `0.9217`
  - Episode-Balanced AUROC: `1.0000` | Episode-Balanced AUPRC: `1.0000`
  - Failure Episode Detection Rate @ Best Val F1: `100.0%`
  - Success Episode False Alarm Rate @ Best Val F1: `7.29%`
