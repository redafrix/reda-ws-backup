# Finalize Integrated Working Branch Report

Goal:
Move the validated upstream integration onto object-integration-static-assets without losing the old branch state.

No push.
No history rewrite.
Keep integration and backup branches.
## Initial state

### current branch
integration/master-sync-20260615_093855

### HEAD
07dab834f1d5db2f56647c486ee00e75a17fbdfb

### status

### relevant branches
  backup/object-integration-before-master-20260615_093855
* integration/master-sync-20260615_093855
  object-integration-static-assets

### integration commit
07dab83 Merge upstream master and preserve local Isaac 4.5 integration

## Backup created
- old_working_sha: 4a65eac8b2acc1642478efd03b216b0a0143960c
- backup_branch: backup/object-integration-before-finalized-master-20260615_104358
Fast-forward is valid.

## Branch finalized
- branch: object-integration-static-assets
- final_sha: 07dab834f1d5db2f56647c486ee00e75a17fbdfb

*   07dab83 (HEAD -> object-integration-static-assets, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
|\  
| * 74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
| * 43da87b feat: add geometry-aware deterministic table clutter
| * 8cc8080 feat: use receptacle bottom clearance for placement release height
| * 286fa2b fix: make receptacle placement success geometry-aware
| * 6e2cb86 feat: add sampled placement receptacle target
| * ce9fc15 fix: stop simulation before scene prim teardown
| * e27fc0b feat: add waypoint path motion primitive
| * 6cc68c3 fix: extend collection timeouts for minimum-jerk motion
| * 3c711f4 fix: make minimum-jerk motion respect max speed
| * 4a663bf refactor: replace trapezoidal motion with minimum-jerk motion
| * f48a36a refactor: centralize pick-place geometry and TCP targeting
| * 63cca69 fix: latch lift_pos to prevent runaway heights during transit
| * 3430d5c fix: derive placement height from object bbox
| * bd18033 fix: use latched grasp offset for placement

## Video run directory
VIDEO_RUN_DIR=/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/003_final_working_branch_validation
## Step 7 — apple smoke test
APPLE_CFG=local_isaac45/baseline_reachable_apple_integrated.yaml
## Isaac process cleanup
Stopping relevant stale processes: 44016
f564eaca3ddaa3236ae6eb47ab0a91615568c2edcac7396d2105e50acffb8cf2  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_apple/000000/meta.json
2b3a987482ae966cb82fb8a48130c129470c0652a6ad85c936bca7f98df016fb  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_apple/000000/trajectory.npz
552b3ab0b94ca15604e9a1f0a82af2b77bada84a916969c432f655cd395abf12  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/003_final_working_branch_validation/apple_final_working_branch_000000_SUCCESS_agent_plus_wrist.mp4
## Step 8 — sampled receptacle smoke test
RECEPTACLE_CFG=local_isaac45/upstream_sampled_receptacle_smoke.yaml
## Isaac process cleanup
Stopping relevant stale processes: 44893
instruction: pick up the avocado and place it in the bowl
success: True
object_category_id: avocado
object_variant_id: avocado02
object_usd_path: objects/avocado/avocado02.usd
placement_target_category_id: bowl
placement_target_variant_id: bowl08
placement_target_usd_path: objects/bowl/bowl08.usd
success_metric: target_area_center
939f389b659bd9ad163adb8a7b8149bf2fdf46490436e2c0f8faf55ca927b4a1  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_sampled_receptacle/000000/meta.json
abc054f76cdb0f9d9b9a63860a8044fe0b06339086faca194407e26d92eeea1b  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_sampled_receptacle/000000/trajectory.npz
7dfe1ee7c1e055850c5d4ce5158f3be99a8e801fef4b1e1b50d5605d3ecf6a1e  /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/003_final_working_branch_validation/sampled_receptacle_final_working_branch_000000_SUCCESS_agent_plus_wrist.mp4
## Step 9 — create gallery
## Step 10 — checkpoint tag

# FINAL SUMMARY
- working_branch: object-integration-static-assets
- working_branch_sha: 07dab834f1d5db2f56647c486ee00e75a17fbdfb
- validated_integration_sha: 07dab834f1d5db2f56647c486ee00e75a17fbdfb
- old_working_backup_branch: backup/object-integration-before-finalized-master-20260615_104358
- integration_branch_preserved: YES
- compile_status: 0
- pytest_status: 0
- apple_status: 0
- apple_success: YES
- sampled_receptacle_status: 0
- sampled_receptacle_success: YES
- checkpoint_tag: checkpoint/upstream-master-integrated-20260615
- video_run_dir: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/003_final_working_branch_validation
- html_gallery: /home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs/object_test_videos/003_final_working_branch_validation/index.html
- generated_video_count: 2
- generated_preview_count: 2
- repo_clean: YES
- push_performed: NO

## Final branches
  integration/master-sync-20260615_093855
* object-integration-static-assets

## Final status

## Recent history
*   07dab83 (HEAD -> object-integration-static-assets, tag: checkpoint/upstream-master-integrated-20260615, integration/master-sync-20260615_093855) Merge upstream master and preserve local Isaac 4.5 integration
|\  
| * 74bb9c1 (origin/master, origin/HEAD) refactor: clean up clutter sampling and config
| * 43da87b feat: add geometry-aware deterministic table clutter
| * 8cc8080 feat: use receptacle bottom clearance for placement release height
| * 286fa2b fix: make receptacle placement success geometry-aware
| * 6e2cb86 feat: add sampled placement receptacle target
| * ce9fc15 fix: stop simulation before scene prim teardown
| * e27fc0b feat: add waypoint path motion primitive
| * 6cc68c3 fix: extend collection timeouts for minimum-jerk motion
| * 3c711f4 fix: make minimum-jerk motion respect max speed
| * 4a663bf refactor: replace trapezoidal motion with minimum-jerk motion
| * f48a36a refactor: centralize pick-place geometry and TCP targeting
| * 63cca69 fix: latch lift_pos to prevent runaway heights during transit
| * 3430d5c fix: derive placement height from object bbox
| * bd18033 fix: use latched grasp offset for placement
