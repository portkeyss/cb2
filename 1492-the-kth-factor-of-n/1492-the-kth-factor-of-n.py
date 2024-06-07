class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        p = floor(sqrt(n))
        A = []
        for i in range(1,p+1):
            if n%i==0:
                A.append(i)
                if len(A)==k: return i
        if p*p==n:
            if 2*len(A)-1<k: return -1
            else:
                return n//A[-(k-len(A)+1)]
        else:
            if 2*len(A)<k: return -1
            else:
                return n//A[-(k-len(A))]