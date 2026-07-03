import json
import tempfile
import unittest
from pathlib import Path

from franka_wrist_camera_scene.simvla.language_audit import audit_episode_prompts, audit_verified_episode_prompts


class LanguageAuditTests(unittest.TestCase):
    def test_accepts_clean_reaching_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "000001"
            episode_dir.mkdir()
            (episode_dir / "meta.json").write_text(
                json.dumps({"instruction": "reach the avocado", "object_label": "avocado"}),
                encoding="utf-8",
            )

            findings = audit_episode_prompts([Path(tmp)])

        self.assertEqual(findings, [])

    def test_rejects_asset_suffix_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "000001"
            episode_dir.mkdir()
            (episode_dir / "meta.json").write_text(
                json.dumps({"instruction": "reach the avocado_1", "object_label": "avocado_1"}),
                encoding="utf-8",
            )

            findings = audit_episode_prompts([Path(tmp)])

        self.assertGreaterEqual(len(findings), 1)
        self.assertTrue(any(finding.reason == "asset_suffix_like_token" for finding in findings))

    def test_reports_bad_meta_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "000001"
            episode_dir.mkdir()
            (episode_dir / "meta.json").write_text("", encoding="utf-8")

            findings = audit_episode_prompts([Path(tmp)])

        self.assertEqual(len(findings), 1)
        self.assertTrue(findings[0].reason.startswith("bad_meta_json:"))

    def test_audits_raw_exact_report_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            episode_dir = Path(tmp) / "000001"
            episode_dir.mkdir()
            (episode_dir / "meta.json").write_text(
                json.dumps({"instruction": "reach the avocado", "object_label": "avocado"}),
                encoding="utf-8",
            )
            report_path = Path(tmp) / "raw_exact_verification_report.json"
            report_path.write_text(
                json.dumps(
                    {
                        "files": [
                            {
                                "path": "/tmp/shard.hdf5",
                                "verified_demos": [{"source_episode_path": str(episode_dir)}],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            findings = audit_verified_episode_prompts(report_path)

        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
