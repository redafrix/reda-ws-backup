#!/usr/bin/env bash
# Exit on error
set -e

echo "Resuming reaching dataset collection (episodes 55-99)..."
./run_collect.sh --collection_config collection_reaching_resume.yaml --headless

echo "Merging collection manifest..."
# Source environment variables if conda environment is not currently active
CONDA_ROOT="${CONDA_ROOT:-$HOME/miniconda3}"
source "$CONDA_ROOT/etc/profile.d/conda.sh"
conda activate env_isaaclab_6_0
PYTHONPATH=src python scratch/finalize_manifest_reaching.py

echo "Starting 100 pick and place episodes..."
./run_collect.sh --collection_config collection_pick_place_100.yaml --headless

echo "All collections resumed and finished successfully!"
