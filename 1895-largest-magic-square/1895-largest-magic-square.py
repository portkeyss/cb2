class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        A = [[0]*(n+1) for _ in range(m+1)]
        B = [[0]*(n+1) for _ in range(m+1)]
        C = [[0]*(n+1) for _ in range(m+1)]
        D = [[0]*(n+2) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                    A[i][j] = A[i][j-1]+grid[i-1][j-1]
                    B[i][j] = B[i-1][j]+grid[i-1][j-1]
                    C[i][j] = C[i-1][j-1]+grid[i-1][j-1]
        for i in range(1,m+1):
            for j in range(n,0,-1):
                D[i][j] = D[i-1][j+1]+grid[i-1][j-1]
        k = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                for p in range(k+1,min(i,j)+1):
                    if (C[i][j]-C[i-p][j-p])!=(D[i][j-p+1]-D[i-p][j+1]):
                        continue
                    a = C[i][j]-C[i-p][j-p]
                    flag = True
                    for r in range(i-p+1,i+1):
                        if A[r][j]-A[r][j-p] != a:
                            flag = False
                            break
                    if flag is False:
                        continue
                    for c in range(j-p+1,j+1):
                        if B[i][c]-B[i-p][c] != a:
                            flag = False
                            break
                    if flag:
                        k = p              
        return k