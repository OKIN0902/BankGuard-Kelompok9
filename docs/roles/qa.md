# Quality assurance

Branch: `test/quality-assurance`

Baca [panduan kolaborasi](../../CONTRIBUTING.md) dan [kontrak](../contracts.md). Sinkronkan main. File: tests/, docs/test-report.md.

## Tugas
Uji delapan kombinasi skor, batas nominal/frekuensi, input invalid, autentikasi, persistensi, tiga VM serta browser perangkat lain. Catat expected vs actual.

Kasus skor: 0,25,35,40,60,65,75,100. Rata-rata 500000: nominal 1500000 tidak aktif, 1500001 aktif; frekuensi 3 tidak aktif, 4 aktif.

## Selesai jika
- [ ] Output sesuai kontrak
- [ ] Uji aktual atau catat blocker
- [ ] Commit, push, PR ke main dengan referensi Issue
- [ ] Review ketua
