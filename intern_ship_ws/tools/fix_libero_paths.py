import os
import yaml
from pathlib import Path

# New paths
ROOT = Path(__file__).parents[1]
benchmark_root = ROOT / "assets/data/LIBERO/libero/libero"

new_config = {
    "benchmark_root": str(benchmark_root),
    "bddl_files": str(benchmark_root / "bddl_files"),
    "init_states": str(benchmark_root / "init_files"),
    "datasets": str(benchmark_root.parent / "datasets"),
    "assets": str(benchmark_root / "assets"),
}

# Update ~/.libero/config.yaml
libero_config_path = os.path.expanduser("~/.libero")
global_config_file = os.path.join(libero_config_path, "config.yaml")
os.makedirs(libero_config_path, exist_ok=True)
with open(global_config_file, "w") as f:
    yaml.dump(new_config, f)
print(f"Updated {global_config_file}")

# Update workspace config if it exists
workspace_config_file = ROOT / "simvla/config/libero/config.yaml"
if workspace_config_file.exists():
    with open(workspace_config_file, "w") as f:
        yaml.dump(new_config, f)
    print(f"Updated {workspace_config_file}")

for k, v in new_config.items():
    print(f"  {k}: {v}")
