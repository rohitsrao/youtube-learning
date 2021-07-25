import unittest

from shopping_basket import Basket
from item import Item

class ShoppingBasketTest(unittest.TestCase):

    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_single_item_should_have_quantity_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)

if __name__ == '__main__':
    pass
