# OpenVLA-OFT Test Workspace

This workspace was created on 2026-06-16 to set up and test the OpenVLA-OFT (One-step Fine-Tuning) model on the LIBERO benchmark.

## Workspace Structure
- `src/`: Contains model code, cloning `openvla-oft` repository.
- `logs/`: For execution and training logs.
- `reports/`: Documentation and test reports.
- `checkpoints/`: Model checkpoint storage.
- `hf_cache/`: Hugging Face downloads and cache.
- `outputs/smoke/`: Artifacts, logs, and outputs from smoke testing.

## Isolation Policy
This workspace is completely isolated from the FIPER/SimVLA workspace (`fiper_ws`).
- No modification of existing SimVLA/FIPER workspace configurations.
- No modification of existing SimVLA checkpoints or LIBERO-PRO assets.
- No disruption to active processes running on this machine.
