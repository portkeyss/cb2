class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        cost = dict()
        visitedNodes = Counter()
        visitedEdges = set()
        
        neighbors = [[] for _ in range(n)]
        for u,v,t in edges:
            neighbors[u].append(v)
            cost[(u,v)] = t
            neighbors[v].append(u)
            cost[(v,u)] = t
            
        def f(u,v,timeleft):
            if timeleft<0: return -inf
            if (u,v) in visitedEdges: return -inf
            visitedEdges.add((u,v))
            x = values[v] if visitedNodes[v]==0 else 0 
            visitedNodes[v] += 1
            q = x if v==0 else -inf
            for w in neighbors[v]:
                q = max(q,x+f(v,w,timeleft-cost[(v,w)]))
            visitedNodes[v] -= 1
            visitedEdges.remove((u,v))
            return q
            
        return f(-1,0,maxTime)