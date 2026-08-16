from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

from risk_collection.schema import RowValidationError, validate_row
from risk_collection.smoke_safety import validate_forced_timeout_smoke_request
from risk_collection.storage import (
    EpisodeStore,
    authoritative_episode_dirs,
    verify_aggregate_indexes,
)


def valid_row(episode_id: str = "000001", decision: int = 0) -> dict:
    zeros_action = np.zeros(7, dtype=np.float32).tolist()
    zeros_chunk = np.zeros((10, 7), dtype=np.float32).tolist()
    return {
        "schema_version": "simvla_isaac_risk_collection_v1",
        "episode_id": episode_id,
        "decision_index": decision,
        "execution_mode": "chunk_h10",
        "main_seed": 1,
        "ace_candidate_seeds": list(range(2, 10)),
        "main_candidate_action_chunk_normalized": zeros_chunk,
        "main_candidate_action_chunk_env": zeros_chunk,
        "ace_candidate_chunks_normalized": np.zeros((8, 10, 7)).tolist(),
        "ace_candidate_chunks_env": np.zeros((8, 10, 7)).tolist(),
        "ace_features_7d": zeros_action,
        "executed_action": zeros_action,
        "executed_action_sequence": [zeros_action] * 10,
        "simvla_uncertainty_49d": np.zeros(49).tolist(),
        "simvla_uncertainty_delta_49d": np.zeros(49).tolist(),
        "simvla_uncertainty_raw": {"parameterization": "softplus_raw_variance"},
        "history": np.zeros((16, 21)).tolist(),
        "current": {"proprio": np.zeros(8).tolist()},
        "parent_episode_outcome": "success",
        "parent_episode_risk_label": 0,
        "metadata": {
            "checkpoint_model_sha256": "a" * 64,
            "uncertainty_parameterization": "softplus_raw_variance",
            "manifest_fingerprint_sha256": "b" * 64,
            "policy_sampling_seed": 1,
        },
    }


class StorageSchemaCpuTest(unittest.TestCase):
    def test_bundled_json_schema_contract(self) -> None:
        schema_path = (
            Path(__file__).resolve().parents[1]
            / "schemas"
            / "risk_collection_row.schema.json"
        )
        schema = json.loads(schema_path.read_text())
        row = valid_row()
        self.assertEqual(schema["properties"]["schema_version"]["const"], row["schema_version"])
        self.assertEqual(set(schema["required"]), set(row))
        self.assertEqual(schema["properties"]["execution_mode"]["const"], "chunk_h10")
        self.assertEqual(schema["$defs"]["action"]["minItems"], 7)
        self.assertEqual(schema["$defs"]["chunk"]["minItems"], 10)
        self.assertEqual(schema["$defs"]["candidates"]["minItems"], 8)
        self.assertEqual(schema["$defs"]["features49"]["minItems"], 49)

    def test_schema_accepts_exact_shapes(self) -> None:
        validate_row(valid_row())

    def test_schema_rejects_h1_execution(self) -> None:
        row = valid_row()
        row["execution_mode"] = "receding_h1"
        row["executed_action_sequence"] = row["executed_action_sequence"][:1]
        with self.assertRaises(RowValidationError):
            validate_row(row)

    def test_schema_rejects_duplicate_seed(self) -> None:
        row = valid_row()
        row["ace_candidate_seeds"][-1] = row["ace_candidate_seeds"][0]
        with self.assertRaises(RowValidationError):
            validate_row(row)

    def test_atomic_finalize_and_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = {"schema_version": "test", "seed": 1}
            store = EpisodeStore(root, manifest)
            row = valid_row()
            summary = {"episode_id": "000001", "success": True}
            destination = store.finalize_episode("000001", [row], summary)
            self.assertTrue((destination / "COMMITTED").is_file())
            self.assertEqual(store.completed_episode_ids(), {"000001"})

            resumed = EpisodeStore(root, manifest)
            self.assertEqual(resumed.completed_episode_ids(), {"000001"})
            rows = [
                json.loads(line)
                for line in resumed.rows_path.read_text().splitlines()
            ]
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["episode_id"], "000001")

    def test_round_robin_append_order_survives_audit_lookup_and_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = {"schema_version": "test", "seed": 1}
            store = EpisodeStore(root, manifest)
            append_order = ["000010", "000002", "000007"]
            for episode_id in append_order:
                store.finalize_episode(
                    episode_id,
                    [valid_row(episode_id)],
                    {"episode_id": episode_id, "success": True},
                )
            self.assertNotEqual(append_order, sorted(append_order))
            self.assertEqual(
                [path.name for path in authoritative_episode_dirs(root)], append_order
            )
            aggregate_identity = verify_aggregate_indexes(
                root, authoritative_episode_dirs(root)
            )
            self.assertGreater(aggregate_identity["aggregate_rows_bytes"], 0)
            aggregate_order = [
                json.loads(line)["episode_id"]
                for line in store.rows_path.read_text().splitlines()
            ]
            self.assertEqual(aggregate_order, append_order)

            EpisodeStore(root, manifest)
            self.assertEqual(
                [path.name for path in authoritative_episode_dirs(root)], append_order
            )
            resumed_aggregate_order = [
                json.loads(line)["episode_id"]
                for line in (root / "risk_receding_samples.jsonl").read_text().splitlines()
            ]
            self.assertEqual(resumed_aggregate_order, append_order)

    def test_manifest_mismatch_aborts(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            EpisodeStore(root, {"schema_version": "test", "seed": 1})
            with self.assertRaises(RuntimeError):
                EpisodeStore(root, {"schema_version": "test", "seed": 2})

    def test_resume_accepts_only_documented_operational_source_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            original = {
                "schema_version": "test",
                "seed": 1,
                "codebases": {
                    "isolated_workspace_source_sha256": {
                        "scripts/collect_isaac_risk.py": "collector",
                        "src/risk_collection/storage.py": "old-storage",
                    }
                },
            }
            EpisodeStore(root, original)
            resumed = copy.deepcopy(original)
            resumed["codebases"]["isolated_workspace_source_sha256"].update(
                {
                    "src/risk_collection/storage.py": "new-storage",
                    "src/risk_collection/parity_audit.py": "new-parity",
                }
            )
            store = EpisodeStore(root, resumed)
            records = [
                json.loads(line)
                for line in store.resume_amendments_path.read_text().splitlines()
            ]
            self.assertEqual(len(records), 1)
            self.assertFalse(records[0]["original_run_manifest_modified"])
            self.assertEqual(json.loads(store.manifest_path.read_text()), original)

            incompatible = copy.deepcopy(resumed)
            incompatible["codebases"]["isolated_workspace_source_sha256"][
                "src/risk_collection/features.py"
            ] = "changed-science"
            with self.assertRaises(RuntimeError):
                EpisodeStore(root, incompatible)

    def test_incomplete_staging_is_quarantined(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            store = EpisodeStore(root, {"schema_version": "test", "seed": 1})
            partial = store.staging_dir / "000001.fake"
            partial.mkdir()
            (partial / "partial").write_text("x")
            resumed = EpisodeStore(root, {"schema_version": "test", "seed": 1})
            self.assertFalse(partial.exists())
            self.assertTrue(any(resumed.quarantine_dir.iterdir()))

    def test_infrastructure_errors_are_atomic_and_not_training_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = {"schema_version": "test", "seed": 1}
            store = EpisodeStore(root, manifest)
            destination = store.record_episode_error(
                {
                    "schema_version": "simvla_isaac_risk_infrastructure_error_v1",
                    "source_episode_id": 6,
                    "attempt": 1,
                    "timestamp_utc": "2026-07-31T00:00:00+00:00",
                    "traceback": "example",
                }
            )
            self.assertTrue(destination.is_file())
            record = json.loads(destination.read_text())
            self.assertFalse(record["training_rows_written"])
            self.assertFalse(record["risk_label_written"])
            self.assertEqual(store.completed_episode_ids(), set())
            self.assertTrue(
                not store.rows_path.exists() or store.rows_path.read_bytes() == b""
            )
            self.assertEqual(store.next_error_attempt(6), 2)

            resumed = EpisodeStore(root, manifest)
            errors = [
                json.loads(line)
                for line in resumed.errors_path.read_text().splitlines()
            ]
            self.assertEqual(len(errors), 1)
            self.assertEqual(errors[0]["source_episode_id"], 6)

    def test_stop_after_current_episode_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            store = EpisodeStore(
                Path(temp), {"schema_version": "test", "seed": 1}
            )
            self.assertFalse(store.stop_after_current_episode_requested())
            store.stop_marker_path.write_text("stop\n")
            self.assertTrue(store.stop_after_current_episode_requested())

            smoke_root = Path(temp) / "smokes_timeout2400"
            validate_forced_timeout_smoke_request(
                enabled=True,
                output_dir=smoke_root / "forced",
                smoke_root=smoke_root,
                count=1,
                execution_mode="chunk_h10",
                inference_only=False,
                max_steps_override=None,
            )
            with self.assertRaises(ValueError):
                validate_forced_timeout_smoke_request(
                    enabled=True,
                    output_dir=Path(temp) / "production",
                    smoke_root=smoke_root,
                    count=1,
                    execution_mode="chunk_h10",
                    inference_only=False,
                    max_steps_override=None,
                )


if __name__ == "__main__":
    unittest.main()
