# Status pengujian implementasi referensi
Kode dan tes disediakan. Lingkungan pembuat tidak dapat mengunduh paket Python/npm; Flask dan paket Vue/Vite belum tersedia, sehingga pytest penuh dan build npm belum terverifikasi. VirtualBox/Ubuntu host dan PowerShell tidak tersedia di lingkungan pengujian. Jangan menganggap prototype lulus demo.

| Uji | Target | Status |
|---|---|---|
| Risk engine | 8 skor, batas, input salah | Tes disediakan |
| SQLite | persistensi, satu tabel, parameter SQL | Tes disediakan |
| Flask API | login/session/CSRF, 400/401/403/415/503, simpan data | Tes disediakan, belum dijalankan penuh |
| Vue | npm run build, login/dashboard/simulator | Belum diuji build/browser |
| Nginx/Gunicorn | /api/health dan UI melalui port 80 | Belum diuji pada VM |
| Full Clone | 3 VM, identitas unik, tanpa instal ulang | Belum diuji |
| Jaringan | akses browser dari perangkat lain | Belum diuji |

Isi hasil aktual dan bukti setelah menjalankan perintah pada README/deployment.md. Jangan unggah kredensial, data asli atau file VM.
