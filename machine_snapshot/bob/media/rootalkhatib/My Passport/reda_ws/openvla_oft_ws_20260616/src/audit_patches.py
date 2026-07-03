import subprocess
import os
import sys

workspace_dir = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616"
log_dir = os.path.join(workspace_dir, "logs/patch_audit_20260616")

env = os.environ.copy()
env["HF_HOME"] = os.path.join(workspace_dir, "hf_cache")
env["TRANSFORMERS_CACHE"] = os.path.join(workspace_dir, "hf_cache")
env["PYTHONPATH"] = f"{workspace_dir}/src/openvla-oft:{env.get('PYTHONPATH', '')}"

def run_test_case(name, code):
    log_file_path = os.path.join(log_dir, f"{name}.log")
    print(f"\nRunning {name}...")
    
    proc = subprocess.Popen(
        [sys.executable, "-c", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
        text=True
    )
    stdout, _ = proc.communicate()
    
    with open(log_file_path, "w") as f:
        f.write(stdout)
        
    status = "PASSED" if proc.returncode == 0 else "FAILED"
    print(f"Finished {name} - Status: {status}")
    if proc.returncode != 0:
        lines = stdout.strip().split("\n")
        print("  Last 10 lines of output:")
        for line in lines[-10:]:
            print(f"    {line}")
    return proc.returncode == 0

# Test 1: Official load path, 8-bit, no monkey patch
code_no_patch_8bit = """
import torch
from experiments.robot.openvla_utils import get_vla

class MockConfig:
    pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
    load_in_8bit = True
    load_in_4bit = False
    use_film = False
    num_images_in_input = 2

cfg = MockConfig()
vla = get_vla(cfg)
print("SUCCESSFULLY LOADED 8-BIT MODEL")
"""

# Test 2: Official load path, 4-bit, no monkey patch
code_no_patch_4bit = """
import torch
from experiments.robot.openvla_utils import get_vla

class MockConfig:
    pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
    load_in_8bit = False
    load_in_4bit = True
    use_film = False
    num_images_in_input = 2

cfg = MockConfig()
vla = get_vla(cfg)
print("SUCCESSFULLY LOADED 4-BIT MODEL")
"""

# Test 3: Patched 8-bit path
code_patched_8bit = """
import torch
import transformers.modeling_utils as _mu
_original_to = _mu.PreTrainedModel.to

def _patched_to(self, *args, **kwargs):
    if getattr(self, "quantization_method", None) is not None:
        return self
    return _original_to(self, *args, **kwargs)

_mu.PreTrainedModel.to = _patched_to

from experiments.robot.openvla_utils import get_vla

class MockConfig:
    pretrained_checkpoint = "moojink/openvla-7b-oft-finetuned-libero-goal"
    load_in_8bit = True
    load_in_4bit = False
    use_film = False
    num_images_in_input = 2

cfg = MockConfig()
vla = get_vla(cfg)
print("SUCCESSFULLY LOADED PATCHED 8-BIT MODEL")
"""

run_test_case("test_no_patch_8bit", code_no_patch_8bit)
run_test_case("test_no_patch_4bit", code_no_patch_4bit)
run_test_case("test_patched_8bit", code_patched_8bit)
