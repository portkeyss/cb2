class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        step = 0
        drs = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = [[False]*n for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True
        q = [entrance]
        while q:
            t = []
            for a,b in q:
                for d0,d1 in drs:
                    x,y = a+d0, b+d1
                    if x in [-1,m] or y in [-1,n]: 
                        if [a,b]!=entrance: return step
                        else: continue
                    if visited[x][y] is False and maze[x][y]==".":
                        t.append([x,y])
                        visited[x][y] = True
            step += 1
            q = t
        return -1       