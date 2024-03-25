class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        cuboids = sorted(sorted(x) for x in cuboids)
        cuboids = [[0,0,0]]+cuboids
        dp = [0]*(n+1)
        for j in range(1,n+1):
            for i in range(j):
                if all(x>=y for x,y in zip(cuboids[j],cuboids[i])):
                    dp[j] = max(dp[j],dp[i]+cuboids[j][2])
        return max(dp)