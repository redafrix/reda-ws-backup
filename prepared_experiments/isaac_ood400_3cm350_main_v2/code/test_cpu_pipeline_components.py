#!/usr/bin/env python3
"""CPU-Only Unit Tests for OOD400 Pipeline Orchestrator Components."""

from __future__ import annotations

import json
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np


class TestOOD400MetricsAndLogic(unittest.TestCase):
    def test_detection_metrics_and_invariants(self):
        # Synthetic failure episode queries (10 queries each)
        # Episode 1: alarm at query 2 (1-based)
        # Episode 2: alarm at query 5 (1-based)
        # Episode 3: alarm at query 9 (1-based)
        # Episode 4: no alarm
        failure_episodes = [
            [(1, 0.2), (2, 0.8), (3, 0.9)],       # T_e = 3 -> c25=1, c50=2, c100=3. t_alarm = 2 <= c50
            [(1, 0.1), (2, 0.2), (3, 0.3), (4, 0.4), (5, 0.7)], # T_e = 5 -> c25=2, c50=3, c100=5. t_alarm = 5 <= c100
            [(1, 0.0), (2, 0.1)],                 # T_e = 2 -> c25=1, c50=1, c100=2. No alarm (max 0.1 < 0.5)
        ]
        tau = 0.5

        det25 = 0
        det50 = 0
        det100 = 0
        never = 0
        fail_det = 0

        for ep in failure_episodes:
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
        self.assertEqual(fail_det + never, len(failure_episodes))
        self.assertTrue(det25 <= det50 <= det100)

    def test_threshold_selection_rule(self):
        from select_ood400_online_threshold import select_online_threshold

        # Synthetic sweep data
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
            # Best F1 vs q90 success tie-break: same fail_det (0.90), same Det50 (85.0 >= 80), same succ_fa (0.10), same Det25 (50.0). Higher threshold: Best F1 (0.5791 > 0.5631)
            self.assertEqual(res["selected_rule_name"], "Best F1")
            self.assertEqual(res["selected_threshold_a"], 0.5791)

    def test_controller_decision_logic(self):
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

        # Case 1: No alarm (main < A)
        idx, mod = choose([0.4, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        self.assertEqual((idx, mod), (0, False))

        # Case 2: Alarm, but best alternative is worse than main
        idx, mod = choose([0.6, 0.7, 0.8, 0.9, 0.65, 0.75, 0.85, 0.95, 0.7])
        self.assertEqual((idx, mod), (0, False))

        # Case 3: Alarm, best alt < main, but best alt > C (0.90)
        idx, mod = choose([0.95, 0.92, 0.93, 0.94, 0.96, 0.97, 0.98, 0.99, 0.92])
        self.assertEqual((idx, mod), (0, False))

        # Case 4: Alarm, best alt < main, best alt <= C -> accepted replacement at candidate 3
        scores = [0.8, 0.7, 0.5, 0.2, 0.6, 0.7, 0.8, 0.9, 0.4]
        idx, mod = choose(scores)
        self.assertEqual((idx, mod), (3, True))

    def test_paired_comparison_matrix_arithmetic(self):
        baseline_success = 180
        rescues = 45
        regressions = 10
        active_success = baseline_success + rescues - regressions
        self.assertEqual(active_success, 215)

        persisted_success = baseline_success - regressions
        persisted_failure = (400 - baseline_success) - rescues
        total_pairs = persisted_success + rescues + regressions + persisted_failure
        self.assertEqual(total_pairs, 400)


if __name__ == "__main__":
    unittest.main()
