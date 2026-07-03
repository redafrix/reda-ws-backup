# Robustness and fcan03 Diagnosis Report

## Starting state
- branch: object-integration-static-assets
- commit: e448c6a22235217b7a3d0970674935f118ac1291
- status:

e448c6a (HEAD -> object-integration-static-assets) Fix placement success metadata and validate diverse receptacle tasks
07dab83 (tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
43da87b feat: add geometry-aware deterministic table clutter
4a65eac (backup/object-integration-before-master-20260615_093855, backup/object-integration-before-finalized-master-20260615_104358) Add true receptacle-goal metadata, instruction generation, success mode, and exit watchdog

## Step 1 — Previous 004 Video Folder Audit

The folder `004_diverse_object_receptacle_matrix` contains **11 MP4 videos** for what was intended as a **6-pair + 1-baseline = 7-run** matrix. The extra videos are from iterative object substitutions during the diversity exploration phase.

### Video-to-Episode Mapping

| # | Video filename | Source dir | Object | Receptacle | Success | Reason |
|---|---------------|-----------|--------|------------|---------|--------|
| 1 | `01_apple01_into_bowl08_SUCCESS` | `pair1_apple_bowl` | apple01 | bowl08 | ✅ | Intended run 1 |
| 2 | `02_avocado02_into_bowl01_SUCCESS` | `pair2_avocado_bowl` | avocado02 | bowl01 | ✅ | Intended run 2 |
| 3 | `03_fcan03_into_tray04_FAIL` | `pair3_can_tray` | fcan03 | tray04 | ❌ | Intended run 3 — can slipped |
| 4a | `04_box01_into_bowl07_FAIL` | (overwritten) | box01 | bowl07 | ❌ | **1st attempt** at slot 4 — box too large |
| 4b | `04_potato00_into_bowl07_FAIL` | (overwritten) | potato00 | bowl07 | ❌ | **2nd attempt** at slot 4 — potato slipped |
| 4c | `04_onion00_into_bowl07_SUCCESS` | `pair4_box_bowl` | onion00 | bowl07 | ✅ | **3rd attempt** at slot 4 — final config |
| 5 | `05_kiwi00_into_bowl10_SUCCESS` | `pair5_kiwi_bowl` | kiwi00 | bowl10 | ✅ | Intended run 5 |
| 6a | `06_beer00_into_box00_FAIL` | (overwritten) | beer00 | box00 | ❌ | **1st attempt** at slot 6 — beer can too tall |
| 6b | `06_egg03_into_box00_FAIL` | (overwritten) | egg03 | box00 | ❌ | **2nd attempt** at slot 6 — egg too fragile |
| 6c | `06_lime00_into_box00_SUCCESS` | `pair6_beer_box` | lime00 | box00 | ✅ | **3rd attempt** at slot 6 — final config |
| 7 | `07_apple01_baseline_SUCCESS` | (inline) | apple01 | — | ✅ | Apple regression baseline |

### Explanation

Slots 4 and 6 were iteratively retried with different objects until a successful pair was found. The config YAML files (`pair4_box_bowl.yaml`, `pair6_beer_box.yaml`) were updated in-place each time, and the output directories were overwritten (`rm -rf`). However, the **video files in the 004 folder** were never deleted, so intermediate failed attempts accumulated alongside the final successful ones.

**Result**: 6 intended pairs + 4 intermediate retries + 1 apple baseline = **11 videos**. No data corruption. All videos are genuine episode renders from distinct Isaac Sim runs.

## Phase 1 — Robustness Matrix (5 pairs × 3 seeds)

| # | Config | Object | Target | Seed | Success | Metric | Steps | Duration |
|---|--------|--------|--------|------|---------|--------|-------|----------|
| 1 | robust_01_apple01_into_bowl08_ | apple01 | bowl08 | 301 | ✅ | inside_receptacle_center_ | 2540 | 99.7s |
| 2 | robust_02_apple01_into_bowl08_ | apple01 | bowl08 | 302 | ✅ | inside_receptacle_center_ | 2437 | 94.1s |
| 3 | robust_03_apple01_into_bowl08_ | apple01 | bowl08 | 303 | ✅ | inside_receptacle_center_ | 2392 | 95.7s |
| 4 | robust_04_avocado02_into_bowl0 | avocado02 | bowl01 | 301 | ✅ | inside_receptacle_center_ | 2531 | 114.7s |
| 5 | robust_05_avocado02_into_bowl0 | avocado02 | bowl01 | 302 | ✅ | inside_receptacle_center_ | 2429 | 82.7s |
| 6 | robust_06_avocado02_into_bowl0 | avocado02 | bowl01 | 303 | ✅ | inside_receptacle_center_ | 2382 | 110.9s |
| 7 | robust_07_onion00_into_bowl07_ | onion00 | bowl07 | 301 | ✅ | inside_receptacle_center_ | 2590 | 97.6s |
| 8 | robust_08_onion00_into_bowl07_ | onion00 | bowl07 | 302 | ✅ | inside_receptacle_center_ | 2488 | 86.0s |
| 9 | robust_09_onion00_into_bowl07_ | onion00 | bowl07 | 303 | ✅ | inside_receptacle_center_ | 2443 | 90.0s |
| 10 | robust_10_kiwi00_into_bowl10_s | kiwi00 | bowl10 | 301 | ✅ | inside_receptacle_center_ | 2608 | 105.6s |
| 11 | robust_11_kiwi00_into_bowl10_s | kiwi00 | bowl10 | 302 | ✅ | inside_receptacle_center_ | 2506 | 83.8s |
| 12 | robust_12_kiwi00_into_bowl10_s | kiwi00 | bowl10 | 303 | ✅ | inside_receptacle_center_ | 2460 | 88.1s |
| 13 | robust_13_lime00_into_box00_se | lime00 | box00 | 301 | ✅ | inside_receptacle_center_ | 2523 | 87.6s |
| 14 | robust_14_lime00_into_box00_se | lime00 | box00 | 302 | ✅ | inside_receptacle_center_ | 2422 | 92.1s |
| 15 | robust_15_lime00_into_box00_se | lime00 | box00 | 303 | ✅ | inside_receptacle_center_ | 2375 | 95.9s |

**Summary**: 15/15 succeeded, 0 failed, 0 errors


## Phase 2 — fcan03 Diagnosis Variants

| # | Config | Object | Target | Seed | Success | Metric | Steps | Duration |
|---|--------|--------|--------|------|---------|--------|-------|----------|
| 1 | fcan03_diag_A_default.yaml | fcan03 | tray04 | 401 | ❌ | on_receptacle_center | 2398 | 93.7s |
| 2 | fcan03_diag_B_deeper_grasp.yam | fcan03 | tray04 | 401 | ❌ | on_receptacle_center | 2465 | 96.1s |
| 3 | fcan03_diag_C_moderate_depth.y | fcan03 | tray04 | 401 | ❌ | on_receptacle_center | 2419 | 93.2s |
| 4 | fcan03_diag_D_mass_override.ya | fcan03 | tray04 | 401 | ✅ | on_receptacle_center | 2461 | 128.0s |

**Summary**: 1/4 succeeded, 3 failed, 0 errors

### fcan03 Diagnosis Analysis

**fcan03_diag_A_default.yaml**: success=False

**fcan03_diag_B_deeper_grasp.yaml**: success=False

**fcan03_diag_C_moderate_depth.yaml**: success=False

**fcan03_diag_D_mass_override.yaml**: success=True

**Recommended fix**: Use configuration from `fcan03_diag_D_mass_override.yaml`


## Phase 3 — Clutter Robustness

| # | Config | Object | Target | Seed | Success | Metric | Steps | Duration |
|---|--------|--------|--------|------|---------|--------|-------|----------|
| 1 | clutter_apple_bowl.yaml | apple01 | bowl08 | 501 | ✅ | inside_receptacle_center_ | 2487 | 140.3s |
| 2 | clutter_lime_box.yaml | lime00 | box00 | 502 | ✅ | inside_receptacle_center_ | 2497 | 110.8s |

**Summary**: 2/2 succeeded, 0 failed, 0 errors


## Phase 4 — Apple Regression Baseline

| # | Config | Object | Target | Seed | Success | Metric | Steps | Duration |
|---|--------|--------|--------|------|---------|--------|-------|----------|
| 1 | apple_regression_final.yaml | apple01 | None | 123 | ✅ | target_area_center | 2536 | 92.4s |

**Summary**: 1/1 succeeded, 0 failed, 0 errors


## Final Summary

- **Total episodes**: 22
- **Successful**: 19
- **Failed**: 3
- **Errors**: 0
- **Video folder**: `/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/005_robustness_and_fcan03`
- **Gallery**: `/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/005_robustness_and_fcan03/index.html`
- **Completed**: 2026-06-15T15:03:30.293843

### Robustness Success Rate by Pair

| Pair | Seed 301 | Seed 302 | Seed 303 | Rate |
|------|----------|----------|----------|------|
| apple01→bowl08 | ✅ | ✅ | ✅ | 3/3 |
| avocado02→bowl01 | ✅ | ✅ | ✅ | 3/3 |
| onion00→bowl07 | ✅ | ✅ | ✅ | 3/3 |
| kiwi00→bowl10 | ✅ | ✅ | ✅ | 3/3 |
| lime00→box00 | ✅ | ✅ | ✅ | 3/3 |

