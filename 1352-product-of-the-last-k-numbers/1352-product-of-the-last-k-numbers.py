class ProductOfNumbers:

    def __init__(self):
        self.productPrefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.productPrefix = [1]
        else:
            self.productPrefix.append(num*self.productPrefix[-1])

    def getProduct(self, k: int) -> int:
        if k > len(self.productPrefix)-1:
            return 0
        else:
            return self.productPrefix[-1]//self.productPrefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)