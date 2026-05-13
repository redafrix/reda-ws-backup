# Candidate Debug Dataset Report

- Dataset: `/media/rootalkhatib/My Passport/reda_ws/asynchvla_ws/data/debug/candidate_debug.pt`
- File size bytes: `6965754`
- Number of contexts: `200`
- Number of candidates: `1200`
- Schema: `candidate_debug_v1`

## Candidate Types

- `expert_action`: count=`200`, min=`0.000000`, mean=`0.000000`, max=`0.000000`
- `other_demo_or_other_task`: count=`200`, min=`0.263316`, mean=`0.994390`, max=`2.001455`
- `perturb_large`: count=`200`, min=`1.477771`, mean=`1.914658`, max=`2.414777`
- `perturb_small`: count=`200`, min=`0.208526`, mean=`0.255305`, max=`0.334091`
- `same_task_far`: count=`200`, min=`0.218204`, mean=`0.800747`, max=`1.810308`
- `simvla_seed0`: count=`200`, min=`0.453315`, mean=`1.652940`, max=`3.221538`

## Same-Context Proof

- context_id: `ctx_000000`
- candidate types: `['expert_action', 'simvla_seed0', 'perturb_small', 'perturb_large', 'same_task_far', 'other_demo_or_other_task']`
- true errors: `[('expert_action', 0.0), ('simvla_seed0', 1.405077), ('perturb_small', 0.251612), ('perturb_large', 2.265432), ('same_task_far', 0.63465), ('other_demo_or_other_task', 0.263316)]`
- pooled VLM identical across candidates: `True`
- proprio identical across candidates: `True`
- target expert action identical across candidates: `True`
