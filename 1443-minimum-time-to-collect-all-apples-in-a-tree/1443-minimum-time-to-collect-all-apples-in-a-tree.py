class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.res = 0
        def dfs(node, par):
            mustVisit = hasApple[node]
            for nei in graph[node]:
                if nei!=par and dfs(nei,node): mustVisit = True
            if mustVisit and node!=0:
                self.res += 2
            return mustVisit
               
        dfs(0,-1)
        return self.res