class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        res = 0
        p = 0
        for i in range(1,1+n):
            if i&(i-1)==0: p += 1
            res = ((res<<p)%mod+i)%mod
        return res