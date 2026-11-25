# Menguji aplikasi dan mencatat kesalahan

**Branch:** `test/quality-assurance` · **Tugas:** [Issue #7](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/7)

## Mulai dari mana?
Baca [cara menggunakan GitHub](../../CONTRIBUTING.md), lalu [panduan teknis](../contracts.md). Ambil pembaruan main ke branch sendiri. File yang dikerjakan: tests/, docs/test-report.md.

## Langkah kerja
1. Buat pengujian delapan kombinasi skor: 0, 25, 35, 40, 60, 65, 75, 100.
2. Uji batas: rata-rata Rp500.000, nominal Rp1.500.000 tidak menambah skor nominal; Rp1.500.001 menambah 35. Frekuensi 3 tidak menambah skor; 4 menambah 25.
3. Uji input salah, login, dan apakah data tetap tersimpan setelah restart.
4. Saat tiga VM siap, uji akses dari perangkat lain. Catat hasil yang diharapkan, hasil sebenarnya, dan kendala.

## Hasil yang dikumpulkan
File pengujian dan laporan lulus/gagal/belum diuji.

## Tanda tugas selesai
- [ ] Hasil sesuai panduan teknis.
- [ ] Sudah diuji dan dicatat hasilnya, atau tulis kendala yang mencegah pengujian.
- [ ] Commit, push, dan buat Pull Request ke main; cantumkan Issue terkait.
- [ ] Ketua sudah memeriksa dan menyetujui.
