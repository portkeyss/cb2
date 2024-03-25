class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1
        for c in coins:
            if c<=res:
                res += c
            else:
                break
        return res