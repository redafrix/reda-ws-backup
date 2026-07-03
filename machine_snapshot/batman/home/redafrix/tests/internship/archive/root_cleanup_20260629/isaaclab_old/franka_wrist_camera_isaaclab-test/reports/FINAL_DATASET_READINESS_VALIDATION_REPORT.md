# Final Dataset Readiness Validation Report

Goal:
Verify fcan03 robustness, test harder object geometries, and determine whether the pipeline is ready for medium-scale dataset collection.

No large collection.
No push.
All episodes require videos and previews.
## Starting repository state
- branch: object-integration-static-assets
- commit: 6a3c181e0912099f530e3e8e415bb4be67a84abf
- status:
 M src/franka_wrist_camera_scene/objects/catalog.py
 M src/franka_wrist_camera_scene/objects/geometry_registry.py
 M src/franka_wrist_camera_scene/scene/clutter.py

6a3c181 (HEAD -> object-integration-static-assets, tag: checkpoint/robustness-verified-20260615) fix(configs): adjust fcan03 grasp depth and target mass to prevent slip in tray placement
e448c6a Fix placement success metadata and validate diverse receptacle tasks
07dab83 (tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
43da87b feat: add geometry-aware deterministic table clutter
4a65eac (backup/object-integration-before-master-20260615_093855, backup/object-integration-before-finalized-master-20260615_104358) Add true receptacle-goal metadata, instruction generation, success mode, and exit watchdog
8cc8080 feat: use receptacle bottom clearance for placement release height
286fa2b fix: make receptacle placement success geometry-aware
6e2cb86 feat: add sampled placement receptacle target
441bebd Implement config-driven receptacle-goal mode for pick-place and add verified configs

## Phase 1 — fcan03 Verification (5 seeds)

| # | Config | Object | Target | Seed | Success | Audit | Steps | Duration |
|---|--------|--------|--------|------|---------|-------|-------|----------|
| 1 | fcan03_verification_seed601.ya | fcan03 | tray04 | 601 | ✅ | ACCEPTED | 2342 | 0.0s |
| 2 | fcan03_verification_seed602.ya | fcan03 | tray04 | 602 | ✅ | ACCEPTED | 2391 | 0.0s |
| 3 | fcan03_verification_seed603.ya | fcan03 | tray04 | 603 | ✅ | ACCEPTED | 2375 | 0.0s |
| 4 | fcan03_verification_seed604.ya | fcan03 | tray04 | 604 | ✅ | ACCEPTED | 2329 | 0.0s |
| 5 | fcan03_verification_seed605.ya | fcan03 | tray04 | 605 | ✅ | ACCEPTED | 2369 | 0.0s |

**Summary**: 5/5 succeeded programmatically, 5/5 accepted physically, 0 errors


## Phase 2 — Hard Object Geometries (6 objects)

| # | Config | Object | Target | Seed | Success | Audit | Steps | Duration |
|---|--------|--------|--------|------|---------|-------|-------|----------|
| 1 | hard_01_beer00_into_bowl01_see | beer00 | bowl01 | 701 | ❌ | FAILED | 2062 | 0.0s |
| 2 | hard_02_box01_into_bowl08_seed | box01 | bowl08 | 702 | ❌ | FAILED | 2486 | 0.0s |
| 3 | hard_03_tangerine06_into_tray0 | tangerine06 | tray04 | 703 | ✅ | ACCEPTED | 2565 | 0.0s |
| 4 | hard_04_egg03_into_box00_seed7 | egg03 | box00 | 704 | ✅ | ACCEPTED | 2495 | 0.0s |
| 5 | hard_05_potato00_into_bowl10_s | potato00 | bowl10 | 705 | ❌ | FAILED | 2388 | 0.0s |
| 6 | hard_06_wbottle01_into_bowl07_ | wbottle01 | bowl07 | 706 | ❌ | FAILED | 2086 | 0.0s |

**Summary**: 2/6 succeeded programmatically, 2/6 accepted physically, 0 errors


## Phase 3 — Clutter Robustness

| # | Config | Object | Target | Seed | Success | Audit | Steps | Duration |
|---|--------|--------|--------|------|---------|-------|-------|----------|
| 1 | clutter_01_avocado_bowl_seed80 | avocado02 | bowl01 | 801 | ✅ | ACCEPTED | 2467 | 0.0s |
| 2 | clutter_02_lime_box_seed802.ya | lime00 | box00 | 802 | ✅ | ACCEPTED | 2442 | 0.0s |

**Summary**: 2/2 succeeded programmatically, 2/2 accepted physically, 0 errors


## Phase 4 — Apple Regression Baseline

| # | Config | Object | Target | Seed | Success | Audit | Steps | Duration |
|---|--------|--------|--------|------|---------|-------|-------|----------|
| 1 | apple_regression_final.yaml | apple01 | None | 123 | ✅ | ACCEPTED | 2536 | 0.0s |

**Summary**: 1/1 succeeded programmatically, 1/1 accepted physically, 0 errors


## Dataset Readiness Decision

- **Decision**: `READY_WITH_EXCLUSIONS`
- **fcan03 Verification**: 5/5 accepted (Supported: `YES`)
- **Hard Objects**: 2/6 accepted
- **Clutter Robustness**: 2/2 accepted
- **Apple Regression**: Accepted: `YES`

### Object Compatibility Profile

- **Supported Objects**: avocado02, onion00, kiwi00, lime00, fcan03, tangerine06, egg03
- **Unsupported Objects**: beer00, box01, potato00, wbottle01

### Audit Explanations

- **hard_01_beer00_into_bowl01_seed701.yaml**: classified as `FAILED` due to `task_failure`. The policy finished but the object did not land within the success tolerance boundary.
- **hard_02_box01_into_bowl08_seed702.yaml**: classified as `FAILED` due to `task_failure`. The policy finished but the object did not land within the success tolerance boundary.
- **hard_05_potato00_into_bowl10_seed705.yaml**: classified as `FAILED` due to `task_failure`. The policy finished but the object did not land within the success tolerance boundary.
- **hard_06_wbottle01_into_bowl07_seed706.yaml**: classified as `FAILED` due to `task_failure`. The policy finished but the object did not land within the success tolerance boundary.

