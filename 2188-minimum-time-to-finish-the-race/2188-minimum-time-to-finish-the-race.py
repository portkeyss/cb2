class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        f_min, r_min = min(f for f,_ in tires), min(r for _,r in tires)
        #f_min*r_min^(N-1)<changeTime+f_min, otherwise, the tire can be surely replaced by the new tire with min f, reducing the total time
        N = ceil(log((changeTime+f_min)/f_min, r_min))+1
        
        minTimeForLaps = [inf]*(1+N)
        for f,r in tires:
            t = 0
            for x in range(1,N+1):
                t += f*r**(x-1)
                minTimeForLaps[x] = min(minTimeForLaps[x], t)

        dp = [inf]*(1+numLaps)
        dp[0] = 0
        for lap in range(1,numLaps+1):
            for x in range(1,min(N,lap)+1):
                dp[lap] = min(dp[lap],dp[lap-x]+changeTime+minTimeForLaps[x])

        return dp[numLaps]-changeTime