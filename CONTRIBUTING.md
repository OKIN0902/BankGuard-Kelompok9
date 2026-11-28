# Cara bekerja bersama di GitHub
Repository = folder bersama. Branch = ruang kerja peran. Commit = simpan catatan perubahan. Push = kirim perubahan. Pull = ambil perubahan. Pull Request (PR) = ajukan penggabungan. Merge = gabungkan perubahan setelah diperiksa. Issue = daftar tugas.

## Pertama kali
1. Terima undangan GitHub, instal GitHub Desktop dan VS Code. Tim Vue instal Node.js seri 22 minimal 22.18; tim Python/QA instal Python 3.12. Hanya tim infrastruktur perlu VM.
2. GitHub Desktop → File → Clone repository → pilih BankGuard-Perbankan. Repository → Open in Visual Studio Code.
3. Pilih branch peran yang sudah ada. Baca Issue dan kontrak API sebelum menulis kode.
4. Jika sudah clone sebelumnya, ambil perubahan terbaru. Simpan pekerjaan sendiri dahulu; jangan hapus file hasil kerja tanpa koordinasi.

## Setiap mulai bekerja
1. Pindah main, Fetch/Pull origin, kembali ke branch sendiri, Branch → Merge into current branch → main. Jika konflik, minta bantuan ketua.
2. Edit hanya file tanggung jawab. Frontend dan backend bekerja paralel menggunakan contoh JSON pada kontrak API.
3. Save, uji, periksa Changes, Commit, Push origin.
4. Buat PR dengan base main dan compare branch peran; jelaskan hasil nyata dan Issue terkait. Ketua review, uji dan merge; jangan hapus branch aktif.
5. Jangan push langsung ke main, jangan unggah rahasia/data asli/ISO/VDI/node_modules/dist. Commit package-lock.json setelah npm install berhasil.

Urutan integrasi: kontrak → scoring/database/API dan Vue → tes/build → Nginx/Gunicorn pada template → clone → jaringan → demo. Infrastruktur dapat disiapkan paralel.
