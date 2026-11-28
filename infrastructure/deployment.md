# Pemasangan prototype BankGuard pada Ubuntu

Branch referensi: prototype/full-implementation. Jangan gunakan data bank asli. Script disediakan untuk VM Ubuntu Server 24.04 LTS khusus BankGuard; instalasi fisik belum diuji.

## 1. Buat satu VM template
VirtualBox: BankGuard-Template, 2 vCPU, RAM 2 GB, disk dinamis 15 GB, Ubuntu Server 24.04 LTS, adapter 1 NAT. Instal OS sekali saja. Gunakan akun OS demo yang tidak dipakai di sistem lain.

## 2. Siapkan aplikasi
Di komputer pengembang, clone branch prototype/full-implementation; Node.js seri 22 minimal 22.18. Dari frontend jalankan npm install lalu npm run build. Commit lockfile setelah pengujian tim jika akan menerapkan referensi; gunakan npm ci setelah lockfile ada. Salin backend, infrastructure dan frontend/dist beserta struktur folder repo ke VM (mis. SCP jika SSH diaktifkan sementara, shared folder atau media lokal). Jangan menyalin .env, database, node_modules atau .venv pengembang. Node.js tidak diperlukan untuk menjalankan dist di VM.

Di VM, masuk folder proyek:
    
    sudo bash infrastructure/setup.sh
    sudo bash /opt/bankguard/infrastructure/init-instance.sh BankGuard-Template
    sudo systemctl status bankguard --no-pager
    curl http://127.0.0.1/api/health

Init meminta password demo (minimal 8 karakter) tanpa menampilkannya. Username petugas. Secret dan hash baru disimpan root-only pada /etc/bankguard/bankguard.env. SQLite di /var/lib/bankguard/bankguard.sqlite3. Nginx port 80, Gunicorn hanya 127.0.0.1:8000. Jangan buka 8000 melalui NAT.

## 3. Uji template
Buat sementara port forwarding host 8080 → guest 80, bind 127.0.0.1. Buka http://127.0.0.1:8080, login, klik Simulator → Isi contoh demo → Analisis & simpan. Hasil wajib 75 TINGGI. Kembali dashboard, restart VM dan cek data tetap ada. Periksa sudo journalctl -u bankguard jika gagal. Hapus aturan forwarding sementara sebelum cloning.

## 4. Sanitasi template
Cadangkan bukti (tanpa rahasia). Di console VM template, bukan SSH:

    sudo bash /opt/bankguard/infrastructure/prepare-template.sh

Script khusus template menghapus database demo dan environment, menonaktifkan backend/SSH, mengosongkan machine-id dan mematikan VM. Tindakan ini sengaja menghapus data demo; jangan jalankan pada VM yang menyimpan pekerjaan. Jika template perlu diuji lagi, boot dan jalankan init-instance lalu sanitasi lagi sebelum clone.

## 5. Full Clone
Lihat cloning.md dan network.md. Setelah clone, lakukan init-instance di setiap console. Cek nama VM, MAC, machine-id yang berbeda tanpa menampilkan machine-id pada screenshot publik. Setelah tiga VM aktif, uji ulang login, simulasi, dashboard dan health dari host serta perangkat lain.

## 6. Troubleshooting
- nginx -t gagal: periksa situs aktif, jangan hapus konfigurasi kustom.
- 502: periksa systemctl status bankguard; pastikan environment dan database dapat digunakan.
- 503: cek izin /var/lib/bankguard dan journalctl.
- Login gagal: gunakan password demo lokal. Untuk mengganti password/secret, stop bankguard, jalankan sudo /opt/bankguard/.venv/bin/python /opt/bankguard/infrastructure/create-env.py --replace, start bankguard.
- Perangkat lain gagal: cek alamat bind NAT, IP host, firewall dan isolasi Wi-Fi. Jangan buka port router internet.
- HTTP hanya untuk demo LAN tepercaya. Sistem bank nyata memerlukan HTTPS dan kontrol tambahan.
