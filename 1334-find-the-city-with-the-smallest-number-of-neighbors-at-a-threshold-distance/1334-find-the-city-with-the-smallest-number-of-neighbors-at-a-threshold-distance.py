class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for a,b,c in edges:
            graph[a].append([b,c])
            graph[b].append([a,c])
        res = [inf,-1]
        for i in range(n):
            dist = [inf]*n
            hq = [(0,i)]
            dist[i] = 0
            while hq:
                d,j = heapq.heappop(hq)
                if dist[j]<d: continue
                for k,w in graph[j]:
                    if d+w<dist[k] and d+w<=distanceThreshold:
                        dist[k]=d+w
                        heapq.heappush(hq,(dist[k],k))
            cities = sum(d<inf for d in dist)
            if cities<=res[0]:
                res = [cities,i]
        return res[1]