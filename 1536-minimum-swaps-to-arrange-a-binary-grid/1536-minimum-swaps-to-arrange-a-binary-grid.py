class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        A = []
        for i in range(n):
            j = n-1
            while j>=0 and grid[i][j]==0:
                j -= 1
            A.append(n-1-j)
        #greedy
        res = 0
        for i in range(n):
            k = i
            while k<n and A[k]<n-1-i: k+=1
            if k==n: return -1
            if k==i: continue
            x = A[k]
            A[i+1:k+1] = A[i:k]
            A[i] = x
            res += k-i
        return res