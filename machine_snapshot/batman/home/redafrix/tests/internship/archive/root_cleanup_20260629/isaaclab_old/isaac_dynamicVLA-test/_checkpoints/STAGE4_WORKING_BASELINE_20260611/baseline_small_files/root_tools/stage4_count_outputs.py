from pathlib import Path
import h5py
import json

root = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test")

def inspect_dir(name, d):
    d = root / d
    print(f"\n## {name}: {d}")
    if not d.exists():
        print("missing")
        return
    h5s = sorted(list(d.rglob("*.h5")) + list(d.rglob("*.hdf5")))
    jsons = sorted(d.rglob("*.json"))
    mp4s = sorted(d.rglob("*.mp4"))
    print("h5_count:", len(h5s))
    print("json_count:", len(jsons))
    print("mp4_count:", len(mp4s))
    for p in h5s:
        try:
            with h5py.File(p, "r") as f:
                keys = list(f.keys())
                frames = None
                if "action" in f:
                    frames = f["action"].shape[0]
                cams = [k for k in keys if k.endswith("_rgb")]
                print(f"H5 {p.relative_to(root)} size={p.stat().st_size} frames={frames} cams={cams}")
        except Exception as e:
            print(f"H5_ERROR {p}: {e!r}")
    for p in jsons[:20]:
        try:
            data = json.loads(p.read_text())
            inst = data.get("instruction", {})
            print(f"JSON {p.relative_to(root)} task={inst.get('task')} objects={inst.get('objects')} containers={inst.get('containers')}")
        except Exception as e:
            print(f"JSON_ERROR {p}: {e!r}")
    for p in mp4s:
        print(f"MP4 {p.relative_to(root)} size={p.stat().st_size}")

inspect_dir("raw datasets", "datasets")
inspect_dir("translated stage3", "datasets-tr-stage3")
inspect_dir("translated stage4", "datasets-tr-stage4")
