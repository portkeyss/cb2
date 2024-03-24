class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        neighbors = [[] for _ in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        res = [0]*n   
        def dfs(node, par):
            ctr = Counter()
            for v in neighbors[node]:
                if v != par:
                    ctr += dfs(v,node)
            ctr[labels[node]] += 1
            res[node] = ctr[labels[node]]
            return ctr
        dfs(0, None)
        return res