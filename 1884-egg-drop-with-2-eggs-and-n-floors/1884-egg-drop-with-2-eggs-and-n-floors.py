class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp=[math.inf]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] = min(dp[i], max(j, 1+dp[i-j]))
        return dp[n]