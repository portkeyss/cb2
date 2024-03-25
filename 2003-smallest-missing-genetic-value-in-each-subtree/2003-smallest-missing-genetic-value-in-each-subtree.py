class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        res = [1]*n
        p = -1
        for i in range(n):
            if nums[i]==1:
                p = i
                break
        if p==-1: return res
        
        children = [[] for _ in range(n)]
        for ch, par in enumerate(parents):
            if par != -1:
                children[par].append(ch)
            
        visited = set()
        def dfs(node):
            if nums[node] in visited: return
            for ch in children[node]:
                dfs(ch)
            visited.add(nums[node])
            
        missing = 1
        while p!=-1:
            dfs(p)
            while missing in visited:
                missing += 1
            res[p] = missing
            p = parents[p]
        return res