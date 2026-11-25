# Panduan teknis bersama v0.1 — sepakati sebelum membuat kode

Panduan ini memastikan kode backend (proses aplikasi), frontend (tampilan) dan database (penyimpanan) dapat disambungkan. Nama fungsi/field di bawah harus tetap sama.

## 1. Data yang dimasukkan
| Nama field | Arti | Format |
|---|---|---|
| user_id | ID pengguna fiktif | string 1–64 karakter |
| amount | Nominal transfer | integer rupiah 1–10^12 |
| historical_average | Rata-rata transfer | integer rupiah 1–10^12 |
| destination_new | Apakah tujuan baru? | boolean true/false |
| transfers_10min | Jumlah transfer 10 menit, termasuk sekarang | integer 1–10^6 |

Riwayat diisi sebagai simulasi. Tolak tipe/nilai yang salah. Integer artinya bilangan bulat; boolean artinya ya/tidak.

## 2. Bagian skor (backend)
Fungsi `risk_engine.score_transaction(amount, historical_average, destination_new, transfers_10min) -> dict` mengembalikan data berbentuk dictionary (pasangan nama dan nilai): score:int, level:str (RENDAH/SEDANG/TINGGI), reasons:list[str]. Reasons hanya memuat indikator aktif dalam urutan: Rekening tujuan baru, Nominal tidak biasa, Frekuensi tinggi. Input salah menimbulkan ValueError. Lebih dari 3 kali dan lebih dari 3 transfer berarti batas tepat 3 tidak mendapat tambahan skor.

Contoh hasil: `{"score":75,"level":"TINGGI","reasons":["Rekening tujuan baru","Nominal tidak biasa"]}`.

## 3. Bagian penyimpanan (SQLite)
- `database.init_db(db_path)`: menyiapkan tabel dan dapat dijalankan kembali tanpa menghapus data.
- `save_transaction(db_path, transaction:dict)->str`: menyimpan seluruh input, score, level dan reasons, lalu mengembalikan ID unik UUID.
- `list_transactions(db_path, limit=100)->list[dict]`: mengambil maksimal 100 transaksi secara default, paling baru dahulu.

Database juga menambahkan id dan created_at (waktu UTC ISO). Simpan reasons sebagai JSON dan boolean sebagai 0/1; gunakan parameter SQL (jangan gabungkan input langsung ke SQL), commit (simpan perubahan database) dan close (tutup koneksi). SQLite lokal tiap VM.

## 4. Bagian aplikasi web
`app.create_app(test_config=None)` membuat aplikasi Flask. Baca pengaturan dari environment (pengaturan lokal sistem): BANKGUARD_SECRET_KEY, BANKGUARD_DEMO_USER, BANKGUARD_DEMO_PASSWORD_HASH (Werkzeug), BANKGUARD_DB_PATH. Jika secret/hash kosong, jangan jalankan aplikasi. CSRF adalah perlindungan formulir dari permintaan palsu: gunakan token pada setiap POST. Session (catatan login) HttpOnly/SameSite=Lax, Secure pada HTTPS; periksa password dengan check_password_hash, session.clear saat login/logout. Dashboard/simulator wajib login.

| Alamat dan metode | Nama endpoint Flask | Data/hasil |
|---|---|---|
| GET / | home | arahkan ke login/dashboard |
| GET/POST /login | login | login.html; username,password,csrf_token; gagal 401 |
| POST /logout | logout | csrf_token; arahkan login |
| GET /dashboard | dashboard | dashboard.html; transactions, instance_name, total, high_count, medium_count, low_count (dari daftar yang tampil) |
| GET/POST /simulator | simulator | simulator.html; input bagian 1, destination_new 0/1, csrf_token; salah 400; sukses simpan lalu arahkan dashboard |
| GET /health | health | JSON status:ok, instance:hostname; 503 jika DB belum siap |

GET untuk membuka halaman, POST untuk mengirim data. Semua template menerima instance_name, error, csrf_token. Gunakan url_for sesuai endpoint dan autoescape Jinja (melindungi tampilan HTML). Skor dihitung pada server, bukan browser.

## 5. Menjalankan di VM
Gunicorn Linux: `gunicorn --bind 0.0.0.0:8000 'bankguard.app:create_app()'`. Jalankan sebagai akun non-root, file environment hanya dapat dibaca pihak berwenang, secret berbeda tiap clone. Jangan gunakan data/password asli.
