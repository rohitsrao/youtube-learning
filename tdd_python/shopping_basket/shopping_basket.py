class Basket():

    def __init__(self, items):
        self.items = items

    def total(self):
        if len(self.items) > 0:
            return self.items[0].unit_price
        return 0


if __name__ == '__main__':
    pass
