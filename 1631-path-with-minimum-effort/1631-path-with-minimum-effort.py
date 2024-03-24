class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        if m == 0 and n == 0:
            return 0
        q = deque()
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        q.append((0,0))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            (r,c) = q.popleft()
            for d in directions:
                r1, c1 = r+d[0], c+d[1]
                if 0 <= r1 < m and 0 <= c1 < n and dist[r1][c1] > max(dist[r][c], abs(heights[r1][c1] - heights[r][c])):
                    q.append((r1,c1))
                    dist[r1][c1] = max(dist[r][c], abs(heights[r1][c1] - heights[r][c]))
        return dist[m-1][n-1]