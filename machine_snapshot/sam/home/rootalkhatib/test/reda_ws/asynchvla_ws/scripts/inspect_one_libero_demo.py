#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import h5py

ROOT = Path("/media/rootalkhatib/My Passport/reda_ws")
DATA_ROOT = ROOT / "intern_ship_ws/assets/data/libero_datasets"
OUT = ROOT / "asynchvla_ws/outputs/reports/one_libero_demo_inspection.md"


def shape_dtype(obj):
    return f"shape={tuple(obj.shape)} dtype={obj.dtype}"


def main() -> None:
    files = sorted(DATA_ROOT.rglob("*.hdf5"), key=lambda p: p.stat().st_size)
    if not files:
        raise SystemExit(f"No HDF5 files found under {DATA_ROOT}")
    path = files[0]
    lines = []
    lines.append("# One LIBERO Demo Inspection")
    lines.append("")
    lines.append(f"HDF5 path: `{path}`")
    lines.append(f"File size: `{path.stat().st_size}` bytes")
    lines.append("")
    with h5py.File(path, "r") as f:
        lines.append(f"Top-level keys: `{list(f.keys())}`")
        data = f["data"]
        demo_keys = list(data.keys())
        lines.append(f"Number of demos: `{len(demo_keys)}`")
        demo_key = demo_keys[0]
        demo = data[demo_key]
        lines.append(f"Selected demo: `{demo_key}`")
        lines.append("")
        lines.append("## Demo Keys")
        lines.append("")
        lines.append(f"Demo direct keys: `{list(demo.keys())}`")
        obs = demo.get("obs")
        if obs is not None:
            lines.append(f"Obs keys: `{list(obs.keys())}`")
        lines.append("")
        lines.append("## Required Shapes")
        lines.append("")
        keys = [
            "actions",
            "obs/agentview_rgb",
            "obs/eye_in_hand_rgb",
            "obs/ee_pos",
            "obs/ee_ori",
            "obs/gripper_states",
            "obs/joint_states",
        ]
        for key in keys:
            if key in demo:
                lines.append(f"- `{key}`: `{shape_dtype(demo[key])}`")
            else:
                lines.append(f"- `{key}`: MISSING")
        if demo.attrs:
            lines.append("")
            lines.append("## Demo Attributes")
            for k, v in demo.attrs.items():
                lines.append(f"- `{k}`: `{v}`")
        if f.attrs:
            lines.append("")
            lines.append("## File Attributes")
            for k, v in f.attrs.items():
                lines.append(f"- `{k}`: `{v}`")
    OUT.write_text("\n".join(lines) + "\n")
    print("wrote", OUT)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
