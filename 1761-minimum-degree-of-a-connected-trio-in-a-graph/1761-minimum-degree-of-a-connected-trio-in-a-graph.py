class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [set() for _ in range(n+1)]
        degree = [0]*(n+1)
        for edge in edges:
            edge.sort()
            a,b = edge[0], edge[1]
            neighbors[a].add(b)
            degree[a] += 1
            degree[b] += 1
        res = inf
        for a,b in edges:
            for c in neighbors[b]:
                if c in neighbors[a]:
                    res = min(res, degree[a]+degree[b]+degree[c]-6)
        return res if res<inf else -1