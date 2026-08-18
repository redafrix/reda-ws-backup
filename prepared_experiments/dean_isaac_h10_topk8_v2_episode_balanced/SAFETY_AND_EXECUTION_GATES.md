# Safety and Execution Gates

V2 is a standalone risk-head training experiment. It must not launch Isaac Sim, Isaac Lab, Omniverse, SimVLA policy inference, or any OOD400 rollout.

Before launch, record read-only:

- HARD1000 completed episode count
- HARD1000 pipeline PID/alive
- HARD1000 collector PID/alive
- `nvidia-smi` total/used/free VRAM and utilization
- GPU process table

Proceed only if HARD1000 pipeline and collector are alive and a small PyTorch process can be started without creating a second Isaac/Omniverse process.

During V2 training:

- use the existing frozen `.npy` dataset only
- no simulation
- no scene loader
- no policy server
- no new data collection
- do not modify HARD1000 configs, outputs, STOP files, PIDs, or GPU settings

After each training/evaluation stage, verify HARD1000 is still alive and completed count has not decreased.

If CUDA allocation fails, OOM occurs, GPU becomes unstable, HARD1000 process exits, or collector health changes: terminate only the V2 process and stop the V2 task. Do not restart HARD1000 automatically.

OOD400 remains sealed and must not be read for outcomes or executed.
