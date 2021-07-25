import unittest

from shopping_basket import Basket

class ShoppingBasketTest(unittest.TestCase):

    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

if __name__ == '__main__':
    pass
