#!/usr/bin/env bash
set -euo pipefail

cp -a /etc/gdm3/custom.conf "/etc/gdm3/custom.conf.backup_$(date +%Y%m%d_%H%M%S)"

python3 - <<'PY'
from pathlib import Path

path = Path("/etc/gdm3/custom.conf")
text = path.read_text()
lines = text.splitlines()

out = []
in_daemon = False
seen_daemon = False
inserted = False

for line in lines:
    stripped = line.strip()
    if stripped == "[daemon]":
        in_daemon = True
        seen_daemon = True
        out.append(line)
        continue
    if stripped.startswith("[") and stripped.endswith("]") and stripped != "[daemon]":
        if in_daemon and not inserted:
            out.append("AutomaticLoginEnable = true")
            out.append("AutomaticLogin = redafrix")
            inserted = True
        in_daemon = False
        out.append(line)
        continue
    if in_daemon and (
        stripped.startswith("AutomaticLoginEnable")
        or stripped.startswith("#  AutomaticLoginEnable")
        or stripped.startswith("AutomaticLogin =")
        or stripped.startswith("#  AutomaticLogin =")
    ):
        continue
    out.append(line)

if not seen_daemon:
    out.append("[daemon]")
    out.append("AutomaticLoginEnable = true")
    out.append("AutomaticLogin = redafrix")
elif in_daemon and not inserted:
    out.append("AutomaticLoginEnable = true")
    out.append("AutomaticLogin = redafrix")

path.write_text("\n".join(out) + "\n")
PY

mkdir -p /var/lib/AccountsService/users
cat > /var/lib/AccountsService/users/dean <<'EOF'
[User]
SystemAccount=true
EOF
cat > /var/lib/AccountsService/users/redafrix <<'EOF'
[User]
SystemAccount=false
EOF
chown root:root /var/lib/AccountsService/users/dean /var/lib/AccountsService/users/redafrix
chmod 0644 /var/lib/AccountsService/users/dean /var/lib/AccountsService/users/redafrix

if [ -S /run/user/1000/bus ]; then
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.desktop.screensaver lock-enabled false || true
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.desktop.session idle-delay 0 || true
fi

systemctl restart gdm3.service

echo "DEAN_GDM_REDAFRIX_AUTOLOGIN_FIX_DONE"
