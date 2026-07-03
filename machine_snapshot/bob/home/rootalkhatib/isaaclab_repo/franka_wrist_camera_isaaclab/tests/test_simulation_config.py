import importlib
import sys
from types import ModuleType
from unittest import TestCase
from unittest.mock import patch


class DummyPhysxCfg:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DummySimulationCfg:
    __dataclass_fields__ = {"physics": object(), "use_fabric": object()}

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DummySimModule(ModuleType):
    def __init__(self):
        super().__init__("isaaclab.sim")
        self.SimulationCfg = DummySimulationCfg
        self.PhysxCfg = DummyPhysxCfg
        self.RenderCfg = lambda **kwargs: kwargs


class TestSimulationConfig(TestCase):
    def _load_module(self):
        sys.modules.pop("franka_wrist_camera_scene.app.simulation_config", None)
        isaaclab = ModuleType("isaaclab")
        sim = DummySimModule()
        isaaclab.sim = sim
        with patch.dict(sys.modules, {"isaaclab": isaaclab, "isaaclab.sim": sim}):
            return importlib.import_module("franka_wrist_camera_scene.app.simulation_config")

    def test_simulation_cfg_keeps_fabric_enabled_by_default(self) -> None:
        module = self._load_module()

        cfg = module.make_simulation_cfg("cuda:0")

        self.assertTrue(cfg.kwargs["use_fabric"])
        self.assertEqual(cfg.kwargs["device"], "cuda:0")
        self.assertEqual(
            cfg.kwargs["render"]["carb_settings"][module.FABRIC_RENDER_TRANSFORM_SETTING],
            False,
        )

    def test_simulation_cfg_allows_explicit_fabric_override(self) -> None:
        module = self._load_module()

        cfg = module.make_simulation_cfg("cuda:0", use_fabric=False)

        self.assertFalse(cfg.kwargs["use_fabric"])
