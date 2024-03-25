class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @lru_cache(None)
        def f(p,q):
            if q==0: return 0
            if p==n: return -inf
            ans = f(p+1,q)
            x = 0
            for i in range(min(q,len(piles[p]))):
                x += piles[p][i]
                ans = max(ans, x+f(p+1,q-i-1))
            return ans

        return f(0,k)