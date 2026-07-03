from pathlib import Path
import h5py, json
import numpy as np

EXP = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v1")
raw = EXP / "raw"

print("## Static V1 raw inspection")
h5s = sorted(raw.glob("*.h5"))
jsons = sorted(raw.glob("*.json"))
mp4s = sorted(raw.glob("*.mp4"))
print("h5_count", len(h5s))
print("json_count", len(jsons))
print("mp4_count", len(mp4s))

for h5p in h5s:
    print("\n###", h5p.name)
    with h5py.File(h5p, "r") as f:
        print("keys", list(f.keys()))
        frames = f["action"].shape[0] if "action" in f else None
        print("frames", frames)
        if "object_vel" in f:
            vel = f["object_vel"][:min(25, f["object_vel"].shape[0])]
            norms = np.linalg.norm(vel, axis=1)
            print("object_vel_first_25_norms_min_mean_max", float(norms.min()), float(norms.mean()), float(norms.max()))
            print("object_vel_first_10", vel[:10].tolist())
        for cam in ["wrist_cam_rgb", "side_cam_rgb", "opst_cam_rgb"]:
            if cam in f:
                print(cam, f[cam].shape, f[cam].dtype)

for jp in jsons:
    data = json.loads(jp.read_text())
    print("\nJSON", jp.name)
    print("instruction", data.get("instruction"))
    scene = data.get("scene", {})
    obj = scene.get("object", {})
    init_state = obj.get("init_state", {})
    print("json_object_init_lin_vel", init_state.get("lin_vel"))
