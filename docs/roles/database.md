# Menyimpan dan membaca data transaksi

Branch: `feature/database` · [Issue #6](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/6)

## Mulai dari mana?
Baca [cara kolaborasi](../../CONTRIBUTING.md) dan [kontrak API](../contracts.md). Ambil perubahan main ke branch sendiri. File yang dikerjakan: backend/database.py, backend/schema.sql.

## Langkah kerja
1. Buat tabel SQLite sesuai kontrak API. SQLite menyimpan file database terpisah di setiap VM.
2. Buat init_db, save_transaction dan list_transactions sesuai nama dan format di docs/contracts.md.
3. Gunakan parameter SQL, UUID, waktu UTC dan JSON untuk alasan risiko; jangan masukkan input langsung ke SQL.
4. Uji data tetap ada setelah restart dan hasil dapat dibaca oleh Flask.

## Hasil yang dikumpulkan
database.py, schema.sql dan catatan pengujian.

## Tanda selesai
- [ ] Hasil sesuai kontrak API dan sudah diperiksa.
- [ ] Uji aktual dicatat, atau jelaskan jika belum bisa diuji.
- [ ] Commit, push dan buat Pull Request ke main dengan referensi Issue.
- [ ] Ketua memeriksa dan menyetujui.
