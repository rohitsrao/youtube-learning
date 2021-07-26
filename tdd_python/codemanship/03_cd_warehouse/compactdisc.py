class CompactDisc:

    def __init__(self, initial_stock):
        self._stock_count = initial_stock

    def get_stock_count(self):
        return self._stock_count

    def buy(self, quantity):
        self._stock_count -= quantity
