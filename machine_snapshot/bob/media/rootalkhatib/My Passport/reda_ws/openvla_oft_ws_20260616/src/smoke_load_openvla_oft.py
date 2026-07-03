import os
import sys
import time
import json
import torch

# Add paths to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")

import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

# From openvla-oft
from experiments.robot.openvla_utils import get_vla, get_processor, get_proprio_projector, get_action_head

class MockConfig:
    def __init__(self, load_in_8bit=False, load_in_4bit=False):
        self.model_family = "openvla"
        self.pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
        self.use_l1_regression = True
        self.use_diffusion = False
        self.use_film = False
        self.num_images_in_input = 2
        self.use_proprio = True
        self.center_crop = True
        self.lora_rank = 32
        self.load_in_8bit = load_in_8bit
        self.load_in_4bit = load_in_4bit

def print_gpu_memory(msg=""):
    if torch.cuda.is_available():
        free, total = torch.cuda.mem_get_info()
        print(f"{msg} GPU Memory: Free = {free / (1024**3):.2f} GB / Total = {total / (1024**3):.2f} GB")
    else:
        print(f"{msg} GPU not available")

def main():
    print("=== OpenVLA-OFT Model Load Smoke Test ===")
    print_gpu_memory("Initial")

    # Try different loading modes
    load_modes = [
        {"load_in_8bit": True, "load_in_4bit": False, "name": "8-bit Quantized"},
        {"load_in_8bit": False, "load_in_4bit": True, "name": "4-bit Quantized"},
        {"load_in_8bit": False, "load_in_4bit": False, "name": "bf16 Precision"}
    ]

    vla = None
    selected_mode = None

    for mode in load_modes:
        print(f"\nAttempting to load in {mode['name']}...")
        cfg = MockConfig(load_in_8bit=mode['load_in_8bit'], load_in_4bit=mode['load_in_4bit'])
        try:
            os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
            os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"

            t0 = time.time()
            vla = get_vla(cfg)
            openvla_oft_bob_compat.align_rotary_emb_devices(vla)
            load_time = time.time() - t0
            print(f"Successfully loaded VLA model in {load_time:.1f}s!")
            selected_mode = mode
            break
        except Exception as e:
            print(f"Failed to load in {mode['name']}: {e}")
            import traceback
            traceback.print_exc()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

    if vla is None:
        print("\nERROR: All loading attempts failed!")
        sys.exit(1)

    print_gpu_memory("After VLA Load")

    # Load processor, proprio projector, and action head
    cfg = MockConfig(load_in_8bit=selected_mode['load_in_8bit'], load_in_4bit=selected_mode['load_in_4bit'])
    try:
        print("\nLoading processor...")
        processor = get_processor(cfg)
        print("Processor loaded successfully!")

        print("\nLoading proprio projector...")
        llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
        proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
        print("Proprio projector loaded successfully!")

        print("\nLoading action head...")
        action_head = get_action_head(cfg, llm_dim=llm_dim)
        print("Action head loaded successfully!")

        print("\n=== Summary ===")
        print(f"Model ID: {cfg.pretrained_checkpoint}")
        print(f"Quantization Mode: {selected_mode['name']}")
        print(f"Action Head Loaded: {action_head is not None} ({type(action_head)})")
        print(f"Proprio Projector Loaded: {proprio_projector is not None} ({type(proprio_projector)})")
        print_gpu_memory("Final")

    except Exception as e:
        print(f"Failed to load extra components: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
