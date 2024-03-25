class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n = len(points), len(points[0])
        dp = points[0].copy()
        for i in range(1,m):
            t = []
            mx = -inf
            for j in range(n):
                mx = max(mx,dp[j]+j)
                t.append(mx+points[i][j]-j)
            mx = -inf  
            for j in range(n-1,-1,-1):
                mx = max(mx,dp[j]-j)
                t[j] = max(t[j], mx+points[i][j]+j)
            dp = t
        return max(dp)