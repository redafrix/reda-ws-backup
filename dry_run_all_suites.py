import os
import sys
import traceback
from pathlib import Path

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
    from data_collection_stage9.libero_pro_env_utils import make_env, reset_to_init
    from libero.libero import benchmark
except Exception as e:
    print(f"Failed to import modules: {e}")
    traceback.print_exc()
    sys.exit(1)

def dry_run_suites():
    d = benchmark.get_benchmark_dict()
    suites = sorted(list(d.keys()))
    
    results = {}
    
    for suite_name in suites:
        print(f"\n==================================================")
        print(f"Testing Suite: {suite_name}")
        print(f"==================================================")
        
        try:
            bench = d[suite_name]()
            num_tasks = bench.get_num_tasks()
            print(f"Found {num_tasks} tasks in suite {suite_name}")
            if num_tasks == 0:
                results[suite_name] = ("SKIPPED", "No tasks found")
                continue
        except Exception as e:
            err_msg = str(e)
            print(f"Failed to instantiate benchmark for {suite_name}: {err_msg}")
            results[suite_name] = ("FAILED_BENCHMARK_INSTANTIATION", err_msg)
            continue
            
        # Try to make and reset the first task
        task_id = 0
        task = bench.get_task(task_id)
        task_name = task.name
        print(f"Instantiating Task {task_id}: {task_name}")
        
        env = None
        try:
            env, b = make_env(suite_name, task_id)
            init_state = b["init_states"][0] if len(b["init_states"]) > 0 else None
            obs = reset_to_init(env, init_state=init_state)
            print("Successfully instantiated and reset!")
            results[suite_name] = ("SUCCESS", f"Task: {task_name}")
        except Exception as e:
            err_msg = str(e)
            print(f"Failed to make/reset task {task_name}: {err_msg}")
            traceback.print_exc()
            results[suite_name] = ("FAILED_TASK_EXECUTION", err_msg)
        finally:
            if env is not None:
                try:
                    env.close()
                except Exception:
                    pass
                    
    print("\n\n================ FINAL RESULTS ================")
    success_count = 0
    skipped_count = 0
    failed_count = 0
    for s, (status, detail) in sorted(results.items()):
        print(f"{s}: {status} - {detail}")
        if status == "SUCCESS":
            success_count += 1
        elif status == "SKIPPED":
            skipped_count += 1
        else:
            failed_count += 1
            
    print(f"\nSummary: {success_count} succeeded, {skipped_count} skipped, {failed_count} failed out of {len(suites)} suites.")

if __name__ == "__main__":
    dry_run_suites()
