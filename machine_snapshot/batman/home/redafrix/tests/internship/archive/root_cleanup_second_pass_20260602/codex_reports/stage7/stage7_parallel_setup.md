# Stage 7 Parallel Bob/Sam Setup

## Scope

This report documents Stage 7 parallel setup only. It does not include passwords or sensitive guide contents.

## Bob Status

- Host: `PCROBOTUBUNTU02`
- Workspace: `/media/rootalkhatib/My Passport/reda_ws`
- Git branch: `bob`
- Active Python after `source asynchvla_ws/scripts/activate_simvla_bob.sh`: `/usr/bin/python3`
- Python: `3.10.12`
- Torch/CUDA: `torch 2.5.1+cu121`, CUDA available `True`, CUDA runtime `12.1`
- GPU: `NVIDIA GeForce RTX 4070 Ti SUPER`, `16376 MiB`, driver `570.211.01`
- Disk: workspace drive `/dev/sda1` has about `1.6T` free; home drive has about `402G` free.

Bob has the Stage 5 processed datasets and Stage 6 checkpoints/reports needed for Stage 7:

- `asynchvla_ws/data/processed_stage5/id_task_split`
- `asynchvla_ws/data/processed_stage5/holdout_libero_object`
- `asynchvla_ws/data/processed_stage5/holdout_object_bowl`
- `asynchvla_ws/data/processed_stage5/holdout_libero_spatial`
- `asynchvla_ws/outputs/checkpoints/stage6`
- `asynchvla_ws/outputs/reports/stage6`

Pre-existing dirty files were present before Stage 7, including Stage 5/6 artifacts and modified Stage 5 source files. Stage 7 did not revert them. New Stage 7 files are isolated under `asynchvla_ws/src/*stage7`, `asynchvla_ws/outputs/reports/stage7`, `asynchvla_ws/outputs/logs/stage7`, and Stage 7 scripts.

## Sam Status

- Host: `PCROBOTUBUNTU05`
- Workspace found: `/home/rootalkhatib/test/reda_ws`
- Git branch: `sam`
- Existing dirty file before Stage 7: `intern_ship_ws/simvla/code/SimVLA/evaluation/libero/serve_smolvlm_libero.py`
- Activation script created: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh`
- Active Python after script: `/home/rootalkhatib/envs/simvla/bin/python3`
- Python: `3.10.20`
- Torch/CUDA: `torch 2.5.1+cu121`, CUDA available `True`, CUDA runtime `12.1`
- GPU: `NVIDIA GeForce RTX 4070 Ti SUPER`, `16376 MiB`, driver `570.211.01`
- Disk: about `202G` free on `/`.

Sam already has:

- LIBERO HDF5 data under `/home/rootalkhatib/test/reda_ws/intern_ship_ws/assets/data/libero_datasets` (`94G` observed earlier).
- SimVLA checkpoint `/home/rootalkhatib/test/reda_ws/intern_ship_ws/outputs/runs/simvla_libero_uncertainty/ckpt-60000` (`3.1G` observed earlier).
- Python environment `/home/rootalkhatib/envs/simvla` with `torch`, `transformers`, `h5py`, `safetensors`, `sklearn`, and CUDA working.

Sam is not fully ready for SimVLA model loading yet:

- The SmolVLM backbone copy is incomplete. Current `model.safetensors` size on Sam is `479232000` bytes; Bob's complete `model.safetensors` is part of a `1023M` backbone directory.
- Direct remote-to-remote `rsync` is unsupported from this laptop (`source and destination cannot both be remote`).
- Tar streaming through local SSH stalled/was interrupted after a partial copy.
- Local relay `rsync` from Bob to laptop completed in about `6:18` at roughly `2.6 MB/s`, but laptop-to-Sam upload slowed to `~0.1-1.6 MB/s` and was interrupted at about `46%` to avoid blocking all Stage 7 work.
- `asynchvla_ws/src` and `asynchvla_ws/data/splits` are present on Sam only as a lightweight partial sync; model smoke/load was not run on Sam because the backbone is incomplete.

## Parallel Decision

- Bob is the active Stage 7 execution machine now.
- Sam can be used after resuming the SmolVLM backbone sync and doing a checkpoint smoke test.
- Because Sam is not fully model-ready yet, the remaining OOD completion job was launched on Bob with `nohup`.

## Jobs Launched

Bob job launcher:

```bash
cd "/media/rootalkhatib/My Passport/reda_ws"
bash asynchvla_ws/scripts/stage7_parallel_job_launcher.sh extra-ood-bob
```

Launched job:

- PID observed: `466022`
- Log: `asynchvla_ws/outputs/logs/stage7/extra_ood_completion_bob.log`
- First split running: `holdout_libero_goal`
- Command class: `build_multiseed_trace_dataset.py`, then `build_multiseed_candidate_dataset.py`, then `run_stage6_experiments.py` for `action_only_baseline`, `full_old_baseline`, and `context_gated_action`.

## Files Created/Modified In This Phase

- `asynchvla_ws/scripts/stage7_parallel_job_launcher.sh`
- `asynchvla_ws/scripts/stage7_collect_reports.sh`
- `asynchvla_ws/outputs/reports/stage7/stage7_parallel_setup.md`
- Sam-only: `/home/rootalkhatib/test/reda_ws/asynchvla_ws/scripts/activate_simvla_sam.sh`

## Next Required Sam Step

Resume the backbone upload when network is acceptable, then run:

```bash
cd /home/rootalkhatib/test/reda_ws
source asynchvla_ws/scripts/activate_simvla_sam.sh
python3 asynchvla_ws/scripts/smoke_load_simvla_local_backbone.py
```

If that smoke test passes, Sam can run data extraction/rollout jobs in parallel.
