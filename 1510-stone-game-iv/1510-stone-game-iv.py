class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def f(k):
            m = floor(sqrt(k))
            if m*m==k: return True
            for p in range(1,m+1):
                if not f(k-p*p): return True
            return False
        return f(n)