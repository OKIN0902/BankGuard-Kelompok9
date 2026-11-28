"""SQLite lokal; setiap operasi menutup koneksinya."""
from contextlib import closing
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from uuid import uuid4

SCHEMA = Path(__file__).with_name("schema.sql")
FIELDS = ("user_id", "amount", "historical_average", "destination_new",
          "transfers_10min", "score", "level", "reasons")


def _connect(db_path):
    conn = sqlite3.connect(str(db_path), timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    with closing(_connect(db_path)) as conn, conn:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))


def save_transaction(db_path, transaction):
    record = {key: transaction[key] for key in FIELDS}
    record["id"] = str(uuid4())
    record["created_at"] = datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")
    record["destination_new"] = int(record["destination_new"])
    record["reasons"] = json.dumps(record["reasons"], ensure_ascii=False)
    with closing(_connect(db_path)) as conn, conn:
        conn.execute(
            """INSERT INTO transactions
               (id,user_id,amount,historical_average,destination_new,transfers_10min,score,level,reasons,created_at)
               VALUES (:id,:user_id,:amount,:historical_average,:destination_new,:transfers_10min,:score,:level,:reasons,:created_at)""",
            record,
        )
    return record["id"]


def _decode(row):
    result = dict(row)
    result["destination_new"] = bool(result["destination_new"])
    result["reasons"] = json.loads(result["reasons"])
    return result


def get_transaction(db_path, transaction_id):
    with closing(_connect(db_path)) as conn:
        row = conn.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,)).fetchone()
        return _decode(row) if row is not None else None


def list_transactions(db_path, limit=100):
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError("Limit harus 1–100.")
    with closing(_connect(db_path)) as conn:
        rows = conn.execute(
            "SELECT * FROM transactions ORDER BY created_at DESC, id DESC LIMIT ?", (limit,)
        ).fetchall()
        return [_decode(row) for row in rows]
