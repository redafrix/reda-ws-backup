"""Relative paths resolution, config path helpers, and dataset output path builders."""

from __future__ import annotations

from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]


def get_config_path(config_name: str) -> Path:
    """Return the absolute path for a config name or repo-relative config path."""
    config_path = Path(config_name)
    if config_path.is_absolute():
        return config_path
    if config_path.parts[:1] == ("configs",):
        return REPO_ROOT / config_path
    return REPO_ROOT / "configs" / config_path


def load_yaml_config(config_name: str) -> dict:
    """Load and return a YAML configuration file as a dict."""
    config_path = get_config_path(config_name)
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
