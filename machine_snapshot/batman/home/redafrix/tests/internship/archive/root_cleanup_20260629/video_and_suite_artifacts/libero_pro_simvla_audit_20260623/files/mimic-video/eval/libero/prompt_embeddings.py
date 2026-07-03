"""Prompt helpers for LIBERO text embedding precomputation and lookup."""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path


LIBERO_EVALUATION_SUITES = ("libero_spatial", "libero_object", "libero_goal", "libero_10", "libero_90")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _task_map_path() -> Path:
    return _repo_root() / "eval" / "libero" / "LIBERO" / "libero" / "libero" / "benchmark" / "libero_suite_task_map.py"


def _load_libero_task_map() -> dict[str, list[str]]:
    spec = importlib.util.spec_from_file_location("libero_suite_task_map", _task_map_path())
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load LIBERO task map from {_task_map_path()}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.libero_task_map


def _language_from_task_name(task_name: str) -> str:
    if task_name[0].isupper():
        if "SCENE10" in task_name:
            language = " ".join(task_name[task_name.find("SCENE") + 8 :].split("_"))
        else:
            language = " ".join(task_name[task_name.find("SCENE") + 7 :].split("_"))
    else:
        language = " ".join(task_name.split("_"))
    return language.replace("black bowl", "bowl")


def libero_evaluation_prompts(suites: tuple[str, ...] = LIBERO_EVALUATION_SUITES) -> tuple[str, ...]:
    """Return the prompts used by LIBERO eval, derived from the vendored LIBERO task map."""
    task_map = _load_libero_task_map()
    prompts = [""]
    for suite in suites:
        prompts.extend(_language_from_task_name(task_name) for task_name in task_map[suite])
    return tuple(dict.fromkeys(prompts))


def prompt_embedding_filename(prompt: str) -> str:
    """Return the stable embedding filename for a LIBERO task prompt."""
    processed_prompt = prompt.lower().strip()
    processed_prompt = re.sub(r"[\s/]+", "_", processed_prompt)
    processed_prompt = re.sub(r"[^a-z0-9_-]", "", processed_prompt)
    return f"{processed_prompt}.pt" if processed_prompt else "empty_prompt.pt"
