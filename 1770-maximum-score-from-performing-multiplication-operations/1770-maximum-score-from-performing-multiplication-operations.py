class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)      
        dp = [[0]*(1+m) for _ in range(1+m)]
        for k in range(m-1,-1,-1):
            for i in range(k+1):
                j = i+n-1-k
                dp[i][k] = max(nums[i]*multipliers[k]+dp[i+1][k+1], nums[j]*multipliers[k]+dp[i][k+1])
        return dp[0][0]