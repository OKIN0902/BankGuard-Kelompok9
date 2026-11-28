"""Flask REST API sesuai kontrak v0.2."""
from datetime import timedelta
from functools import wraps
import hashlib
import hmac
import os
import secrets
import socket
import sqlite3

from flask import Flask, jsonify, request, session
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash
from . import database
from .risk_engine import score_transaction


def create_app(test_config=None):
    app = Flask(__name__)
    instance_name = socket.gethostname()
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("BANKGUARD_SECRET_KEY"),
        BANKGUARD_DEMO_USER=os.environ.get("BANKGUARD_DEMO_USER", "petugas"),
        BANKGUARD_DEMO_PASSWORD_HASH=os.environ.get("BANKGUARD_DEMO_PASSWORD_HASH"),
        BANKGUARD_DB_PATH=os.environ.get("BANKGUARD_DB_PATH", "instance/bankguard.sqlite3"),
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.environ.get("BANKGUARD_COOKIE_SECURE") == "1",
        # Cookie berbeda antar VM, karena port bukan bagian dari ruang lingkup cookie.
        SESSION_COOKIE_NAME="bankguard_" + hashlib.sha256(instance_name.encode()).hexdigest()[:12],
        PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
        MAX_CONTENT_LENGTH=64 * 1024,
        INSTANCE_NAME=instance_name,
    )
    if test_config is not None:
        app.config.update(test_config)
    if not app.config["SECRET_KEY"] or not app.config["BANKGUARD_DEMO_PASSWORD_HASH"]:
        raise RuntimeError("Atur secret key dan hash password BankGuard sebelum menjalankan server.")
    if not app.config["BANKGUARD_DEMO_USER"]:
        raise RuntimeError("Nama petugas demo tidak boleh kosong.")
    db = app.config["BANKGUARD_DB_PATH"]
    instance = app.config["INSTANCE_NAME"]
    try:
        database.init_db(db)
    except (OSError, sqlite3.Error):
        app.logger.error("Database belum siap saat startup; periksa izin dan lokasi.")

    def error(message, status):
        return jsonify(error=message), status

    def csrf_token():
        if not session.get("csrf_token"):
            session["csrf_token"] = secrets.token_urlsafe(32)
        return session["csrf_token"]

    def session_payload():
        username = session.get("username")
        return dict(authenticated=bool(username), username=username,
                    csrf_token=csrf_token(), instance_name=instance)

    @app.before_request
    def protect_post():
        if request.path.startswith("/api/") and request.method == "POST":
            actual = request.headers.get("X-CSRF-Token", "")
            expected = session.get("csrf_token")
            if not expected or not hmac.compare_digest(actual.encode("utf-8"), expected.encode("utf-8")):
                return error("Token keamanan tidak valid. Muat ulang halaman.", 403)

    @app.after_request
    def protect_response(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response

    @app.errorhandler(HTTPException)
    def http_error(exc):
        messages = {400: "Data JSON tidak valid.", 404: "Alamat tidak ditemukan.",
                    405: "Metode tidak diizinkan.", 413: "Data terlalu besar.", 415: "Gunakan JSON."}
        return error(messages.get(exc.code, "Permintaan tidak dapat diproses."), exc.code)

    @app.errorhandler(sqlite3.Error)
    @app.errorhandler(OSError)
    def database_error(exc):
        app.logger.error("Operasi penyimpanan gagal: %s", type(exc).__name__)
        return error("Database belum siap. Hubungi pengelola VM.", 503)

    @app.errorhandler(500)
    def internal_error(exc):
        return error("Terjadi kesalahan internal.", 500)

    def login_required(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            if not session.get("username"):
                return error("Silakan login terlebih dahulu.", 401)
            return fn(*args, **kwargs)
        return wrapped

    def json_object():
        if not request.is_json:
            return None, error("Gunakan Content-Type application/json.", 415)
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return None, error("Data harus berupa objek JSON.", 400)
        return data, None

    @app.get("/api/health")
    def health():
        database.list_transactions(db, limit=1)
        return jsonify(status="ok", instance=instance)

    @app.get("/api/session")
    def session_status():
        return jsonify(session_payload())

    @app.post("/api/login")
    def login():
        data, failure = json_object()
        if failure:
            return failure
        username, password = data.get("username"), data.get("password")
        if not isinstance(username, str) or not isinstance(password, str) or not username or not password or len(username) > 128 or len(password) > 1024:
            return error("Nama pengguna dan password harus diisi dengan benar.", 400)
        valid_password = check_password_hash(app.config["BANKGUARD_DEMO_PASSWORD_HASH"], password)
        if username != app.config["BANKGUARD_DEMO_USER"] or not valid_password:
            return error("Nama pengguna atau password salah.", 401)
        session.clear()
        session["username"] = username
        session.permanent = True
        return jsonify(session_payload())

    @app.post("/api/logout")
    @login_required
    def logout():
        session.clear()
        return jsonify(session_payload())

    @app.get("/api/transactions")
    @login_required
    def transactions():
        rows = database.list_transactions(db)
        return jsonify(transactions=rows, total=len(rows),
                       high_count=sum(x["level"] == "TINGGI" for x in rows),
                       medium_count=sum(x["level"] == "SEDANG" for x in rows),
                       low_count=sum(x["level"] == "RENDAH" for x in rows),
                       instance_name=instance)

    @app.post("/api/transactions")
    @login_required
    def create_transaction():
        data, failure = json_object()
        if failure:
            return failure
        fields = ("user_id", "amount", "historical_average", "destination_new", "transfers_10min")
        if any(key not in data for key in fields):
            return error("Semua kolom transaksi wajib diisi.", 400)
        user = data["user_id"]
        if not isinstance(user, str) or not 1 <= len(user) <= 64 or not user.strip():
            return error("ID pengguna fiktif harus 1–64 karakter.", 400)
        record = {key: data[key] for key in fields}
        try:
            record.update(score_transaction(record["amount"], record["historical_average"],
                                            record["destination_new"], record["transfers_10min"]))
        except ValueError as exc:
            return error(str(exc), 400)
        transaction_id = database.save_transaction(db, record)
        return jsonify(transaction=database.get_transaction(db, transaction_id)), 201

    return app
