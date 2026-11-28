# Status pengujian implementasi referensi — 28 November 2026
**GitHub Actions: sukses.** [Lihat run dan log pengujian](https://github.com/OKIN0902/BankGuard-Perbankan/actions/runs/46107674584), commit kode yang diuji: 0fb3146dcae84812a7d917a98768c11c3fc41752.

| Uji | Status aktual |
|---|---|
| Python 3.12 / pytest | Lulus: 18 tes dan 17 subtes, termasuk 8 kombinasi skor, batas, validasi, skor contoh 75, autentikasi, CSRF, persistensi, dan database tidak siap |
| Vue/Vite | npm install dan npm run build berhasil; Vite 7.3.8, 35 modul; belum diuji browser secara langsung |
| Bash | bash -n setup.sh, init-instance.sh, prepare-template.sh lulus |
| PowerShell | Parser clone.ps1 lulus; belum menjalankan VirtualBox |
| Nginx | nginx -t lokal dalam konfigurasi uji terisolasi lulus; routing runtime belum diuji |
| Nginx/Gunicorn pada VM | Belum diuji |
| Full Clone | Belum diuji pada VirtualBox; tiga VM, identitas unik dan akses browser perlu bukti asli |
| Jaringan | Belum diuji dari perangkat lain |

Pengujian lokal tambahan terhadap salinan file sumber dengan SHA blob yang cocok: Python 3.13.5, SQLite 3.46.1, 4 tes unittest lulus. Lingkungan pembuat tidak dapat mengunduh paket, tetapi GitHub Actions dapat menjalankan instalasi dan build pada Ubuntu 24.04. Workflow memberi peringatan deprecation Node.js 20 pada versi action lama; tidak ada kegagalan tes. Lockfile npm belum disimpan; buat dan commit setelah tim memilih versi yang akan dipakai. Build CI tidak menyimpan dist sebagai artefak, jadi jalankan npm run build untuk deployment.

Isi bukti runtime pada docs/demo-checklist.md setelah menjalankan panduan deployment. Jangan unggah kredensial, data asli, atau file VM. Aplikasi adalah simulasi akademik dan tidak membuktikan kesiapan sistem bank produksi.
