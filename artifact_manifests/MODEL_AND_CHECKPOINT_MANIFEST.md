# Model & Checkpoint Manifest

| Model Name | Checkpoint Path | Architecture / Backbone | Training Data | Primary Metrics | Status |
|---|---|---|---|---|---|
| **SimVLA Softplus 110k** | `/mnt/ai/projects/simvla_reaching_inference_package_20260730/checkpoints/softplus_110k.pt` | SmolVLM-500M + Transformer Action Head | Franka Reaching 110k steps | Base reaching policy (98.05% seen success) | `PRODUCTION` |
| **Pi0.5 Reaching Pose v1** | `/mnt/ai/pi05/training/reaching_pose_v1_4400_pi05_fullpose_v3/checkpoints/production_v1_30000.pt` | Pi0.5 Flow Matching Backbone | 4,400 IsaacLab demonstrations | Loss 0.0034 at step 30,000 | `VALIDATED` |
| **TopK8 SeqRiskModel (Round 0)** | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/models/isaac_topk8_temporal_v1/best_model.pt` | Temporal Transformer (8 features) + MLP | 4,000 Round 0 IsaacLab episodes | OOD AUROC: 0.8194, OOD AUPRC: 0.9612 | `PROMOTED` |
| **Idea 166 Softplus Detector** | `/media/redafrix/My Passport1/reda_ws/fiper_ws/checkpoints/idea_166_softplus.pt` | Time-Blind MLP + Softplus Deltas | LIBERO-PRO 6 suites | Seen Recall: 86.88%, FPR: 7.31%, OOD Recall: 85.0% | `STATE_OF_THE_ART` |
| **TopK8 SeqRiskModel (H10)** | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813/models/` | Temporal Transformer (Chunk H10) | 4,000 H10 episodes (In Progress) | Pending training post-collection | `TRAINING_PENDING` |
