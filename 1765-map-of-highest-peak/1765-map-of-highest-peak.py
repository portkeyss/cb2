class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        waters = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]: waters.append([i,j])
        A = [[-1]*n for _ in range(m)]
        for i,j in waters:
            A[i][j] = 0
            
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = waters
        height = 0
        while q:
            t = []
            for c,r in q:
                for dc,dr in directions:
                    c1, r1 = c+dc, r+dr
                    if 0<=c1<m and 0<=r1<n and A[c1][r1]==-1:
                        A[c1][r1] = height+1
                        t.append([c1,r1])
            q = t
            height += 1
        return A