class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def humpSum(idx, val):
            res = 0
            if idx>=val-1:
                res += (1+val)*val//2+(1+idx-val)
            else:
                res += (val-idx+val)*(idx+1)//2
            if idx<=n-val:
                res += (val)*(val-1)//2+(n-idx-val)
            else:
                res += (val-1+val-n+1+idx)*(n-1-idx)//2
            return res
        
        l, r = 1, maxSum
        while l<r:
            m = (l+r+1)//2
            hs = humpSum(index,m)
            if hs<=maxSum:
                l = m
            else:
                r = m-1
        return l