class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums[-1]
        res = 0
        for i in range(n-2,-1,-1):
            segments = ceil(nums[i]/x)
            res += segments-1
            x = nums[i]//segments
        return res