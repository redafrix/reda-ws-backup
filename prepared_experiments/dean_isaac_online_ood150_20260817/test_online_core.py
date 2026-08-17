import numpy as np
from online_isaac_runtime import select_argmin_on_alarm

def test_select_main_below_threshold():
    s = np.array([0.3, 0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], dtype=np.float32)
    d = select_argmin_on_alarm(s, main_threshold=0.5, selected_score_cap=0.2)
    assert d.selected_index == 0
    assert d.reason == "main_below_alarm_threshold"
    assert not d.proposed_modification

def test_select_main_is_lowest():
    s = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], dtype=np.float32)
    d = select_argmin_on_alarm(s, main_threshold=0.05, selected_score_cap=0.5)
    assert d.selected_index == 0
    assert d.reason == "main_is_lowest"
    assert not d.proposed_modification

def test_select_best_above_cap():
    s = np.array([0.8, 0.6, 0.7, 0.65, 0.75, 0.85, 0.9, 0.95, 0.99], dtype=np.float32)
    d = select_argmin_on_alarm(s, main_threshold=0.5, selected_score_cap=0.4)
    assert d.selected_index == 0
    assert d.reason == "best_alternative_above_cap"
    assert not d.proposed_modification

def test_select_intervention_pass():
    s = np.array([0.8, 0.6, 0.15, 0.65, 0.75, 0.85, 0.9, 0.95, 0.99], dtype=np.float32)
    d = select_argmin_on_alarm(s, main_threshold=0.5, selected_score_cap=0.3)
    assert d.selected_index == 2
    assert d.reason == "argmin_on_alarm_cap_pass"
    assert d.proposed_modification
    assert abs(d.selected_score - 0.15) < 1e-6
