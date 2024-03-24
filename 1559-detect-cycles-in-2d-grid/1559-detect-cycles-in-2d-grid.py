class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c, prevR,prevC):
            grid[r][c] = grid[r][c].upper()
            for x,y in directions:
                if 0<=r+x<m and 0<=c+y<n:
                    if grid[r+x][c+y]==grid[r][c]: #already Upper case,i.e.,visited
                        if r+x!=prevR and c+y!=prevC: return True
                    elif grid[r+x][c+y]==grid[r][c].lower():
                        if dfs(r+x,c+y,r,c): return True
            return False
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower() and dfs(i,j, None,None):
                    return True
        return False