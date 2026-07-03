# Dean Reachability Fix (2026-06-03)

## Objective

Make Dean remain reachable remotely, especially from Bob and Sam, even when the laptop is not on Dean's local hotspot/network.

## Root Cause Findings

- Dean's SSH service was listening on `0.0.0.0:22` and `[::]:22`.
- Dean could reach Bob and Sam through Tailscale.
- Before the fix, Bob and Sam could see Dean in `tailscale status`, but inbound TCP/22 from Bob/Sam to Dean failed.
- Dean's graphical session was configured to suspend:
  - `sleep-inactive-ac-type = suspend`
  - `sleep-inactive-battery-type = suspend`
- `systemd-inhibit` was denied without root.
- The `dean` account has a locked password for sudo purposes. Root fixes were applied through the `redafrix` account, which has sudo access.

## Fixes Applied On Dean

Applied as root on Dean:

- Masked sleep targets:
  - `sleep.target`
  - `suspend.target`
  - `hibernate.target`
  - `hybrid-sleep.target`
- Added `/etc/systemd/logind.conf.d/99-dean-keep-awake.conf`:
  - ignore lid switch
  - ignore suspend/hibernate keys
  - ignore idle action
- Set GNOME power settings for users `redafrix` and `dean` where a session bus exists:
  - AC sleep: `nothing`
  - battery sleep: `nothing`
  - idle delay: `0`
- Disabled Wi-Fi powersave persistently in NetworkManager:
  - `/etc/NetworkManager/conf.d/99-dean-wifi-powersave-off.conf`
  - `tp_hotspot` powersave disabled
- Enabled SSH and added keepalive config:
  - `/etc/ssh/sshd_config.d/99-dean-keepalive.conf`
- Enabled Tailscale:
  - `tailscaled` active/enabled
  - operator set to `dean`
  - accept DNS disabled
- Added `dean-keep-reachable.service`:
  - persistent root `systemd-inhibit` blocking sleep/idle/lid sleep
- UFW was checked and is inactive.

## Verification

Dean local status after fix:

- `ssh`: active
- `tailscaled`: active
- `NetworkManager`: active
- `dean-keep-reachable.service`: active
- sleep inhibitor present:
  - `dean-remote ... sleep:idle:handle-lid-switch ... block`
- GPU idle:
  - RTX A5000, `15 MiB / 24564 MiB`, `0%`

Bob to Dean real SSH test:

```text
BOB_TO_DEAN_SSH_OK
Batman
dean
```

Sam to Dean real SSH test:

```text
SAM_TO_DEAN_SSH_OK
Batman
dean
```

Public SSH keys from Bob and Sam were added to `/home/dean/.ssh/authorized_keys`, so they can log in as `dean@100.124.50.124`.

## Current Caveat

After the successful Bob/Sam-to-Dean tests, Sam itself became unreachable from this laptop and from Bob:

```text
ssh: connect to host 100.112.19.30 port 22: Connection timed out
```

That is a Sam reachability issue, not a Dean inbound SSH issue. Bob still reaches Dean successfully after the fix.

## Remaining Tailscale Note

Dean's `tailscale netcheck` still reports:

- `UDP: false`
- `IPv4: (no addr found)`
- nearest DERP: Paris

So Dean is currently using DERP relay rather than direct UDP for remote peers. That is slower but acceptable for SSH and experiment control. The critical requirement, remote SSH from Bob/Sam to Dean, passed.
