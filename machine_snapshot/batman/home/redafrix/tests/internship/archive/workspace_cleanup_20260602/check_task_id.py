import os, sys
from pathlib import Path
# Add necessary paths
sys.path.append(str(Path.cwd() / "fiper_ws/stage9_v2_tools"))
# Libero is in site-packages of the env, so it should be found.
try:
    from libero_pro_env_utils import task_bundle
    b = task_bundle("libero_10_with_milk", 7)
    print(f"TASK: {b['task'].language}")
    print(f"PROBLEM: {b['task'].problem_folder}")
    print(f"BDDL: {b['task'].bddl_file}")
    print(f"INIT_STATES: {len(b['init_states'])}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
