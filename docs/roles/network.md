# Membuka aplikasi dari perangkat lain

Branch: `infra/network` · [Issue #8](https://github.com/OKIN0902/BankGuard-Perbankan/issues/8)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: infrastructure/network.md; koordinasi nginx.conf dengan tim setup.

## Langkah kerja
1. Atur NAT port forwarding: host 8081,8082,8083 ke port 80 masing-masing VM (Nginx). Jangan buka port 8000 Gunicorn ke jaringan.
2. Uji localhost, lalu IP host di LAN dari perangkat lain. Pastikan halaman Vue dan /api/health bekerja pada alamat yang sama.
3. Untuk pengujian beda lokasi, Tailscale opsional; periksa kuota dan izin. Batasi Windows Firewall ke LAN/VPN yang digunakan, jangan membuka router ke internet.
4. Dokumentasikan bukti tiap VM dan rencana demo di kelas tanpa VPN jika LAN memungkinkan.

## Hasil yang dikumpulkan
Panduan jaringan dan bukti akses tiga VM.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
