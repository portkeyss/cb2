class UnionFind:
    def __init__(self,sz):
        self.parent = dict()
        self.rank = Counter()
        self.size = sz
    
    def find(self,x):
        if x not in self.parent: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y: return False
        if self.rank[x]<self.rank[y]:
            self.parent[x] = y
        elif self.rank[x]>self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1
        self.size -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        indices = list(range(m))
        indices.sort(key=lambda x:edges[x][2])
        minWeight = 0
        uf = UnionFind(n)
        for i in indices:
            if uf.union(edges[i][0],edges[i][1]): minWeight += edges[i][2]
        
        critical = []
        pseudo = []
        for i in range(m):
            weight_drop = 0
            uf_drop = UnionFind(n)
            for j in indices:
                if j!=i and uf_drop.union(edges[j][0],edges[j][1]): weight_drop += edges[j][2]
            if uf_drop.size>1 or weight_drop>minWeight:
                critical.append(i)
                continue
            weight_enforce = 0
            uf_enforce = UnionFind(n)
            uf_enforce.union(edges[i][0],edges[i][1])
            weight_enforce += edges[i][2]
            for j in indices:
                if uf_enforce.union(edges[j][0],edges[j][1]): weight_enforce += edges[j][2]
            if weight_enforce==minWeight: pseudo.append(i)
        return [critical,pseudo]