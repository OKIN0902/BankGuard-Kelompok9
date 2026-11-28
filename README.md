# BankGuard — Kelompok 3 · Perbankan

Prototype akademik Cloud Computing untuk penilaian risiko transaksi fiktif. Branch ini adalah implementasi referensi berbantuan AI, terpisah dari main dan branch tugas anggota. Tidak ada transaksi bank nyata, blokir rekening, AI/ML, notifikasi eksternal atau database terpusat.

## Fitur
Login/logout petugas demo, dashboard transaksi terbaru (maksimal 100), statistik kategori dan distribusi risiko, simulator, skor resmi dari Flask, alasan risiko, penyimpanan SQLite satu tabel dan identitas VM. Vue 3 + Vite + Bootstrap 5 + Vue Router; Python 3.12 + Flask REST API; Nginx + Gunicorn; VirtualBox Ubuntu Server 24.04 LTS.

## Menjalankan di laptop (Windows)
1. Instal Git, Python 3.12 dan Node.js seri 22 minimal 22.18.
2. Clone dan pilih branch referensi:

       git clone -b prototype/full-implementation https://github.com/OKIN0902/BankGuard-Perbankan.git
       cd BankGuard-Perbankan
       py -3.12 -m venv .venv
       .\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
       .\.venv\Scripts\python.exe -m backend.local_demo

   Buat password demo melalui prompt. Username petugas. Backend localhost:8000. Password/secret tidak di-commit, password hanya untuk demo lokal. Server ini untuk pengembangan, bukan produksi.
3. Buka terminal kedua (root repository):

       cd frontend
       npm install
       npm run dev

   Buka http://127.0.0.1:5173. Vite proxy /api ke Flask. Klik Simulator → Isi contoh demo → Analisis & simpan. Skor contoh 75 TINGGI. Untuk build jalankan npm run build. Lockfile belum dapat dibuat dari lingkungan ini karena akses registry diblokir; simpan lockfile hasil instalasi yang diuji sebelum penggunaan berulang.

## Pengujian
Dari root (venv terpasang):

    .\.venv\Scripts\python.exe -m pytest -q

Tes scoring/database tanpa Flask/pytest juga dapat dijalankan dengan Python standar (SQLite dengan STRICT/JSON, seperti Ubuntu 24.04):

    python -m unittest discover -s tests -p test_risk.py
    python -m unittest discover -s tests -p test_database.py

Lihat docs/test-report.md untuk status aktual. Jangan menganggap tes lulus sebelum benar-benar dijalankan.

## Deployment dan demo
- [Kontrak API v0.2](docs/contracts.md) dan [ERD](docs/erd.md)
- [Panduan instalasi Ubuntu](infrastructure/deployment.md)
- [Full Clone](infrastructure/cloning.md) dan [jaringan](infrastructure/network.md)
- [Checklist demo](docs/demo-checklist.md)

Browser → Nginx port 80 (Vue dist) → /api → Gunicorn 127.0.0.1:8000 → Flask → SQLite lokal. Template diuji lalu disanitasi dan dimatikan sebelum clone. Tiga full clone: BankGuard-01/02/03, port host 8081/8082/8083 ke guest 80, setiap clone punya identitas dan secret baru.

Aturan: tujuan baru +40; nominal >3 kali rata-rata +35; frekuensi >3 dalam 10 menit +25. RENDAH 0–39, SEDANG 40–59, TINGGI 60–100. Skor bukan bukti penipuan. Riwayat/frekuensi adalah input manual fiktif. HTTP hanya untuk jaringan demo tepercaya.

Deadline kelompok 30 November 2026, 23.59 WIB. [Issues anggota](https://github.com/OKIN0902/BankGuard-Perbankan/issues) tetap terpisah; jangan merge referensi tanpa review ketua.
