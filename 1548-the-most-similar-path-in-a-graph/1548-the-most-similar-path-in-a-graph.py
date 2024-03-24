class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        m = len(targetPath)
        dp = [[names[p]!=targetPath[0] for p in range(n)]]+[[math.inf]*n for _ in range(m-1)]
        prev = [[-1]*n for _ in range(m)]
        for i in range(1,m):
            for v in range(n):
                editCost = (names[v]!=targetPath[i])
                for u in graph[v]:
                    if dp[i-1][u]+editCost < dp[i][v]:
                        dp[i][v] = dp[i-1][u]+editCost
                        prev[i][v] = u
        w = 0
        for v in range(1,n):
            if dp[-1][v]<dp[-1][w]:
                w = v
        path = [w]
        
        for i in range(m-1,0,-1):
            path.append(prev[i][path[-1]])
        return path[::-1]