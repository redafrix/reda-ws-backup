import ast
from pathlib import Path
from unittest import TestCase


COLLECT_SCRIPT = Path("scripts/collect.py")


def main_call_order() -> list[str]:
    module = ast.parse(COLLECT_SCRIPT.read_text(encoding="utf-8"))
    main_function = next(
        node
        for node in module.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    )
    calls = (
        node
        for statement in main_function.body
        for node in ast.walk(statement)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    )
    return [call.func.id for call in calls]


class TestCollectEntrypoint(TestCase):
    def test_preflights_run_before_app_launcher(self) -> None:
        calls = main_call_order()
        required_calls = [
            "parse_args",
            "load_yaml_config",
            "preflight_collection_output",
            "validate_collection_config",
            "AppLauncher",
        ]

        self.assertEqual(
            [call for call in calls if call in required_calls],
            required_calls,
        )

    def test_fabric_render_transform_reads_are_disabled_by_default(self) -> None:
        source = COLLECT_SCRIPT.read_text(encoding="utf-8")

        self.assertIn('FABRIC_RENDER_TRANSFORM_SETTING = "/rtx/hydra/readTransformsFromFabricInRenderDelegate"', source)
        self.assertIn('f"--{FABRIC_RENDER_TRANSFORM_SETTING}=false"', source)
        self.assertIn("allow_fabric_render_transforms", source)

    def test_camera_collection_can_shard_by_process_before_app_launcher(self) -> None:
        source = COLLECT_SCRIPT.read_text(encoding="utf-8")

        self.assertIn("run_process_sharded_collections", source)
        self.assertIn("subprocess.Popen", source)
        self.assertIn("start_new_session=True", source)
        self.assertIn("_terminate_child_process_group", source)
        self.assertIn("disable_collection_sharding", source)
        self.assertIn("SKIP_COLLECTION_MANIFEST_KEY", source)
