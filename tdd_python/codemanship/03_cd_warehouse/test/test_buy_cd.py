import unittest

from compactdisc import CompactDisc

class BuyCdTest(unittest.TestCase):

    def test_buy_cd_in_stock(self):
        cd = CompactDisc(10)
        self.assertEqual(5, cd.get_stock_count())


if __name__ == "__main__":
    pass
