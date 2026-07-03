import re
from pathlib import Path

root_dir = Path("/home/redafrix/isaac_franka_env_probe")
report_file = root_dir / "DYNAMICVLA_OFFICIAL_ASSETS_ONLY_REPORT.md"
readme_path = root_dir / "dynamic-vla" / "README.md"

links = []
if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "download" in line.lower() or "dataset" in line.lower():
            if "http" in line:
                links.append(line.strip())
        elif "baidu" in line.lower() or "drive.google" in line.lower():
            links.append(line.strip())

with open(report_file, "a") as f:
    f.write("## Official Asset Links\n")
    f.write("Extracted from README.md:\n```\n")
    for link in links:
        f.write(link + "\n")
    f.write("```\n")

print("\n".join(links))
