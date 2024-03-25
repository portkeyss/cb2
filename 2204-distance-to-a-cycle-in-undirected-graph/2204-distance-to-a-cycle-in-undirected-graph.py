class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        visited = [0]*n
        stack = []
        self.cycle = None
        def dfs(i):
            stack.append(i)
            visited[i] = 1
            for nei in graph[i]:
                if visited[nei]==0:
                    dfs(nei)
                    if self.cycle: break
                elif len(stack)>2 and nei!=stack[-2]:
                    k = len(stack)-1
                    while stack[k]!=nei: k -= 1
                    self.cycle = stack[k:]
                    break
            stack.pop()
            
        dfs(0)
        
        dist = [inf]*n
        q = deque()
        for node in self.cycle:
            q.append(node)
            dist[node] = 0
        while q:
            x = q.popleft()
            for y in graph[x]:
                if dist[y]<inf: continue
                q.append(y)
                dist[y] = dist[x]+1
        return dist    