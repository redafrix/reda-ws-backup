#!/usr/bin/env python3
"""Verify that LIBERO-PRO libero_goal_object_ood assets are installed."""
import argparse
import json
import os
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--libero-root", required=True, help="Path to LIBERO-PRO/libero/libero")
    ap.add_argument("--import-check", action="store_true", help="Also import libero and query benchmark registry")
    args = ap.parse_args()

    libero_root = Path(args.libero_root).expanduser().resolve()
    manifest = json.loads((PACKAGE_ROOT / "metadata" / "task_manifest.json").read_text())
    bddl_dirs = [libero_root / "bddl_files" / "libero_goal_object_ood", libero_root / "bddl_files" / "libero_goal_object_ood_temp"]
    init_dir = libero_root / "init_files" / "libero_goal_object_ood"

    errors = []
    for task in manifest["tasks"]:
        bddl_ok = any((d / task["bddl_file"]).exists() for d in bddl_dirs)
        init_ok = (init_dir / task["init_states_file"]).exists()
        if not bddl_ok:
            errors.append(f"missing BDDL for task {task['task_id']}: {task['bddl_file']}")
        if not init_ok:
            errors.append(f"missing init for task {task['task_id']}: {task['init_states_file']}")

    print(f"Suite: {manifest['suite']}")
    print(f"Expected tasks: {manifest['task_count']}")
    print(f"BDDL dirs checked: {[str(d) for d in bddl_dirs]}")
    print(f"Init dir checked: {init_dir}")
    if errors:
        print("FAILED asset verification:")
        for err in errors:
            print(" -", err)
        raise SystemExit(1)
    print("Asset verification: PASS")

    if args.import_check:
        repo_root = libero_root.parents[1] if libero_root.name == "libero" else libero_root.parent
        sys.path.insert(0, str(repo_root))
        os.environ.setdefault("LIBERO_CONFIG_PATH", str(libero_root.parent / "configs"))
        from libero.libero import benchmark
        bd = benchmark.get_benchmark_dict()
        if "libero_goal_object_ood" not in bd:
            print("Import check: FAIL - benchmark registry lacks libero_goal_object_ood")
            raise SystemExit(2)
        ts = bd["libero_goal_object_ood"]()
        print("Import check task count:", ts.get_num_tasks())
        for i in range(ts.get_num_tasks()):
            task = ts.get_task(i)
            print(f"  {i:02d}: {task.language} | folder={task.problem_folder} | bddl={task.bddl_file}")
        if ts.get_num_tasks() != manifest["task_count"]:
            raise SystemExit("Import check task count mismatch")
        print("Import check: PASS")


if __name__ == "__main__":
    main()
