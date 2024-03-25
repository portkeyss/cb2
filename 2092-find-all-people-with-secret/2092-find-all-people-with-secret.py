class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        class UnionFind:
            def __init__(self):
                self.parent = [-1]*n
                self.rank = [0]*n

            def find(self,a):
                if self.parent[a]==-1: return a
                self.parent[a] = self.find(self.parent[a])
                return self.parent[a]

            def union(self,a,b):
                pa = self.find(a)
                pb = self.find(b)
                if pa==pb: return
                if self.rank[pa]<self.rank[pb]:
                    self.parent[pa]=pb
                elif self.rank[pa]>self.rank[pb]:
                    self.parent[pb]=pa
                else:
                    self.parent[pb]=pa
                    self.rank[pa] += 1

            def reset(self,a):
                self.parent[a] = -1
                self.rank[a] = 0
        
        uf = UnionFind()
        uf.union(0,firstPerson)
        A = defaultdict(list)
        for x,y,t in meetings:
            A[t].append([x,y])
            
        T = sorted(list(A.keys()))
        for t in T:
            for x,y in A[t]:
                uf.union(x,y)
            anc = uf.find(0)
            for x,y in A[t]:
                if uf.find(x)!=anc: uf.reset(x)
                if uf.find(y)!=anc: uf.reset(y)
                    
        res = []
        anc = uf.find(0)
        for i in range(n):
            if uf.find(i)==anc: res.append(i)
        return res