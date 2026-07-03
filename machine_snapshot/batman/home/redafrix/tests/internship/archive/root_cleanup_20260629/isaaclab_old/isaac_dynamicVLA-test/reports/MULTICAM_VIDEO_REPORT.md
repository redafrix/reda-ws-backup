# Multi-Camera Video Report

Goal:
Create combined multi-camera videos from existing DynamicVLA H5 datasets for visual inspection.

No Isaac Sim launch. Offline H5-to-MP4 only.
FIRST_H5=datasets-tr-stage4/pick_franka_fcan18d_O02_00000401_384c-tr.h5
input: datasets-tr-stage4/pick_franka_fcan18d_O02_00000401_384c-tr.h5
output: videos/multicam/test_one_multicam.mp4
frame_count: 86
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
-rw-rw-r-- 1 redafrix redafrix 1.5M Jun 11 13:54 videos/multicam/test_one_multicam.mp4
Creating multicam videos from raw datasets...
RAW: datasets/long-horizon_franka_lemon13d_O02_00000500_0fab.h5 -> videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/long-horizon_franka_lemon13d_O02_00000500_0fab.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab_raw_multicam.mp4
frame_count: 106
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/pick_franka_fcan18d_O02_00000401_384c.h5 -> videos/multicam/pick_franka_fcan18d_O02_00000401_384c_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/pick_franka_fcan18d_O02_00000401_384c.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_fcan18d_O02_00000401_384c_raw_multicam.mp4
frame_count: 87
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/pick_franka_onion09d_O02_00000402_f42d.h5 -> videos/multicam/pick_franka_onion09d_O02_00000402_f42d_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/pick_franka_onion09d_O02_00000402_f42d.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_onion09d_O02_00000402_f42d_raw_multicam.mp4
frame_count: 75
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/pick_franka_tomato03d_O02_00000400_b0c0.h5 -> videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/pick_franka_tomato03d_O02_00000400_b0c0.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0_raw_multicam.mp4
frame_count: 250
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_beer05d_O02_00000301_e443.h5 -> videos/multicam/place_franka_beer05d_O02_00000301_e443_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_beer05d_O02_00000301_e443.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_beer05d_O02_00000301_e443_raw_multicam.mp4
frame_count: 59
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_cup01d_O02_00000304_b4b0.h5 -> videos/multicam/place_franka_cup01d_O02_00000304_b4b0_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_cup01d_O02_00000304_b4b0.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_cup01d_O02_00000304_b4b0_raw_multicam.mp4
frame_count: 172
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_fcan17d_O02_00000101_fb10.h5 -> videos/multicam/place_franka_fcan17d_O02_00000101_fb10_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_fcan17d_O02_00000101_fb10.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_fcan17d_O02_00000101_fb10_raw_multicam.mp4
frame_count: 118
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_tangerine00d_O02_00000303_9d65.h5 -> videos/multicam/place_franka_tangerine00d_O02_00000303_9d65_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tangerine00d_O02_00000303_9d65.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_tangerine00d_O02_00000303_9d65_raw_multicam.mp4
frame_count: 300
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_tomato02d_O02_00000042_e954.h5 -> videos/multicam/place_franka_tomato02d_O02_00000042_e954_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_tomato02d_O02_00000042_e954.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_tomato02d_O02_00000042_e954_raw_multicam.mp4
frame_count: 204
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
RAW: datasets/place_franka_wbottle07d_O02_00000300_2dfc.h5 -> videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc_raw_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets/place_franka_wbottle07d_O02_00000300_2dfc.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc_raw_multicam.mp4
frame_count: 300
available_keys: ['action', 'ee_pos', 'ee_quat', 'joints', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'sm_state', 'wrist_cam_rgb', 'wrist_cam_seg']
Creating multicam videos from translated stage4 datasets...
TR: datasets-tr-stage4/long-horizon_franka_lemon13d_O02_00000500_0fab-tr.h5 -> videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/long-horizon_franka_lemon13d_O02_00000500_0fab-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab-tr_translated_multicam.mp4
frame_count: 104
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/pick_franka_fcan18d_O02_00000401_384c-tr.h5 -> videos/multicam/pick_franka_fcan18d_O02_00000401_384c-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/pick_franka_fcan18d_O02_00000401_384c-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_fcan18d_O02_00000401_384c-tr_translated_multicam.mp4
frame_count: 86
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/pick_franka_onion09d_O02_00000402_f42d-tr.h5 -> videos/multicam/pick_franka_onion09d_O02_00000402_f42d-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/pick_franka_onion09d_O02_00000402_f42d-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_onion09d_O02_00000402_f42d-tr_translated_multicam.mp4
frame_count: 75
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/pick_franka_tomato03d_O02_00000400_b0c0-tr.h5 -> videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/pick_franka_tomato03d_O02_00000400_b0c0-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0-tr_translated_multicam.mp4
frame_count: 90
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/place_franka_beer05d_O02_00000301_e443-tr.h5 -> videos/multicam/place_franka_beer05d_O02_00000301_e443-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_beer05d_O02_00000301_e443-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_beer05d_O02_00000301_e443-tr_translated_multicam.mp4
frame_count: 59
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/place_franka_cup01d_O02_00000304_b4b0-tr.h5 -> videos/multicam/place_franka_cup01d_O02_00000304_b4b0-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_cup01d_O02_00000304_b4b0-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_cup01d_O02_00000304_b4b0-tr_translated_multicam.mp4
frame_count: 171
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/place_franka_fcan17d_O02_00000101_fb10-tr.h5 -> videos/multicam/place_franka_fcan17d_O02_00000101_fb10-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_fcan17d_O02_00000101_fb10-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_fcan17d_O02_00000101_fb10-tr_translated_multicam.mp4
frame_count: 118
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/place_franka_tomato02d_O02_00000042_e954-tr.h5 -> videos/multicam/place_franka_tomato02d_O02_00000042_e954-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_tomato02d_O02_00000042_e954-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_tomato02d_O02_00000042_e954-tr_translated_multicam.mp4
frame_count: 204
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
TR: datasets-tr-stage4/place_franka_wbottle07d_O02_00000300_2dfc-tr.h5 -> videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc-tr_translated_multicam.mp4
input: /home/redafrix/tests/internship/isaac_dynamicVLA-test/datasets-tr-stage4/place_franka_wbottle07d_O02_00000300_2dfc-tr.h5
output: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc-tr_translated_multicam.mp4
frame_count: 300
available_keys: ['action', 'ee_pos', 'ee_quat', 'object_pos', 'object_quat', 'object_vel', 'opst_cam_rgb', 'opst_cam_seg', 'side_cam_rgb', 'side_cam_seg', 'wrist_cam_rgb', 'wrist_cam_seg']
Done. Videos are in: /home/redafrix/tests/internship/isaac_dynamicVLA-test/videos/multicam

# Final Multicam Video Summary
- workspace: /home/redafrix/tests/internship/isaac_dynamicVLA-test
- raw H5 count: 10
- translated H5 count: 9
- multicam MP4 count: 20

## Videos
videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab_raw_multicam.mp4 | 1860174 bytes
videos/multicam/long-horizon_franka_lemon13d_O02_00000500_0fab-tr_translated_multicam.mp4 | 1877642 bytes
videos/multicam/pick_franka_fcan18d_O02_00000401_384c_raw_multicam.mp4 | 1423948 bytes
videos/multicam/pick_franka_fcan18d_O02_00000401_384c-tr_translated_multicam.mp4 | 1487685 bytes
videos/multicam/pick_franka_onion09d_O02_00000402_f42d_raw_multicam.mp4 | 1154740 bytes
videos/multicam/pick_franka_onion09d_O02_00000402_f42d-tr_translated_multicam.mp4 | 1180407 bytes
videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0_raw_multicam.mp4 | 3548170 bytes
videos/multicam/pick_franka_tomato03d_O02_00000400_b0c0-tr_translated_multicam.mp4 | 1847025 bytes
videos/multicam/place_franka_beer05d_O02_00000301_e443_raw_multicam.mp4 | 1100132 bytes
videos/multicam/place_franka_beer05d_O02_00000301_e443-tr_translated_multicam.mp4 | 1137349 bytes
videos/multicam/place_franka_cup01d_O02_00000304_b4b0_raw_multicam.mp4 | 3960715 bytes
videos/multicam/place_franka_cup01d_O02_00000304_b4b0-tr_translated_multicam.mp4 | 3909643 bytes
videos/multicam/place_franka_fcan17d_O02_00000101_fb10_raw_multicam.mp4 | 2168972 bytes
videos/multicam/place_franka_fcan17d_O02_00000101_fb10-tr_translated_multicam.mp4 | 2175784 bytes
videos/multicam/place_franka_tangerine00d_O02_00000303_9d65_raw_multicam.mp4 | 7526423 bytes
videos/multicam/place_franka_tomato02d_O02_00000042_e954_raw_multicam.mp4 | 4291937 bytes
videos/multicam/place_franka_tomato02d_O02_00000042_e954-tr_translated_multicam.mp4 | 4641844 bytes
videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc_raw_multicam.mp4 | 6005791 bytes
videos/multicam/place_franka_wbottle07d_O02_00000300_2dfc-tr_translated_multicam.mp4 | 6084086 bytes
videos/multicam/test_one_multicam.mp4 | 1487685 bytes

## Disk
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p5  302G  258G   29G  91% /
