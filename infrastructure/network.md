# Rencana jaringan
Laptop host menjalankan VirtualBox. Guest adalah VM di dalamnya. NAT port forwarding: 8081→80 BankGuard-01, 8082→80 BankGuard-02, 8083→80 BankGuard-03. Nginx port 80 menyajikan Vue dan /api diteruskan ke Gunicorn 127.0.0.1:8000. Jangan buka port 8000 ke jaringan.

Awali bind 127.0.0.1 untuk uji laptop host. Untuk perangkat lain, gunakan IP LAN/VPN host yang sesuai dan firewall terbatas. Uji halaman dan /api/health pada URL yang sama. Tailscale opsional; cek kuota dan izin. Jangan buka port router internet. Belum diuji.
