# End-to-End Pipeline Topology & Dataflow

```
[1. Literature & Theoretical Foundation]
   ├── intern_ship_research & biblio
   └── TDQC / Softplus uncertainty parameterization (Idea 166)
           │
           ▼
[2. Robotic Simulation & Policy Backbone]
   ├── Franka Emika Panda in NVIDIA IsaacLab (franka_wrist_camera_isaaclab)
   ├── SimVLA (SmolVLM-500M backbone + Softplus 110k policy)
   └── Pi0.5 Flow Matching Policy (30k fine-tuning)
           │
           ▼
[3. Closed-Loop Rollout Data Collection]
   ├── Round 0 Broad Collection (4,000 episodes, receding H1) [ARCHIVED]
   └── True Chunk H10 Execution Workspace (simvla_isaac_risk_collection_H10_EXECUTION_20260813) [ACTIVE]
           │
           ├── Dual-Threshold Label Contract (strict 2cm vs operational 4cm)
           └── Automated Supervision (pipeline_supervisor.py + progress watchdog)
           │
           ▼
[4. Dataset Stratification & Risk Head Training]
   ├── Frozen Dataset Build (70% Train / 15% Val / 15% Test grouped by scene_family_id)
   └── SeqRiskModel (Temporal Transformer over TopK8 uncertainty features)
           │
           ▼
[5. Locked Benchmark Evaluation]
   ├── Seen Test Partition
   ├── Locked OOD-150 Evaluation Set (AUROC: 0.8194, AUPRC: 0.9612)
   └── Hard1000 Seen Enrichment
           │
           ▼
[6. Scientific Publication & Evidence Consolidation]
   └── vowel_publication_workspace (redafrix/u-vowel-publication @ a03fcbf)
```
