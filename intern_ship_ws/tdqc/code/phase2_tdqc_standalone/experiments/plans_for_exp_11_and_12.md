


Here are two comprehensive, end-to-end master plans. One for the **Causal Transformer** and one for **Mamba**. 

These plans serve as your exact architectural checklist. I have broken them down into Setup, Data Formatting, Core Architecture, Inference (the `step` function), and Training modifications.

---

# PLAN A: The Causal "LLaMA-Style" Transformer Blueprint
*The reliable, native PyTorch approach. Uses modern LLM tricks optimized for continuous time-series, with a strict causal mask to mathematically prevent looking into the future.*

### Phase 1: Environment & Setup
*   **Dependencies:** No external libraries required. However, you must ensure your environment runs **PyTorch 2.0 or higher**. This is mandatory because we will rely on `torch.nn.functional.scaled_dot_product_attention`, which automatically routes to hardware-accelerated **FlashAttention** and handles causal masking at the C++/CUDA level.
*   **File Structure:** Create a new capsule: `experiments/v8_exp09_transformer/`. Copy over the dataset and existing code.

### Phase 2: Architectural Rewrite (`tdqc_model.py`)
You will scrap the `nn.LSTM` and build a `TDQCTransformerCalibrator` from scratch.
1.  **Replace LayerNorm with RMSNorm:** Write a custom `RMSNorm` class. It stabilizes continuous 22D features much better than PyTorch's default `LayerNorm`.
2.  **Replace ReLU with SwiGLU:** Write a custom `SwiGLU` MLP block. 
3.  **Positional Encoding:** You must add positional awareness. Since your episodes are mostly capped at ~200-500 steps, a simple `nn.Embedding(max_steps, hidden_dim)` (Absolute Positional Encoding) will work perfectly for V1. You will add this embedding to your 22D features before they hit the attention layers.
4.  **The Prefix Token (`suite_id`):** 
    *   Instead of adding the suite embedding to every step like you did in the LSTM, you will prepend it.
    *   If your batch is `[B, T, 22]`, you project it to `[B, T, 256]`. Then, you get the suite embedding `[B, 1, 256]`, and `torch.cat` them together to create a sequence of `[B, T+1, 256]`.
    *   This forces the first "timestep" to be the static suite context.
5.  **The Attention Block:** Use PyTorch's `scaled_dot_product_attention` with the flag `is_causal=True`. This forces the lower-triangular mask. Step $t$ will never see $t+1$.

### Phase 3: The Online Inference Loop (`step()` function)
This is the most critical mechanical change. You cannot pass `(h, c)` anymore. 
1.  **The KV Cache:** Your `state` variable will now be a dictionary storing two things: `timestep_index` (an integer) and `kv_cache` (a list of Keys and Values for every transformer layer).
2.  **Step-by-step logic:**
    *   Robot sends `phi_t` (22D vector).
    *   Project it to 256D, add the positional embedding for `timestep_index`.
    *   Pass it into Layer 1. Calculate the new Key ($K$) and Value ($V$).
    *   Concatenate the new $K$ and $V$ to the `kv_cache` from the past.
    *   Calculate attention using the *new* Query against the *accumulated* Keys/Values.
    *   Output failure probability and return the updated `kv_cache` as the new `state`.

### Phase 4: Training Pipeline Adjustments (`train_tdqc.py`)
1.  **Remove Padding Mask from Attention (Careful here):** In the LSTM, you padded short episodes with zeros and used a binary mask for the loss. In a Causal Transformer, you must ensure the padded zeros don't corrupt the attention. You will need to pass an `attention_mask` to the transformer that combines the causal mask AND your padding mask.
2.  **Optimizer Warmup:** Transformers *hate* starting with a high learning rate. Your LSTM used a flat `1e-4` LR. For the Transformer, you MUST use a **Linear Warmup** scheduler for the first ~5 epochs, ramping up to `1e-4`, followed by your existing `ReduceLROnPlateau` or a Cosine Decay. If you don't do this, the loss will explode immediately.

---
---

# PLAN B: The Mamba (SSM) Blueprint
*The bleeding-edge robotics approach. Replaces attention entirely with differential equations, providing parallel training but $O(1)$ constant-time inference, completely side-stepping the KV Cache nightmare.*

### Phase 1: Environment & Setup (The Danger Zone)
*   **Dependencies:** Mamba requires custom CUDA kernels. 
    *   You must run: `pip install causal-conv1d>=1.2.0` followed by `pip install mamba-ssm`.
    *   *Warning:* This must be compiled against the exact version of CUDA that your PyTorch installation uses. If your robot runs on an older Jetson or specific hardware, compiling Mamba can be a headache. Make sure this installs properly on your workstation before committing.
*   **File Structure:** Create capsule: `experiments/v8_exp10_mamba/`.

### Phase 2: Architectural Rewrite (`tdqc_model.py`)
You will build `TDQCMambaCalibrator`. It is mechanically much closer to your LSTM than the Transformer.
1.  **Drop Positional Encodings:** Mamba inherently understands continuous time. You do not need absolute or relative positional encodings. Remove them completely.
2.  **Drop Causal Masks:** Mamba's architecture is a "Selective Scan" that sweeps strictly from left to right (past to present). It is natively causal. No masks are needed.
3.  **The Core Block:** You will import `Mamba` from `mamba_ssm` and stack 2 to 4 layers of it, separated by `RMSNorm`. 
4.  **Handling `suite_id`:** Because Mamba processes sequences linearly, prepending a token (like we did in the Transformer) works, but simply adding the suite embedding to every step (exactly as you did in your LSTM code) is actually standard practice for SSMs acting on continuous physical data.

### Phase 3: The Online Inference Loop (`step()` function)
This is where Mamba destroys the Transformer.
1.  **No KV Cache:** You do not need to store massive arrays of past features. 
2.  **The State Object:** You will import `InferenceParams` from `mamba_ssm.utils.generation`. This object pre-allocates a tiny, fixed-size memory buffer (usually `[Batch, 16, 256]`).
3.  **Step-by-step logic:**
    *   Robot sends `phi_t`.
    *   Project to 256D.
    *   Call `mamba_layer.step(phi_t, state)`. 
    *   Mamba calculates the new failure probability, updates the 16D state matrix in-place, and you're done. It takes the exact same amount of time at step 2 as it does at step 200,000.

### Phase 4: Training Pipeline Adjustments (`train_tdqc.py`)
1.  **Learning Rate Scaling:** Mamba has specific internal parameters (like the $\Delta$ step size and state matrices $A$ and $B$). The `mamba-ssm` library handles this mostly under the hood, but it's recommended to not use weight decay on Mamba's internal 1D parameters. 
2.  **Padding:** Just like the LSTM, Mamba processes padded tensors fine. You just apply your exact existing `tdqc_brier_mc_loss` masking to the output predictions so the padded zeros don't affect the Brier score.
3.  **Stability:** Mamba does not require strict LR warmup like the Transformer. You can likely plug-and-play your existing optimizer and scheduler.

---

### How to Execute This
1.  **Try Plan B (Mamba) first in an isolated notebook.** Run `pip install mamba-ssm`. If it compiles instantly and imports without CUDA errors, proceed with Plan B. It is fundamentally superior for what you are building.
2.  **If Mamba compilation fails or throws CUDA version mismatch errors**, immediately fall back to **Plan A (Transformer)**. PyTorch 2.0+ FlashAttention is incredibly fast, and for 200-step episodes, the KV Cache memory footprint will be negligible on any modern GPU. 

Both architectures will solve your LSTM's "forgetting" bottleneck and give you the localized, razor-sharp failure detection required to push your OOD Stepwise AUC even higher. Which one would you like to start mocking up the code for?
