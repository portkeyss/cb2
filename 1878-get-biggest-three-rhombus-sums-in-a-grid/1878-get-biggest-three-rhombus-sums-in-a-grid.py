class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        A = [[0]*(n+1) for _ in range(m+1)]
        B = [[0]*(n+2) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                A[i+1][j+1] = A[i][j]+grid[i][j]
            for j in range(n-1,-1,-1):
                B[i+1][j+1] = B[i][j+2]+grid[i][j]
        
        def edge(x,y,l,dx,dy): #sum on edge starting from (x,y)(exclusive), ending at(x+l*dx,y+l*dy)(inclusive)
            #all the +1 modifies index convention from 0 based to 1 based to suit A and B convention
            if dx==1 and dy==1:
                return A[x+l+1][y+l+1]-A[x+1][y+1]
            if dx==-1 and dy==1:
                return B[x-1+1][y+1+1]-B[x-l-1+1][y+l+1+1]
            if dx==-1 and dy==-1:
                return A[x-1+1][y-1+1]-A[x-l-1+1][y-l-1+1]
            if dx==1 and dy==-1:
                return B[x+l+1][y-l+1]-B[x+1][y+1]
        
        ans = set([grid[i][j] for i in range(m) for j in range(n)])
        for i in range(m):
            for j in range(n):
                l = 1
                while j+2*l<n and i+l<m and i-l>=0:
                    a = edge(i,j,l,1,1) + edge(i+l,j+l,l, -1, 1) + edge(i,j+2*l, l, -1, -1) + edge(i-l,j+l,l,1,-1) #all 4 edges added up, note that all end points must be counted only once
                    ans.add(a)
                    l += 1
        ans = list(ans)
        ans.sort(reverse=True)
        return ans[:3]