# First Pass Summary

## What Was Done

- Ran the first seed-search pass across the priority buckets using the P1 query families
- Used OpenAlex as the main structured discovery source
- Tried Semantic Scholar, but the public API rate-limited during the run
- Wrote the initial seed set to `first_pass_seeds.csv`

## Strongest Seeds So Far

- `AcTExplore: Active Tactile Exploration on Unknown Objects`
- `Active Perception and Representation for Robotic Manipulation`
- `Tactile-Based Task Definition Through Edge Contact Formation Setpoints for Object Exploration and Manipulation`
- `OpenVLA: An Open-Source Vision-Language-Action Model`
- `RT-1: Robotics Transformer for Real-World Control at Scale`
- `Unsupervised Reinforcement Learning for Transferable Manipulation Skill Discovery`
- `Sim-to-Real Model-Based and Model-Free Deep Reinforcement Learning for Tactile Pushing`
- `DiffOcclusion: Differentiable Optimization Based Control Barrier Functions for Occlusion-Free Visual Servoing`

## Coverage Quality By Bucket

- `contact-tactile`: strongest early coverage
- `active-perception`: promising and directly relevant
- `vla-language`: good modern baseline coverage
- `rl-exploration`: usable first seeds, but still broad
- `classical-methods`: enough to start a baseline branch
- `sim2real-fusion`: has relevant contact and transfer seeds
- `unseen-generalization`: has broad anchors, still needs more direct papers
- `reaching-touch-scan`: weakest bucket so far and needs a more targeted pass

## Biggest Gaps Right Now

- direct papers on `reaching` or `approach` to previously unseen objects
- papers that change only one object factor first, such as color, then shape
- strong evaluation papers focused on generalization rather than generic manipulation
- benchmarks or setups explicitly matching `reach or touch an unseen object`

## Best Next Moves

1. Do citation expansion on the strongest direct seeds:
   - `AcTExplore`
   - `Active Perception and Representation for Robotic Manipulation`
   - `OpenVLA`
   - `Unsupervised Reinforcement Learning for Transferable Manipulation Skill Discovery`
2. Run the venue sweep for:
   - `ICRA`
   - `IROS`
   - `RSS`
   - `CoRL`
   focusing on 2020 to 2026
3. Run a more targeted second pass for the weak bucket:
   - `reaching unseen object robot arm`
   - `approach unknown object robot arm`
   - `vision based reaching unknown object`
   - `goal conditioned reaching manipulation generalization`
4. After the seed set is stable, use the installed `research` skill to generate a deeper outline
