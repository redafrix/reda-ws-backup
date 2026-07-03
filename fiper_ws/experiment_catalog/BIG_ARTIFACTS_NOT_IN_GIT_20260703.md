# Big Artifacts Not In Git

Updated: 2026-07-03.

This file is the Git substitute for large datasets, checkpoints, tensors, videos, and logs. Commit this manifest instead of the artifacts themselves.

## Rule

Do not commit:

- `.pt`, `.pth`, `.ckpt`, `.safetensors`, `.npz`, `.zarr`, `.mp4`, `.avi`, `.mkv`
- JSONL datasets larger than a few MB
- rendered images/videos except tiny documentation images
- full copied external repos or conda/env folders

## Current Heavy Artifacts

| Artifact | Host/path | Size/count | What it is | How it was produced |
|---|---|---:|---|---|
| Sam official goal-object source rows | Sam: `/home/rootalkhatib/test/reda_ws/fiper_ws/datasets/simvla_official_libero_goal_object_h10_uncertainty_17410ep_20260626/fiper_receding_samples.jsonl` | 52,251,571,234 bytes; 1,060,884 rows | Official `libero_goal_object_official` H10 uncertainty/ACE dataset. | Modified SimVLA `ckpt-60000`, H10, 8 ACE candidates, 49D uncertainty, saved states. |
| Bob copy of Sam source rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/source_seen_goal_object_from_sam_20260630/fiper_receding_samples.jsonl` | 52,251,571,234 bytes | Same official seen-source dataset copied to Bob. | Sam-to-Bob transfer for cross-suite official OOD campaign. |
| Cross-suite OOD `goal_swap_100` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_swap_100/fiper_receding_samples.jsonl` | 1,462,703,206 bytes; 100 episodes | Official goal-swap OOD H10 dataset. | Bob cross-suite collector, max 300. |
| Cross-suite OOD `goal_task_100` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_task_100/fiper_receding_samples.jsonl` | 1,351,962,878 bytes; 100 episodes | Official goal-task OOD H10 dataset. | Bob cross-suite collector, max 300. |
| Cross-suite OOD `goal_object_ood_180` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/goal_object_ood_180/fiper_receding_samples.jsonl` | 1,432,128,149 bytes; 180 episodes | Local 18-task goal-object OOD H10 dataset. | Bob cross-suite collector with `libero_goal_object_ood_temp` BDDL alias. |
| Cross-suite OOD `spatial_object_100` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/spatial_object_100/fiper_receding_samples.jsonl` | 602,267,676 bytes; 100 episodes | Official spatial/object OOD H10 dataset. | Bob cross-suite collector, max 300. |
| Cross-suite OOD `object_object_100` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/object_object_100/fiper_receding_samples.jsonl` | 990,372,453 bytes; 100 episodes | Official object/object OOD H10 dataset. | Bob cross-suite collector, max 300. |
| Cross-suite OOD `libero10_object_100` rows | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/cross_suite_official_ood_20260630/datasets/libero10_object_100/fiper_receding_samples.jsonl` | 1,436,932,507 bytes; 100 episodes | Official LIBERO-10 object OOD H10 dataset. | Bob cross-suite collector, max 300. |
| Official FIPER seen tensors | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_train_eval_20260701/official_fiper_data` | tensor files, hundreds of MB to GB | `obs_embeddings.pt`, `action_preds.pt`, `metadata.pkl`, RND checkpoints. | Materialized from selected seen states and SimVLA/SmolVLM visual embeddings. |
| Official FIPER cross-suite tensors | Bob: `/media/rootalkhatib/My Passport/reda_ws/fiper_ws/official_fiper_original_bob_20260701/official_fiper_seen_thresholds_cross_suite_ood_20260702` | tensor files, multiple datasets | Combined 150 seen calibration successes plus OOD test rollouts for official FIPER evaluation. | Built from seen official FIPER tensors plus OOD materialization. |
| OpenVLA model/checkpoints | Bob: `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616` | model checkpoints and rollout outputs | OpenVLA-OFT risk datasets, model checkpoints, online eval records. | OpenVLA-OFT risk pipeline. |
| Pi0.5 checkpoints/datasets/videos | Bob: `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623` | large JSONL/videos/checkpoints | Pi0.5 risk head training and online/offline OOD records. | Pi0.5 LIBERO risk collection and evaluation. |
| Isaac Lab environment | Bob: `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab` and `/home/rootalkhatib/miniconda3/envs/env_isaaclab_6_0` | environment/repo size not for Git | Isaac Lab 6.0 Franka wrist-camera project. | Separate setup with NVIDIA driver 595.71.05 and PyTorch 2.11.0+cu130. |
| Local temporary checkpoint chunks | Local: `/home/redafrix/tests/internship/fiper_ws/tmp_checkpoint/chunk_ac`, `chunk_ad`, `chunk_ae`, `chunk_af`, `chunk_ag` | about 1.98GB total | Temporary chunk files found by large-file audit. | Existing local artifact; not catalog evidence and not suitable for Git. |

## Git Substitute Practice

For every heavy artifact, commit only:

- path
- host
- generation script
- source dataset/checkpoint
- count/shape/hash if available
- report path
- trust caveat

This manifest plus the experiment maps should be enough for a future session to locate or regenerate the heavy artifact without pushing it to GitHub.
