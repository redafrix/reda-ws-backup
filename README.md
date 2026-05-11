# Internship Research: Generalized VLA and Failure Detection

This repository contains the full lifecycle of an internship research project focused on **Generalizing Vision-Language-Action (VLA) models** and implementing **Temporal-Difference Quality Calibration (TDQC)** for proactive failure detection in robotic manipulation.

## 🚀 Project Overview
The project is divided into two major tracks:
1.  **Literature & Structured Research:** Mapping the state-of-the-art in unseen object exploration, world models, and VLA uncertainty.
2.  **Implementation (Phase 1 & 2):** Fine-tuning the SimVLA model on LIBERO datasets and developing a standalone LSTM-based failure calibrator.

---

## 📂 Repository Structure

### 🔬 Research Track
- **`00_subjects/`**: Official internship briefs and requirements.
- **`02_search_strategy/` & `03_search_runs/`**: Comprehensive literature search history and paper shortlists.
- **`04_structured_research/`**: Deep-dive analysis and field schemas for "Unseen Object Exploration" and "World Models."
- **`06_papers/`**: Local repository of key PDF papers and reading manifests.

### 💻 Implementation Track (`intern_ship_ws/`)
- **`SimVLA/`**: The base VLA model repository (SmolVLM backbone).
- **`envs/simvla/`**: Dedicated Conda environment (Python 3.10, PyTorch, CUDA 12.4).
- **`phase2_tdqc_standalone/`**: **[ACTIVE]** Consolidated failure detection project.
- **`config/` & `data/`**: Simulation settings and LIBERO datasets.

---

## 📍 Current Project State (April 2026)
We have successfully completed the training of the **Phase 2 TDQC LSTM Calibrator**.
- **Model:** 1-layer, 128-unit LSTM.
- **Status:** Finalized (Stage 5 Polish).
- **Checkpoint:** `intern_ship_ws/phase2_tdqc_standalone/results/checkpoints/lstm_td0_final_polish_v2/best.pt`
- **Primary Metric:** Global Brier Score of **0.0823**.

## 🛠 Quick Start for Gemini
If you are resuming this project in a new session:
1.  Check `intern_ship_ws/phase2_tdqc_standalone/README.md` for the failure detection metrics.
2.  Activate the environment: `source intern_ship_ws/activate_simvla.sh`.
3.  Ensure `PYTHONPATH` includes `intern_ship_ws/phase2_tdqc_standalone/code`.
