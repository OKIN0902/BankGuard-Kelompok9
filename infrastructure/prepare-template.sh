#!/usr/bin/env bash
# PERHATIAN: khusus VM template setelah demo diuji. Menghapus data demo dan rahasia.
# Jalankan melalui console VirtualBox. Script langsung mematikan VM.
set -euo pipefail
[[ $EUID -eq 0 ]] || { echo "Gunakan sudo."; exit 1; }
[[ "$(hostname)" == BankGuard-Template ]] || { echo "Hanya boleh pada BankGuard-Template."; exit 1; }
[[ -f /opt/bankguard/backend/schema.sql && -f /opt/bankguard/frontend/dist/index.html ]] || exit 1
read -r -p "Hapus data demo/rahasia dan matikan template? Ketik SIAP-CLONE: " answer
[[ "$answer" == SIAP-CLONE ]] || { echo "Dibatalkan."; exit 1; }
systemctl disable --now bankguard
rm -f /etc/bankguard/bankguard.env
rm -f /var/lib/bankguard/bankguard.sqlite3{,-wal,-shm,-journal}
# Bila SSH tersedia, nonaktifkan akses sampai host keys baru dibuat di clone.
for unit in ssh.socket ssh.service; do
  if systemctl list-unit-files "$unit" --no-legend | grep -q "^$unit"; then
    systemctl disable --now "$unit"
  fi
done
rm -f /etc/ssh/ssh_host_*_key /etc/ssh/ssh_host_*_key.pub
# Jangan clone akun login OS dengan password yang dipakai di luar lab.
# Hapus cache identitas D-Bus jika terpisah; biarkan symlink ke /etc/machine-id.
if [[ -e /var/lib/dbus/machine-id && ! -L /var/lib/dbus/machine-id ]]; then rm /var/lib/dbus/machine-id; fi
truncate -s 0 /etc/machine-id
sync
systemctl poweroff
