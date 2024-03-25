class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        neis = [[] for _ in range(n+1)]
        for a,b in edges:
            neis[a].append(b)
            neis[b].append(a)

        self.visited = set()
        def f(x):
            group = [x]
            q = deque([x])
            while q:
                y = q.popleft()
                for z in neis[y]:
                    if z not in self.visited:
                        q.append(z)
                        group.append(z)
                        self.visited.add(z)
            h = 1
            for w in group:
                q = deque()
                d = dict()
                q.append(w)
                d[w] = 1
                while q:
                    y = q.popleft()
                    for z in neis[y]:
                        if z not in d:
                            q.append(z)
                            d[z] = d[y]+1
                            h = max(h,d[z])
                        elif abs(d[z]-d[y])!=1:
                            return -1
            return h

        res = 0
        for i in range(1,n+1):
            if i in self.visited: continue
            a = f(i)
            if a==-1: return -1
            res += a
        return res