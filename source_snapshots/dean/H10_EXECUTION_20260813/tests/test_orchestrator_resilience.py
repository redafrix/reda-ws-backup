from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


WORKSPACE = Path("/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OrchestratorResilienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.hard = load_module(
            "hard1000_pipeline_test",
            WORKSPACE / "automation/hard1000_pipeline.py",
        )
        cls.supervisor = load_module(
            "pipeline_supervisor_test",
            WORKSPACE / "automation/pipeline_supervisor.py",
        )

    def test_completion_marker_requires_parseable_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "COMPLETE").write_text("complete\n")
            (root / "manifest.json").write_text('{"pass": true}\n')
            self.hard.require_complete_artifact(
                root, "COMPLETE", ("manifest.json",)
            )
            (root / "manifest.json").write_text("not-json\n")
            with self.assertRaises(json.JSONDecodeError):
                self.hard.require_complete_artifact(
                    root, "COMPLETE", ("manifest.json",)
                )

    def test_hard_round_retries_only_infrastructure_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            summary = root / "summary.json"
            audit = root / "audit.json"
            self.assertEqual(
                self.hard.hard_round_completion_state(summary, audit), "missing"
            )
            audit.write_text('{"pass": true}\n')
            summary.write_text(
                json.dumps(
                    {
                        "exhaustive_audit_pass": True,
                        "valid_episodes": 999,
                        "infrastructure_excluded_episodes": 1,
                    }
                )
            )
            self.assertEqual(
                self.hard.hard_round_completion_state(summary, audit),
                "recoverable_infrastructure_exclusion",
            )
            summary.write_text(
                json.dumps(
                    {
                        "exhaustive_audit_pass": True,
                        "valid_episodes": 1000,
                        "infrastructure_excluded_episodes": 0,
                    }
                )
            )
            self.assertEqual(
                self.hard.hard_round_completion_state(summary, audit), "complete"
            )

    def test_supervisor_requires_all_finalized_artifact_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "COMPLETE").write_text("complete\n")
            with self.assertRaises(RuntimeError):
                self.supervisor.require_complete_artifact(
                    root, "COMPLETE", ("results.json",)
                )

    def test_supervisors_have_stage_timeouts_and_completion_gates(self) -> None:
        hard_source = (WORKSPACE / "automation/hard1000_pipeline.py").read_text()
        supervisor_source = (WORKSPACE / "automation/pipeline_supervisor.py").read_text()
        self.assertIn("start_new_session=True", hard_source)
        self.assertIn("TRAINING_COMPLETE", hard_source)
        self.assertIn("LOCKED_OOD150_EVALUATION_COMPLETE", hard_source)
        self.assertIn("start_new_session=True", supervisor_source)
        self.assertIn("FROZEN_AND_VALIDATED", supervisor_source)
        self.assertIn("LOCKED_OOD150_EVALUATION_COMPLETE", supervisor_source)

    def test_audits_have_bounded_runtime(self) -> None:
        ood_stage = (WORKSPACE / "automation/run_locked_ood150_stage.sh").read_text()
        round_stage = (WORKSPACE / "automation/run_production_round_stage.sh").read_text()
        self.assertIn("timeout --signal=INT --kill-after=120s 4h", ood_stage)
        self.assertIn("timeout --signal=INT --kill-after=120s 4h", round_stage)
        self.assertIn("timeout --signal=INT --kill-after=120s 30m", round_stage)

    def test_hard_generator_emits_direct_source_provenance(self) -> None:
        generator = (WORKSPACE / "automation/generate_hard_seen_round.py").read_text()
        self.assertIn('"source_manifest": str(source_manifest)', generator)
        self.assertIn('"source_manifest_sha256": source_manifest_sha256', generator)


if __name__ == "__main__":
    unittest.main()
