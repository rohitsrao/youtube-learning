from functools import reduce

class Basket():

    def __init__(self, items):
        self.items = items

    def total(self):
        return reduce(lambda subtotal, item: subtotal + item.quantity*item.unit_price, self.items, 0.0)


if __name__ == '__main__':
    pass
