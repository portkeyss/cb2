class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[inf]*(n+1) for _ in range(1+target)]
        dp[0][0] = 0 #suppose the outer boundary is painted in a color different from all other houses' colors
        for i in range(1,m+1):
            t = [[inf]*(n+1) for _ in range(1+target)]
            if houses[i-1]==0:
                for j in range(1,target+1):
                    for k in range(1,n+1):
                        t[j][k] = dp[j][k]+cost[i-1][k-1]
                        for l in range(n+1):#previous house's color
                            if l!=k:
                                t[j][k] = min(t[j][k],dp[j-1][l]+cost[i-1][k-1])
            else:
                for j in range(1,target+1):
                    for k in range(1,n+1):
                        if k==houses[i-1]:
                            t[j][k] = dp[j][k]
                            for l in range(n+1):#previous house color
                                if l!=k:
                                    t[j][k] = min(t[j][k],dp[j-1][l])
            dp = t
        res = min(dp[target])
        return res if res<inf else -1