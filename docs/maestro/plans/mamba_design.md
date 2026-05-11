# Design Document: Mamba Evolution for TDQC

## Context
This design document covers 'Plan B' (Mamba Evolution) for the TDQC project. It involves replacing the existing LSTM-based calibrator with a Mamba-based State Space Model (SSM).

## Goals
1. Implement `TDQCMambaCalibrator` with $O(1)$ constant-time inference.
2. Establish a stable environment for Mamba's CUDA kernels on the SSD.
3. Verify the implementation via isolated dry runs in a research capsule.

## Architecture
- **Environment**: Isolated Python environment at `/home/redafrix/envs/simvla_mamba`.
- **Capsule**: `/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/v8_exp12_mamba/`.
- **Model**: Stacked Mamba blocks with RMSNorm.
- **Inference**: Stateful updates using `InferenceParams`.

## Verification
- Environment verification (`import mamba_ssm`).
- Mock training run (1 epoch).
- Mock inference step test.
