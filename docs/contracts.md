# Kontrak teknis v0.1 — sepakati sebelum coding

Input: user_id string fiktif 1–64 karakter, amount dan historical_average integer rupiah 1–10^12, destination_new boolean, transfers_10min integer 1–10^6 termasuk transaksi sekarang. Riwayat diisi simulatif. Tolak tipe/nilai invalid.

`risk_engine.score_transaction(amount, historical_average, destination_new, transfers_10min) -> dict` berisi score:int, level:str (RENDAH/SEDANG/TINGGI), reasons:list[str] berurutan: Rekening tujuan baru, Nominal tidak biasa, Frekuensi tinggi (hanya indikator aktif). ValueError untuk input invalid. Batas ketat >3 kali dan >3 transfer.

`database.init_db(db_path)`, `save_transaction(db_path, transaction:dict)->str`, `list_transactions(db_path, limit=100)->list[dict]` newest first. Record: semua input + score, level, reasons; database menambahkan id UUID dan created_at UTC ISO. JSON reasons, bool 0/1; parameter SQL, commit dan close. SQLite lokal tiap VM.

`app.create_app(test_config=None)` membaca BANKGUARD_SECRET_KEY, BANKGUARD_DEMO_USER, BANKGUARD_DEMO_PASSWORD_HASH (Werkzeug), BANKGUARD_DB_PATH. Tanpa secret/hash gagal start aman. Gunakan CSRF setiap POST, session HttpOnly/SameSite=Lax, Secure pada HTTPS, check_password_hash, session.clear saat login/logout. Dashboard/simulator wajib login.

| Route | Endpoint | Context/form |
|---|---|---|
| GET / | home | redirect login/dashboard |
| GET/POST /login | login | login.html; username,password,csrf_token; gagal 401 |
| POST /logout | logout | csrf_token; redirect login |
| GET /dashboard | dashboard | dashboard.html; transactions, instance_name, total, high_count, medium_count, low_count (dari list yang tampil) |
| GET/POST /simulator | simulator | simulator.html; input di atas, destination_new 0/1, csrf_token; invalid 400; sukses simpan redirect dashboard |
| GET /health | health | JSON status:ok, instance:hostname; 503 jika DB tidak siap |

Semua template menerima instance_name,error,csrf_token; url_for sesuai endpoint; autoescape Jinja. Scoring di server. Gunicorn Linux: `gunicorn --bind 0.0.0.0:8000 'bankguard.app:create_app()'`; service non-root, environment file izin ketat; secret unik per clone. Jangan gunakan data/password asli.
