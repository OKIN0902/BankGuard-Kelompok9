# Cara kerja BankGuard

Rancangan awal: simulator mengirim transaksi ke Cloud Functions untuk menghitung skor; Firestore menyimpan profil dan hasil; dashboard menampilkan peringatan. Firebase Auth dan IAM mengatur akses.

Prototype praktikum: browser → Flask/Jinja (aplikasi web) → aturan skor → SQLite (file database lokal). Aplikasi dipasang pada Ubuntu di VirtualBox, kemudian VM template digandakan tiga kali. Setiap VM punya database sendiri. Riwayat dan login hanya simulasi, bukan sistem bank sungguhan. Perbedaan ini perlu dijelaskan pada presentasi.
