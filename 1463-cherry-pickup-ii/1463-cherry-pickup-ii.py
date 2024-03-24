class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {(0,n-1):grid[0][0]+grid[0][-1]}
        ds = [-1,0,1]
        for i in range(1,m):
            t = defaultdict(lambda:-inf)
            for j,k in dp.keys():  
                    for d1 in ds:
                        for d2 in ds:
                            if 0<=j+d1<n and 0<=k+d2<n:
                                cur = grid[i][j+d1]+grid[i][k+d2] if j+d1!=k+d2 else grid[i][j+d1]
                                t[(j+d1,k+d2)] = max(t[(j+d1,k+d2)], dp[(j,k)]+cur)
            dp = t
        return max(dp.values())