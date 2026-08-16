from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from risk_collection.constants import (
    ACTIONS_PER_REPLAN,
    EXECUTION_MODE,
    MAX_CONTROL_TICKS,
    MAX_DECISION_ROWS,
)
from risk_collection.parity_audit import validate_h10_executed_sequence


WORKSPACE = Path(__file__).resolve().parents[1]


def test_h10_timing_invariants() -> None:
    assert EXECUTION_MODE == "chunk_h10"
    assert ACTIONS_PER_REPLAN == 10
    assert MAX_CONTROL_TICKS == 600
    assert MAX_DECISION_ROWS == 60


def test_full_h10_sequence_equals_main_chunk() -> None:
    main = np.arange(70, dtype=np.float32).reshape(10, 7)
    assert validate_h10_executed_sequence(main[0], main.copy(), main) == 0.0


def test_terminal_success_may_execute_a_strict_prefix() -> None:
    main = np.arange(70, dtype=np.float32).reshape(10, 7)
    assert validate_h10_executed_sequence(main[0], main[:4].copy(), main) == 0.0


def test_h1_or_non_prefix_execution_is_rejected() -> None:
    main = np.arange(70, dtype=np.float32).reshape(10, 7)
    bad = main[:1].copy()
    bad[0, 0] += 1.0
    with pytest.raises(RuntimeError):
        validate_h10_executed_sequence(bad[0], bad, main)


def test_production_launchers_cannot_request_h1() -> None:
    launchers = [
        WORKSPACE / "automation/run_production_round_stage.sh",
        WORKSPACE / "automation/run_locked_ood150_stage.sh",
    ]
    for launcher in launchers:
        text = launcher.read_text()
        assert "--execution-mode chunk_h10" in text
        assert "receding_h1" not in text


def test_round_zero_supervisor_distinguishes_start_from_resume() -> None:
    source = (WORKSPACE / "automation/pipeline_supervisor.py").read_text()
    assert 'action = "resume" if (root / "run_manifest.json").is_file() else "start"' in source
    assert '"paused_after_current_episode"' in source


def test_post_round0_chain_is_h10_only_and_builds_hard1000() -> None:
    hard = (WORKSPACE / "automation/hard1000_pipeline.py").read_text()
    handoff = (WORKSPACE / "automation/handoff_first_cycle_to_hard1000.sh").read_text()
    assert "simvla_isaac_risk_collection_H10_EXECUTION_20260813" in hard
    assert "isaac_seen_h10_topk8_v2_round0_hard1000" in hard
    assert "isaac_h10_topk8_temporal_v2_round0_hard1000" in hard
    assert '"--episodes"' in hard
    assert '"1000"' in hard
    assert "ensure_hard_candidate_pool()" in hard
    assert "generate_official_seen_round.py" in hard
    assert "STOP_PIPELINE_AFTER_CURRENT_EPISODE" in handoff
    assert "hard1000_pipeline_tmux.sh" in handoff
    assert "receding_h1" not in hard
    assert "receding_h1" not in handoff


def test_primary_supervisor_explicitly_hands_off_instead_of_collecting_forever() -> None:
    source = (WORKSPACE / "automation/pipeline_supervisor.py").read_text()
    assert 'hard1000_pipeline_tmux.sh"), "ensure"' in source
    assert "first_train_and_locked_eval_complete_handed_off_to_hard1000" in source
    main_body = source[source.index("def main()") :]
    assert "continuous_collection()" not in main_body


def test_external_round_stage_blocks_old_supervisor_broad_round_race() -> None:
    source = (WORKSPACE / "automation/run_production_round_stage.sh").read_text()
    assert "FIRST_RISK_TRAIN_AND_LOCKED_EVAL_COMPLETE" in source
    assert '"$ROUND_KIND" == broad' in source
    assert '"$ROUND_ID" != 0' in source
    assert "blocked_by_hard1000_handoff" in source
