# Dean Isaac online OOD150 — exact execution only

You have ZERO authority to design, edit, optimize, reinterpret, or replace any part of this protocol.

Repository: `redafrix/reda-ws-backup`
Branch: `experiment/dean-isaac-online-ood150-20260817`
Prepared bundle Git blob: `f5d9bffddadc83dc0581c48c526901f3a1ba9399`
Expected reconstructed bundle SHA256: `9f54d0b9b3d41b0645dfcc041f5e13c5e5e075fa2cf0a0446fdae115f57029da`

IMPORTANT: do NOT use the checked-out `.tar.gz` working-tree file. A previous checkout produced a corrupted gzip stream. Reconstruct the exact archive bytes directly from the Git object database using `git cat-file` as prescribed below.

## Execute exactly

1. Fetch/pull this branch and verify checkout is clean.
2. Verify HEAD is the expected branch HEAD supplied by Reda.
3. Verify the exact prepared Git blob exists locally:

```bash
git cat-file -e f5d9bffddadc83dc0581c48c526901f3a1ba9399^{blob}
```

If that command fails, STOP.

4. Reconstruct the archive DIRECTLY from the Git blob, never from the working-tree file:

```bash
rm -rf /tmp/dean_online_protocol_chatgpt
mkdir -p /tmp/dean_online_protocol_chatgpt
git cat-file blob f5d9bffddadc83dc0581c48c526901f3a1ba9399 > /tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817.tar.gz
printf '%s  %s\n' '9f54d0b9b3d41b0645dfcc041f5e13c5e5e075fa2cf0a0446fdae115f57029da' '/tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817.tar.gz' | sha256sum -c -
gzip -t /tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817.tar.gz
tar -xzf /tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817.tar.gz -C /tmp/dean_online_protocol_chatgpt
cd /tmp/dean_online_protocol_chatgpt/dean_isaac_online_ood150_20260817
sha256sum -c LOCAL_SHA256SUMS.txt
```

If ANY checksum or `gzip -t` fails, STOP. Do not attempt repair.

5. Read `AGY_RUN_EXACTLY.md` inside the extracted directory and execute it EXACTLY.

## Forbidden
- do not use or extract the checked-out working-tree tarball;
- do not edit any extracted file;
- do not modify the threshold grid;
- do not create your own online controller;
- do not kill the HARD1000 process;
- do not remove stop markers;
- do not launch any command other than those prescribed by the exact instruction and orchestrator;
- do not scientifically interpret the results.
