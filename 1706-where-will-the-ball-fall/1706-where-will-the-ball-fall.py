class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for j in range(n):
            k = j
            for i in range(m):
                if grid[i][k] == -1:
                    if k == 0 or grid[i][k-1] == 1:
                        res.append(-1)
                        break
                    elif grid[i][k-1] == -1:
                        k -= 1
                else:
                    if k == n-1 or grid[i][k+1] == -1:
                        res.append(-1)
                        break
                    elif grid[i][k+1] == 1:
                        k += 1
            if len(res) == j:
                res.append(k)
                        
        return res           