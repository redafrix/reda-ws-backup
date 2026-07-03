"""
Test: accelerate==0.30.1 + ONLY rotary patch (no .to() patch).
"""
import sys, os, time
import torch
import numpy as np

WS = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616"
sys.path.insert(0, os.path.join(WS, "src", "openvla-oft"))

print("=" * 60)
print("ROTARY PATCH ONLY (accelerate 0.30.1, no .to() patch)")
print("=" * 60)

import transformers, accelerate, bitsandbytes
print(f"transformers={transformers.__version__}, accelerate={accelerate.__version__}, bnb={bitsandbytes.__version__}")

from transformers import AutoModelForVision2Seq, AutoProcessor, BitsAndBytesConfig

MODEL_ID = "moojink/openvla-7b-oft-finetuned-libero-goal"
HF_CACHE = os.path.join(WS, "hf_cache")

processor = AutoProcessor.from_pretrained(MODEL_ID, cache_dir=HF_CACHE, trust_remote_code=True)

bnb_config = BitsAndBytesConfig(load_in_8bit=True, llm_int8_skip_modules=["action_head"])
model = AutoModelForVision2Seq.from_pretrained(
    MODEL_ID, cache_dir=HF_CACHE, torch_dtype=torch.bfloat16,
    quantization_config=bnb_config, low_cpu_mem_usage=True, trust_remote_code=True,
)
print("[OK] Model loaded")

# Apply ONLY rotary fix
count = 0
if hasattr(model, "language_model") and hasattr(model.language_model, "model"):
    for layer in model.language_model.model.layers:
        if hasattr(layer, "self_attn") and hasattr(layer.self_attn, "rotary_emb"):
            rot = layer.self_attn.rotary_emb
            if hasattr(rot, "inv_freq") and rot.inv_freq is not None:
                target = layer.self_attn.q_proj.weight.device
                if rot.inv_freq.device != target:
                    rot.inv_freq = rot.inv_freq.to(target)
                    count += 1
print(f"[Compat] Aligned {count} rotary inv_freq buffers")

# Test inference
dummy_img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
from PIL import Image
pil_img = Image.fromarray(dummy_img)
prompt = "In: What action should the robot take to pick the black bowl on the table?\nOut:"
inputs = processor(prompt, pil_img).to("cuda:0", dtype=torch.bfloat16)

with torch.no_grad():
    action = model.predict_action(**inputs, unnorm_key="libero_goal_no_noops", do_sample=False)
print(f"[OK] Action: shape={action.shape}, sample={action[0]}")
print("\n*** RESULT: accelerate 0.30.1 + rotary-only patch = FULL SUCCESS ***")
