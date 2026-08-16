#!/usr/bin/env python3
"""Losslessly compact an audited round without retaining its aggregate duplicate."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


WORKSPACE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKSPACE / "src"))

from risk_collection.storage import authoritative_episode_dirs  # noqa: E402


ZSTD_COMMAND = ["zstd", "-q", "-T0", "-19", "--long=27"]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decompressed_identity(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    process = subprocess.Popen(["zstd", "-q", "-dc", str(path)], stdout=subprocess.PIPE)
    assert process.stdout is not None
    for chunk in iter(lambda: process.stdout.read(1024 * 1024), b""):
        digest.update(chunk)
        size += len(chunk)
    rc = process.wait()
    if rc:
        raise RuntimeError(f"zstd verification failed rc={rc}: {path}")
    return digest.hexdigest(), size


def reconstructed_identity(paths: list[Path]) -> tuple[str, int]:
    """Hash the exact concatenation represented by compressed episode streams."""
    digest = hashlib.sha256()
    size = 0
    for path in paths:
        process = subprocess.Popen(
            ["zstd", "-q", "-dc", str(path)], stdout=subprocess.PIPE
        )
        assert process.stdout is not None
        for chunk in iter(lambda: process.stdout.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
        rc = process.wait()
        if rc:
            raise RuntimeError(f"zstd reconstruction failed rc={rc}: {path}")
    return digest.hexdigest(), size


def fsync_directory(path: Path) -> None:
    directory_fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def compress_one(path: Path) -> dict[str, Any]:
    destination = path.with_suffix(path.suffix + ".zst")
    if destination.is_file() and not path.exists():
        digest, size = decompressed_identity(destination)
        return {
            "source_path": str(path),
            "compressed_path": str(destination),
            "uncompressed_bytes": size,
            "uncompressed_sha256": digest,
            "compressed_bytes": destination.stat().st_size,
            "compressed_sha256": sha256_file(destination),
            "reused_verified_stream": True,
        }
    if not path.is_file():
        raise FileNotFoundError(path)
    source_hash = sha256_file(path)
    source_size = path.stat().st_size
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    subprocess.run(
        [*ZSTD_COMMAND, "-f", str(path), "-o", str(temporary)],
        check=True,
    )
    decoded_hash, decoded_size = decompressed_identity(temporary)
    if decoded_hash != source_hash or decoded_size != source_size:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(f"zstd round-trip mismatch: {path}")
    temporary.replace(destination)
    fsync_directory(destination.parent)
    compressed_hash = sha256_file(destination)
    compressed_size = destination.stat().st_size
    path.unlink()
    return {
        "source_path": str(path),
        "compressed_path": str(destination),
        "uncompressed_bytes": source_size,
        "uncompressed_sha256": source_hash,
        "compressed_bytes": compressed_size,
        "compressed_sha256": compressed_hash,
        "reused_verified_stream": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("round_root", type=Path)
    args = parser.parse_args()
    root = args.round_root.resolve()
    report_dir = root / "reports"
    audit_path = report_dir / "exhaustive_audit.json"
    summary_path = report_dir / "round_audit_summary.json"
    manifest_path = report_dir / "lossless_zstd_manifest.json"
    reconstruction_path = report_dir / "aggregate_reconstruction.json"
    marker = report_dir / "ROUND_ROWS_COMPRESSED"
    if marker.is_file():
        print(manifest_path.read_text())
        return 0
    audit = json.loads(audit_path.read_text())
    summary = json.loads(summary_path.read_text())
    if not audit.get("pass") or not summary.get("exhaustive_audit_pass"):
        raise RuntimeError("round must pass exhaustive audit before compression")
    aggregate = root / "risk_receding_samples.jsonl"
    aggregate_compressed = aggregate.with_suffix(aggregate.suffix + ".zst")
    episode_dirs = authoritative_episode_dirs(root)
    targets = [path / "risk_rows.jsonl" for path in episode_dirs]
    if len(targets) != int(summary["valid_episodes"]):
        raise RuntimeError("round episode count does not match its audited summary")
    if any(
        not path.is_file()
        and not path.with_suffix(path.suffix + ".zst").is_file()
        for path in targets
    ):
        raise RuntimeError("round has a missing episode row payload")

    expected_aggregate_hash = str(audit["aggregate_rows_sha256"])
    reconstruction = (
        json.loads(reconstruction_path.read_text())
        if reconstruction_path.is_file()
        else None
    )
    if aggregate.is_file():
        aggregate_hash = sha256_file(aggregate)
        aggregate_size = aggregate.stat().st_size
    elif aggregate_compressed.is_file():
        aggregate_hash, aggregate_size = decompressed_identity(aggregate_compressed)
    elif reconstruction is not None:
        aggregate_hash = str(reconstruction["aggregate_sha256"])
        aggregate_size = int(reconstruction["aggregate_bytes"])
    else:
        raise RuntimeError("aggregate disappeared without a reconstruction manifest")
    if aggregate_hash != expected_aggregate_hash:
        raise RuntimeError(
            "aggregate hash no longer matches the exhaustive audit: "
            f"actual={aggregate_hash} expected={expected_aggregate_hash}"
        )

    records = []
    started = time.time()
    for index, path in enumerate(targets, start=1):
        records.append(compress_one(path))
        if index % 100 == 0:
            print(f"COMPRESSED_FILES={index}/{len(targets)}", flush=True)

    compressed_paths = [Path(item["compressed_path"]) for item in records]
    rebuilt_hash, rebuilt_size = reconstructed_identity(compressed_paths)
    if rebuilt_hash != aggregate_hash or rebuilt_size != aggregate_size:
        raise RuntimeError(
            "compressed episode streams do not reconstruct the audited aggregate: "
            f"hash={rebuilt_hash}/{aggregate_hash} size={rebuilt_size}/{aggregate_size}"
        )

    reconstruction = {
        "schema_version": "simvla_aggregate_reconstruction_v1",
        "aggregate_logical_path": str(aggregate),
        "aggregate_sha256": aggregate_hash,
        "aggregate_bytes": aggregate_size,
        "concatenation_order": [
            str(path.relative_to(root)) for path in compressed_paths
        ],
        "episode_stream_count": len(compressed_paths),
        "reconstruction_verified": True,
    }
    reconstruction_tmp = reconstruction_path.with_suffix(".tmp")
    reconstruction_tmp.write_text(json.dumps(reconstruction, indent=2) + "\n")
    reconstruction_tmp.replace(reconstruction_path)
    fsync_directory(report_dir)

    aggregate_physical_bytes = sum(
        path.stat().st_size
        for path in (aggregate, aggregate_compressed)
        if path.is_file()
    )
    aggregate.unlink(missing_ok=True)
    aggregate_compressed.unlink(missing_ok=True)
    fsync_directory(root)

    unique_uncompressed_bytes = sum(item["uncompressed_bytes"] for item in records)
    compressed_bytes = sum(item["compressed_bytes"] for item in records)
    report = {
        "schema_version": "simvla_audited_round_lossless_zstd_v2",
        "round_root": str(root),
        "exhaustive_audit_sha256": sha256_file(audit_path),
        "round_summary_sha256": sha256_file(summary_path),
        "compression": "zstd level 19, long window 27, multithreaded",
        "streaming_loader_required": True,
        "authoritative_storage": "per-episode compressed row streams",
        "aggregate_elided_as_exact_duplicate": True,
        "aggregate_reconstruction_manifest": str(reconstruction_path),
        "aggregate_sha256": aggregate_hash,
        "aggregate_bytes": aggregate_size,
        "aggregate_physical_bytes_reclaimed": aggregate_physical_bytes,
        "files": records,
        "uncompressed_bytes": unique_uncompressed_bytes,
        "compressed_bytes": compressed_bytes,
        "compression_ratio": unique_uncompressed_bytes / max(1, compressed_bytes),
        "elapsed_seconds": time.time() - started,
        "all_decompression_hashes_verified": True,
        "aggregate_reconstruction_verified": True,
    }
    temporary = manifest_path.with_suffix(".tmp")
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    temporary.replace(manifest_path)
    fsync_directory(report_dir)
    marker.write_text("verified\n")
    fsync_directory(report_dir)
    print(
        json.dumps(
            {
                "schema_version": report["schema_version"],
                "files": len(records),
                "uncompressed_bytes": unique_uncompressed_bytes,
                "compressed_bytes": compressed_bytes,
                "compression_ratio": report["compression_ratio"],
                "aggregate_physical_bytes_reclaimed": aggregate_physical_bytes,
                "aggregate_reconstruction_verified": True,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
