#!/usr/bin/env python3
"""Install LIBERO-PRO libero_goal_object_ood assets into an existing LIBERO repo.

Usage:
  python scripts/install_libero_goal_object_ood.py --libero-root /path/to/LIBERO-PRO/libero/libero

The target --libero-root must contain bddl_files/, init_files/, and benchmark/.
"""
import argparse
import json
import shutil
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
TASK_MAP_SNIPPET = '''
    "libero_goal_object_ood": [
            "open_the_middle_drawer_of_the_cabinet(yellow_cabinet)",
            "open_the_top_drawer_and_put_the_bowl_inside(yellow_bowl)",
            "open_the_top_drawer_and_put_the_bowl_inside(yellow_cabinet)",
            "push_the_plate_to_the_front_of_the_stove(yellow_plate)",
            "push_the_plate_to_the_front_of_the_stove(yellow_stove)",
            "put_the_bowl_on_the_plate(yellow_bowl)",
            "put_the_bowl_on_the_plate(yellow_plate)",
            "put_the_bowl_on_the_stove(yellow_bowl)",
            "put_the_bowl_on_the_stove(yellow_stove)",
            "put_the_bowl_on_top_of_the_cabinet(yellow_bowl)",
            "put_the_bowl_on_top_of_the_cabinet(yellow_cabinet)",
            "put_the_cream_cheese_in_the_bowl(red_cream_cheese)",
            "put_the_cream_cheese_in_the_bowl(yellow_bowl)",
            "put_the_wine_bottle_on_the_rack(brown_rack)",
            "put_the_wine_bottle_on_the_rack(green_bottle)",
            "put_the_wine_bottle_on_top_of_the_cabinet(green_bottle)",
            "put_the_wine_bottle_on_top_of_the_cabinet(yellow_cabinet)",
            "turn_on_the_stove(yellow_stove)",
        ],
'''
BENCHMARK_CLASS_SNIPPET = '''
@register_benchmark
class LIBERO_GOAL_OBJECT_OOD(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_goal_object_ood"
        self._make_benchmark()

'''


def copytree_replace(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def maybe_patch_registry(libero_root: Path, dry_run: bool):
    bench_dir = libero_root / "benchmark"
    init_py = bench_dir / "__init__.py"
    task_map = bench_dir / "libero_suite_task_map.py"
    patch_notes = []

    if task_map.exists():
        text = task_map.read_text()
        if '"libero_goal_object_ood"' not in text and "'libero_goal_object_ood'" not in text:
            patch_notes.append("libero_suite_task_map.py missing libero_goal_object_ood")
            if not dry_run:
                backup = task_map.with_suffix(task_map.suffix + ".bak_before_goal_object_ood")
                if not backup.exists():
                    shutil.copy2(task_map, backup)
                idx = text.rfind("}")
                if idx == -1:
                    patch_notes.append("could not auto-patch libero_suite_task_map.py: no closing dict brace found")
                else:
                    text = text[:idx] + TASK_MAP_SNIPPET + text[idx:]
                    task_map.write_text(text)
    else:
        patch_notes.append("benchmark/libero_suite_task_map.py not found")

    if init_py.exists():
        text = init_py.read_text()
        if "LIBERO_GOAL_OBJECT_OOD" not in text:
            patch_notes.append("benchmark/__init__.py missing LIBERO_GOAL_OBJECT_OOD class")
            if not dry_run:
                backup = init_py.with_suffix(init_py.suffix + ".bak_before_goal_object_ood")
                if not backup.exists():
                    shutil.copy2(init_py, backup)
                text = text.rstrip() + "\n\n" + BENCHMARK_CLASS_SNIPPET
                # Also add to libero_suites list only if the literal does not exist anywhere.
                # The class registration is usually sufficient for get_benchmark_dict().
                init_py.write_text(text)
    else:
        patch_notes.append("benchmark/__init__.py not found")

    return patch_notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--libero-root", required=True, help="Path to LIBERO-PRO/libero/libero")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-registry-patch", action="store_true")
    args = ap.parse_args()

    libero_root = Path(args.libero_root).expanduser().resolve()
    required = [libero_root / "bddl_files", libero_root / "init_files", libero_root / "benchmark"]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise SystemExit(f"Invalid --libero-root {libero_root}; missing: {missing}")

    src_bddl = PACKAGE_ROOT / "bddl_files" / "libero_goal_object_ood_temp"
    src_init = PACKAGE_ROOT / "init_files" / "libero_goal_object_ood"
    if not src_bddl.exists() or not src_init.exists():
        raise SystemExit("Package is incomplete: missing bddl_files/libero_goal_object_ood_temp or init_files/libero_goal_object_ood")

    targets = [
        (src_bddl, libero_root / "bddl_files" / "libero_goal_object_ood_temp"),
        # Mirror BDDL to the registry folder name too. This avoids the Bob-specific alias issue.
        (src_bddl, libero_root / "bddl_files" / "libero_goal_object_ood"),
        (src_init, libero_root / "init_files" / "libero_goal_object_ood"),
    ]
    for src, dst in targets:
        print(f"INSTALL {src} -> {dst}")
        if not args.dry_run:
            copytree_replace(src, dst)

    patch_notes = []
    if not args.no_registry_patch:
        patch_notes = maybe_patch_registry(libero_root, args.dry_run)

    manifest = json.loads((PACKAGE_ROOT / "metadata" / "task_manifest.json").read_text())
    print("\nInstalled suite:", manifest["suite"])
    print("Task count:", manifest["task_count"])
    for task in manifest["tasks"]:
        print(f"  {task['task_id']:02d}: {task['language']}")
    if patch_notes:
        print("\nRegistry patch notes:")
        for note in patch_notes:
            print(" -", note)
    print("\nNext: run scripts/verify_libero_goal_object_ood.py --libero-root", libero_root)


if __name__ == "__main__":
    main()
