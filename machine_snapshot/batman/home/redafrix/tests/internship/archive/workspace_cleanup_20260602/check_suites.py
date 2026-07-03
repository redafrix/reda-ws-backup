import os
import sys
import traceback

try:
    from libero.libero import benchmark
    from libero.libero.envs import OffScreenRenderEnv
    from libero.libero import get_libero_path
except ImportError as e:
    print(f"IMPORT_ERROR: {e}")
    sys.exit(1)

TARGET_SUITES = [
    "libero_spatial_object",
    "libero_object_object",
    "libero_goal_object",
    "libero_spatial_env",
    "libero_object_env",
    "libero_goal_env"
]

def main():
    print(f"LIBERO_PATH: {get_libero_path()}")
    for suite in TARGET_SUITES:
        print(f"--- Testing Suite: {suite} ---")
        try:
            task_dict = benchmark.get_benchmark_dict()[suite]()
            num_tasks = task_dict.get_num_tasks()
            print(f"Suite {suite} registered with {num_tasks} tasks.")
            
            for task_id in range(min(10, num_tasks)):
                task_name = "unknown"
                try:
                    task = task_dict.get_task(task_id)
                    task_name = task.name
                    task_bddl = task.bddl_file
                    task_init = task.init_states_file
                    
                    env_args = {
                        "bddl_file_name": task_bddl,
                        "camera_heights": 256,
                        "camera_widths": 256,
                        "control_freq": 20,
                    }
                    
                    env = OffScreenRenderEnv(**env_args)
                    env.seed(0)
                    env.reset()
                    
                    try:
                        init_state = benchmark.get_task_init_states(task_id, task_dict)
                    except Exception:
                        # Fallback for some libero versions
                        init_state = benchmark.get_task_init_states(task_id, task_init)
                        
                    # Get instruction
                    instruction = task.language
                    
                    # Generate one action (dummy)
                    action = [0.0] * 7
                    env.step(action)
                    env.close()
                    print(f"  Task {task_id} ({task_name}): PASS")
                except Exception as e:
                    print(f"  Task {task_id} ({task_name}): FAIL - {type(e).__name__}: {str(e)}")
                    # traceback.print_exc()
                    if "env" in locals() and hasattr(env, "close"):
                        try:
                            env.close()
                        except:
                            pass
        except KeyError:
            print(f"Suite {suite} FAIL: KeyError (Suite not registered in benchmark.py)")
        except Exception as e:
            print(f"Suite {suite} FAIL: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    main()
