# Dean Isaac online OOD150 — exact execution only

You have ZERO authority to design, edit, optimize, reinterpret, or replace any part of this protocol.

Repository: `redafrix/reda-ws-backup`
Branch: `experiment/dean-isaac-online-ood150-20260817`
Bundle: `prepared_experiments/dean_isaac_online_ood150_20260817/dean_isaac_online_ood150_20260817.tar.gz`
Expected bundle SHA256: `9f54d0b9b3d41b0645dfcc041f5e13c5e5e075fa2cf0a0446fdae115f57029da`

## Execute exactly

1. Fetch/pull this branch and verify checkout is clean.
2. Verify the bundle SHA256 exactly matches the value above. If it does not, STOP.
3. Extract the bundle exactly into `/tmp/dean_online_protocol_chatgpt/`:

```bash
rm -rf /tmp/dean_online_protocol_chatgpt
mkdir -p /tmp/dean_online_protocol_chatgpt
sha256sum prepared_experiments/dean_isaac_online_ood150_20260817/dean_isaac_online_ood150_20260817.tar.gz
tar -xzf prepared_experiments/dean_isaac_online_ood150_20260817/dean_isaac_online_ood150_20260817.tar.gz -C /tmp/dean_online_protocol_chatgpt
cd /tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817
sha256sum -c LOCAL_SHA256SUMS.txt
```

If any checksum fails, STOP.

4. Read `AGY_RUN_EXACTLY.md` inside the extracted directory and execute it EXACTLY.

## Forbidden
- do not edit any extracted file;
- do not modify the threshold grid;
- do not create your own online controller;
- do not kill the HARD1000 process;
- do not remove stop markers;
- do not launch any command other than those prescribed by the exact instruction and orchestrator;
- do not scientifically interpret the results.
