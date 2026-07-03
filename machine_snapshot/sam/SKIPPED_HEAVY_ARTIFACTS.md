# Sam Snapshot: Skipped Heavy Artifacts

Generated: 2026-07-03T16:34:23 Europe/Paris

This branch stores a GitHub-safe Sam snapshot: experiment catalogs, scripts, configs, reports, and small structured summaries. Large rollout datasets and raw simulator artifacts remain on Sam/Bob and are referenced by path in the experiment maps.

## Remote Roots Represented

- `/home/rootalkhatib/test/reda_ws/fiper_ws`
- `/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts`

## Included Policy

- Included text/code/report/config files up to 1 MB.
- Excluded raw `*.jsonl` records, checkpoints, arrays, videos, archives, generated media, environments, external repos, and heavy dataset folders.

## Major Omitted Artifact Classes

- Raw data: `datasets/`, `data/`, `trash/`, `states/`, `videos/`, `outputs/`, `runs/`.
- Logs and raw streams: `logs/`, raw `*.jsonl` episode/sample files.
- Models/checkpoints: `models/`, `checkpoints/`, `*.pt`, `*.pth`, `*.ckpt`, `*.safetensors`, `*.npz`, `*.zarr`.
- Third-party code and environments: `repos/`, `external/`, `LIBERO-PRO/`, conda/venv/site-packages.

## Reconstruction Notes

- The frozen SimVLA uncertainty datasets and official-suite collection outputs are intentionally not pushed; use the paths recorded in `fiper_ws/experiment_catalog/` to fetch them from Sam/Bob.
- This branch should be enough to recover scripts, reports, and provenance without storing heavy training/evaluation data in Git.
