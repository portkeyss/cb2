class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        def getPrefix(mat):
            a, b = len(mat), len(mat[0])
            A = [[0]*(b+1) for _ in range(a+1)]
            prefix = [[0]*(b+1) for _ in range(a+1)]
            for i in range(a):
                for j in range(b):
                    A[i+1][j+1] = A[i][j+1]+mat[i][j]
                    prefix[i+1][j+1] = prefix[i+1][j]+A[i+1][j+1]
            return prefix
        
        m, n = len(grid), len(grid[0])
        pre = getPrefix(grid)
        stampBR = [[0]*n for _ in range(m)] #bottom right corner of a legitimate stamp
        h,w = stampHeight, stampWidth
        for i in range(h-1,m):
            for j in range(w-1,n):
                if pre[i+1][j+1]-pre[i+1-h][j+1]-pre[i+1][j+1-w]+pre[i+1-h][j+1-w]==0:
                    stampBR[i][j] = 1
        
        pre2 = getPrefix(stampBR)
        for i in range(m):
            for j in range(n):
                p = min(m-1,i+h-1)
                q = min(n-1,j+w-1)
                if grid[i][j]==0 and (pre2[p+1][q+1]-pre2[i][q+1]-pre2[p+1][j]+pre2[i][j]==0): 
                    return False
        return True