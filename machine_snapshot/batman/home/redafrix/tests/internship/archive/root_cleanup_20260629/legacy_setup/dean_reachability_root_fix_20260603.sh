#!/usr/bin/env bash
set -euo pipefail

report=/home/redafrix/dean_reachability_root_fix_20260603.txt
{
  echo "Dean reachability root fix started: $(date)"
  echo "Host: $(hostname)"
  echo "User: $(id)"
} > "$report"

systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target >> "$report" 2>&1 || true

mkdir -p /etc/systemd/logind.conf.d
cat > /etc/systemd/logind.conf.d/99-dean-keep-awake.conf <<'EOF'
[Login]
HandleLidSwitch=ignore
HandleLidSwitchExternalPower=ignore
HandleLidSwitchDocked=ignore
HandlePowerKey=ignore
HandleSuspendKey=ignore
HandleHibernateKey=ignore
IdleAction=ignore
IdleActionSec=0
EOF

for u in redafrix dean; do
  if id "$u" >/dev/null 2>&1; then
    uid=$(id -u "$u")
    if [ -S "/run/user/$uid/bus" ]; then
      sudo -u "$u" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$uid/bus" gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing' >> "$report" 2>&1 || true
      sudo -u "$u" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$uid/bus" gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing' >> "$report" 2>&1 || true
      sudo -u "$u" DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$uid/bus" gsettings set org.gnome.desktop.session idle-delay 0 >> "$report" 2>&1 || true
    fi
  fi
done

mkdir -p /etc/NetworkManager/conf.d
cat > /etc/NetworkManager/conf.d/99-dean-wifi-powersave-off.conf <<'EOF'
[connection]
wifi.powersave = 2
EOF
nmcli connection modify tp_hotspot connection.autoconnect yes 802-11-wireless.powersave 2 >> "$report" 2>&1 || true
nmcli connection modify "Wired connection 1" connection.autoconnect yes >> "$report" 2>&1 || true
nmcli connection modify laptop_shared_usb_eth connection.autoconnect yes >> "$report" 2>&1 || true
nmcli general reload >> "$report" 2>&1 || true

mkdir -p /etc/ssh/sshd_config.d
cat > /etc/ssh/sshd_config.d/99-dean-keepalive.conf <<'EOF'
ClientAliveInterval 60
ClientAliveCountMax 10
TCPKeepAlive yes
EOF
systemctl enable --now ssh >> "$report" 2>&1 || true
systemctl reload ssh >> "$report" 2>&1 || systemctl reload sshd >> "$report" 2>&1 || true

systemctl enable --now tailscaled >> "$report" 2>&1 || true
tailscale set --operator=dean >> "$report" 2>&1 || true
tailscale set --accept-dns=false >> "$report" 2>&1 || true

if command -v ufw >/dev/null 2>&1; then
  ufw allow in on tailscale0 to any port 22 proto tcp >> "$report" 2>&1 || true
fi

cat > /etc/systemd/system/dean-keep-reachable.service <<'EOF'
[Unit]
Description=Keep Dean reachable for remote experiments by inhibiting sleep and idle suspend
After=network-online.target tailscaled.service ssh.service
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/systemd-inhibit --what=sleep:idle:handle-lid-switch --who=dean-remote --why=keep_dean_reachable_for_remote_experiments --mode=block /usr/bin/sleep infinity
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload >> "$report" 2>&1
systemctl enable --now dean-keep-reachable.service >> "$report" 2>&1 || true

systemctl restart systemd-logind >> "$report" 2>&1 || true

{
  echo "--- final services"
  systemctl is-active ssh tailscaled NetworkManager dean-keep-reachable.service 2>&1 || true
  echo "--- final service enabled"
  systemctl is-enabled ssh tailscaled NetworkManager dean-keep-reachable.service 2>&1 || true
  echo "--- final tailscale"
  tailscale status 2>&1 | head -80 || true
  echo "--- final netcheck"
  tailscale netcheck 2>&1 | grep -E "UDP:|IPv4:|Nearest DERP|Captive|MappingVaries" || true
  echo "--- final inhibitors"
  systemd-inhibit --list --no-pager 2>&1 | grep -E 'dean-remote|sleep|idle|handle-lid' || true
  echo "--- final nm"
  nmcli -f NAME,TYPE,DEVICE,AUTOCONNECT con show --active 2>/dev/null || true
  echo "--- ufw"
  ufw status 2>&1 || true
  echo "Dean reachability root fix finished: $(date)"
} >> "$report"
cat "$report"
