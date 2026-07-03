import os
from pathlib import Path

root_dir = Path("/home/redafrix/isaac_franka_env_probe")
report_file = root_dir / "DYNAMICVLA_OFFICIAL_ASSETS_ONLY_REPORT.md"

with open(report_file, "w") as f:
    f.write("# DynamicVLA Official Assets Pipeline\n\n")
    f.write("## Cleanup and Preparation\n\n")

    for dir_name in ["downloads", "scenes", "tests"]:
        (root_dir / dir_name).mkdir(exist_ok=True, parents=True)

    for dir_name in ["scenes", "tests"]:
        p = root_dir / dir_name
        if p.is_symlink():
            target = os.readlink(p)
            if "objects" in target:
                f.write(f"Removing invalid {dir_name} symlink to {target}\n")
                p.unlink()
                p.mkdir(exist_ok=True, parents=True)

    f.write("\n## Current Structure\n```\n")
    for dir_name in ["objects", "scenes", "tests", "downloads"]:
        p = root_dir / dir_name
        if p.exists():
            if p.is_symlink():
                f.write(f"{dir_name} -> {os.readlink(p)}\n")
            else:
                f.write(f"{dir_name} (directory)\n")
        else:
            f.write(f"{dir_name} (missing)\n")
    f.write("```\n\n")
