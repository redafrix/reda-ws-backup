# Main Canonical Isaac Risk Model (Exact 4,904 Episodes, Unified Label Split)

## Summary
This directory records the frozen training metadata, split manifest, training curves, thresholds, and locked test evaluation for the canonical main Isaac risk head: `isaac_seen4904_h10_topk8_temporal_3cm350_main_v2`.

## Split & Dataset Configuration
- **Dataset**: `isaac_seen4904_h10_3cm350_exact_v1` (4,904 episodes, 96,813 decision rows).
- **Split Philosophy**: Unified label-only stratification (seed 20260819, 70/15/15 ratio).
  - Train: 3,433 episodes (3,071 success, 362 failure / 67,725 rows)
  - Validation: 735 episodes (658 success, 77 failure / 14,562 rows)
  - Test: 736 episodes (658 success, 78 failure / 14,526 rows)
- **Source Campaign**: Recorded as provenance metadata only; not used for split assignment or official evaluations.

## Model & Training Results
- **Architecture**: `SeqRiskModel` (hist_dim=21, action_dim=7, static_dim=51, width=128, layers=3, heads=4, ffn=512, dropout=0.1).
- **Training Objective**: `BCEWithLogitsLoss(pos_weight = 4.3453)`.
- **Model Selection**: Best Epoch 9 selected by highest validation query AUPRC (`0.9020`).
- **Locked Test Evaluation (736 episodes / 14,526 rows)**:
  - Query AUROC: `0.9408` | Query AUPRC: `0.8748`
  - Episode-Balanced AUROC: `0.9987` | Episode-Balanced AUPRC: `0.9782`
  - Failure Episode Detection Rate @ Best Val F1 (`0.5791`): `100.0%`
  - Success Episode False Alarm Rate @ Best Val F1: `7.60%`
