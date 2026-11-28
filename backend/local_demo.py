"""Jalankan dari root: python -m backend.local_demo. Khusus laptop pengembangan."""
import getpass
import os
import secrets
from werkzeug.security import generate_password_hash
from .app import create_app

if __name__ == "__main__":
    password = getpass.getpass("Buat password demo lokal (minimal 8 karakter): ")
    if len(password) < 8:
        raise SystemExit("Password demo minimal 8 karakter.")
    os.environ["BANKGUARD_SECRET_KEY"] = secrets.token_hex(32)
    os.environ["BANKGUARD_DEMO_PASSWORD_HASH"] = generate_password_hash(password)
    os.environ.setdefault("BANKGUARD_DEMO_USER", "petugas")
    os.environ["BANKGUARD_COOKIE_SECURE"] = "0"
    create_app().run(host="127.0.0.1", port=8000, debug=False)
