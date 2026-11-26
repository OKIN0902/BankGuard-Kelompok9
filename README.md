# BankGuard — Kelompok 9

BankGuard adalah prototype akademik Cloud Computing untuk memeriksa transaksi transfer fiktif dan menampilkan peringatan risiko kepada petugas. Skor bukan bukti penipuan; tidak ada pemblokiran rekening.

## Target tugas
Satu VM template Ubuntu Server dengan aplikasi BankGuard, tiga VM hasil Full Clone (salinan lengkap tanpa instal ulang), dan akses ketiganya melalui browser perangkat lain.

## Teknologi yang digunakan
| Alat | Kegunaan |
|---|---|
| Vue.js 3 | Membuat halaman web interaktif |
| Vite | Menjalankan frontend saat pengembangan dan membuat file siap dipasang |
| Bootstrap 5 | Membantu desain halaman |
| Flask REST API (Python 3.12) | Memproses transaksi dan mengirim data JSON |
| SQLite | Menyimpan transaksi pada masing-masing VM |
| Nginx | Menyajikan frontend dan meneruskan permintaan API |
| Gunicorn | Menjalankan Flask di Ubuntu |
| VirtualBox + Ubuntu Server 24.04 LTS | Membuat template dan tiga VM |
| GitHub | Kolaborasi remote |

## Cara kerja
Browser membuka Vue lewat Nginx (port 80), Vue meminta data melalui /api, Nginx meneruskan ke Gunicorn/Flask (127.0.0.1:8000), lalu Flask membaca/menyimpan data di SQLite. Setiap VM punya database sendiri, berbeda dari Firestore terpusat pada rancangan awal.

## Aturan skor
Tujuan baru +40; nominal lebih dari 3 kali rata-rata +35; lebih dari 3 transfer dalam 10 menit +25. RENDAH 0–39, SEDANG 40–59, TINGGI 60–100. Contoh Rp10 juta, rata-rata Rp500 ribu, tujuan baru, frekuensi 1 = 75 TINGGI. Semua data dan ambang hanya simulasi.

## Mulai bekerja
Baca [cara kolaborasi](CONTRIBUTING.md), [kontrak API](docs/contracts.md) dan panduan peran. Branch sudah dibuat; jangan push langsung ke main.

Frontend: instal Node.js seri 22 minimal 22.18, lalu dari folder frontend:
```bash
npm install
npm run dev
npm run build
```
Setelah dependensi diuji, commit package-lock.json dan gunakan npm ci untuk instalasi berikutnya. Server Vite pada 127.0.0.1:5173 meneruskan /api ke 127.0.0.1:8000.

Backend (dari root proyek, Windows PowerShell):
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
```
Set pengaturan lokal sesuai [kontrak API](docs/contracts.md), kemudian setelah backend selesai:
```powershell
.\.venv\Scripts\python.exe -m flask --app backend.app:create_app run --host 127.0.0.1 --port 8000
.\.venv\Scripts\python.exe -m pytest
```

**Status:** kerangka frontend, backend dan contoh konfigurasi infrastruktur. Aplikasi lengkap, build dan deployment belum teruji. Lihat Issues.

| Tugas | Branch | Panduan |
|---|---|---|
| Mengatur dan menyatukan pekerjaan kelompok | `integration/leader` | [Panduan](docs/roles/leader.md) · [Issue #1](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/1) |
| Menyiapkan Ubuntu dan server aplikasi | `infra/setup` | [Panduan](docs/roles/setup.md) · [Issue #2](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/2) |
| Menggandakan satu VM menjadi tiga | `infra/cloning` | [Panduan](docs/roles/cloning.md) · [Issue #3](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/3) |
| Membuat API dan logika skor risiko | `feature/backend` | [Panduan](docs/roles/backend.md) · [Issue #4](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/4) |
| Membuat tampilan Vue di browser | `feature/frontend` | [Panduan](docs/roles/frontend.md) · [Issue #5](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/5) |
| Menyimpan dan membaca data transaksi | `feature/database` | [Panduan](docs/roles/database.md) · [Issue #6](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/6) |
| Menguji aplikasi dan mencatat kesalahan | `test/quality-assurance` | [Panduan](docs/roles/qa.md) · [Issue #7](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/7) |
| Membuka aplikasi dari perangkat lain | `infra/network` | [Panduan](docs/roles/network.md) · [Issue #8](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/8) |
| Menyiapkan PPT dan bukti demo | `docs/presentation` | [Panduan](docs/roles/documentation.md) · [Issue #9](https://github.com/OKIN0902/BankGuard-Kelompok9/issues/9) |

## Demo
Host localhost:8081/8082/8083 → Nginx port 80 pada setiap VM. [Panduan pemasangan](infrastructure/deployment.md) dan [checklist demo](docs/demo-checklist.md). Jangan unggah kredensial, database, file VM, data pribadi, node_modules atau dist. Matikan VM setelah demo.
