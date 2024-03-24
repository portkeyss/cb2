class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n<m*k: return -1
        
        def f(x):
            cur = 0
            bq = 0
            for d in bloomDay:
                if x>=d: 
                    cur+=1
                    if cur==k:
                        bq += 1
                        cur = 0
                else:
                    cur = 0
            return bq
        
        l, r = min(bloomDay), max(bloomDay)
        while l<r:
            mid = (l+r)//2
            if f(mid)>=m:
                r = mid
            else:
                l = mid+1
        return l