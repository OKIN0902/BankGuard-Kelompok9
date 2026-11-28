# Menyiapkan Ubuntu dan server aplikasi

Branch: `infra/setup` · [Issue #2](https://github.com/OKIN0902/BankGuard-Perbankan/issues/2)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: infrastructure/setup.sh, infrastructure/bankguard.service, infrastructure/nginx.conf, infrastructure/deployment.md.

## Langkah kerja
1. Buat VM Ubuntu Server 24.04 LTS (RAM 2 GB, 2 vCPU, disk dinamis 15 GB).
2. Instal Python 3.12, venv, Nginx; gunakan Node.js 22.18+ di laptop pengembang untuk membuat frontend dist, tidak wajib di VM.
3. Periksa contoh setup.sh, unit systemd dan nginx.conf; pasang hasil build frontend pada /opt/bankguard/frontend/dist dan backend pada /opt/bankguard/backend.
4. Gunicorn berjalan sebagai akun bankguard pada 127.0.0.1:8000; Nginx membuka port 80 dan meneruskan /api/ ke Gunicorn. Uji setelah reboot.
5. Siapkan secret dan password hash unik per clone; jangan menyimpannya di template.

## Hasil yang dikumpulkan
Script dan konfigurasi yang sudah diuji, catatan instalasi.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
