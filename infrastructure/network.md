# Akses browser dari perangkat lain

| VM | Port host | Port guest |
|---|---:|---:|
| BankGuard-01 | 8081 | 80 |
| BankGuard-02 | 8082 | 80 |
| BankGuard-03 | 8083 | 80 |

Nginx menerima HTTP di port 80 VM, meneruskan /api ke Gunicorn 127.0.0.1:8000. Tidak perlu membuka 8000.

1. Uji host terlebih dahulu. Default clone.ps1 bind ke 127.0.0.1. Buka browser pada host dan cek /api/health.
2. Untuk demo LAN, cari IPv4 host dengan ipconfig. Jika sudah membuat VM, matikan VM dan ubah Host IP pada VirtualBox Settings → Network → Adapter 1 → Advanced → Port Forwarding menjadi IP LAN host. Port tetap 8081–8083 ke 80. Jika membuat clone baru, gunakan clone.ps1 -BindIP IP-LAN-HOST.
3. Windows Firewall: izinkan TCP 8081–8083 hanya pada profil Private dan jaringan tepercaya. Contoh PowerShell sebagai Administrator (ganti IP host sesuai kondisi):

       New-NetFirewallRule -DisplayName "BankGuard Demo LAN" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8081,8082,8083 -LocalAddress 192.168.1.10 -RemoteAddress LocalSubnet -Profile Private

4. Dari perangkat lain satu jaringan, buka http://IP-HOST:8081, :8082, :8083. Uji login, simulator dan /api/health. Nama VM harus berbeda.
5. Setelah demo, hapus rule yang dibuat: Remove-NetFirewallRule -DisplayName "BankGuard Demo LAN". Matikan VM.
6. Tailscale opsional untuk beda lokasi: gunakan hanya dengan izin dan konfigurasi akses terbatas. Jangan forward port router atau mempublikasikan sistem HTTP ke internet.

Jaringan kampus dapat memblokir komunikasi antarperangkat. Siapkan jaringan demo tepercaya alternatif. Tidak ada data bank asli; semua password khusus demo.
