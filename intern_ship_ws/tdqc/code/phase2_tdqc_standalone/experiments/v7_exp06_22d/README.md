# v7 Experiment 06 — 22D Inputs (based on v7_exp01_combined134)

**Concept**: Re-running the successful combined architecture (MC loss + Task embed + 256/2L LSTM) but with the expanded 22-dimensional feature set.
**Dataset**: v7 22D (39k episodes)
**Architecture**: 
- LSTM: 2 layers, 256 hidden units
- Task Embeddings: enabled (20 tasks)
- Loss: Temporal Difference Brier MC loss
**Source**: Copied from `v7_exp01_combined134`.
