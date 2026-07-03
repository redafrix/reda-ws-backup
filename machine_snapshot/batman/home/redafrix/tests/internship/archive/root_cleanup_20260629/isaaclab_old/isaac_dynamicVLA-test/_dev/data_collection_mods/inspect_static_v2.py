from pathlib import Path
import h5py, json
import numpy as np

EXP = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v2_stable_spawn")
raw = EXP / "raw"

print("## Static V2 raw inspection")
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
            vel = f["object_vel"][:min(50, f["object_vel"].shape[0])]
            norms = np.linalg.norm(vel, axis=1)
            print("object_vel_first_50_norms_min_mean_max", float(norms.min()), float(norms.mean()), float(norms.max()))
            print("object_vel_first_10", vel[:10].tolist())
        if "object_quat" in f:
            print("object_quat_first_3", f["object_quat"][:3].tolist())

for jp in jsons:
    data = json.loads(jp.read_text())
    print("\nJSON", jp.name)
    print("instruction", data.get("instruction"))
    scene = data.get("scene", {})
    obj = scene.get("object", {})
    init_state = obj.get("init_state", {})
    print("json_object_init_pos", init_state.get("pos"))
    print("json_object_init_quat", init_state.get("quat"))
    print("json_object_init_lin_vel", init_state.get("lin_vel"))
