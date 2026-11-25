# Menghubungkan VM dengan browser perangkat lain

**Branch:** `infra/network` · **Tugas:** [Issue #8](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/8)

## Mulai dari mana?
Baca [cara menggunakan GitHub](../../CONTRIBUTING.md), lalu [panduan teknis](../contracts.md). Ambil pembaruan main ke branch sendiri. File yang dikerjakan: infrastructure/network.md.

## Langkah kerja
1. Siapkan NAT port forwarding (meneruskan koneksi dari laptop host ke VM): port 8081, 8082, 8083 masing-masing ke port 8000 pada VM.
2. Uji melalui localhost di laptop host, lalu melalui IP laptop host dari perangkat lain di jaringan lokal (LAN).
3. Untuk jarak jauh, Tailscale boleh dipakai sebagai jaringan privat; periksa izin dan batas penggunaan. Batasi firewall ke jaringan yang diperlukan; jangan membuka port router ke internet.
4. Catat hasil tiap URL dan bukti akses. Simpan alamat sensitif secara privat.

## Hasil yang dikumpulkan
Panduan jaringan dan bukti browser dapat membuka ketiga VM.

## Tanda tugas selesai
- [ ] Hasil sesuai panduan teknis.
- [ ] Sudah diuji dan dicatat hasilnya, atau tulis kendala yang mencegah pengujian.
- [ ] Commit, push, dan buat Pull Request ke main; cantumkan Issue terkait.
- [ ] Ketua sudah memeriksa dan menyetujui.
