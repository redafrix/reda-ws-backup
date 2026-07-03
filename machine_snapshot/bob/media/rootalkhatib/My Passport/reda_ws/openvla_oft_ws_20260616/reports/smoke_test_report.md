# OpenVLA-OFT Setup and Smoke Test Report

This report summarizes the setup and successful smoke testing of the OpenVLA-OFT (One-Step Fine-Tuning) model on Bob.

## Workspace & Setup Details

- **Target Host:** Bob (`rootalkhatib@100.105.217.20`)
- **Workspace Root:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
- **Virtual Environment:** `/home/rootalkhatib/openvla_oft_env_20260616`
- **Model:** `moojink/openvla-7b-oft-finetuned-libero-goal`
- **Hugging Face Cache:** Isolated in `openvla_oft_ws_20260616/hf_cache`

---

## Technical Issues Resolved

During model loading and action prediction, two critical runtime errors were encountered and resolved via runtime monkey-patching:

### 1. `bitsandbytes` / `accelerate` Version Incompatibility
- **Issue:** The custom `OpenVLAForActionPrediction` model has `is_loaded_in_8bit = None` instead of `True`. This causes `accelerate`'s `dispatch_model` to attempt `model.to(device)` on quantized weights, raising a `ValueError` in `transformers`.
- **Solution:** Patched `PreTrainedModel.to()` to act as a no-op when the model has a defined `quantization_method` (since weights are already placed on the correct device during loading).

### 2. Rotary Embedding Device Mismatch (`cpu` vs. `cuda:0`)
- **Issue:** The `inv_freq` buffers of `LlamaRotaryEmbedding` inside the language model were initialized on CPU and not properly dispatched to GPU, causing a `RuntimeError` during matrix multiplication: `RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0!`.
- **Solution:** Added a manual device alignment pass post-loading to transfer all rotary embedding `inv_freq` buffers to the corresponding device of their attention layers.

---

## Smoke Test Results

The action inference test was executed successfully on a sample observation from LIBERO:

- **Quantization Mode:** 8-bit Quantized
- **Task Description:** *'pick up the black bowl between the plate and the ramekin and place it on the plate'*
- **VLA Model Load Time:** 8.7 seconds
- **GPU VRAM Usage:**
  - Initial Free: `12.16 GB / 15.57 GB`
  - Post-Load Free: `4.62 GB` (model footprint: ~7.54 GB VRAM)
  - Final Free (with head/projector): `4.05 GB`
- **Inference Time:** 0.71 seconds
- **Predicted Action Shape:** `(8, 7)` (chunk of 8 actions, 7-dimensions each)
- **First Predicted Action Vector:**
  ```json
  [0.375298, 0.113880, -0.160217, 0.000102, 0.023207, -0.021599, 0.972656]
  ```
- **Inference Output Path:** `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/smoke/action_smoke_result.json`

---

## Workspace Navigation & Activation

To activate and work in this environment on Bob, source the helper script:
```bash
source "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/activate_openvla_oft_bob.sh"
```
The smoke scripts are located in:
- Load Test: `src/smoke_load_openvla_oft.py`
- Action Test: `src/smoke_openvla_oft_action.py`
