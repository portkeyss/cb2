class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:return -1
        graph = [[] for _ in range(n)]
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False]*n
        islands = 0
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            islands += 1
            q = deque([i])
            while q:
                a = q.popleft()
                for b in graph[a]:
                    if visited[b]:continue
                    visited[b] = True
                    q.append(b)
        return islands-1