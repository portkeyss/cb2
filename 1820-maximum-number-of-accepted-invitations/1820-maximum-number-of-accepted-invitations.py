class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        graph = defaultdict(lambda:defaultdict(lambda:0))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    graph[i][j+m]=1
        for i in range(m):
            graph[-1][i]=1
        for j in range(n):
            graph[j+m][m+n]=1
            
        def bfs(s,t):
            q = deque()
            q.append(s)
            visited = defaultdict(lambda:False)
            visited[s] = True
            while q:
                u = q.popleft()
                for v,c in graph[u].items():
                    if not visited[v] and c>0:
                        visited[v]=True
                        q.append(v)
                        parent[v] = u
                        if v==t: return True
            return False
        
        parent = defaultdict(lambda:-inf)
        maxflow = 0
        source, sink = -1,m+n
        while bfs(source,sink):
            x = sink
            while x!=source:
                y = parent[x]
                graph[y][x] -= 1
                graph[x][y] += 1
                x = y
            maxflow += 1
        return maxflow