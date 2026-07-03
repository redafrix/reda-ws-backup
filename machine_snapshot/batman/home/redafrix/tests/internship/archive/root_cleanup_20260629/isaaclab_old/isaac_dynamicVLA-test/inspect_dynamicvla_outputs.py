from pathlib import Path
import json
import h5py
import os

root = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
datasets = root / "datasets"

print("## Deep validation of existing generated outputs")

h5_files = sorted(list(datasets.glob("*.h5")) + list(datasets.glob("*.hdf5")))
json_files = sorted(datasets.glob("*.json"))
mp4_files = sorted(datasets.glob("*.mp4"))

print("h5_count:", len(h5_files))
print("json_count:", len(json_files))
print("mp4_count:", len(mp4_files))

def walk_h5(name, obj, prefix=""):
    if isinstance(obj, h5py.Dataset):
        print("DATASET", name, "shape=", obj.shape, "dtype=", obj.dtype)
    elif isinstance(obj, h5py.Group):
        print("GROUP", name)

for p in h5_files[:5]:
    print("\n### H5:", p, "size=", p.stat().st_size)
    try:
        with h5py.File(p, "r") as f:
            print("top_keys:", list(f.keys()))
            f.visititems(walk_h5)
    except Exception as e:
        print("ERROR reading H5:", repr(e))

for p in json_files[:5]:
    print("\n### JSON:", p, "size=", p.stat().st_size)
    try:
        data = json.loads(p.read_text())
        print("top_keys:", list(data.keys())[:50])
        print("instruction:", data.get("instruction", None))
        print("seed:", data.get("seed", None))
    except Exception as e:
        print("ERROR reading JSON:", repr(e))

for p in mp4_files[:10]:
    print("\n### MP4:", p, "size=", p.stat().st_size)
