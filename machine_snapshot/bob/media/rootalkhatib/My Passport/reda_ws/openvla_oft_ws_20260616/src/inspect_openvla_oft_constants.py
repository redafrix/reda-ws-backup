import os
import sys
import json
import torch

# Add paths to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")

# Set HF Cache
os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"

import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

from experiments.robot.openvla_utils import get_vla, find_checkpoint_file
from prismatic.vla.constants import NUM_ACTIONS_CHUNK, PROPRIO_DIM, ACTION_DIM

class MockConfig:
    pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
    load_in_8bit = True
    load_in_4bit = False
    use_film = False
    num_images_in_input = 2

cfg = MockConfig()
vla = get_vla(cfg)
openvla_oft_bob_compat.align_rotary_emb_devices(vla)

from huggingface_hub import hf_hub_download

# Find paths
action_head_path = hf_hub_download(
    repo_id=cfg.pretrained_checkpoint, filename="action_head--50000_checkpoint.pt"
)
proprio_projector_path = hf_hub_download(
    repo_id=cfg.pretrained_checkpoint, filename="proprio_projector--50000_checkpoint.pt"
)

snapshot_path = None
if hasattr(vla.config, "_name_or_path"):
    snapshot_path = str(vla.config._name_or_path)

norm_stats_keys = list(vla.norm_stats.keys())

data = {
    "NUM_ACTIONS_CHUNK": int(NUM_ACTIONS_CHUNK),
    "ACTION_DIM": int(ACTION_DIM),
    "PROPRIO_DIM": int(PROPRIO_DIM),
    "model_norm_stats_keys": norm_stats_keys,
    "action_head_checkpoint_path": str(action_head_path),
    "proprio_projector_checkpoint_path": str(proprio_projector_path),
    "model_repo_snapshot_path": snapshot_path,
}

output_path = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/outputs/smoke/constants_inspection.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    json.dump(data, f, indent=4)

print(f"Constants inspection saved to {output_path}")
print(json.dumps(data, indent=4))
