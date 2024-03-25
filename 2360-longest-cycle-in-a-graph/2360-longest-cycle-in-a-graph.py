class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0]*n
        for j in edges:
            if j>-1: indegree[j] += 1
        
        A = [i for i in range(n) if indegree[i]==0]
        q = deque()
        visited = [False]*n
        for i in A:
            q.append(i)
            visited[i] = True
        while q:
            x = q.popleft()
            y = edges[x] 
            if y>-1:
                indegree[y] -= 1
                if indegree[y]==0:
                    q.append(y)
                    visited[y] = True
        
        res = 0
        for i in range(n):
            if visited[i]: continue
            visited[i] = True
            l = 1
            j = edges[i]
            while j!=i:
                visited[j] = True
                l += 1
                j = edges[j]
            res = max(res,l)
        return res if res>0 else -1