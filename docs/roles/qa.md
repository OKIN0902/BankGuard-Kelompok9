# Menguji aplikasi dan mencatat kesalahan

Branch: `test/quality-assurance` · [Issue #7](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/7)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: tests/, docs/test-report.md.

## Langkah kerja
1. Uji semua skor: 0,25,35,40,60,65,75,100. Nominal tepat 3 kali rata-rata dan frekuensi tepat 3 tidak menambah skor terkait.
2. Uji API JSON: input salah 400, belum login 401, CSRF salah 403, login/logout, data tersimpan setelah restart.
3. Uji frontend Vue, npm run build, tampilan HP, dan komunikasi /api melalui Nginx. Pastikan dashboard tidak bisa membaca data tanpa login.
4. Uji ketiga VM dan akses browser dari perangkat lain. Catat hasil nyata, bukan hanya hasil yang diharapkan.

## Hasil yang dikumpulkan
Tes Python dan laporan pengujian API, UI, jaringan.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
