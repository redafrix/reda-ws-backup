import os
import sys
import json
import traceback
import numpy as np
from pathlib import Path

def get_machine_info():
    hostname = os.uname()[1]
    if "pcrobot" in hostname:
        return "Bob", Path("/media/rootalkhatib/My Passport/reda_ws")
    elif "sam" in hostname:
        return "Sam", Path("/home/rootalkhatib/test/reda_ws")
    else:
        # Try to guess from environment or current path
        cwd = os.getcwd()
        if "/media/rootalkhatib/My Passport/reda_ws" in cwd:
            return "Bob", Path("/media/rootalkhatib/My Passport/reda_ws")
        elif "/home/rootalkhatib/test/reda_ws" in cwd:
            return "Sam", Path("/home/rootalkhatib/test/reda_ws")
        return hostname, Path(os.environ.get("REDA_WS", "/media/rootalkhatib/My Passport/reda_ws"))

machine, REDA_WS = get_machine_info()

SIM = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_PRO = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
ASYNCHVLA = REDA_WS / "asynchvla_ws/src"

for p in [ASYNCHVLA, SIM, LIBERO_PRO]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

def setup_env_vars():
    config_name = "libero_pro_bob" if machine == "Bob" else "libero_pro_sam"
    config_path = REDA_WS / f"asynchvla_ws/configs/{config_name}"
    if not config_path.exists():
        config_path = REDA_WS / "asynchvla_ws/configs/libero_pro_bob"
        
    os.environ["LIBERO_CONFIG_PATH"] = str(config_path)
    os.environ["MUJOCO_GL"] = "egl"
    os.environ["PYOPENGL_PLATFORM"] = "egl"
    
    # Ensure LIBERO_PRO is in PYTHONPATH for subprocesses if any
    if "PYTHONPATH" in os.environ:
        os.environ["PYTHONPATH"] = str(LIBERO_PRO) + ":" + os.environ["PYTHONPATH"]
    else:
        os.environ["PYTHONPATH"] = str(LIBERO_PRO)

def smoke_test():
    setup_env_vars()
    
    # LIBERO imports after path setup
    try:
        from libero.libero import benchmark, get_libero_path
        from libero.libero.envs import OffScreenRenderEnv
    except ImportError as e:
        print(f"Failed to import libero: {e}")
        return [{"machine": machine, "status": "FAIL", "error_message": f"ImportError: {e}", "error_type": "IMPORT_ERROR"}]

    results = []
    
    # Try to get suites from libero_suites list if it exists in libero.benchmark
    try:
        import libero.benchmark as lb
        suite_names = getattr(lb, "libero_suites", None)
        if suite_names is None:
            # Fallback to benchmark dict
            suite_names = sorted(benchmark.get_benchmark_dict().keys())
    except Exception:
        suite_names = sorted(benchmark.get_benchmark_dict().keys())
    
    print(f"Found {len(suite_names)} suites.")
    
    benchmark_dict = benchmark.get_benchmark_dict()
    
    for suite_name in suite_names:
        if suite_name not in benchmark_dict:
            print(f"Suite {suite_name} not found in benchmark_dict, skipping.")
            continue
            
        print(f"Testing suite: {suite_name}")
        try:
            bench = benchmark_dict[suite_name]()
            num_tasks = bench.get_num_tasks()
            
            for task_id in range(num_tasks):
                task = bench.get_task(task_id)
                task_name = task.name
                print(f"  Task {task_id}: {task_name}")
                
                status = "PASS"
                error_message = ""
                error_type = "SUCCESS"
                
                try:
                    bddl_path = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
                    if not bddl_path.exists():
                        raise FileNotFoundError(f"BDDL file not found: {bddl_path}")
                    
                    env_args = {
                        "bddl_file_name": str(bddl_path),
                        "camera_heights": 128,
                        "camera_widths": 128,
                    }
                    
                    env = OffScreenRenderEnv(**env_args)
                    env.reset()
                    # Step once with zero action
                    zero = np.array([0,0,0,0,0,0,-1], dtype=np.float32)
                    env.step(zero)
                    env.close()
                    
                except FileNotFoundError as e:
                    status = "FAIL"
                    error_message = str(e)
                    error_type = "MISSING_ASSET"
                except Exception as e:
                    status = "FAIL"
                    error_message = str(e)
                    # Try to categorize error
                    err_str = str(e).lower()
                    if "xml" in err_str or "obj" in err_str or "mesh" in err_str or "file not found" in err_str:
                        error_type = "MISSING_ASSET"
                    elif "init" in err_str:
                        error_type = "MISSING_INIT"
                    else:
                        error_type = "CONFIG_ERROR"
                    print(f"    FAILED: {error_message}")
                
                results.append({
                    "machine": machine,
                    "suite_name": suite_name,
                    "task_name": task_name,
                    "status": status,
                    "error_message": error_message,
                    "error_type": error_type
                })
                
        except Exception as e:
            print(f"Failed to instantiate suite {suite_name}: {e}")
            results.append({
                "machine": machine,
                "suite_name": suite_name,
                "task_name": "ALL",
                "status": "FAIL",
                "error_message": str(e),
                "error_type": "SUITE_INSTANTIATION_ERROR"
            })

    return results

if __name__ == "__main__":
    all_results = smoke_test()
    output_file = "smoke_test_results.json"
    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Results saved to {output_file}")
