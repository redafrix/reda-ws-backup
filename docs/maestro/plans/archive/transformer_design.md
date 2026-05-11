# Design Document: TDQC Causal Transformer Transition (Plan A)

## 1. Overview
Transition the TDQC (Temporal-Difference Quality Calibration) system from an LSTM-based architecture to a state-of-the-art Causal Decoder-Only Transformer. This evolution aims to solve the "forgetting" bottleneck of LSTMs and improve failure prediction reliability in Out-of-Distribution (OOD) scenarios.

## 2. Architectural Specifications

### 2.1 Model Components (LLaMA-inspired)
- **RMSNorm**: Custom implementation for continuous feature stability.
- **SwiGLU MLP**: Custom block using `nn.SiLU` and gated linear units.
- **Positional Awareness**: Absolute Positional Embeddings (`nn.Embedding(501, 256)`) to handle trajectory progress.
- **Suite Token Integration**: Prepend a `suite_id` embedding at sequence index 0, forcing static context into the model's "memory".
- **Causal Attention Engine**: Leverage `torch.nn.functional.scaled_dot_product_attention` with `is_causal=True`.

### 2.2 Model Definition: `TDQCTransformerCalibrator`
- **Input Projection**: `nn.Linear(input_dim, hidden_dim)`
- **Backbone**: Multiple `TransformerBlock` layers.
    - Each block: `RMSNorm` -> `CausalAttention` -> `RMSNorm` -> `SwiGLU MLP`.
- **Head**: `RMSNorm` -> `Linear` -> `1` (p_fail logits).

### 2.3 Online Inference (KV Caching)
- The `step(phi_t, state)` function will implement Key-Value caching.
- `state` structure:
    ```python
    {
        "timestep_index": int,
        "kv_cache": List[Tuple[torch.Tensor, torch.Tensor]] # (K, V) per layer
    }
    ```
- On step 0 (suite initialization): Process suite token, store KV.
- On subsequent steps: Process `phi_t`, append to KV cache, compute causal attention.

## 3. Training & Validation Strategy

### 3.1 Optimizer & Scheduler
- **Linear Warmup**: 5 epochs ramping from `1e-7` to `1e-4`.
- **Main Scheduler**: `ReduceLROnPlateau` on Validation Sequential Brier Score.
- **Optimizer**: `AdamW` with `weight_decay=1e-2`.

### 3.2 Hybrid Masking
- Construct an attention mask that combines:
    1. **Causal Mask**: Ensures step $t$ only attends to steps $\le t$.
    2. **Padding Mask**: Ensures non-data steps (zeros) are ignored.

### 3.3 Evaluation track
- **ID (In-Distribution)**: `v8_test.pt`.
- **OOD (Out-of-Distribution)**: `v8_unseen_obj_ood.pt`.
- **Metrics**: Stepwise AUC-ROC, Sequential Brier Score.

## 4. Workspace & Environment Isolation

### 4.1 Capsule Setup
- Folder: `experiments/v8_exp11_transformer/`
- Contents: Copy `core/phase2_tdqc/` and `train_tdqc.py` into the capsule.

### 4.2 Environment Setup
- Path: `/home/redafrix/envs/simvla_transformer`
- Process: Clone stable environment, verify PyTorch 2.5+, install any additional needs.
- Activation: Update `activate_simvla.sh` within the experiment capsule.

## 5. Implementation Phases (Maestro)
1. **Phase 1 (Setup)**: Workspace isolation, environment creation, capsule population.
2. **Phase 2 (Implementation)**: `TDQCTransformerCalibrator` implementation and `train_tdqc.py` refactoring.
3. **Phase 3 (Training)**: Training loop execution with warmup.
4. **Phase 4 (Analysis)**: Evaluation, comparative analysis vs Exp 08 baseline, and final report.
