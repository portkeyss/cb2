from random import randrange
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def generateLargePrime(low, high):
            def millerRabinTest(cand, trials=50):
                def witness(a):   
                    x = pow(a,d,cand)
                    if x==1 or x==cand-1: return False
                    for _ in range(s):
                        x = pow(x,2,cand)
                        if x==cand-1: return False
                    return True
                
                if cand%2==0: return True
                s, d = 0, cand-1
                while d%2==0:
                    d>>=1
                    s += 1   
                for _ in range(trials):
                    if witness(randrange(1,cand-1)): return False
                return True
            
            return next(num for num in iter(lambda: randrange(low,high),None) if millerRabinTest(num))
                
        mod = generateLargePrime(1e17, 1e18)
        base = n
        l = 0
        r = min(len(p) for p in paths)
        while l<r:
            m = (l+r+1)//2
            A = set()
            for i in range(len(paths)):
                h = 0
                b = 1
                B = set()
                for j in range(len(paths[i])):
                    h = (h*base+paths[i][j])%mod
                    if j>=m: 
                        h = (h-paths[i][j-m]*b)%mod
                    else:
                        b = (b*base)%mod
                    if j>=m-1:
                        if i==0:
                            B.add(h)
                        elif h in A:
                            B.add(h) 
                A = B
                if not A: break
            if A: l = m
            else: r = m-1
        return r