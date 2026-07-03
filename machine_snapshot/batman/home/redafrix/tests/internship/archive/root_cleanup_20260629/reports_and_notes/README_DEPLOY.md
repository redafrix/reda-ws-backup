# SimVLA + Risk-Aware TopK8 Model Deployment Package (H10, 20260608)

This deployment package contains the necessary checkpoint, risk model files, and execution scripts to deploy the modified SimVLA policy combined with the **H10-only Risk-Aware TopK8 detector** for LIBERO / LIBERO-PRO tasks on a new workstation.

---

## 1. What This Package Contains

This package provides a clean, self-contained set of weights and runtime scripts for model inference:

*   **Modified SimVLA Checkpoint (`ckpt-60000`)**: The fine-tuned policy model.
*   **H10-only Risk-Aware TopK8 Detector**: The continuous risk detector trained on uncertainty features with a history horizon of 10.
*   **Runtime Scripts**: The core evaluation runner and helper scripts.
*   **Configuration Template**: An example JSON configuration setup for running task evaluations.

### Files Directory Tree

```text
simvla_modified_risk_topk8_h10_20260608/
├── README_DEPLOY.md           # This deployment instructions file
├── MANIFEST.json              # Package metadata and verification checksums
├── checkpoints/
│   └── simvla_modified_ckpt_60000/
│       ├── config.json        # Checkpoint structure configuration
│       ├── state.json         # Checkpoint optimization state details
│       └── model.safetensors  # Model weights (~3.0 GB)
├── risk_models/
│   └── h10_unc_topk8/
│       ├── model.pt           # PyTorch risk detector network weights
│       ├── normalization.json # Normalization parameters for inputs
│       ├── thresholds.json    # Pre-calculated threshold quantiles (e.g., q95)
│       ├── metrics.json       # Heldout test set evaluation metrics
│       ├── history.json       # Model training history log
│       └── config.json        # Risk model parameters
├── scripts/
│   ├── run_policy_matrix.py                       # Main policy evaluator script
│   ├── collect_fiper_uncertainty_receding_dean_v1.py # Uncertainty tracker & recorder
│   ├── generate_h10_online_configs.py             # Script to generate run configurations
│   └── run_online_groups.py                       # Helper script to execute runs in parallel
├── configs/
│   └── example_modified_topk8_task_config.json    # Edit this template for your local PC
└── checksums/
    └── SHA256SUMS.txt         # SHA256 verification sums for package integrity
```

---

## 2. What Is NOT Included

To keep the package clean and lightweight, the following resources must be obtained/configured separately on the destination machine:
1.  **Datasets & Training Logs**: Raw dataset NPZs, train/val logs, and query samples are omitted.
2.  **Original Repositories**: The full repository codebases for SimVLA and LIBERO-PRO are not included.
3.  **Python Environment**: Conda environments, package dependencies (PyTorch, Transformers, Robosuite, etc.) must be set up locally.

---

## 3. Required External Dependencies on the New PC

Before running the model, verify that the following are set up on the destination machine:

*   **SimVLA Modified Codebase**: A local copy of the modified SimVLA repository containing the architecture files matching the policy imports.
*   **LIBERO / LIBERO-PRO Task Assets**: The robosuite environment configuration and asset files.
*   **Python Conda Environment**: An environment containing:
    *   Python $\ge$ 3.10
    *   PyTorch (CUDA compatible)
    *   `transformers` (Hugging Face)
    *   `robosuite` & `libero`
    *   `numpy`, `pillow`, etc.
*   **SmolVLM Cache/Model**: Local cache folder for SmolVLM weights (e.g. `smolvlm_path`).
*   **Normalization Statistics**: The `libero_norm.json` stats file (path configured via `norm_stats`).

---

## 4. Configuration Steps

Before executing any script, copy `configs/example_modified_topk8_task_config.json` to a local configuration file (e.g. `configs/my_local_task_config.json`) and edit the placeholder paths:

1.  `simvla_root`: Point to your local modified SimVLA repository root directory.
2.  `libero_pro_root`: Point to the root directory containing LIBERO-PRO assets.
3.  `norm_stats`: Point to the path of the `libero_norm.json` normalization stats file.
4.  `smolvlm_path`: Point to the local SmolVLM cache folder.
5.  `output_dir`: Point to the folder where you want logs and evaluation results to be saved.
6.  `checkpoint` and `risk_model_unc_topk8_dir`: Ensure these point to the relative paths of the packaged checkpoint and risk model directories, or their absolute paths.

---

## 5. Execution Instructions

Run all commands from the root directory of the extracted package.

### A. Run a Smoke Test (Verify Environment & Code Integrity)

Execute a quick smoke test with 1 step to verify imports, PyTorch/CUDA setup, and that assets load correctly:

```bash
python scripts/run_policy_matrix.py \
  --config configs/example_modified_topk8_task_config.json \
  --policy risk_topk8 \
  --smoke
```

> [!NOTE]
> The `--policy risk_topk8` flag is required to enable the Risk-Aware TopK8 detector logic during execution.

### B. Run Full Evaluation Episodes

To execute the full policy evaluation across the specified `reset_seeds` (e.g., 300 environment steps per episode):

```bash
python scripts/run_policy_matrix.py \
  --config configs/example_modified_topk8_task_config.json \
  --policy risk_topk8
```

---

## 6. Verification & Troubleshooting

### Successful Run Verification
*   **Loader Logs**: When started, SimVLA will output Hugging Face model loaded logs.
*   **Risk Model Dims**: The script validates that the uncertainty feature dimensions match the expected `expected_topk8_dims` shape sequence: `[6, 21, 25, 27, 23, 2, 26, 24]`.
*   **Outputs**: Results will save to `output_dir` as json/npz summaries containing metrics, actions, and detected risk points.

### Common Errors

> [!WARNING]
> *   **`FileNotFoundError` / Checkpoint missing**: Ensure the relative/absolute paths in the config file are edited to match your local directory structure.
> *   **`ImportError` on simvla module**: Make sure `simvla_root` is correct and added to `PYTHONPATH` if required, or is properly resolved by the runner.
> *   **`ModuleNotFoundError: robosuite / libero`**: Check that your Conda environment is activated and has the simulation environments installed.
> *   **CUDA Out of Memory (OOM)**: SimVLA + SmolVLM requires a GPU with sufficient VRAM (minimum 16GB recommended, 24GB preferred). If OOM occurs, ensure no other heavy GPU processes are running.
> *   **Wrong suite or task ID**: Check that the simulation environment matches the specified `suite` ("libero_goal_object") and that the assets exist.
