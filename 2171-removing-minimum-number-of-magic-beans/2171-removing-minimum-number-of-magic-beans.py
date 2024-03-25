class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        sm = sum(beans)
        n = len(beans)
        res = inf
        prefix = 0
        for i in range(n):
            res = min(res, sm-beans[i]*(n-i))
        return res