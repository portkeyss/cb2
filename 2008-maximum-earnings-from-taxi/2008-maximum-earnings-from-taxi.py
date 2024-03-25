class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [[0,0]]
        rides.sort(key=lambda x:x[1])
        m = len(rides)
        for a,b,t in rides:
            i = bisect.bisect(dp,[a,inf])-1
            p = dp[i][1]+b-a+t
            if dp[-1][1]<p:
                if dp[-1][0]==b: dp[-1][1]=p
                else: dp.append([b,p])
        return dp[-1][1]