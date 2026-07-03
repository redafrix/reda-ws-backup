from pathlib import Path
import json
import h5py
import os

root = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")
datasets_tr = root / "datasets-tr-stage3"

print("## Validation of Translated Outputs")

h5_files = sorted(list(datasets_tr.glob("*.h5")))
json_files = sorted(datasets_tr.glob("*.json"))

print("Translated h5_count:", len(h5_files))
print("Translated json_count:", len(json_files))

def walk_h5(name, obj, prefix=""):
    if isinstance(obj, h5py.Dataset):
        print("DATASET", name, "shape=", obj.shape, "dtype=", obj.dtype)
    elif isinstance(obj, h5py.Group):
        print("GROUP", name)

for p in h5_files:
    print(f"\n### H5: {p.name} | size: {p.stat().st_size} bytes")
    try:
        with h5py.File(p, "r") as f:
            print("top_keys:", list(f.keys()))
            f.visititems(walk_h5)
    except Exception as e:
        print("ERROR reading H5:", repr(e))

for p in json_files:
    print(f"\n### JSON: {p.name} | size: {p.stat().st_size} bytes")
    try:
        data = json.loads(p.read_text())
        print("top_keys:", list(data.keys()))
        print("instruction:", data.get("instruction", None))
        print("seed:", data.get("seed", None))
    except Exception as e:
        print("ERROR reading JSON:", repr(e))
