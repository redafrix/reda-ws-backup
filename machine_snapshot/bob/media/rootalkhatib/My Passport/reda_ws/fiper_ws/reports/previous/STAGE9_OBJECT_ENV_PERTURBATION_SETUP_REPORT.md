# Stage 9 — Object & Env Perturbation Setup Report

**Date**: 2026-05-22  
**Machines**: Sam (PCROBOTUBUNTU05), Bob (PCROBOTUBUNTU02)  
**Verdict**: `OBJECT_ENV_PERTURBATIONS_READY = YES`

---

## 1. Summary

All 6 target LIBERO-PRO perturbation suites now work on **both** Sam and Bob.  
Every task (60 total per machine) passes the full pipeline:  
`register → instantiate → create env → reset → get instruction → SimVLA chunk → step → close`.

---

## 2. PASS/FAIL Table

### Sam (PCROBOTUBUNTU05)

| Suite | Task 0 | Task 1 | Task 2 | Task 3 | Task 4 | Task 5 | Task 6 | Task 7 | Task 8 | Task 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| `libero_spatial_object` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_object_object`  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_goal_object`    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_spatial_env`    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_object_env`     | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_goal_env`       | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Sam total: 60/60 PASS**

### Bob (PCROBOTUBUNTU02)

| Suite | Task 0 | Task 1 | Task 2 | Task 3 | Task 4 | Task 5 | Task 6 | Task 7 | Task 8 | Task 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| `libero_spatial_object` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_object_object`  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_goal_object`    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_spatial_env`    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_object_env`     | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `libero_goal_env`       | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Bob total: 60/60 PASS**

---

## 3. Root Cause & Fix

### Problem

Both machines had a **stale `config.yaml`** for the `libero` package. The config pointed `benchmark_root`, `init_states`, `bddl_files`, and `assets` paths to an old, non-existent site-packages installation:

```
# OLD (broken) — pointed at a path that no longer exists
benchmark_root: /home/redafrix/tests/intern_ship_research/intern_ship_ws/envs/simvla/lib/python3.10/site-packages/libero/libero
init_states:    ...same prefix.../init_files
bddl_files:     ...same prefix.../bddl_files
assets:         ...same prefix.../assets
```

Meanwhile, the actual LIBERO-PRO repository (with all `_object` and `_env` init_files, bddl_files, and assets) was already correctly cloned and populated on both machines — the config just wasn't pointing to it.

### Files Modified

#### Sam

| File | Action |
|---|---|
| `/home/rootalkhatib/.libero/config.yaml` | **Updated** — all paths now point to `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/` |
| `/home/rootalkhatib/test/reda_ws/intern_ship_ws/simvla/config/libero/config.yaml` | **Updated** — same fix (secondary config) |
| Backups | `.bak.20260522123922` suffix on originals |

New Sam config values:
```yaml
benchmark_root: /home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero
bddl_files:     /home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files
init_states:    /home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files
datasets:       /home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/data/libero_datasets
assets:         /home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/assets
```

#### Bob

| File | Action |
|---|---|
| `/home/rootalkhatib/.libero/config.yaml` | **Created** (did not previously exist) |
| `/media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/simvla/config/libero/config.yaml` | **Updated** — all paths now point to Bob's LIBERO-PRO repo |
| `/tmp/bob_site_packages/pydantic_core/` | **Repaired** — Synced missing `__init__.py` and files from Sam to resolve `ImportError` on `pydantic_core` |
| `/tmp/bob_site_packages/scipy.libs/` | **Repaired** — Synced missing shared libraries (e.g. `libgfortran-040039e1.so.5.0.0`) from Sam to resolve SciPy `RuntimeError` |
| `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/scripts/fiper_sweep_bob.sh` | **Updated** — Added `SIMVLA_PATH="/tmp/bob_simvla"` and prepended it to `PYTHONPATH` to resolve `ModuleNotFoundError: No module named 'models'` |
| Backups | `.bak` suffix on secondary config original |

New Bob config values:
```yaml
benchmark_root: /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero
bddl_files:     /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/bddl_files
init_states:    /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/init_files
datasets:       /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/data/libero_datasets
assets:         /media/rootalkhatib/My Passport/reda_ws/intern_ship_ws/assets/repos/LIBERO-PRO/libero/libero/assets
```

---

## 4. Pre-existing Assets Verified (No Generation Needed)

All assets were already present in the LIBERO-PRO repository on both machines:

| Asset Type | Count per Suite | All 6 Suites |
|---|---|---|
| `.pruned_init` files | 10 | 60 total ✅ |
| `bddl_files` | 11 (10 tasks + 1 index) | 66 total ✅ |
| Suite registration in benchmark | All registered | 6/6 ✅ |

No files were copied, symlinked, or generated. The repo already had everything.

---

## 5. Verification Method

Test script: `test_target_suites.py` (deployed to both machines)

For each of the 6 suites × 10 tasks, the script:
1. Checks suite registration in `benchmark.get_benchmark_dict()`
2. Instantiates the benchmark and retrieves the task
3. Creates the environment via `make_env(suite, task_id)`
4. Resets environment to init state via `reset_to_init(env, init_state)`
5. Extracts observation images and proprioception
6. Generates a SimVLA action chunk via `sample_candidate()`
7. Executes the first action via `env.step(first_action)`
8. Closes the environment

Environment variables used for test runs:
- Sam: `PYTHONPATH=.../LIBERO-PRO:$PYTHONPATH MUJOCO_GL=egl PYOPENGL_PLATFORM=egl`
- Bob: `PYTHONPATH=.../site-packages:.../LIBERO-PRO:... MUJOCO_GL=egl PYOPENGL_PLATFORM=egl`

---

## 6. Remaining Blockers

**None.** All 120 task tests (60 per machine) pass.

---

## 7. Final Usable Suite List for Collection

| Suite Name | Perturbation Type | Tasks | Sam | Bob |
|---|---|---|---|---|
| `libero_spatial_object` | Object | 10 | ✅ READY | ✅ READY |
| `libero_object_object`  | Object | 10 | ✅ READY | ✅ READY |
| `libero_goal_object`    | Object | 10 | ✅ READY | ✅ READY |
| `libero_spatial_env`    | Env    | 10 | ✅ READY | ✅ READY |
| `libero_object_env`     | Env    | 10 | ✅ READY | ✅ READY |
| `libero_goal_env`       | Env    | 10 | ✅ READY | ✅ READY |

---

## 8. Final Decision

```
OBJECT_ENV_PERTURBATIONS_READY = YES
```
