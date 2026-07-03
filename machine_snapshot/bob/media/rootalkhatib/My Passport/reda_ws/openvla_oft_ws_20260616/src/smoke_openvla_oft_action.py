import os
import sys
import time
import json
import pickle
import numpy as np
import torch

# Add paths to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")

import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

from experiments.robot.openvla_utils import get_vla, get_processor, get_proprio_projector, get_action_head, get_vla_action

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
        self.unnorm_key = ""  # Will be set dynamically

def get_gpu_memory_str():
    if torch.cuda.is_available():
        free, total = torch.cuda.mem_get_info()
        return f"Free = {free / (1024**3):.2f} GB / Total = {total / (1024**3):.2f} GB"
    return "GPU not available"

def main():
    print("=== OpenVLA-OFT One-Action Inference Smoke Test ===")
    
    gpu_before = get_gpu_memory_str()
    
    # We must specify the cache_dir to use our isolated hf_cache
    os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
    os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
    
    # Try loading in 8-bit first, then 4-bit, then bf16
    load_modes = [
        {"load_in_8bit": True, "load_in_4bit": False, "name": "8-bit Quantized"},
        {"load_in_8bit": False, "load_in_4bit": True, "name": "4-bit Quantized"},
        {"load_in_8bit": False, "load_in_4bit": False, "name": "bf16 Precision"}
    ]
    
    vla = None
    selected_mode = None
    
    for mode in load_modes:
        print(f"\nAttempting to load VLA model in {mode['name']}...")
        cfg = MockConfig(load_in_8bit=mode['load_in_8bit'], load_in_4bit=mode['load_in_4bit'])
        try:
            vla = get_vla(cfg)
            selected_mode = mode
            print(f"Successfully loaded VLA model!")
            openvla_oft_bob_compat.align_rotary_emb_devices(vla)
            break
        except Exception as e:
            print(f"Failed to load: {e}")
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                
    if vla is None:
        print("ERROR: Could not load VLA model!")
        sys.exit(1)
        
    cfg = MockConfig(load_in_8bit=selected_mode['load_in_8bit'], load_in_4bit=selected_mode['load_in_4bit'])
    
    # Enforce exact unnormalization key
    expected_key = "libero_goal_no_noops"
    if expected_key not in vla.norm_stats:
        raise ValueError(f"Expected unnormalization key '{expected_key}' not found in VLA norm_stats! Available keys: {list(vla.norm_stats.keys())}")
    cfg.unnorm_key = expected_key
    print(f"Using unnorm_key: '{cfg.unnorm_key}'")
    
    try:
        print("\nLoading processor...")
        processor = get_processor(cfg)
        
        print("Loading proprio projector...")
        llm_dim = vla.llm_dim if hasattr(vla, "llm_dim") else vla.config.text_config.hidden_size
        proprio_projector = get_proprio_projector(cfg, llm_dim=llm_dim, proprio_dim=8)
        
        print("Loading action head...")
        action_head = get_action_head(cfg, llm_dim=llm_dim)
        
        print("\nLoading sample observation...")
        obs_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft/experiments/robot/libero/sample_libero_spatial_observation.pkl"
        with open(obs_path, "rb") as f:
            obs = pickle.load(f)
            
        print(f"Observation loaded. Task: '{obs['task_description']}'")
        
        # Prepare inputs for get_vla_action
        # obs dictionary has keys: 'full_image', 'wrist_image', 'state', 'task_description'
        # Let's clone state to avoid modifying in place multiple times
        obs_copy = {
            "full_image": obs["full_image"],
            "wrist_image": obs["wrist_image"],
            "state": obs["state"].copy()
        }
        
        print("\nGenerating actions...")
        t0 = time.time()
        actions = get_vla_action(
            cfg=cfg,
            vla=vla,
            processor=processor,
            obs=obs_copy,
            task_label=obs["task_description"],
            action_head=action_head,
            proprio_projector=proprio_projector
        )
        duration = time.time() - t0
        print(f"Action generation completed in {duration:.2f}s!")
        
        # Verify result
        actions_arr = np.array(actions)
        print("\n=== Inference Results ===")
        print(f"Action chunk shape: {actions_arr.shape}")
        print(f"First action vector: {actions_arr[0]}")
        print(f"NUM_ACTIONS_CHUNK: {len(actions)}")
        print(f"PROPRIO_DIM: {obs['state'].shape[-1]}")
        
        is_finite = np.isfinite(actions_arr).all()
        print(f"Output is finite numeric: {is_finite}")
        
        # Capture GPU memory after action prediction
        gpu_after = get_gpu_memory_str()

        # Save result JSON v2
        result = {
            "model_id": cfg.pretrained_checkpoint,
            "repo_commit": "e4287e94541f459edc4feabc4e181f537cd569a8",
            "quantization_mode": selected_mode["name"],
            "unnorm_key": cfg.unnorm_key,
            "task_description": obs["task_description"],
            "action_shape": list(actions_arr.shape),
            "first_action_vector": actions_arr[0].tolist(),
            "finite_check": bool(is_finite),
            "inference_time": duration,
            "gpu_memory_before": gpu_before,
            "gpu_memory_after": gpu_after,
            "compatibility_patch_used": True,
            "official_no_patch_path_passed": False
        }
        
        out_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/smoke/action_smoke_result_v2.json"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(result, f, indent=4)
        print(f"\nSaved inference result to: {out_path}")
        
    except Exception as e:
        print(f"Action inference failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
