"""Helpers for exact raw-episode replay manifests produced during conversion."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True, slots=True)
class SourceEpisodeRef:
    hdf5_path: Path
    demo: str
    source_episode_path: Path
    timesteps: int


def load_source_episode_refs(report_path: Path) -> list[SourceEpisodeRef]:
    report = json.loads(report_path.read_text(encoding="utf-8"))
    refs: list[SourceEpisodeRef] = []
    for file_record in report.get("files", []):
        hdf5_path = Path(file_record["path"])
        for demo in file_record.get("verified_demos", []):
            timesteps = int(demo["timesteps"])
            if timesteps <= 0:
                raise ValueError(f"timesteps must be positive for {hdf5_path}/{demo['demo']}, got {timesteps}.")
            refs.append(
                SourceEpisodeRef(
                    hdf5_path=hdf5_path,
                    demo=str(demo["demo"]),
                    source_episode_path=Path(demo["source_episode_path"]),
                    timesteps=timesteps,
                )
            )
    if not refs:
        raise ValueError(f"No verified demos found in {report_path}.")
    _validate_unique_refs(refs, report_path)
    return refs


def validate_source_episode_refs(refs: list[SourceEpisodeRef], require_existing_paths: bool) -> None:
    for ref in refs:
        if require_existing_paths:
            if not ref.hdf5_path.is_file():
                raise FileNotFoundError(ref.hdf5_path)
            if not ref.source_episode_path.is_dir():
                raise FileNotFoundError(ref.source_episode_path)
        if ref.timesteps <= 0:
            raise ValueError(f"timesteps must be positive for {ref.hdf5_path}/{ref.demo}, got {ref.timesteps}.")


def _validate_unique_refs(refs: list[SourceEpisodeRef], report_path: Path) -> None:
    keys = [(ref.hdf5_path, ref.demo) for ref in refs]
    if len(keys) != len(set(keys)):
        raise ValueError(f"Duplicate HDF5 demo refs found in {report_path}.")
