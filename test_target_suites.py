import os
import sys
import traceback
import argparse
from pathlib import Path
import numpy as np
import torch

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

def test_suites():
    # 1. Load SimVLA model
    print("Loading SimVLA model...")
    try:
        model, processor, device = load_simvla()
        print(f"SimVLA model loaded successfully on device: {device}")
    except Exception as e:
        print(f"Failed to load SimVLA model: {e}")
        traceback.print_exc()
        return False

    target_suites = [
        "libero_spatial_object",
        "libero_object_object",
        "libero_goal_object",
        "libero_spatial_env",
        "libero_object_env",
        "libero_goal_env",
    ]
    
    d = benchmark.get_benchmark_dict()
    overall_results = {}
    
    for suite_name in target_suites:
        if suite_name not in d:
            print(f"\nERROR: Suite {suite_name} not registered!")
            overall_results[suite_name] = {"registered": False, "tasks": []}
            continue
            
        print(f"\n==================================================")
        print(f"Testing Suite: {suite_name}")
        print(f"==================================================")
        
        try:
            bench = d[suite_name]()
            num_tasks = bench.get_num_tasks()
            print(f"Found {num_tasks} tasks in suite {suite_name}")
        except Exception as e:
            err_msg = str(e)
            print(f"Failed to instantiate benchmark for {suite_name}: {err_msg}")
            overall_results[suite_name] = {"registered": True, "instantiate_error": err_msg, "tasks": []}
            continue
            
        suite_task_results = []
        for task_id in range(min(10, num_tasks)):
            task = bench.get_task(task_id)
            task_name = task.name
            task_instruction = task.language
            print(f"\n  --- Task {task_id}: {task_name} ---")
            print(f"      Instruction: '{task_instruction}'")
            
            env = None
            task_status = "SUCCESS"
            error_details = ""
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
                first_action = actions[0].numpy()
                print(f"    Executing first action: {first_action}")
                
                obs, reward, done, info = env.step(first_action)
                print("    Step execution successful!")
                
            except Exception as e:
                err_msg = str(e)
                print(f"    ERROR on task {task_name}: {err_msg}")
                traceback.print_exc()
                task_status = "FAILED"
                error_details = err_msg
            finally:
                if env is not None:
                    try:
                        env.close()
                    except Exception:
                        pass
            
            suite_task_results.append({
                "task_id": task_id,
                "task_name": task_name,
                "status": task_status,
                "error": error_details
            })
            
        overall_results[suite_name] = {
            "registered": True,
            "tasks": suite_task_results
        }
        
    print("\n\n================ FINAL RESULTS SUMMARY ================")
    import json
    print(json.dumps(overall_results, indent=2))
    
    # Also write results to a local file inside workspace if needed
    with open("target_suites_results.json", "w") as f:
        json.dump(overall_results, f, indent=2)

if __name__ == "__main__":
    test_suites()
