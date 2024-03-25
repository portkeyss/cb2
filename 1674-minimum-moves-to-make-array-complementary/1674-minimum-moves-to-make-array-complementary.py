class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = Counter()
        n = len(nums)
        for i in range(n//2):
            a, b = sorted((nums[i], nums[n-1-i]))
            delta[2] += 2
            delta[a+1] -= 1
            delta[a+b] -= 1
            delta[a+b+1] += 1
            delta[limit+b+1] += 1
        
        res = math.inf
        moves = 0
        for t in range(2, 2*limit+1):
            moves += delta[t]
            res = min(res, moves)
        return res