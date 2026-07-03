import sys
from pathlib import Path

readme_path = Path("/home/redafrix/isaac_franka_env_probe/dynamic-vla/README.md")
if readme_path.exists():
    print(readme_path.read_text())
else:
    print("README not found")
