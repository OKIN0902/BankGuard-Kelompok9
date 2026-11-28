# Mengatur dan menyatukan pekerjaan kelompok

Branch: `integration/leader` · [Issue #1](https://github.com/OKIN0902/BankGuard-Perbankan/issues/1)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: README.md, docs/contracts.md, backend/requirements.txt.

## Langkah kerja
1. Sepakati format API dengan tim frontend, backend dan database sebelum mulai coding.
2. Periksa PR anggota, jalankan pengujian Python, npm install dan npm run build; simpan package-lock.json hasil instalasi yang diuji.
3. Pasang frontend hasil build, backend, Nginx dan Gunicorn pada VM template. Catat commit yang dipakai.
4. Koordinasikan pengujian tiga VM dan demo.

## Hasil yang dikumpulkan
Catatan integrasi, versi kode dan hasil uji.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
