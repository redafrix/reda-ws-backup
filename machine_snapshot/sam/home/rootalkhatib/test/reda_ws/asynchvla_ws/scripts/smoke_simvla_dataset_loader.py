#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import torch

REDA_WS = Path("/media/rootalkhatib/My Passport/reda_ws")
SIMVLA_MODIFIED = REDA_WS / "intern_ship_ws/simvla/code/SimVLA_modified"
LIBERO_ROOT = REDA_WS / "intern_ship_ws/assets/data/libero_datasets"
REPORT = REDA_WS / "asynchvla_ws/outputs/reports/simvla_dataset_loader_smoke.md"
DEBUG_META = REDA_WS / "asynchvla_ws/data/debug/one_libero_meta.json"

sys.path.insert(0, str(SIMVLA_MODIFIED))

from datasets.dataset_smolvlm import SmolVLMDataReader  # noqa: E402


def shape_of(value):
    if torch.is_tensor(value):
        return {"shape": list(value.shape), "dtype": str(value.dtype)}
    return {"type": type(value).__name__, "repr": repr(value)[:500]}


def main() -> int:
    h5_files = sorted(LIBERO_ROOT.glob("**/*.hdf5"), key=lambda p: p.stat().st_size)
    if not h5_files:
        raise FileNotFoundError(f"No HDF5 files under {LIBERO_ROOT}")
    h5_path = h5_files[0]
    task = h5_path.stem
    if task.endswith("_demo"):
        task = task[:-5]
    m = re.search(r"SCENE\d+_", task)
    if m:
        task = task[m.end():]
    task = task.replace("_", " ")

    meta = {
        "dataset_name": "libero_hdf5",
        "data_dir": str(LIBERO_ROOT),
        "datalist": [{"path": str(h5_path), "task": task, "subset": h5_path.parent.name}],
        "num_episodes": 1,
        "observation_key": ["obs/agentview_rgb", "obs/eye_in_hand_rgb"],
        "action_key": "actions",
        "state_dim": 8,
        "action_dim": 7,
        "fps": 10,
    }
    DEBUG_META.write_text(json.dumps(meta, indent=2) + "\n")

    ds = SmolVLMDataReader(
        metas_path=str(DEBUG_META),
        num_actions=10,
        num_views=3,
        training=False,
        action_mode="libero_joint",
        image_size=384,
    )
    sample = next(iter(ds))

    terminal_lines = []
    terminal_lines.append("dataset_loader_smoke: OK")
    terminal_lines.append(f"hdf5 {h5_path}")
    terminal_lines.append(f"debug_meta {DEBUG_META}")
    terminal_lines.append(f"keys {sorted(sample.keys())}")
    for k in sorted(sample.keys()):
        terminal_lines.append(f"{k} {shape_of(sample[k])}")
    action = sample.get("action")
    if torch.is_tensor(action):
        terminal_lines.append(f"expert_action_chunk_shape {list(action.shape)}")
        terminal_lines.append(f"expert_action_min_mean_max {float(action.min())} {float(action.mean())} {float(action.max())}")
        assert list(action.shape) == [10, 7], f"Expected action [10,7], got {list(action.shape)}"

    lines = [
        "# SimVLA Dataset Loader Smoke Test",
        "",
        f"- Workspace: `{REDA_WS}`",
        f"- Loader: `{SIMVLA_MODIFIED / 'datasets/dataset_smolvlm.py'}`",
        f"- Handler: `{SIMVLA_MODIFIED / 'datasets/domain_handler/libero_hdf5.py'}`",
        f"- Debug meta: `{DEBUG_META}`",
        f"- HDF5: `{h5_path}`",
        f"- Task text: `{sample.get('language_instruction')}`",
        "",
        "## Sample Keys And Shapes",
        "",
    ]
    for key in sorted(sample.keys()):
        lines.append(f"- `{key}`: `{shape_of(sample[key])}`")
    lines.extend([
        "",
        "## Alignment Decision",
        "",
        "The official `LiberoHDF5Handler._get_action_chunk()` creates `[num_actions + 1, 7]` chunks internally: current action at index 0 plus 10 future actions. `datasets/utils.py::action_slice()` then sets `action = abs_traj[1:].clone()`, so the dataset sample exposes `action` as `[10, 7]`.",
        "",
        "For SimVLA generated chunks with `num_actions=10`, compare generated normalized `[10,7]` against `sample['action']` normalized with the model action space. Do not include the current action at index 0 in the error target.",
        "",
        "## Terminal Output",
        "",
        "```text",
        *terminal_lines,
        "```",
    ])
    REPORT.write_text("\n".join(lines) + "\n")
    print("\n".join(terminal_lines))
    print("report", REPORT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
