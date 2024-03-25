class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = inf
        res = -inf
        for num in nums:
            if num>mi:
                res = max(res, num-mi)
            mi = min(mi, num)
        return res if res>0 else -1