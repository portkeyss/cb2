class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = Counter()

    def find(self,x):
        if x not in self.parent: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y: return
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
        else:
            self.parent[x]=y
            self.rank[y] += 1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        cells = [tuple(x) for x in cells]
        A = set()
        for i in range(1,row+1):
            for j in range(1,col+1):
                A.add((i,j))
        source, sink = (-100,-100), (-200,-200)
        A.add(source)
        A.add(sink)
        for x in cells: A.remove(x)
        uf = UnionFind()
        ds = [(1,0),(0,1),(-1,0),(0,-1)]
        for r,c in A:
            for dr,dc in ds:
                r1, c1 = r+dr, c+dc
                if (r1,c1) in A: uf.union((r,c),(r1,c1))
        for j in range(1,1+col):
            uf.union((1,j),source)
            uf.union((row,j),sink)
        if uf.find(source)==uf.find(sink): return n
        for t in range(n-1,-1,-1):
            r,c = cells[t][0], cells[t][1]
            A.add((r,c))
            for dr,dc in ds:
                r1, c1 = r+dr, c+dc
                if (r1,c1) in A: uf.union((r,c),(r1,c1))
            if uf.find(source)==uf.find(sink): return t