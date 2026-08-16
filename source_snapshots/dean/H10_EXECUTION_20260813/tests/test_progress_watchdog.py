from __future__ import annotations

import importlib.util
import json
import signal
from pathlib import Path
import sys
import tempfile
import textwrap
import unittest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "automation"
    / "run_with_progress_watchdog.py"
)
SPEC = importlib.util.spec_from_file_location("progress_watchdog", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ProgressWatchdogTest(unittest.TestCase):
    def test_zero_exit_requires_durable_terminal_status(self) -> None:
        rc, error = MODULE.effective_collector_return_code(0, {})
        self.assertEqual(rc, 125)
        self.assertIn("without a durable terminal status", error or "")
        self.assertEqual(
            MODULE.effective_collector_return_code(0, {"state": "complete"}),
            (0, None),
        )
        self.assertEqual(
            MODULE.effective_collector_return_code(
                0, {"state": "paused_after_current_episode"}
            ),
            (0, None),
        )

    def test_nonzero_exit_is_preserved(self) -> None:
        self.assertEqual(
            MODULE.effective_collector_return_code(17, {"state": "complete"}),
            (17, None),
        )

    def test_native_style_signal_wedge_has_bounded_sigkill_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            child = Path(temp_dir) / "ignore.py"
            child.write_text(
                textwrap.dedent(
                    """
                    import signal, time
                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                    signal.signal(signal.SIGTERM, signal.SIG_IGN)
                    while True:
                        time.sleep(1)
                    """
                )
            )
            process = MODULE.subprocess.Popen(
                [sys.executable, str(child)], start_new_session=True
            )
            # Allow the child to install both handlers before signaling it.
            MODULE.time.sleep(0.1)
            return_code, forced = MODULE.terminate_process_group(
                process, interrupt_grace_s=0.1, term_grace_s=0.1
            )
            self.assertTrue(forced)
            self.assertEqual(return_code, -signal.SIGKILL)

    def test_stalled_child_is_restarted_and_atomic_progress_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            child = root / "child.py"
            status = root / "live_status.json"
            attempts = root / "attempts.txt"
            events = root / "events.jsonl"
            watchdog_status = root / "watchdog.json"
            child.write_text(
                textwrap.dedent(
                    """
                    import json, pathlib, sys, time
                    status, attempts = map(pathlib.Path, sys.argv[1:])
                    attempt = int(attempts.read_text()) + 1 if attempts.exists() else 1
                    attempts.write_text(str(attempt))
                    status.write_text(json.dumps({"completed_episodes": 3, "current_source_episode_id": 7, "attempt": attempt}))
                    if attempt == 1:
                        time.sleep(30)
                    status.write_text(json.dumps({"completed_episodes": 4, "state": "complete"}))
                    """
                )
            )
            args = MODULE.argparse.Namespace(
                status=status,
                events=events,
                watchdog_status=watchdog_status,
                stall_seconds=0.3,
                poll_seconds=0.05,
                interrupt_grace_seconds=0.5,
                term_grace_seconds=0.5,
                max_stall_restarts=2,
                command=[sys.executable, str(child), str(status), str(attempts)],
            )
            self.assertEqual(MODULE.run(args), 0)
            self.assertEqual(attempts.read_text(), "2")
            event_rows = [json.loads(line) for line in events.read_text().splitlines()]
            self.assertEqual(
                [row["event"] for row in event_rows],
                ["collector_stall_detected", "collector_stall_process_stopped"],
            )
            self.assertTrue(
                all(not row["training_rows_written"] for row in event_rows)
            )
            self.assertTrue(all(not row["risk_label_written"] for row in event_rows))
            self.assertEqual(json.loads(status.read_text())["completed_episodes"], 4)


if __name__ == "__main__":
    unittest.main()
