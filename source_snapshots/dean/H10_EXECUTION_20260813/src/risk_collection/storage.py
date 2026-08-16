"""Episode-atomic output store with deterministic resume recovery."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from datetime import datetime, timezone
from typing import Any, Iterable

from .schema import validate_row


RESUME_COMPATIBLE_OPERATIONAL_SOURCES = frozenset(
    {
        "src/risk_collection/parity_audit.py",
        "src/risk_collection/storage.py",
    }
)


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def canonical_sha256(payload: Any) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


def _write_bytes_fsync(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.parent.chmod(0o755)
    with path.open("wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    path.chmod(0o644)


def _write_parts_fsync(path: Path, parts: Iterable[bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(temp_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            for part in parts:
                handle.write(part)
            handle.flush()
            os.fsync(handle.fileno())
        temp.chmod(0o644)
        temp.replace(path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        temp.unlink(missing_ok=True)


def _file_identity(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    if not path.is_file():
        return digest.hexdigest(), size
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def _iter_file_chunks(path: Path) -> Iterable[bytes]:
    with path.open("rb") as handle:
        yield from iter(lambda: handle.read(1024 * 1024), b"")


def write_json_atomic(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.parent.chmod(0o755)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temp.chmod(0o644)
        temp.replace(path)
        dir_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    finally:
        temp.unlink(missing_ok=True)


def _jsonl_bytes(rows: Iterable[dict[str, Any]]) -> bytes:
    return "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows
    ).encode("utf-8")


def authoritative_episode_dirs(root: Path) -> list[Path]:
    """Return committed episodes in the append order recorded by the store."""
    root = root.resolve()
    episodes_dir = root / "episodes"
    committed = {
        path.name: path
        for path in episodes_dir.iterdir()
        if path.is_dir() and (path / "COMMITTED").is_file()
    }
    summaries_path = root / "episode_summaries.jsonl"
    if not summaries_path.is_file():
        raise RuntimeError(f"missing authoritative summary index: {summaries_path}")
    ordered: list[Path] = []
    seen: set[str] = set()
    for line_number, line in enumerate(summaries_path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        episode_id = str(json.loads(line)["episode_id"])
        if episode_id in seen:
            raise RuntimeError(
                f"duplicate episode in summary index at line {line_number}: {episode_id}"
            )
        if episode_id not in committed:
            raise RuntimeError(
                f"summary index references uncommitted episode: {episode_id}"
            )
        seen.add(episode_id)
        ordered.append(committed[episode_id])
    if seen != set(committed):
        raise RuntimeError(
            "summary index and committed episode membership differ: "
            f"missing={sorted(set(committed) - seen)} "
            f"unexpected={sorted(seen - set(committed))}"
        )
    return ordered


def verify_aggregate_indexes(
    root: Path, episode_dirs: list[Path]
) -> dict[str, str | int]:
    """Verify derived aggregates against episodes without materializing the round."""
    root = root.resolve()
    rows_digest = hashlib.sha256()
    summaries_digest = hashlib.sha256()
    rows_bytes = 0
    summaries_bytes = 0
    with (root / "risk_receding_samples.jsonl").open("rb") as aggregate_rows, (
        root / "episode_summaries.jsonl"
    ).open("rb") as aggregate_summaries:
        for episode_dir in episode_dirs:
            with (episode_dir / "risk_rows.jsonl").open("rb") as rows_file:
                for chunk in iter(lambda: rows_file.read(1024 * 1024), b""):
                    actual = aggregate_rows.read(len(chunk))
                    if actual != chunk:
                        raise RuntimeError(
                            "aggregate rows differ from authoritative episode order at "
                            f"{episode_dir.name}"
                        )
                    rows_digest.update(chunk)
                    rows_bytes += len(chunk)
            summary_payload = (
                canonical_json(json.loads((episode_dir / "summary.json").read_text()))
                + "\n"
            ).encode("utf-8")
            actual_summary = aggregate_summaries.read(len(summary_payload))
            if actual_summary != summary_payload:
                raise RuntimeError(
                    "aggregate summaries differ from authoritative episode order at "
                    f"{episode_dir.name}"
                )
            summaries_digest.update(summary_payload)
            summaries_bytes += len(summary_payload)
        if aggregate_rows.read(1):
            raise RuntimeError("aggregate rows contain trailing data")
        if aggregate_summaries.read(1):
            raise RuntimeError("aggregate summaries contain trailing data")
    return {
        "aggregate_rows_sha256": rows_digest.hexdigest(),
        "aggregate_rows_bytes": rows_bytes,
        "aggregate_summaries_sha256": summaries_digest.hexdigest(),
        "aggregate_summaries_bytes": summaries_bytes,
    }


class EpisodeStore:
    """Final episode directories are authoritative; aggregate JSONL is derived."""

    def __init__(self, root: Path, run_manifest: dict[str, Any]) -> None:
        self.root = root.resolve()
        self.episodes_dir = self.root / "episodes"
        self.staging_dir = self.root / ".staging"
        self.quarantine_dir = self.root / "quarantine"
        self.errors_dir = self.root / "errors"
        self.rows_path = self.root / "risk_receding_samples.jsonl"
        self.summaries_path = self.root / "episode_summaries.jsonl"
        self.errors_path = self.root / "episode_errors.jsonl"
        self.status_path = self.root / "live_status.json"
        self.manifest_path = self.root / "run_manifest.json"
        self.resume_amendments_path = self.root / "resume_provenance_amendments.jsonl"
        self.stop_marker_path = self.root / "STOP_AFTER_CURRENT_EPISODE"
        self.run_manifest = run_manifest
        self.manifest_hash = canonical_sha256(run_manifest)
        self.root.mkdir(parents=True, exist_ok=True)
        self.episodes_dir.mkdir(exist_ok=True)
        self.staging_dir.mkdir(exist_ok=True)
        self.quarantine_dir.mkdir(exist_ok=True)
        self.errors_dir.mkdir(exist_ok=True)
        for directory in (
            self.root,
            self.episodes_dir,
            self.staging_dir,
            self.quarantine_dir,
            self.errors_dir,
        ):
            directory.chmod(0o755)
        self._initialize_manifest()
        self._quarantine_staging()
        self._recover_aggregate_indexes_if_needed()

    def _initialize_manifest(self) -> None:
        if self.manifest_path.exists():
            existing = json.loads(self.manifest_path.read_text())
            if canonical_sha256(existing) != self.manifest_hash:
                changed_sources = self._resume_compatible_source_changes(
                    existing, self.run_manifest
                )
                if changed_sources is None:
                    raise RuntimeError("existing run manifest differs from requested run")
                self._record_resume_provenance(existing, changed_sources)
        else:
            write_json_atomic(self.manifest_path, self.run_manifest)

    @staticmethod
    def _resume_compatible_source_changes(
        existing: dict[str, Any], requested: dict[str, Any]
    ) -> dict[str, dict[str, str | None]] | None:
        """Allow only the documented post-launch ordering/parity audit patch."""
        existing_copy = json.loads(json.dumps(existing))
        requested_copy = json.loads(json.dumps(requested))
        try:
            existing_sources = existing_copy["codebases"].pop(
                "isolated_workspace_source_sha256"
            )
            requested_sources = requested_copy["codebases"].pop(
                "isolated_workspace_source_sha256"
            )
        except (KeyError, TypeError):
            return None
        if canonical_sha256(existing_copy) != canonical_sha256(requested_copy):
            return None

        changed = {
            path: {
                "original_sha256": existing_sources.get(path),
                "resume_sha256": requested_sources.get(path),
            }
            for path in sorted(set(existing_sources) | set(requested_sources))
            if existing_sources.get(path) != requested_sources.get(path)
        }
        if not changed or not set(changed).issubset(
            RESUME_COMPATIBLE_OPERATIONAL_SOURCES
        ):
            return None
        return changed

    def _record_resume_provenance(
        self,
        existing_manifest: dict[str, Any],
        changed_sources: dict[str, dict[str, str | None]],
    ) -> None:
        """Persist the accepted operational-only source transition without mutation."""
        requested_hash = canonical_sha256(self.run_manifest)
        records: list[dict[str, Any]] = []
        if self.resume_amendments_path.is_file():
            records = [
                json.loads(line)
                for line in self.resume_amendments_path.read_text().splitlines()
                if line.strip()
            ]
        if any(record.get("requested_manifest_sha256") == requested_hash for record in records):
            return
        records.append(
            {
                "schema_version": "simvla_risk_resume_provenance_v1",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "original_manifest_sha256": canonical_sha256(existing_manifest),
                "requested_manifest_sha256": requested_hash,
                "accepted_source_changes": changed_sources,
                "allowed_paths": sorted(RESUME_COMPATIBLE_OPERATIONAL_SOURCES),
                "scope": (
                    "post-launch aggregate-order recovery and independent parity audit; "
                    "collector, model, feature, seed, schema, and config hashes unchanged"
                ),
                "original_run_manifest_modified": False,
            }
        )
        _write_bytes_fsync(
            self.resume_amendments_path,
            _jsonl_bytes(records),
        )

    def _quarantine_staging(self) -> None:
        for path in sorted(self.staging_dir.iterdir()):
            destination = self.quarantine_dir / f"incomplete-{path.name}"
            suffix = 0
            while destination.exists():
                suffix += 1
                destination = self.quarantine_dir / f"incomplete-{path.name}-{suffix}"
            path.replace(destination)

    def completed_episode_ids(self) -> set[str]:
        completed: set[str] = set()
        for path in self.episodes_dir.iterdir():
            if not path.is_dir():
                continue
            if (path / "COMMITTED").is_file():
                completed.add(path.name)
        return completed

    def _recovery_episode_dirs(self) -> list[Path]:
        committed = {
            path.name: path
            for path in self.episodes_dir.iterdir()
            if path.is_dir() and (path / "COMMITTED").is_file()
        }
        ordered_ids: list[str] = []
        if self.summaries_path.is_file():
            for line in self.summaries_path.read_text().splitlines():
                if not line.strip():
                    continue
                episode_id = str(json.loads(line)["episode_id"])
                if episode_id in ordered_ids:
                    raise RuntimeError(f"duplicate aggregate summary: {episode_id}")
                if episode_id not in committed:
                    raise RuntimeError(
                        f"aggregate summary references uncommitted episode: {episode_id}"
                    )
                ordered_ids.append(episode_id)
        ordered_ids.extend(sorted(set(committed) - set(ordered_ids)))
        return [committed[episode_id] for episode_id in ordered_ids]

    def _recover_aggregate_indexes_if_needed(self) -> None:
        episode_dirs = self._recovery_episode_dirs()
        seen_rows: set[tuple[str, int]] = set()
        rows_digest = hashlib.sha256()
        rows_size = 0
        summaries_digest = hashlib.sha256()
        summaries_size = 0
        for episode_dir in episode_dirs:
            rows_file = episode_dir / "risk_rows.jsonl"
            summary_file = episode_dir / "summary.json"
            if not rows_file.is_file() or not summary_file.is_file():
                raise RuntimeError(f"incomplete committed episode: {episode_dir}")
            with rows_file.open("rb") as handle:
                for line in handle:
                    row = json.loads(line)
                    key = (str(row["episode_id"]), int(row["decision_index"]))
                    if key in seen_rows:
                        raise RuntimeError(f"duplicate decision row: {key}")
                    seen_rows.add(key)
                    validate_row(row)
                    rows_digest.update(line)
                    rows_size += len(line)
            summary_payload = (
                canonical_json(json.loads(summary_file.read_text())).encode("utf-8")
                + b"\n"
            )
            summaries_digest.update(summary_payload)
            summaries_size += len(summary_payload)

        if _file_identity(self.rows_path) != (rows_digest.hexdigest(), rows_size):
            _write_parts_fsync(
                self.rows_path,
                (
                    chunk
                    for episode_dir in episode_dirs
                    for chunk in _iter_file_chunks(episode_dir / "risk_rows.jsonl")
                ),
            )
        if _file_identity(self.summaries_path) != (
            summaries_digest.hexdigest(),
            summaries_size,
        ):
            _write_parts_fsync(
                self.summaries_path,
                (
                    canonical_json(
                        json.loads((episode_dir / "summary.json").read_text())
                    ).encode("utf-8")
                    + b"\n"
                    for episode_dir in episode_dirs
                ),
            )
        self._recover_error_index()

    def _authoritative_error_records(self) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for episode_dir in sorted(self.errors_dir.iterdir()):
            if not episode_dir.is_dir():
                continue
            for record_path in sorted(episode_dir.glob("attempt_*.json")):
                record = json.loads(record_path.read_text())
                if str(record.get("source_episode_id_padded")) != episode_dir.name:
                    raise RuntimeError(f"error record identity mismatch: {record_path}")
                records.append(record)
        return records

    def _recover_error_index(self) -> None:
        expected = _jsonl_bytes(self._authoritative_error_records())
        actual = self.errors_path.read_bytes() if self.errors_path.exists() else b""
        if actual != expected:
            _write_bytes_fsync(self.errors_path, expected)

    def next_error_attempt(self, source_episode_id: int) -> int:
        episode_dir = self.errors_dir / f"{int(source_episode_id):06d}"
        if not episode_dir.exists():
            return 1
        attempts = [
            int(path.stem.removeprefix("attempt_"))
            for path in episode_dir.glob("attempt_*.json")
        ]
        return max(attempts, default=0) + 1

    def record_episode_error(self, record: dict[str, Any]) -> Path:
        source_episode_id = int(record["source_episode_id"])
        attempt = int(record["attempt"])
        if attempt <= 0:
            raise ValueError("error attempt must be positive")
        episode_id = f"{source_episode_id:06d}"
        payload = {
            **record,
            "source_episode_id": source_episode_id,
            "source_episode_id_padded": episode_id,
            "attempt": attempt,
            "training_rows_written": False,
            "risk_label_written": False,
        }
        episode_dir = self.errors_dir / episode_id
        episode_dir.mkdir(parents=True, exist_ok=True)
        episode_dir.chmod(0o755)
        destination = episode_dir / f"attempt_{attempt:06d}.json"
        if destination.exists():
            raise RuntimeError(f"error attempt already recorded: {destination}")
        write_json_atomic(destination, payload)
        self._recover_error_index()
        return destination

    def finalize_episode(
        self,
        episode_id: str,
        rows: list[dict[str, Any]],
        summary: dict[str, Any],
    ) -> Path:
        if not episode_id or "/" in episode_id:
            raise ValueError("invalid episode_id")
        destination = self.episodes_dir / episode_id
        if destination.exists():
            raise RuntimeError(f"episode already finalized: {episode_id}")
        if not rows:
            raise ValueError("cannot finalize an episode without decision rows")

        seen_decisions: set[int] = set()
        for row in rows:
            if row.get("episode_id") != episode_id:
                raise ValueError("row episode_id does not match finalization target")
            decision = int(row["decision_index"])
            if decision in seen_decisions:
                raise ValueError(f"duplicate decision index {decision}")
            seen_decisions.add(decision)
            validate_row(row)
        if seen_decisions != set(range(len(rows))):
            raise ValueError("decision indices must be contiguous from zero")
        if str(summary.get("episode_id")) != episode_id:
            raise ValueError("summary episode_id mismatch")

        stage = self.staging_dir / f"{episode_id}.{os.getpid()}"
        stage.mkdir()
        stage.chmod(0o755)
        rows_payload = _jsonl_bytes(rows)
        _write_bytes_fsync(stage / "risk_rows.jsonl", rows_payload)
        write_json_atomic(stage / "summary.json", summary)
        write_json_atomic(
            stage / "validation.json",
            {
                "episode_id": episode_id,
                "decision_rows": len(rows),
                "rows_sha256": hashlib.sha256(rows_payload).hexdigest(),
                "validated": True,
            },
        )
        _write_bytes_fsync(stage / "COMMITTED", b"committed\n")
        stage.replace(destination)
        destination.chmod(0o755)
        dir_fd = os.open(self.episodes_dir, os.O_RDONLY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)

        with self.rows_path.open("ab") as handle:
            handle.write(rows_payload)
            handle.flush()
            os.fsync(handle.fileno())
        self.rows_path.chmod(0o644)
        with self.summaries_path.open("ab") as handle:
            handle.write(
                canonical_json(summary).encode("utf-8")
                + b"\n"
            )
            handle.flush()
            os.fsync(handle.fileno())
        self.summaries_path.chmod(0o644)
        return destination

    def update_status(self, payload: dict[str, Any]) -> None:
        write_json_atomic(self.status_path, payload)

    def stop_after_current_episode_requested(self) -> bool:
        return self.stop_marker_path.is_file()

    def discard_uncommitted_episode(self, episode_id: str) -> None:
        for stage in self.staging_dir.glob(f"{episode_id}.*"):
            destination = self.quarantine_dir / f"failed-{stage.name}"
            if destination.exists():
                shutil.rmtree(destination)
            stage.replace(destination)
