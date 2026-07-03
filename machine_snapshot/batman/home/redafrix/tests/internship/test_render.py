import sys
import os
from pathlib import Path
import numpy as np

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
LIBERO_PRO = REDA_WS / "intern_ship_ws/assets/repos/LIBERO-PRO"
ASYNCHVLA = REDA_WS / "asynchvla_ws/src"
SIMVLA = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"

for p in [ASYNCHVLA, LIBERO_PRO, SIMVLA]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

os.environ["LIBERO_CONFIG_PATH"] = str(REDA_WS / "asynchvla_ws/configs/libero_pro_bob")
os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"

from libero.libero.envs import OffScreenRenderEnv
from data_collection_stage9.sim_state_utils import set_state
from data_collection_stage9.libero_pro_env_utils import obs_images, obs_to_proprio

# Find a state file
state_file = "/home/rootalkhatib/states_temp/worker_0_libero_goal_object_official_t0_r107_s0000.npz"
if not os.path.exists(state_file):
    # Try finding any state file
    import glob
    files = glob.glob("/home/rootalkhatib/states_temp/*.npz")
    if files:
        state_file = files[0]
    else:
        print("No NPZ files found in /home/rootalkhatib/states_temp")
        sys.exit(1)

print(f"Loading state file: {state_file}")
data = np.load(state_file, allow_pickle=True)
state_dict = {"kind": str(data["kind"]), "flat": data["flat"]}

# Let's instantiate environment for Task 0
bddl_path = LIBERO_PRO / "libero/libero/bddl_files/libero_goal_object_official/open_the_middle_drawer_of_the_cabinet.bddl"
print(f"BDDL exists: {bddl_path.exists()} ({bddl_path})")

env = OffScreenRenderEnv(bddl_file_name=str(bddl_path), camera_heights=128, camera_widths=128)
obs = env.reset()
set_state(env, state_dict)
obs = env._get_observations()

img, wrist = obs_images(obs)
prop = obs_to_proprio(obs)

print(f"img shape: {img.shape}, min/max: {img.min()}/{img.max()}")
print(f"wrist shape: {wrist.shape}, min/max: {wrist.min()}/{wrist.max()}")
print(f"proprio: {prop}")
env.close()
