class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        A = sorted((a,s) for a,s in zip(ages,scores))
        n = len(A)
        dp = [0]*n
        for j in range(n):
            dp[j] = A[j][1]
            for i in range(j):
                if A[i][1]<=A[j][1]:
                    dp[j] = max(dp[j],dp[i]+A[j][1])
        return max(dp)   