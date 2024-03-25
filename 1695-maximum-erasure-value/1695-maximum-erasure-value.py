class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        windowStart = 0
        num2idx = dict()
        curSum = 0
        for i,num in enumerate(nums):
            if num in num2idx:
                while windowStart<=num2idx[num]:
                    curSum -= nums[windowStart]
                    windowStart += 1
            curSum += num
            res = max(res,curSum)
            num2idx[num] = i
        return res