# BankGuard — Kelompok 9

## Apa itu BankGuard?
BankGuard adalah contoh aplikasi perbankan untuk tugas Cloud Computing. Aplikasi memeriksa transaksi transfer fiktif, menghitung skor risiko, lalu menampilkan peringatan agar petugas dapat meninjau transaksi. Aplikasi tidak memblokir rekening dan skor bukan bukti penipuan.

## Apa yang harus dibuat?
- Satu VM template: komputer virtual Ubuntu Server yang sudah dipasang aplikasi BankGuard.
- Tiga VM hasil Full Clone: salinan lengkap dari template, tanpa memasang ulang OS satu per satu.
- Ketiganya menyala bersamaan dan aplikasinya dapat dibuka dari perangkat lain melalui browser.

## Alat yang digunakan
| Alat | Kegunaan |
|---|---|
| VirtualBox | Membuat dan menggandakan komputer virtual |
| Ubuntu Server | Sistem operasi di dalam VM |
| Python 3.12 + Flask/Jinja | Memproses data dan menampilkan halaman web |
| SQLite | Menyimpan transaksi pada setiap VM |
| Gunicorn | Menjalankan server aplikasi di Linux |
| GitHub | Tempat menyimpan dan menggabungkan pekerjaan anggota |

Rancangan awal memakai Cloud Functions dan Firestore. Untuk praktikum VM, keduanya diganti Flask dan SQLite. Database tiap VM terpisah, bukan database terpusat. Lihat [penjelasan arsitektur](docs/architecture.md).

## Cara menghitung skor
| Kondisi | Tambahan skor |
|---|---:|
| Rekening tujuan baru | 40 |
| Nominal lebih dari 3 kali rata-rata historis | 35 |
| Lebih dari 3 transfer dalam 10 menit | 25 |

0–39 RENDAH, 40–59 SEDANG, 60–100 TINGGI. Contoh: transfer Rp10 juta, rata-rata Rp500 ribu, tujuan baru, frekuensi 1 → 40 + 35 + 0 = 75 (TINGGI). Riwayat dan data seluruhnya simulasi.

## Mulai dari sini
1. Baca [cara bekerja bersama di GitHub](CONTRIBUTING.md).
2. Pilih branch (ruang kerja) dan buka Issue (daftar tugas) sesuai peran.
3. Tim kode membaca [panduan teknis](docs/contracts.md) agar nama fungsi dan format data sama.
4. Untuk tim Python, dari folder proyek buat lingkungan terpisah: `python -m venv .venv`, aktifkan venv, lalu `python -m pip install -r requirements.txt`.
5. Setelah kode selesai, jalankan `python -m flask --app bankguard.app:create_app run --port 8000` dan uji dengan `python -m pytest`.

**Status saat ini:** kerangka file sudah tersedia, aplikasi dan VM belum selesai/diuji.

| Tugas | Branch | Panduan |
|---|---|---|
| Mengatur dan menyatukan pekerjaan kelompok | `integration/leader` | [Panduan](docs/roles/leader.md) · [Issue #1](../../issues/1) |
| Menyiapkan Ubuntu dan menjalankan aplikasi | `infra/setup` | [Panduan](docs/roles/setup.md) · [Issue #2](../../issues/2) |
| Menggandakan VM menjadi tiga | `infra/cloning` | [Panduan](docs/roles/cloning.md) · [Issue #3](../../issues/3) |
| Membuat logika aplikasi dan skor risiko | `feature/backend` | [Panduan](docs/roles/backend.md) · [Issue #4](../../issues/4) |
| Membuat tampilan aplikasi di browser | `feature/frontend` | [Panduan](docs/roles/frontend.md) · [Issue #5](../../issues/5) |
| Menyimpan dan membaca data transaksi | `feature/database` | [Panduan](docs/roles/database.md) · [Issue #6](../../issues/6) |
| Menguji aplikasi dan mencatat kesalahan | `test/quality-assurance` | [Panduan](docs/roles/qa.md) · [Issue #7](../../issues/7) |
| Menghubungkan VM dengan browser perangkat lain | `infra/network` | [Panduan](docs/roles/network.md) · [Issue #8](../../issues/8) |
| Menyiapkan dokumentasi dan presentasi | `docs/presentation` | [Panduan](docs/roles/documentation.md) · [Issue #9](../../issues/9) |

## Target demo
Di laptop utama, rencana alamat browser: http://localhost:8081, http://localhost:8082, http://localhost:8083. Masing-masing diteruskan ke port 8000 di VM. Alamat belum aktif. Lihat [checklist demo](docs/demo-checklist.md).

Jangan unggah password, token, data pribadi, database lokal, ISO atau file VM. Matikan VM setelah demo.
