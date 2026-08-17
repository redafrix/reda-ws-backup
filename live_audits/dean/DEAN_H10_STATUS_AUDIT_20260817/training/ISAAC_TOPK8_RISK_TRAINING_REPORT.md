# Isaac TopK8 Risk Training Report

- Model: `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/isaac_h10_topk8_temporal_v1/model.pt`
- SHA-256: `ad049519746913c4c2ce1a0b57fb32ad5c3395f5bce6841648c68cc94f862b38`
- Best epoch: `6`
- Best seen-validation AUPRC: `0.84944627`
- Architecture: one SeqRiskModel, width 128, 3 layers, 4 heads, FFN 512.
- Optimization: weighted BCEWithLogitsLoss, AdamW, lr 2e-4, weight decay 1e-4, batch 512, 10 epochs.
- Selection and calibration: seen validation only.

OOD150_USED_FOR_TRAINING=NO
OOD150_USED_FOR_NORMALIZATION=NO
OOD150_USED_FOR_MODEL_SELECTION=NO
OOD150_USED_FOR_THRESHOLD_CALIBRATION=NO
