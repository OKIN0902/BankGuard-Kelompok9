# Status pengujian implementasi referensi — 28 November 2026
Pengujian lokal terhadap salinan file sumber yang SHA blob-nya cocok dengan GitHub: Python 3.13.5, SQLite 3.46.1, empat tes unittest lulus. Target deployment tetap Python 3.12 pada Ubuntu Server 24.04. Nginx -t berhasil dengan konfigurasi server yang sama dalam konfigurasi uji terisolasi; bash -n setup.sh berhasil. Tidak ada layanan VM yang dipasang/dijalankan oleh pengujian ini.

| Uji | Target | Status aktual |
|---|---|---|
| Risk engine | 8 skor, batas, input salah, skor contoh 75 | Lulus 3 tes unittest (termasuk subtes) |
| SQLite | persistensi, satu tabel, parameter SQL, UUID, pengurutan | Lulus 1 tes unittest |
| Nginx | sintaks konfigurasi | Lulus nginx -t terisolasi; routing runtime belum diuji |
| setup.sh | sintaks Bash | Lulus bash -n; instalasi belum diuji |
| Flask API | login/session/CSRF, 400/401/403/415/503, simpan data | Tes disediakan, belum dijalankan lokal (Flask tidak tersedia) |
| Vue | npm run build, login/dashboard/simulator | Belum diuji build/browser (registry npm tidak dapat diakses) |
| Nginx/Gunicorn | /api/health dan UI melalui port 80 | Belum diuji pada VM |
| Full Clone | 3 VM, identitas unik, tanpa instal ulang | Belum diuji (VirtualBox/PowerShell tidak tersedia) |
| Jaringan | akses browser dari perangkat lain | Belum diuji |

Lingkungan pembuat tidak dapat mengunduh paket Python/npm. Lockfile npm belum dibuat. Jalankan pytest dan npm install/npm run build pada laptop atau CI dengan akses dependensi. Isi hasil aktual dan bukti setelah menjalankan perintah pada README/deployment.md. Jangan unggah kredensial, data asli atau file VM. PRD bukan bukti bahwa demo sudah lulus.
