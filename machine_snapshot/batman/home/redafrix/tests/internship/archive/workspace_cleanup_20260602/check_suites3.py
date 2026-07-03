import os
import sys

try:
    from libero.libero import benchmark
    from libero.libero.envs import OffScreenRenderEnv
    from libero.libero import get_libero_path
except ImportError as e:
    print(f"IMPORT_ERROR: {e}")
    sys.exit(1)

TARGET_SUITES = [
    "libero_spatial_object",
]

def main():
    for suite in TARGET_SUITES:
        print(f"--- Testing Suite: {suite} ---")
        try:
            task_dict = benchmark.get_benchmark_dict()[suite]()
            num_tasks = task_dict.get_num_tasks()
            
            for task_id in range(1):
                task = task_dict.get_task(task_id)
                bddl_dir = get_libero_path("bddl_files")
                expected_path = os.path.join(bddl_dir, task.problem_folder, task.bddl_file)
                print(f"Expected BDDL path: {expected_path}")
                print(f"Path exists? {os.path.exists(expected_path)}")
                
                if not os.path.exists(expected_path):
                    print("Let's see what is inside bddl_dir:")
                    print(os.listdir(bddl_dir))
                    
        except Exception as e:
            print(f"Suite {suite} FAIL: {type(e).__name__}: {str(e)}")

if __name__ == "__main__":
    main()
