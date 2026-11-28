# Membuat API dan logika skor risiko

Branch: `feature/backend` · [Issue #4](https://github.com/OKIN0902/BankGuard-Perbankan/issues/4)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: backend/app.py, backend/risk_engine.py.

## Langkah kerja
1. Buat Flask REST API (alamat web yang menerima dan mengirim JSON) sesuai docs/contracts.md.
2. Hitung skor tujuan baru +40, nominal >3 kali rata-rata +35, frekuensi >3 dalam 10 menit +25. Validasi input di server.
3. Buat API session/login/logout, CSRF, daftar transaksi, analisis transaksi dan health. Gunakan cookie session; tidak perlu CORS karena frontend dan API satu alamat.
4. Hubungkan ke fungsi database. Uji API sebelum dihubungkan dengan Vue.

## Hasil yang dikumpulkan
app.py, risk_engine.py dan hasil uji API.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
