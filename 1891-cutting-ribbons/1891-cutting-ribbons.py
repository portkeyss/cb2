class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 0
        r = max(ribbons)
        def f(length):
            return sum(r//length for r in ribbons)
        while l<r:
            m = (l+r+1)//2
            ct = f(m)
            if ct>=k:
                l = m
            else:
                r = m-1
        return l