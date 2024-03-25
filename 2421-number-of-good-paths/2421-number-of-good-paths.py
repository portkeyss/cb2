class UnionFind:
    def __init__(self):
        self.rank = defaultdict(lambda:0)
        self.parent = dict()
    
    def find(self,x):
        if x not in self.parent: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y: return
        if self.rank[x]>self.rank[y]:
            self.parent[y] = x
        elif self.rank[x]<self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        neis = [[] for _ in range(n)]
        for a,b in edges:
            neis[a].append(b)
            neis[b].append(a)

        v2i = defaultdict(list)
        for i,v in enumerate(vals):
            v2i[v].append(i)
        
        vs = sorted(v2i.keys())
        res = 0
        uf = UnionFind()
        for v in vs:
            for i in v2i[v]:
                for j in neis[i]:
                    if vals[i]>=vals[j]:
                        uf.union(i,j)
            A = Counter()
            for i in v2i[v]:
                A[uf.find(i)] += 1
            for x in A.values():
                res += x*(x+1)//2
        return res