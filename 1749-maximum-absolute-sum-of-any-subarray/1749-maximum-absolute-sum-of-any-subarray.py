class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx = -inf
        mi = inf
        curMax = 0
        curMin = 0
        for n in nums:
            curMax += n
            mx = max(mx, curMax)
            curMin += n
            mi = min(mi, curMin)
            if curMax < 0:
                curMax = 0
            if curMin > 0:
                curMin = 0
        return max(abs(mx), abs(mi))