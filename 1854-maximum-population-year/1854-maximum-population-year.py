class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        start, end = min(x[0] for x in logs), max(x[1] for x in logs)
        flow = [0]*(end+1)
        for b,d in logs:
            flow[b]+=1
            flow[d]-=1
        ans = (0,0)
        population = 0
        for y in range(start, end+1):
            population += flow[y]
            if population > ans[1]:
                ans = (y, population)
        return ans[0]