# Activate virtual environment
source /home/rootalkhatib/openvla_oft_env_20260616/bin/activate

# HF Home and Cache
export HF_HOME="/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
export TRANSFORMERS_CACHE="/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
export HF_HUB_CACHE="/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/hf_cache"
export HF_HUB_ENABLE_HF_TRANSFER=1

# Mujoco GL & PyOpenGL Settings
export MUJOCO_GL="egl"
export PYOPENGL_PLATFORM="egl"

# Execution configs
export TOKENIZERS_PARALLELISM="false"
export USE_TF="0"
export USE_FLAX="0"
export CUDA_VISIBLE_DEVICES="0"

# PYTHONPATH entries
export PYTHONPATH="/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616/src/openvla-oft:/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO:$PYTHONPATH"
