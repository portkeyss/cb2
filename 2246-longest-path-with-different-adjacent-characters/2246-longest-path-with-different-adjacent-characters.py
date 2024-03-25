class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        root = None
        for i,j in enumerate(parent):
            if j==-1: root = i
            else: children[j].append(i)
        
        self.res = 0
        def dfs(node):
            a = b = 0 #longest and second longest downward path starting from any of node's child
            for c in children[node]:
                p = dfs(c)
                if s[c]!=s[node]:
                    if p>=a:
                        a, b = p,a
                    elif p>=b:
                        b = p
            self.res = max(self.res, a+b+1)
            return max(a,b)+1

        dfs(root)
        return self.res