# BankGuard — Kelompok 9

Prototype akademik Cloud Computing: pemantauan transaksi tidak wajar dan peringatan dini berbasis cloud.

## Target
Satu VM template Ubuntu Server dengan aplikasi BankGuard (Flask dan SQLite), tiga full clone VirtualBox aktif bersamaan, dan akses browser dari perangkat lain.

## Aturan risiko
- Rekening tujuan baru: +40
- Nominal >3 kali rata-rata historis: +35
- Frekuensi >3 transfer dalam 10 menit: +25

0–39 RENDAH, 40–59 SEDANG, 60–100 TINGGI. Semua data fiktif; skor bukan bukti fraud.

## Kolaborasi
Gunakan branch masing-masing dan Pull Request ke main. Jangan unggah kredensial, data pribadi, atau file VM.

Status: dalam pengembangan; aplikasi dan VM belum diuji.
