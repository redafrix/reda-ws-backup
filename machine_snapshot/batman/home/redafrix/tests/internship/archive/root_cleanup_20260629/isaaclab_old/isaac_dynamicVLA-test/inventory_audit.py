import os
import subprocess
from pathlib import Path

root = Path("/home/redafrix/isaac_franka_env_probe")
report_path = root / "DYNAMICVLA_ASSET_INVENTORY_REPORT.md"
isaaclab_path = root / "IsaacLab"
repo_path = root / "dynamic-vla"

def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, shell=True, cwd=str(cwd) if cwd else str(root), capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error running command: {e}"

with open(report_path, "w") as f:
    f.write("# DynamicVLA Asset Inventory Report\n\n")
    f.write("This is a read-only audit. No downloads, extraction, deletion, symlink creation, simulation, or patching were performed.\n\n")
    
    f.write("## System / Disk\n")
    f.write(run_cmd("date; pwd; df -h ."))
    f.write("\n\n")

    f.write("## Top-level workspace\n")
    f.write(run_cmd("ls -lah"))
    f.write("\n\n")

    f.write("## Important paths and symlinks\n")
    paths = ["objects", "scenes", "tests", "test-envs.txt", "downloads", "assets_staging", "assets_staging_official", "datasets", "dynamic-vla", "IsaacLab", "dynamicvla_logs"]
    for p in paths:
        path_obj = root / p
        f.write(f"### {p}\n")
        if path_obj.exists() or path_obj.is_symlink():
            f.write(run_cmd(f"ls -lahd {p}"))
            if path_obj.is_symlink():
                f.write(f"SYMLINK_TARGET={path_obj.resolve()}\n")
        else:
            f.write("MISSING\n")
        f.write("\n")

    f.write("## Downloads inventory\n")
    if (root / "downloads").is_dir():
        f.write(run_cmd("find downloads -maxdepth 2 -type f -printf '%p | %s bytes\n' | sort"))
        f.write("\n\n## Downloads file types\n")
        f.write(run_cmd("find downloads -maxdepth 2 -type f -print0 | xargs -0 -r file"))
    else:
        f.write("downloads/ MISSING\n")
    f.write("\n")

    f.write("## Downloads HTML/CAPTCHA check\n")
    d = root / "downloads"
    if d.exists():
        for p in sorted(d.rglob("*")):
            if not p.is_file(): continue
            try:
                data = p.read_bytes()[:4096].lower()
                is_html = b"<html" in data
                is_captcha = b"captcha" in data or b"recaptcha" in data
                f.write(f"{p} size={p.stat().st_size} html={is_html} captcha={is_captcha}\n")
            except Exception as e:
                f.write(f"{p} ERROR {e}\n")
    else:
        f.write("downloads missing\n")
    f.write("\n")

    f.write("## Staging folders\n")
    for d_name in ["assets_staging", "assets_staging_official"]:
        f.write(f"### {d_name}\n")
        d_path = root / d_name
        if d_path.is_dir():
            f.write(run_cmd(f"du -sh {d_name}"))
            f.write(run_cmd(f"find {d_name} -maxdepth 4 -type d | sort | head -200"))
            f.write("\nKey files:\n")
            f.write(run_cmd(f"find {d_name} -maxdepth 7 -type f \\( -name '*.usd' -o -name '*.usda' -o -name '*.json' -o -name 'metadata.json' -o -name 'test-envs.txt' -o -name '*.png' -o -name '*.jpg' \\) | head -300"))
        else:
            f.write("MISSING\n")
        f.write("\n")

    f.write("## Objects validity check\n")
    if (root / "objects").exists():
        f.write("objects exists\n")
        if (root / "objects").is_symlink():
            f.write(f"objects symlink target: {(root / 'objects').resolve()}\n")
        f.write(run_cmd("du -sh objects 2>/dev/null"))
        f.write("USD count:\n")
        f.write(run_cmd("find objects -type f \\( -name '*.usd' -o -name '*.usda' \\) 2>/dev/null | wc -l"))
        f.write("metadata files:\n")
        f.write(run_cmd("find objects -type f -name 'metadata.json' 2>/dev/null"))
        f.write("object sample:\n")
        f.write(run_cmd("find objects -maxdepth 4 -type f \\( -name '*.usd' -o -name '*.usda' -o -name 'metadata.json' \\) 2>/dev/null | head -80"))
    else:
        f.write("objects MISSING\n")
    f.write("\n")

    f.write("## Scenes validity check\n")
    if (root / "scenes").exists():
        f.write("scenes exists\n")
        if (root / "scenes").is_symlink():
            f.write(f"scenes symlink target: {(root / 'scenes').resolve()}\n")
        f.write(run_cmd("du -sh scenes 2>/dev/null"))
        f.write("Scene USD count:\n")
        f.write(run_cmd("find scenes -type f \\( -name '*.usd' -o -name '*.usda' \\) 2>/dev/null | wc -l"))
        f.write("Texture count:\n")
        f.write(run_cmd("find scenes -type f \\( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' \\) 2>/dev/null | wc -l"))
        f.write("scene sample:\n")
        f.write(run_cmd("find scenes -maxdepth 4 -type f \\( -name '*.usd' -o -name '*.usda' -o -name '*.png' -o -name '*.jpg' \\) 2>/dev/null | head -100"))
    else:
        f.write("scenes MISSING\n")
    f.write("\n")

    f.write("## Scene USD structural check for /house/furniture/Table\n")
    scenes_root = root / "scenes"
    if not scenes_root.exists():
        f.write("scenes missing\n")
    else:
        # We'll run a separate subprocess turn for the Isaac Lab check to avoid nesting logic too deeply
        f.write("Check skipped in this turn - running in next step.\n")
    f.write("\n")

    f.write("## Tests validity check\n")
    if (root / "tests").exists():
        f.write("tests exists\n")
        if (root / "tests").is_symlink():
            f.write(f"tests symlink target: {(root / 'tests').resolve()}\n")
        f.write(run_cmd("du -sh tests 2>/dev/null"))
        f.write("JSON count:\n")
        f.write(run_cmd("find tests -type f -name '*.json' 2>/dev/null | wc -l"))
        f.write("tests sample:\n")
        f.write(run_cmd("find tests -maxdepth 4 -type f -name '*.json' 2>/dev/null | head -100"))
    else:
        f.write("tests MISSING\n")
    f.write("\n")

    f.write("## test-envs.txt validity check\n")
    te_path = root / "test-envs.txt"
    if te_path.exists():
        f.write("test-envs.txt exists\n")
        if te_path.is_symlink():
            f.write(f"test-envs.txt symlink target: {te_path.resolve()}\n")
        f.write(run_cmd(f"ls -lh test-envs.txt"))
        f.write("line count: ")
        f.write(run_cmd(f"wc -l < test-envs.txt"))
        f.write("first 50 lines:\n")
        f.write(run_cmd(f"head -50 test-envs.txt"))
    else:
        f.write("test-envs.txt MISSING\n")
    f.write("\n")

    f.write("## DynamicVLA repo status\n")
    f.write(run_cmd("git remote -v; git rev-parse HEAD; git status --short", cwd=repo_path))
    f.write("\n## simulate.py args\n")
    f.write(run_cmd("grep -nE 'add_argument|--task|--robot|--enable_cameras|--debug|--save|n_simulations|scene|object|test|env' simulations/simulate.py | head -250", cwd=repo_path))
    f.write("\n## README asset references\n")
    f.write(run_cmd("grep -nA60 -B10 -Ei 'DOM Testing Set|DOM 3D Objects|DOM 3D Scenes|Prepare scenes|Simulated Dataset Generation|test-envs|objects|scenes|tests' README.md | head -250", cwd=repo_path))
    f.write("\n")

    # Final Summary Logic
    objects_usd = int(run_cmd("find objects -type f \\( -name '*.usd' -o -name '*.usda' \\) 2>/dev/null | wc -l").strip() or 0)
    scenes_usd = int(run_cmd("find scenes -type f \\( -name '*.usd' -o -name '*.usda' \\) 2>/dev/null | wc -l").strip() or 0)
    tests_json = int(run_cmd("find tests -type f -name '*.json' 2>/dev/null | wc -l").strip() or 0)
    te_exists = te_path.exists() and te_path.stat().st_size > 0
    
    f.write("# FINAL INVENTORY VERDICT\n\n")
    f.write("| Item | Status | Evidence |\n")
    f.write("|---|---|---|\n")
    f.write(f"| objects/ | {'OK' if objects_usd > 0 else 'MISSING/BAD'} | {objects_usd} USD/USDA files |\n")
    f.write(f"| scenes/ | {'OK' if scenes_usd > 0 else 'MISSING/BAD'} | {scenes_usd} USD/USDA files |\n")
    f.write(f"| tests/ | {'OK' if tests_json > 0 else 'MISSING/BAD'} | {tests_json} JSON files |\n")
    f.write(f"| test-envs.txt | {'OK' if te_exists else 'MISSING/BAD'} | exists={te_path.exists()}, size={te_path.stat().st_size if te_path.exists() else 0} |\n\n")
    
    ready = objects_usd > 0 and scenes_usd > 0 and tests_json > 0 and te_exists
    f.write("## Can we run official DynamicVLA automated collection now?\n")
    f.write("YES\n" if ready else "NO\n")
    f.write("\n")
    if not ready:
        f.write("## Missing exactly:\n")
        if objects_usd <= 0: f.write("- official objects/ with USD files\n")
        if scenes_usd <= 0: f.write("- official scenes/ with scene USD files\n")
        if tests_json <= 0: f.write("- official tests/ with JSON config files\n")
        if not te_exists: f.write("- official test-envs.txt\n")
    f.write("\n## Recommended next action\n")
    if ready:
        f.write("Run simulate.py with --task place --robot franka --enable_cameras --save --debug -n 1\n")
    else:
        f.write("Download/extract only the missing official asset(s), not the full 299GB DOM training set.\n")
