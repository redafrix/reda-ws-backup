from pathlib import Path
from unittest import TestCase

from franka_wrist_camera_scene.utils.paths import REPO_ROOT, get_config_path


class TestConfigPaths(TestCase):
    def test_config_name_resolves_under_configs(self) -> None:
        self.assertEqual(get_config_path("collection.yaml"), REPO_ROOT / "configs" / "collection.yaml")

    def test_configs_relative_path_is_not_nested(self) -> None:
        self.assertEqual(get_config_path("configs/collection.yaml"), REPO_ROOT / "configs" / "collection.yaml")

    def test_absolute_config_path_is_preserved(self) -> None:
        path = Path("/tmp/example.yaml")
        self.assertEqual(get_config_path(str(path)), path)
