#!/usr/bin/env bash
set -euo pipefail

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

# Keep the physical redafrix desktop usable while remote experiments run.
if [ -S /run/user/1000/bus ]; then
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.desktop.screensaver lock-enabled false || true
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.desktop.session idle-delay 0 || true
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing' || true
  runuser -u redafrix -- env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing' || true
fi

# If the current physical session is locked, unlock it without restarting GDM.
loginctl unlock-session 2 2>/dev/null || true

# Refresh account metadata only. Do not restart gdm/display-manager.
systemctl try-reload-or-restart accounts-daemon.service 2>/dev/null || true

echo "DEAN_DESKTOP_USER_VISIBILITY_FIX_DONE"
