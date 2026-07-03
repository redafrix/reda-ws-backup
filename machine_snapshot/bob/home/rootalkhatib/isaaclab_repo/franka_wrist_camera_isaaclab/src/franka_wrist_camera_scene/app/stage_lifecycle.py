"""Isaac Sim lifecycle helpers for collection scripts."""

from __future__ import annotations

import isaaclab.sim as sim_utils


def clear_simulation_context(sim: sim_utils.SimulationContext) -> None:
    sim._disable_app_control_on_stop_handle = True
    try:
        sim.stop()
    finally:
        sim._disable_app_control_on_stop_handle = False
    if hasattr(sim, "clear_all_callbacks"):
        sim.clear_all_callbacks()
    sim.clear_instance()
