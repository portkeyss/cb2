class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a,b in connections:
            graph[a].add((b,True))
            graph[b].add((a,False))
        res = 0    
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            for m,d in graph[node]:
                if d:
                    res += 1
                graph[m].remove((node,not d))
                q.append(m)
            graph.pop(node)
        return res