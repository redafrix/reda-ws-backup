# Internship Research & Implementation: Master Repository Guide (MIGRATED)

This document is the **authoritative single source of truth** for the project, now residing on external storage.

---

## 🌍 Migration Status: EXTERNAL DRIVE
- **Workspace Root (Current):** /media/rootalkhatib/My Passport/reda_ws (on pcrobot)
- **Workspace Root (Fallback):** /media/redafrix/My Passport/reda_ws (on Batman)
- **Python Environment:** /home/redafrix/envs/simvla (Located on SSD for stability/performance)
- **Filesystem:** exfat (External) / ext4 (SSD)

---

## 🌟 Project North Star: Generalized Reliability
Robotic Vision-Language-Action (VLA) models often fail silently. This project aims to bridge the gap between **high-performance VLA models** and **reliable robotic deployment**.

- **Primary Goal:** Proactive online failure prediction (**TDQC**) that generalizes to **Out-of-Distribution (OOD)** scenarios.
- **Core Technology:** Combining temporal uncertainty features from VLA backbones with LSTM-based temporal difference learning.

---

## 🛠 Engineering Standards & Launch Commands

### Environment Setup
- **Python Path:** /home/redafrix/envs/simvla/bin/python3.10
- **Activation:** source intern_ship_ws/activate_simvla.sh (Now handles the Hybrid SSD/External setup)

### Workspace Layout (intern_ship_ws/)
- simvla/: Modified SimVLA code with uncertainty output heads.
- tdqc/code/phase2_tdqc_standalone/: **[ACTIVE]** The experiment hub.
- assets/data/v7_22d/: The production dataset (39k episodes).

### The "Capsule" Protocol
- **Isolation:** Each run gets a new experiments/v8_expXX/ folder.
- **Independence:** Library code is copied locally.
- **Causality:** STRICT ban on non-causal normalization. Always use global training statistics.

### Granular Evaluation Reporting
- **Requirement:** Every evaluation request must produce detailed tables for specific sequence steps: **10, 12, 15, 50, 100, 150, 200, 300, and Overall**.
- **Metrics:** Each table must include **Accuracy (Acc)**, **Brier Score (Brier)**, **AUC-ROC (AUC)**, and **Sample Count (N)**.
- **Datasets:** Always run this granular report on both the **Standard Test Set** (v8_test.pt) and the **OOD Unseen Objects Set** (v8_unseen_obj_ood.pt).
- **Proactivity Logic:** For step-based evaluation, the score is defined as the `max()` probability observed from step 0 to the target step (Horizon Max-Pooling). This ensures the model is credited for any early warnings it generates.

---

## 🚀 Active Experiment Snapshot (Exp 16)
- **Concept:** Anticipation Brier & TD-Bootstrapping.
- **Status:** Training in progress (Transformer, TD Loss, ALiBi).
- **Goal:** Optimize for early failure prediction (measured by Brier in [L-100, L-10] range) using temporal difference bootstrapping.

## 📈 Recent Results
- **Exp 14:** Monte Carlo (MC) Loss Validation. **Completed.** Result: 0.050164 Sequential Brier. Stable but potentially less proactive than TD.
- **Exp 15:** Honest Dynamics. **Terminated.**

---

## 🤖 Orchestration & Subagent Workflow (Maestro)

To handle complex architectural transitions, this project utilizes a **Master Orchestrator (Maestro)** pattern. This ensures high precision, surgical edits, and rigorous validation through specialized subagents.

### The 4-Phase Execution Cycle
1.  **Phase 1: Setup & Isolation (DevOps Engineer)**:
    - Creation of isolated experiment "capsules".
    - Setup of dedicated Python environments on the internal SSD.
    - Provisioning of activation scripts.
2.  **Phase 2: Core Implementation (Coder)**:
    - Surgical rewrites of models and training logic.
    - Implementation of new architectural primitives (e.g., Transformers, RMSNorm, SwiGLU).
    - Ensuring unbuffered logging and clean API contracts.
3.  **Phase 3: Training & Monitoring (ML Engineer)**:
    - Launching training loops with linear warmup and early stopping.
    - Monitoring convergence and hardware utilization.
4.  **Phase 4: Analysis & Reporting (Performance Engineer)**:
    - Comparative benchmarking against ID and OOD baselines.
    - Detailed statistical analysis of Brier scores and ROC-AUC.

### Subagent Mandates
- **Surgical Edits:** Use `replace` for existing code; never overwrite entire files unless requested.
- **Unbuffered Logging:** Always use `flush=True` in print statements to ensure real-time `tail -f` capability.
- **Reproducibility:** Every experiment must have a documented configuration and locked seeds.

---

## 🆘 Troubleshooting
- **Environment Errors:** Ensure you are using the SSD-based environment at /home/redafrix/envs/simvla. Do NOT attempt to run an environment from the exfat drive.
- **spawn ENOENT**: If you see this, restart your terminal/CLI session in the new workspace path.
