"""
openvla_oft_bob_compat.py

Compatibility utility to resolve accelerate/bitsandbytes/transformers conflicts
and device alignment issues for OpenVLA-OFT models on Bob.
"""

import torch
import transformers.modeling_utils as _mu

def apply_quantized_to_patch():
    """
    Monkey-patches PreTrainedModel.to() to be a no-op if the model is quantized
    and has a defined quantization_method. This works around version incompatibility
    between accelerate and transformers where dispatch_model incorrectly attempts
    to call .to() on a quantized model whose is_loaded_in_8bit or is_loaded_in_4bit
    properties are None instead of True.
    """
    _original_to = _mu.PreTrainedModel.to
    
    def _patched_to(self, *args, **kwargs):
        if getattr(self, "quantization_method", None) is not None:
            # Model is already quantized and on the correct device; skip .to()
            return self
        return _original_to(self, *args, **kwargs)
        
    _mu.PreTrainedModel.to = _patched_to
    print("[Compat] Applied quantized PreTrainedModel.to() monkey-patch successfully.")

def align_rotary_emb_devices(model):
    """
    Walks the model layers and moves all LlamaRotaryEmbedding `inv_freq` buffers
    to the device of the containing layer's parameters (e.g. self_attn.q_proj.weight).
    This resolves the device mismatch error:
    RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0!
    """
    if hasattr(model, "language_model") and hasattr(model.language_model, "model") and hasattr(model.language_model.model, "layers"):
        layers = model.language_model.model.layers
        count = 0
        for i, layer in enumerate(layers):
            if hasattr(layer, "self_attn") and hasattr(layer.self_attn, "rotary_emb"):
                rot = layer.self_attn.rotary_emb
                if hasattr(rot, "inv_freq") and rot.inv_freq is not None:
                    if hasattr(layer.self_attn, "q_proj") and hasattr(layer.self_attn.q_proj, "weight"):
                        target_device = layer.self_attn.q_proj.weight.device
                        if rot.inv_freq.device != target_device:
                            rot.inv_freq = rot.inv_freq.to(target_device)
                            count += 1
        print(f"[Compat] Successfully aligned {count} rotary embedding inv_freq buffers.")
    else:
        print("[Compat] Warning: Model structure not recognized as Llama VLA. No alignment performed.")
