# Isaac Results Catalog Schema Definition

## Enums

### `scientific_status`
- `valid`: Fully audited, verified, and canonical experimental result.
- `historical_reference`: Valid historical run under legacy or earlier protocol.
- `incomplete`: Partial run stopped before target sample size.
- `superseded`: Predeclared or exploratory run replaced by a subsequent design.
- `quarantined_invalid`: Flawed, corrupted, or bypassed run (`safe_to_use = false`).
- `development_only`: Tool, renderer, or infrastructure test.
- `predeclared_not_executed`: Predeclared formal experiment design that was superseded before GPU execution.

### `canonicality`
- `canonical_primary`: Primary authoritative scientific benchmark or result.
- `canonical_ablation`: Official planned ablation study.
- `canonical_baseline`: Authoritative benchmark baseline.
- `historical_reference`: Contextual historical evaluation.
- `noncanonical`: Exploratory or superseded variation.
- `invalid`: Quarantined data forbidden from primary aggregates.
