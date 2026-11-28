#!/usr/bin/env bash
# Jalankan pada VM Ubuntu khusus BankGuard, dari repo yang sudah memiliki frontend/dist.
set -euo pipefail
[[ $EUID -eq 0 ]] || { echo "Gunakan sudo bash infrastructure/setup.sh"; exit 1; }
repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[[ -f "$repo/frontend/dist/index.html" ]] || { echo "Build Vue dahulu (npm install && npm run build)."; exit 1; }
[[ -f "$repo/backend/schema.sql" ]] || { echo "Backend tidak ditemukan."; exit 1; }
apt-get update
apt-get install -y python3 python3-venv nginx curl
if ! id bankguard >/dev/null 2>&1; then
  useradd --system --user-group --home-dir /var/lib/bankguard --shell /usr/sbin/nologin bankguard
fi
if systemctl is-active --quiet bankguard; then systemctl stop bankguard; fi
install -d -m 0755 /opt/bankguard/backend /opt/bankguard/frontend/dist /opt/bankguard/infrastructure
install -d -o bankguard -g bankguard -m 0750 /var/lib/bankguard
install -d -m 0700 /etc/bankguard
install -m 0644 "$repo/backend/"*.py "$repo/backend/schema.sql" "$repo/backend/requirements.txt" /opt/bankguard/backend/
cp -a "$repo/frontend/dist/." /opt/bankguard/frontend/dist/
chown -R root:root /opt/bankguard
chmod -R a+rX /opt/bankguard/frontend/dist
python3 -m venv /opt/bankguard/.venv
/opt/bankguard/.venv/bin/python -m pip install -r /opt/bankguard/backend/requirements.txt
install -m 0644 "$repo/infrastructure/bankguard.service" /etc/systemd/system/bankguard.service
install -m 0644 "$repo/infrastructure/nginx.conf" /etc/nginx/sites-available/bankguard
install -m 0755 "$repo/infrastructure/"{prepare-template.sh,init-instance.sh} /opt/bankguard/infrastructure/
install -m 0644 "$repo/infrastructure/create-env.py" /opt/bankguard/infrastructure/
systemctl daemon-reload
# Hanya hapus symlink default bawaan nginx, bukan situs kustom.
if [[ -L /etc/nginx/sites-enabled/default && "$(readlink -f /etc/nginx/sites-enabled/default)" == /etc/nginx/sites-available/default ]]; then
  rm /etc/nginx/sites-enabled/default
fi
if [[ ! -e /etc/nginx/sites-enabled/bankguard && ! -L /etc/nginx/sites-enabled/bankguard ]]; then
  ln -s /etc/nginx/sites-available/bankguard /etc/nginx/sites-enabled/bankguard
fi
nginx -t
systemctl enable --now nginx
systemctl reload nginx
echo "Pemasangan selesai. Lanjutkan sudo bash /opt/bankguard/infrastructure/init-instance.sh BankGuard-Template"
