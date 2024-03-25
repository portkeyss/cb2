class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        x = 0
        s = sum(nums)
        n = len(nums)
        for i in range(n):
            if x*2==s-nums[i]: return i
            x += nums[i]
        return -1