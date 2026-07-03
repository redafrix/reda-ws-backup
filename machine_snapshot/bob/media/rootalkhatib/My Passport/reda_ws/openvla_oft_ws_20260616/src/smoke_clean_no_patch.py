"""
Clean-room smoke test: Load OpenVLA-OFT and run action inference
WITHOUT any monkey patches, using the clean environment.
"""
import sys, os, time
import torch
import numpy as np

WS = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616"
REPO = os.path.join(WS, "src", "openvla-oft")
sys.path.insert(0, REPO)

print("=" * 60)
print("CLEAN-ROOM SMOKE: NO MONKEY PATCHES")
print("=" * 60)
print(f"Python: {sys.executable}")
print(f"torch: {torch.__version__}")

import transformers
print(f"transformers: {transformers.__version__}")
print(f"transformers file: {transformers.__file__}")

import accelerate
print(f"accelerate: {accelerate.__version__}")

import bitsandbytes
print(f"bitsandbytes: {bitsandbytes.__version__}")

# ---- Step 1: Load model (NO patches) ----
print("\n--- STEP 1: Loading model (NO patches) ---")
MODEL_ID = "moojink/openvla-7b-oft-finetuned-libero-goal"
HF_CACHE = os.path.join(WS, "hf_cache")

from transformers import AutoModelForVision2Seq, AutoProcessor, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_skip_modules=["action_head"],
)

t0 = time.time()
try:
    processor = AutoProcessor.from_pretrained(MODEL_ID, cache_dir=HF_CACHE, trust_remote_code=True)
    print(f"[OK] Processor loaded in {time.time()-t0:.1f}s")
except Exception as e:
    print(f"[FAIL] Processor: {e}")
    sys.exit(1)

t1 = time.time()
try:
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_ID,
        cache_dir=HF_CACHE,
        torch_dtype=torch.bfloat16,
        quantization_config=bnb_config,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
    )
    print(f"[OK] Model loaded in {time.time()-t1:.1f}s")
except Exception as e:
    print(f"[FAIL] Model load: {type(e).__name__}: {e}")
    sys.exit(1)

# ---- Step 2: Check rotary device ----
print("\n--- STEP 2: Checking rotary embedding devices ---")
mismatch_count = 0
if hasattr(model, "language_model") and hasattr(model.language_model, "model"):
    for i, layer in enumerate(model.language_model.model.layers):
        if hasattr(layer, "self_attn") and hasattr(layer.self_attn, "rotary_emb"):
            rot = layer.self_attn.rotary_emb
            if hasattr(rot, "inv_freq") and rot.inv_freq is not None:
                qw = layer.self_attn.q_proj.weight.device if hasattr(layer.self_attn.q_proj, "weight") else "N/A"
                if str(rot.inv_freq.device) != str(qw):
                    mismatch_count += 1
                    if mismatch_count <= 3:
                        print(f"  Layer {i}: inv_freq on {rot.inv_freq.device}, q_proj on {qw}")
    if mismatch_count == 0:
        print("[OK] All rotary embeddings on correct device")
    else:
        print(f"[WARN] {mismatch_count} layers have rotary device mismatch")

# ---- Step 3: Action inference ----
print("\n--- STEP 3: Action inference (NO patches) ---")
dummy_img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
from PIL import Image
pil_img = Image.fromarray(dummy_img)
prompt = "In: What action should the robot take to pick the black bowl on the table?\nOut:"

inputs = processor(prompt, pil_img).to("cuda:0", dtype=torch.bfloat16)

try:
    with torch.no_grad():
        action = model.predict_action(**inputs, unnorm_key="libero_goal_no_noops", do_sample=False)
    print(f"[OK] Action shape: {action.shape}, dtype: {action.dtype}")
    print(f"     Action sample: {action[0]}")
except Exception as e:
    print(f"[FAIL] Action inference: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("SMOKE TEST COMPLETE")
print("=" * 60)
