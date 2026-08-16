# Dean (RTX 5090 32GB) Artifact Manifest

| Logical Name | Current Absolute Path | Type | Approx Size | Status | Description |
|---|---|---|---|---|---|
| H10_Execution_Workspace | `/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813` | Code / Active Pipeline | 35.5 GB | `ACTIVE` | True chunk_h10 data collection (3,737/4,000 committed) |
| Round0_Broad_Workspace | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730` | Archived Pipeline | 38.5 GB | `AUDITED_PASS` | Completed Round 0 broad collection (4,000 episodes, zstd compressed) |
| SimVLA_Inference_Package | `/mnt/ai/projects/simvla_reaching_inference_package_20260730` | Model / Weights | 9.0 GB | `PERSISTED` | Pretrained SimVLA Softplus 110k weights & SmolVLM backbone |
| IsaacLab_Reproduction_WS | `/mnt/ai/projects/simvla_reproduction_workspace` | Simulation / Assets | 4.2 GB | `ACTIVE` | Franka robot assets, 3D USD objects, SimVLA model repo |
| Pi05_30k_Loss_Report | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/reports/production_v1_loss_0_30000_final.png` | Loss Plot | 280 KB | `VALIDATED` | 30,000-step training loss curve for fine-tuned Pi0.5 |
| Visual_Audit_Video | `/mnt/ai/projects/simvla_isaac_risk_collection_20260730/audits/success_label_visual_audit_20260803/SIMVLA_SUCCESS_FAILURE_VISUAL_AUDIT.mp4` | Video Audit | 18 MB | `VALIDATED` | Visual audit resolving 2cm vs 4cm dual thresholds |
