import sys
import numpy as np
from pathlib import Path

# Add openpi src to path
sys.path.append("/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/openpi/src")

from openpi.policies import policy_config as _policy_config
from openpi.training import config as _config
from openpi.policies import libero_policy

def main():
    checkpoint_dir = "/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623/checkpoints/pi05_libero"
    config_name = "pi05_libero"
    
    print("Loading policy...")
    policy = _policy_config.create_trained_policy(
        _config.get_config(config_name), 
        checkpoint_dir
    )
    
    print("Generating dummy observation...")
    obs = libero_policy.make_libero_example()
    
    print("Running inference...")
    outputs = policy.infer(obs)
    
    actions = outputs["actions"]
    print("Inference success!")
    print(f"Action shape: {actions.shape}")
    print(f"Action finite: {np.isfinite(actions).all()}")
    print("Action chunk values:")
    print(actions)

if __name__ == "__main__":
    main()
