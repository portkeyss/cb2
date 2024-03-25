from sortedcontainers import SortedList
class MRUQueue:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.clock = 1
        while self.clock<=n:
            self.sl.add((self.clock,self.clock))
            self.clock += 1

    def fetch(self, k: int) -> int:
        ans = self.sl.pop(k-1)[1]
        self.sl.add((self.clock,ans))
        self.clock += 1
        return ans


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)