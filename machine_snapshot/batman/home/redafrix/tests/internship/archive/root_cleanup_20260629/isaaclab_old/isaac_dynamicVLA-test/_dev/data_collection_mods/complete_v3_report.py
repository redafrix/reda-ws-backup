import subprocess
import os
import re
from pathlib import Path

ROOT = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
DEV = ROOT / "_dev/data_collection_mods"
EXP = DEV / "experiments/static_v3_true_stable_physics_gate"
REPORT_PATH = DEV / "reports/STATIC_COLLECTION_V3_TRUE_STABLE_PHYSICS_GATE_REPORT.md"
TRANSLATE_LOG_PATH = EXP / "logs/static_v3_translate.log"

# Read current report
report_content = REPORT_PATH.read_text()

# We want to make sure the report content only contains lines up to where Step 5 finished (i.e. PHYSICS_GATE_REASONS [])
# Let's find "PHYSICS_GATE_REASONS" and truncate everything after its corresponding block.
lines = report_content.splitlines()
trunc_idx = -1
for i, line in enumerate(lines):
    if "PHYSICS_GATE_REASONS" in line:
        trunc_idx = i + 1

if trunc_idx != -1:
    lines = lines[:trunc_idx + 1]

new_report = "\n".join(lines) + "\n"

# Step 6: Translate Result
new_report += "\n## Static V3 translate result\n"
new_report += "exit_status=0\n"
new_report += f"log={TRANSLATE_LOG_PATH}\n"

# Grep from translate log
translate_log_content = TRANSLATE_LOG_PATH.read_text()
grep_lines = []
pattern = re.compile(r"Recovering test environment|Saving|SUCCESS|FAIL|Object Occluded|Cam Occluded|Container Occluded|Traceback|TypeError|Exception|Error|failed|FileNotFound|CUDA out of memory|out of memory|omni.kvdb|lock", re.IGNORECASE)
for line in translate_log_content.splitlines():
    if pattern.search(line):
        grep_lines.append(line)

new_report += "\n".join(grep_lines[-400:]) + "\n"

# Step 7: Make multicam videos
new_report += "\n## Multicam video generation logs\n"
raw_h5s = sorted((EXP / "raw").glob("*.h5"))
tr_h5s = sorted((EXP / "translated").glob("*.h5"))
all_h5s = raw_h5s + tr_h5s

for h5 in all_h5s:
    base = h5.stem
    out_video = EXP / "videos" / f"{base}_multicam.mp4"
    cmd = [
        str(ROOT / "IsaacLab/isaaclab.sh"),
        "-p",
        str(ROOT / "tools/make_multicam_video.py"),
        "--input", str(h5),
        "--output", str(out_video),
        "--fps", "20"
    ]
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    new_report += f"\n### Video generation for {h5.name}\n"
    new_report += f"Command: {' '.join(cmd)}\n"
    new_report += f"Stdout:\n{res.stdout}\n"
    if res.stderr:
        # Filter out noisy warnings from output/stderr to keep report clean
        filtered_stderr = "\n".join([l for l in res.stderr.splitlines() if "[Warning]" not in l and "Warning:" not in l and "[DEBUG]" not in l])
        if filtered_stderr.strip():
            new_report += f"Stderr:\n{filtered_stderr}\n"

# Step 8: Save final patch/report
final_summary = f"""
# FINAL STATIC V3 SUMMARY
- static repo: {DEV}/repos/dynamic-vla-static-v1
- experiment: {EXP}
- raw H5 count: {len(list((EXP / 'raw').glob('*.h5')))}
- raw JSON count: {len(list((EXP / 'raw').glob('*.json')))}
- raw MP4 count: {len(list((EXP / 'raw').glob('*.mp4')))}
- translated H5 count: {len(list((EXP / 'translated').glob('*.h5')))}
- translated JSON count: {len(list((EXP / 'translated').glob('*.json')))}
- videos count: {len(list((EXP / 'videos').glob('*.mp4')))}

## Raw files
"""

for f in sorted((EXP / "raw").iterdir()):
    if f.is_file():
        final_summary += f"{f} | {f.stat().st_size} bytes\n"

final_summary += "\n## Translated files\n"
for f in sorted((EXP / "translated").iterdir()):
    if f.is_file():
        final_summary += f"{f} | {f.stat().st_size} bytes\n"

final_summary += "\n## Videos\n"
for f in sorted((EXP / "videos").iterdir()):
    if f.is_file():
        final_summary += f"{f} | {f.stat().st_size} bytes\n"

final_summary += f"\n## Patch path\n{DEV}/patches/static_true_stable_physics_gate_v3_simulate.patch\n\n## Disk\n"

df_res = subprocess.run(["df", "-h", str(ROOT)], capture_output=True, text=True)
final_summary += df_res.stdout

new_report += final_summary

# Write new report
REPORT_PATH.write_text(new_report)
print("Report generation complete!")
