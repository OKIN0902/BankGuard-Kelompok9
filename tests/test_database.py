import tempfile
from pathlib import Path
import unittest
import sqlite3
from backend import database
from backend.risk_engine import score_transaction


class DatabaseTest(unittest.TestCase):
    def test_persistence_and_parameterization(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "instance" / "demo.sqlite3"
            database.init_db(path)
            row = dict(user_id="A'--", amount=301, historical_average=100,
                       destination_new=True, transfers_10min=3)
            row.update(score_transaction(301,100,True,3))
            first = database.save_transaction(path,row)
            second = database.save_transaction(path,row)
            self.assertNotEqual(first,second)
            database.init_db(path)
            records = database.list_transactions(path)
            self.assertEqual([x["id"] for x in records],[second,first])
            self.assertEqual(database.get_transaction(path,first)["reasons"],row["reasons"])
            self.assertIs(records[0]["destination_new"],True)
            self.assertEqual(records[0]["user_id"],"A'--")
            with sqlite3.connect(path) as conn:
                self.assertEqual(conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(),[("transactions",)])
            self.assertEqual(len(database.list_transactions(path,1)),1)
