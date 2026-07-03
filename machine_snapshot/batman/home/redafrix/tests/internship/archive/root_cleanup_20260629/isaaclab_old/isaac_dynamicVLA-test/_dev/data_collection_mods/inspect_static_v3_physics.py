from pathlib import Path
import h5py, json
import numpy as np

EXP = Path("/home/redafrix/tests/internship/isaac_dynamicVLA-test/_dev/data_collection_mods/experiments/static_v3_true_stable_physics_gate")
raw = EXP / "raw"

print("## Static V3 orientation + physics sanity inspection")
h5s = sorted(raw.glob("*.h5"))
jsons = sorted(raw.glob("*.json"))
mp4s = sorted(raw.glob("*.mp4"))
print("h5_count", len(h5s))
print("json_count", len(jsons))
print("mp4_count", len(mp4s))

json_by_stem = {p.stem: json.loads(p.read_text()) for p in jsons}

for h5p in h5s:
    print("\n###", h5p.name)
    stem = h5p.stem
    meta = json_by_stem.get(stem, {})
    init = meta.get("scene", {}).get("object", {}).get("init_state", {})

    print("json_object_init_lin_vel", init.get("lin_vel"))
    print("json_object_init_quat", init.get("rot") or init.get("quat"))
    print("json_object_init_pos", init.get("pos"))

    with h5py.File(h5p, "r") as f:
        print("keys", list(f.keys()))
        frames = f["action"].shape[0] if "action" in f else None
        print("frames", frames)

        keep = True
        reasons = []

        if "object_quat" in f:
            q = f["object_quat"][:min(10, f["object_quat"].shape[0])]
            xy_abs_max = float(np.max(np.abs(q[:, 1:3])))
            print("quat_xy_abs_max_first_10", xy_abs_max)
            yaw_only_like = xy_abs_max < 1e-3
            print("yaw_only_like_first_10", "YES" if yaw_only_like else "NO")
            if not yaw_only_like:
                keep = False
                reasons.append("not_yaw_only_quat_first_10")

        if "object_vel" in f:
            vel = f["object_vel"][:min(50, f["object_vel"].shape[0])]
            norms = np.linalg.norm(vel, axis=1)
            v_min = float(norms.min())
            v_mean = float(norms.mean())
            v_max = float(norms.max())
            print("object_vel_first_50_norms_min_mean_max", v_min, v_mean, v_max)
            if v_max > 0.25:
                keep = False
                reasons.append(f"early_velocity_spike_gt_0.25:{v_max:.3f}")

        if "object_pos" in f:
            pos = f["object_pos"][:min(80, f["object_pos"].shape[0])]
            z = pos[:, 2]
            z0 = float(z[0])
            z_min = float(z.min())
            z_max = float(z.max())
            dz_min = z_min - z0
            dz_max = z_max - z0
            dz_frame = float(np.max(np.abs(np.diff(z)))) if len(z) > 1 else 0.0
            print("object_z_first80_z0_min_max_dzmin_dzmax_max_step", z0, z_min, z_max, dz_min, dz_max, dz_frame)

            if dz_min < -0.08:
                keep = False
                reasons.append(f"z_drop_gt_8cm:{dz_min:.3f}")
            if dz_frame > 0.08:
                keep = False
                reasons.append(f"z_step_jump_gt_8cm:{dz_frame:.3f}")

        print("PHYSICS_GATE_KEEP", "YES" if keep else "NO")
        print("PHYSICS_GATE_REASONS", reasons)
