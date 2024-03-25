class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        A = [0]*(n-1)
        for i in range(n-1):
            A[i] = weights[i]+weights[i+1]
        
        A.sort()
        res = 0
        for i in range(k-1):
            res += A[n-2-i]-A[i]
        return res