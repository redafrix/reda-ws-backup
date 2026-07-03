#!/usr/bin/env bash

set -euo pipefail

SRC_DIR="${1:-/home/redafrix/LIBERO/libero/datasets}"
DEST_DIR="${2:-./datasets/metas}"
SUBSETS=(libero_10 libero_90 libero_goal libero_object libero_spatial)

mkdir -p "${DEST_DIR}"

echo "Linking LIBERO datasets from ${SRC_DIR} -> ${DEST_DIR}"

for subset in "${SUBSETS[@]}"; do
    src_path="${SRC_DIR}/${subset}"
    dest_path="${DEST_DIR}/${subset}"

    if [[ ! -d "${src_path}" ]]; then
        echo "Skipping ${subset}: not found in source"
        continue
    fi

    if [[ -L "${dest_path}" || -d "${dest_path}" ]]; then
        rm -rf "${dest_path}"
    fi

    ln -s "${src_path}" "${dest_path}"
    count=$(find -L "${dest_path}" -maxdepth 1 -type f -name '*.hdf5' | wc -l)
    echo "Linked ${subset}: ${count} HDF5 files"
done

echo "Done."
