# Menyimpan dan membaca data transaksi

**Branch:** `feature/database` · **Tugas:** [Issue #6](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/6)

## Mulai dari mana?
Baca [cara menggunakan GitHub](../../CONTRIBUTING.md), lalu [panduan teknis](../contracts.md). Ambil pembaruan main ke branch sendiri. File yang dikerjakan: bankguard/database.py, bankguard/schema.sql.

## Langkah kerja
1. Buat struktur tabel SQLite sesuai panduan teknis; SQLite menyimpan data dalam file lokal tiap VM.
2. Buat fungsi menyiapkan database, menyimpan transaksi dan mengambil daftar transaksi. Persiapan boleh dijalankan ulang tanpa menghapus data.
3. Gunakan parameter SQL (nilai input dipisah dari perintah SQL), ID unik UUID dan waktu UTC; simpan alasan sebagai JSON.
4. Uji apakah transaksi yang tersimpan masih ada setelah aplikasi ditutup atau dijalankan ulang.

## Hasil yang dikumpulkan
Struktur tabel, fungsi Python dan bukti data tersimpan.

## Tanda tugas selesai
- [ ] Hasil sesuai panduan teknis.
- [ ] Sudah diuji dan dicatat hasilnya, atau tulis kendala yang mencegah pengujian.
- [ ] Commit, push, dan buat Pull Request ke main; cantumkan Issue terkait.
- [ ] Ketua sudah memeriksa dan menyetujui.
