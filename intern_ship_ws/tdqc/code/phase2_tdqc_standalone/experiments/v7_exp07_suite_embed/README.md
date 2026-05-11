# v7 Experiment 07 — Suite Embeddings (22D Inputs)

**Concept**: Replacing task-level embeddings with suite-level embeddings (11 suites total) and standardizing the use of early stopping.
**Dataset**: v7 22D
**Architecture**: 
- LSTM: 2 layers, 256 hidden units
- Suite Embeddings: enabled (11 suites: `libero_10_lan` to `libero_spatial_swap`)
- Loss: Temporal Difference Brier MC loss
- **Early Stopping**: enabled (patience=40)
**Source**: Refactored from `v7_exp06_22d` with the requested logic for `suite_id`.
