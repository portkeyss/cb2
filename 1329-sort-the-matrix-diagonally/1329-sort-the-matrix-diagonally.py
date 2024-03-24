class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        A = [[] for  _ in range(m+n+1)]
        for i in range(m):
            for j in range(n):
                heapq.heappush(A[i-j+n], mat[i][j])
        res = [[0]*n for _ in range(m)]
        for k,hq in enumerate(A):
            (r,c) = (k-n, 0) if k-n >= 0 else (0,n-k)
            while hq:
                res[r][c] = heapq.heappop(hq)
                r += 1
                c += 1
        return res      