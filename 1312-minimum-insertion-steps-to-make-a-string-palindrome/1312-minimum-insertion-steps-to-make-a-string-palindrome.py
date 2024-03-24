class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def f(i,j):
            if j-i<1: return 0
            if s[i]==s[j]:
                return f(i+1,j-1)
            p = 1+f(i,j-1)
            q = 1+f(i+1,j)
            return min(p,q)
        return f(0,len(s)-1)