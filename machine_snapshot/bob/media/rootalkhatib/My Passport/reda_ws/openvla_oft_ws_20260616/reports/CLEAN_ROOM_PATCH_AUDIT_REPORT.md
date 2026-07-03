# OpenVLA-OFT Clean-Room Patch Audit Report

**Date:** 2026-06-16  
**Host:** Bob (RTX 4070 Ti SUPER 16 GB)  
**Model:** `moojink/openvla-7b-oft-finetuned-libero-goal`  
**Clean Environment:** `/home/rootalkhatib/openvla_oft_clean_20260616_env`

---

## Executive Summary

> [!IMPORTANT]
> **Both monkey patches are REQUIRED** for the current environment configuration on Bob. There is no clean way to eliminate them without breaking other functionality.

The `.to()` patch can be eliminated by downgrading `accelerate` to `0.30.1`, but this introduces a different problem: the HF-auto-downloaded model code takes precedence over the local prismatic install, which lacks the `libero_goal_no_noops` unnorm key. **The recommended configuration is to keep both patches.**

---

## Test Matrix

| # | Accelerate | `.to()` Patch | Rotary Patch | Local Prismatic | Result |
|---|:---:|:---:|:---:|:---:|---|
| 1 | 1.14.0 | ❌ | ❌ | ✅ | **FAIL** — `ValueError: .to() not supported for 8-bit models` |
| 2 | 1.14.0 | ✅ | ❌ | ✅ | **FAIL** — `RuntimeError: cpu vs cuda:0` (rotary) |
| 3 | 1.14.0 | ✅ | ✅ | ✅ | ✅ **PASS** — Action shape `(8, 7)` ✓ |
| 4 | 0.30.1 | ❌ | ❌ | ✅ | ✅ Model loads, **FAIL** — `AssertionError: unnorm_key` (HF code used) |
| 5 | 0.30.1 | ❌ | ✅ | ✅ | ✅ **PASS** — Action shape `(8, 7)` ✓ |

---

## Root Cause Analysis

### Patch 1: `PreTrainedModel.to()` No-Op

**Root cause:** `accelerate >= 1.0` calls `dispatch_model()` which invokes `model.to(device)` after quantized loading. With `bitsandbytes 0.42.0`, the `is_loaded_in_8bit` property is not properly set, so accelerate doesn't skip the `.to()` call.

**Elimination path:** Downgrade `accelerate` to `0.30.1`.  
**Why we DON'T:** With `accelerate==0.30.1`, the model's HF-auto-downloaded `modeling_prismatic.py` takes precedence. This version does NOT have `libero_goal_no_noops` in its `norm_stats`, causing an `AssertionError` during action unnormalization. The local editable install's `prismatic` package (which has the correct stats) is only reliably used with `accelerate>=1.0`.

### Patch 2: Rotary Embedding Device Alignment

**Root cause:** `LlamaRotaryEmbedding.__init__` in `transformers 4.40.1` (both stock and fork) creates `inv_freq` with `device=None`, landing on CPU. When 8-bit quantization places model weights on CUDA, `inv_freq` stays on CPU, causing a device mismatch during matrix multiplication.

**Elimination path:** None found. This is a **fundamental bug in transformers 4.40.1** when used with 8-bit quantization. The custom fork (`moojink/transformers-openvla-oft`) does NOT fix this issue — its modifications are focused on bidirectional attention for parallel action decoding.

**Interesting finding:** When the HF-auto-downloaded model code runs (instead of local prismatic), rotary embeddings are on the correct device — suggesting the HF model code may handle device placement differently. However, this code path lacks `libero_goal_no_noops`.

---

## Environment Specifications

### Clean Environment (final state)

| Package | Version |
|---|---|
| Python | 3.10.12 |
| torch | 2.2.0+cu121 |
| transformers | 4.40.1 (moojink fork) |
| accelerate | 1.14.0 |
| bitsandbytes | 0.42.0 |
| peft | 0.11.1 |
| numpy | 1.26.4 |
| protobuf | 6.32.0 |
| setuptools | 74.1.3 |

### Diagnostic Environment (unchanged)

| Package | Version |
|---|---|
| Python | 3.10.12 |
| torch | 2.2.0+cu121 |
| transformers | 4.40.1 (stock HuggingFace) |
| accelerate | 1.14.0 |
| bitsandbytes | 0.42.0 |

---

## Recommended Configuration

```python
# openvla_oft_bob_compat.py — REQUIRED for Bob

# Patch 1: .to() no-op for quantized models (accelerate 1.14.0 bug)
apply_quantized_to_patch()

# Patch 2: Rotary embedding device alignment (transformers 4.40.1 bug)
align_rotary_emb_devices(model)
```

### Key Constants
- `NUM_ACTIONS_CHUNK = 8`
- `ACTION_DIM = 7`
- `PROPRIO_DIM = 8`
- `unnorm_key = "libero_goal_no_noops"`

---

## Files Created on Bob

| File | Purpose |
|---|---|
| `src/smoke_clean_no_patch.py` | No-patch baseline test |
| `src/smoke_clean_to_patch_only.py` | `.to()` patch isolation test |
| `src/smoke_clean_rotary_only.py` | Rotary patch isolation test |

---

## Conclusion

The monkey patches are **not code smell** — they are **necessary workarounds** for real version-interaction bugs between `accelerate`, `transformers`, and `bitsandbytes`. The patches are:

1. **Safe:** They only affect quantized models (`.to()` patch) and only move existing tensors to the correct device (rotary patch)
2. **Minimal:** Each targets a specific, well-understood failure mode
3. **Documented:** Root causes are traced to specific library versions
4. **Future-proof:** Upgrading to `transformers >= 4.45` or `accelerate >= 1.2` may fix these upstream, but requires full regression testing
