import sys
import os

# Add workspace and LIBERO repo paths to sys.path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages")
sys.path.append("/usr/lib/python3/dist-packages")

os.environ["LIBERO_CONFIG_PATH"] = "/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/configs/libero_pro_bob"

import openvla_oft_bob_compat
openvla_oft_bob_compat.apply_quantized_to_patch()

from libero.libero import benchmark
from experiments.robot.libero.libero_utils import get_libero_env

# Apply our monkey patch so we can load the env
from run_openvla_goal_object_pro_correct_smoke_bob import patch_libero_tabletop_manipulation
patch_libero_tabletop_manipulation()

benchmark_dict = benchmark.get_benchmark_dict()
task_suite = benchmark_dict['libero_goal_object']()
task = task_suite.get_task(9)

class MockCfg:
    model_family = 'openvla'
    env_img_res = 256
    use_film = False
    num_trials_per_task = 1
    initial_states_path = 'DEFAULT'
    task_suite_name = 'libero_goal_object'
    seed = 0
    pretrained_checkpoint = 'moojink/openvla-7b-oft-finetuned-libero-goal'
    load_in_8bit = True
    load_in_4bit = False
    use_l1_regression = True
    use_diffusion = False
    use_film = False
    num_images_in_input = 2
    use_proprio = True
    center_crop = True
    lora_rank = 32
    unnorm_key = 'libero_goal_no_noops'
    num_open_loop_steps = 8
    num_steps_wait = 10
    use_wandb = False

cfg = MockCfg()
env, desc = get_libero_env(task, 'openvla', resolution=256)

print("\n--- Environmental Diagnostics ---")
print("Parsed regions in problem:", env.env.parsed_problem["regions"].keys())
print("Fixtures in env:", list(env.env.fixtures_dict.keys()))
print("Objects in env:", list(env.env.objects_dict.keys()))
print("Object sites loaded:", list(env.env.object_sites_dict.keys()))

# Let's inspect raw XML sites
print("\n--- Raw XML Site traversal ---")
for name, body in list(env.env.fixtures_dict.items()) + list(env.env.objects_dict.items()):
    if hasattr(body, "worldbody") and body.worldbody is not None:
        top_body = body.worldbody.find("body")
        if top_body is not None:
            all_bodies = [top_body] + top_body.findall(".//body")
            print(f"Body: {name}")
            for part in all_bodies:
                part_name = part.get("name")
                sites = part.findall("./site")
                for s in sites:
                    print(f"  Part: {part_name}, Site Name: {s.get('name')}")
