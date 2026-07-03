import os

report_path = "/home/redafrix/isaac_franka_env_probe/DYNAMICVLA_OFFICIAL_ASSETS_ONLY_REPORT.md"
content = """# DynamicVLA Official Assets Pipeline

## Official asset manual download links
DOM Testing Set: https://gateway.infinitescript.com/?f=DOM-Test
DOM 3D Objects: https://gateway.infinitescript.com/?f=DOM-3D-Objects
DOM 3D Scenes: https://gateway.infinitescript.com/?f=DOM-3D-Scenes

Objects are already downloaded, so priority is:
1. DOM Testing Set
2. DOM 3D Scenes

Save all downloaded archives into:
/home/redafrix/isaac_franka_env_probe/downloads
"""

with open(report_path, "a") as f:
    f.write(content)
