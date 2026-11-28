#!/usr/bin/env bash
# Jalankan dari console VirtualBox, bukan SSH, pada template/clone yang dimaksud.
set -euo pipefail
[[ $EUID -eq 0 ]] || { echo "Gunakan sudo."; exit 1; }
name="${1:-}"
[[ "$name" =~ ^BankGuard-(Template|01|02|03)$ ]] || { echo "Gunakan BankGuard-Template, BankGuard-01, BankGuard-02, atau BankGuard-03."; exit 1; }
[[ -x /opt/bankguard/.venv/bin/python ]] || { echo "Aplikasi belum dipasang."; exit 1; }
if [[ -e /etc/bankguard/bankguard.env ]]; then
  echo "Environment sudah ada. Tidak mengganti identitas/rahasia otomatis."
  exit 1
fi
os_name="${name,,}"
hostnamectl set-hostname "$os_name"
if [[ -d /etc/cloud/cloud.cfg.d ]]; then
  printf 'preserve_hostname: true\n' > /etc/cloud/cloud.cfg.d/99-bankguard-hostname.cfg
fi
# Ubuntu dapat memiliki alias 127.0.1.1 untuk hostname lama.
if grep -qE '^127\.0\.1\.1[[:space:]]' /etc/hosts; then
  sed -i -E "s/^127\.0\.1\.1[[:space:]].*/127.0.1.1 $os_name/" /etc/hosts
else
  printf '\n127.0.1.1 %s\n' "$os_name" >> /etc/hosts
fi
# Template telah mengosongkan machine-id; systemd membuat identitas baru saat boot clone.
if [[ ! -s /etc/machine-id ]]; then systemd-machine-id-setup; fi
if command -v ssh-keygen >/dev/null; then ssh-keygen -A; fi
/opt/bankguard/.venv/bin/python /opt/bankguard/infrastructure/create-env.py
systemctl enable --now bankguard
if ! curl --fail --silent --show-error --retry 5 --retry-connrefused --retry-delay 1 http://127.0.0.1/api/health; then
  systemctl status bankguard --no-pager || true
  echo "Health gagal; periksa journalctl -u bankguard."
  exit 1
fi
printf '\nInstance %s siap. Login dengan petugas dan password demo lokal.\n' "$name"
