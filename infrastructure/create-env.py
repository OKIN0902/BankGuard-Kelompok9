"""Membuat environment unik secara interaktif; tidak mencetak password/secret."""
import argparse
import getpass
import os
from pathlib import Path
import secrets
import tempfile
from werkzeug.security import generate_password_hash

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replace", action="store_true", help="Ganti environment yang ada (mengakhiri sesi lama).")
    args = parser.parse_args()
    if os.geteuid() != 0:
        raise SystemExit("Jalankan sebagai root di VM.")
    target = Path("/etc/bankguard/bankguard.env")
    target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if target.exists() and not args.replace:
        raise SystemExit("Environment sudah ada; tidak ditimpa. Gunakan --replace bila memang ingin mengganti.")
    password = getpass.getpass("Buat password demo unik (minimal 8 karakter): ")
    if len(password) < 8 or len(password) > 1024:
        raise SystemExit("Panjang password harus 8–1024 karakter.")
    if password != getpass.getpass("Ulangi password: "):
        raise SystemExit("Password tidak cocok.")
    # Hanya nilai yang aman untuk format systemd EnvironmentFile.
    data = (
        f"BANKGUARD_SECRET_KEY={secrets.token_hex(32)}\n"
        "BANKGUARD_DEMO_USER=petugas\n"
        f"BANKGUARD_DEMO_PASSWORD_HASH={generate_password_hash(password)}\n"
        "BANKGUARD_DB_PATH=/var/lib/bankguard/bankguard.sqlite3\n"
        "BANKGUARD_COOKIE_SECURE=0\n"
    )
    fd, name = tempfile.mkstemp(dir=target.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(data)
        os.chmod(name, 0o600)
        os.replace(name, target)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    print("Environment unik dibuat (password dan secret tidak dicetak).")

if __name__ == "__main__":
    main()
