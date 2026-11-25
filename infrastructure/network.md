# Rencana jaringan
Laptop host adalah laptop yang menjalankan VirtualBox. Guest adalah VM di dalamnya. NAT port forwarding meneruskan koneksi port host 8081, 8082, 8083 ke port 8000 di masing-masing guest.

Awali dengan alamat 127.0.0.1 (hanya laptop sendiri). Untuk perangkat lain, gunakan IP LAN/VPN host yang sesuai dan batasi firewall. Jangan buka port router ke internet. Tailscale opsional untuk jaringan privat jarak jauh; cek izin dan kuota. Status: belum diuji.
