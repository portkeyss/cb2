class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9+7
        s = [["r"],["g"],["b"]]
        for i in range(1,m):
            t = []
            for x in "rgb":
                for a in s:
                    if a[-1]!=x:
                        t.append(a+[x])
            s = t
        s = ["".join(l) for l in s]
        nei = defaultdict(list)
        for x in s:
            for y in s:
                if all(a!=b for a,b in zip(x,y)):
                    nei[x].append(y)
        
        res = 0
        states = [state for state in s if state[0]=="r"] #due to symmetry, this step cut runtime by 2/3
        A = Counter()
        for x in states:
            A[x]=1
            
        for j in range(1,n):
            B = Counter()
            for x in s:
                for y in nei[x]:
                    B[x] = (B[x]+A[y])%mod          
            A = B
        
        res = 0
        for v in A.values():
            res = (res+v)%mod
        res = (3*res)%mod
        return res