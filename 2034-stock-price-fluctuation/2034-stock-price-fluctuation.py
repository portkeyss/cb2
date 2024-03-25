from sortedcontainers import SortedDict,SortedList
class StockPrice:

    def __init__(self):
        self.stock = SortedDict()
        self.prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.stock:
            self.prices.remove(self.stock[timestamp])
        self.stock[timestamp] = price
        self.prices.add(price)

    def current(self) -> int:
        return self.stock.peekitem()[1]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()