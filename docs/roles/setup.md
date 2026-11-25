# Menyiapkan Ubuntu dan menjalankan aplikasi

**Branch:** `infra/setup` · **Tugas:** [Issue #2](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/2)

## Mulai dari mana?
Baca [cara menggunakan GitHub](../../CONTRIBUTING.md), lalu [panduan teknis](../contracts.md). Ambil pembaruan main ke branch sendiri. File yang dikerjakan: infrastructure/setup.sh, infrastructure/bankguard.service.

## Langkah kerja
1. Siapkan VM Ubuntu Server 24.04 LTS: 2 CPU virtual, RAM 2 GB, disk dinamis 15 GB. Gunakan VM uji jika perangkat memungkinkan.
2. Buat script instalasi Python, lingkungan Python terpisah (venv) dan paket pada requirements.txt.
3. Buat layanan systemd agar Gunicorn (server aplikasi) berjalan otomatis pada port 8000 dengan akun biasa, bukan root.
4. Uji setelah VM dinyalakan ulang. Jangan menyimpan password atau kunci rahasia pada VM template.

## Hasil yang dikumpulkan
Script instalasi, file layanan, dan catatan hasil uji.

## Tanda tugas selesai
- [ ] Hasil sesuai panduan teknis.
- [ ] Sudah diuji dan dicatat hasilnya, atau tulis kendala yang mencegah pengujian.
- [ ] Commit, push, dan buat Pull Request ke main; cantumkan Issue terkait.
- [ ] Ketua sudah memeriksa dan menyetujui.
