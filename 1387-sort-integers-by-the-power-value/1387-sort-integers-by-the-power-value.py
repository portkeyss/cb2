class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(None)
        def f(num):
            if num==1: return 0
            if num%2==0:
                return 1+f(num//2)
            return 1+f(3*num+1)
        
        l = [x for x in range(lo,hi+1)]
        l.sort(key=lambda x:f(x))
        return l[k-1]