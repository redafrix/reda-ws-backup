# v8 Experiment 08 — Balanced Dataset (22D Inputs)

**Concept**: Training the successful Suite Embedding architecture on a perfectly balanced 50/50 success/failure dataset.
**Dataset**: v8 Balanced (22k episodes)
- Train: `data/v8_balanced/v8_train.pt`
- Val: `data/v8_balanced/v8_val.pt`
- Test: `data/v8_balanced/v8_test.pt`
- OOD: `data/v8_balanced/v8_unseen_obj_ood.pt` (Chocolate Pudding & Orange Juice)

**Architecture**: 
- LSTM: 2 layers, 256 hidden units
- Suite Embeddings: enabled (11 suites)
- Loss: Temporal Difference Brier MC loss
- Early Stopping: enabled (patience=40)

**Goal**: Solve the "Accuracy Paradox" and improve early-warning reliability (Stepwise AUC) on unseen objects.
