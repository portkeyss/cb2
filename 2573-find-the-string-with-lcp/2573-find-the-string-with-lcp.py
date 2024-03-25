class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        A = [-1]*n
        x = 0
        for i in range(n):
            if A[i]>-1: continue
            for j in range(i,n):
                if lcp[i][j]>0: A[j] = x
            x += 1
            if x>26: return ""
        for i in range(n):
            for j in range(n):
                l = lcp[i+1][j+1] if i<n-1 and j<n-1 else 0
                l = l+1 if A[i]==A[j] else 0
                if l != lcp[i][j]: return ""
        return "".join([chr(x+ord("a")) for x in A])