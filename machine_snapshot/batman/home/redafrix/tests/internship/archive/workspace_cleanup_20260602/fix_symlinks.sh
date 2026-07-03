#!/usr/bin/env bash
set -ex

BASE_DIR="$1"
BDDL_DIR="$BASE_DIR/libero/libero/bddl_files"
INIT_DIR="$BASE_DIR/libero/libero/init_files"

suites=("spatial" "object" "goal")
perts=("object" "env")

for s in "${suites[@]}"; do
    for p in "${perts[@]}"; do
        src="libero_$s"
        dst="libero_${s}_${p}"
        
        # BDDL
        if [ ! -d "$BDDL_DIR/$dst" ]; then
            ln -s "$src" "$BDDL_DIR/$dst"
        fi
        
        # INIT
        if [ ! -d "$INIT_DIR/$dst" ]; then
            ln -s "$src" "$INIT_DIR/$dst"
        fi
    done
done
echo "Symlinks created successfully in $BASE_DIR"
