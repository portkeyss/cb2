class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        A = [min(cost[i][j] for i in range(m)) for j in range(n)]
        
        @lru_cache(None)
        def f(k,mask):
            if k>=m:
                res = 0
                for i in range(n):
                    if (1<<i)&mask==0:
                        res += A[i]
                return res
            res = inf
            for i in range(n):
                res = min(res,cost[k][i]+f(k+1,mask|(1<<i)))
            return res
        
        return f(0,0)