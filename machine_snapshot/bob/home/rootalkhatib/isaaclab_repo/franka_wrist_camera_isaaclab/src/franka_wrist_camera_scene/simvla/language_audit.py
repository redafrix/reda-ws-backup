"""Language prompt audits for saved raw episodes."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from json import JSONDecodeError
from pathlib import Path
import re

ASSET_SUFFIX_RE = re.compile(r"\b[a-z][a-z0-9]*(?:_[0-9]+|_[a-f0-9]{6,})\b")


@dataclass(frozen=True, slots=True)
class PromptAuditFinding:
    episode_dir: str
    instruction: str
    reason: str

    def to_dict(self) -> dict:
        return asdict(self)


def audit_episode_prompts(collection_roots: list[Path]) -> list[PromptAuditFinding]:
    findings: list[PromptAuditFinding] = []
    for root in collection_roots:
        if not root.is_dir():
            raise FileNotFoundError(root)
        for meta_path in sorted(root.glob("*/meta.json")):
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except (OSError, JSONDecodeError) as exc:
                findings.append(PromptAuditFinding(str(meta_path.parent), "", f"bad_meta_json:{exc}"))
                continue
            instruction = str(meta.get("instruction", ""))
            object_label = meta.get("object_label")
            placement_label = meta.get("placement_target_label")
            findings.extend(_audit_instruction(meta_path.parent, instruction, object_label, placement_label))
    return findings


def audit_verified_episode_prompts(report_path: Path) -> list[PromptAuditFinding]:
    report = json.loads(report_path.read_text(encoding="utf-8"))
    findings: list[PromptAuditFinding] = []
    for file_record in report.get("files", []):
        for demo in file_record.get("verified_demos", []):
            episode_dir = Path(demo["source_episode_path"])
            try:
                meta = json.loads((episode_dir / "meta.json").read_text(encoding="utf-8"))
            except (OSError, JSONDecodeError) as exc:
                findings.append(PromptAuditFinding(str(episode_dir), "", f"bad_meta_json:{exc}"))
                continue
            findings.extend(
                _audit_instruction(
                    episode_dir,
                    str(meta.get("instruction", "")),
                    meta.get("object_label"),
                    meta.get("placement_target_label"),
                )
            )
    return findings


def _audit_instruction(
    episode_dir: Path,
    instruction: str,
    object_label: object,
    placement_label: object,
) -> list[PromptAuditFinding]:
    findings: list[PromptAuditFinding] = []
    if not instruction:
        return [PromptAuditFinding(str(episode_dir), instruction, "missing_instruction")]
    if ASSET_SUFFIX_RE.search(instruction):
        findings.append(PromptAuditFinding(str(episode_dir), instruction, "asset_suffix_like_token"))
    for label_name, label in (("object_label", object_label), ("placement_target_label", placement_label)):
        if label in (None, ""):
            continue
        label_text = str(label)
        if label_text not in instruction:
            findings.append(PromptAuditFinding(str(episode_dir), instruction, f"missing_{label_name}:{label_text}"))
        if ASSET_SUFFIX_RE.search(label_text):
            findings.append(PromptAuditFinding(str(episode_dir), instruction, f"{label_name}_contains_asset_suffix:{label_text}"))
    return findings
