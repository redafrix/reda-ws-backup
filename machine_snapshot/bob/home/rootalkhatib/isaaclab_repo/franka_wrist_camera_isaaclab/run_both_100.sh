#!/usr/bin/env bash
# Exit on error
set -e

echo "Starting 100 reaching episodes..."
./run_collect.sh --collection_config collection_reaching_100.yaml --headless

echo "Reaching dataset collection complete. Starting 100 pick and place episodes..."
./run_collect.sh --collection_config collection_pick_place_100.yaml --headless

echo "All collection runs completed successfully!"
