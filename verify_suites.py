import os
import sys
import traceback
from pathlib import Path
import numpy as np
import torch

# Determine workspace path
REDA_WS = Path(os.environ.get("REDA_WS", "/home/rootalkhatib/test/reda_ws"))
print(f"REDA_WS: {REDA_WS}")

# Insert paths to sys.path
SIM = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_PRO = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
ASYNCHVLA = REDA_WS / "asynchvla_ws/src"

for p in [ASYNCHVLA, SIM, LIBERO_PRO]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

try:
    from data_collection_stage9.libero_pro_env_utils import make_env, reset_to_init, obs_images, obs_to_proprio
    from data_collection_stage9.simvla_candidate_sampler import load_simvla, sample_candidate
    from libero.libero import benchmark
except Exception as e:
    print(f"Failed to import modules: {e}")
    traceback.print_exc()
    sys.exit(1)

def verify_all_suites():
    # 1. Load SimVLA model
    print("Loading SimVLA model...")
    try:
        model, processor, device = load_simvla()
        print(f"SimVLA model loaded successfully on device: {device}")
    except Exception as e:
        print(f"Failed to load SimVLA model: {e}")
        traceback.print_exc()
        return False

    # Get benchmarks dict
    d = benchmark.get_benchmark_dict()
    
    # Check if we want to run all suites (1 task each)
    run_all = len(sys.argv) > 1 and sys.argv[1] == "--all"
    
    if run_all:
        target_suites = sorted(list(d.keys()))
        print(f"Running all {len(target_suites)} registered suites (1 task each)...")
    else:
        # Target suites
        target_suites = [
            "libero_object_with_mug",
            "libero_spatial_with_mug",
            "libero_goal_with_mug",
            "libero_10_with_mug"
        ]
    
    overall_success = True
    
    for suite_name in target_suites:
        if suite_name not in d:
            print(f"ERROR: Suite {suite_name} not found in registered benchmarks!")
            overall_success = False
            continue
            
        print(f"\n==================================================")
        print(f"Testing Suite: {suite_name}")
        print(f"==================================================")
        
        try:
            bench = d[suite_name]()
            num_tasks = bench.get_num_tasks()
            print(f"Found {num_tasks} tasks in suite {suite_name}")
            if num_tasks == 0:
                print(f"Skipping suite {suite_name} (no tasks found)")
                continue
        except Exception as e:
            print(f"Failed to instantiate benchmark for {suite_name}: {e}")
            overall_success = False
            continue
            
        # Test only 1 task if run_all is specified, otherwise all tasks in target suites
        num_to_test = 1 if run_all else num_tasks
        for task_id in range(num_to_test):
            task = bench.get_task(task_id)
            task_name = task.name
            task_instruction = task.language
            print(f"\n  --- Task {task_id}: {task_name} ---")
            print(f"      Instruction: '{task_instruction}'")
            
            env = None
            try:
                # Instantiate env
                print("    Instantiating environment...")
                env, b = make_env(suite_name, task_id)
                
                # Reset environment
                print("    Resetting environment...")
                init_state = b["init_states"][0] if len(b["init_states"]) > 0 else None
                obs = reset_to_init(env, init_state=init_state)
                
                # Get images and proprio
                img0, img1 = obs_images(obs)
                proprio = obs_to_proprio(obs)
                
                # Run candidate sampler to predict action chunk
                print("    Generating SimVLA chunk (1 candidate action prediction)...")
                # We use seed=42, steps=10, flowtrace=True
                out = sample_candidate(
                    model=model,
                    processor=processor,
                    prompt=task_instruction,
                    image0=img0,
                    image1=img1,
                    proprio=proprio,
                    seed=42,
                    device=device,
                    steps=10,
                    flowtrace=True
                )
                
                # Get action chunk and take first step
                actions = out["candidate_action_env"]
                print(f"    Action chunk shape: {actions.shape}")
                first_action = actions[0].numpy()
                print(f"    Executing first action: {first_action}")
                
                obs, reward, done, info = env.step(first_action)
                print("    Step execution successful!")
                
            except Exception as e:
                print(f"    ERROR on task {task_name}: {e}")
                traceback.print_exc()
                overall_success = False
            finally:
                if env is not None:
                    try:
                        env.close()
                    except Exception:
                        pass
                        
    return overall_success

if __name__ == "__main__":
    success = verify_all_suites()
    if success:
        print("\nAll suites/tasks verified successfully!")
        sys.exit(0)
    else:
        print("\nVerification failed for one or more tasks.")
        sys.exit(1)
