# Implementation Workspace (intern_ship_ws)

This workspace is organized for clarity, separating the base VLA model (SimVLA) from the Failure Probability Estimator (TDQC).

## 📂 Directory Structure

### 🤖 1. SimVLA (`simvla/`)
Everything related to the core Vision-Language-Action model.
- `code/`: Contains the original and modified SimVLA codebases.
- `scripts/`: Implementation scripts for servers, finetuning, and evaluation.
- `config/`: Configuration files and environment variables for LIBERO.
- `audit/`: Performance logs and baseline verification records.

### 🛡 2. TDQC (`tdqc/`)
The Failure Probability / Uncertainty quantification system.
- `code/`: Contains the standalone TDQC package and development integration.
- `scripts/`: Execution scripts for uncertainty servers and evaluations.
- `analysis/`: Plotting and data analysis scripts for failure detection metrics.

### 📦 3. Shared Assets (`assets/`)
Heavy assets shared across sub-projects.
- `data/`: LIBERO datasets and processed trajectory data.
- `models/`: Weights for SimVLM backbones and VLA checkpoints.
- `envs/`: Conda environment storage.

### 🛠 4. Tools (`tools/`)
Utility scripts for data management and environment setup.
- `activate_simvla.sh`: Source this to enter the environment (linked at root).
- `fix_libero_paths.py`: Updates local config for LIBERO dataset paths.
- `download_libero_datasets.sh`: Resumable downloader for LIBERO HDF5 files.

### 📊 5. Outputs (`outputs/`)
Centralized storage for all execution results.
- `logs/`: Application and training logs.
- `eval/`: Evaluation metrics and JSON trajectory results.
- `plots/`: Visualizations and performance charts.
- `runs/`: Training checkpoints and TB/WandB logs.
- `temp/`: Temporary files, downloads, and generated normalization stats.

---

## 🚀 Quick Start

1. **Activate Environment:**
   ```bash
   source activate_simvla.sh
   ```

2. **Run Uncertainty-Aware Server:**
   ```bash
   ./tdqc/scripts/run_uncertainty_server.sh
   ```

3. **Run Evaluation:**
   ```bash
   ./tdqc/scripts/run_uncertainty_eval.sh
   ```

## 🛤 Sub-Projects Detail
- **`simvla/code/SimVLA_modified`**: The production-ready VLA code with uncertainty output heads.
- **`tdqc/code/phase2_tdqc_standalone`**: The "Golden" failure probability estimator package (LSTM-TD0).
