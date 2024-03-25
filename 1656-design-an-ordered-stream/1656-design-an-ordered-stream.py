class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.l = [None]*n
        self.cur = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        if self.cur != idKey: return []
        while self.cur<=self.n and self.l[self.cur-1] is not None:
            self.cur += 1
        return  self.l[idKey-1:self.cur-1]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)