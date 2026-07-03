import numpy as np
import json
from pathlib import Path

def debug_run(out_dir_name):
    base_dir = Path("/home/redafrix/tests/internship/franka_wrist_camera_isaaclab-test/outputs")
    run_dir = base_dir / out_dir_name / "000000"
    if not run_dir.exists():
        print(f"{out_dir_name} does not exist.")
        return
    
    meta = json.loads((run_dir / "meta.json").read_text())
    traj = np.load(run_dir / "trajectory.npz", allow_pickle=True)
    
    print(f"\n=== Debugging {out_dir_name} ===")
    print("Trajectory keys:", list(traj.keys()))
    
    # Get last frame object position
    for key in traj.keys():
        if "object" in key or "pos" in key or "pose" in key or "root" in key:
            print(f"{key} last value:", traj[key][-1])
                
    # Print bbox and placements from meta
    print("Object BBox Min:", meta.get("object_local_bbox_min"))
    print("Object BBox Max:", meta.get("object_local_bbox_max"))
    print("Placement Target Pos:", meta.get("placement_target_pos_local"))
    print("Placement Target BBox Min:", meta.get("placement_target_local_bbox_min"))
    print("Placement Target BBox Max:", meta.get("placement_target_local_bbox_max"))

debug_run("pair3_can_tray")
debug_run("pair4_box_bowl")
debug_run("pair6_beer_box")
