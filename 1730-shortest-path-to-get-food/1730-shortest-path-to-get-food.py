class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        def startingPoint():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "*":
                        return i,j
        i0,j0 = startingPoint()
        q = []
        q.append((i0,j0))
        step = 0
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            t = []
            for i,j in q:
                for dx,dy in d:
                    x = i+dx
                    y = j+dy
                    if 0<=x<m and 0<=y<n:
                        if grid[x][y]=="#":
                            return step+1
                        elif grid[x][y]=="O":
                            grid[x][y] = "X"
                            t.append((x,y))
            q = t
            step += 1
        return -1