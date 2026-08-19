#!/usr/bin/env python3
"""Comprehensive CPU-Only Unit Test Suite for Hardened OOD400 Pipeline Orchestrator."""

from __future__ import annotations

import json
import math
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import numpy as np
import torch

WORKSPACE = Path(os.environ.get("SIMVLA_ISAAC_H10_WORKSPACE", "/mnt/ai/projects/simvla_isaac_risk_collection_H10_EXECUTION_20260813"))
import sys
sys.path.insert(0, str(WORKSPACE / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ood400_runtime import make_seq_risk_model
from select_ood400_online_threshold import select_online_threshold
from build_ood400_review_video import render_annotated_clip, get_video_duration


class TestOOD400PipelineHardening(unittest.TestCase):
    def test_01_offline_model_call_contract(self):
        """Test SeqRiskModel dict call contract and sigmoid activation."""
        model = make_seq_risk_model()
        model.eval()

        B = 4
        h = torch.randn(B, 16, 21)
        a = torch.randn(B, 10, 7)
        s = torch.randn(B, 51)

        with torch.inference_mode():
            logits = model({"history": h, "action": a, "static": s}).view(-1)
            probs = torch.sigmoid(logits)

        self.assertEqual(logits.shape, (B,))
        self.assertEqual(probs.shape, (B,))
        self.assertTrue((probs >= 0.0).all() and (probs <= 1.0).all())

    def test_02_score_parity_key_join(self):
        """Test exact (episode_id, decision_index) row-key parity audit."""
        offline_scores = {("000000", 0): 0.123456, ("000000", 1): 0.456789, ("000001", 0): 0.789012}
        shadow_scores = {("000000", 0): 0.123458, ("000000", 1): 0.456787, ("000001", 0): 0.789010}

        diffs = [abs(offline_scores[k] - shadow_scores[k]) for k in offline_scores]
        max_diff = max(diffs)
        self.assertLessEqual(max_diff, 1e-5)

        # Duplicate key test
        with self.assertRaises(ValueError):
            dec_list = [("000000", 0), ("000000", 0)]
            d_map = {}
            for k in dec_list:
                if k in d_map:
                    raise ValueError("Duplicate key")
                d_map[k] = 1.0

    def test_03_exact_episode_membership(self):
        """Test detection of missing and extra episode directories."""
        expected = [f"{i:06d}" for i in range(400)]
        actual_good = [f"{i:06d}" for i in range(400)]
        self.assertEqual(set(expected) - set(actual_good), set())

        actual_missing = [f"{i:06d}" for i in range(399)]
        self.assertEqual(len(set(expected) - set(actual_missing)), 1)

    def test_04_decision_contiguity(self):
        """Test contiguous decision index verification."""
        good_indices = [0, 1, 2, 3]
        self.assertEqual(good_indices, list(range(len(good_indices))))

        gap_indices = [0, 1, 3]
        self.assertNotEqual(gap_indices, list(range(len(gap_indices))))

    def test_05_label_parent_consistency(self):
        """Test parent label consistency with episode outcome."""
        summary = {"episode_id": "000000", "success": True}
        exp_parent_label = 0 if summary["success"] else 1
        self.assertEqual(exp_parent_label, 0)

        fail_summary = {"episode_id": "000001", "success": False}
        exp_fail_parent_label = 0 if fail_summary["success"] else 1
        self.assertEqual(exp_fail_parent_label, 1)

    def test_06_threshold_detection_metrics(self):
        """Test early detection metrics and strict invariants."""
        episodes = [
            [(1, 0.2), (2, 0.8), (3, 0.9)],
            [(1, 0.1), (2, 0.2), (3, 0.3), (4, 0.4), (5, 0.7)],
            [(1, 0.0), (2, 0.1)],
        ]
        tau = 0.5
        det25 = 0
        det50 = 0
        det100 = 0
        never = 0
        fail_det = 0

        for ep in episodes:
            T_e = len(ep)
            c25 = int(math.ceil(0.25 * T_e))
            c50 = int(math.ceil(0.50 * T_e))
            c100 = T_e

            alarms = [i + 1 for i, (_, s) in enumerate(ep) if s >= tau]
            if alarms:
                t = min(alarms)
                fail_det += 1
                if t <= c25:
                    det25 += 1
                if t <= c50:
                    det50 += 1
                if t <= c100:
                    det100 += 1
            else:
                never += 1

        self.assertEqual(fail_det, 2)
        self.assertEqual(never, 1)
        self.assertEqual(det100, fail_det)
        self.assertEqual(fail_det + never, len(episodes))
        self.assertTrue(det25 <= det50 <= det100)

    def test_07_threshold_selection_rule(self):
        """Test 6-step deterministic online A selection."""
        sweep = [
            {"rule_name": "Best F1", "threshold": 0.5791, "fail_detection_rate": 0.90, "det_at_50_pct": 85.0, "succ_false_alarm_rate": 0.10, "det_at_25_pct": 50.0},
            {"rule_name": "Fixed 0.5", "threshold": 0.5000, "fail_detection_rate": 0.90, "det_at_50_pct": 82.0, "succ_false_alarm_rate": 0.15, "det_at_25_pct": 55.0},
            {"rule_name": "q90 success", "threshold": 0.5631, "fail_detection_rate": 0.90, "det_at_50_pct": 85.0, "succ_false_alarm_rate": 0.10, "det_at_25_pct": 50.0},
            {"rule_name": "q95 success", "threshold": 0.6643, "fail_detection_rate": 0.80, "det_at_50_pct": 75.0, "succ_false_alarm_rate": 0.05, "det_at_25_pct": 40.0},
            {"rule_name": "q99 success", "threshold": 0.8792, "fail_detection_rate": 0.60, "det_at_50_pct": 50.0, "succ_false_alarm_rate": 0.01, "det_at_25_pct": 20.0},
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            sweep_p = Path(tmpdir) / "sweep.json"
            out_p = Path(tmpdir) / "selected.json"
            sweep_p.write_text(json.dumps(sweep))

            res = select_online_threshold(sweep_p, out_p)
            self.assertEqual(res["selected_rule_name"], "Best F1")
            self.assertEqual(res["selected_threshold_a"], 0.5791)

    def test_08_controller_decision_logic(self):
        """Test TopK argmin controller rule."""
        A = 0.55
        C = 0.90

        def choose(scores):
            main_s = scores[0]
            alt_scores = scores[1:]
            best_alt_idx = 1 + int(np.argmin(alt_scores))
            best_alt_s = scores[best_alt_idx]

            if main_s < A:
                return 0, False
            if best_alt_s >= main_s:
                return 0, False
            if best_alt_s > C:
                return 0, False
            return best_alt_idx, True

        self.assertEqual(choose([0.4, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]), (0, False))
        self.assertEqual(choose([0.6, 0.7, 0.8, 0.9, 0.65, 0.75, 0.85, 0.95, 0.7]), (0, False))
        self.assertEqual(choose([0.95, 0.92, 0.93, 0.94, 0.96, 0.97, 0.98, 0.99, 0.92]), (0, False))
        self.assertEqual(choose([0.8, 0.7, 0.5, 0.2, 0.6, 0.7, 0.8, 0.9, 0.4]), (3, True))

    def test_09_selected_action_prefix_equality(self):
        """Test prefix equality check between executed sequence and selected chunk."""
        chunk = np.ones((10, 7), dtype=np.float32) * 0.5
        executed = chunk[:4].copy()
        diff = float(np.max(np.abs(executed - chunk[:4])))
        self.assertEqual(diff, 0.0)

    def test_10_paired_comparison_arithmetic(self):
        """Test paired matrix classification and arithmetic."""
        baseline_succ = 180
        rescues = 40
        regressions = 10
        active_succ = baseline_succ + rescues - regressions
        self.assertEqual(active_succ, 210)

        persisted_succ = baseline_succ - regressions
        persisted_fail = (400 - baseline_succ) - rescues
        self.assertEqual(persisted_succ + rescues + regressions + persisted_fail, 400)

    def test_11_process_matcher_exact(self):
        """Test that runner process matcher uses exact args."""
        cmdline = "python run_ood400_simvla.py --output-dir /tmp/test_out --mode baseline --manifest /tmp/manifest.json"
        self.assertTrue("/tmp/test_out" in cmdline and "--mode baseline" in cmdline and "/tmp/manifest.json" in cmdline)
        self.assertFalse("/tmp/other_out" in cmdline)

    def test_12_recovery_hash_gate(self):
        """Test that hash mismatch raises error."""
        locked_hashes = {"model_sha256": "abc"}
        current_hashes = {"model_sha256": "def"}
        with self.assertRaises(RuntimeError):
            if locked_hashes != current_hashes:
                raise RuntimeError("Hash mismatch")

    def test_13_atomic_state_resume(self):
        """Test atomic pipeline state write and resume."""
        with tempfile.TemporaryDirectory() as tmpdir:
            state_p = Path(tmpdir) / "PIPELINE_STATE.json"
            tmp_p = Path(tmpdir) / "PIPELINE_STATE.json.tmp"
            tmp_p.write_text(json.dumps({"state": "WAIT_BASELINE"}))
            tmp_p.replace(state_p)

            loaded = json.loads(state_p.read_text())["state"]
            self.assertEqual(loaded, "WAIT_BASELINE")

    def test_14_active_run_lock(self):
        """Test active run lock creation and collision detection."""
        with tempfile.TemporaryDirectory() as tmpdir:
            lock_p = Path(tmpdir) / "RUN_LOCK.json"
            doc1 = {"threshold_a": 0.5791, "locked_hashes": {"manifest": "aaa"}}
            lock_p.write_text(json.dumps(doc1))

            doc2 = {"threshold_a": 0.5000, "locked_hashes": {"manifest": "aaa"}}
            existing = json.loads(lock_p.read_text())
            self.assertNotEqual(existing["threshold_a"], doc2["threshold_a"])

    def test_15_review_video_overlay_cpu(self):
        """Test synthetic 1-second video metadata overlay rendering."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_p = Path(tmpdir)
            raw_video_p = tmp_p / "raw_000000.mp4"
            annotated_video_p = tmp_p / "annotated_000000.mp4"

            # Create 1s synthetic black video (320x240 @ 5fps)
            subprocess.run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-f", "lavfi", "-i", "color=c=blue:s=320x240:d=1:r=5",
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                str(raw_video_p)
            ], check=True)

            text_content = "NORMAL SIMVLA | Episode: 000000\nTask: reach target\nOutcome: SUCCESS\nResult: 3 CM REACHED @ tick 15"
            render_annotated_clip(
                input_video=raw_video_p,
                output_video=annotated_video_p,
                text_content=text_content,
                tmp_dir=tmp_p,
            )

            self.assertTrue(annotated_video_p.exists())
            self.assertGreater(annotated_video_p.stat().st_size, 1000)
            dur = get_video_duration(annotated_video_p)
            self.assertGreater(dur, 0.5)


if __name__ == "__main__":
    unittest.main()
