#!/usr/bin/env bash
set -euo pipefail

ROOT=/home/redafrix/tests/internship/isaac_dynamicVLA-test
cd "$ROOT"

mkdir -p videos/multicam

echo "Creating multicam videos from raw datasets..."
for h5 in datasets/*.h5 datasets/*.hdf5; do
  [ -f "$h5" ] || continue
  base="$(basename "$h5")"
  stem="${base%.*}"
  out="videos/multicam/${stem}_raw_multicam.mp4"
  echo "RAW: $h5 -> $out"
  python3 "$ROOT/tools/make_multicam_video.py" \
    --input "$ROOT/$h5" \
    --output "$ROOT/$out" \
    --fps 20
done

echo "Creating multicam videos from translated stage4 datasets..."
for h5 in datasets-tr-stage4/*.h5 datasets-tr-stage4/*.hdf5; do
  [ -f "$h5" ] || continue
  base="$(basename "$h5")"
  stem="${base%.*}"
  out="videos/multicam/${stem}_translated_multicam.mp4"
  echo "TR: $h5 -> $out"
  python3 "$ROOT/tools/make_multicam_video.py" \
    --input "$ROOT/$h5" \
    --output "$ROOT/$out" \
    --fps 20
done

echo "Done. Videos are in: $ROOT/videos/multicam"
