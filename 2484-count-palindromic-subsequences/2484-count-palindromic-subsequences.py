class Solution:
    def countPalindromes(self, s: str) -> int:
        s = [int(ch) for ch in s]
        mod = 10**9+7
        def findPrefix(t):
            m = len(t)
            p1 = [[0]*10 for _ in range(m)]
            p2 = [[[0]*10 for _ in range(10)] for __ in range(m)]
            for k in range(m):
                for j in range(10):
                    for i in range(10): 
                        p2[k][i][j] = ((p2[k-1][i][j] if k>0 else 0)+(j==t[k])*(p1[k-1][i] if k>0 else 0))%mod
                for j in range(10):
                    p1[k][j] = ((p1[k-1][j] if k>0 else 0) + (j==t[k]))%mod
            return p2

        prefix = findPrefix(s)
        suffix = findPrefix(s[::-1])[::-1]
        
        n = len(s)
        res = 0
        for k in range(2,n-2):
            for i in range(10):
                for j in range(10):
                    res = (res+prefix[k-1][i][j]*suffix[k+1][i][j])%mod
        return res