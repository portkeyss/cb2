class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cur = None
        prev = -1
        res = 0
        for p in prices:
            if p==prev-1: 
                cur += 1
            else:
                cur = 1
            res += cur
            prev = p
        return res    