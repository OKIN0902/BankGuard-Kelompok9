import itertools
import unittest
from backend.risk_engine import score_transaction


class RiskTest(unittest.TestCase):
    def test_all_combinations(self):
        expected = {(False,False,False):0,(False,False,True):25,(False,True,False):35,
                    (True,False,False):40,(False,True,True):60,(True,False,True):65,
                    (True,True,False):75,(True,True,True):100}
        for new, large, frequent in itertools.product((False,True), repeat=3):
            with self.subTest(new=new, large=large, frequent=frequent):
                result = score_transaction(301 if large else 300, 100, new, 4 if frequent else 3)
                score = expected[new,large,frequent]
                self.assertEqual(result["score"], score)
                self.assertEqual(result["level"], "TINGGI" if score>=60 else "SEDANG" if score>=40 else "RENDAH")
                self.assertEqual(len(result["reasons"]), sum((new,large,frequent)))

    def test_example(self):
        self.assertEqual(score_transaction(10000000,500000,True,1),
                         {"score":75,"level":"TINGGI","reasons":["Rekening tujuan baru","Nominal tidak biasa"]})

    def test_invalid(self):
        for args in [(True,100,False,1),(0,100,False,1),(1,0,False,1),
                     (1,100,1,1),(1,100,False,0),(1,100,False,1.0),
                     ("1",100,False,1),(10**12+1,100,False,1),(1,100,False,10**6+1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                score_transaction(*args)
