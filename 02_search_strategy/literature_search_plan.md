# Literature Search Plan

## Goal

Build a recall-maximizing search process for:

- active robotic exploration of unseen static objects
- reaching, approach, touch, and scan tasks
- RL, VLA, classical robotics, and hybrid methods
- vision plus optional local confirmation sensors such as tactile, thermal, or ultrasound

This plan is designed to minimize missed important papers and methods. It does not assume that one site or one query is enough.

## Core Principle

Do not search only the final internship title.

Search by buckets, then expand from seed papers, then sweep venues, then check gaps.

## Tool Roles

- Google Scholar: broad catch-all and forward/backward expansion
- OpenAlex: systematic and reproducible harvesting
- Semantic Scholar: semantic discovery and relevance triage
- IEEE Xplore and ACM DL: core engineering and robotics sources
- arXiv: newest preprints
- ResearchRabbit or Litmaps: citation-network expansion and monitoring
- CNKI, PubScholar, ChinaXiv: China-specific pass when needed
- Zotero: source of truth for stored papers
- Better BibTeX: stable citekeys for notes and writing
- Installed Deep-Research skill stack:
  - `research`: create outline.yaml and fields.yaml
  - `research-deep`: run structured deep search on outline items
  - `research-report`: summarize JSON outputs into report.md

## How The Installed Skills Fit

The installed `Deep-Research-skills` workflow is a helper layer, not a replacement for the overall method.

Use it like this:

1. Use `research` after the first manual search pass to build a structured outline of method families, benchmarks, and key items worth deeper investigation.
2. Use `research-deep` to systematically deepen research on the outline items.
3. Use `research-report` to generate a structured summary after the deep pass.

Do not use the skill stack as the only discovery method.

Still do manual:

- seed-paper selection
- citation chasing
- venue sweeps
- coverage checking by bucket

## Search Buckets

1. Unseen or novel object generalization
2. Active perception and active exploration
3. Reaching, approach, touch, and scan tasks
4. Contact-based and tactile exploration
5. VLA and language-conditioned control
6. RL for exploration, goal reaching, and hierarchical behavior
7. Classical robotics methods such as visual servoing, planning, POMDP, and next-best-view
8. Sim-to-real transfer, domain randomization, and multimodal fusion

## Query Design Rules

Every search query should combine terms from at least two of these groups:

- task: reaching, approach, touch, scan, exploration
- novelty: unseen object, novel object, unknown object, generalization, out of distribution, OOD
- method: RL, reinforcement learning, VLA, vision language action, visual servoing, planning, active perception, next best view
- sensing: vision, tactile, contact, thermal, ultrasound, multimodal
- transfer: sim to real, domain randomization, sensor noise

Do not trust title words alone.

## Search Execution Order

### Phase 1: Broad Discovery

For each high-priority query in `query_matrix.csv`:

1. Run in Google Scholar
2. Run in OpenAlex
3. Run in Semantic Scholar
4. Save the strongest 3 to 5 results to Zotero

Target after Phase 1:

- 3 to 5 seed papers per bucket
- 25 to 40 candidate papers total
- enough material to define a useful `research` outline if you want to use the installed skill stack

### Phase 2: Seed Expansion

For each bucket:

1. Pick the 2 strongest seed papers
2. Check references
3. Check cited-by
4. Check related or similar papers
5. Add any repeated or clearly central papers to Zotero

Target after Phase 2:

- seminal papers captured
- most repeated names and labs identified
- bucket-level duplicates reduced

### Phase 2.5: Structured Deep Research Pass

After Phase 2, optionally use the installed skill workflow:

1. Run `research` to generate:
   - `../04_structured_research/unseen-object-exploration/outline.yaml`
   - `../04_structured_research/unseen-object-exploration/fields.yaml`
2. Edit the generated outline so it matches your actual buckets and excludes irrelevant items
3. Run `research-deep`
4. Run `research-report`

Use this phase to deepen research on:

- method families
- benchmarks
- simulators
- core papers or labs
- transferable approaches outside your exact wording

Do not use this phase to skip manual checking of references, cited-by, and venue coverage.

### Phase 3: Venue Sweep

Sweep these venues manually for years 2020 through 2026:

- ICRA
- IROS
- RSS
- CoRL
- RA-L
- T-RO
- IJRR
- ICLR
- ICML
- NeurIPS

Use venue search even when keywords fail.

### Phase 4: Method Expansion Beyond Your Exact Topic

For each bucket, explicitly look for methods that could transfer into your problem even if they do not mention unseen objects directly:

- next-best-view
- active perception
- tactile exploration
- contact-rich control
- visual servoing
- planning under uncertainty
- POMDP
- multimodal sensor fusion

### Phase 5: China-Specific Pass

Only after the main pass is stable:

1. Re-run top queries in CNKI, PubScholar, and ChinaXiv
2. Search by labs and institutions if topic search is weak
3. Check whether any methods appear there earlier or under different naming

## Screening Rules

Keep a paper if at least one of these is true:

- directly addresses unseen or novel object behavior
- solves a simpler subproblem you can reuse, such as reaching or contact verification
- provides a benchmark, dataset, simulator, or evaluation method you can reuse
- contains a method family that could be adapted to your setup
- clearly defines a limitation that gives you a research angle

Drop or deprioritize a paper if:

- it is only loosely about generic manipulation with no relevance to generalization
- it has no reusable method, benchmark, or evaluation insight
- it is far outside your embodiment or sensing setup and offers no transferable idea

## What To Record For Every Kept Paper

Use `paper_tracking_template.csv` and fill:

- title
- year
- venue
- authors
- bucket
- method family
- task
- sensing
- action space
- what counts as unseen
- benchmark or environment
- sim-to-real
- main result
- main limitation
- why it matters for this internship

## Coverage Checklist

You are not done with a bucket until you have:

- at least 1 review or survey if it exists
- seminal papers
- the newest papers
- at least 1 strong baseline
- at least 1 non-deep-learning or classical method when relevant
- clear limitation papers or failure cases

If you use the installed skill workflow, also confirm:

- the generated outline did not miss an important method family
- the deep pass did not drift into irrelevant “adjacent but not reusable” work
- report output matches your manual coverage expectations

## Practical Operating Rule

Do not spend more than one session on setup before the first search pass.

Use tools to support the search, not replace the search.

The installed research skills are now part of the toolkit, but they are secondary to the search method itself.

## Recommended Next Action

1. Run all priority `P1` queries in `query_matrix.csv`
2. Collect the first seed set
3. Start filling `paper_tracking_template.csv`
4. After the seed set is stable, use the installed `research` skill to generate a structured deep-research outline
