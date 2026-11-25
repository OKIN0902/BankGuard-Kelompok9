# Membuat logika aplikasi dan skor risiko

**Branch:** `feature/backend` · **Tugas:** [Issue #4](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/4)

## Mulai dari mana?
Baca [cara menggunakan GitHub](../../CONTRIBUTING.md), lalu [panduan teknis](../contracts.md). Ambil pembaruan main ke branch sendiri. File yang dikerjakan: bankguard/app.py, bankguard/risk_engine.py.

## Langkah kerja
1. Buat fungsi menghitung skor: rekening tujuan baru +40, nominal lebih dari 3 kali rata-rata +35, lebih dari 3 transfer dalam 10 menit +25.
2. Periksa input pada server; tolak input yang salah. Contoh: 10 juta, rata-rata 500 ribu, tujuan baru, 1 transfer menghasilkan 75 (TINGGI).
3. Buat halaman login/logout, jalur dashboard, simulator dan health (cek server), serta perlindungan CSRF untuk formulir POST.
4. Hubungkan hasil analisis ke fungsi database dan halaman frontend sesuai nama fungsi dan data pada panduan teknis.

## Hasil yang dikumpulkan
Kode Python yang menghitung skor dan menjalankan alur aplikasi.

## Tanda tugas selesai
- [ ] Hasil sesuai panduan teknis.
- [ ] Sudah diuji dan dicatat hasilnya, atau tulis kendala yang mencegah pengujian.
- [ ] Commit, push, dan buat Pull Request ke main; cantumkan Issue terkait.
- [ ] Ketua sudah memeriksa dan menyetujui.
