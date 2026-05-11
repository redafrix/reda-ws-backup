# Implementation Plan: TDQC Causal Transformer Transition (Plan A)

## Phase 1: Setup & Isolation
**Goal**: Create a secure, isolated workspace and environment for the Transformer experiment.

1. **Capsule Creation**:
   - Create directory `experiments/v8_exp11_transformer/code/`.
   - Copy all content from `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/core/phase2_tdqc/` to the new capsule `code/phase2_tdqc/`.
   - Copy `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/core/phase2_tdqc/train_tdqc.py` to `experiments/v8_exp11_transformer/code/`.
2. **Environment Cloning**:
   - Clone the stable environment `/home/redafrix/envs/simvla` to `/home/redafrix/envs/simvla_transformer`.
   - Verify `torch` version and CUDA availability in the new environment.
3. **Activation Script**:
   - Create/Update `experiments/v8_exp11_transformer/code/activate_simvla.sh` to point to the new environment.

## Phase 2: Core Implementation
**Goal**: Rewrite the TDQC model and training logic for the Causal Transformer.

1. **Model Architecture (`tdqc_model.py`)**:
   - Implement `RMSNorm` class.
   - Implement `SwiGLU` MLP class.
   - Implement `TransformerBlock` (Attention + MLP).
   - Implement `TDQCTransformerCalibrator`:
     - Suite Token embedding and prepending.
     - Absolute Positional Embeddings.
     - Causal self-attention with KV-caching support.
     - `step(phi_t, state)` implementation with KV-cache dictionary.
2. **Loss & Masking (`tdqc_losses.py`)**:
   - Ensure `tdqc_brier_td_loss` and `sequential_brier_score` handle Transformer outputs correctly (sequence length $T+1$ due to suite token).
3. **Training Script (`train_tdqc.py`)**:
   - Refactor to use `TDQCTransformerCalibrator`.
   - Implement **Linear Warmup Scheduler** (first 5 epochs).
   - Implement **Hybrid Attention Mask** (Causal + Padding).
   - Update `collect_train_stats` and `evaluate` for the new model signature.

## Phase 3: Training & Monitoring
**Goal**: Execute the training loop and ensure convergence.

1. **Launch Training**:
   - Run `train_tdqc.py` within the `v8_exp11_transformer` capsule.
   - Use hyperparams: `lr=1e-4`, `warmup_epochs=5`, `weight_decay=1e-2`, `hidden_dim=256`.
2. **Monitoring**:
   - Track Train Loss and Validation Sequential Brier Score.
   - Verify that the warmup phase stabilizes the initial loss.

## Phase 4: Analysis & Reporting
**Goal**: Validate the Transformer's performance against the LSTM baseline.

1. **Evaluation**:
   - Run `eval_tdqc.py` on ID (`v8_test.pt`) and OOD (`v8_unseen_obj_ood.pt`).
2. **Comparison**:
   - Compare results with `v8_exp08_balanced` (LSTM baseline).
   - Generate comparative plots for Stepwise AUC-ROC.
3. **Final Report**:
   - Document findings on "forgetting" bottleneck and generalization.
