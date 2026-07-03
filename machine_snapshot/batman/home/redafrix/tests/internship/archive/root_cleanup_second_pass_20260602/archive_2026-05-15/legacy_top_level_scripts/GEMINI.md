# TDQC Project Mandates

## Failure Prediction Strategy (Marathon V6 Baseline)

### Architectural Constraints
- **Architecture:** Use **Time-Blind MLPs**. Avoid global self-attention/Transformers to prevent the "Timer Trap" (counting steps to failure).
- **Features (NEW ABSOLUTE CHAMPION - Idea 166):** Prioritize **Multi-Scale Temporal Deltas** ($dt \in \{1, 3, 5\}$) concatenated with **Softplus-Compressed Uncertainty Deltas** (`F.softplus(v_{dt, 14:22})`). This has achieved **86% Recall** with **7% FPR** (Test) and **85% Recall** / **0% FPR** (OOD).
- **Safety Constraint:** For high-safety deployments, use **Wide MLPs (H=512)** with Dropout 0.1 to achieve **<2% FPR**.

### Training & Dataset Hygiene
- **Truncation Mandate:** Always use end-anchored randomized truncation ($H \in [50, 150]$) during training.
- **Evaluation Mandate:** Use a fixed 150-step maximum horizon for all metrics (Recall, FPR, Lead Time) to maintain consistency.
- **Loss Function:** Use **TD Brier Loss** with optional **Focal Gamma $\gamma \in [0.5, 1.0]$**. Avoid $\gamma \ge 2.0$ to prevent FPR collapse.
- **Class Balancing:** Use a **3x weight** for failure states.

### System & Performance
- **GPU Optimization:** Use `batch_size=512`, `num_workers=4`, and `pin_memory=True` for fast iteration on the RTX 4070.
- **Checkpoints:** Models must save `config` metadata (hidden_dim, num_layers) inside the checkpoint to ensure evaluation script compatibility.
