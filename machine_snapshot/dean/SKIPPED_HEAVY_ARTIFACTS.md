# Dean Snapshot: Skipped Heavy Artifacts

Generated: 2026-07-03T16:36:29 Europe/Paris

This branch stores a GitHub-safe Dean snapshot for the official-FIPER and SimVLA ablation work. It includes code, configs, catalogs, reports, and small result summaries. It intentionally excludes the materialized tensors, VLM embeddings, rollout caches, checkpoints, raw states, videos, and external environments.

## Remote Roots Represented

- `/home/dean/fiper_uncertainty_collection`
- `/home/dean/fiper_goal_object_collection_20260605`
- `/home/redafrix/SimVLA_modified`
- `/home/dean/LIBERO-PRO`
- `/home/redafrix/LIBERO-PRO`

## Included Policy

- Included text/code/report/config files up to 1 MB.
- Excluded raw `*.jsonl`, tensors, arrays, pickles, checkpoints, videos, archives, generated images, and environment directories.

## Major Omitted Artifact Classes

- Official FIPER materializations: `obs_embeddings.pt`, `action_preds.pt`, `metadata.pkl`, `processed_rollouts/`, `official_fiper_data/`, `materialized_shards/`.
- Dataset and rollout sources: `datasets/`, `data/`, `states/`, `rollouts/`, `videos/`, `outputs/`, `runs/`.
- Model/checkpoint files: `models/`, `checkpoints/`, `*.pt`, `*.pth`, `*.ckpt`, `*.safetensors`, `*.npz`, `*.npy`, `*.zarr`, `*.pkl`.
- Third-party/cache/env payloads: `repos/`, `external/`, conda/venv/site-packages, `wandb/`, `cache/`.

## Reconstruction Notes

- The included reports and experiment catalog files contain the exact remote paths and protocol decisions for official FIPER train/calibration/test evaluations.
- Heavy tensors and dataset caches remain on Dean or must be regenerated from the scripts captured here.
