# LIBERO-PRO Goal-Object OOD Setup Package

This zip installs the LIBERO-PRO `libero_goal_object_ood` benchmark assets.
It is intended for a machine that already has LIBERO / LIBERO-PRO installed but is missing the goal-object OOD suite files.

## What This Package Contains

- `bddl_files/libero_goal_object_ood_temp/`
  - 18 BDDL files for the goal-object OOD task definitions.
- `init_files/libero_goal_object_ood/`
  - 18 matching `.pruned_init` files.
- `metadata/task_manifest.json`
  - task ids, language strings, BDDL filenames, and init filenames.
- `scripts/install_libero_goal_object_ood.py`
  - copies the assets into a target LIBERO-PRO checkout.
- `scripts/verify_libero_goal_object_ood.py`
  - verifies file presence and optionally verifies the Python benchmark registry.
- `scripts/libero_goal_object_ood_runtime_alias.py`
  - helper for codebases where the benchmark registry expects `libero_goal_object_ood` but BDDL files live under `libero_goal_object_ood_temp`.

## Important Naming Detail

On our Bob workspace, the OOD assets are split like this:

- BDDL files are under:
  - `libero/libero/bddl_files/libero_goal_object_ood_temp`
- init states are under:
  - `libero/libero/init_files/libero_goal_object_ood`

Some LIBERO runners expect BDDL under `bddl_files/libero_goal_object_ood` instead.
To make setup easy, the installer copies the BDDL files to both locations:

- `bddl_files/libero_goal_object_ood_temp`
- `bddl_files/libero_goal_object_ood`

That makes both styles work.

## Task List

Suite: `libero_goal_object_ood`

| Task ID | Language |
|---:|---|
| 0 | open the middle drawer of the cabinet(yellow cabinet) |
| 1 | open the top drawer and put the bowl inside(yellow bowl) |
| 2 | open the top drawer and put the bowl inside(yellow cabinet) |
| 3 | push the plate to the front of the stove(yellow plate) |
| 4 | push the plate to the front of the stove(yellow stove) |
| 5 | put the bowl on the plate(yellow bowl) |
| 6 | put the bowl on the plate(yellow plate) |
| 7 | put the bowl on the stove(yellow bowl) |
| 8 | put the bowl on the stove(yellow stove) |
| 9 | put the bowl on top of the cabinet(yellow bowl) |
| 10 | put the bowl on top of the cabinet(yellow cabinet) |
| 11 | put the cream cheese in the bowl(red cream cheese) |
| 12 | put the cream cheese in the bowl(yellow bowl) |
| 13 | put the wine bottle on the rack(brown rack) |
| 14 | put the wine bottle on the rack(green bottle) |
| 15 | put the wine bottle on top of the cabinet(green bottle) |
| 16 | put the wine bottle on top of the cabinet(yellow cabinet) |
| 17 | turn on the stove(yellow stove) |

## Install Instructions

On the other PC, unzip this package somewhere, then run:

```bash
cd libero_goal_object_ood_setup_package_20260618
python3 scripts/install_libero_goal_object_ood.py --libero-root /ABS/PATH/TO/LIBERO-PRO/libero/libero
```

Example target root layouts that are valid:

```text
/ABS/PATH/TO/LIBERO-PRO/libero/libero/bddl_files
/ABS/PATH/TO/LIBERO-PRO/libero/libero/init_files
/ABS/PATH/TO/LIBERO-PRO/libero/libero/benchmark
```

The installer will:

1. copy BDDL files to `bddl_files/libero_goal_object_ood_temp`;
2. mirror BDDL files to `bddl_files/libero_goal_object_ood` for compatibility;
3. copy init states to `init_files/libero_goal_object_ood`;
4. patch the benchmark registry only if `libero_goal_object_ood` is missing.

Before changing anything, you can preview:

```bash
python3 scripts/install_libero_goal_object_ood.py --libero-root /ABS/PATH/TO/LIBERO-PRO/libero/libero --dry-run
```

## Verify Install

Basic asset verification:

```bash
python3 scripts/verify_libero_goal_object_ood.py --libero-root /ABS/PATH/TO/LIBERO-PRO/libero/libero
```

Optional import/registry verification:

```bash
python3 scripts/verify_libero_goal_object_ood.py --libero-root /ABS/PATH/TO/LIBERO-PRO/libero/libero --import-check
```

The import check should show:

```text
Import check task count: 18
Import check: PASS
```

## If Your Runner Still Says BDDL Does Not Exist

If your runner errors with something like:

```text
.../bddl_files/libero_goal_object_ood/open_the_middle_drawer_of_the_cabinet(yellow_cabinet).bddl does not exist
```

then the mirrored folder should already fix it. Confirm:

```bash
ls /ABS/PATH/TO/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_ood
```

If your runner instead expects `libero_goal_object_ood_temp`, confirm:

```bash
ls /ABS/PATH/TO/LIBERO-PRO/libero/libero/bddl_files/libero_goal_object_ood_temp
```

Both should exist after install.

## Runtime Alias Helper

If you do not want to mirror BDDL folders, or if your local benchmark registry is immutable, use:

```python
from scripts.libero_goal_object_ood_runtime_alias import alias_goal_object_ood_task

task = task_suite.get_task(task_id)
task = alias_goal_object_ood_task(task)
env, task_description = get_libero_env(task, model_family, resolution=256)
```

This changes only the task object used by the runner, not the LIBERO repo.

## Notes

- This package does not include the whole LIBERO-PRO repo.
- It assumes standard LIBERO-PRO object/assets/textures are already installed.
- It only adds the goal-object OOD BDDL/init assets and registry compatibility helpers.
- If your installed LIBERO-PRO already contains `libero_goal_object_ood`, the installer is still safe: it replaces only the two OOD asset folders and leaves other suites alone.
