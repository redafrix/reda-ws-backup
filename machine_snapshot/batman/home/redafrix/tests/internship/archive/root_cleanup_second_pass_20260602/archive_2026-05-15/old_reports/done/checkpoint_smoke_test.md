# Checkpoint Smoke Test

## Command

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
source asynchvla_ws/scripts/activate_simvla_bob.sh >/dev/null
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
python3 - <<PY
import os, json, traceback
from pathlib import Path
ckpt = "intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000"
print("cwd", os.getcwd())
print("offline", os.environ.get("HF_HUB_OFFLINE"), os.environ.get("TRANSFORMERS_OFFLINE"))
from models.modeling_smolvlm_vla import SmolVLMVLA
print("import_model OK", SmolVLMVLA)
m = SmolVLMVLA.from_pretrained(ckpt)
print("load OK")
PY
```

## Checkpoint path

```text
intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000
```

Files:

```text
config.json 570 bytes
model.safetensors 3245557952 bytes
state.json 22 bytes
```

Config values from `config.json`:

```json
{
  "action_mode": "libero_joint",
  "architectures": ["SmolVLMVLA"],
  "depth": 24,
  "dim_time": 32,
  "dtype": "float32",
  "hidden_size": 1024,
  "image_size": 384,
  "max_len_seq": 512,
  "mlp_ratio": 4.0,
  "model_type": "smolvlm_vla",
  "num_actions": 10,
  "num_heads": 16,
  "num_views": 3,
  "predict_uncertainty": true,
  "return_uncertainty": false,
  "smolvlm_model_path": "HuggingFaceTB/SmolVLM-500M-Instruct",
  "transformers_version": "4.57.6",
  "uncertainty_beta": 0.5,
  "uncertainty_eps": 1e-06,
  "use_adaln": false,
  "use_proprio": true
}
```

## Result

The model class imported successfully:

```text
import_model OK <class models.modeling_smolvlm_vla.SmolVLMVLA>
```

Checkpoint loading failed before the action checkpoint could be fully instantiated because the SmolVLM backbone referenced by `smolvlm_model_path = HuggingFaceTB/SmolVLM-500M-Instruct` was not found in the local Hugging Face cache. Offline mode was set intentionally to avoid triggering a large model download during the smoke test.

Exact error excerpt:

```text
load ERR OSError We couldnt connect to https://huggingface.co to load the files, and couldnt find them in the cached files.
Check your internet connection or see how to run the library in offline mode at https://huggingface.co/docs/transformers/installation#offline-mode.

huggingface_hub.errors.LocalEntryNotFoundError: Cannot find the requested files in the disk cache and outgoing traffic has been disabled. To enable hf.co look-ups and downloads online, set local_files_only to False.

File "/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/code/SimVLA_modified/models/modeling_smolvlm_vla.py", line 84, in __init__
  self.vlm = AutoModelForImageTextToText.from_pretrained(
```

## Decision

Stop at Phase 2. Do not implement trace extraction or rater training until the SmolVLM backbone files are available locally or the user explicitly approves downloading them.
