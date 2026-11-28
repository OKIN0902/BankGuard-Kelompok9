# Membuat tampilan Vue di browser

Branch: `feature/frontend` · [Issue #5](https://github.com/OKIN0902/BankGuard-Perbankan/issues/5)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: frontend/.

## Langkah kerja
1. Instal Node.js 22.18+ (seri 22) dan npm. Dari frontend jalankan npm install lalu npm run dev.
2. Gunakan Vue 3, Vite dan Bootstrap 5 yang sudah tercantum di package.json. Buat login, dashboard dan simulator dalam file .vue.
3. Gunakan Vue Router dan services/api.js untuk meminta JSON dari /api. Tampilkan nama VM, skor, kategori, alasan, serta pesan ketika gagal atau menunggu.
4. Gunakan CSRF token dari API dan cookie session; jangan menyimpan password/token sesi di localStorage. Skor resmi dihitung backend.
5. Uji tampilan laptop/HP, jalankan npm run build dan commit package-lock.json; jangan commit node_modules atau dist.

## Hasil yang dikumpulkan
Komponen Vue, halaman, service API dan build yang berhasil.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
