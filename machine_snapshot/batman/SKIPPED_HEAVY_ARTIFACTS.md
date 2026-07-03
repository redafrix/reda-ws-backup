# Batman Snapshot - Skipped Heavy Artifacts

This branch snapshot intentionally tracks small source code, configs, reports, maps, manifests, and small result files from `/home/redafrix/tests/internship`. Heavy datasets, videos, tensors, environments, copied external repos, and binary assets stay on disk and are represented here instead of being pushed to GitHub.

## Skipped Heavy/Generated Folders

| Path | Approx size | Reason |
|---|---:|---|
| `archive/workspace_cleanup_20260602/videos_testes/runs` | 364M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/workspace_cleanup_20260602/tmp_site_packages` | 3.4G | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/workspace_cleanup_20260602/tmp_opengl` | 30M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/workspace_cleanup_20260602/tmp_numba` | 27M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/workspace_cleanup_20260602/tmp_robosuite` | 591M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/workspace_cleanup_20260602/tmp_mujoco` | 23M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `archive/root_cleanup_20260629/isaaclab_old` | 11G | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `fiper_ws/tmp_checkpoint` | 1.9G | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `fiper_ws/external` | 19M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `fiper_ws/data` | 272M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `fiper_ws/experiments` | 9.4G | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `fiper_ws/realtime_deployment` | 2.7M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `cross_suite_official_ood_20260630` | 128K | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `isaac-sim` | 2.0M | heavy/generated artifact or copied dependency; keep on local disk, not Git |
| `vids` | 38M | heavy/generated artifact or copied dependency; keep on local disk, not Git |

## Large Files Detected In Source Workspace

Files >=20 MB were not intentionally added to the snapshot. If a file is needed later, fetch it from the source path or regenerate it from the documented script/report.

| Source-relative path | Size MB |
|---|---:|
| `archive/root_cleanup_20260629/packages_and_manifests/simvla_modified_risk_topk8_h10_20260608.zip` | 2709.0 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/failure_eval_all.jsonl` | 1860.7 |
| `archive/workspace_cleanup_20260602/tmp_transfers/bob_instance_A/.fiper_receding_samples.jsonl.GJFAjC` | 1237.5 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/success_train.jsonl` | 579.1 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/selective_scan_cuda.cpython-310-x86_64-linux-gnu.so` | 522.6 |
| `fiper_ws/tmp_checkpoint/chunk_ad` | 500.0 |
| `fiper_ws/tmp_checkpoint/chunk_ae` | 500.0 |
| `fiper_ws/tmp_checkpoint/chunk_ac` | 500.0 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/failure_eval_late.jsonl` | 465.8 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/failure_eval_early.jsonl` | 464.2 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/triton/_C/libtriton.so` | 450.7 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/ood_suite_success_test.jsonl` | 334.4 |
| `fiper_ws/tmp_checkpoint/chunk_af` | 295.6 |
| `fiper_ws/data/manifests/fiper_sweep_eternal_20260526_combined/rows.refs.jsonl` | 270.0 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/success_test.jsonl` | 244.4 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/failure_eval_near_end.jsonl` | 232.9 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/place_franka_tangerine00d_O02_00000303_9d65.h5` | 223.4 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/cusparselt/lib/libcusparseLt.so.0` | 202.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/patches/local_before_master_merge_20260615_093855.bundle` | 185.6 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/causal_conv1d_cuda.cpython-310-x86_64-linux-gnu.so` | 169.1 |
| `fiper_ws/experiments/receding_full_test_20260522_100546/splits/success_calib.jsonl` | 166.9 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154228/ood_perturbation_success.jsonl` | 164.4 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154257/ood_perturbation_success.jsonl` | 164.4 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/llvmlite/binding/libllvmlite.so` | 160.0 |
| `archive/workspace_cleanup_20260602/tmp_llvmlite/binding/libllvmlite.so` | 160.0 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_cup05s_O02_00000901_d4f8-tr.h5` | 138.9 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_cup05s_O02_00000901_d4f8.h5` | 137.7 |
| `fiper_ws/experiments/prepared_20260526/07_final_deployed_global/datasets/refs/success_train.rows.jsonl` | 136.8 |
| `fiper_ws/experiments/prepared_20260526/00_global_main/datasets/refs/success_train.rows.jsonl` | 136.8 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_wbottle07d_O02_00000300_2dfc-tr.h5` | 133.9 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_tangerine04s_O02_00000701_0b41-tr.h5` | 133.3 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_tangerine04s_O02_00000701_0b41.h5` | 132.7 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/place_franka_wbottle07d_O02_00000300_2dfc.h5` | 132.4 |
| `archive/workspace_cleanup_20260602/remote_pull_used_for_riskaware_zip/current_baseline_v2_018_20260528/02_ood_perturbation_holdout_object/jobs/v2_018_transformer_k16/scores.jsonl` | 127.9 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_10_family/datasets/refs/success_train_seen.rows.jsonl` | 127.1 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/pick_franka_tomato03d_O02_00000400_b0c0.h5` | 126.1 |
| `archive/workspace_cleanup_20260602/remote_pull_used_for_riskaware_zip/current_baseline_v2_018_20260528/02_ood_perturbation_holdout_mug/jobs/v2_018_transformer_k16/scores.jsonl` | 125.7 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_apple07s_O02_00000800_b329.h5` | 125.3 |
| `archive/workspace_cleanup_20260602/remote_pull_used_for_riskaware_zip/current_baseline_v2_018_20260528/02_ood_perturbation_holdout_milk/jobs/v2_018_transformer_k16/scores.jsonl` | 124.2 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_apple07s_O02_00000800_b329-tr.h5` | 123.6 |
| `archive/workspace_cleanup_20260602/remote_pull_used_for_riskaware_zip/current_baseline_v2_018_20260528/01_ood_task_8_9/jobs/v2_018_transformer_k16/scores.jsonl` | 123.5 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_tomato02d_O02_00000042_e954-tr.h5` | 113.3 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage3/place_franka_tomato02d_O02_00000042_e954-tr.h5` | 113.1 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154228/failure_eval_all.jsonl` | 110.2 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154257/failure_eval_all.jsonl` | 110.2 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.h5` | 109.4 |
| `archive/workspace_cleanup_20260602/remote_pull_used_for_riskaware_zip/current_baseline_v2_018_20260528/00_global_main/jobs/v2_018_transformer_k16/scores.jsonl` | 108.8 |
| `fiper_ws/experiments/prepared_20260526/01_ood_task_8_9/datasets/refs/success_train_seen.rows.jsonl` | 107.7 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_milk/datasets/refs/success_train_seen.rows.jsonl` | 107.4 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_mug/datasets/refs/success_train_seen.rows.jsonl` | 104.5 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_train_seen.rows.jsonl` | 99.7 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_env/datasets/refs/success_train_seen.rows.jsonl` | 99.5 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/place_franka_cup01d_O02_00000304_b4b0.h5` | 96.3 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_cup01d_O02_00000304_b4b0-tr.h5` | 95.6 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_goal/datasets/refs/success_train_seen.rows.jsonl` | 95.5 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_spatial/datasets/refs/success_train_seen.rows.jsonl` | 95.4 |
| `fiper_ws/tmp_checkpoint/chunk_ag` | 95.2 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_object_family/datasets/refs/success_train_seen.rows.jsonl` | 92.5 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_avocado06s_O02_00000801_e89a.h5` | 87.0 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_avocado06s_O02_00000801_e89a-tr.h5` | 85.7 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2` | 76.1 |
| `fiper_ws/experiments/prepared_20260526/07_final_deployed_global/datasets/refs/failure_eval_all.rows.jsonl` | 74.4 |
| `fiper_ws/experiments/prepared_20260526/00_global_main/datasets/refs/failure_eval_all.rows.jsonl` | 74.4 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_fcan03s_O02_00000902_dbb6.h5` | 66.7 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_fcan03s_O02_00000902_dbb6-tr.h5` | 66.4 |
| `fiper_ws/experiments/prepared_20260526/01_ood_task_8_9/datasets/refs/failure_eval_seen.rows.jsonl` | 66.1 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_object_family/datasets/refs/success_test_ood.rows.jsonl` | 63.5 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_env/datasets/refs/failure_eval_seen.rows.jsonl` | 62.2 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/clang/native/libclang.so` | 60.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_apple_bowl/000000/trajectory.npz` | 60.5 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/failure_eval_seen.rows.jsonl` | 60.2 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/raw/place_franka_potato14s_O02_00000802_103e.h5` | 59.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000004/trajectory.npz` | 59.4 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_spatial/datasets/refs/success_test_ood.rows.jsonl` | 59.1 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_goal/datasets/refs/success_test_ood.rows.jsonl` | 59.1 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn/translated/place_franka_potato14s_O02_00000802_103e-tr.h5` | 59.1 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_10_family/datasets/refs/failure_eval_seen.rows.jsonl` | 58.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_10_kiwi00_into_bowl10_seed301/000000/trajectory.npz` | 58.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair1_apple_bowl/000000/trajectory.npz` | 58.5 |
| `fiper_ws/scratch/scores/fiper_scores_by_split.jsonl` | 58.5 |
| `fiper_ws/experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/fiper_scores_by_split.jsonl` | 58.5 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_goal/datasets/refs/failure_eval_seen.rows.jsonl` | 58.3 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_01_apple01_into_bowl08_seed301/000000/trajectory.npz` | 58.2 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_object_family/datasets/refs/failure_eval_seen.rows.jsonl` | 58.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_lime_box/000000/trajectory.npz` | 57.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair4_box_bowl/000000/trajectory.npz` | 57.3 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/translated/place_franka_kiwi07s_O02_00000900_4f2d-tr.h5` | 56.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_07_onion00_into_bowl07_seed301/000000/trajectory.npz` | 56.7 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate/raw/place_franka_kiwi07s_O02_00000900_4f2d.h5` | 56.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_02_box01_into_bowl08_seed702/000000/trajectory.npz` | 56.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_03_tangerine06_into_tray04_seed703/000000/trajectory.npz` | 55.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_11_kiwi00_into_bowl10_seed302/000000/trajectory.npz` | 55.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_01_avocado_bowl_seed801/000000/trajectory.npz` | 55.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair5_kiwi_bowl/000000/trajectory.npz` | 55.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_02_apple01_into_bowl08_seed302/000000/trajectory.npz` | 55.3 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_12_kiwi00_into_bowl10_seed303/000000/trajectory.npz` | 54.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/master_integration_clutter/000000/trajectory.npz` | 54.6 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/long-horizon_franka_lemon13d_O02_00000500_0fab.h5` | 54.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_03_apple01_into_bowl08_seed303/000000/trajectory.npz` | 54.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000000/trajectory.npz` | 54.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_01_avocado_bowl_3episodes/000000/trajectory.npz` | 54.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_04_avocado02_into_bowl01_seed301/000000/trajectory.npz` | 53.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_01_avocado_bowl_3episodes/000002/trajectory.npz` | 53.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_13_lime00_into_box00_seed301/000000/trajectory.npz` | 53.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_08_onion00_into_bowl07_seed302/000000/trajectory.npz` | 53.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000002/trajectory.npz` | 53.5 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/long-horizon_franka_lemon13d_O02_00000500_0fab-tr.h5` | 53.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000003/trajectory.npz` | 53.5 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_peach06s_O02_00000702_c698.h5` | 53.4 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_peach06s_O02_00000702_c698-tr.h5` | 53.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_01_avocado_bowl_3episodes/000001/trajectory.npz` | 53.3 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_env/datasets/refs/success_test_ood.rows.jsonl` | 53.3 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/clutter_02_lime_box_seed802/000000/trajectory.npz` | 53.2 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_object/datasets/refs/success_test_ood.rows.jsonl` | 53.1 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/pick_franka_tomato03d_O02_00000400_b0c0-tr.h5` | 53.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_09_onion00_into_bowl07_seed303/000000/trajectory.npz` | 52.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000001/trajectory.npz` | 52.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/master_integration_sampled_receptacle/000000/trajectory.npz` | 52.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_sampled_receptacle/000000/trajectory.npz` | 52.8 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_mug/datasets/refs/failure_eval_seen.rows.jsonl` | 52.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/smart_strict_validation/000005/trajectory.npz` | 52.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_04_egg03_into_box00_seed704/000000/trajectory.npz` | 52.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/final_working_branch_apple/000000/trajectory.npz` | 51.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_regression_smart/000000/trajectory.npz` | 51.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_regression_robustness/000000/trajectory.npz` | 51.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/master_integration_apple_baseline/000000/trajectory.npz` | 51.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_regression_readiness/000000/trajectory.npz` | 51.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_05_avocado02_into_bowl01_seed302/000000/trajectory.npz` | 51.3 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_14_lime00_into_box00_seed302/000000/trajectory.npz` | 51.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_diag_D_mass_override/000000/trajectory.npz` | 50.8 |
| `fiper_ws/scratch/scores/ace_scores_by_split.jsonl` | 50.8 |
| `fiper_ws/experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/ace_scores_by_split.jsonl` | 50.8 |
| `fiper_ws/scratch/scores/rnd_scores_by_split.jsonl` | 50.6 |
| `fiper_ws/experiments/fiper_ood_task_8_9_v2_loaderfix_20260526/scores/rnd_scores_by_split.jsonl` | 50.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_06_avocado02_into_bowl01_seed303/000000/trajectory.npz` | 50.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_05_potato00_into_bowl10_seed705/000000/trajectory.npz` | 50.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair2_avocado_bowl/000000/trajectory.npz` | 50.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/robust_15_lime00_into_box00_seed303/000000/trajectory.npz` | 50.1 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/translated/place_franka_apple12s_O02_00000700_b4c3-tr.h5` | 50.0 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/pyarrow/libarrow.so.2300` | 49.9 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1/raw/place_franka_apple12s_O02_00000700_b4c3.h5` | 49.7 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_fcan17d_O02_00000101_fb10-tr.h5` | 49.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair6_beer_box/000000/trajectory.npz` | 49.2 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage3/place_franka_fcan17d_O02_00000101_fb10-tr.h5` | 49.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_verification_seed602/000000/trajectory.npz` | 49.1 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.h5` | 49.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_verification_seed603/000000/trajectory.npz` | 48.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_verification_seed605/000000/trajectory.npz` | 48.6 |
| `fiper_ws/experiments/prepared_20260526/03_ood_suite_family_holdout_spatial/datasets/refs/failure_eval_seen.rows.jsonl` | 48.3 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_milk/datasets/refs/failure_eval_seen.rows.jsonl` | 48.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_diag_B_deeper_grasp/000000/trajectory.npz` | 48.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_verification_seed601/000000/trajectory.npz` | 48.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_verification_seed604/000000/trajectory.npz` | 47.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_diag_C_moderate_depth/000000/trajectory.npz` | 47.1 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_mug/datasets/refs/success_test_ood.rows.jsonl` | 46.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/pair3_can_tray/000000/trajectory.npz` | 46.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_diag_A_default/000000/trajectory.npz` | 45.8 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets-tr-stage4/pick_franka_fcan18d_O02_00000401_384c-tr.h5` | 42.6 |
| `archive/root_cleanup_20260629/isaaclab_old/isaac_dynamicVLA-test/datasets/pick_franka_fcan18d_O02_00000401_384c.h5` | 42.6 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/wandb/bin/wandb-core` | 42.5 |
| `fiper_ws/experiments/prepared_20260526/02_ood_perturbation_holdout_milk/datasets/refs/success_test_ood.rows.jsonl` | 42.3 |
| `fiper_ws/experiments/prepared_20260526/01_ood_task_8_9/datasets/refs/success_test_ood.rows.jsonl` | 41.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default_true_mode/000000/trajectory.npz` | 40.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_apple01_default/000000/trajectory.npz` | 40.9 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150/000000/trajectory.npz` | 40.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150/000000/trajectory.npz` | 40.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_plate_plate00_mass020_stiff150_ila/episodes/000000.npz` | 40.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_bowl_bowl01_mass020_stiff150_ila/episodes/000000.npz` | 40.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_recheck/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_after_fcan03_patch/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_after_receptacle_patch/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_after_complex_objects/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_after_true_receptacle_mode/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_before_true_receptacle_mode/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/apple_recheck_before_complex_objects/000000/trajectory.npz` | 39.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/baseline_reachable_apple_ila/episodes/000000.npz` | 39.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020_true_mode/000000/trajectory.npz` | 39.5 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_fcan03_mass020/000000/trajectory.npz` | 39.5 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154228/success_train.jsonl` | 39.3 |
| `fiper_ws/experiments/archive_20260522_full_analysis_20260522_154257/success_train.jsonl` | 39.3 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default/000000/trajectory.npz` | 38.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/receptacle_tray_tray04_cup05_default_true_mode/000000/trajectory.npz` | 38.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220/000000/trajectory.npz` | 38.1 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff220_ila/episodes/000000.npz` | 38.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150/000000/trajectory.npz` | 38.0 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/fcan03_mass020_stiff150_ila/episodes/000000.npz` | 37.8 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup06_default/000000/trajectory.npz` | 37.7 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup05_default/000000/trajectory.npz` | 37.6 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup06_default_ila/episodes/000000.npz` | 37.5 |
| `fiper_ws/experiments/success_only_fiper_20260521_102354/rnd_observation_only_fix_20260521_112832/train_success_id_enriched.jsonl` | 37.5 |
| `fiper_ws/experiments/prepared_20260526/04_per_perturbation_env/datasets/refs/success_train.rows.jsonl` | 37.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_06_wbottle01_into_bowl07_seed706/000000/trajectory.npz` | 37.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/complex_cup_cup05_default_ila/episodes/000000.npz` | 37.4 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/hard_01_beer00_into_bowl01_seed701/000000/trajectory.npz` | 37.4 |
| `fiper_ws/experiments/prepared_20260526/07_final_deployed_global/datasets/refs/failure_eval_mid.rows.jsonl` | 37.2 |
| `fiper_ws/experiments/prepared_20260526/00_global_main/datasets/refs/failure_eval_mid.rows.jsonl` | 37.2 |
| `fiper_ws/experiments/prepared_20260526/04_per_perturbation_object/datasets/refs/success_train.rows.jsonl` | 37.2 |
| `archive/root_cleanup_20260629/isaaclab_old/franka_wrist_camera_isaaclab-test/outputs/tiny_collect/000000/trajectory.npz` | 37.0 |
| `archive/workspace_cleanup_20260602/tmp_site_packages/opencv_python.libs/libopenblasp-r0-59ffcd50.3.15.so` | 36.9 |
| ... | 68 additional large files omitted from this table |

## Snapshot Rule

Included file classes were small `.py`, `.sh`, `.md`, `.txt`, `.json`, `.jsonl`, `.csv`, `.tsv`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`, `.xml`, `.bddl`, `.html`, `.css`, `.js`, and notebook files. Files larger than 2 MB were excluded during snapshot copy.
