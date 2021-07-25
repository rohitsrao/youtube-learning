import unittest

class Basket():

    def __init__(self, itemsList):
        self.itemList = itemsList

    def total(self):
        return 0

class ShoppingBasketTest(unittest.TestCase):

    def test_empty_basket_total(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

if __name__ == '__main__':
    pass
