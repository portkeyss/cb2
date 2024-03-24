class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: 
            return -1
        dp = [[float('inf') for j in range(n)] for _ in range(d+1)] #(day, start)
        
        def minDiff(day, start):
            if dp[day][start] < float('inf'): 
                return dp[day][start]
            if day == 1:
                dp[day][start] = max(jobDifficulty[start:])
            else:
                maxVal = jobDifficulty[start]
                for j in range(start, n-day+1):
                    maxVal = max(maxVal, jobDifficulty[j])
                    dp[day][start] = min(dp[day][start], maxVal + minDiff(day-1, j+1))
            return dp[day][start]
        
        return minDiff(d, 0)