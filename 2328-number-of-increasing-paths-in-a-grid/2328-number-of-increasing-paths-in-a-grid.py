class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ds = [[1,0],[0,1],[-1,0],[0,-1]]
        mod = 10**9+7

        @lru_cache(None)
        def f(r,c):
            ans = 1
            for dr,dc in ds:
                r1, c1 = r+dr, c+dc
                if 0<=r1<m and 0<=c1<n and grid[r1][c1]>grid[r][c]:
                    ans = (ans+f(r1,c1))%mod
            return ans

        res = 0
        for i in range(m):
            for j in range(n):
                res = (res+f(i,j))%mod
        
        return res