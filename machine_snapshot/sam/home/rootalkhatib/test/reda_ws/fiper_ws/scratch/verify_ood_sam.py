import sys
import os
from pathlib import Path

# Add the src folder to path
sys.path.insert(0, "/home/rootalkhatib/test/reda_ws/fiper_ws/trash/h10_goal_object_ood_all_tasks_100ep_selected_cap_timeout800_20260615/src")
from collect_fiper_uncertainty_receding_dean_v1 import make_env

def mock_get_libero_path(key):
    root = "/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO"
    if key == "bddl_files":
        return f"{root}/libero/libero/bddl_files"
    if key == "init_states":
        return f"{root}/libero/libero/init_states"
    return ""

def test():
    from libero.libero.benchmark import get_benchmark_dict
    class DummyOffScreen:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
        def seed(self, s): pass
        def reset(self): return {}
        def set_init_state(self, s): return {}
        def step(self, a): return {}, 0, False, {}
        def close(self): pass

    bench_dict = get_benchmark_dict()
    for task_id in range(18):
        env, bundle = make_env(bench_dict, mock_get_libero_path, DummyOffScreen, "libero_goal_object_ood", task_id, 128, 10)
        print(f"Task {task_id}: {bundle['resolved_problem_folder']}")
        if "ood" not in bundle["resolved_problem_folder"]:
            print(f"WARNING: Task {task_id} did not resolve to an OOD folder!")
            sys.exit(1)

test()