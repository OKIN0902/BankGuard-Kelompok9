# Kontrak API BankGuard v0.2
Kontrak ini adalah kesepakatan nama data dan alamat API supaya Vue, Flask dan SQLite bisa dibuat terpisah lalu disambungkan. Jangan mengubah nama tanpa koordinasi.

## 1. Data transaksi JSON
| Nama | Arti | Format |
|---|---|---|
| user_id | ID pengguna fiktif | string 1–64 karakter |
| amount | Nominal transfer | integer rupiah 1–10^12 |
| historical_average | Rata-rata transfer simulasi | integer rupiah 1–10^12 |
| destination_new | Tujuan baru? | boolean true/false |
| transfers_10min | Jumlah transfer termasuk sekarang | integer 1–10^6 |

Integer = bilangan bulat; boolean = ya/tidak. Tolak angka berbentuk string, boolean sebagai angka, nilai di luar batas, field wajib hilang. Contoh POST /api/transactions:
```json
{"user_id":"USER-001","amount":10000000,"historical_average":500000,"destination_new":true,"transfers_10min":1}
```

## 2. Skor dan database
`backend.risk_engine.score_transaction(amount, historical_average, destination_new, transfers_10min) -> dict` mengembalikan score:int, level:str (RENDAH/SEDANG/TINGGI), reasons:list[str]. Urutan alasan aktif: Rekening tujuan baru (+40), Nominal tidak biasa (+35 jika >3 kali), Frekuensi tinggi (+25 jika >3 transfer). Batas tepat 3 tidak menambah skor; input salah ValueError.

`backend.database.init_db(db_path)` membuat tabel tanpa menghapus data yang sudah ada.
`save_transaction(db_path, transaction:dict)->str` menyimpan input, score, level, reasons, id UUID dan created_at UTC ISO, mengembalikan id.
`list_transactions(db_path, limit=100)->list[dict]` paling baru dahulu; semua field dan id/created_at dikembalikan; reasons list, destination_new boolean. Gunakan parameter SQL, JSON untuk reasons, 0/1 untuk boolean di SQLite, commit dan close. Satu database per VM.

## 3. Alamat API
Frontend selalu meminta alamat relatif /api/... (bukan IP/port tetap). Vite dan Nginx meneruskan /api ke Flask tanpa menghapus awalan /api. Tidak perlu CORS karena satu origin (alamat browser).

| Metode dan URL | Login? | Respons sukses |
|---|---|---|
| GET /api/health | Tidak | 200 {status:"ok", instance:"BankGuard-01"}; 503 jika DB belum siap |
| GET /api/session | Tidak | 200 {authenticated:boolean, username:string/null, csrf_token:string, instance_name:string} |
| POST /api/login | Tidak | 200 {authenticated:true, username:string, csrf_token:string, instance_name:string} |
| POST /api/logout | Ya | 200 {authenticated:false, username:null, csrf_token:string, instance_name:string} |
| GET /api/transactions | Ya | 200 {transactions:[], total:int, high_count:int, medium_count:int, low_count:int, instance_name:string} |
| POST /api/transactions | Ya | 201 {transaction:{...record}} |

Login body JSON: {"username":"petugas","password":"<password demo lokal>"}. Setiap POST termasuk login/logout mengirim header X-CSRF-Token dari GET /api/session atau respons login/logout terbaru. GET session selalu dapat dipakai untuk mengambil token baru. Setelah login/logout, session.clear dan buat token baru. Gunakan hmac.compare_digest untuk pemeriksaan token. Session Flask lewat cookie HttpOnly, SameSite=Lax, Secure jika HTTPS; jangan simpan token sesi/password di localStorage. Aplikasi HTTP hanya untuk jaringan demo tepercaya, bukan internet publik. Password diverifikasi dengan Werkzeug check_password_hash. Semua respons API kesalahan JSON berbentuk {"error":"Pesan mudah dipahami"}; 400 input salah, 401 belum login/login gagal, 403 CSRF salah, 415 Content-Type bukan JSON untuk POST yang memerlukan body, 503 database belum siap. Jangan tampilkan stack trace. GET transaksi menghitung jumlah kategori dari maksimal 100 record yang ditampilkan.

Contoh respons analisis 201 (ID/waktu hanya contoh):
```json
{"transaction":{"id":"550e8400-e29b-41d4-a716-446655440000","created_at":"2026-01-01T00:00:00Z","user_id":"USER-001","amount":10000000,"historical_average":500000,"destination_new":true,"transfers_10min":1,"score":75,"level":"TINGGI","reasons":["Rekening tujuan baru","Nominal tidak biasa"]}}
```

## 4. Pengaturan backend
`backend.app.create_app(test_config=None)` membaca BANKGUARD_SECRET_KEY, BANKGUARD_DEMO_USER, BANKGUARD_DEMO_PASSWORD_HASH, BANKGUARD_DB_PATH, BANKGUARD_COOKIE_SECURE (1 jika HTTPS, 0 untuk demo HTTP). Default DB lokal instance/bankguard.sqlite3; VM memakai /var/lib/bankguard/bankguard.sqlite3. Tanpa secret/hash gagal start dengan pesan aman. Test_config boleh menyediakan nilai uji. Gunicorn: `gunicorn --bind 127.0.0.1:8000 'backend.app:create_app()'`.

## 5. Halaman Vue
/login, /dashboard, /simulator melalui Vue Router. Ambil session saat membuka aplikasi; halaman privat perlu login dan API tetap memeriksa hak akses. Gunakan fetch melalui services/api.js, credentials same-origin, JSON body dan token CSRF. Saat mendapat 401, arahkan login; tampilkan kesalahan dengan aman. Frontend menampilkan data, tidak menentukan skor resmi. Untuk kerja paralel, contoh JSON di atas dapat digunakan sebagai data mock (contoh sementara, bukan hasil pengujian).
