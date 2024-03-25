from bisect import bisect_right
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[[-1,0] for _ in range(n+1)] for __ in range(k+1)]
        for i in range(k):
            for j,(s,e,v) in enumerate(events):
                p = bisect_right(dp[i],[s-1,inf])-1
                x = max(dp[i][p][1]+v,dp[i+1][j][1])
                dp[i+1][j+1] = [e,x]
        return dp[k][n][1]