# Menggandakan satu VM menjadi tiga

Branch: `infra/cloning` · [Issue #3](https://github.com/OKIN0902/BankGuard-Perbankan/issues/3)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: infrastructure/clone.ps1, infrastructure/cloning.md.

## Langkah kerja
1. Tunggu aplikasi pada template selesai diuji. Matikan template sebelum Full Clone.
2. Buat BankGuard-01, BankGuard-02 dan BankGuard-03 tanpa instal ulang. Gunakan MAC, hostname, machine-id dan bila ada SSH host keys yang berbeda.
3. Buat secret, password hash dan database demo masing-masing; jangan membawa data uji pribadi dari template.
4. Atur port host 8081, 8082, 8083 menuju port 80 guest. Nyalakan ketiganya dan buktikan aplikasi berjalan.

## Hasil yang dikumpulkan
Script PowerShell, panduan dan bukti tiga VM aktif.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
