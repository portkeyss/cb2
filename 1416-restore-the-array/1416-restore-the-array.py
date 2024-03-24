class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9+7
        n = len(s)
        ks = str(k)
        m = len(ks)

        @lru_cache(None)
        def f(i):
            if i==n: return 1
            if s[i]=="0": return 0
            ans = 0
            for j in range(i+1, min(n,i+m)+1):
                if j<i+m or ks>=s[i:j]:
                    ans = (ans+f(j))%mod
            return ans

        return f(0)