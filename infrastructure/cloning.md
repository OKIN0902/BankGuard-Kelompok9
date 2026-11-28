# Full Clone tiga VM di VirtualBox

Prasyarat: template sudah dipasang dan diuji, lalu prepare-template.sh dijalankan sehingga VM mati dan rahasia/data demo bersih. Pastikan ruang disk cukup (disk dinamis dapat membesar).

Pada Windows PowerShell, dari root repo:

    powershell -ExecutionPolicy Bypass -File .\infrastructure\clone.ps1

ExecutionPolicy Bypass hanya untuk proses ini; periksa script dahulu. Full Clone dibuat tanpa opsi linked, MAC baru secara default. Script tidak menimpa VM yang sudah ada. Jika gagal sebagian, periksa VM yang telah dibuat sebelum mengulang; jangan menghapus data tanpa persetujuan. Port host 8081–8083 menuju 80 tiap VM, awalnya bind 127.0.0.1. Untuk demo LAN gunakan parameter -BindIP dengan IP LAN host saat membuat clone.

Nyalakan setiap VM melalui VirtualBox GUI, lalu dari console:
    
    sudo bash /opt/bankguard/infrastructure/init-instance.sh BankGuard-01

Ulangi dengan BankGuard-02 dan BankGuard-03. Pilih password demo yang berbeda dan catat secara privat. Cek hostname, machine-id dan MAC berbeda; machine-id dihasilkan systemd ketika clone boot setelah template dikosongkan. SSH tidak diaktifkan kembali secara otomatis; jika dibutuhkan, aktifkan setelah host key baru dibuat. Jangan boot template lagi selama membuat clone.

Akses host: http://127.0.0.1:8081, 8082, 8083. Jika bind IP LAN, gunakan alamat IP LAN host pada browser host dan perangkat lain. Nyalakan ketiganya bersama, template tetap mati. Catat bukti Full Clone dan akses browser sesungguhnya. Belum diuji pada VirtualBox dari lingkungan ini.
