class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        F = [1,1]
        while F[-1]+F[-2]<=k:
            F.append(F[-1]+F[-2])
        S = set(F)
        n = len(F)
        #@lru_cache(None)
        def g(num, i):
            if num in S: return 1
            if num < 1: return inf
            for j in range(i,-1,-1):
                a = 1+g(num-F[j], j)
                if a<inf: return a
            return inf
        return g(k, n-1)