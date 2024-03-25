class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        A = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    A[i][j] = 0
                else:
                    A[i][j] = 1+A[i-1][j] if i>0 else 1
        res = 0
        for i in range(m):
            A[i].sort(reverse=True)
            for j in range(n):
                if A[i][j]==0: break
                res = max(res, A[i][j]*(j+1))
        return res