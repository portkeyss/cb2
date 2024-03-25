class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = []
        q.append((start[0], start[1]))
        res = []
        if pricing[0]<=grid[start[0]][start[1]]<=pricing[1]:
            res.append([start[0],start[1]])
            k -= 1
        grid[start[0]][start[1]] *= -1
        while k>0 and q:
            t = []
            pq = []
            for r,c in q:
                for d0, d1 in directions:
                    x, y = r+d0, c+d1
                    if 0<=x<m and 0<=y<n and grid[x][y]>0:
                        t.append((x,y))
                        if pricing[0]<=grid[x][y]<=pricing[1]:
                            heapq.heappush(pq, (grid[x][y], x, y))
                        grid[x][y] *= -1
            while pq and k>0:
                _, a, b = heapq.heappop(pq)
                res.append([a,b])
                k -= 1
            q = t
        return res           