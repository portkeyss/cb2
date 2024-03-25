class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start==end: return True
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set([start])
        q = deque([start])
        while q:
            z = q.popleft()
            for w in graph[z]:
                if w not in visited:
                    q.append(w)
                    visited.add(w)
                    if w==end: return True
        return False