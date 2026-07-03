import sys
import os

# Add paths to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft")
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO")
sys.path.append("/home/rootalkhatib/envs/simvla/lib/python3.10/site-packages")
sys.path.append("/usr/lib/python3/dist-packages")

# Set HF Cache
os.environ["HF_HOME"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
os.environ["TRANSFORMERS_CACHE"] = "/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"

# Mujoco GL & PyOpenGL Settings
os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"

try:
    print("Attempting to import libero benchmark...")
    from libero.libero import benchmark
    from experiments.robot.libero.libero_utils import get_libero_env
    print("Libero imported successfully!")

    print("Fetching benchmark libero_goal...")
    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict["libero_goal"]()
    
    print("Getting task 0...")
    task = task_suite.get_task(0)
    print(f"Task 0 description: {task.language}")
    
    print("Creating environment...")
    env, task_description = get_libero_env(task, "openvla", resolution=256)
    print("Environment created successfully!")
    
    print("Resetting environment...")
    obs = env.reset()
    print("Environment reset successfully!")
    
    print("Closing environment...")
    env.close()
    print("LIBERO env smoke test passed!")
except Exception as e:
    print(f"LIBERO env smoke test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
