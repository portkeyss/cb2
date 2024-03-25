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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x:x[2])
        uf = UnionFind()
        A = sorted([d,i,a,b,False] for i,(a,b,d) in enumerate(queries))
        j = 0
        for i in range(len(A)):
            while j<len(edgeList) and edgeList[j][2]<A[i][0]:
                uf.union(edgeList[j][0],edgeList[j][1])
                j += 1
            if uf.find(A[i][2])==uf.find(A[i][3]): 
                A[i][4] = True
        res = [False]*len(A)
        for i in range(len(A)):
            res[A[i][1]] = A[i][4]
        return res