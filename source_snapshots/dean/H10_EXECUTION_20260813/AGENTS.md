# Workspace Rules

- Never modify either pinned repository under
  `/mnt/ai/projects/simvla_reproduction_workspace`.
- Never modify the verified package under
  `/mnt/ai/projects/simvla_reaching_inference_package_20260730`.
- Never signal, pause, renice, restart, or compete with the pi0.5 trainer.
- Do not import or launch Isaac, EGL, CUDA, or the SimVLA model while
  `train_grad_accum.py` is active.
- Use `softplus_110k` with `softplus_raw_variance`; never use log-sigma.
- OOD-150 is smoke/final-evaluation only, never risk training/calibration.
- Keep episode writes atomic and validate before finalization.
- Do not add outcome, reward, timestep, seed, task ID, or scenario ID to
  deployable model inputs.
- Do not train the temporal risk head in this workspace.
