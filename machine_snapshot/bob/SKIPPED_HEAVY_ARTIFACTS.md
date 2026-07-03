# Bob Snapshot: Skipped Heavy Artifacts

Generated: 2026-07-03T16:31:55 Europe/Paris

This branch is a GitHub-safe mirror of Bob experiment code, configs, reports, catalogs, and small structured result files. It intentionally excludes raw datasets, model checkpoints, videos, simulator states, Python environments, external source checkouts, and large episode streams. The goal is to preserve every actionable script/report/map while avoiding files that GitHub cannot store reliably.

## Included Policy

- Included text/code/report/config files up to 1 MB: `.py`, `.sh`, `.md`, `.txt`, `.json`, `.csv`, `.tsv`, `.yaml`, `.yml`, `.toml`, `.ini`, `.cfg`, `.xml`, `.bddl`, `.html`, `.css`, `.js`, `.log`, README/LICENSE/Makefile/Dockerfile/.gitignore.
- Excluded raw `.jsonl` episode streams even when small, because these are data records rather than source/result summaries.
- Excluded all binary checkpoints, state arrays, videos, archives, native objects, images, and environment folders.

## Remote Roots Represented

- `/media/rootalkhatib/My Passport/reda_ws/fiper_ws`
- `/media/rootalkhatib/My Passport/reda_ws/openvla_oft_ws_20260616`
- `/media/rootalkhatib/My Passport/reda_ws/pi05_libero_risk_ws_20260623`
- `/home/rootalkhatib/isaaclab_repo/franka_wrist_camera_isaaclab`

## Major Omitted Artifact Classes

- **Raw datasets and derived dataset folders:** `datasets/`, `data/`, `trash/`, `states/`, `processed_rollouts/`, `official_fiper_data/`
- **Online rollout streams and logs:** `online_evals/`, `logs/`, `runs/`, raw `*.jsonl` episode/sample streams
- **Model weights and checkpoints:** `models/`, `checkpoints/`, `*.pt`, `*.pth`, `*.ckpt`, `*.safetensors`, `*.npz`, `*.zarr`
- **Videos and media:** `videos/`, `*.mp4`, `*.avi`, `*.mkv`, `*.mov`, image files
- **Third-party repos and environments:** `repos/`, `external/`, `openpi/`, `openvla-oft/`, `LIBERO-PRO/`, conda/venv/site-packages
- **Large simulator and Isaac artifacts:** `outputs/`, `wandb/`, `cache/`, USD/native/object/archive files

## Notes For Reconstruction

- The exact remote source paths above remain the canonical locations for the omitted large files on Bob.
- Experiment catalogs and reports in this snapshot document the dataset/checkpoint paths and metrics needed to recover or rerun the heavy artifacts.
- If a future workflow requires a specific omitted checkpoint or dataset, fetch it from Bob by path rather than trying to restore it from Git.

