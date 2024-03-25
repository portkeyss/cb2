class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        #one only needs to try two cases, row 0 flip even times, or row 1 flip odd times
        def f(x): #x=0 refers to even number of flips, x=1 odd flips
            A = [None]*m
            B = [None]*n
            A[0] = x
            for j in range(n):
                if A[0]==0:
                    B[j] = 0 if grid[0][j]==0 else 1
                else:
                    B[j] = 1 if grid[0][j]==0 else 0
            for i in range(1,m):
                if B[0]==0:
                    A[i] = 0 if grid[i][0]==0 else 1
                else:
                    A[i] = 1 if grid[i][0]==0 else 0 
                for j in range(1,n):
                    if (A[i]+B[j])%2==0:  
                        if grid[i][j]==1:
                            return False
                    else:
                        if grid[i][j]==0:
                            return False
            return True  
                        
        return f(0) or f(1)