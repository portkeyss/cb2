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
        if x==y: return 0
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
        else:
            self.parent[x]=y
            self.rank[y] += 1
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = [[] for _ in range(4)]
        for t,u,v in edges:
            A[t].append([u,v])
        netEdges = 0
        alice, bob = UnionFind(), UnionFind()
        a, b = 0, 0
        for u,v in A[3]:
            x, y = alice.union(u,v), bob.union(u,v)
            a += x
            b += y
            netEdges += x #note that in this case, x==y
        for u,v in A[1]:
            x = alice.union(u,v)
            a += x
            netEdges += x
        for u,v in A[2]:
            y = bob.union(u,v)
            b += y
            netEdges += y
        if a!= n-1 or b!= n-1: return -1
        return len(edges)-netEdges