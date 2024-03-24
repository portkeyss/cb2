class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0]*n for _ in range(m)]
        s = [sum(mat[i][:K+1]) for i in range(m)]
        
        ans[0][0] = sum(s[:K+1])
        for i in range(1,m):
            ans[i][0] = ans[i-1][0] - (s[i-K-1] if i-K-1 >= 0 else 0) + (s[i+K] if i+K < m else 0)
        
        p = [[0]*n for _ in range(m)]
        for j in range(n):
            p[0][j] = sum(mat[i][j] for i in range(min(m,K+1)))
        for i in range(1,m):
            for j in range(n):
                p[i][j] = p[i-1][j] - (mat[i-1-K][j] if i-1-K >= 0 else 0) +(mat[i+K][j] if i+K < m else 0)
        
        for i in range(m):
            for j in range(1,n):
                ans[i][j] = ans[i][j-1] - (p[i][j-1-K] if j-1-K >= 0 else 0) + (p[i][j+K] if j+K < n else 0)
        
        return ans