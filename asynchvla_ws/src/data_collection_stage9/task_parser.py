from __future__ import annotations
import re
from dataclasses import dataclass

STOP = {
    "the", "a", "an", "and", "it", "both", "left", "right", "front", "back",
    "of", "to", "in", "on", "at", "into", "onto",
    "place", "put", "pick", "up", "move", "stack", "with",
}
GOAL_HINTS = {
    "basket", "tray", "plate", "drawer", "cabinet", "stove", "microwave", "caddy",
    "rack", "shelf", "compartment", "bowl", "middle", "top", "bottom",
}

def norm(s: str) -> str:
    s = s.lower().replace("-", " ")
    s = re.sub(r"[^a-z0-9_ ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def obs_bases(obs: dict) -> list[str]:
    bases = []
    for k in obs.keys():
        if k.endswith("_pos") and not k.endswith("_to_robot0_eef_pos"):
            bases.append(k[:-4])
    return sorted(set(bases), key=len, reverse=True)

def base_to_phrase(base: str) -> str:
    return re.sub(r"_\d+", "", base).replace("_", " ")

def base_to_body_prefix(base: str) -> str:
    return base

def mentioned_bases(language: str, obs: dict, all_bodies: list[str] | None = None) -> list[str]:
    text = norm(language)
    found_with_score = []
    bases = obs_bases(obs)
    if all_bodies:
        ignore = ("world", "robot", "gripper", "eef", "mount", "base", "link", "wrist", "camera", "table", "floor")
        filtered_bodies = [b for b in all_bodies if not any(x in b.lower() for x in ignore)]
        bases = sorted(set(bases + filtered_bodies), key=len, reverse=True)

    for base in bases:
        phrase = base_to_phrase(base)
        toks = [t for t in phrase.split() if t not in STOP]
        score = 0
        if phrase in text:
            score = 100 # Exact phrase match
        elif toks:
            shared = [t for t in toks if t in text]
            if len(shared) > 0:
                # Count how many distinct tokens from base are in text
                distinct_shared = set(shared)
                if len(distinct_shared) >= 2 or (len(distinct_shared) == 1 and any(h in distinct_shared for h in GOAL_HINTS)):
                    score = len(distinct_shared)
        
        if score > 0:
            found_with_score.append((base, score))
    
    # Sort by score descending, then by length descending
    found_with_score.sort(key=lambda x: (x[1], len(x[0])), reverse=True)
    return [x[0] for x in found_with_score]

def extract_relation(language: str) -> str:
    t = norm(language)
    if any(w in t for w in ["place", "put", "stack"]):
        return "place_or_put"
    if "open" in t or "close" in t or "turn" in t:
        return "articulation_or_toggle"
    if "pick" in t:
        return "pick"
    return "unknown"

def parse_task_context(language: str, obs: dict, all_bodies: list[str] | None = None) -> dict:
    mentioned = mentioned_bases(language, obs, all_bodies)
    text = norm(language)
    target = mentioned[0] if mentioned else None
    goal = None
    for base in mentioned:
        if base == target: continue
        phrase = base_to_phrase(base)
        if any(h in phrase.split() or h in phrase for h in GOAL_HINTS):
            goal = base
            break
    if goal is None and len(mentioned) >= 2:
        goal = mentioned[1]
    return {
        "task_language": language,
        "relation": extract_relation(language),
        "mentioned_bases": mentioned,
        "target_base": target,
        "goal_base": goal,
        "target_body_prefix": base_to_body_prefix(target) if target else None,
        "goal_body_prefix": base_to_body_prefix(goal) if goal else None,
        "parse_confidence": "MEDIUM" if target else "LOW",
    }
