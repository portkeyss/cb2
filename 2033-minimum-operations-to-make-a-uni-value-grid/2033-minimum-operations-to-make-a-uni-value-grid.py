class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        counter = Counter(grid[i][j] for i in range(m) for j in range(n))
        nums = sorted(list(counter.keys()))
        if len(nums)==1: return 0
        moves = 0
        for a in nums[1:]:
            if (a-nums[0])%x==0:
                moves += counter[a]*((a-nums[0])//x)
            else:
                return -1
        l = counter[nums[0]] #count of less than current number
        res = moves
        for u in range(nums[0]+x, nums[-1]+x,x):  
            moves += (2*l-m*n)
            res = min(res, moves)
            l += counter[u]
        return res