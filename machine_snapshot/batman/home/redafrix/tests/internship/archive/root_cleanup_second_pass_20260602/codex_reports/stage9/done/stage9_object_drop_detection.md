# Stage 9 Object Drop Detection

Status: available as a numeric signal, but not validated on a real drop event.

Implementation: `outcome_metrics.compute_delta()` records `height_drop_max` from MuJoCo object body positions before/after candidate execution. `label_rules.py` marks a large drop as BAD only when `height_drop_max > 0.15`.

Pilot result: no object-drop BAD labels occurred. Max observed height drop in later-state pilot: `0.000405379`.

Decision: keep as strong evidence when triggered, but collect/construct a dedicated lifted-object drop sanity state before relying on it for final data.
