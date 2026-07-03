#!/usr/bin/env python3
"""Create the fixed 600-episode LIBERO-PRO LAN/OBJECT benchmark."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import re
from dataclasses import dataclass
from typing import Any

import torch


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_LIBERO_PRO_ROOT = REPO_ROOT.parent / "LIBERO-PRO"
DEFAULT_OUTPUT_PREFIX = (
    REPO_ROOT
    / "configs"
    / "uq_benchmarks"
    / "libero_goal_lan_object_balanced600_eval_seed0_20260622"
)
SUITES = {
    "libero_goal_lan": "language_ood",
    "libero_goal_object": "target_object_asset_ood",
}
TASK_FILES = {
    0: "open_the_middle_drawer_of_the_cabinet.bddl",
    1: "put_the_bowl_on_the_stove.bddl",
    2: "put_the_wine_bottle_on_top_of_the_cabinet.bddl",
    3: "open_the_top_drawer_and_put_the_bowl_inside.bddl",
    4: "put_the_bowl_on_top_of_the_cabinet.bddl",
    5: "push_the_plate_to_the_front_of_the_stove.bddl",
    6: "put_the_cream_cheese_in_the_bowl.bddl",
    7: "turn_on_the_stove.bddl",
    8: "put_the_bowl_on_the_plate.bddl",
    9: "put_the_wine_bottle_on_the_rack.bddl",
}
AVAILABLE_STATE_COUNT = 50
SELECTED_STATES_PER_TASK = 30
EVAL_SEED = 0
EPISODE_SEED = 0
SELECTION_SEED = 2026062201


@dataclass(frozen=True)
class ProtocolPaths:
    libero_pro_root: pathlib.Path
    output_prefix: pathlib.Path

    @property
    def bddl_root(self) -> pathlib.Path:
        return self.libero_pro_root / "libero" / "libero" / "bddl_files"

    @property
    def init_root(self) -> pathlib.Path:
        return self.libero_pro_root / "libero" / "libero" / "init_files"


def main() -> None:
    paths = _parse_args()
    assets = _load_assets(paths)
    rows = _build_rows(assets)
    _validate_rows(rows)
    csv_path = paths.output_prefix.with_suffix(".csv")
    json_path = paths.output_prefix.with_suffix(".json")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    _write_csv(csv_path, rows)
    _write_json(json_path, paths, assets, rows)
    print(f"wrote {csv_path}")
    print(f"wrote {json_path}")
    print(f"episodes={len(rows)} suites={len(SUITES)} tasks_per_suite={len(TASK_FILES)}")


def _parse_args() -> ProtocolPaths:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--libero-pro-root", type=pathlib.Path, default=DEFAULT_LIBERO_PRO_ROOT)
    parser.add_argument("--output-prefix", type=pathlib.Path, default=DEFAULT_OUTPUT_PREFIX)
    args = parser.parse_args()
    return ProtocolPaths(
        libero_pro_root=args.libero_pro_root.resolve(),
        output_prefix=args.output_prefix.resolve(),
    )


def _load_assets(paths: ProtocolPaths) -> dict[tuple[str, int], dict[str, Any]]:
    assets: dict[tuple[str, int], dict[str, Any]] = {}
    for suite, perturbation in SUITES.items():
        for task_id, bddl_file in TASK_FILES.items():
            bddl_path = paths.bddl_root / suite / bddl_file
            init_path = paths.init_root / suite / bddl_file.replace(".bddl", ".pruned_init")
            if not bddl_path.is_file():
                raise FileNotFoundError(bddl_path)
            if not init_path.is_file():
                raise FileNotFoundError(init_path)
            state_count = len(torch.load(init_path, map_location="cpu", weights_only=False))
            if state_count < AVAILABLE_STATE_COUNT:
                raise RuntimeError(f"{init_path} has {state_count} states; at least 50 are required.")
            assets[(suite, task_id)] = {
                "task_suite_name": suite,
                "task_id": task_id,
                "task_description": _bddl_language(bddl_path),
                "perturbation_family": perturbation,
                "bddl_file": bddl_file,
                "bddl_path": str(bddl_path),
                "bddl_sha256": _sha256(bddl_path),
                "init_state_file": init_path.name,
                "init_state_path": str(init_path),
                "init_state_sha256": _sha256(init_path),
                "num_initial_states": state_count,
            }
    return assets


def _selected_states(suite: str, task_id: int) -> list[int]:
    ranked = sorted(
        range(AVAILABLE_STATE_COUNT),
        key=lambda state: hashlib.sha256(
            f"{SELECTION_SEED}:{suite}:{task_id}:{state}".encode("ascii")
        ).digest(),
    )
    return sorted(ranked[:SELECTED_STATES_PER_TASK])


def _build_rows(assets: dict[tuple[str, int], dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for suite in SUITES:
        for task_id in TASK_FILES:
            asset = assets[(suite, task_id)]
            for state_index in _selected_states(suite, task_id):
                order = len(rows)
                rows.append(
                    {
                        "episode_uid": f"{suite}_task{task_id:02d}_init{state_index:03d}_seed{EVAL_SEED}",
                        "execution_order_in_run": order,
                        "selected_manifest_order": order,
                        "task_suite_name": suite,
                        "task_id": task_id,
                        "task_description": asset["task_description"],
                        "initial_state_index": state_index,
                        "trial_index": state_index,
                        "eval_seed": EVAL_SEED,
                        "episode_seed": EPISODE_SEED,
                        "perturbation_family": asset["perturbation_family"],
                        "bddl_file": asset["bddl_file"],
                        "bddl_path": asset["bddl_path"],
                        "init_state_path": asset["init_state_path"],
                    }
                )
    return rows


def _validate_rows(rows: list[dict[str, Any]]) -> None:
    expected_total = len(SUITES) * len(TASK_FILES) * SELECTED_STATES_PER_TASK
    if len(rows) != expected_total:
        raise RuntimeError(f"Expected {expected_total} episodes, got {len(rows)}.")
    identities = {
        (row["task_suite_name"], row["task_id"], row["initial_state_index"], row["eval_seed"])
        for row in rows
    }
    if len(identities) != expected_total:
        raise RuntimeError("The generated protocol contains duplicate episode identities.")
    for suite in SUITES:
        for task_id in TASK_FILES:
            selected = [
                row["initial_state_index"]
                for row in rows
                if row["task_suite_name"] == suite and row["task_id"] == task_id
            ]
            if len(selected) != SELECTED_STATES_PER_TASK or len(set(selected)) != len(selected):
                raise RuntimeError(f"Invalid state selection for {suite} task {task_id}: {selected}")


def _write_csv(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_json(
    path: pathlib.Path,
    paths: ProtocolPaths,
    assets: dict[tuple[str, int], dict[str, Any]],
    rows: list[dict[str, Any]],
) -> None:
    payload = {
        "schema_version": "libero_goal_lan_object_balanced600_v1",
        "protocol_id": path.stem,
        "libero_pro_root": str(paths.libero_pro_root),
        "task_suites": list(SUITES),
        "task_ids": list(TASK_FILES),
        "available_initial_state_indices": list(range(AVAILABLE_STATE_COUNT)),
        "selected_states_per_task": SELECTED_STATES_PER_TASK,
        "selection_method": "lowest SHA-256 ranks, then ascending execution order",
        "selection_seed": SELECTION_SEED,
        "eval_seed": EVAL_SEED,
        "episode_seed": EPISODE_SEED,
        "episode_count": len(rows),
        "episodes_per_suite": len(TASK_FILES) * SELECTED_STATES_PER_TASK,
        "episodes_per_task": SELECTED_STATES_PER_TASK,
        "assets": list(assets.values()),
        "episode_uids_in_order": [row["episode_uid"] for row in rows],
        "csv_sha256": _sha256(path.with_suffix(".csv")),
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _bddl_language(path: pathlib.Path) -> str:
    match = re.search(r"\(:language\s+([^)]+)\)", path.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"Missing (:language ...) in {path}")
    return " ".join(match.group(1).strip().lower().split())


def _sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    main()
