class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = [set() for _ in range(n)]
        for road in roads:
            a, b = road[0], road[1]
            edges[a].add(b)
            edges[b].add(a)
        res = 0
        for c1 in range(n-1):
            for c2 in range(c1+1, n):
                res = max(res, len(edges[c1])+len(edges[c2])-(1 if c2 in edges[c1] else 0))
        return res