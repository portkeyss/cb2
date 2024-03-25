class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        obs = obstacles
        dp = [math.inf,0,math.inf]
        for i in range(len(obs)):
            lanes = set([1,2,3])
            j = obs[i]
            lanes.discard(j)
            lanes = list(lanes)
            if j > 0:
                dp[j-1] = math.inf
            pairs = None
            if j==0:
                pairs = [[1,2],[1,3],[2,3]]
            elif j==1:
                pairs = [[2,3]]
            elif j==2:
                pairs = [[1,3]]
            else:
                pairs = [[1,2]]
            for k,l in pairs:
                dp[k-1] = min(dp[k-1],1+dp[l-1])
                dp[l-1] = min(dp[l-1],1+dp[k-1])
        return min(dp)   