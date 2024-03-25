from heapq import heappush,heappop
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        maxHq = []
        x = 0
        minNSum = [inf]*(2*n)
        for i in range(2*n):
            heappush(maxHq,-nums[i])
            x += nums[i]
            if len(maxHq)>n:
                x -= -heappop(maxHq)
            minNSum[i] = x if len(maxHq)==n else inf
        minHq = []
        y = 0
        res = inf
        for i in range(3*n-1,n-1,-1):
            heappush(minHq,nums[i])
            y += nums[i]
            if len(minHq)>n:
                y -= heappop(minHq)
            if len(minHq)==n:
                res = min(res,minNSum[i-1]-y)
        return res